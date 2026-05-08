# Signal Forge — AI Opportunity Radar

## Purpose
This workspace tracks the AI landscape to find tool-building opportunities.
The workflow: collect signals → identify pain points → find gaps → evaluate ideas.

This is not a general bookmark folder. It is a taste-building workspace for collecting fresh AI builder signals, studying what is getting traction, and gradually turning repeated pain into scoped product opportunities.

## Focus Areas
- **AI Agents** — agent frameworks, orchestration, reliability, memory, tool use
- **Vibe Coding** — AI-assisted development, code generation UX, developer workflows

## Folder Structure

| Folder | What goes here |
|--------|---------------|
| `inbox/` | Raw captures: links, screenshots, quotes, Reddit threads — unprocessed |
| `pain-points/` | Organized pain points by theme, sourced from communities |
| `opportunities/` | Tool ideas derived from pain points, with feasibility notes |
| `news/` | Weekly AI news summaries, focus on agent + vibe coding space |
| `tools-research/` | Deep dives on a specific idea: market, competitors, build cost |
| `reference/` | Existing working repos kept as comparison baseline — never commit, gitignored |

## File Naming Convention
- Pain points: `pain-points/YYYY-MM-DD_topic.md`
- Opportunities: `opportunities/YYYY-MM-DD_idea-name.md`
- News: `news/YYYY-Www.md` (e.g. `2026-W19.md`)
- Research: `tools-research/idea-name.md`

## My Background
- Interested in building tools, not just researching
- Focus on things that can be prototyped fast (vibe coding friendly)
- Prefer tools with clear user pain, not solutions looking for problems

## Phase 0: Taste Building

**Goal:** Develop intuition for what's being built and why — before evaluating opportunities.
**Duration:** 4–6 weeks, or until patterns start appearing before Claude points them out.
**Cadence:** Once a week, 30 minutes.

### The ritual

Three sources, in this order:

1. **GitHub Trending** — filter by Weekly. Scan for AI / agent / LLM related repos only.
2. **Reddit** — r/LocalLLaMA + r/ChatGPTCoding, sorted by Top/Week. Look for high-comment threads.
3. **HN** — search `Show HN` or `Ask HN`, last 7 days.

### Capture format

Drop items into `inbox/` as a single file per session (`inbox/YYYY-MM-DD_phase0.md`). Each entry is three lines:

```md
## [repo name or post title]
Link:
What made me stop: (one sentence, instinct only — no analysis yet)
```

No templates, no scoring. Capture the gut reaction.

### When I ask "triage phase 0 inbox"

For each captured item, ask three questions and record the answers alongside:
1. What pain does this exist to solve?
2. Why is someone building this now and not two years ago?
3. What does the traction (stars / comments / upvotes) signal?

Keep answers short. The goal is to force the thinking, not produce a report.

### When I ask "scan phase 0"

Read all `inbox/YYYY-MM-DD_phase0.md` files. Surface:
- Themes that appear more than once
- User types that keep showing up
- "Why now" factors that repeat across different items

Output as a short list, not a report. Flag when a theme looks strong enough to graduate to a `pain-points/` file.

### Graduation

Move to Phase 1 (full Research Protocol) when: patterns start appearing before Claude points them out — that's when taste is forming.

---

## Favorite Product Pattern

One product pattern I am especially interested in: AI is used at setup time to create rules, contracts, schemas, checklists, mappings, or detectors, while the actual runtime does not need AI.

This is a lens, not a filter. In Phase 0, do not force every signal into this pattern. First notice what people are building, using, starring, complaining about, and hacking together. Apply this lens later when a repeated pain starts looking like a possible product.

The ideal product shape:
1. AI reads messy context once: forum threads, repo code, traces, docs, PR history, screenshots, logs, or user intent.
2. AI generates a structured artifact: rules, validators, tests, templates, contracts, workflows, schemas, mappings, or detectors.
3. A deterministic runtime executes the artifact repeatedly: CLI, CI, IDE extension, browser extension, GitHub Action, local service, or lightweight web app.
4. Users can inspect, edit, version, and trust the artifact.

