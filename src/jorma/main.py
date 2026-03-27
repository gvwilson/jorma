"""Command-line entry point for jorma."""

import argparse
import sys
from pathlib import Path

from .dynamic import run_as_main, run_dynamic
from .static import analyze, format_dynamic, format_static


def main() -> None:
    args = parse_args()
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

    wants_dynamic = args.run or args.func_name is not None
    if wants_dynamic:
        print("### Static analysis\n")
    output = format_static(results, args.fmt)
    if output:
        print(output)

    if args.func_name is not None:
        try:
            dynamic = run_dynamic(
                path, args.func_name, args.func_args, suppress=args.suppress
            )
        except Exception as exc:
            print(
                f"{path}: error during dynamic analysis ({type(exc).__name__}): {exc}",
                file=sys.stderr,
            )
            sys.exit(1)
        dyn_output = format_dynamic(dynamic, args.fmt)
        if dyn_output:
            print("\n### Dynamic analysis\n")
            print(dyn_output)
    elif args.run:
        try:
            dynamic = run_as_main(path, suppress=args.suppress)
        except Exception as exc:
            print(
                f"{path}: error during dynamic analysis ({type(exc).__name__}): {exc}",
                file=sys.stderr,
            )
            sys.exit(1)
        dyn_output = format_dynamic(dynamic, args.fmt)
        if dyn_output:
            print("\n### Dynamic analysis\n")
            print(dyn_output)


def parse_args():
    parser = argparse.ArgumentParser(prog="jorma", description="Analyse variable roles",)
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
    parser.add_argument(
        "--run",
        action="store_true",
        help="Run file as __main__ to collect dynamic role information",
    )
    parser.add_argument(
        "--suppress",
        action="store_true",
        help="Discard stdout from the program being examined; show only jorma's output",
    )
    return parser.parse_args()
