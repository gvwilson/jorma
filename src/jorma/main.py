"""Command-line entry point for jorma."""

import argparse
import sys
from pathlib import Path

from .dynamic import run_dynamic
from .static import analyze, format_static


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="jorma",
        description="Analyse variable roles in a Python program.",
    )
    parser.add_argument("program", type=Path, help="Python source file to analyse")
    parser.add_argument("func_name", nargs="?", help="Function to trace dynamically")
    parser.add_argument("func_args", nargs="*", help="Arguments to pass to func_name")
    parser.add_argument(
        "--format",
        choices=["markdown", "html", "csv"],
        default="markdown",
        dest="fmt",
        help="Output format (default: markdown)",
    )
    args = parser.parse_args()

    path: Path = args.program
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

    if args.func_name is not None:
        print("=== Static Analysis ===")
    output = format_static(results, args.fmt)
    if output:
        print(output)

    if args.func_name is not None:
        print("\n=== Dynamic Analysis ===")
        try:
            dynamic = run_dynamic(path, args.func_name, args.func_args)
        except Exception as exc:
            print(f"Error during dynamic analysis ({type(exc).__name__}): {exc}", file=sys.stderr)
            sys.exit(1)
        if not dynamic:
            print("  (no phase or follower variables detected)")
        else:
            for (name, scope), role in sorted(dynamic.items()):
                print(f"  [{scope}]  {name:<24} {role}")
