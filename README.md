<p align="left">
  <img src="assets/horizon-logo.png" alt="Horizon" height="271">
</p>

# Horizon Agent Skills

Portable [Agent Skills](https://agentskills.io) for AI Agents operating Horizon through machine-facing Discovery. Horizon Discovery is source of truth for schemas, affordances, authorization, Metadata Context, and runtime behavior. Skills provide workflow policy, safety, and continuity; they do not replace Discovery.

## Skills

- [`horizon`](skills/horizon/SKILL.md)
- [`horizon-metadata-authoring`](skills/horizon-metadata-authoring/SKILL.md)
- [`horizon-architecture-analysis`](skills/horizon-architecture-analysis/SKILL.md)
- [`horizon-runtime`](skills/horizon-runtime/SKILL.md)
- [`horizon-ask-for-guidance`](skills/horizon-ask-for-guidance/SKILL.md) — user-invoked router

## Required setup

Initial supported AI Harnesses are OpenAI Codex, Claude Code, and Pi. Complete setup in this order.

1. Install Horizon CLI and verify `horizon version`.
2. Install Horizon Skills in your Harness.

### 1. Install Horizon CLI

macOS/Linux:

```sh
curl -fsSL https://platform.hrz.digital/cli/install.sh | sh
horizon version
```

Windows PowerShell:

```powershell
irm https://platform.hrz.digital/cli/install.ps1 | iex
horizon version
```

### 2. Install Horizon Skills

List available skills:

```bash
npx skills add hrz-digital/horizon-agent-skills --list
```

Install all skills globally:

```bash
npx skills add hrz-digital/horizon-agent-skills --all -g
```

After both steps, create an Agent Credential in the target Installation, copy the one-time Connection Profile, and personally run `horizon connection add` in a separate terminal. Never paste Connection Profile JSON or API keys into Agent chat.

## Updating Skills

Update installed Skills to latest published version:

```bash
npx skills update
```

Install this Skill Set at an exact version:

```bash
npx skills add https://github.com/hrz-digital/horizon-agent-skills/archive/refs/tags/v1.0.0.tar.gz --all -g
```

## Authentication

Horizon CLI is required authentication and transport boundary. It stores Agent Credential API keys in operating-system credential store, exchanges short-lived tokens, and sends authenticated requests. API keys and tokens never belong in Harness storage, environment variables, prompts, skills, repositories, URLs, command arguments, output, or logs.

Skills verify CLI, list live-checked non-secret Connection Profiles, require explicit customer Installation choice, and pass selected profile on every request. Shared procedure lives in [`horizon`](skills/horizon/SKILL.md).

## Compatibility

Each workflow declares supported CLI and Discovery contract majors in frontmatter. Missing or unsupported CLI or Discovery major stops platform work; Skills never guess routes, schemas, payloads, or fall back to raw credential-bearing HTTP.
