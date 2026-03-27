"""Static analysis: AST visitor, role determination, and public analyze()."""

import ast

from prettytable import PrettyTable, TableStyle

from .constants import (
    CONTAINER,
    CONTAINER_METHODS,
    FIXED_VALUE,
    GATHERER,
    LAZY_VALUE,
    LOG,
    MOST_RECENT,
    MOST_WANTED,
    ONE_WAY_FLAG,
    ORGANIZER,
    ORGANIZER_METHODS,
    STEPPER,
    TEMPORARY,
    TOGGLE,
    UNKNOWN,
    _LOG_METHODS,
    _SENTINEL_CONSTANTS,
)
from .varinfo import VarInfo


# -- AST helpers ----------------------------------------------------------------


def _names_in(node: ast.expr) -> set[str]:
    """All variable names referenced anywhere inside node."""
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def _only_self_and_constants(name: str, node: ast.expr) -> bool:
    """True if node references only 'name' itself and literal constants."""
    for child in ast.walk(node):
        if isinstance(child, ast.Name) and child.id != name:
            return False
    return True


def _is_toggle(name: str, value: ast.expr) -> bool:
    """True if value encodes a two-value cycle over 'name'.

    Recognised patterns:
      not name          (boolean flip)
      C - name          (e.g. 1 - side, 0 - flag)
    Augmented x ^= 1 is handled separately in visit_AugAssign.
    """
    if (
        isinstance(value, ast.UnaryOp)
        and isinstance(value.op, ast.Not)
        and isinstance(value.operand, ast.Name)
        and value.operand.id == name
    ):
        return True
    if (
        isinstance(value, ast.BinOp)
        and isinstance(value.op, ast.Sub)
        and isinstance(value.left, ast.Constant)
        and isinstance(value.right, ast.Name)
        and value.right.id == name
    ):
        return True
    return False


def _is_sentinel(node: ast.expr) -> bool:
    """True if node is a recognised sentinel literal: None, -1, or ''."""
    if isinstance(node, ast.Constant):
        return node.value in _SENTINEL_CONSTANTS
    # -1 in source is parsed as UnaryOp(USub, Constant(1)), not Constant(-1)
    return (
        isinstance(node, ast.UnaryOp)
        and isinstance(node.op, ast.USub)
        and isinstance(node.operand, ast.Constant)
        and node.operand.value == 1
    )


# -- AST visitor ----------------------------------------------------------------


