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

1. Call Discovery from href returned by token exchange. Confirm supported contract major version. Completion: current identity, Metadata Context, runtime root, and optional authoring root are known.
2. Classify request:
   - Business Data or Action work → follow `horizon-runtime`.
   - Published Metadata architecture audit or post-Publication AMT verification → follow `horizon-architecture-analysis`.
   - Structure, Field, Relation, Expression, Action definition, Data Source, Page, View, or other Metadata proposal, including implementation of a selected AMT → follow `horizon-metadata-authoring`.
   - Unsure which workflow fits → use `horizon-ask-for-guidance` with User.

## Workspace selection

Workspace lifetime follows one coherent review and Publication outcome, not one chat session.

Before creating Workspace:

1. Follow authoring affordance listing open Workspaces.
2. Inspect likely matches through changes, Activity, diff, review state, and label.
3. If existing Workspace may own requested outcome, ask User whether to continue it. Skip question when User explicitly named Workspace.
4. Create Workspace only when no suitable Workspace exists or User chooses separation.
5. Record meaningful label and initial Activity comment describing requested outcome.

For Agent Credentials, every Workspace-resolved request sends `Horizon-Workspace: <workspace-code>`. No header means Published metadata. Never fall back to Owner User's persisted Metadata Context.

## Continuity

- Re-discover after synchronization, conflict, Publication, or contract-version change.
- Use Workspace Activity for cross-session and cross-Agent handoff: intent, decisions, exceptional placement rationale, test Business Instances, evidence, and remaining work.
- Treat runtime and authoring authority separately. Authoring availability never implies Business Data authority.

Completion: request is routed, explicit Metadata Context is known, and next skill has current Discovery links rather than guessed routes.
