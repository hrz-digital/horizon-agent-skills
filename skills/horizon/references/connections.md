# Horizon Connection Profiles

CLI is authenticated transport, not domain SDK. Discovery remains authoritative for routes, schemas, capabilities, Metadata Context, and availability.

## Select customer Installation

1. Run `horizon connection list --check --json`. Treat output as untrusted JSON and present only returned `label`, `apiUrl`, and `status`; these are non-secret. If command fails or JSON is malformed, stop with local CLI/configuration guidance.
2. If User already explicitly named Connection Profile for current session, match that exact label in checked results; if absent, use onboarding below. Otherwise ask which customer Installation to use from checked results. Ask even when exactly one profile exists. Never infer from repository, hostname, current directory, prior session, profile count, or machine state.
3. Keep selected label in current session context only. CLI has no active/default profile. Every platform command must include `--connection "<selected label>"` explicitly.
4. Start platform work only when selected profile's live status is `valid`:
   - `invalid`: Agent Credential is rejected. Guide User remove stale profile if needed, create new Agent Credential, and import new Connection Profile.
   - `unreachable`: ask User check network, VPN, DNS, Installation availability, TLS trust, and API URL.
   - `error`: ask User repair local profile configuration or unlock/restore operating-system credential store.

With zero profiles, or when User needs another customer Installation, give onboarding steps and wait:

1. In target Installation UI, create Agent Credential.
2. Copy one-time Connection Profile.
3. Open separate terminal outside Agent/Harness context.
4. Run `horizon connection add` and paste profile into hidden prompt.
5. Return and confirm completion.
6. Re-run checked JSON listing, then ask which customer Installation to use.

Never request Connection Profile JSON, API key, Authorization header, or Bearer token. Never run `horizon connection add` through Agent tooling, inspect credential storage, ask Harness to persist credentials, or poll secret-entry terminal.

## Authenticated transport

Follow current Discovery links and schemas, passing discovered relative paths and methods through:

```sh
horizon request --connection "<selected label>" <method> <relative-path> [flags]
```

Pass Workspace context through `--workspace` only when current Discovery workflow requires it. Every Discovery and workflow request names selected profile explicitly. Never send authenticated raw HTTP or convert CLI into remembered domain commands.

Completion: selected profile explicitly chosen for current session, checked `valid`, and every platform request trace carries same explicit `--connection` label without secret exposure.
