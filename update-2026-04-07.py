# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-04-07"""
import json
import urllib.request
import urllib.error
import re
import ssl

def get_og_image(url):
    """Fetch og:image from a URL."""
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            html = resp.read(50000).decode("utf-8", errors="ignore")
            m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', html)
            if not m:
                m = re.search(r'content=["\']([^"\']+)["\'][^>]+property=["\']og:image', html)
            return m.group(1) if m else ""
    except Exception:
        return ""

# Fetch og:images for sources
og_images = {}
urls_to_fetch = [
    "https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627",
    "https://moonchild.ai/blog/best-ai-design-tools-for-product-teams-in-2026",
    "https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745",
    "https://www.metaintro.com/blog/openai-robot-tax-public-wealth-fund-ai-jobs",
    "https://rawpickai.com/blog/ai-tool-news-roundup-april-7-2026",
    "https://dig.watch/updates/openai-proposals-highlight-ai-impact-on-jobs-wealth-and-taxation",
]

for u in urls_to_fetch:
    og_images[u] = get_og_image(u)
    print(f"OG: {u[:60]}... -> {og_images[u][:80] if og_images[u] else '(none)'}")

# Load existing issues
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

design_issue = {
    "date": "2026-04-07",
    "section": "design",
    "title": {
        "zh": "「仪表盘和设计系统的终结」引爆设计圈 · Moonchild AI：从 PRD 到设计系统的全链路 AI 工具 · 设计师正在离开 Figma？大迁移背后的真相",
        "en": "\"The End of Dashboards and Design Systems\" Goes Viral · Moonchild AI: PRD-to-Design-System Pipeline · Are Designers Leaving Figma? The Great Transition"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Michal Malewicz 万字长文「仪表盘和设计系统的终结」引爆 Medium——6500+ 赞，265 条评论</strong> — 资深设计师 Michal Malewicz 发表了一篇在设计圈引发地震的文章：《The End of Dashboards and Design Systems》。核心论点：<strong>AI 正在让传统的仪表盘界面和组件化设计系统变得过时</strong>——当 AI Agent 可以直接理解用户意图并执行任务时，用户根本不需要看一堆图表和按钮。设计正在「悄悄地重新变得人性化」。这篇文章在 Medium 上获得了 6500+ 赞和 265 条评论，成为 2026 年设计领域讨论度最高的文章之一。<br><small>来源：<a href=\"https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627\">Medium - Michal Malewicz</a></small></li><li><strong>Moonchild AI 崛起：从 PRD 到可用设计系统的全链路 AI 设计工具</strong> — Moonchild AI 正在成为 2026 年最受关注的 AI 设计工具之一。与 Figma Make 等工具不同，Moonchild 的定位是<strong>全链路覆盖——从产品需求文档（PRD）到多屏幕流程、交互原型、再到可导出到 Figma/Claude Code/Cursor 的设计系统</strong>。UX Planet 的评测指出，Moonchild 生成的不是随机 mockup，而是「有意图、可用的界面流程」。多篇 Medium 热文（总计数千赞）记录了设计师用 Moonchild 生成设计系统再与 Claude Code 协作开发的工作流。<br><small>来源：<a href=\"https://moonchild.ai/blog/best-ai-design-tools-for-product-teams-in-2026\">Moonchild AI Blog</a>、<a href=\"https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345\">UX Planet</a></small></li><li><strong>「设计师正在离开 Figma」：Bootcamp 热文探讨设计工具大迁移</strong> — Design Bootcamp 上一篇获得 2600+ 赞的文章深入分析了设计师离开 Figma 的趋势。原因不是 Figma 变差了，而是<strong>AI 原生工具正在重新定义「设计工具」的边界</strong>——Cursor、Claude Code、Moonchild 等工具让设计师可以直接生成可用代码和原型，传统的「画线框图→做组件→交付开发」流程被压缩甚至跳过。文章指出，Figma 正面临一个「创意行业快速变化」的挑战——它需要从设计工具进化为「AI 设计平台」，否则将被新工具蚕食。<br><small>来源：<a href=\"https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745\">Design Bootcamp</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>后仪表盘时代</strong>：AI Agent 让传统 GUI 范式受到根本质疑——设计的对象从「界面」变成「对话和意图」</li><li><strong>全链路 AI 设计</strong>：Moonchild 代表的新范式——从需求到设计到代码的一体化生成</li><li><strong>Figma 的身份危机</strong>：从设计工具之王到 AI 设计平台的转型压力</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Malewicz 这篇「仪表盘的终结」是 2026 年我读到的最具颠覆性的设计观点——它不是在讨论工具迭代，而是在质疑整个 GUI 设计范式的存在基础。</strong></p><p>让我把这篇文章放在更大的背景下看。上期我们讨论了 NN/g 的报告，结论是「窄范围 AI 工具胜过广范围工具」——AI 在具体任务上好用，在开放创意上拉胯。Malewicz 的文章从完全不同的角度切入，但指向了同一个方向：<strong>如果 AI 可以直接理解用户意图并执行任务，那用户为什么还需要点击按钮、查看图表、在仪表盘上做筛选？</strong>这不是「AI 工具替代设计师」的老故事——这是「AI 让整个界面层变薄」的新故事。</p><p>想想你日常用的 SaaS 产品——Notion、Linear、Figma、Slack。它们的核心界面都是仪表盘+组件系统。但如果一个 AI Agent 可以直接帮你「把上周的任务进度汇总成报告发给老板」，你还需要打开 Linear 的仪表盘手动筛选吗？<strong>当 AI 成为主要交互界面时，传统 GUI 从「必须品」降级为「备用方案」。</strong></p><p>这就解释了 Moonchild AI 为什么火了。它的成功不在于「生成更好看的 UI」——它的成功在于<strong>承认了一个事实：设计的起点不再是画布，而是需求文档</strong>。PRD → 多屏流程 → 交互原型 → 可用代码，这个全链路自动化意味着「设计」和「开发」之间的边界正在消失。Medium 上那些记录 Moonchild + Claude Code 工作流的文章，本质上在展示一种新的产品开发范式：设计师不再画像素，而是定义意图；AI 把意图变成界面和代码。</p><p>而 Figma 的困境恰恰在这里。2600+ 赞的「设计师离开 Figma」文章不是空穴来风——<strong>当设计师可以用 Cursor 直接写出比 Figma 原型更完整的产品，当 Moonchild 可以从 PRD 直接生成 Figma 文件，Figma 的角色从「创作工具」变成了「渲染层」</strong>。这就像 Word 在 Google Docs 面前的困境，但更严峻——因为 AI 工具不只是换了个平台，而是改变了整个工作流的起点和终点。</p><p>把今天的三条新闻连起来，我看到一个清晰的叙事弧：<strong>界面在变薄（仪表盘的终结）→ 工作流在缩短（PRD 直达代码）→ 工具在重组（Figma 的大迁移）。</strong>这三件事是同一个趋势的三个面向。设计师的核心价值不再是「画出好看的界面」，而是「定义好的用户体验——无论那个体验是通过 GUI、对话、还是 Agent 来实现的」。</p><p><strong>我的预判：「后仪表盘设计」将在 2026 下半年成为设计行业的主流议题。Figma 会在今年的 Config 大会上大幅加码 AI Agent 相关功能——否则它将面临 Moonchild 等新工具的正面竞争。而对设计师来说，最危险的不是 AI 取代你，而是你还在用 2020 年的工作流做 2026 年的产品。</strong></p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Michal Malewicz's \"The End of Dashboards and Design Systems\" Goes Viral — 6,500+ Claps, 265 Comments</strong> — Senior designer Michal Malewicz published a seismic article arguing that <strong>AI is making traditional dashboard interfaces and component-based design systems obsolete</strong> — when AI agents can directly understand user intent and execute tasks, users don't need charts and buttons. \"Design is becoming quietly human again.\" The piece earned 6,500+ claps and 265 comments on Medium, becoming one of 2026's most discussed design articles.<br><small>Source: <a href=\"https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627\">Medium - Michal Malewicz</a></small></li><li><strong>Moonchild AI Rises: Full-Pipeline AI Design Tool from PRD to Design System</strong> — Moonchild AI is becoming one of 2026's most talked-about AI design tools. Unlike Figma Make, Moonchild covers the <strong>entire pipeline — from PRD to multi-screen flows, interactive prototypes, and exportable design systems for Figma/Claude Code/Cursor</strong>. UX Planet notes Moonchild generates \"intentional, usable interface flows, not random mockups.\" Multiple viral Medium posts document designers using Moonchild to generate design systems then collaborating with Claude Code for development.<br><small>Source: <a href=\"https://moonchild.ai/blog/best-ai-design-tools-for-product-teams-in-2026\">Moonchild AI Blog</a>, <a href=\"https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345\">UX Planet</a></small></li><li><strong>\"Designers Are Leaving Figma\": The Great Transition Explored</strong> — A 2,600+ clap Design Bootcamp article analyzes the trend of designers leaving Figma. The issue isn't that Figma got worse — it's that <strong>AI-native tools are redefining what \"design tool\" means</strong>. Cursor, Claude Code, and Moonchild let designers generate usable code and prototypes directly, compressing or skipping the traditional wireframe→component→handoff workflow. Figma faces an existential challenge: evolve into an \"AI design platform\" or be eaten by newcomers.<br><small>Source: <a href=\"https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745\">Design Bootcamp</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Post-dashboard era: AI agents fundamentally question traditional GUI paradigms — design objects shift from \"interfaces\" to \"conversations and intent\"</li><li>Full-pipeline AI design: Moonchild represents a new paradigm — integrated generation from requirements to design to code</li><li>Figma's identity crisis: pressure to transform from design tool king to AI design platform</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Malewicz's \"End of Dashboards\" is the most subversive design opinion I've read in 2026 — it's not discussing tool iterations, but questioning the very foundation of the GUI design paradigm.</strong></p><p>Let me place this in context. Last issue, we discussed NN/g's report concluding that narrow-scope AI tools beat broad ones. Malewicz approaches from a completely different angle but points in the same direction: <strong>if AI can directly understand user intent and execute tasks, why do users need to click buttons, view charts, and filter dashboards?</strong> This isn't the old \"AI replaces designers\" story — it's the new \"AI makes the entire interface layer thinner\" story.</p><p>Think about your daily SaaS products — Notion, Linear, Figma, Slack. Their core interfaces are dashboards + component systems. But if an AI agent can directly \"summarize last week's task progress into a report for my boss,\" do you still need to open Linear's dashboard and manually filter? <strong>When AI becomes the primary interaction interface, traditional GUI downgrades from \"necessity\" to \"fallback.\"</strong></p><p>This explains Moonchild AI's rise. Its success isn't about generating prettier UI — it's about <strong>acknowledging a reality: design's starting point is no longer the canvas but the requirements document</strong>. PRD → multi-screen flows → interactive prototypes → usable code — this full-pipeline automation means the boundary between \"design\" and \"development\" is disappearing.</p><p>Figma's predicament lies precisely here. <strong>When designers can use Cursor to build more complete products than Figma prototypes, when Moonchild can generate Figma files from a PRD, Figma's role shifts from \"creation tool\" to \"rendering layer.\"</strong> Today's three stories form a clear narrative arc: <strong>interfaces are thinning (end of dashboards) → workflows are shortening (PRD to code) → tools are reorganizing (Figma's great migration).</strong> These are three facets of the same trend.</p><p><strong>My prediction: \"Post-dashboard design\" will become a mainstream industry topic in H2 2026. Figma will double down on AI agent features at this year's Config — or face direct competition from Moonchild and others. For designers, the biggest danger isn't AI replacing you, but you still using a 2020 workflow to build 2026 products.</strong></p></div>"
    },
    "cover": og_images.get("https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627", ""),
    "sources": [
        {
            "title": {
                "zh": "仪表盘和设计系统的终结",
                "en": "The End of Dashboards and Design Systems"
            },
            "url": "https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627",
            "image": og_images.get("https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627", "")
        },
        {
            "title": {
                "zh": "2026 年产品团队最佳 AI 设计工具",
                "en": "The Best AI Design Tools for Product Teams in 2026"
            },
            "url": "https://moonchild.ai/blog/best-ai-design-tools-for-product-teams-in-2026",
            "image": og_images.get("https://moonchild.ai/blog/best-ai-design-tools-for-product-teams-in-2026", "")
        },
        {
            "title": {
                "zh": "设计师正在离开 Figma：大迁移",
                "en": "Why Are Designers Leaving Figma? The Great Transition"
            },
            "url": "https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745",
            "image": og_images.get("https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745", "")
        }
    ]
}

