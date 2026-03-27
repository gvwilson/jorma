"""Command-line entry point for jorma."""

import sys
from pathlib import Path

from .dynamic import run_dynamic
from .static import analyze, _print_static


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <program.py> [func_name [arg …]]", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    func_name = sys.argv[2] if len(sys.argv) > 2 else None
    func_args = sys.argv[3:] if len(sys.argv) > 3 else []

    if not path.exists():
        print(f"Error: '{path}' not found", file=sys.stderr)
        sys.exit(1)

    try:
        source = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Error reading '{path}': {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        results = analyze(source)
    except SyntaxError as exc:
        print(f"Syntax error in '{path}': {exc}", file=sys.stderr)
        sys.exit(1)

    if func_name is not None:
        print("=== Static Analysis ===")
    _print_static(results)

    if func_name is not None:
        print("\n=== Dynamic Analysis ===")
        try:
            dynamic = run_dynamic(path, func_name, func_args)
        except Exception as exc:
            print(f"Error during dynamic analysis ({type(exc).__name__}): {exc}", file=sys.stderr)
            sys.exit(1)
        if not dynamic:
            print("  (no phase or follower variables detected)")
        else:
            for (name, scope), role in sorted(dynamic.items()):
                print(f"  [{scope}]  {name:<24} {role}")
