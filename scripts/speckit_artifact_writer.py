from __future__ import annotations

import json
import re
from pathlib import Path

from artifact_writer import CLONE_READINESS_RULE, EDITABILITY_RULE, GLOBAL_PARTS_RULE, PAGES_RULE, VISUAL_RULE
from project_detector import detect_files


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "html-to-sage-conversion"


def title_from_source(source: Path) -> str:
    html_files = detect_files(source).get("html", [])
    for html in html_files:
        text = (source / html).read_text(encoding="utf-8", errors="ignore")
        match = re.search(r"<title>(.*?)</title>", text, flags=re.IGNORECASE | re.DOTALL)
        if match:
            return re.sub(r"\s+", " ", match.group(1)).strip()
    return "HTML to Sage WordPress Conversion"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_blockers(project: Path, theme_name: str, wp_path: str | None) -> list[str]:
    blockers: list[str] = []
    if not wp_path:
        blockers.append("Confirm WordPress install path before implementation.")
    if not theme_name:
        blockers.append("Confirm final Sage theme slug before implementation.")

    body = [
        "# BLOCKERS",
        "",
        "The planning workflow can run with defaults, but implementation must stop until these choices are resolved.",
        "",
    ]
    if blockers:
        body.extend(f"- {item}" for item in blockers)
    else:
        body.append("- None.")
    write(project / ".html-to-sage" / "BLOCKERS.md", "\n".join(body))
    return blockers


def write_constitution(project: Path) -> None:
    write(
        project / ".specify" / "memory" / "constitution.md",
        f"""<!--
Sync Impact Report
Version change: generated -> 1.0.0
Modified principles: HTML-to-Sage WordPress conversion principles applied
Added sections: Sage Architecture Requirements, Spec Kit Workflow, Quality Gates
Removed sections: unresolved template placeholders
Templates requiring updates: generated spec, plan, tasks, and .html-to-sage artifacts
Follow-up TODOs: none
-->

# HTML to Sage WordPress Conversion Constitution

## Core Principles

### I. HTML Visual Parity First

The original HTML website is the visual source of truth. {VISUAL_RULE}

No redesign, improvement, layout simplification, spacing change, typography change, color change, or animation removal is permitted without explicit user approval. Visual mismatch is failed work.

### II. Section-by-Section Conversion

Each original HTML section MUST be classified as one of: ACF Block, global template part, CPT archive/single template, or reusable component. The full page MUST NOT be flattened into one giant block.

Headers, footers, navigation, announcement bars, mobile sticky CTAs, schema data, and other site-wide UI MUST be mapped to Sage layout partials/template parts by default, not normal page ACF blocks.

### III. Sage Architecture Enforcement

The WordPress theme MUST use Sage, Acorn, Blade, Vite, SCSS, ACF Pro, and code-owned ACF field groups. The implementation MUST include `framework/builder/acf-blocks/`, `framework/builder/front-end/`, `framework/builder/blocks.php`, `framework/custom-fields/`, `framework/post-type/`, and `framework/taxonomies/`.

### IV. ACF Editability Without Over-Dynamic DOM

{EDITABILITY_RULE}

Wrappers, container classes, grid classes, animation hooks, JS hooks, ARIA structure, and technical layout markup SHOULD remain in templates unless the editor explicitly needs control over them.

### V. Justified CPTs Only

Custom post types and taxonomies are allowed only when content is repeatable across pages, independently managed, filterable, archiveable, searchable, requires its own URL, or needs a separate admin workflow.

## Sage Architecture Requirements

Every ACF block MUST define registration, fields, frontend template, SCSS file, optional JS module, editor preview behavior, and visual parity checklist.

Global site UI MUST use Sage partials, layout SCSS, WordPress menus, ACF options, theme options, Customizer, or approved plugins.

## Spec Kit Workflow

Spec Kit artifacts are the planning source of truth for implementation. The workflow MUST produce and keep aligned `.specify/memory/constitution.md`, `specs/<feature>/spec.md`, `plan.md`, `research.md`, `data-model.md`, `quickstart.md`, `tasks.md`, and `.html-to-sage/*`.

The source HTML/CSS/JS/assets MUST be preserved in `stock/` and treated as read-only source material.

## Quality Gates

Implementation MUST NOT begin until stock source is preserved, every HTML section has a WordPress target decision, every ACF block has a field contract, every meaningful content item has an editable source or documented exception, every global template part has a data source, CPT decisions are justified, visual QA tasks exist, Spec Kit spec/plan/tasks exist, and WordPress clone-readiness tasks exist.

{CLONE_READINESS_RULE}

## Governance

This constitution supersedes conflicting implementation shortcuts. Changes require updating this file, affected Spec Kit artifacts, and `.html-to-sage/DECISIONS.md`.

**Version**: 1.0.0 | **Ratified**: 2026-06-17 | **Last Amended**: 2026-06-17
""",
    )


