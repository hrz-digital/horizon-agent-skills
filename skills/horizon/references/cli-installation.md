# Horizon CLI installation

Horizon CLI 1.x is required transport for Horizon Skills. Check `horizon version` before any platform command. Accept only output reporting a valid semantic version with major `1`; prereleases such as `v1.0.0-beta.1` are compatible. Missing command, `dev`, malformed output, or another major is unsupported.

After confirming a supported installed version, attempt `horizon version --check --json` once per bootstrap. Treat an unsupported flag, network failure, malformed check output, or `available: false` as unavailable and continue platform work. When `available` and `updateAvailable` are true, tell the User the installed and latest versions and offer the official installer. If the User accepts, run the current operating system's installer below and verify the new version; otherwise continue current work. Never run the installer without explicit User approval.

On missing or unsupported CLI:

1. Stop platform work and ask User whether Agent may install or upgrade CLI.
2. If User refuses, report CLI requirement and stop. Never substitute raw HTTP, `curl`, another connector, or credential-bearing command.
3. After approval, run official installer for macOS/Linux: `curl -fsSL https://platform.hrz.digital/cli/install.sh | sh`. Windows PowerShell: `irm https://platform.hrz.digital/cli/install.ps1 | iex`. Installers use official `platform.hrz.digital` artifacts, verify SHA-256, install user-locally, update PATH, and verify `horizon version`. Do not use administrator access.
4. Stop after verified install. Credential import belongs User in separate terminal under [connection guidance](connections.md).

Completion: compatible Horizon CLI 1.x verified before any connection listing or platform work; one non-blocking update check attempted when supported; available update reported without automatic installation; or workflow stopped without fallback transport.
