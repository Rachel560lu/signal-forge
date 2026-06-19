---
name: deep-dive
description: Research a shaped idea (ideas/<slug>.md) across four dimensions — similar projects, reusable open-source tools, existing solutions, and the differentiation gap — and append findings to the same file. Use when the reader says "deep dive this idea".
---

# deep-dive

Take a shaped idea and research how to actually build it, appending evidence-backed
findings to the same `ideas/<slug>.md` file.

## When to use

The reader points at an `ideas/<slug>.md` (created by `shape-idea`) and asks to
research it — "deep dive this", "what's out there for this idea".

## Inputs

- An `ideas/<slug>.md` file with a filled-in bet and Proposed Shape.
- Live web access (WebSearch) and the GitHub public API.

## GitHub API token

Default: **no token needed.** The unauthenticated GitHub API allows 60 requests/hour,
which is enough for one idea's research. If you hit a rate limit (HTTP 403), tell the
reader they can optionally set a `GITHUB_TOKEN` environment variable to raise the
limit to 5000/hour, and continue with whatever results you already have.

## Steps

Research four dimensions. For each, do real searches — do not guess.

1. **Similar projects.** Search GitHub and the web for projects already doing this.
   Note maturity and activity. Judge: is this a red ocean (many mature players) or
   blue ocean (little exists)?

2. **Reusable open-source tools.** What existing libraries/frameworks would you build
   *with* to implement this fast — not compete against. Name concrete tools.

3. **Existing solutions / competitors.** How do people cope with this pain today,
   including non-software workarounds? What do current solutions miss?

4. **Differentiation gap.** Given the above, where is the seam — the underserved
   angle this idea could take? State it as an opinion, labeled as inference.

## Output

Append to the `## Deep Dive` section of the same `ideas/<slug>.md`, structured under
the four headings above. If a `## Deep Dive` already has content, update/replace it
rather than appending a duplicate.

## Rules

- Every factual claim carries a source URL.
- Separate evidence (what you found) from inference (your read of the gap).
- Do not invent competitors, star counts, traction, dates, or quotes.
- If a dimension turns up little, say so plainly ("no obvious direct competitor
  found") — do not pad with fabricated entries.

## Error handling

- **GitHub rate limit (403):** note it, suggest optional `GITHUB_TOKEN`, continue.
- **Dead source link:** proceed from the idea text, flag the source as unreachable.
