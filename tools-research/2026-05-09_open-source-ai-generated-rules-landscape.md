# Open-Source Landscape: AI-Generated Rules, Deterministic Runtime

Date researched: 2026-05-09
Research window: Current landscape, with emphasis on projects active or visible in 2025-2026.

## Thesis

There is already meaningful open-source activity around the pattern:

> AI helps create a durable artifact; deterministic software executes or enforces it later.

The market is not empty. The strongest existing clusters are:
- AI coding workflow harnesses
- Natural-language test generation
- Agent runtime policy/governance
- LLM output validation and schema enforcement
- Static analysis / code transformation recipe engines
- Agent skill/rule generation

The most crowded area is agent runtime governance. The least saturated opportunity still appears to be repo/team-specific developer workflow rules: PR review rules, AI-generated CI checks, task contracts, and agent trace rule mining.

## 1. AI Coding Workflow Harnesses

### Archon

Source:
- https://github.com/coleam00/Archon
- https://archon.diy/

What it does:
- Open-source workflow engine for AI coding agents.
- Encodes development processes as YAML DAG workflows.
- Mixes AI nodes with deterministic nodes such as bash scripts, tests, validation gates, git operations, and approval gates.
- Works with Claude Code SDK and Codex SDK.

Fit with thesis:
- Strong.
- Artifact: YAML workflow.
- Runtime: Archon workflow engine.
- AI still participates during workflow nodes, but the sequence, gates, isolation, and validation are deterministic.

What this validates:
- Developers want repeatable AI coding workflows.
- "Make AI coding deterministic and repeatable" is already a clear positioning.

Gap / opportunity:
- Archon is process-level orchestration. There is still room for tools that generate repo-specific rules/checks/contracts that run inside CI or pre-merge review.

## 2. Natural-Language Test Generation

### Assrt

Source:
- https://assrt.ai/
- https://assrt.ai/how-it-works

What it does:
- Open-source AI framework for web app testing.
- Discovers user flows, generates real Playwright TypeScript tests, and can self-heal selectors.
- Positions itself around deterministic output: AI generates the test once, then standard Playwright runs it.

Fit with thesis:
- Very strong.
- Artifact: Playwright test files and discovery reports.
- Runtime: Playwright + CI.
- Runtime does not need the original AI generation loop for normal test execution.

What this validates:
- "AI writes durable tests that you own" is a strong version of the thesis.
- Git-native, reviewable, diffable artifacts are a meaningful trust mechanism.

Gap / opportunity:
- Similar approach could be applied beyond browser tests: PR rules, API contract checks, agent trace checks, MCP tool-call validators.

### Shortest

Source:
- https://shortest.com/

What it does:
- Open-source natural-language testing tool built on Playwright.
- Users write tests in plain English and AI handles execution/implementation.

Fit with thesis:
- Medium.
- It is close to natural-language test authoring, but it appears more AI-in-the-loop during execution than Assrt's "generate real Playwright code you own" positioning.

Gap / opportunity:
- The more durable-artifact approach may be easier for developers to trust than persistent AI execution.

### Passmark

Source:
- https://passmark.dev/

What it does:
- Open-source Playwright library for AI regression testing.
- Natural-language steps via Playwright, caching, auto-healing, multi-model assertion verification.

Fit with thesis:
- Medium.
- Uses Playwright and structured steps, but AI appears closer to the runtime path than static generated tests.

Gap / opportunity:
- Demonstrates demand for test maintenance and AI regression tooling, but leaves room for more deterministic, generated-artifact-first designs.

## 3. Agent Runtime Policy / Governance

### Sponsio

Source:
- https://sponsio.dev/

What it does:
- Runtime contract enforcement for AI agents.
- Users write natural-language policies; Sponsio compiles them into deterministic contracts using formal logic/automata and enforces at tool-call time.
- Apache-2.0, v0.1.0 alpha according to site.

Fit with thesis:
- Extremely strong.
- Artifact: deterministic agent contract.
- Runtime: in-process enforcement engine.
- Claims zero LLM in the hot path.

