---
name: shape-idea
description: Turn a raw signal from inbox/ into a testable idea, written to ideas/<slug>.md. Use when the reader picks a signal and says "I want to build X based on this" or "shape this into an idea".
---

# shape-idea

Turn one raw signal from the public `inbox/` dataset into a structured, testable
idea file that `deep-dive` can later research.

## When to use

The reader has browsed `inbox/` and picked a signal — they paste a link/title or
say something like "I want to build X based on this". This skill captures that into
a durable `ideas/<slug>.md` file.

## Inputs

- A signal: an `inbox/` link, a title, or the reader's own one-line description.
- Optional: the reader's extra context about who they are or what they want to build.

## Steps

1. **Locate the signal.** If given a link or title, find it in `inbox/` and read the
   surrounding capture for context (source, traction, "what made me stop"). If the
   reader only gave a description, work from that and note no inbox source.

2. **Restate as a testable bet.** Compress the idea into one falsifiable sentence:
   who has what pain, and what the proposed thing does about it. Avoid vague verbs
   ("improve", "streamline"). The bet should be something evidence could later kill.

3. **Extract the core fields:**
   - **Pain / Who** — the specific pain and the specific people who have it.
   - **Proposed Shape** — the smallest thing that would test the bet.
   - **Open Questions** — what you don't yet know (feeds `deep-dive`).

4. **Pick a slug.** Short kebab-case, derived from the idea (e.g.
   `agent-bash-permission-guard`).

5. **Write `ideas/<slug>.md`** using `templates/idea.md`. Leave the `## Deep Dive`
   section empty — `deep-dive` fills it.

## Output

`ideas/<slug>.md` — a structured idea container. This is a local working file
(gitignored in this repo); it does not flow back to the public dataset.

## Rules

- Restate the reader's idea faithfully. Do not silently swap it for a different idea.
- Preserve the source URL when there is one.
- Separate what the signal shows (evidence) from what you infer.
- One clear, falsifiable bet — not a paragraph of hedges.

## Next step

Once the file exists, suggest running `deep-dive` on it.