Strong examples:
- AI-generated PR review rules executed by CI
- AI-generated agent trace failure detectors executed during agent runs
- AI-generated task contracts checked before/after coding agents work
- AI-generated tool schemas and validators for MCP/API integrations
- AI-generated extraction recipes, mappings, tests, or regression checks

Avoid opportunities where the only value is "ask an AI every time." Prefer durable artifacts that compound, but do not reject interesting Phase 0 signals just because they do not fit this pattern yet.

## Research Protocol

When asked to research "latest", "recent", "this month", "last 30 days", or similar, use current sources and record the date window explicitly.

Default research window:
- Last 30 days unless the user says otherwise.

Preferred sources for AI builder/developer pain:
- Reddit: `r/ChatGPTCoding`, `r/ClaudeAI`, `r/cursor`, `r/LocalLLaMA`, `r/AI_Agents`, `r/aiagents`, `r/ExperiencedDevs`, `r/programming`, `r/webdev`, `r/SaaS`, `r/SideProject`
- Hacker News: HN Search / Algolia, sorted by date and comments
- GitHub Issues and Discussions: AI coding tools, agent frameworks, MCP servers, observability tools, IDE extensions
- Product/community forums: Cursor Forum, Anthropic/Claude community, OpenAI community, Vercel AI, LangChain/LangGraph, LlamaIndex, AutoGen, CrewAI, browser-use
- Stack Overflow only as supplemental evidence; it is no longer the best place for fresh AI workflow pain
- X/Twitter only for trend discovery; do not treat it as strong frequency evidence by itself

Evidence rules:
- Always preserve source links.
- Record publication/post date when available.
- Separate evidence from inference.
- Do not invent citations, quotes, votes, dates, or source details.
- Do not treat one viral post as a validated market pain.
- Mark a pain as High frequency only when it appears across at least 3 independent sources or many independent comments in one high-signal thread.
- Capture representative user language, but quote sparingly and only when useful.

Search query patterns:
- `"Claude Code" "pain" OR "frustrating" OR "broken"`
- `"Cursor" "rules" OR "context" OR "agent" OR "not working"`
- `"MCP" "schema" OR "auth" OR "tool call" OR "debugging"`
- `"AI code review" "noise" OR "false positive" OR "expensive"`
- `"agent debugging" OR "tool calls" OR "observability"`
- `"AI generated tests" OR "trust AI code" OR "verify AI code"`

## Standing Instructions for Claude

### When I say "market scan [topic]"

Load `templates/market-scan.md`. Use the topic I provide to fill Slot 1.
If I add extra instructions (e.g. "focus on open source only" or "what's the workaround people use"), map them to Slot 2 or Slot 3.
Run the search and return results in the fixed output format.
Save output to `tools-research/YYYY-MM-DD_[topic]-scan.md`.

### When I drop something in inbox/
Triage it into a normalized signal. Extract the core pain point, source, user type, workaround, and opportunity hint. File it appropriately and flag if it suggests a strong product opportunity.

Use this signal format:

```md
## Signal: Short descriptive title

Source:
- URL:
- Platform:
- Date:

User type:

Raw pain:

Evidence:
- What the source directly says
- Any vote/comment/frequency clues, if visible

Current workaround:

Why it matters:

Opportunity hint:

Rule-based fit:
- What could AI generate once?
- What deterministic runtime could execute it?
- Does runtime need AI? yes/no

Confidence:
- Weak / Medium / Strong
```

### When I ask "scan pain points"
Read all files in `pain-points/`, find recurring themes, output a ranked list with frequency count and opportunity potential (High / Medium / Low).

For each theme include:
- Who feels it
- Repeated symptoms
- Representative sources
- Current workaround
- Why existing tools fall short
- Rule-based product fit
- Fastest validation test