What this validates:
- The "natural language in, deterministic enforcement out" idea is already becoming a category.
- Agent tool-call governance is a hot area.

Gap / opportunity:
- Agent security/governance may become crowded fast.
- More specific developer-facing wedges may be easier: "contracts for Claude/Codex PR work", "repo-safe shell/file policies", "MCP schema contract generator".

### Actra

Source:
- https://actra.dev/

What it does:
- AI agent governance and in-process policy engine.
- Site positioning: generate policies with Claude, enforce with Actra.
- Deterministic runtime decisions with no server/latency dependency.

Fit with thesis:
- Very strong.
- Artifact: policy.
- Runtime: in-process policy evaluator.

Gap / opportunity:
- Similar to Sponsio; broad governance may be crowded.
- A narrow vertical with concrete defaults could beat a broad policy platform.

### Runtime Guard

Source:
- https://runtime-guard.ai/

What it does:
- Open-source tool that enforces security policies on AI agent actions.
- Focuses on file operations, shell commands, destructive actions, backups, approvals, and activity logs.
- Works with Claude Desktop, Cursor, Codex, and MCP-compatible clients.

Fit with thesis:
- Strong.
- Artifact: user rules/policy.
- Runtime: local enforcement on agent actions.

Gap / opportunity:
- Strong signal that agent action interception is real.
- Differentiation likely needs rule generation, repo-specific defaults, audit summaries, or developer workflow integration.

### DashClaw

Source:
- https://www.dashclaw.io/

What it does:
- Open-source AI governance runtime / policy firewall for AI agents.
- Intercepts agent intent before production actions.
- Self-hosted with Node + Python SDKs.

Fit with thesis:
- Strong.
- Artifact: policy.
- Runtime: interception layer.

Gap / opportunity:
- Again points to governance category crowding.

### TrapDefense

Source:
- https://trapdefense.com/

What it does:
- Runtime security for MCP servers and AI agents.
- Policy checks at tool execution time, PII redaction, audit logs, MCP adapter.

Fit with thesis:
- Strong.
- Artifact: policy file.
- Runtime: SDK guard around tools.

Gap / opportunity:
- MCP-specific runtime guardrails are emerging. Opportunity may be in generated per-tool schemas/policies from existing MCP server code.

### Microsoft Agent Governance Toolkit

Source:
- https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/

What it does:
- Microsoft open-source runtime security/governance toolkit for AI agents.
- Motivated by agent autonomy and OWASP Agentic Top 10 risks.

Fit with thesis:
- Strong as a runtime governance baseline.

Gap / opportunity:
- If large vendors enter agent governance, small tools need a sharp wedge: local-first, repo-specific, dev workflow-specific, or plugin-native.

## 4. LLM Output Schema / Guardrails

### Guardrails AI

Source:
- https://github.com/guardrails-ai/guardrails

What it does:
- Open-source framework for LLM input/output guards.
- Validates structure, type, and quality of LLM outputs.
- Guardrails Hub provides composable validators.

Fit with thesis:
- Medium to strong.
- Artifact: validators/guards/schemas.
- Runtime: validation engine.
- Often still wraps LLM calls and can re-ask the LLM, so not always "no AI at runtime."

Opportunity implication:
- Schema/validator ecosystems are proven.
- There may be room for "generate validators from app examples/API docs/traces, then run them without LLM."

### Instructor

Source:
- https://github.com/567-labs/instructor

What it does:
- Open-source library for reliable structured LLM outputs using Pydantic.
- Defines response models and validates/retries outputs.

Fit with thesis:
- Medium.
- Artifact: Pydantic model.
- Runtime: validation + retry around LLM.

Opportunity implication:
- Developers already accept schema-first LLM workflows.
- Good baseline for any product that turns fuzzy input into typed artifacts.

### TypeChat

Source:
- https://github.com/microsoft/TypeChat

What it does:
- Microsoft open-source library for building natural-language interfaces using types.
- Replaces prompt engineering with schema engineering.

