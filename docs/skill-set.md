# Horizon Skill Set

## Purpose

This repository packages portable workflow skills for AI Agents operating Horizon. Skills add workflow judgment, safety, and continuity without becoming API documentation. Horizon Discovery remains authoritative for routes, schemas, catalogs, availability, authorization, Metadata Context, and runtime behavior; each workflow must read current values from Discovery.

## Skill map

- [`horizon`](../skills/horizon/SKILL.md) — verify CLI, explicitly select live-valid customer Installation, bootstrap Discovery, classify work, select or resume Workspace, and record handoff.
- [`horizon-interview`](../skills/horizon-interview/SKILL.md) — clarify intent, summarize agreed work in chat, obtain required confirmations, and reserve files for exceptional plans.
- [`horizon-metadata-authoring`](../skills/horizon-metadata-authoring/SKILL.md) — propose Metadata, including Process Definitions and their Structure Action bindings, through a Workspace and human review.
- [`horizon-architecture-analysis`](../skills/horizon-architecture-analysis/SKILL.md) — analyze Published Metadata and maintain Architectural Metadata Tickets.
- [`horizon-runtime`](../skills/horizon-runtime/SKILL.md) — operate Business Data, execute runtime Actions and Process runs, inspect authorized Process Instances, and configure and test Installation SMTP servers.
- [`horizon-ask-for-guidance`](../skills/horizon-ask-for-guidance/SKILL.md) — user-invoked, read-only guidance for Metadata decisions and explaining configured Installation behavior.

Bootstrap and inspect first through [`horizon`](../skills/horizon/SKILL.md), then apply the [interview and plan gates](../skills/horizon-interview/SKILL.md#planning-gates). Default to a chat summary and same-session execution, validation, User testing, and adjustments. Routine Metadata continuity uses Workspace Activity; files follow the exceptional plan-file gate. Generic guidance needs no bootstrap.

Keep policy with its owner: `horizon` owns routing, target verification, and Workspace selection; `horizon-interview` owns planning gates; its [plan reference](../skills/horizon-interview/references/implementation-plan.md) owns the saved-file lifecycle; `horizon-metadata-authoring` owns modeling/Page defaults and execution; guidance explains these workflows without running them. Shared [CLI installation](../skills/horizon/references/cli-installation.md) and [Connection Profile](../skills/horizon/references/connections.md) references own setup. Link to these owners rather than copying their rules.

## Repository boundary

Skills are separate from Horizon Core so they can release independently and install through GitHub, `npx skills`, or skills.sh. Skill frontmatter declares supported Horizon CLI and Discovery contract majors. OpenAI Codex, Claude Code, and Pi are initial supported Harnesses; each requires both CLI and Horizon Skill Set. Runtime behavior for an unsupported major is defined by [`horizon`](../skills/horizon/SKILL.md).

## Verification

Validate workflows against black-box Horizon Discovery without Core repository access. Judge decisions and observable platform use, not exact prose; use each skill's completion criteria as the checkable boundary.
