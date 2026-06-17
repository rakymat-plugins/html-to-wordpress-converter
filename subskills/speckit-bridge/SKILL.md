---
name: html-to-wordpress-speckit-bridge
description: Bridge the HTML-to-Sage WordPress workflow to the real GitHub Spec Kit CLI and commands, including installation checks, agent integration selection, command usage, and artifact logging.
---

# Spec Kit Bridge

Read `../../references/enterprise-html-to-acf-rules.md` and `../../references/full-acf-editability-rules.md`, then pass both constraint sets into the Spec Kit prompts.

Do not fake Spec Kit. Verify the real CLI:

```bash
specify --version
```

If missing:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Initialize:

```bash
specify init <project-name> --integration <agent>
```

Use the current integration. For Claude Code use the Claude integration. For Codex CLI, use the Codex integration or skills mode if available. For generic agents, initialize with the closest supported integration and keep reusable prompts in project files.

Run:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.tasks
/speckit.analyze
```

Run `/speckit.implement` only after approval.

Log commands and outcomes in `.html-to-sage/SPECKIT-RUNS.md`.
