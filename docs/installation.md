# Installation

Install the `success` runtime pack from the independently versioned
`gabros20/success-skill` repository.

## Prerequisites

- An Agent Skills-compatible client.
- No skill-specific credentials or tools are required. `success` is tool-agnostic: it names which
  class of system a job touches (a help-desk/ticketing tool, a health-score or CDP platform, a
  support-bot framework) and recommends re-verifying current pricing, licensing, and vendor claims
  at analysis time, but ships no keys and requires no fixed toolchain.

## Install with skills.sh

```bash
npx skills add gabros20/success-skill
```

## Clone and install

```bash
git clone https://github.com/gabros20/success-skill.git
cd success-skill
./install.sh codex
```

Available targets:

| Argument | Destination |
|---|---|
| `codex` | `${CODEX_HOME:-$HOME/.codex}/skills/success/` |
| `agents` | `~/.agents/skills/success/` |
| `claude` | `~/.claude/skills/success/` |
| `cursor` | `~/.cursor/skills/success/` |
| `antigravity` | Gemini IDE and Antigravity CLI skill paths |
| `opencode` | `~/.config/opencode/skills/success/` |
| `grok` | `~/.grok/skills/success/` |
| `hermes` | `~/.hermes/skills/success/` |
| `all` | Claude, Codex, and the cross-agent path |

The installer stages a complete copy before replacing an existing installation. If replacement
fails, it restores the previous copy.

## Verify

Start a new client session and use the client's supported invocation form:

- Codex: `$success`
- Slash-command clients: `/success`
- Other clients: an `@` mention, skill tool, or natural-language trigger

For Codex, verify the installed files directly:

```bash
test -f "${CODEX_HOME:-$HOME/.codex}/skills/success/SKILL.md"
```

## Update

```bash
cd success-skill
git pull --ff-only
./install.sh codex
```

Review `CHANGELOG.md` and GitHub Releases for version history. Version metadata intentionally stays
outside runtime `SKILL.md`.

## Uninstall

```bash
rm -rf "${CODEX_HOME:-$HOME/.codex}/skills/success"
```