def write_spec_feature(project: Path, feature_slug: str, source_title: str, theme_name: str) -> Path:
    feature_dir = project / "specs" / f"001-{feature_slug}"
    write(
        project / ".specify" / "feature.json",
        json.dumps({"feature_directory": str(Path("specs") / f"001-{feature_slug}")}),
    )
    write(
        feature_dir / "spec.md",
        f"""# Feature Specification: HTML to Sage WordPress Conversion

**Feature Branch**: `001-{feature_slug}`
**Created**: 2026-06-17
**Status**: Draft ready for planning
**Input**: Convert `{source_title}` from preserved static HTML in `stock/` into the `{theme_name}` WordPress Sage theme using ACF Blocks, global template parts, justified CPT decisions, and mandatory visual parity.

## User Scenarios & Testing

### User Story 1 - Rebuild the pages visually (Priority: P1)

A site editor can rebuild the original HTML pages in WordPress using documented ACF blocks and see frontend pages that match the original static HTML.

**Independent Test**: Compare the WordPress output against `stock/` at desktop, tablet, and mobile viewports.

### User Story 2 - Edit all meaningful content safely (Priority: P1)

A non-technical editor can update headings, paragraphs, images, buttons, cards, reviews, FAQ items, contact details, and global site content without editing templates or pasting HTML.

**Independent Test**: Change representative content in each block/options source and verify the frontend updates without layout breakage.

### User Story 3 - Preserve maintainable Sage architecture (Priority: P2)

A developer can maintain the converted site using Sage, Acorn, Blade, Vite, SCSS, code-owned ACF field groups, modular JS, and documented block contracts.

**Independent Test**: Inspect the theme structure and verify every section has its registration, field group, frontend template, SCSS ownership, optional JS ownership, and QA checklist.

### User Story 4 - Validate before implementation completion (Priority: P2)

A reviewer can verify implementation is complete only after visual parity, editability, architecture, security, and performance gates pass.

**Independent Test**: Run the documented QA checklist and confirm every converted section passes or has explicit user-approved exception.

## Requirements

- **FR-001**: The system MUST preserve the original static source in `stock/` and treat it as read-only source material.
- **FR-002**: The system MUST map every original HTML page and section to a WordPress target before implementation.
- **FR-003**: Each page-owned visual section MUST become an ACF block with code-owned fields, frontend template, SCSS ownership, optional JS, editor preview behavior, and visual parity checklist.
- **FR-004**: Header, navigation, footer, announcement, mobile sticky CTA, schema data, and other site-wide UI MUST be global Sage template parts/options/menus, not page ACF blocks.
- **FR-005**: {EDITABILITY_RULE}
- **FR-006**: Templates MUST NOT hardcode client-editable content.
- **FR-007**: CPTs and taxonomies MUST NOT be created unless justified by reuse, archive, filtering, independent URL, search, or separate admin workflow.
- **FR-008**: The conversion MUST preserve source behavior including navigation, accordions, sliders, animation hooks, hover states, and responsive behavior.
- **FR-009**: The implementation MUST use Sage, Acorn, Blade, Vite, SCSS, ACF Pro, and the documented framework layer.
- **FR-010**: The implementation MUST avoid live frontend references to `stock/`.
- **FR-011**: Dynamic output MUST be escaped/sanitized with WordPress-appropriate functions.
- **FR-012**: Completion MUST be blocked until visual QA passes.
- **FR-013**: The delivered theme MUST work when cloned into `wp-content/themes/<theme-slug>` and activated, or the final report MUST document exactly which runtime checks could not be run and why.

## Success Criteria

- **SC-001**: 100% of original visible sections are mapped to a WordPress target before implementation begins.
- **SC-002**: 100% of meaningful original content items have an editable field/source or documented approved exception.
- **SC-003**: 100% of converted sections pass desktop, tablet, and mobile visual comparison before completion.
- **SC-004**: 0 header/footer/navigation elements are implemented as page ACF blocks unless explicitly approved.
- **SC-005**: 0 unjustified CPTs or taxonomies are introduced.
- **SC-006**: 0 live frontend template references point to `stock/`.
- **SC-007**: WordPress recognizes the cloned theme from `style.css`, and activation has a valid bootstrap/render path.

## Assumptions

- Visual improvements are not allowed unless explicitly approved.
- Forms, multilingual support, and CPTs are optional only when the source or user requires them.
""",
    )
    write(
        feature_dir / "checklists" / "requirements.md",
        """# Specification Quality Checklist: HTML to Sage WordPress Conversion

**Purpose**: Validate specification completeness and quality before proceeding to planning
**Created**: 2026-06-17
**Feature**: ../spec.md

## Content Quality

- [x] No unapproved implementation details leak beyond mandated architecture constraints
- [x] Focused on user value and business needs
- [x] All mandatory sections completed

## Requirement Completeness

- [x] No [NEEDS CLARIFICATION] markers remain
- [x] Requirements are testable and unambiguous
- [x] Success criteria are measurable
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified
""",
    )
    return feature_dir


