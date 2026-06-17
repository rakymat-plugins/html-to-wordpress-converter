import argparse
from pathlib import Path

from artifact_writer import VISUAL_RULE, write_initial_artifacts, write_markdown
from asset_collector import copy_to_stock
from html_section_analyzer import analyze_html_sections
from project_detector import detect_files
from speckit_artifact_writer import generate_speckit_artifacts
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
            if (project / ".specify").exists():
                lines.extend(
                    [
                        "",
                        f"## `specify {' '.join(init_args)}`",
                        "",
                        "- exit code: `already-initialized`",
                        "- result: `.specify/` already exists; preserving existing Spec Kit project files.",
                    ]
                )
            else:
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


def _audit(source: Path, project: Path) -> None:
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


def cmd_prepare(args: argparse.Namespace) -> int:
    source = Path(args.source).resolve()
    project = Path(args.project).resolve()
    write_initial_artifacts(project)

    if not args.skip_stock:
        html_in_source = detect_files(source).get("html", [])
        if html_in_source:
            copy_to_stock(source, project, overwrite=args.overwrite_stock, move_source=args.move_source)

    stock = project / "stock"
    audit_source = stock if stock.exists() else source
    _audit(audit_source, project)

    speckit_args = argparse.Namespace(
        project=str(project),
        integration=args.integration,
        skills=args.skills,
        install=args.install_speckit,
        init=args.init_speckit,
        ignore_agent_tools=True,
    )
    cmd_speckit(speckit_args)

    feature_dir = generate_speckit_artifacts(
        project=project,
        source=audit_source,
        theme_name=args.theme_name,
        wp_path=args.wp_path,
        feature_name=args.feature_name,
    )

    lines = [
        f"- project: `{project}`",
        f"- stock source: `{stock if stock.exists() else 'not created'}`",
        f"- audit source: `{audit_source}`",
        f"- feature directory: `{feature_dir}`",
        f"- theme name: `{args.theme_name}`",
        f"- WordPress path: `{args.wp_path or 'NEEDS CONFIRMATION'}`",
        "",
        "## Status",
        "",
        "- Spec Kit installed/initialized when available.",
        "- Spec Kit constitution/spec/plan/research/data-model/quickstart/tasks artifacts generated.",
        "- `.html-to-sage/SPECKIT-ANALYZE.md` generated.",
        "- Implementation remains stopped until the user explicitly approves it.",
    ]
    if not args.wp_path:
        lines.extend(["", "## Needs User Answer", "", "- WordPress install path is required before implementation."])
    write_markdown(project / ".html-to-sage" / "PREPARE-SUMMARY.md", "PREPARE SUMMARY", "\n".join(lines))

    print(f"Prepared HTML-to-Sage workflow in {project}")
    print(f"Feature artifacts: {feature_dir}")
    if not args.wp_path:
        print("Blocked before implementation: WordPress install path is missing.")
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

    prepare = sub.add_parser("prepare")
    prepare.add_argument("--source", required=True)
    prepare.add_argument("--project", required=True)
    prepare.add_argument("--theme-name", default="mei-sage")
    prepare.add_argument("--wp-path")
    prepare.add_argument("--feature-name", default="html-to-sage-conversion")
    prepare.add_argument("--integration", default="codex")
    prepare.add_argument("--skills", dest="skills", action="store_true")
    prepare.add_argument("--no-skills", dest="skills", action="store_false")
    prepare.add_argument("--install-speckit", dest="install_speckit", action="store_true")
    prepare.add_argument("--no-install-speckit", dest="install_speckit", action="store_false")
    prepare.add_argument("--init-speckit", dest="init_speckit", action="store_true")
    prepare.add_argument("--no-init-speckit", dest="init_speckit", action="store_false")
    prepare.add_argument("--overwrite-stock", dest="overwrite_stock", action="store_true")
    prepare.add_argument("--no-overwrite-stock", dest="overwrite_stock", action="store_false")
    prepare.add_argument("--move-source", dest="move_source", action="store_true")
    prepare.add_argument("--copy-source", dest="move_source", action="store_false")
    prepare.add_argument("--skip-stock", action="store_true")
    prepare.set_defaults(skills=True, install_speckit=True, init_speckit=True, overwrite_stock=True, move_source=True)
    prepare.set_defaults(func=cmd_prepare)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
