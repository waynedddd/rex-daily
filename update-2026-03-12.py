# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import json, urllib.request, re, html

def fetch_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', data, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data, re.I)
        return html.unescape(m.group(1)) if m else None
    except:
        return None

# Fetch og:images for key sources
urls = {
    "moonchild_medium": "https://medium.muz.li/moonchild-ai-vs-uizard-vs-figma-make-the-ux-design-tool-that-wins-in-2026-2bc509a12555",
    "uxplanet": "https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345",
    "pragmatic": "https://newsletter.pragmaticengineer.com/p/ai-tooling-2026",
    "codex_security": "https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html",
    "codex_fortune": "https://fortune.com/2026/03/04/openai-codex-growth-enterprise-ai-agents/",
    "qwen_agent": "https://aiagentstore.ai/ai-agent-news/daily/2026-03-07",
    "faros": "https://www.faros.ai/blog/best-ai-coding-agents-2026",
}

print("Fetching og:images...")
images = {}
for k, u in urls.items():
    img = fetch_og_image(u)
    images[k] = img
    print(f"  {k}: {img}")

design_issue = {
    "date": "2026-03-12",
    "section": "design",
    "title": {
        "zh": "Moonchild AI 崛起挑战 Figma · AI 设计工具分裂为「灵魂派」与「系统派」· Anthropic 把 Figma 搬进对话框",
        "en": "Moonchild AI Challenges Figma · AI Design Tools Split Into 'Soul' vs 'System' Camps · Anthropic Brings Figma Inside the Chat"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Moonchild AI 崛起：高保真「情绪驱动」设计挑战 Figma Make</strong> — 多篇深度横评显示，Moonchild AI 在创意驱动的高保真 UI 生成上已经超越 Figma Make 和 Uizard。一个关键对比：Figma Make 生成「数学上正确但审美平淡」的设计系统，而 Moonchild 能即时生成带玻璃质感、模糊效果的「有灵魂的 UI」。设计师社区开始分裂为两个阵营：追求创意表达的转向 Moonchild，维护大型设计系统的留在 Figma。<br><small>来源：<a href=\"https://medium.muz.li/moonchild-ai-vs-uizard-vs-figma-make-the-ux-design-tool-that-wins-in-2026-2bc509a12555\">Moonchild AI vs Uizard vs Figma Make - Muzli</a> | <a href=\"https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345\">AI Tools Designers Should Stick With - UX Planet</a></small></li><li><strong>Figma 效率已成基线，设计师角色向「创意总监」转型</strong> — Instagram 上 Figma 2026 AI 集成的讨论引发热议：当高保真原型和响应式布局可以由 AI 自动生成时，设计师的价值从手动执行转向高层次创意方向把控。「效率不再是目标，而是起点。」<br><small>来源：<a href=\"https://www.instagram.com/p/DVQrVv_kpvA/\">Instagram - Figma AI 2026 讨论</a></small></li><li><strong>Anthropic 把 Figma、Canva 搬进 Claude 对话框</strong> — Anthropic 的 Cowork 平台新增 interactive apps，Claude 可以直接在聊天界面内操作 Figma、Canva、Slack、Box 等工具，无需离开对话。这是 AI 设计协作的一个范式转变——工具不再是你打开的窗口，而是 AI 调用的能力。<br><small>来源：<a href=\"https://aimultiple.com/ai-agent-tools\">AI Agent Tools 2026 - AIMultiple</a></small></li><li><strong>UX 设计师真实工作流曝光：8 款 AI 工具如何协同</strong> — 一位设计师详解其 2026 工作流：Moonchild 用于概念探索，Uizard 快速线框，Figma 精细打磨，Attention Insight 做预测性热力图。结论：未来不属于某个「完美 AI 工具」，而属于能组合使用多个 AI 的设计师。<br><small>来源：<a href=\"https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d\">8 Top AI Tools in My UX Workflow - Muzli</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「灵魂派 vs 系统派」</strong>：AI 设计工具正在分化为创意表达型（Moonchild）和工程规范型（Figma Make）</li><li><strong>设计工具进入对话</strong>：Anthropic 将 Figma/Canva 嵌入 Claude，工具从「窗口」变成「能力」</li><li><strong>组合拳成为新常态</strong>：顶级设计师同时使用 4-5 个 AI 工具，各司其职</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>AI 设计工具领域正在经历一次有趣的分裂，我把它叫做「灵魂派 vs 系统派」之争。</strong></p><p>Moonchild AI 的崛起不是偶然。当 Figma Make 还在生成「数学上正确但缺乏灵魂」的 UI 时，Moonchild 直接跳到了「情绪驱动设计」——你告诉它一个氛围，它给你带玻璃质感和精致模糊效果的高保真界面。这触及了一个根本问题：<strong>设计到底是工程还是艺术？</strong>Figma 选择了工程路线（精确、可复用、可维护），Moonchild 选择了艺术路线（表达、氛围、视觉冲击力）。两条路都对，但服务的是完全不同的需求。</p><p>更值得关注的是 Anthropic 的动作。把 Figma 和 Canva 直接嵌入 Claude 对话框——这不是简单的「集成」，而是在重新定义设计工具的交互范式。传统模式：设计师打开 Figma → 手动操作 → 导出。新模式：设计师对 Claude 说「基于我们的设计系统，生成一个定价页面」→ Claude 直接在 Figma 里操作 → 设计师审核。<strong>工具从「你操作的界面」变成了「AI 调用的 API」。</strong>这是 Figma 该警惕的信号：如果设计师的主要入口变成了 AI 对话框而不是 Figma 画布，Figma 就从主角变成了后台服务。</p><p>那篇 UX 设计师的真实工作流文章也印证了一个趋势：<strong>2026 年的顶级设计师不是某个工具的专家，而是「AI 工具组合师」。</strong>Moonchild 负责灵感、Uizard 负责速度、Figma 负责精度、Attention Insight 负责验证——四个 AI 各司其职，设计师的角色彻底变成了创意总监和质量把控者。这跟昨天 Figma 报告中「设计系统从组件库进化为活的框架」的结论完美呼应。</p><p>我的预测：到 2026 年底，「你用什么设计工具？」这个问题会变得和「你用什么浏览器？」一样无聊。真正重要的是：你的 AI 工具组合策略是什么？你如何在灵魂和系统之间找到平衡？</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Moonchild AI Rises: High-Fidelity 'Mood-Driven' Design Challenges Figma Make</strong> — Multiple deep comparisons show Moonchild AI surpassing Figma Make and Uizard in creative high-fidelity UI generation. Key contrast: Figma Make produces \"mathematically correct but aesthetically flat\" design systems, while Moonchild instantly generates UI with glass textures and refined blur effects. The design community is splitting into two camps.<br><small>Source: <a href=\"https://medium.muz.li/moonchild-ai-vs-uizard-vs-figma-make-the-ux-design-tool-that-wins-in-2026-2bc509a12555\">Muzli</a> | <a href=\"https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345\">UX Planet</a></small></li><li><strong>Figma Efficiency Is Now Baseline</strong> — Designers' value shifts from manual execution to high-level creative direction as AI handles prototyping and responsive layouts automatically.<br><small>Source: <a href=\"https://www.instagram.com/p/DVQrVv_kpvA/\">Instagram</a></small></li><li><strong>Anthropic Brings Figma, Canva Inside Claude Chat</strong> — Cowork's interactive apps let Claude operate Figma, Canva, Slack directly within the conversation. Tools become capabilities AI calls, not windows you open.<br><small>Source: <a href=\"https://aimultiple.com/ai-agent-tools\">AIMultiple</a></small></li><li><strong>Real UX Workflow: 8 AI Tools Working Together</strong> — A designer details their 2026 stack: Moonchild for exploration, Uizard for wireframes, Figma for precision, Attention Insight for predictive heatmaps. The future belongs to AI tool composers, not single-tool experts.<br><small>Source: <a href=\"https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d\">Muzli</a></small></li></ul><h3>🔄 Trends</h3><ul><li>'Soul vs System' split: creative expression tools (Moonchild) vs engineering rigor (Figma Make)</li><li>Design tools enter the conversation: Anthropic embeds Figma/Canva into Claude</li><li>Multi-tool composition becomes the norm for top designers</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>The AI design tool landscape is splitting into 'Soul vs System' — and it's the most interesting development since Figma ate Sketch.</strong> Moonchild AI's rise isn't accidental: it targets the emotional, mood-driven design that Figma Make's engineering-first approach can't deliver. But the real story is Anthropic embedding Figma directly into Claude's chat — transforming tools from 'windows you operate' into 'capabilities AI calls.' If designers' primary entry point becomes an AI conversation rather than the Figma canvas, Figma risks becoming a backend service. The smartest designers in 2026 aren't tool experts — they're 'AI tool composers' running 4-5 specialized AIs in concert. By year-end, 'what design tool do you use?' will be as boring as 'what browser do you use?'</p></div>"
    },
    "cover": images.get("moonchild_medium"),
    "sources": [
        {
            "title": {"zh": "Moonchild AI vs Uizard vs Figma Make - Muzli", "en": "Moonchild AI vs Uizard vs Figma Make - Muzli"},
            "url": "https://medium.muz.li/moonchild-ai-vs-uizard-vs-figma-make-the-ux-design-tool-that-wins-in-2026-2bc509a12555",
            "image": images.get("moonchild_medium")
        },
        {
            "title": {"zh": "AI Tools Designers Should Stick With - UX Planet", "en": "AI Tools Designers Should Stick With - UX Planet"},
            "url": "https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345",
            "image": images.get("uxplanet")
        },
        {
            "title": {"zh": "AI Agent Tools 2026 横评 - AIMultiple", "en": "AI Agent Tools 2026 Comparison - AIMultiple"},
            "url": "https://aimultiple.com/ai-agent-tools",
            "image": None
        },
        {
            "title": {"zh": "8 Top AI Tools in My UX Workflow - Muzli", "en": "8 Top AI Tools in My UX Workflow - Muzli"},
            "url": "https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d",
            "image": None
        }
    ]
}

