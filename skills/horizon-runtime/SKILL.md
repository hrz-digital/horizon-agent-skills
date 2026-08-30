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

1. Open the current runtime Discovery entry and select the Published Metadata context it exposes for ordinary runtime work. Keep authoring Workspace context out of ordinary runtime requests.
2. Select Structure from compact Semantic summaries, then follow the detail link.
3. Follow the authorized runtime affordance for Business Instance CRUD, Relations, Assets, Data Sources, recovery, following, notifications, or Actions.
4. Read the linked JSON Schema before constructing a request. Use stable codes and runtime-provided links; never infer URL, payload, Relation Edge storage, or task implementation.

Completion: target Structure or Business Instance, current runtime affordance, required context, linked schema, and request links are identified.

## Execute

1. Fetch current Business Instance state before mutation.
2. For Action, use current runtime availability and concrete execution href. Metadata Action existence does not prove availability.
3. Explain the material effect and obtain explicit User intent when the current affordance declares destructive impact, irreversible behavior, external side effect, or a confirmation requirement.
4. Respect concurrency, idempotency, atomicity, and retry declarations.
5. Send request once. On stale state, refetch and reassess; never silently overwrite. Authentication refresh belongs to Harness connector, not skill.
6. Report result using Business Instance Display Label and stable instance code.

Workspace runtime preview is exceptional. Use it only when User explicitly asks to test proposed Metadata, through the current Discovery context mechanism, and after explaining that Business Data remains shared, real, and audited.

Completion: current runtime result is returned, or current stable denial/unavailability reason is reported; required confirmation was obtained; no route, payload, availability, or authorization was guessed, and no identity was impersonated.