### When I ask "scan reference/"
Read READMEs in `reference/` subfolders and compare against the idea at hand:
- Does a reference project already solve this? Where does it fall short?
- Can any code pattern or architecture be reused?
- What did these projects get right that a new tool should preserve?

### When evaluating an opportunity
Frame it as:
1. **Pain** — who feels it, how often, how badly
2. **Gap** — why doesn't a good solution exist yet
3. **Build** — can this be prototyped in a weekend? What's the stack?
4. **Edge** — why would I be well-positioned to build this

Then score it:

```md
## Opportunity Scorecard

Pain intensity: 1-5
Frequency: 1-5
Buyer clarity: 1-5
Existing workaround is bad: 1-5
Rule-based execution fit: 1-5
MVP difficulty: 1-5
Distribution path: 1-5
Competition risk: 1-5

Decision: Build now / Watch / Ignore
Confidence: Weak / Medium / Strong
```

Rule-based execution fit must answer:
- What artifact does AI generate?
- Who reviews or edits it?
- Where is it stored/versioned?
- What deterministic engine runs it?
- What inputs does the runtime need?
- What are pass/fail conditions?
- How does the user debug failures?
- Why is this better than calling an LLM every time?

An opportunity should not be marked "Build now" unless it has:
- A clear user
- A repeated pain
- A narrow first workflow
- A plausible distribution path
- A weekend-sized MVP
- At least one source-backed reason people might care

### Bias toward
- Tools that agents or vibe coders would pay for immediately
- Narrow scope, fast to ship, clear value prop
- Avoid: broad platforms, anything requiring large datasets to be useful

## File Templates

### Pain Point File

Use this structure for `pain-points/YYYY-MM-DD_topic.md`:

```md
# Pain Point: Topic

Date researched:
Research window:

## Summary

## Who Feels It

## Symptoms

## Evidence
- Source:
- Source:
- Source:

## Representative User Language

## Frequency Estimate
Weak / Medium / High, with reasoning.

## Current Workarounds

## Why Existing Solutions Fall Short

## Rule-Based Opportunity
- AI-generated artifact:
- Deterministic runtime:
- Runtime AI needed? yes/no

## Candidate Products

## Open Questions
```

### Opportunity File

Use this structure for `opportunities/YYYY-MM-DD_idea-name.md`:

```md
# Opportunity: Idea Name

Date:

## One-Line Product

## User

## Pain

## Evidence

## Gap

## Product Shape

## Rule-Based Execution Fit
- AI setup step:
- Generated artifact:
- Runtime:
- User editing/approval:
- Validation:

## MVP

## Distribution

## Competition / Alternatives

## Risks

## Fastest Validation

## Scorecard
Pain intensity:
Frequency:
Buyer clarity:
Existing workaround is bad:
Rule-based execution fit:
MVP difficulty:
Distribution path:
Competition risk:

Decision:
Confidence:
```

### Weekly News File

Use this structure for `news/YYYY-Www.md`:

```md
# AI Opportunity Radar — YYYY-Www

Date range:

## Executive Summary

## Top Signals

## Repeated Pain Points

## Notable Launches / Releases

## Forum Heat

## Opportunity Candidates

## What To Watch Next Week

## Sources
```

## Weekly Workflow

When asked to do a weekly scan:
1. Collect fresh signals from the last 7-30 days.
2. Save raw links or notes into `inbox/` if useful.
3. Normalize strong signals into pain point files.
4. Update or create opportunity files for promising ideas.
5. Produce a weekly summary in `news/YYYY-Www.md`.
6. Rank the top 3 opportunities and identify the fastest validation action for each.

## Quality Bar

- No raw idea without evidence.
- No evidence without source.
- No opportunity without a clear user.
- No "platform" ideas unless a narrow wedge is defined.
- No "AI wrapper" ideas unless the output becomes durable and reusable.
- Prefer products that can be demoed with one repo, one trace file, one PR, one browser page, or one workflow.
- Every promising idea should end with a concrete next action: landing page, prototype, GitHub Action, CLI demo, forum reply test, or manual concierge test.