def write_plan_docs(feature_dir: Path, theme_name: str, wp_path: str | None) -> None:
    wp_text = wp_path or "NEEDS CONFIRMATION before implementation"
    write(
        feature_dir / "plan.md",
        f"""# Implementation Plan: HTML to Sage WordPress Conversion

**Branch**: `001-html-to-sage-conversion` | **Date**: 2026-06-17 | **Spec**: `spec.md`

## Summary

Convert preserved static HTML from `stock/` into `{theme_name}` using Sage, Acorn, Blade, Vite, SCSS, ACF Pro, global template parts, justified CPT decisions, and mandatory 100% visual parity.

## Technical Context

**Language/Version**: PHP 8.2+, WordPress 6.6+, Node.js 20+, JavaScript ES modules, SCSS

**Primary Dependencies**: Roots Sage, Acorn, Blade, Vite, Advanced Custom Fields Pro

**Storage**: WordPress database for pages, ACF fields/options, menus, media library; `stock/` as read-only source archive

**Target Platform**: WordPress Sage theme in `{wp_text}`

**Project Type**: WordPress theme conversion

**Constraints**: No redesign; no page builders; no hardcoded meaningful content; no unjustified CPTs; no live `stock/` references; visual mismatch fails the task.

**WordPress Clone Readiness**: {CLONE_READINESS_RULE}

## Constitution Check

- HTML Visual Parity First: PASS
- Section-by-Section Conversion: PASS
- Sage Architecture Enforcement: PASS
- ACF Editability Without Over-Dynamic DOM: PASS
- Justified CPTs Only: PASS

## Project Structure

```text
{theme_name}/
|-- app/
|-- framework/
|   |-- builder/
|   |   |-- acf-blocks/
|   |   |-- front-end/
|   |   `-- blocks.php
|   |-- custom-fields/
|   |-- post-type/
|   `-- taxonomies/
`-- resources/
    |-- css/
    |   |-- common/
    |   |-- components/
    |   |-- layout/
    |   `-- blocks/
    |-- js/
    `-- views/
        |-- layouts/
        `-- partials/
```

## Design References

- `.html-to-sage/SECTION-MAP.md`
- `.html-to-sage/ACF-BLOCKS.md`
- `.html-to-sage/GLOBAL-TEMPLATE-PARTS.md`
- `.html-to-sage/CPT-TAXONOMY-MAP.md`
- `.html-to-sage/ASSET-MAP.md`
- `.html-to-sage/JS-BEHAVIOR-MAP.md`

## Post-Design Constitution Check

PASS. No known constitution violations. Implementation remains blocked until user explicitly approves implementation and required choices in `.html-to-sage/BLOCKERS.md` are resolved.
""",
    )
    write(
        feature_dir / "research.md",
        """# Research: HTML to Sage WordPress Conversion

## Decision: Use ACF repeaters for page-local repeated content

Rationale: Use CPTs only when content needs archive/single/filter/search/reuse/admin workflow.

## Decision: Use global template parts for site chrome

Rationale: Header/footer/navigation/global CTA/schema are site-wide concerns and must not be repeated as page-local ACF blocks.

## Decision: Split CSS and JS by ownership

Rationale: Preserve maintainability while keeping visual output identical.

## Decision: Preserve original source in stock

Rationale: `stock/` is the immutable source of visual truth and QA comparison baseline.
""",
    )
    write(
        feature_dir / "data-model.md",
        """# Data Model: HTML to Sage WordPress Conversion

## Page
- title
- slug
- ordered ACF block list

## ACF Block
- name
- field group key
- source selector
- frontend template path
- SCSS path
- optional JS path
- fields
- visual parity notes

## Field
- name
- label
- type
- original value
- source selector
- required
- editor note

## Global Template Part
- element
- template path
- editable data source
- options fields
- menu location
- SCSS path
- JS path

## CPT Decision
- candidate
- decision
- justification
- future trigger
""",
    )
    write(
        feature_dir / "quickstart.md",
        f"""# Quickstart: Validate HTML to Sage WordPress Conversion

## Prerequisites

- WordPress install path confirmed: `{wp_text}`
- Sage theme created as `{theme_name}`
- ACF Pro active

## Validation

1. Build pages using `.html-to-sage/PAGES.md`.
2. Populate fields using `.html-to-sage/ACF-BLOCKS.md`.
3. Render global UI using `.html-to-sage/GLOBAL-TEMPLATE-PARTS.md`.
4. Compare WordPress output against `stock/`.
5. Confirm no meaningful content is hardcoded and no frontend path references `stock/`.
6. Confirm the theme can be cloned into `wp-content/themes/<theme-slug>` and activated, or record skipped runtime checks in `.html-to-sage/FINAL-REPORT.md`.

## Pass Condition

{VISUAL_RULE}
""",
    )


