# Signal Forge — Claude Code Instructions

Signal Forge is a **public, curated dataset of AI builder signals**. Every three days a
Claude Cloud Routine scans GitHub Trending, Reddit, and Hacker News, filters for AI
builder signals, and commits a capture file to `inbox/`.

## Folder Reference

| Folder | What goes here |
|--------|----------------|
| `inbox/` | The dataset: one `YYYY-MM-DD_phase0.md` capture per run |
| `skills/` | Reader-facing skills: `shape-idea`, `deep-dive` |
| `templates/` | `idea.md` — the shape-idea output template |
| `ideas/` | Reader's local idea files (gitignored except `EXAMPLE.md`) |
| `docs/specs/` | Design documents |

## Naming Convention

- Captures: `inbox/YYYY-MM-DD_phase0.md`
- Idea files: `ideas/<slug>.md`

## Phase 1 Skills

Readers clone the repo and run these with their own agent:

- `shape-idea` — turn an `inbox/` signal into a testable `ideas/<slug>.md`.
- `deep-dive` — research a shaped idea (similar projects, reusable tools, existing
  solutions, differentiation gap) and append findings to the same file.

Skills are self-contained: no hardcoded tokens, no maintainer-private config. Reader
products stay local and do not flow back to the public dataset.

## How Captures Are Produced

The collection logic lives entirely in a Claude Cloud Routine (managed at
https://claude.ai/code/routines), **not** in this repo. The routine fetches the
sources, curates 5–10 items per section, and uploads the file via the GitHub API.

This repo is the output archive. Do not add local collection scripts or analysis
workflows unless the user explicitly asks to expand scope beyond a public dataset.
