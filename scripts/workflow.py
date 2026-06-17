import argparse
from pathlib import Path

from artifact_writer import VISUAL_RULE, write_initial_artifacts, write_markdown
from asset_collector import copy_to_stock
from html_section_analyzer import analyze_html_sections
from project_detector import detect_files
from speckit_runner import has_specify, install_command


def cmd_check(args: argparse.Namespace) -> int:
    project = Path(args.project).resolve()
    write_initial_artifacts(project)
    spec = "available" if has_specify() else f"missing; install with `{install_command()}`"
    print(f"Project: {project}")
    print(f"Spec Kit: {spec}")
    print(VISUAL_RULE)
    return 0


def cmd_audit(args: argparse.Namespace) -> int:
    source = Path(args.source).resolve()
    project = Path(args.project).resolve()
    write_initial_artifacts(project)
    files = detect_files(source)
    lines = [VISUAL_RULE, "", "## Files"]
    for kind, items in files.items():
        lines.append(f"\n### {kind}")
        lines.extend(f"- {item}" for item in items)
    lines.append("\n## Sections")
    for html in files["html"]:
        path = source / html
        lines.append(f"\n### {html}")
        sections = analyze_html_sections(path)
        if not sections:
            lines.append("- No section/header/footer/main/nav tags detected")
        for section in sections:
            label = section["id"] or section["class"] or "(unlabeled)"
            lines.append(f"- `{section['tag']}` {label}")
    write_markdown(project / ".html-to-sage" / "HTML-AUDIT.md", "HTML AUDIT", "\n".join(lines))
    print(f"Wrote {project / '.html-to-sage' / 'HTML-AUDIT.md'}")
    return 0


def cmd_stock(args: argparse.Namespace) -> int:
    stock = copy_to_stock(Path(args.source).resolve(), Path(args.project).resolve(), overwrite=args.overwrite)
    print(f"Copied source into {stock}")
    print("Treat stock/ as read-only.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Safe helpers for HTML to Sage WordPress Spec Kit workflows.")
    sub = parser.add_subparsers(required=True)

    check = sub.add_parser("check")
    check.add_argument("--project", required=True)
    check.set_defaults(func=cmd_check)

    audit = sub.add_parser("audit")
    audit.add_argument("--source", required=True)
    audit.add_argument("--project", required=True)
    audit.set_defaults(func=cmd_audit)

    stock = sub.add_parser("stock")
    stock.add_argument("--source", required=True)
    stock.add_argument("--project", required=True)
    stock.add_argument("--overwrite", action="store_true")
    stock.set_defaults(func=cmd_stock)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
