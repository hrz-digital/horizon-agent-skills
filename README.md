# Horizon Agent Skills

Portable [Agent Skills](https://agentskills.io) for AI Agents operating Horizon through its machine-facing Discovery contract.

Skills carry workflow policy and best practices. Horizon remains source of truth for schemas, affordances, authorization, Metadata Context, and runtime behavior.

## Skills

- `horizon` — bootstrap Discovery, classify work, select or resume Workspace, and coordinate handoff.
- `horizon-metadata-authoring` — propose coherent Metadata through Workspace validation and human review, including AMT implementation.
- `horizon-architecture-analysis` — audit Published Metadata architecture and maintain Architectural Metadata Tickets.
- `horizon-runtime` — operate Business Data and execute Actions on behalf of Agent Credential's Owner User.
- `horizon-ask-for-guidance` — route a User to suitable Horizon workflow and skill.

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

Preferred setup gives Agent an authenticated HTTP or MCP tool backed by Harness secret storage. API keys never belong in prompts, skills, repositories, URLs, or logs.

Harnesses without secret storage may inject:

```text
HORIZON_API_URL
HORIZON_AGENT_API_KEY
```

A connector exchanges Agent Credential API key through `/auth/token`, keeps returned Bearer token in memory, and exchanges again after expiry. Skills assume authenticated access and never request secret value.

## Compatibility

Initial skills target Horizon Discovery contract major version `1`. Skills stop and report unsupported major versions rather than guessing.
