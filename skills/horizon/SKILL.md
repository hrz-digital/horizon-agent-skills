---
name: horizon
description: Coordinate work against Horizon Platform through Discovery. Use when AI Agent must bootstrap Horizon, choose customer Installation, choose runtime or Metadata work, resume or create Workspace, carry work across sessions, or route into another Horizon skill.
compatibility: Requires Horizon CLI 1.x and Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.0.0"
---

# Horizon

Treat CLI as authenticated transport and Discovery as platform contract. Skills supply workflow, never endpoint memory.

## Bootstrap

1. Read and follow shared [CLI installation](references/cli-installation.md) guidance. Verify compatible `horizon` before platform work.
2. Read and follow shared [Connection Profile](references/connections.md) guidance. Run checked JSON listing, obtain explicit customer Installation choice when absent, and require selected status `valid`.
3. Request Discovery through `horizon request --connection "<selected label>" GET /discovery`. Confirm current contract major version. If unsupported, stop and report mismatch; never guess routes, schemas, or payloads from memory.

Completion: compatible CLI 1.x and Discovery v1 confirmed, selected Connection Profile is explicit and live-valid, current identity known, available Metadata Context and Discovery roots recorded. Selected label remains current session context and every later request carries it explicitly.

## Classify

- Business Data or Action work → follow `horizon-runtime`.
- Published Metadata architecture audit or post-Publication AMT verification → follow `horizon-architecture-analysis`.
- Structure, Field, Relation, Expression, Action definition, Data Source, Page, View, or other Metadata proposal, including implementation of selected AMT → follow `horizon-metadata-authoring`.
- Unsure which workflow fits → ask User to invoke user-only router `horizon-ask-for-guidance`.

Completion: request classified, next skill selected, User has clear instruction when router is needed.

## Workspace selection

Workspace lifetime follows one coherent review and Publication outcome, not one chat session. Before creating Workspace:

1. Follow authoring affordance listing open Workspaces.
2. Inspect likely matches through changes, Activity, diff, review state, and label.
3. If existing Workspace may own requested outcome, ask User whether to continue it. Skip question when User explicitly named Workspace.
4. Create Workspace only when no suitable Workspace exists or User chooses separation.
5. Record meaningful label and initial Activity comment describing requested outcome.

For Agent Credentials, pass selected Connection Profile on every CLI request and Workspace context required by current Discovery on every Workspace-resolved request. With no Workspace selected, use context current Discovery identifies as Published Metadata. Resolve context explicitly; re-discover after synchronization, conflict, Publication, or contract-version change.

Use Workspace Activity for cross-session and cross-Agent handoff: intent, decisions, exceptional placement rationale, test Business Instances, evidence, remaining work. Treat runtime and authoring authority separately; authoring availability never implies Business Data authority.

Completion: after any listed event, current context is synchronized and handoff Activity records intent, decisions, evidence, remaining work.

Overall completion: request routed, Connection Profile and Metadata Context explicit, next skill has current Discovery links rather than guessed routes.