Fit with thesis:
- Medium.
- Artifact: TypeScript/Python types representing intents.
- Runtime: model maps natural language to typed intent; app executes typed structures.

Opportunity implication:
- "Schema engineering" is a recognized framing.
- For this workspace, a better framing may be "rule engineering" or "contract engineering."

## 5. Static Rules / Code Transformation Engines

These are not necessarily AI-generated, but they are the strongest deterministic runtimes to study.

### Semgrep

Source:
- https://github.com/semgrep/semgrep

What it does:
- Open-source static analysis engine.
- Rules look like source code.
- Runs in IDE, pre-commit, and CI.
- Used to find bugs, enforce standards, and codify project-specific knowledge.

Fit with thesis:
- Strong runtime, weak AI-generation component.
- Artifact: Semgrep rules.
- Runtime: Semgrep CLI/CI/IDE.

Opportunity implication:
- A product could use AI to generate Semgrep rules from team guidelines, PR review history, bug reports, or code examples.
- Semgrep already proves that developers will run deterministic code rules in CI.

### OpenRewrite

Source:
- https://docs.openrewrite.org/
- https://github.com/openrewrite/rewrite

What it does:
- Open-source automated refactoring ecosystem.
- Uses recipes to make repeatable, large-scale source code changes.
- Recipes operate on Lossless Semantic Trees and are composable/testable.

Fit with thesis:
- Strong runtime, weak AI-generation component.
- Artifact: OpenRewrite recipe.
- Runtime: OpenRewrite engine and build tool plugins.

Opportunity implication:
- AI-generated or AI-assisted recipes for repo-specific migrations could be valuable.
- A narrower version: "describe migration in English; generate tested OpenRewrite recipe."

### GoRules

Source:
- https://gorules.io/open-source

What it does:
- Open-source rules engine with Rust core and SDKs for several languages.
- Evaluates decision tables and business rules.

Fit with thesis:
- Strong generic deterministic runtime.
- Artifact: rules/decision tables.
- Runtime: embedded rules engine.

Opportunity implication:
- Useful baseline if building a generic "AI generates rules, app enforces rules" tool, but developer workflow wedges need domain-specific integrations.

## 6. Agent Skill / Rule Generation

### SkilldoAI

Source:
- https://skilldoai.com/

What it does:
- Open-source developer tools around AI coding reliability.
- Skilldo automatically generates validated `SKILL.md` agent rules for open-source libraries.
- It emphasizes locally executed/validated code patterns.

Fit with thesis:
- Very strong.
- Artifact: validated `SKILL.md` guidance and code patterns.
- Runtime: coding agents consume the skill; validation happens locally during generation.

Opportunity implication:
- This is close to the same thesis for agent skills.
- Differentiation should avoid "generate generic skills" and focus on a narrower, high-value artifact: repo rules, CI rules, trace contracts, PR review checks.

### AI Agent Skills

Source:
- https://github.com/skillcreatorai/Ai-Agent-Skills

What it does:
- Open-source installer/repository for portable AI agent skills across Claude Code, Cursor, Codex, Copilot, Gemini CLI, and others.

Fit with thesis:
- Medium.
- Artifact: skill packages.
- Runtime: AI agents use skills as guidance, not deterministic execution.

Opportunity implication:
- Skills are becoming a distribution format.
- Any generated-rule product should consider exporting to `SKILL.md`, `AGENTS.md`, `.cursor/rules`, or Codex skills.

### SkillX / SkillClaw

Sources:
- https://github.com/zjunlp/SkillX
- https://github.com/AMAP-ML/SkillClaw

What they do:
- Research/open-source systems that extract, evolve, or reuse agent skills from experience/session data.

Fit with thesis:
- Medium.
- They generate reusable agent knowledge, but the runtime often remains agent-guidance-heavy rather than deterministic enforcement.

Opportunity implication:
- There is active interest in distilling experience into reusable artifacts.
- The stronger product angle is to distill experience into artifacts that non-AI runtimes can enforce.

## Market Map

