# Market Scan Template

Trigger: "market scan [TOPIC]"

Fill in the three slots below, then hand to Claude as a research prompt.

---

## Slot 1 — TOPIC (required)
What space or problem area to scan.

Examples:
- "agent observability and debugging tools"
- "vibe coding context management"
- "MCP server tooling"
- "AI-generated test frameworks"

## Slot 2 — CATEGORIES (optional, replace or keep defaults)
What types of things to look for. Default set:

1. **Existing products** — commercial tools in this space, free or paid
2. **Open-source repos** — GitHub projects solving this problem
3. **Newsletters or communities** — where people in this space gather
4. **Workarounds and hacks** — what people DIY when no good tool exists
5. **Adjacent tools** — things that partially solve it or could be extended
6. **Build-in-public projects** — people publicly working on this

Swap out any category that doesn't fit the topic.

## Slot 3 — FOCUS ANGLE (optional)
One question you most want answered. Sharpens the output.

Examples:
- "Is anything open source and worth forking?"
- "What's the most common workaround people use today?"
- "Is there a clear market leader, or is it fragmented?"
- "What would a weekend MVP look like?"

---

## Fixed output format (do not change)

For each result:
- Name + URL
- One sentence: what it does
- Open source? Y/N (+ GitHub link if yes)
- Stars or user base if known
- What's interesting or unique

Aim for 10–15 results. Flag uncertainty. Under 400 words.
Honest > complete. If results are sparse, say so — that's signal too.
