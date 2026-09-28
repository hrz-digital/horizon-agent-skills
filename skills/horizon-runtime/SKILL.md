---
name: horizon-runtime
description: Operate Horizon Business Data and execute runtime Actions through Discovery. Use listing, reading, creating, updating, deleting, restoring, relating, querying, exporting, following, or acting on Business Instances.
compatibility: Requires Horizon CLI 1.x and Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.4.0"
---

# Horizon Runtime

Agent Credential acts only on behalf of Owner User. Apply the [interview and plan gates](../horizon-interview/SKILL.md#planning-gates) before mutation; every Business Data mutation requires explicit confirmation. Resume written plans through `horizon`'s [approved-plan procedure](../horizon/SKILL.md#implement-approved-plan). Runtime-only work needs no Workspace:

```text
Agent authority = Owner User current effective authority ∩ Agent governance
```

Never impersonate another User or evaluate authorization locally.

## Enter

Run `horizon` bootstrap. Continue only with explicit live-valid Connection Profile; pass its label through `--connection` on every Discovery and runtime request.

Completion: compatible CLI and Discovery confirmed, customer Installation explicitly selected, profile status `valid`.

## Resolve operation

1. Open current runtime Discovery entry and select Published Metadata context it exposes for ordinary runtime work. Keep authoring Workspace context out of ordinary runtime requests, except for the Workspace feature validation in `horizon-metadata-authoring`.
2. Select Structure from compact Semantic summaries, then follow detail link.
3. Follow authorized runtime affordance for Business Instance CRUD, Relations, Assets, Data Sources, recovery, following, notifications, or Actions.
4. Read linked JSON Schema before constructing request. Use stable codes and runtime-provided links; never infer URL, payload, Relation Edge storage, or task implementation.

Completion: target Structure or Business Instance, current runtime affordance, required context, linked schema, and request links identified.

## Execute

1. Fetch current Business Instance state before mutation.
2. For Action, use current runtime availability and concrete execution href. Metadata Action existence does not prove availability.
3. Explain material effect and obtain explicit User intent when current affordance declares destructive impact, irreversible behavior, external side effect, or confirmation requirement.
4. Respect concurrency, idempotency, atomicity, and retry declarations.
5. Send request once through Horizon CLI with selected `--connection`. On stale state, refetch and reassess; never silently overwrite. Authentication and token refresh belong CLI transport, not skill.
6. Report result using Business Instance Display Label and stable instance code. For changes, follow [Execution and User testing](../horizon-interview/SKILL.md#execution-and-user-testing) for safe manual checks and requested adjustments; do not repeat the operation as a test.

Workspace context is where proposed Metadata gets tested. Current Discovery reports the effective Data Scope, so creation there produces Test Business Instances while Real ones stay read-only, and it publishes the supported Test operations, scope rules, and Data Scope selections: read them instead of learning them by submitting a Real identifier. Follow `horizon-metadata-authoring`'s [test scenarios](../horizon-metadata-authoring/SKILL.md#test-scenarios) for feature validation; its fixture set is confirmed like any other Business Data mutation, and it is the fallback-free path when a Test operation is unsupported or denied.

Completion: current runtime result returned or current stable denial/unavailability reason reported; required confirmation obtained; every request used explicit selected profile; no route, payload, availability, or authorization guessed; no identity impersonated.