| Category | Open-source examples | Artifact | Runtime | Crowding |
|---|---|---|---|---|
| AI coding workflow harness | Archon | YAML workflow | Workflow engine + AI nodes + deterministic nodes | Medium |
| Web test generation | Assrt, Shortest, Passmark | Playwright tests / NL test specs | Playwright / CI | Medium |
| Agent policy governance | Sponsio, Actra, Runtime Guard, DashClaw, TrapDefense, Microsoft Agent Governance Toolkit | Policies/contracts | Tool-call enforcement | High |
| LLM output validation | Guardrails AI, Instructor, TypeChat | Schemas/validators/types | Validation/parsing layer | High |
| Static code rules | Semgrep | Static analysis rules | CLI/CI/IDE | Mature |
| Code transformation recipes | OpenRewrite | Refactoring recipes | Rewrite engine | Mature |
| Agent skills | SkilldoAI, AI Agent Skills, SkillX, SkillClaw | SKILL.md / skill library | Agent guidance | Medium |

## Opportunity Gaps

### 1. AI-generated team-specific PR rule checker

Why it is still open:
- Semgrep provides runtime.
- AI reviewers provide comments.
- But a tool that learns from a team's PR history/guidelines and emits deterministic review rules is less obvious in the open-source landscape.

Artifact:
- `review-rules.yaml`
- Semgrep rules
- test-required mappings
- forbidden-change patterns
- PR checklist contracts

Runtime:
- GitHub Action / pre-commit / CLI.

Why it fits:
- AI only generates/updates rules.
- CI enforces rules without AI.

### 2. Agent trace rule miner

Why it is still open:
- Governance tools enforce policies, but fewer tools mine failed traces and generate detectors.

Artifact:
- loop detectors
- missing tool precondition rules
- schema mismatch rules
- "tool called without prior approval" temporal contracts

Runtime:
- Local trace checker, OpenTelemetry processor, or agent middleware.

Why it fits:
- AI analyzes messy traces once.
- Runtime checks future traces deterministically.

### 3. MCP/API tool schema contract generator

Why it is still open:
- MCP governance tools are emerging.
- But generating high-quality per-tool schemas, validators, mocks, and failure classifications from existing server code/docs is a narrower wedge.

Artifact:
- JSON Schema/Zod/Pydantic validators
- mock fixtures
- tool descriptions
- allow/deny policy defaults

Runtime:
- MCP middleware / CI / test suite.

Why it fits:
- AI helps derive contracts.
- Tool calls are validated deterministically.

### 4. Prompt-to-task-contract for coding agents

Why it is still open:
- Archon provides workflow structure.
- Coding agents still often receive ambiguous one-off tasks.

Artifact:
- task contract: scope, allowed files, forbidden behavior, validation gates, done criteria.

Runtime:
- CLI hook, Codex/Claude skill, PR checker, or local task runner.

Why it fits:
- AI turns fuzzy request into a contract.
- The contract is checked before/after implementation.

## Takeaways

1. The thesis is validated. Many projects now position around "deterministic", "rules", "contracts", "policies", "schemas", or "generated code you own."
2. Agent runtime governance is crowded. Competing directly as a generic policy engine is risky.
3. Testing is also active, especially Playwright + AI.
4. Mature deterministic runtimes already exist: Semgrep, OpenRewrite, Playwright, CI, rules engines.
5. Stronger opportunities may come from generating artifacts for these existing runtimes rather than building a new runtime.
6. The best wedge is likely developer-specific and narrow: PR review rules, trace detectors, MCP tool contracts, or task contracts.

## Recommended Next Research

1. For PR rule checker: search GitHub Issues and Reddit for "AI code review noise", "Semgrep custom rules hard", "team coding standards CI".
2. For trace rule miner: search "agent debugging", "tool call observability", "LangSmith traces", "OpenTelemetry agents".
3. For MCP contract generator: search "MCP schema mismatch", "tool call validation", "MCP server testing".
4. For task contracts: search "Claude Code prompt not following instructions", "Cursor rules not followed", "agent skipped tests".