class RoleCollector(ast.NodeVisitor):
    """Walk the AST and populate a VarInfo for every assigned variable."""

    def __init__(self) -> None:
        self._scope: list[str] = ["module"]
        self._loop_depth: int = 0
        self._cond_depth: int = 0  # if-nesting depth while inside a loop
        self._any_cond_depth: int = 0  # if-nesting depth anywhere
        self.vars: dict[tuple[str, str], VarInfo] = {}

    def _scope_str(self) -> str:
        return ".".join(self._scope)

    def _get(self, name: str) -> VarInfo:
        key = (name, self._scope_str())
        if key not in self.vars:
            self.vars[key] = VarInfo(name=name, scope=self._scope_str())
        return self.vars[key]

    # -- Scope management -------------------------------------------------------

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._scope.append(node.name)
        args = (
            node.args.posonlyargs
            + node.args.args
            + node.args.kwonlyargs
            + ([node.args.vararg] if node.args.vararg else [])
            + ([node.args.kwarg] if node.args.kwarg else [])
        )
        for arg in args:
            v = self._get(arg.arg)
            v.is_parameter = True
            v.total_assigns += 1
            if v.first_line == 0:
                v.first_line = node.lineno
        self.generic_visit(node)
        self._scope.pop()

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self._scope.append(node.name)
        self.generic_visit(node)
        self._scope.pop()

    # -- Loop and conditional depth tracking ------------------------------------

    def visit_For(self, node: ast.For) -> None:
        self._record_for_target(node)
        self.visit(node.iter)  # iterable is evaluated outside the loop
        self._loop_depth += 1
        for child in node.body + node.orelse:
            self.visit(child)
        self._loop_depth -= 1

    def _record_for_target(self, node: ast.For) -> None:
        def _walk(t: ast.expr) -> None:
            if isinstance(t, ast.Name):
                v = self._get(t.id)
                v.for_loop_target = True
                v.total_assigns += 1
                v.loop_assigns += 1
                if v.first_line == 0:
                    v.first_line = node.lineno
            elif isinstance(t, (ast.Tuple, ast.List)):
                for elt in t.elts:
                    _walk(elt)

        _walk(node.target)

    def visit_While(self, node: ast.While) -> None:
        self._loop_depth += 1
        self.generic_visit(node)
        self._loop_depth -= 1

    def visit_If(self, node: ast.If) -> None:
        self._any_cond_depth += 1
        if self._loop_depth > 0:
            self._cond_depth += 1
            self.generic_visit(node)
            self._cond_depth -= 1
        else:
            self.generic_visit(node)
        self._any_cond_depth -= 1

    # -- Assignment recording ---------------------------------------------------

    def _record(self, name: str, value: ast.expr, lineno: int) -> None:
        """Record a regular (non-augmented) assignment to a plain Name."""
        v = self._get(name)
        v.total_assigns += 1
        if v.first_line == 0:
            v.first_line = lineno
        if self._loop_depth > 0:
            v.loop_assigns += 1
        if self._cond_depth > 0:
            v.cond_loop_assigns += 1
        if self._any_cond_depth > 0:
            v.any_cond_assigns += 1

        # Detect toggle before general self-ref so x = not x isn't counted twice
        if _is_toggle(name, value):
            v.toggle_pattern += 1
        elif name in _names_in(value):
            if _only_self_and_constants(name, value):
                v.self_ref_const += 1
            else:
                v.self_ref_var += 1

        # Sentinel assignment outside a loop → candidate lazy-value initialisation
        if _is_sentinel(value) and self._loop_depth == 0:
            v.sentinel_out_assigns += 1

        # Boolean literals for one-way flag detection
        if isinstance(value, ast.Constant):
            if value.value is True:
                if self._loop_depth > 0:
                    v.bool_true_in_loop += 1
                else:
                    v.bool_true_out_loop += 1
            elif value.value is False:
                if self._loop_depth > 0:
                    v.bool_false_in_loop += 1
                else:
                    v.bool_false_out_loop += 1

    def _record_target(self, target: ast.expr, value: ast.expr, lineno: int) -> None:
        """Recursively record assignments only to Name nodes that are direct targets.

        Subscript (arr[i] = x) and Attribute (obj.attr = x) targets are skipped:
        the object/container is not being rebound, only mutated.
        """
        if isinstance(target, ast.Name):
            self._record(target.id, value, lineno)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for elt in target.elts:
                self._record_target(elt, value, lineno)
        elif isinstance(target, ast.Starred):
            self._record_target(target.value, value, lineno)

    def visit_Assign(self, node: ast.Assign) -> None:
        # Detect tuple swap: a, b = b, a
        lhs, rhs = node.targets[0], node.value
        if isinstance(lhs, (ast.Tuple, ast.List)) and isinstance(
            rhs, (ast.Tuple, ast.List)
        ):
            lhs_names = {e.id for e in lhs.elts if isinstance(e, ast.Name)}
            if lhs_names and lhs_names == _names_in(rhs):
                for n in lhs_names:
                    self._get(n).in_swap = True

        for target in node.targets:
            self._record_target(target, rhs, node.lineno)
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        if isinstance(node.target, ast.Name):
            name = node.target.id
            v = self._get(name)
            v.total_assigns += 1
            v.aug_assigns += 1
            if v.first_line == 0:
                v.first_line = node.lineno
            if self._loop_depth > 0:
                v.loop_assigns += 1
            if self._cond_depth > 0:
                v.cond_loop_assigns += 1
            if self._any_cond_depth > 0:
                v.any_cond_assigns += 1
            # x ^= 1 is a classic numeric toggle; don't count as aug_by_const
            if (
                isinstance(node.op, ast.BitXor)
                and isinstance(node.value, ast.Constant)
                and node.value.value == 1
            ):
                v.toggle_pattern += 1
            elif isinstance(node.value, ast.Constant):
                v.aug_by_const += 1
            else:
                v.aug_by_var += 1
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if node.value is not None and isinstance(node.target, ast.Name):
            self._record(node.target.id, node.value, node.lineno)
        self.generic_visit(node)

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:  # walrus :=
        if isinstance(node.target, ast.Name):
            self._record(node.target.id, node.value, node.lineno)
        self.generic_visit(node)

    def visit_With(self, node: ast.With) -> None:
        for item in node.items:
            if item.optional_vars is not None:
                # Record the bound name(s) as assigned without passing a value
                # node — we don't want a placeholder Constant(None) to falsely
                # trigger sentinel / lazy-value detection.
                def _rec(t: ast.expr) -> None:
                    if isinstance(t, ast.Name):
                        v = self._get(t.id)
                        v.total_assigns += 1
                        if v.first_line == 0:
                            v.first_line = node.lineno
                    elif isinstance(t, (ast.Tuple, ast.List)):
                        for elt in t.elts:
                            _rec(elt)

                _rec(item.optional_vars)
        self.generic_visit(node)

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:
        if node.name:
            v = self._get(node.name)
            v.total_assigns += 1
            if v.first_line == 0:
                v.first_line = node.lineno
        self.generic_visit(node)

    # -- Method call tracking ---------------------------------------------------

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Attribute) and isinstance(
            node.func.value, ast.Name
        ):
            method = node.func.attr
            key = (node.func.value.id, self._scope_str())
            if key in self.vars:
                v = self.vars[key]
                if method in CONTAINER_METHODS:
                    v.container_methods.add(method)
                elif method in ORGANIZER_METHODS:
                    v.organizer_methods.add(method)
        self.generic_visit(node)


# -- Role determination ---------------------------------------------------------


