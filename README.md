# Great Ideas — AI Opportunity Radar

A local-first research workspace for tracking the AI builder landscape and developing product intuition.

## What this is

A structured folder + Claude Code workflow for turning raw AI signals into scoped product opportunities. Not a bookmark folder — a taste-building system.

**Focus areas:** AI Agents · Vibe Coding

## How it works

Open Claude Code in this directory. `CLAUDE.md` loads automatically and gives Claude the full context — no setup needed each session.

```bash
cd great-ideas
claude
```

## Workflow

### Phase 0 — Taste Building (ongoing)
Every 3 days, a script auto-fetches GitHub Trending + Reddit + HN into `inbox/`. Browse the file, fill in `What made me stop:` for anything interesting. Once a week, ask Claude to triage.

```
"triage phase 0 inbox"
```

### Market Scan — On demand
Research what already exists in a specific space before evaluating an idea.

```
"market scan [topic]"
```

### Scan Pain Points — Weekly
Find recurring themes across all collected signals.

```
"scan pain points"
```

### Evaluate an Opportunity — When ready
Deep evaluation with scorecard.

```
"evaluate this opportunity: [description]"
```

## Folder Structure

```
inbox/          raw captures, auto-fetched every 3 days
pain-points/    organized pain points by theme
opportunities/  tool ideas with feasibility notes
news/           weekly summaries
tools-research/ deep dives on specific ideas
templates/      reusable research prompts
scripts/        automation scripts
```

## Automation

`scripts/fetch_inbox.py` fetches GitHub Trending + Reddit (r/LocalLLaMA, r/ChatGPTCoding) + HN every run. Scheduled locally via launchd every 3 days.

```bash
python3 scripts/fetch_inbox.py  # run manually anytime
```

## Dependencies

```bash
pip3 install requests beautifulsoup4
```