def write_tasks(feature_dir: Path, theme_name: str) -> None:
    write(
        feature_dir / "tasks.md",
        f"""# Tasks: HTML to Sage WordPress Conversion

**Input**: `spec.md`, `plan.md`, `.html-to-sage/*`

{VISUAL_RULE}

## Phase 1: Setup

- [ ] T001 Resolve `.html-to-sage/BLOCKERS.md` choices before implementation
- [ ] T002 Create Sage theme `{theme_name}` at the approved WordPress path
- [ ] T003 Install Composer and Node dependencies for `{theme_name}`
- [ ] T004 Add framework layer directories in `{theme_name}/framework/`
- [ ] T005 Configure Vite, SCSS, JS, and Blade entries

## Phase 2: Foundations

- [ ] T006 Register ACF block category and shared render callback in `{theme_name}/framework/builder/blocks.php`
- [ ] T007 Register ACF options page and global options field group
- [ ] T008 Register WordPress menu locations for primary and footer menus
- [ ] T009 Split source CSS into common, components, layout, and blocks
- [ ] T010 Split source JS into navigation, reveal/shared behavior, and block modules
- [ ] T011 Confirm no CPTs are needed or document justified CPTs

## Phase 3: Page and Section Conversion

- [ ] T012 For each page in `.html-to-sage/PAGES.md`, create the matching WordPress page and block order
- [ ] T013 For each global template part in `.html-to-sage/GLOBAL-TEMPLATE-PARTS.md`, create the Sage partial, data source, SCSS, and optional JS
- [ ] T014 For each ACF block in `.html-to-sage/ACF-BLOCKS.md`, create block registration, code-owned fields, frontend template, SCSS, optional JS, editor preview behavior, and visual parity checklist
- [ ] T015 For each section in `.html-to-sage/SECTION-MAP.md`, compare the WordPress output to the original source and fix mismatch until 100% visual parity

## Phase 4: Full Editability

- [ ] T016 Verify every meaningful text item is editable through ACF/options/menu/plugin/CPT data
- [ ] T017 Verify every meaningful image, icon, alt text, button label, URL, card, stat, testimonial, FAQ, contact detail, and legal text is editable or documented as approved exception
- [ ] T018 Verify structural wrappers/classes/layout hooks remain in templates and are not over-modeled as fields
- [ ] T019 Verify no frontend template or stylesheet references `stock/`

## Phase 5: QA and Gates

- [ ] T020 Complete desktop visual QA against `stock/`
- [ ] T021 Complete tablet visual QA against `stock/`
- [ ] T022 Complete mobile visual QA against `stock/`
- [ ] T023 Verify JS behavior parity: navigation, menu, accordions, sliders, animations, active states
- [ ] T024 Verify escaping/sanitization for all dynamic output
- [ ] T025 Run PHP syntax checks and Vite production build
- [ ] T026 Complete `.html-to-sage/VISUAL-QA.md`, `SECURITY-CHECKLIST.md`, and final report

## Phase 6: WordPress Clone Readiness

- [ ] T027 Verify `style.css` contains a valid WordPress theme header
- [ ] T028 Verify `functions.php` bootstraps Composer/autoload and theme setup/framework files
- [ ] T029 Verify a valid render path exists after activation: standard WordPress templates or verified Sage/Acorn routing
- [ ] T030 Verify required plugins and install/build commands are documented in `README.md`
- [ ] T031 Verify Home/page block order and global header/footer/options setup are documented in `README.md`
- [ ] T032 Verify local agent folders, skill source folders, uv caches, `node_modules/`, `vendor/`, and build outputs are ignored unless intentionally committed
- [ ] T033 Verify the reusable skill repo/folder `html-to-wordpress-converter` is not inside the delivered theme and is not installed under `wp-content/themes`
- [ ] T034 If WordPress reports a broken theme named `html-to-wordpress-converter`, delete that wrong folder from `wp-content/themes` and install the generated theme repo/folder instead
- [ ] T035 Run or document Composer, Node, PHP syntax, WordPress activation, and frontend smoke checks in `.html-to-sage/FINAL-REPORT.md`

## Dependencies

- Phase 1 blocks all implementation.
- Phase 2 blocks section conversion.
- Phase 3 and Phase 4 must both pass before QA completion.
- Phase 5 blocks final delivery.
- Phase 6 blocks final delivery.

## Implementation Strategy

Implement global template parts first, then page ACF blocks in page order, then editability audit, visual QA, and WordPress clone-readiness verification. Do not start implementation without explicit user approval.
""",
    )