tech_issue = {
    "date": "2026-03-12",
    "section": "tech",
    "title": {
        "zh": "OpenAI Codex Security 扫描 120 万次提交找出隐藏漏洞 · Claude Code 8 个月登顶开发者工具榜 · Qwen 3.5 小模型在笔记本上跑赢大模型",
        "en": "OpenAI Codex Security Scans 1.2M Commits · Claude Code Tops Developer Tools in 8 Months · Qwen 3.5 Compact Models Outperform Giants on Laptops"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>OpenAI Codex Security：AI 安全 Agent 扫描 120 万次提交</strong> — OpenAI 正式推出 Codex Security，一个基于前沿推理模型的安全 Agent。它不只是找漏洞——它会构建整个项目的深层上下文，识别其他 Agent 工具遗漏的复杂漏洞，并在向用户报告前自动验证以降低误报。关键设计理念：「在系统上下文中扎根漏洞发现」，而非泛泛扫描。<br><small>来源：<a href=\"https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html\">OpenAI Codex Security Scanned 1.2M Commits - The Hacker News</a></small></li><li><strong>Claude Code 8 个月从零登顶：Pragmatic Engineer 大规模调研</strong> — Pragmatic Engineer 发布 2026 AI 工具调研：Claude Code 自 2025 年 5 月发布后仅 8 个月即超越 GitHub Copilot 和 Cursor 成为开发者最常用 AI 工具。55% 的受访者定期使用 AI Agent，Staff+ 工程师使用率最高（63.5%）。大公司（10K+）倾向 Copilot（56%），小型创业公司更爱 Claude Code（75%）。<br><small>来源：<a href=\"https://newsletter.pragmaticengineer.com/p/ai-tooling-2026\">AI Tooling for Software Engineers in 2026 - Pragmatic Engineer</a></small></li><li><strong>Qwen 3.5 小模型系列：在笔记本上跑赢大模型</strong> — Alibaba 发布 Qwen 3.5 紧凑模型系列，在普通笔记本和边缘设备上运行，性能超越体量大得多的系统。AI 正从云端走向本地。与此同时，多个 AI Agent 协同编码成为新范式——一个 Agent 规划、一个写代码、一个审查，并行工作。<br><small>来源：<a href=\"https://aiagentstore.ai/ai-agent-news/daily/2026-03-07\">AI Agent News - March 7, 2026</a></small></li><li><strong>Cursor 加入并行子 Agent 和 BugBot</strong> — Cursor 2026 版新增 parallel subagents（将任务拆分给离散子 Agent）和 BugBot（自动 PR 级别代码审查）。AI 编码工具从「单体助手」进化为「Agent 团队」。<br><small>来源：<a href=\"https://aimultiple.com/ai-agent-tools\">AI Agent Tools 2026 - AIMultiple</a></small></li><li><strong>OpenAI Codex 用户飙升至 160 万，瞄准编码之外的 Agent 市场</strong> — Fortune 报道：Codex 正在从编码工具扩展为通用 Agent 平台。OpenAI 的策略与 Anthropic 的 Claude Code → 通用 Agent 路线高度相似。<br><small>来源：<a href=\"https://fortune.com/2026/03/04/openai-codex-growth-enterprise-ai-agents/\">OpenAI Sees Codex Users Spike to 1.6M - Fortune</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 安全从扫描进化为推理</strong>：Codex Security 用深层上下文理解取代传统规则匹配</li><li><strong>Claude Code 的闪电战</strong>：8 个月登顶，证明开发者工具的切换成本比想象中低</li><li><strong>边缘 AI 成为现实</strong>：Qwen 3.5 证明高性能模型不再需要云端</li><li><strong>Agent 协同编码</strong>：从单个 AI 助手到多 Agent 团队并行工作</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天的三条新闻放在一起看，画出了 AI 开发工具的 2026 全景图：安全、效率、本地化三条线正在同时收敛。</strong></p><p>先说 Codex Security。OpenAI 做了一件聪明的事：不是简单地用 AI 替代传统安全扫描器，而是让 AI 先「理解」整个项目，再在这个理解的基础上发现漏洞。120 万次提交的规模验证说明这不是 demo，而是 production-ready 的产品。但这里有个微妙的竞争逻辑：<strong>安全 Agent 天然需要深度代码理解，而深度代码理解恰恰是 Codex 作为编码工具的核心能力。</strong>OpenAI 在用安全场景巩固 Codex 的代码理解护城河。</p><p>Claude Code 8 个月登顶的数据更值得玩味。Pragmatic Engineer 的调研覆盖了真正在写代码的工程师，不是 Twitter 上的 hype。75% 的小创业公司选择 Claude Code——这说明在没有企业合同锁定的情况下，开发者用脚投票选了 Anthropic。但大公司 56% 选 Copilot 也不意外：采购流程、合规要求、现有 GitHub 生态——企业级切换成本不是产品质量能轻松跨越的。<strong>这形成了一个有趣的市场分层：Claude Code 统治创新前沿，Copilot 守住企业基本盘。</strong></p><p>Qwen 3.5 和 Cursor 的子 Agent 更新则指向同一个方向：AI 编码正在去中心化。模型在本地跑、Agent 并行协作、任务自动拆分——这不是「AI 辅助编程」了，这是「AI 团队编程」。结合昨天说的「选择性推理」，我越来越确信：<strong>2026 下半年的主流开发范式将是「人类架构师 + AI Agent 团队」，而不是「人类程序员 + AI 助手」。</strong>编码的民主化不是让更多人写代码，而是让更多人指挥 AI 写代码。</p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>OpenAI Codex Security: AI Agent Scans 1.2M Commits</strong> — Builds deep project context to find complex vulnerabilities other tools miss, auto-validates to reduce false positives.<br><small>Source: <a href=\"https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html\">The Hacker News</a></small></li><li><strong>Claude Code Tops Developer Tools in 8 Months</strong> — Pragmatic Engineer survey: Claude Code overtook Copilot and Cursor. 55% use AI agents regularly. 75% of startups choose Claude Code vs 56% of large enterprises on Copilot.<br><small>Source: <a href=\"https://newsletter.pragmaticengineer.com/p/ai-tooling-2026\">Pragmatic Engineer</a></small></li><li><strong>Qwen 3.5 Compact Models Run on Laptops</strong> — Alibaba's compact series outperforms larger systems on regular hardware. Multi-agent collaborative coding becomes the new paradigm.<br><small>Source: <a href=\"https://aiagentstore.ai/ai-agent-news/daily/2026-03-07\">AI Agent News</a></small></li><li><strong>Cursor Adds Parallel Subagents and BugBot</strong> — Tasks split across discrete sub-agents; BugBot handles automated PR-level code review.<br><small>Source: <a href=\"https://aimultiple.com/ai-agent-tools\">AIMultiple</a></small></li><li><strong>OpenAI Codex Users Spike to 1.6M</strong> — Codex expanding from coding to general-purpose agent platform.<br><small>Source: <a href=\"https://fortune.com/2026/03/04/openai-codex-growth-enterprise-ai-agents/\">Fortune</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI security evolves from scanning to reasoning</li><li>Claude Code's blitz: 8 months to #1 proves low switching costs</li><li>Edge AI becomes real: Qwen 3.5 proves high performance doesn't need cloud</li><li>Multi-agent coding: from single AI assistant to parallel agent teams</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Three stories, one picture: security, efficiency, and localization are converging in AI dev tools.</strong> Codex Security is clever — using deep project understanding rather than pattern matching, reinforcing Codex's code comprehension moat. Claude Code's 8-month blitz to #1 (75% startup adoption) shows developers vote with their feet when enterprise lock-in doesn't apply. Large companies still choose Copilot (56%) — procurement and compliance matter. The market is stratifying: Claude Code owns the innovation frontier, Copilot holds the enterprise base. Qwen 3.5 + Cursor's parallel subagents point to the same future: decentralized AI coding with local models and agent teams. Prediction: H2 2026's dominant dev paradigm will be 'human architect + AI agent team,' not 'human programmer + AI assistant.'</p></div>"
    },
    "cover": images.get("codex_security"),
    "sources": [
        {
            "title": {"zh": "OpenAI Codex Security 扫描 120 万次提交 - The Hacker News", "en": "OpenAI Codex Security Scanned 1.2M Commits - The Hacker News"},
            "url": "https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html",
            "image": images.get("codex_security")
        },
        {
            "title": {"zh": "AI Tooling for Software Engineers 2026 - Pragmatic Engineer", "en": "AI Tooling for Software Engineers 2026 - Pragmatic Engineer"},
            "url": "https://newsletter.pragmaticengineer.com/p/ai-tooling-2026",
            "image": images.get("pragmatic")
        },
        {
            "title": {"zh": "OpenAI Codex 用户飙升至 160 万 - Fortune", "en": "OpenAI Sees Codex Users Spike to 1.6M - Fortune"},
            "url": "https://fortune.com/2026/03/04/openai-codex-growth-enterprise-ai-agents/",
            "image": images.get("codex_fortune")
        },
        {
            "title": {"zh": "AI Agent Tools 2026 横评 - AIMultiple", "en": "AI Agent Tools 2026 - AIMultiple"},
            "url": "https://aimultiple.com/ai-agent-tools",
            "image": None
        }
    ]
}

# Load existing issues.json
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

# Prepend new issues (design first, then tech)
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

# Write back
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("✅ issues.json updated with 2 new entries")
