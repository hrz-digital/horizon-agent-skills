<p align="left">
  <img src="assets/horizon-logo.png" alt="Horizon" height="271">
</p>

# Horizon Agent Skills

Portable [Agent Skills](https://agentskills.io) for AI Agents operating Horizon through machine-facing Discovery. Horizon Discovery is source of truth for schemas, affordances, authorization, Metadata Context, and runtime behavior. Skills provide workflow policy, safety, and continuity; they do not replace Discovery.

## Skills

- [`horizon`](skills/horizon/SKILL.md)
- [`horizon-metadata-authoring`](skills/horizon-metadata-authoring/SKILL.md)
- [`horizon-architecture-analysis`](skills/horizon-architecture-analysis/SKILL.md)
- [`horizon-runtime`](skills/horizon-runtime/SKILL.md)
- [`horizon-ask-for-guidance`](skills/horizon-ask-for-guidance/SKILL.md) — user-invoked router

## Required setup

Horizon CLI is independent of any AI Harness. Horizon Skills work with Harnesses that support Agent Skills directly or through a compatible installer. Complete setup in this order.

1. Install Horizon CLI and verify `horizon version`.
2. Install Horizon Skills in your Harness.
3. Connect the CLI to a Horizon Installation.

### 1. Install Horizon CLI

macOS/Linux:

```sh
curl -fsSL https://platform.hrz.digital/cli/install.sh | sh
horizon version
```

Windows PowerShell:

```powershell
irm https://platform.hrz.digital/cli/install.ps1 | iex
horizon version
```

### 2. Install Horizon Skills

List available skills:

```bash
npx skills add hrz-digital/horizon-agent-skills --list
```

Install all skills globally:

```bash
npx skills add hrz-digital/horizon-agent-skills --skill '*' -g
```

### 3. Connect to a Horizon Installation

1. Open the Account Sidebar in the target Horizon Installation.
2. Create an Agent Credential.
3. Copy the one-time Connection Profile.
4. Open a separate terminal outside the AI Harness.
5. Run `horizon connection add`, paste the Connection Profile into the hidden prompt, and confirm it.
6. Return to the Agent. It can verify the non-secret profile with `horizon connection list --check --json` and ask which Installation to use.

You must personally perform steps 1–5. Never paste Connection Profile JSON or API keys into Agent chat or let the Agent run `horizon connection add`.

## Updating setup

Update Horizon CLI first, then update the Skill Set.

### Update Horizon CLI

Check whether a newer release is available:

```sh
horizon version --check
```

If an update is available, run the installer for your operating system.

macOS/Linux:

```sh
curl -fsSL https://platform.hrz.digital/cli/install.sh | sh
horizon version
```

Windows PowerShell:

```powershell
irm https://platform.hrz.digital/cli/install.ps1 | iex
horizon version
```

The installer resolves the latest release, verifies its checksum, and replaces the existing user-local executable. Stored Connection Profiles remain unchanged.

### Update Horizon Skills

Update installed Skills to latest published version:

```bash
npx skills update
```

Install this Skill Set at an exact version:

```bash
npx skills add https://github.com/hrz-digital/horizon-agent-skills/archive/refs/tags/v1.1.0.tar.gz --all -g
```

## Authentication

Horizon CLI is required authentication and transport boundary. It stores Agent Credential API keys in operating-system credential store, exchanges short-lived tokens, and sends authenticated requests. API keys and tokens never belong in Harness storage, environment variables, prompts, skills, repositories, URLs, command arguments, output, or logs.

Skills verify CLI, list live-checked non-secret Connection Profiles, require explicit customer Installation choice, and pass selected profile on every request. Shared procedure lives in [`horizon`](skills/horizon/SKILL.md).

## Compatibility

Each workflow declares supported CLI and Discovery contract majors in frontmatter. Missing or unsupported CLI or Discovery major stops platform work; Skills never guess routes, schemas, payloads, or fall back to raw credential-bearing HTTP.