def write_analyze(project: Path, feature_dir: Path) -> None:
    write(
        project / ".html-to-sage" / "SPECKIT-ANALYZE.md",
        """# Spec Kit Analysis Report

## Findings

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| A1 | Readiness | MEDIUM | `.html-to-sage/BLOCKERS.md` | Implementation may require user choices such as WordPress path/theme slug. | Resolve blockers before `/speckit.implement` or implementation work. |

## Coverage Summary

| Requirement Area | Has Task? | Notes |
|------------------|-----------|-------|
| Stock preservation | yes | Covered by workflow and tasks. |
| Spec Kit artifacts | yes | Constitution, spec, plan, research, data model, quickstart, tasks are generated. |
| Sage architecture | yes | Covered by plan and tasks. |
| ACF editability | yes | Covered by plan and tasks. |
| Global template parts | yes | Covered by plan and tasks. |
| Visual QA | yes | Covered by plan and tasks. |
| WordPress clone-readiness | yes | Covered by plan and tasks. |

## Constitution Alignment Issues

None known.

## Next Actions

Resolve blockers, then ask the user for explicit implementation approval.
""",
    )


def generate_speckit_artifacts(project: Path, source: Path, theme_name: str, wp_path: str | None, feature_name: str) -> Path:
    stock_source = project / "stock"
    source_for_title = stock_source if stock_source.exists() else source
    source_title = title_from_source(source_for_title)
    feature_slug = slugify(feature_name)
    write_blockers(project, theme_name, wp_path)
    write_constitution(project)
    feature_dir = write_spec_feature(project, feature_slug, source_title, theme_name)
    write_plan_docs(feature_dir, theme_name, wp_path)
    write_tasks(feature_dir, theme_name)
    write_analyze(project, feature_dir)
    return feature_dir
