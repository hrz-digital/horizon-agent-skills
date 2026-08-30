# Horizon Skill Set

## Purpose

Horizon Skill Set makes AI Agents consistent at operating Horizon without becoming second API documentation. Any capable Agent must remain able to work from Discovery alone; skills add workflow judgment, safety, and continuity.

Platform contracts change with installation and Metadata Context. Skills therefore retrieve current affordances, JSON Schemas, catalogs, availability, and stable reasons from Discovery on every task.

## Repository boundary

Skills live in public repository separate from Horizon Core because they have independent release cadence and must install without platform source. Repository follows open Agent Skills format and distributes through GitHub, `npx skills`, and skills.sh.

Skill release declares supported Discovery contract major version. Unsupported major stops clearly rather than falling back to remembered routes or payloads.

## Skill map

```text
horizon-ask-for-guidance
       ↓ recommends
horizon
  ├── horizon-metadata-authoring
  ├── horizon-architecture-analysis
  └── horizon-runtime
```

### `horizon`

Coordinator. Bootstraps Discovery, distinguishes runtime from Metadata work, selects or resumes Workspace, and records handoff.

### `horizon-metadata-authoring`

Metadata proposal workflow. Reviews Semantic neighborhood, follows authoring schemas/catalogs, validates coherent Workspace, treats shared Business Data preview carefully, and hands every Attention acknowledgement and Publication decision to human.

### `horizon-architecture-analysis`

Published Metadata quality workflow for HSC-owned Agents. Inventories every discoverable element, verifies implemented Architectural Metadata Tickets, identifies actionable architecture concerns, and creates or updates Tickets through Discovery without changing Metadata.

### `horizon-runtime`

Business execution workflow. Acts only on behalf of Agent Credential's Owner User, follows current runtime affordances, handles confirmation and concurrency, and never infers storage or task implementation.

### `horizon-ask-for-guidance`

User-invoked router. It gives best-practice flow, Metadata Context, human gate, and next skill.

## Workspace practice

Workspace groups one coherent review and Publication outcome, not one session or one Metadata element. Before creating Workspace, Agent lists open Workspaces and inspects changes, Activity, diff, review state, and label. If one may contain requested continuation, Agent asks User unless User named it directly.

Agent always passes explicit `Horizon-Workspace` header for Workspace-resolved requests. Missing header means Published metadata and never inherits Owner User's persisted context.

Workspace Activity is durable handoff while Workspace exists. Record requested outcome, modeling decisions, confirmed Semantic exceptions, test Business Instances, validation evidence, and remaining work.

## Credential boundary

Harness owns credentials. Preferred connector reads Agent Credential API key from Harness secret storage, exchanges it through `/auth/token`, keeps Bearer token in memory, and refreshes after expiry. Skills never ask for or expose secret values.

Environment variables `HORIZON_API_URL` and `HORIZON_AGENT_API_KEY` are fallback for Harnesses without secret storage. Connector remains non-verbose and redacts authorization headers.

## Verification

Each skill should be tested against black-box Horizon journey with no Core repository access:

1. start from token exchange Discovery href;
2. identify runtime versus authoring flow;
3. resume or create Workspace correctly;
4. author and validate complete Metadata proposal;
5. stop at human Attention/review boundaries;
6. execute authorized runtime Action from current Business Instance link;
7. audit Published Metadata through discovered Architecture Analysis contracts without copying schemas or changing Metadata.

Skill tests judge decisions and observable API use, not exact prose.
