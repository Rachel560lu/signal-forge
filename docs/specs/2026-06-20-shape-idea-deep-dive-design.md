# Signal Forge Phase 1 — `shape-idea` + `deep-dive` 设计文档

> 日期:2026-06-20
> 状态:已批准设计,待写实现计划

## 背景

Signal Forge 是一个公开的 AI builder 信号数据集:一个 Claude Cloud Routine 每三天
扫描 GitHub Trending / Reddit / Hacker News,把策展后的信号写入 `inbox/`。这部分
(Phase 0)由维护者私下运行,读者只消费 `inbox/` 的公开成果。

本文档定义 **Phase 1**:在公开数据之上提供一套**技能工具箱**,让 clone 仓库的读者
用自己的 agent 完成"挑想法 → 深挖"的核心漏斗。读者的产物留在本地,不回流公开仓库。

## 目标

打通核心漏斗的最小可行版本:

```
读者翻 inbox/  →  选中一条信号
      ↓  shape-idea
把信号复述成可验证的想法,落成 ideas/<slug>.md
      ↓  deep-dive
联网研究,把结果追加进同一个文件
```

非目标(留给之后的 Phase):`recommend-signals`(基于 taste 的个性化推荐)、
`cluster-pain`(痛点聚类)。

## 架构

仓库分两层:

```
维护者维护(自动):
  • Phase 0 cloud routine → inbox/   公开数据
  • skills/                          公开工具

读者 clone 后本地跑:
  • 用 skills + inbox 完成 shape-idea / deep-dive
  • 产物留在本地 ideas/(gitignore),不回流
```

技能必须**自包含**:输入只依赖 `inbox/`(公开)和读者本地产物;不硬编码任何 token;
不假设特定 agent(Claude Code / Cursor / Codex 都能读 `SKILL.md`)。

## 组件

### Skill 1:`shape-idea`

**位置**:`skills/shape-idea/SKILL.md`

**触发**:读者贴一条 inbox 信号的链接/标题,或说"我想基于这个做 X"。

**行为**:
1. 把信号复述成**一句可验证的赌注**。
2. 抽取:痛点是什么、谁有这个痛、提议做的东西。
3. 用 `templates/idea.md` 写入 `ideas/<slug>.md`。

**产出文件结构** `ideas/<slug>.md`:
```markdown
# <想法标题>
- Source Signal: <inbox 链接>
- One-line Bet: <一句可验证的话>
- Pain / Who: <痛点 + 人群>
- Proposed Shape: <要做的东西>
- Open Questions: <待解的问题>

## Deep Dive
<!-- 留空,由 deep-dive 填 -->
```

**依赖**:读 `inbox/`;写 `ideas/`。

### Skill 2:`deep-dive`

**位置**:`skills/deep-dive/SKILL.md`

**触发**:读者指向一个 `ideas/<slug>.md`,说"深挖这个"。

**行为**(四个研究维度,联网搜):
1. **相似项目** — GitHub 上谁在做,判断红海/蓝海。
2. **可复用开源工具** — 实现这个想法,哪些现成库/框架最合适。
3. **现有方案/竞品** — 这个痛点现在大家怎么凑合解决。
4. **差异化缝隙** — 现有方案的空隙,能切哪个角。

**工具**:WebSearch + GitHub 公开 API。

**GitHub API token**:默认**不带 token**(未认证 60 次/小时,深挖单个想法够用)。
读者若撞到速率限制,可选配 `GITHUB_TOKEN` 环境变量提到 5000 次/小时。文档说明,
不强制。

**产出**:追加到同一个 `ideas/<slug>.md` 的 `## Deep Dive` 段。

**证据规则**(沿用项目既有标准):
- 每条结论保留源 URL。
- 区分证据与推断。
- 不编造竞品、数据、traction 或引用。

**依赖**:读 `ideas/<slug>.md`;联网;写回同一文件。

## 数据流

```
inbox/<date>_phase0.md ──read──▶ shape-idea ──write──▶ ideas/<slug>.md
                                                            │
                                          ┌─────read────────┘
                                          ▼
 idea + WebSearch + GitHub API ──▶ deep-dive ──append──▶ ideas/<slug>.md (## Deep Dive)
```

## 仓库结构

```
inbox/                     公开数据(Phase 0,不动)
skills/
  shape-idea/SKILL.md
  deep-dive/SKILL.md
templates/idea.md          shape-idea 用的模板
ideas/                     读者本地工作区(gitignore)
ideas/EXAMPLE.md           一个走完整流程的样例(commit)
docs/specs/                设计文档
CLAUDE.md / README.md       指向 skills,便于任何 agent 发现
```

`.gitignore` 规则:忽略 `ideas/` 下除 `EXAMPLE.md` 之外的所有文件。

## 错误处理 / 边界情况

- **信号链接失效**:shape-idea 仍以读者提供的标题/描述继续,标注源不可达。
- **GitHub 速率限制**:deep-dive 命中 403/限制时,提示读者可配 `GITHUB_TOKEN`,
  并用已取得的结果继续,不中断。
- **deep-dive 找不到相似项目**:如实说明"未发现明显竞品",不编造。
- **重复 deep-dive**:再次深挖同一文件时,覆盖/更新 `## Deep Dive` 段而非重复追加。

## 验收标准

- 读者能从一条 inbox 信号跑 `shape-idea`,得到结构完整的 `ideas/<slug>.md`。
- 读者能对该文件跑 `deep-dive`,`## Deep Dive` 段被四个维度的、带源链接的研究填充。
- 全程零配置即可运行(无需 token)。
- `ideas/EXAMPLE.md` 展示一个走完整流程的真实样例。
- 任何能读 `SKILL.md` 的 agent 都能发现并执行这两个技能。

## 之后的 Phase(非本次范围)

- `recommend-signals`:读 taste + inbox,推荐最契合的信号。
- `cluster-pain`:把反复出现的痛点归组。
