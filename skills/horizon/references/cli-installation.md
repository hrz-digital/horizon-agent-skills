# Horizon CLI installation

Horizon CLI 1.x is required transport for Horizon Skills. Check `horizon version` before any platform command. Accept only output reporting released semantic version with major `1`; missing command, `dev`, malformed output, or another major is unsupported.

On missing or unsupported CLI:

1. Stop platform work and ask User whether Agent may install or upgrade CLI.
2. If User refuses, report CLI requirement and stop. Never substitute raw HTTP, `curl`, another connector, or credential-bearing command.
3. After approval, run official installer for macOS/Linux: `curl -fsSL https://platform.hrz.digital/cli/install.sh | sh`. Windows PowerShell: `irm https://platform.hrz.digital/cli/install.ps1 | iex`. Installers use official `platform.hrz.digital` artifacts, verify SHA-256, install user-locally, update PATH, and verify `horizon version`. Do not use administrator access.
4. Stop after verified install. Credential import belongs User in separate terminal under [connection guidance](connections.md).

Completion: released Horizon CLI 1.x verified before any connection listing or platform work, or workflow stopped without fallback transport.
