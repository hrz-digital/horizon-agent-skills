# Horizon Agent Skills

Portable [Agent Skills](https://agentskills.io) for AI Agents operating Horizon through machine-facing Discovery.

Horizon Discovery is the source of truth for schemas, affordances, authorization, Metadata Context, and runtime behavior. Skills provide workflow policy, safety, and continuity; they do not replace Discovery.

## Skills

Current workflow instructions and model-invocation rules live in each skill's `SKILL.md`:

- [`horizon`](skills/horizon/SKILL.md)
- [`horizon-metadata-authoring`](skills/horizon-metadata-authoring/SKILL.md)
- [`horizon-architecture-analysis`](skills/horizon-architecture-analysis/SKILL.md)
- [`horizon-runtime`](skills/horizon-runtime/SKILL.md)
- [`horizon-ask-for-guidance`](skills/horizon-ask-for-guidance/SKILL.md) — user-invoked router

## Install

List available skills:

```bash
npx skills add hrz-digital/horizon-agent-skills --list
```

Install all skills globally:

```bash
npx skills add hrz-digital/horizon-agent-skills --all -g
```

Install one skill:

```bash
npx skills add hrz-digital/horizon-agent-skills --skill horizon-ask-for-guidance -g
```

## Authentication

Preferred setup gives the Agent an authenticated HTTP or MCP tool backed by Harness secret storage. API keys never belong in prompts, skills, repositories, URLs, or logs. Harnesses without secret storage may inject:

```text
HORIZON_API_URL
HORIZON_AGENT_API_KEY
```

The connector handles authentication and token refresh through the current harness integration. Skills assume authenticated access and never request or expose secret values.

## Compatibility

Each skill declares its supported Discovery contract major in frontmatter. If the current major is unsupported, stop before platform work and report the mismatch; never guess routes, schemas, or payloads. The shared bootstrap procedure is in [`horizon`](skills/horizon/SKILL.md).