tech_issue = {
    "date": "2026-04-07",
    "section": "tech",
    "title": {
        "zh": "本周 AI 工具大爆发：Cursor 3 重写、Google Gemma 4 开源、Sora 关停、Claude Code 年化收入破 10 亿 · OpenAI 发布「机器人税」政策白皮书 · Anthropic Claude Code 源码意外泄露",
        "en": "AI Tool Explosion: Cursor 3 Rebuilt, Gemma 4 Open-Source, Sora Shut Down, Claude Code Hits $1B ARR · OpenAI Proposes Robot Tax & 4-Day Workweek · Anthropic Claude Code Source Code Leaked"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>本周 AI 工具大爆发：Cursor 3 从零重写、Google Gemma 4 开源、OpenAI Sora 关停</strong> — RawPickAI 评价这是「自 GPT-5 发布以来最多事的一周」。<strong>Cursor 3</strong> 不是增量更新——它从底层重写，核心是「AI Agent 并行处理」，多个 Agent 同时在不同文件上工作，这是对 Claude Code（顺序处理）的差异化竞争。TechCrunch 还曝光 Cursor 的 Composer 2 模型基于中国月之暗面的 Kimi K2.5。<strong>Google Gemma 4</strong> 以 Apache 2.0 开源发布，被评为「今年最重要的开源发布」。<strong>Sora 正式关停</strong>——OpenAI 的独立 AI 视频生成产品退出舞台，功能被整合进 ChatGPT。<strong>Claude Code 年化收入在 6 个月内突破 10 亿美元</strong>，成为 AI 编码领域最快达到此里程碑的产品。<br><small>来源：<a href=\"https://rawpickai.com/blog/ai-tool-news-roundup-april-7-2026\">RawPickAI</a></small></li><li><strong>OpenAI 发布 13 页政策白皮书：提出「机器人税」、公共财富基金和四天工作制</strong> — OpenAI 发布了一份名为《Intelligence Age 的产业政策》的重磅白皮书。核心提案：<strong>对使用 AI 替代人类工人的企业征收「机器人税」</strong>，税收注入公共财富基金，为每个公民提供年度分红；试行四天工作制；当 AI 导致的失业率超过特定阈值时，自动触发安全网机制。OpenAI 明确表示自己是「政治行动者」——<strong>这是 AI 公司第一次系统性地为自己产品可能造成的社会冲击提出政策解决方案</strong>。Salesforce 等公司已经在裁员以投资 AI——白皮书承认了这个现实。<br><small>来源：<a href=\"https://dig.watch/updates/openai-proposals-highlight-ai-impact-on-jobs-wealth-and-taxation\">DigWatch</a>、<a href=\"https://www.metaintro.com/blog/openai-robot-tax-public-wealth-fund-ai-jobs\">Metaintro</a></small></li><li><strong>Anthropic Claude Code 源码意外泄露——800 份拷贝在被追回前已扩散</strong> — Anthropic 因「人为失误」意外泄露了 Claude Code 的内部源码。公司紧急试图撤回 800 份已扩散的拷贝。这一事件发生在市场高度关注 Anthropic 下一步模型策略的时刻——内部有一个名为 Mythos 的更强模型正在测试中。泄露事件虽然尴尬，但也侧面印证了 Claude Code 的技术复杂度和商业价值（年化收入 10 亿美元）。<strong>Anthropic 的 ARR 已达 190 亿美元，估值 3800 亿美元</strong>——它正在成为 AI 领域仅次于 OpenAI 的第二极。<br><small>来源：<a href=\"https://gardenzhome.com/anthripic-claude-news-updates-today\">Gardenzhome</a>、<a href=\"https://vpssos.com/ai-model-news-today\">VPS SOS</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 编码工具战争白热化</strong>：Cursor 3（并行 Agent）vs Claude Code（10 亿 ARR）vs Windsurf Free——三种路线的正面碰撞</li><li><strong>AI 公司开始面对社会后果</strong>：OpenAI 的「机器人税」白皮书标志着行业从「造产品」进入「治理副作用」阶段</li><li><strong>开源 vs 闭源的新平衡</strong>：Gemma 4 + Apache 2.0 让免费工具能力大幅提升，闭源模型的定价权受到挑战</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>这周的新闻量级之大，用一个词概括就是「分水岭」。但不是技术的分水岭——而是叙事的分水岭。</strong></p><p>先说最有意思的事：OpenAI 提出「机器人税」。让我直说——<strong>这是今年最具讽刺意味的科技新闻</strong>。世界上最积极推进 AI 替代人类工作的公司，现在跳出来说「我们需要为 AI 导致的失业征税」。这就像石油公司提出碳税方案——动机不是环保，而是通过主导规则制定来保护自己的竞争优势。如果「机器人税」真的实施，受冲击最大的不是 OpenAI（它卖模型 API），而是那些直接用 AI 替代员工的传统企业。OpenAI 提这个方案，等于在给自己的客户加成本，同时把自己包装成「负责任的 AI 公司」——公关和竞争策略的双赢。</p><p>但我不否认白皮书本身的价值。它把一个大家都在私下讨论的问题——AI 导致的大规模失业——正式摆上了台面。四天工作制、公共财富基金、自动触发的安全网——这些不是乌托邦幻想，而是对现实的直面。Salesforce 裁了 4000 人说「AI 让我不需要那么多人了」。<strong>当造 AI 的人都在说「是的，AI 会干掉大量工作」，你还能假装这不会发生吗？</strong></p><p>再说 Cursor 3。并行 Agent 是一个值得关注的架构创新——让多个 AI Agent 同时在不同文件上工作，而不是 Claude Code 的顺序处理。但更有意思的是 TechCrunch 曝光 Cursor 用的是月之暗面的 Kimi K2.5。<strong>一个美国最火的 AI 编码工具，核心模型来自中国——这是开源 AI 生态跨越地缘政治边界的活生生案例。</strong>同时 Google Gemma 4 以 Apache 2.0 开源，Windsurf 提供免费版本。免费和开源的 AI 工具组合已经强大到足以让独立开发者零成本起步——这在三个月前还不可能。</p><p>把设计和科技板块的新闻连起来看：<strong>Malewicz 说仪表盘要终结，Cursor 3 说编码要并行化，OpenAI 说工作周要四天——2026 年的主题不是「AI 能做什么」，而是「AI 改变了什么」。</strong>我们正在从技术突破期进入社会适应期。工具在变强，但更重要的是工作方式、设计范式、甚至社会契约都在被重写。</p><p><strong>我的预判：OpenAI 的「机器人税」白皮书会在美国引发真正的政策辩论——尤其在中期选举年。Cursor vs Claude Code 的竞争将在 Q2 定义 AI 编码工具的最终形态。而 Sora 的关停是一个信号：独立 AI 产品的生存空间正在被平台化吞噬，未来的 AI 功能将以「嵌入」而非「独立 app」的形式存在。对设计师和开发者来说：现在是学习 AI Agent 工作流的最佳时机——免费工具已经足够强大，入门成本为零。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>AI Tool Explosion This Week: Cursor 3 Rebuilt from Scratch, Google Gemma 4 Open-Source, Sora Shut Down</strong> — RawPickAI calls this \"the most eventful week since GPT-5 launched.\" <strong>Cursor 3</strong> is a ground-up rebuild centered on parallel AI agents — multiple agents working on different files simultaneously, differentiating from Claude Code's sequential processing. TechCrunch revealed Cursor's Composer 2 model is built on Moonshot AI's Kimi K2.5 from China. <strong>Google Gemma 4</strong> released under Apache 2.0 — \"the most significant open-source release this year.\" <strong>Sora officially shut down</strong> — OpenAI's standalone AI video product exits, bundled into ChatGPT. <strong>Claude Code hit $1B annualized revenue in 6 months</strong> — fastest to this milestone in AI coding.<br><small>Source: <a href=\"https://rawpickai.com/blog/ai-tool-news-roundup-april-7-2026\">RawPickAI</a></small></li><li><strong>OpenAI Publishes 13-Page Policy Blueprint: Robot Tax, Public Wealth Fund, 4-Day Workweek</strong> — OpenAI released \"Industrial Policy for the Intelligence Age.\" Core proposals: <strong>a \"robot tax\" on companies using AI to replace workers</strong>, funding a public wealth fund providing annual dividends to citizens; four-day workweek trials; automatic safety nets triggered when AI job displacement crosses thresholds. OpenAI explicitly positions itself as a \"political actor\" — <strong>the first time an AI company has systematically proposed policy solutions for its own products' societal impact</strong>.<br><small>Source: <a href=\"https://dig.watch/updates/openai-proposals-highlight-ai-impact-on-jobs-wealth-and-taxation\">DigWatch</a>, <a href=\"https://www.metaintro.com/blog/openai-robot-tax-public-wealth-fund-ai-jobs\">Metaintro</a></small></li><li><strong>Anthropic Claude Code Source Code Accidentally Leaked — 800 Copies Spread Before Takedown</strong> — Anthropic accidentally leaked Claude Code's internal source code due to human error, scrambling to recall 800 copies. This happened as markets closely watched Anthropic's next model moves — an internal model called Mythos is reportedly being tested. The leak, while embarrassing, confirms Claude Code's technical complexity and commercial value ($1B ARR). <strong>Anthropic's ARR has reached $19B with a $380B valuation</strong> — it's becoming AI's second pole after OpenAI.<br><small>Source: <a href=\"https://gardenzhome.com/anthripic-claude-news-updates-today\">Gardenzhome</a>, <a href=\"https://vpssos.com/ai-model-news-today\">VPS SOS</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI coding tool war heats up: Cursor 3 (parallel agents) vs Claude Code ($1B ARR) vs Windsurf Free — three paradigms collide</li><li>AI companies face social consequences: OpenAI's \"robot tax\" paper marks the shift from \"building products\" to \"governing side effects\"</li><li>Open-source vs closed-source rebalancing: Gemma 4 + Apache 2.0 dramatically improves free tooling, challenging closed-model pricing power</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>This week's news volume demands a single word: \"watershed.\" Not a technology watershed — a narrative watershed.</strong></p><p>The most fascinating story: OpenAI proposing a \"robot tax.\" Let me be direct — <strong>this is the most ironic tech news of the year</strong>. The company most aggressively advancing AI's replacement of human work now says \"we need to tax AI-caused unemployment.\" It's like an oil company proposing a carbon tax — the motive isn't environmentalism but controlling the regulatory framework to protect competitive advantage. If a robot tax were implemented, the hardest hit wouldn't be OpenAI (which sells model APIs) but traditional companies directly replacing employees with AI. OpenAI's proposal effectively raises costs for its own customers while branding itself as \"responsible\" — a PR and competitive strategy two-fer.</p><p>But the white paper's substance has real value. It puts an issue everyone discusses privately — massive AI-driven unemployment — officially on the table. Four-day workweek, public wealth fund, automatic safety nets — these aren't utopian fantasies but reality confrontation. When the AI builders themselves say \"yes, AI will eliminate massive numbers of jobs,\" can you still pretend it won't happen?</p><p>Cursor 3's parallel agent architecture is a noteworthy innovation. But the TechCrunch revelation that it uses Moonshot AI's Kimi K2.5 is more telling — <strong>America's hottest AI coding tool running on a Chinese core model is a living case study of open-source AI crossing geopolitical boundaries.</strong> Combined with Gemma 4 under Apache 2.0 and Windsurf's free tier, the free open-source AI toolkit is now powerful enough for independent developers to start at zero cost.</p><p><strong>Connecting design and tech: Malewicz says dashboards are ending, Cursor 3 says coding should be parallelized, OpenAI says workweeks should be four days — 2026's theme isn't \"what AI can do\" but \"what AI changes.\" We're shifting from a period of technical breakthroughs to social adaptation. Tools are getting stronger, but more importantly, work methods, design paradigms, and even social contracts are being rewritten.</strong></p></div>"
    },
    "cover": og_images.get("https://rawpickai.com/blog/ai-tool-news-roundup-april-7-2026", ""),
    "sources": [
        {
            "title": {
                "zh": "AI 工具新闻周报 — 2026 年 4 月 7 日",
                "en": "AI Tool News Roundup — Week of April 7, 2026"
            },
            "url": "https://rawpickai.com/blog/ai-tool-news-roundup-april-7-2026",
            "image": og_images.get("https://rawpickai.com/blog/ai-tool-news-roundup-april-7-2026", "")
        },
        {
            "title": {
                "zh": "OpenAI 提出「机器人税」和公共财富基金",
                "en": "OpenAI Wants Robot Taxes and a Citizen Wealth Fund"
            },
            "url": "https://dig.watch/updates/openai-proposals-highlight-ai-impact-on-jobs-wealth-and-taxation",
            "image": og_images.get("https://dig.watch/updates/openai-proposals-highlight-ai-impact-on-jobs-wealth-and-taxation", "")
        },
        {
            "title": {
                "zh": "Anthropic Claude Code 源码意外泄露",
                "en": "Anthropic Claude Code Source Code Leaked"
            },
            "url": "https://gardenzhome.com/anthripic-claude-news-updates-today",
            "image": ""
        }
    ]
}

# Insert new issues at the front
issues.insert(0, design_issue)
issues.insert(1, tech_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("✅ issues.json updated with 2 new issues for 2026-04-07")
