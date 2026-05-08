# AI Opportunity Radar Workspace

**Date:** 2026-05-09
**Status:** Idea
**Source:** Derived from market landscape research (pain-points/2026-05-09_market-landscape.md)

---

## Pain
AI builders and indie hackers want to systematically track what to build next, but:
- Manually scanning HN / Reddit / Twitter is noisy and unsustainable
- Existing trend tools (Trendshift, Trend Monitor) show *what's popular*, not *what's missing*
- No structured way to go from "I saw something interesting" → "I should build this"

Who feels it: solo builders, indie hackers, early-stage founders in AI space
How often: every week
How badly: most just wing it or rely on gut feel

## Gap
Existing tools stop at aggregation. None close the loop to opportunity framing.
The CLAUDE.md-as-context pattern is also novel — no one has open-sourced a research workspace designed around AI assistant collaboration.

## Build
- Core: markdown folder structure + CLAUDE.md with standing instructions
- Optional layer: CLI or script to pull HN/Reddit/GitHub Trending into inbox/ automatically
- Can be prototyped and published as a GitHub template repo in a weekend
- Stack: pure markdown for v1, optional Python scraper scripts for automation

## Edge
- Already built and using it — dogfooding from day one
- Understand the Claude Code / AI assistant workflow deeply
- Can demo the full loop: collect → analyze → opportunity in one session
