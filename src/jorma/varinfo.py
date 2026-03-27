"""VarInfo dataclass: per-variable counters collected during AST traversal."""

from dataclasses import dataclass, field


@dataclass
class VarInfo:
    name: str
    scope: str
    first_line: int = 0

    # Assignment counts by context
    total_assigns: int = 0
    loop_assigns: int = 0  # inside any for / while
    cond_loop_assigns: int = 0  # inside an if that is itself inside a loop
    any_cond_assigns: int = 0  # inside any if-block (in or out of a loop)

    # Augmented assignments (+=, -=, *=, …)
    aug_assigns: int = 0
    aug_by_const: int = 0  # rhs is a literal constant
    aug_by_var: int = 0  # rhs contains another variable

    # Non-augmented self-referential assignments (x = x + 1, x = f(x, y))
    self_ref_const: int = 0  # rhs uses only self and literals
    self_ref_var: int = 0  # rhs uses self plus at least one other variable

    # Toggle pattern: x = not x  |  x = C - x  |  x ^= 1
    toggle_pattern: int = 0

    # Lazy-value pattern: assigned a sentinel (None / -1 / "") outside a loop
    sentinel_out_assigns: int = 0

    # Role-specific flags
    for_loop_target: bool = False  # is the target of a for statement
    is_parameter: bool = False  # function / method parameter
    in_swap: bool = False  # appears in a tuple swap  a, b = b, a

    # Boolean assignment tracking (for one-way flag detection)
    bool_true_in_loop: int = 0
    bool_false_in_loop: int = 0
    bool_true_out_loop: int = 0
    bool_false_out_loop: int = 0

    # Methods called on this name
    container_methods: set = field(default_factory=set)
    organizer_methods: set = field(default_factory=set)
