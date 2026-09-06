# Horizon Skill Set

## Purpose

This repository packages portable workflow skills for AI Agents operating Horizon. Skills add workflow judgment, safety, and continuity without becoming API documentation. Horizon Discovery remains authoritative for routes, schemas, catalogs, availability, authorization, Metadata Context, and runtime behavior; each workflow must read current values from Discovery.

## Skill map

- [`horizon`](../skills/horizon/SKILL.md) — verify CLI, explicitly select live-valid customer Installation, bootstrap Discovery, classify work, select or resume Workspace, and record handoff.
- [`horizon-metadata-authoring`](../skills/horizon-metadata-authoring/SKILL.md) — propose Metadata through a Workspace and human review.
- [`horizon-architecture-analysis`](../skills/horizon-architecture-analysis/SKILL.md) — analyze Published Metadata and maintain Architectural Metadata Tickets.
- [`horizon-runtime`](../skills/horizon-runtime/SKILL.md) — operate Business Data and execute runtime Actions.
- [`horizon-ask-for-guidance`](../skills/horizon-ask-for-guidance/SKILL.md) — user-invoked, read-only guidance for Metadata decisions and explaining configured Installation behavior.

Every platform workflow first runs [`horizon`](../skills/horizon/SKILL.md) bootstrap. It links single shared [CLI installation](../skills/horizon/references/cli-installation.md) and [Connection Profile](../skills/horizon/references/connections.md) references. When classifying runtime versus Metadata work, selecting or resuming Workspace, or recording handoff, continue there. When the request follows another branch, read that branch's linked skill; do not copy its workflow rules here.

## Repository boundary

Skills are separate from Horizon Core so they can release independently and install through GitHub, `npx skills`, or skills.sh. Skill frontmatter declares supported Horizon CLI and Discovery contract majors. OpenAI Codex, Claude Code, and Pi are initial supported Harnesses; each requires both CLI and Horizon Skill Set. Runtime behavior for an unsupported major is defined by [`horizon`](../skills/horizon/SKILL.md).

## Verification

Validate workflows against black-box Horizon Discovery without Core repository access. Judge decisions and observable platform use, not exact prose; use each skill's completion criteria as the checkable boundary.
