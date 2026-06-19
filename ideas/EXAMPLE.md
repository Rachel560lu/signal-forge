# Pre-execution guard for coding-agent bash commands

> This is a sample idea file showing what `shape-idea` + `deep-dive` produce.
> It is committed as documentation; real reader ideas are gitignored.

- **Source Signal:** https://reddit.com/r/LocalLLaMA/comments/1t2uk1m/one_bash_permission_slipped/ (r/LocalLLaMA, 2092 upvotes · 359 comments)
- **One-line Bet:** Developers running coding agents will adopt a lightweight pre-execution guard that intercepts dangerous bash commands before they run, because a single mis-approved permission can wreck a working tree.
- **Pain / Who:** People who let coding agents (Claude Code, Cursor, Codex, etc.) execute shell commands. One careless approval of a destructive command (`rm -rf`, force push, credential exfil) does real damage; current per-command approval prompts cause fatigue and get rubber-stamped.
- **Proposed Shape:** A small CLI/hook that sits between the agent and the shell, classifies each command (safe / review / block) against a ruleset, and blocks or pauses on dangerous patterns — before execution, not after.
- **Open Questions:** Do agents expose a hook point to intercept commands? Is this already built into the major agents? Would a ruleset catch enough without being annoying?

## Deep Dive

<!-- Filled by the deep-dive skill. Each claim carries a source URL. -->

### Similar Projects
- Claude Code ships native permission rules and `PreToolUse` hooks that can block Bash calls — https://docs.claude.com/en/docs/claude-code/hooks — so part of this exists inside one agent already.
- Sandboxing tools like `firejail` (https://github.com/netblue30/firejail) and `bubblewrap` (https://github.com/containers/bubblewrap) constrain processes generally, but are not agent-aware.
- Read: partially red ocean *inside* Claude Code; bluer as an agent-agnostic layer.

### Reusable Open-Source Tools
- `bubblewrap` / devcontainers for the isolation layer rather than building a sandbox from scratch.
- Shell-parsing libraries (e.g. `bashlex`, https://github.com/idank/bashlex) to classify commands instead of regex-only matching.

### Existing Solutions / Competitors
- Today most people rely on the agent's built-in approval prompt or run agents in a throwaway container/VM. The gap: approval fatigue makes prompts ineffective, and full VMs are heavyweight for everyday work.

### Differentiation Gap
- *(inference)* The seam is an **agent-agnostic, rules-based pre-exec classifier** that works across Claude Code / Cursor / Codex via their hook points, focusing on a curated dangerous-command ruleset rather than full sandboxing. Differentiator: low-friction default-deny on a small set of truly destructive patterns, not blanket prompting.
