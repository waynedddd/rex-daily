# Rex Daily — 系统文档

## 概览

Rex Daily 是一个 AI × Design / Tech 领域的每日内容系统，包含两个核心产品线：

1. **Daily Digest** — 每日新闻简报（AI × 设计 + AI × 科技）
2. **Inspiration Board** — 设计灵感看板（按方向分类的案例收集 + Rex 评论）

两者共同服务于一个前端页面（`index.html` + `inspire.html`），数据通过 Supabase 同步。

---

## 一、Daily Digest（每日简报）

### 选题逻辑

每天覆盖两个板块，每个板块一期（可追加晚间更新）：

| 板块 | section 值 | 关注领域 |
|------|-----------|---------|
| AI × 设计 | `design` | AI 设计工具（Figma/Moonchild/Stitch 等）、设计师角色变化、设计工作流、设计趋势 |
| AI × 科技 | `tech` | 大模型动态、AI Agent、开发工具、AI 伦理/政策、中国 AI 产业、企业 AI 部署 |

**选题标准：**
- 行业信号 > 产品发布 > 泛新闻
- 优先选择有深度分析的来源（Pragmatic Engineer、The Gradient、Vox 深度报道）而非 PR 稿
- 关注不同新闻之间的关联和 pattern
- 中国和海外并重

### 信息采集方法

通过 Tavily Search API 搜索以下关键词组合：
- AI design tools 2026, Figma AI, AI UX workflow
- AI news this week, LLM updates, AI agent enterprise
- AI 设计, 大模型, AI 产业（中文源）

辅以特定源的定向搜索（TechCrunch, Axios, The Hacker News, Behance, Dribbble 等）。

### 产出结构

每期 issue 是一个 JSON 对象，存入 `issues.json`（数组），结构：

```json
{
  "date": "2026-03-12",
  "section": "design" | "tech",
  "title": { "zh": "中文标题", "en": "English title" },
  "content": { "zh": "HTML 内容", "en": "HTML 内容" },
  "cover": "封面图 URL",
  "sources": [
    {
      "title": { "zh": "...", "en": "..." },
      "url": "https://...",
      "image": "og:image URL 或 null"
    }
  ]
}
```

**内容 HTML 结构（固定模板）：**
1. `<h3>📌 板块标题</h3>` — 新闻条目列表（`<ul><li>`）
2. `<h3>🔄 趋势</h3>` — 3-4 条趋势总结
3. `<div class="rex-take"><h3>🔍 Rex 的看法</h3>` — 200-400 字深度评论（**核心价值**）

**Rex's Take 写作风格：**
- 有立场，不只总结
- 把多条新闻之间的联系点出来
- 可以大胆预测，标注是推测
- 偶尔犀利幽默
- 中英双语

### 生产流程

1. **Python 脚本**（`update-YYYY-MM-DD.py`）：抓取 og:image → 构建 JSON → 追加到 `issues.json`
2. **手动/Agent 编写**：Rex（AI agent）搜索、分析、撰写内容 → 生成 Python 脚本 → 执行
3. **晚间更新**：同日可追加第二期（`update-YYYY-MM-DD-evening.py`），同一 section 会去重保留最新

### 发布频率

- **早间**：design + tech 各一期
- **晚间**（可选）：追加更新，通常补充重要后续新闻

---

## 二、Inspiration Board（灵感看板）

### 内容方向

灵感板按 4 个 direction 组织：

| ID | 名称 | 主题 |
|----|------|------|
| `finance` | AI × Finance | 金融科技 UI/Dashboard、Trust UX、可解释 AI 设计 |
| `sports` | AI × Sports | 运动健康 App、可穿戴数据可视化、AI 教练设计 |
| `cards` | Content Design | 内容排版、Editorial typography、卡片设计、信息架构 |
| `visual-ai` | Visual for AI | AI 品牌视觉、生成式标识、AI 产品界面设计 |

每个 direction 配有：
- **color** — 主题色
- **stats**（可选）— 2-3 个数据亮点
- **name_en** — 英文名

### Pin 类型

每条 pin 是一个灵感条目：

| type | 说明 |
|------|------|
| `case` | 设计案例，附图片、标签、来源链接 |
| `trend` | 趋势分析，附来源 |
| `rex-note` | Rex 的观察评论（无图片，纯文字） |

**Pin 结构：**
```json
{
  "direction": "finance",
  "type": "case",
  "title": "案例标题",
  "body": "中文描述",
  "body_en": "English description",
  "tags": ["Dashboard", "Dark UI"],
  "link": "https://dribbble.com/...",
  "linkText": "Dribbble",
  "image": "https://cdn.dribbble.com/...",
  "date": "2026-03-12"
}
```

### 采集方法

- **Dribbble / Behance** 搜索特定方向关键词
- **行业趋势报告**（WSA Design、Elementor、Spinta Digital 等）
- 手动策展 + 搜索验证

### Rex Note 写作风格

每个 direction 至少 1-2 条 `rex-note`，200-400 字：
- 跨案例归纳 pattern
- 指出设计背后的本质矛盾
- 联系不同 direction 之间的共性
- 中英双语

---

## 三、数据存储与同步

### 本地文件

| 文件 | 内容 |
|------|------|
| `issues.json` | Daily Digest 全部期刊（JSON 数组） |
| `inspire.json` | Inspiration Board 数据（directions + pins） |
| `index.html` | Daily Digest 前端页面 |
| `inspire.html` | Inspiration Board 前端页面 |

### Supabase 同步

`sync-to-supabase.mjs` 负责将本地 JSON 同步到 Supabase：

- **daily_briefs** 表 ← `issues.json`（按 date + section 去重 upsert）
- **inspire_directions** 表 ← `inspire.json` 的 directions
- **inspire_pins** 表 ← `inspire.json` 的 pins

### Git 版本管理

`rex-daily/` 目录有独立 `.git`，JSON 数据和前端页面均版本控制。

---

## 四、Memory / 日志

每次生产后在 `memory/reports/` 下生成当日摘要：

- `YYYY-MM-DD-daily.md` — 早间 digest 摘要
- `YYYY-MM-DD-evening.md` — 晚间更新摘要（如有）

格式为 Markdown，列出关键条目和趋势，供后续 session 快速回顾。

---

## 五、端到端流程总结

```
搜索（Tavily）→ 筛选 & 分析 → 撰写内容（中英双语）
    ↓
生成 Python 脚本（抓 og:image + 构建 JSON）
    ↓
执行脚本 → 追加到 issues.json / inspire.json
    ↓
node sync-to-supabase.mjs all → 同步到 Supabase
    ↓
git commit & push → 版本管理
    ↓
写入 memory/reports/ → 日志记录
```

---

## 六、内容质量标准

- **每条新闻**：必须有真实来源链接，不编造
- **Rex's Take**：不能只是复述新闻，必须有独立判断和跨新闻关联
- **双语**：所有 title、content、body 均提供中英文
- **图片**：尽量抓取 og:image，inspire pins 必须有图片（rex-note 除外）
- **去重**：同日同 section 只保留最新版本
