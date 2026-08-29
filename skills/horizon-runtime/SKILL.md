---
name: horizon-runtime
description: Operate Horizon Business Data and execute runtime Actions through Discovery. Use when listing, reading, creating, updating, deleting, restoring, relating, querying, exporting, following, or acting on Business Instances.
compatibility: Requires authenticated access to Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.0.0"
---

# Horizon Runtime

Agent Credential acts only on behalf of Owner User:

```text
Agent authority = Owner User current effective authority ∩ Agent governance
```

Never impersonate another User or evaluate authorization locally.

## Resolve operation

1. Call Discovery without `Horizon-Workspace`; runtime defaults to Published metadata.
2. Select Structure from compact Semantic summaries, then follow detail link.
3. Follow authorized runtime affordance for Business Instance CRUD, Relations, Assets, Data Sources, recovery, following, notifications, or Actions.
4. Read linked JSON Schema before constructing request. Use stable codes and runtime-provided links; never infer URL, payload, Relation Edge storage, or task implementation.

## Execute

1. Fetch current Business Instance state before mutation.
2. For Action, use current runtime availability and concrete execution href. Metadata Action existence does not prove availability.
3. Explain material effect and obtain explicit User intent where affordance declares destructive impact, irreversible behavior, external side effect, or confirmation requirement.
4. Respect concurrency, idempotency, atomicity, and retry declarations.
5. Send request once. On stale state, refetch and reassess; never silently overwrite. Authentication refresh belongs to Harness connector, not skill.
6. Report result using Business Instance Display Label and stable instance code.

Workspace runtime preview is exceptional: use `Horizon-Workspace` only when User explicitly asks to test proposed Metadata and acknowledges Business Data remains shared, real, and audited.

Completion: runtime-authoritative result is returned, denial/unavailability is explained from stable reason, and no operation was guessed or impersonated.
