# Signal Forge

> A curated, public archive of AI builder signals — refreshed every three days.

Signal Forge tracks what AI builders are actually shipping, discussing, and
struggling with. Every three days it scans GitHub Trending, Reddit, and Hacker
News, keeps only the signals that matter to people building with AI, and commits
a dated capture to [`inbox/`](inbox/).

You don't have to run anything. **Just read the captures.**

## What You Get

Each file in [`inbox/`](inbox/) is one snapshot in time:

```text
inbox/YYYY-MM-DD_phase0.md
```

Every capture has three sections, with 5–10 hand-filtered items each:

- **GitHub Trending** — new AI agent frameworks, LLM tooling, MCP servers, dev tools
- **Reddit** — pain points, workflows, and tools surfacing in r/LocalLLaMA and r/ChatGPTCoding
- **Hacker News** — Show HN / Ask HN posts about AI tools, coding assistants, and agent workflows

Each item includes a link and a one-line "what made me stop" note explaining why
it's worth your attention.

## Curation Standard

Signal Forge is opinionated on purpose. The value is in what gets left out.

**Kept:** AI agents, LLMs, code generation, MCP, vibe coding, developer tools,
agent frameworks, real builder pain.

**Dropped:** games, generic web frameworks, data science notebooks, hype with no
signal, single viral posts mistaken for trends.

## How To Use It

- **Browse by date** — open the latest file in [`inbox/`](inbox/) for this week's signals.
- **Track over time** — the git history is a timeline; `git log inbox/` shows every refresh.
- **Search across captures** — `grep -ri "mcp" inbox/` to follow a theme.

## Go From Signal To Idea (Phase 1)

Reading is enough. But if a signal sparks something, the repo ships two skills your
own agent can run — clone the repo, open it in Claude Code / Cursor / Codex, and the
agent discovers them via `SKILL.md`.

```text
browse inbox/  →  pick a signal  →  shape-idea  →  deep-dive
```

- **`shape-idea`** — turn a signal into a testable idea, written to `ideas/<slug>.md`.
  > "Shape this into an idea: <paste an inbox signal>"
- **`deep-dive`** — research the idea across four dimensions (similar projects,
  reusable open-source tools, existing solutions, the differentiation gap) and append
  the findings to the same file.
  > "Deep dive ideas/<slug>.md"

Your idea files stay local (gitignored) — they don't flow back into the public
dataset. See [`ideas/EXAMPLE.md`](ideas/EXAMPLE.md) for a full walkthrough.

`deep-dive` needs no setup. It uses the unauthenticated GitHub API (60 req/hour),
which covers one idea. If you hit a rate limit, optionally set a `GITHUB_TOKEN` env
var to raise it to 5000/hour.

## How It's Made

Collection runs on a [Claude Cloud Routine](https://claude.ai/code/routines) on a
3-day cron. The routine fetches each source, applies the curation standard above,
and commits the capture via the GitHub API. There is no code in this repo to run —
the dataset *is* the product.

## Roadmap

- **Phase 0:** automated 3-day capture of raw, curated signals.
- **Phase 1 (now):** `shape-idea` + `deep-dive` skills to take any signal from feed
  to a researched idea.
- **Phase 2 (next):** synthesis across captures — `recommend-signals` (taste-based)
  and `cluster-pain` (recurring pain clusters).
