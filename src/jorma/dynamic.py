"""Dynamic analysis: sys.settrace-based tracer for phase and follower roles."""

import importlib.util
import sys
import types
from pathlib import Path

from .constants import FOLLOWER, PHASE

# Maximum number of distinct scalar states to still classify as a phase variable.
# Sajaniemi's definition implies a small, enumerated set; 6 is a practical limit.
_PHASE_MAX_STATES = 6


def _safe_eq(a: object, b: object) -> bool:
    """Equality comparison that never raises (for tracing contexts)."""
    try:
        result = a == b
        if isinstance(result, bool):
            return result
        return bool(result)
    except Exception:
        return False


class DynamicTracer:
    """Trace a function call and detect phase and follower roles."""

    def __init__(self) -> None:
        # key = (var_name, scope_string)
        self.sequences: dict[tuple[str, str], list] = {}
        # context[key][i] = {other_name: value_before_i-th_change}
        self.contexts: dict[tuple[str, str], list[dict]] = {}
        # is_update[key][i] = True if this was an update to an existing var
        # (False = first assignment / initialization)
        self.is_update: dict[tuple[str, str], list[bool]] = {}
        # snapshot of f_locals before each line, keyed by frame id
        self._prev: dict[int, dict[str, object]] = {}

    # -- sys.settrace callbacks -------------------------------------------------

    def tracer(
        self,
        frame: types.FrameType,
        event: str,
        arg: object,
    ) -> object:
        if event == "call":
            self._prev[id(frame)] = {}
            return self._line_tracer
        return None

    def _line_tracer(
        self,
        frame: types.FrameType,
        event: str,
        arg: object,
    ) -> object:
        if event not in ("line", "return"):
            return self._line_tracer
        curr = {k: v for k, v in frame.f_locals.items() if not k.startswith("__")}
        prev = self._prev.get(id(frame), {})
        scope = self._scope_for(frame)
        for name, new_val in curr.items():
            old_val = prev.get(name)
            if name in prev and _safe_eq(old_val, new_val):
                continue
            key = (name, scope)
            if key not in self.sequences:
                self.sequences[key] = []
                self.contexts[key] = []
                self.is_update[key] = []
            self.sequences[key].append(new_val)
            # Context snapshot: values of all *other* locals just before this change
            self.contexts[key].append(
                {k: prev[k] for k in prev if k != name}
            )
            # Track whether this is an update (variable already existed) or
            # a first assignment; follower detection skips first assignments.
            self.is_update[key].append(name in prev)
        self._prev[id(frame)] = curr
        if event == "return":
            self._prev.pop(id(frame), None)
        return self._line_tracer

    def _scope_for(self, frame: types.FrameType) -> str:
        parts: list[str] = []
        f: types.FrameType | None = frame
        while f is not None:
            name = f.f_code.co_name
            if name == "<module>":
                parts.append("module")
                break
            parts.append(name)
            f = f.f_back
        else:
            parts.append("module")
        return ".".join(reversed(parts))

    # -- Role detectors ---------------------------------------------------------

    def _check_phase(self, values: list) -> bool:
        """True if values look like a state-machine variable."""
        try:
            distinct: set = set(values)
        except TypeError:
            return False
        # Must not be boolean (those are one-way flags or toggles)
        if any(isinstance(v, bool) for v in distinct):
            return False
        # States must be simple scalars
        if not all(isinstance(v, (int, str, float, type(None))) for v in distinct):
            return False
        # Need at least 2 and at most _PHASE_MAX_STATES distinct values
        if not (2 <= len(distinct) <= _PHASE_MAX_STATES):
            return False
        # Must revisit states (more observations than distinct values).
        # This already excludes simple steppers, which never revisit a value.
        if len(values) <= len(distinct):
            return False
        return True

    def _check_follower(
        self, key: tuple[str, str], values: list
    ) -> bool:
        """True if var consistently receives the previous value of some other var.

        Only update observations (not first-assignments) are considered, so
        an initialisation like ``prev = None`` before a loop does not break
        detection of the ``prev = current`` follower pattern inside the loop.
        """
        contexts = self.contexts.get(key, [])
        updates = self.is_update.get(key, [])
        # Gather only the (value, context) pairs where the variable was updated
        update_pairs = [
            (v, c) for v, c, u in zip(values, contexts, updates) if u
        ]
        if len(update_pairs) < 2:
            return False
        candidates: set | None = None
        for new_val, ctx in update_pairs:
            matching = {
                other_name
                for other_name, ctx_val in ctx.items()
                if _safe_eq(ctx_val, new_val)
            }
            candidates = matching if candidates is None else candidates & matching
            if not candidates:
                return False
        return bool(candidates)

    def detect_roles(self) -> dict[tuple[str, str], str]:
        """Return dynamic role assignments for variables with enough observations."""
        result: dict[tuple[str, str], str] = {}
        for key, values in self.sequences.items():
            if len(values) < 2:
                continue
            if self._check_follower(key, values):
                result[key] = FOLLOWER
            elif self._check_phase(values):
                result[key] = PHASE
        return result


def run_dynamic(
    path: Path,
    func_name: str,
    func_args: list[str],
) -> dict[tuple[str, str], str]:
    """Import path, call func_name(*func_args) under tracing, return dynamic roles."""
    spec = importlib.util.spec_from_file_location("_roles_target", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load '{path}'")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]

    if not hasattr(module, func_name):
        raise AttributeError(f"'{path}' has no function '{func_name}'")
    func = getattr(module, func_name)
    tracer = DynamicTracer()
    old_trace = sys.gettrace()
    sys.settrace(tracer.tracer)
    try:
        func(*func_args)
    finally:
        sys.settrace(old_trace)

    return tracer.detect_roles()


def trace_function(
    func: object,
    *args: object,
) -> dict[tuple[str, str], str]:
    """Trace a callable directly and return detected dynamic roles.

    Convenience wrapper used by tests.
    """
    tracer = DynamicTracer()
    old_trace = sys.gettrace()
    sys.settrace(tracer.tracer)
    try:
        func(*args)  # type: ignore[operator]
    finally:
        sys.settrace(old_trace)
    return tracer.detect_roles()
