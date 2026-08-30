---
name: horizon
description: Coordinate work against Horizon Platform through Discovery. Use when an AI Agent must bootstrap Horizon, choose between runtime and Metadata work, resume or create a Workspace, carry work across sessions, or route into another Horizon skill.
compatibility: Requires authenticated access to Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.0.0"
---

# Horizon

Treat Discovery as platform contract. Skills supply workflow, never endpoint memory.

## Bootstrap

1. Follow the Discovery link returned by the authenticated connector and confirm current contract major version. If the major version is unsupported, stop and report the mismatch; do not guess routes, schemas, or payloads from memory. Completion: supported major version confirmed, current identity known, and available Metadata Context and Discovery roots recorded.
2. Classify request:
   - Business Data or Action work → follow `horizon-runtime`.
   - Published Metadata architecture audit or post-Publication AMT verification → follow `horizon-architecture-analysis`.
   - Structure, Field, Relation, Expression, Action definition, Data Source, Page, View, or other Metadata proposal, including implementation of a selected AMT → follow `horizon-metadata-authoring`.
   - Unsure which workflow fits → ask User to invoke the user-only router `horizon-ask-for-guidance`.

Completion: request classified and next skill selected, or User has a clear instruction to invoke the router.

## Workspace selection

Workspace lifetime follows one coherent review and Publication outcome, not one chat session.

Before creating Workspace:

1. Follow authoring affordance listing open Workspaces.
2. Inspect likely matches through changes, Activity, diff, review state, and label.
3. If existing Workspace may own requested outcome, ask User whether to continue it. Skip question when User explicitly named Workspace.
4. Create Workspace only when no suitable Workspace exists or User chooses separation.
5. Record meaningful label and initial Activity comment describing requested outcome.

For Agent Credentials, pass the Workspace context required by current Discovery on every Workspace-resolved request. When no Workspace is selected, use the context current Discovery identifies as Published Metadata. Resolve context explicitly; never fall back to Owner User's persisted Metadata Context.

Completion: Workspace choice is explicit, required context is selected through current Discovery, and initial Activity is recorded for a new Workspace.

## Continuity

- Re-discover after synchronization, conflict, Publication, or contract-version change.
- Use Workspace Activity for cross-session and cross-Agent handoff: intent, decisions, exceptional placement rationale, test Business Instances, evidence, and remaining work.
- Treat runtime and authoring authority separately. Authoring availability never implies Business Data authority.

Completion: after any listed event, current context is synchronized and handoff Activity records intent, decisions, evidence, and remaining work.

Overall completion: request routed, Metadata Context explicit, and next skill has current Discovery links rather than guessed routes.
