---
name: horizon
description: Coordinate work against Horizon Platform through Discovery. Use when AI Agent must bootstrap Horizon, choose customer Installation, choose runtime or Metadata work, resume or create Workspace, carry work across sessions, or route into another Horizon skill.
compatibility: Requires Horizon CLI 1.x and Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.4.0"
---

# Horizon

Treat CLI as authenticated transport and Discovery as platform contract. Skills supply workflow, never endpoint memory. Every Business Data mutation needs explicit confirmation; complex mutations need an approved local implementation plan.

For Metadata proposals, follow **select Installation → inspect Discovery and existing Metadata → interview ↔ targeted Discovery rechecks only for unresolved decisions or substantial execution → Data Modeling → Visualization → Automation → Workspace validation**. Inspect current Installation patterns before asking what they already answer. Route to [`horizon-interview`](../horizon-interview/SKILL.md) when decisions remain, execution is substantial, or a session handoff is likely; also route unclear, broad, multi-step, bulk, relational, destructive, or cross-surface runtime work there. When a localized Metadata request is fully specified and inspection finds no conflict, proceed directly to authoring without questions or a plan file. Recheck Discovery when User answers change the model; settle layer outcomes through the request or clarification, recording `no configuration needed` only when understood, not as a substitute for unresolved meaning. Written plans follow execution workload or handoff risk, not interview depth. Recheck Discovery at each authoring layer and follow explicit User choices over defaults. `horizon-interview` owns planning and approval; `horizon-metadata-authoring` owns execution. This sequence does not govern Business Data or runtime Actions.

## Errors

The normal scenario has no errors. On any HTTP error status or CLI failure, report status and message to User and stop all Horizon requests for this run, including diagnostic reads. Never retry with a guessed variant or continue elsewhere after an error.

## Bootstrap

1. Read and follow shared [CLI installation](references/cli-installation.md) guidance. Verify compatible `horizon` before platform work.
2. Read and follow shared [Connection Profile](references/connections.md) guidance. Run checked JSON listing, obtain explicit customer Installation choice when absent, and require selected status `valid`.
3. Request Discovery through `horizon request --connection "<selected label>" GET /discovery`. Confirm current contract major version. If unsupported, stop and report mismatch. For authoring, follow the returned `authoring.href`, then the returned `structures` and `workspaces` method/href values. Copy hrefs verbatim, including their `/discovery` prefix; `/discovery/catalogs` lists catalogs, not authoring paths. If an affordance is absent, stop and report it instead of constructing a route. Use Architecture Analysis links only for an architecture audit or Ticket workflow, not to inspect existing Structures for ordinary authoring.

Completion: compatible CLI 1.x and Discovery v1 confirmed, selected Connection Profile is explicit and live-valid, current identity known, available Metadata Context and Discovery roots recorded. Selected label remains current session context and every later request carries it explicitly.

## Classify

- Business Data or Action work → follow `horizon-runtime`.
- Published Metadata architecture audit or post-Publication AMT verification → follow `horizon-architecture-analysis`.
- Structure, Field, Relation, Expression, Action definition, Data Source, Page, View, Widget, or other Metadata proposal, including implementation of selected AMT → follow `horizon-metadata-authoring`.
- Architecture guidance or explanation of configured Installation Metadata → ask User to invoke `horizon-ask-for-guidance`.

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

Overall completion: request routed, any required interview plan is approved, Connection Profile and Metadata Context explicit, next skill has current Discovery links rather than guessed routes.
