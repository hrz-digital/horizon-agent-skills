<p align="left">
  <img src="assets/horizon-logo.svg" alt="Horizon" width="220">
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

Initial supported AI Harnesses are OpenAI Codex, Claude Code, and Pi. Each needs both:

1. Horizon Skill Set installed in Harness.
2. Released Horizon CLI 1.x installed and Connection Profile imported by User in separate terminal.

List available skills:

```bash
npx skills add hrz-digital/horizon-agent-skills --list
```

Install all skills globally:

```bash
npx skills add hrz-digital/horizon-agent-skills --all -g
```

Install Horizon CLI from official distribution:

```sh
curl -fsSL https://platform.hrz.digital/cli/install.sh | sh
```

Windows PowerShell:

```powershell
irm https://platform.hrz.digital/cli/install.ps1 | iex
```

Verify with `horizon version`. Then create Agent Credential in target Installation, copy one-time Connection Profile, and personally run `horizon connection add` in separate terminal. Never paste Connection Profile or API key into Agent chat.

## Authentication

Horizon CLI is required authentication and transport boundary. It stores Agent Credential API keys in operating-system credential store, exchanges short-lived tokens, and sends authenticated requests. API keys and tokens never belong in Harness storage, environment variables, prompts, skills, repositories, URLs, command arguments, output, or logs.

Skills verify CLI, list live-checked non-secret Connection Profiles, require explicit customer Installation choice, and pass selected profile on every request. Shared procedure lives in [`horizon`](skills/horizon/SKILL.md).

## Compatibility

Each workflow declares supported CLI and Discovery contract majors in frontmatter. Missing or unsupported CLI or Discovery major stops platform work; Skills never guess routes, schemas, payloads, or fall back to raw credential-bearing HTTP.
