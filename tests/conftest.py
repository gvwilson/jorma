"""Shared helpers for roles tests."""

import sys
from pathlib import Path

# Allow importing roles from the project root
sys.path.insert(0, str(Path(__file__).parent.parent))

from roles import analyze, trace_function


def role_of(source: str, name: str, scope: str = "module") -> str:
    """Return the static role assigned to *name* in *scope* for *source*."""
    results = analyze(source)
    for v, role in results:
        if v.name == name and v.scope == scope:
            return role
    raise KeyError(f"Variable {name!r} in scope {scope!r} not found")


def dynamic_role_of(func, *args, name: str, scope: str | None = None) -> str:
    """Run *func* under tracing and return the dynamic role of *name*.

    If *scope* is None, match the first key whose variable name equals *name*.
    Raises KeyError if not found.
    """
    roles = trace_function(func, *args)
    for (var_name, var_scope), role in roles.items():
        if var_name == name:
            if scope is None or var_scope == scope:
                return role
    raise KeyError(f"Dynamic variable {name!r} not detected")