def _determine_role(v: VarInfo) -> str:
    """Apply heuristics to assign a role to a variable."""

    # Temporary: appears in an explicit tuple swap  a, b = b, a
    if v.in_swap:
        return TEMPORARY

    # Toggle: every self-referential assignment is a two-value cycle.
    #   x = not x  |  x = C - x  |  x ^= 1
    # Checked before stepper/gatherer so cyclic patterns aren't misread as steppers.
    if (
        v.toggle_pattern > 0
        and v.self_ref_const == 0
        and v.self_ref_var == 0
        and v.aug_by_const == 0
        and v.aug_by_var == 0
    ):
        return TOGGLE

    # Log: append-only collection — only additive methods, no removal.
    if v.container_methods and v.container_methods.issubset(_LOG_METHODS):
        return LOG

    # Container: mutable collection with elements added or removed
    if v.container_methods:
        return CONTAINER

    # Organizer: collection only sorted or reversed, never mutated
    if v.organizer_methods and not v.container_methods:
        return ORGANIZER

    # Stepper: explicit for-loop iteration variable
    if v.for_loop_target:
        return STEPPER

    # Stepper / Gatherer: augmented assignment (+=, -=, …) inside a loop
    if v.aug_assigns > 0 and v.loop_assigns > 0:
        return STEPPER if v.aug_by_var == 0 else GATHERER

    # Stepper / Gatherer: non-augmented self-referential assignment in a loop
    #   x = x + 1  →  stepper      x = x + y  →  gatherer
    if (v.self_ref_const + v.self_ref_var) > 0 and v.loop_assigns > 0:
        return STEPPER if v.self_ref_var == 0 else GATHERER

    # One-way flag: boolean initialised one way, only ever flipped the other way.
    # Checked before general loop-assignment tests to avoid misclassification
    # as most-wanted holder (flag set inside an if inside a loop).
    if (
        v.bool_false_out_loop >= 1
        and v.bool_true_in_loop >= 1
        and v.bool_false_in_loop == 0
    ):
        return ONE_WAY_FLAG
    if (
        v.bool_true_out_loop >= 1
        and v.bool_false_in_loop >= 1
        and v.bool_true_in_loop == 0
    ):
        return ONE_WAY_FLAG

    # Most-wanted / most-recent holder: assignments inside loops
    if v.loop_assigns > 0:
        if v.cond_loop_assigns == v.loop_assigns:
            return MOST_WANTED  # every loop assign is inside an if
        return MOST_RECENT  # at least one unconditional loop assign

    # Lazy value: sentinel (None / -1 / "") assigned outside a loop, then set
    # for real inside a conditional (also outside a loop).
    if (
        v.sentinel_out_assigns >= 1
        and v.any_cond_assigns >= 1
        and v.loop_assigns == 0
        and v.aug_assigns == 0
    ):
        return LAZY_VALUE

    # Fixed value: no loop assignments, augmented assignments, or self-references
    if (
        v.loop_assigns == 0
        and v.aug_assigns == 0
        and v.self_ref_const == 0
        and v.self_ref_var == 0
    ):
        return FIXED_VALUE

    return UNKNOWN


# -- Public API -----------------------------------------------------------------


def analyze(source: str) -> list[tuple[VarInfo, str]]:
    """Parse Python source and return (VarInfo, role) pairs, sorted for display."""
    tree = ast.parse(source)
    collector = RoleCollector()
    collector.visit(tree)
    results = [
        (v, _determine_role(v)) for v in collector.vars.values() if v.total_assigns > 0
    ]
    results.sort(key=lambda pair: (pair[0].scope, pair[0].first_line, pair[0].name))
    return results


def format_static(results: list[tuple[VarInfo, str]], fmt: str = "markdown") -> str:
    """Format static-analysis results as a table in the requested format.

    fmt must be one of: 'markdown', 'html', 'csv'.
    Returns an empty string (and prints a warning) when results is empty.
    """
    if not results:
        return ""

    table = PrettyTable(["Scope", "Variable", "Role", "Location"])
    table.align = "l"
    for v, role in results:
        table.add_row(
            [v.scope, v.name, role, f"line {v.first_line}" if v.first_line else "?"]
        )

    if fmt == "html":
        return table.get_html_string()
    if fmt == "csv":
        return table.get_csv_string().rstrip("\r\n")
    # default: markdown
    table.set_style(TableStyle.MARKDOWN)
    return str(table)


def format_dynamic(roles: dict[tuple[str, str], str], fmt: str = "markdown") -> str:
    """Format dynamic-analysis results as a table.

    fmt must be one of: 'markdown', 'html', 'csv'.
    Returns an empty string when no dynamic roles were detected.
    """
    if not roles:
        return ""
    table = PrettyTable(["Variable", "Scope", "Role"])
    table.align = "l"
    for (name, scope), role in sorted(roles.items()):
        table.add_row([name, scope, role])
    if fmt == "html":
        return table.get_html_string()
    if fmt == "csv":
        return table.get_csv_string().rstrip("\r\n")
    table.set_style(TableStyle.MARKDOWN)
    return str(table)
