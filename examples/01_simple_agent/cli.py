"""CLI wrapper for Track 01 Smart Task Execution Agent.

Usage examples:
  python cli.py demo
  python cli.py run --task "Prioritize this backlog: ..."
  python cli.py export --text "<plan text>" --output logs/custom_plan.json
  python cli.py refine --input logs/track01_execution_plan.json --hours 6 --output logs/today_refined_plan.json
"""
import argparse
import os
import sys

# Allow running the CLI from the examples directory
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from main import main as run_demo
from agent import (
    SimpleAgent,
    export_plan_json,
    load_plan_json,
    refine_plan_from_export,
)


def cmd_demo(args):
    run_demo()


def cmd_run(args):
    agent = SimpleAgent(verbose=not args.quiet)
    out = agent.run(args.task)
    print(out)


def cmd_export(args):
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = args.text or ""

    if not text.strip():
        print("No plan text provided. Use --text or --file.")
        return

    res = export_plan_json(text, args.output)
    print(res)


def cmd_load(args):
    out = load_plan_json(args.path)
    print(out)


def cmd_refine(args):
    res = refine_plan_from_export(args.input, available_hours=args.hours, save_to=args.output)
    print(res)


def cmd_tools(args):
    agent = SimpleAgent(verbose=False)
    tools = agent.get_tools_info()
    for t in tools:
        print(f"- {t['name']}: {t['description']}")


def build_parser():
    p = argparse.ArgumentParser(prog="track01-cli")
    sub = p.add_subparsers(dest="command")

    sub_demo = sub.add_parser("demo", help="Run the example demo sequence")
    sub_demo.set_defaults(func=cmd_demo)

    sub_run = sub.add_parser("run", help="Run the agent on a single task")
    sub_run.add_argument("--task", required=True, help="Task text to run the agent on")
    sub_run.add_argument("--quiet", action="store_true", help="Suppress verbose agent output")
    sub_run.set_defaults(func=cmd_run)

    sub_export = sub.add_parser("export", help="Export plan text to repository JSON")
    sub_export.add_argument("--text", help="Plan text to export")
    sub_export.add_argument("--file", help="Read plan text from file")
    sub_export.add_argument("--output", default="logs/track01_execution_plan.json", help="Output path inside repo")
    sub_export.set_defaults(func=cmd_export)

    sub_load = sub.add_parser("load", help="Load an exported plan JSON and print its text")
    sub_load.add_argument("path", help="Path to exported JSON inside repo")
    sub_load.set_defaults(func=cmd_load)

    sub_refine = sub.add_parser("refine", help="Refine an exported plan into a day plan")
    sub_refine.add_argument("--input", required=True, help="Path to exported JSON inside repo")
    sub_refine.add_argument("--hours", type=float, default=6.0, help="Available hours to allocate")
    sub_refine.add_argument("--output", default="logs/today_refined_plan.json", help="Output JSON path inside repo for refined plan")
    sub_refine.set_defaults(func=cmd_refine)

    sub_tools = sub.add_parser("list-tools", help="List available agent tools")
    sub_tools.set_defaults(func=cmd_tools)

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()
    if not getattr(args, "command", None):
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()
