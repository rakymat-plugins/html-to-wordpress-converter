import argparse
from pathlib import Path

from artifact_writer import VISUAL_RULE, write_initial_artifacts, write_markdown
from asset_collector import copy_to_stock
from html_section_analyzer import analyze_html_sections
from project_detector import detect_files
from speckit_runner import format_result, has_specify, has_uv, install_command, run_specify, run_uv


def cmd_check(args: argparse.Namespace) -> int:
    project = Path(args.project).resolve()
    write_initial_artifacts(project)
    spec = "available" if has_specify(project) else f"missing; install with `{install_command()}`"
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
    stock = copy_to_stock(
        Path(args.source).resolve(),
        Path(args.project).resolve(),
        overwrite=args.overwrite,
        move_source=args.move_source,
    )
    action = "Moved source into" if args.move_source else "Copied source into"
    print(f"{action} {stock}")
    print("Treat stock/ as read-only.")
    return 0


def cmd_speckit(args: argparse.Namespace) -> int:
    project = Path(args.project).resolve()
    write_initial_artifacts(project)

    lines = [
        "# SPECKIT RUNS",
        "",
        "Spec Kit is the required planning foundation. Do not fake Spec Kit artifacts.",
        "",
        f"- project: `{project}`",
        f"- integration: `{args.integration}`",
        f"- skills mode: `{args.skills}`",
        "",
    ]

    if has_specify(project):
        version_result = run_specify(["--version"], project)
        lines.append(format_result(["specify", "--version"], version_result))
    else:
        lines.extend(
            [
                "## `specify --version`",
                "",
                "- exit code: `missing-command`",
                f"- install command: `{install_command()}`",
            ]
        )
        if args.install:
            if not has_uv():
                lines.extend(
                    [
                        "",
                        "## `uv --version`",
                        "",
                        "- exit code: `missing-command`",
                        "- result: `uv is required before the skill can install specify-cli automatically.`",
                    ]
                )
            else:
                uv_version = run_uv(["--version"], project)
                lines.append(format_result(["uv", "--version"], uv_version))
                install_args = [
                    "tool",
                    "install",
                    "specify-cli",
                    "--from",
                    "git+https://github.com/github/spec-kit.git",
                ]
                install_result = run_uv(install_args, project)
                lines.append(format_result(["uv", *install_args], install_result))

    if has_specify(project):
        integration_result = run_specify(["integration", "list"], project)
        lines.append(format_result(["specify", "integration", "list"], integration_result))

        if args.init:
            init_args = ["init", "--here", "--force", "--integration", args.integration]
            if args.ignore_agent_tools:
                init_args.append("--ignore-agent-tools")
            if args.skills:
                init_args.append("--integration-options=--skills")
            init_result = run_specify(init_args, project)
            lines.append(format_result(["specify", *init_args], init_result))
    else:
        lines.extend(
            [
                "",
                "## Not Initialized",
                "",
                "Spec Kit CLI is still unavailable, so `specify init` was not run.",
            ]
        )

    lines.extend(
        [
            "",
            "## Agent Commands",
            "",
            "After successful `specify init`, run the real agent commands/skills:",
            "",
            "```text",
            "/speckit.constitution or $speckit-constitution",
            "/speckit.specify or $speckit-specify",
            "/speckit.clarify or $speckit-clarify",
            "/speckit.plan or $speckit-plan",
            "/speckit.tasks or $speckit-tasks",
            "/speckit.analyze or $speckit-analyze",
            "```",
            "",
            "Do not run `/speckit.implement` or `$speckit-implement` until the user explicitly approves implementation.",
        ]
    )

    path = project / ".html-to-sage" / "SPECKIT-RUNS.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {path}")
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
    stock.add_argument("--move-source", action="store_true")
    stock.set_defaults(func=cmd_stock)

    speckit = sub.add_parser("speckit")
    speckit.add_argument("--project", required=True)
    speckit.add_argument("--integration", default="codex")
    speckit.add_argument("--skills", action="store_true")
    speckit.add_argument("--install", action="store_true")
    speckit.add_argument("--init", action="store_true")
    speckit.add_argument("--ignore-agent-tools", action="store_true", default=True)
    speckit.set_defaults(func=cmd_speckit)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
