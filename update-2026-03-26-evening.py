# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-03-26 Evening Update"""
import json, re, urllib.request, urllib.error, html.parser

class OGImageParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.og_image = ""
    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            d = dict(attrs)
            if d.get("property") == "og:image" or d.get("name") == "og:image":
                self.og_image = d.get("content", "")

def get_og_image(url, timeout=8):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read(100000).decode("utf-8", errors="ignore")
        p = OGImageParser()
        p.feed(data)
        return p.og_image
    except Exception:
        return ""

# Fetch og:images for key sources
urls = {
    "stitch_google": "https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/",
    "stitch_muzli": "https://muz.li/blog/google-just-introduced-vibe-design-heres-what-it-means-for-ui-designers/",
    "stitch_techradar": "https://www.techradar.com/pro/google-unveils-new-vibe-design-tool-to-help-anyone-design-a-high-fidelity-ui-using-natural-language",
    "figma_ux": "https://www.figma.com/resource-library/ai-tools-for-ux-designers/",
    "nemoclaw_cnbc": "https://www.cnbc.com/2026/03/10/nvidia-open-source-ai-agent-platform-nemoclaw-wired-agentic-tools-openclaw-clawdbot-moltbot.html",
    "nemoclaw_forbes": "https://www.forbes.com/sites/jonmarkman/2026/03/11/nvidia-moves-beyond-chips-with-an-open-source-platform-for-ai-agents/",
    "nemoclaw_yahoo": "https://finance.yahoo.com/news/nvidia-launches-nemoclaw-platform-for-ai-agents-200851962.html",
    "gumloop": "https://www.indexbox.io/blog/gumloop-secures-50m-series-b-funding-led-by-benchmark-to-expand-ai-agent-platform/",
    "deerflow": "https://radicaldatascience.wordpress.com/2026/03/17/ai-news-briefs-bulletin-board-for-march-2026/",
    "aiapps": "https://www.aiapps.com/blog/ai-news-march-2026-breakthroughs-launches-trends/",
}

print("Fetching og:images...")
images = {}
for k, u in urls.items():
    img = get_og_image(u)
    images[k] = img
    print(f"  {k}: {img[:80] if img else '(none)'}")

# Build new issues
design_issue = {
    "date": "2026-03-26",
    "section": "design",
    "title": {
        "zh": "Google 推出「Vibe Design」重新定义设计起点：从结构到意图 · Figma 生态 AI 工具全面整合 · 生成式 AI 设计市场突破 11 亿美元",
        "en": "Google Launches 'Vibe Design' Redefining Design Starting Points: From Structure to Intent · Figma Ecosystem AI Tools Consolidate · Generative AI in Design Market Surpasses $1.1B"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Google 推出 Stitch「Vibe Design」：用意图而非线框图开始设计</strong> — Google Labs 对 Stitch 进行了重大改版，引入「Vibe Design」概念——设计师不再从线框图和结构开始，而是从意图、感觉、甚至商业目标出发，AI 生成高保真 UI。新增功能包括：AI 原生无限画布（从构思到原型一站式完成）、语音设计（用语音描述需求，AI 实时更新设计）、Agent 管理器（并行处理多个设计方案并追踪进度）、以及一键导出到 AI Studio 和 Antigravity。产品经理 Rustin Banks 表示，Stitch 鼓励用户「探索多个想法、头脑风暴和自我批评」。TechRadar 评价这是 Google 在设计工具领域「最认真的一次出手」。<br><small>来源：<a href=\"https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/\">Google Blog</a> | <a href=\"https://www.techradar.com/pro/google-unveils-new-vibe-design-tool-to-help-anyone-design-a-high-fidelity-ui-using-natural-language\">TechRadar</a> | <a href=\"https://muz.li/blog/google-just-introduced-vibe-design-heres-what-it-means-for-ui-designers/\">Muzli</a></small></li><li><strong>Figma 发布 2026 年 AI 工具全景：从 UX 研究到产品设计的完整 AI 工作流</strong> — Figma 官方发布了三份深度资源：UX 设计师 AI 工具 Top 9（包括 Figma Make、UX Pilot、Khroma 等）、AI 设计工具 Top 11（涵盖 Canva Magic Studio、Microsoft Designer、Adobe Firefly）、以及 AI 产品设计工具 Top 5（Figma Design、Figma Make、Relume、Visily、Midjourney）。核心信息是：<strong>Figma 正在把自己定位为 AI 设计工具的「枢纽」</strong>——不只做自己的 AI 功能，还把第三方工具（Relume、Visily）纳入自己的推荐生态。Ironhack 的分析指出，2026 年 UX 设计师对话中出现频率最高的三个 AI 工具是 ChatGPT、FigJam AI 和 Gemini Flash Image。<br><small>来源：<a href=\"https://www.figma.com/resource-library/ai-tools-for-ux-designers/\">Figma UX Tools</a> | <a href=\"https://www.figma.com/resource-library/ai-design-tools/\">Figma Design Tools</a> | <a href=\"https://www.ironhack.com/us/blog/ai-tools-for-the-uxui-designer-in-2026\">Ironhack</a></small></li><li><strong>生成式 AI 设计市场 2025 年突破 11 亿美元，持续高速增长</strong> — IntelMarketResearch 报告显示，全球生成式 AI 设计市场 2024 年估值 9.37 亿美元，2025 年增长至 11 亿美元。McKinsey 预测，AI 领先企业与落后企业的差距将持续扩大——前者已进入多模态 AI、实时个性化、自主决策阶段，后者还在尝试基础的预测分析。<br><small>来源：<a href=\"https://www.intelmarketresearch.com/generative-ai-in-design-market-25269\">IntelMarketResearch</a> | <a href=\"https://www.linkedin.com/pulse/ai-transformation-2026-26-predictions-redefining-cx-ex-saltz-gulko-twspf\">LinkedIn</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「Vibe Design」：设计范式从「结构优先」到「意图优先」</strong>：Google Stitch 把设计的起点从线框图和组件移到了意图和情感——这可能是比「AI 生成图片」更深层的变革</li><li><strong>Figma 从工具到平台</strong>：通过官方推荐第三方 AI 工具并强调集成，Figma 在巩固「设计操作系统」的地位</li><li><strong>市场验证：生成式 AI 设计不是概念</strong>：11 亿美元的市场规模证明这已经是真实的商业赛道</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Google Stitch 的「Vibe Design」看起来只是又一个设计工具的营销概念，但它触及了一个比大多数人意识到的更根本的问题：设计的起点应该是什么？</strong></p><p>过去 20 年，设计工作流的起点是「结构」——先画线框图，再填内容，再调视觉。Figma、Sketch、Adobe XD 都是围绕这个范式构建的。Stitch 的「Vibe Design」把起点移到了「意图」——你告诉 AI 你想要什么感觉、什么商业目标，AI 生成高保真 UI，你在这个基础上迭代。这不只是效率提升，<strong>这是设计认知模型的根本变化：从「自下而上的构建」到「自上而下的雕刻」。</strong></p><p>但这里有一个 Google 不会告诉你的问题。语音设计、意图驱动、AI 生成——这些功能在 demo 中看起来很酷，但它们天然倾向于生成「看起来正确但缺乏独特性」的设计。为什么？因为 AI 模型是从大量现有设计中学习的，它生成的东西必然是统计意义上的「平均值」。当每个人都用 Stitch 从意图出发生成 UI 时，你会得到大量「看起来都差不多但都还不错」的设计。<strong>这对 MVP 和快速验证是巨大的效率提升，但对品牌差异化和设计创新是隐性威胁。</strong></p><p>Figma 的策略更值得长期关注。它没有像 Google 那样做一个全新的 AI 设计工具，而是把自己定位为「AI 设计工具的枢纽」——官方推荐 Relume（AI 网站设计）、Visily（快速线框图）、Midjourney（视觉探索），同时强化自己的 Figma Make 和 FigJam AI。这个策略的聪明之处在于：<strong>Figma 不需要赢得 AI 能力的军备竞赛，它只需要确保所有最好的 AI 工具都与 Figma 集成。</strong>这和 iOS 的 App Store 策略如出一辙——平台不需要做最好的 app，只需要最好的 app 都在你的平台上。</p><p>把 Stitch 和 Figma 放在一起看，你会看到两种截然不同的路径。Google 在赌「AI 原生设计工具会取代传统工具」——Stitch 的无限画布、语音设计、Agent 管理器都是从零开始构建的，和 Figma 的设计系统概念几乎没有交集。Figma 在赌「现有设计系统和工作流会被 AI 增强而非取代」——它的每个 AI 功能都是对现有工作流的叠加，而非替代。<strong>我的判断：短期（1-2 年）Figma 赢，因为企业设计系统的迁移成本极高；长期（3-5 年）要看 Stitch 能不能建立自己的设计系统生态——如果 Google 能让 Stitch 的输出与 Material Design 深度绑定，并提供从设计到 Flutter/Web 的完整链路，它就有机会成为 Figma 的真正威胁。</strong></p><p>最后一个数据点：生成式 AI 设计市场一年增长 17%（从 9.37 亿到 11 亿美元），这个增速在企业软件领域算得上「爆发式增长」。但更有趣的是 McKinsey 的观察——AI 领先企业和落后企业的差距在加速扩大。这意味着对设计团队来说，「是否使用 AI」已经不是一个选择题，而是一个生存题。不用 AI 的设计团队不会被 AI 取代，但会被<strong>用 AI 的设计团队</strong>取代。</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Google Launches 'Vibe Design' with Stitch: Starting from Intent, Not Wireframes</strong> — Google Labs redesigned Stitch as an AI-native design platform with 'Vibe Design' — designers start from intent, feelings, or business goals, and AI generates high-fidelity UI. New features: infinite canvas, voice design (describe needs verbally, AI updates in real-time), Agent manager for parallel ideas, and export to AI Studio/Antigravity.<br><small>Source: <a href=\"https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/\">Google Blog</a> | <a href=\"https://www.techradar.com/pro/google-unveils-new-vibe-design-tool-to-help-anyone-design-a-high-fidelity-ui-using-natural-language\">TechRadar</a></small></li><li><strong>Figma Publishes 2026 AI Tool Landscape: Complete AI Workflow from Research to Product</strong> — Three official resource guides covering UX tools (9), design tools (11), and product design tools (5). Figma positions itself as the AI design tool 'hub' — not just building its own AI features but recommending third-party tools within its ecosystem.<br><small>Source: <a href=\"https://www.figma.com/resource-library/ai-tools-for-ux-designers/\">Figma</a> | <a href=\"https://www.ironhack.com/us/blog/ai-tools-for-the-uxui-designer-in-2026\">Ironhack</a></small></li><li><strong>Generative AI Design Market Hits $1.1B in 2025</strong> — Market grew from $937M (2024) to $1.1B (2025). McKinsey notes the gap between AI leaders and laggards is accelerating.<br><small>Source: <a href=\"https://www.intelmarketresearch.com/generative-ai-in-design-market-25269\">IntelMarketResearch</a></small></li></ul><h3>🔄 Trends</h3><ul><li>'Vibe Design': paradigm shift from structure-first to intent-first design</li><li>Figma evolving from tool to platform by curating AI ecosystem</li><li>$1.1B market validates generative AI design as real business</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Google Stitch's 'Vibe Design' touches something more fundamental than most realize: what should the starting point of design be?</strong> For 20 years, it's been structure — wireframes first, content second, visuals last. Stitch moves it to intent. This isn't efficiency — it's a cognitive model shift from bottom-up construction to top-down sculpting. But AI-generated designs from intent tend toward statistical averages — great for MVPs, a hidden threat to brand differentiation. Figma's hub strategy (recommending third-party tools while strengthening its own) mirrors iOS's App Store playbook — the platform doesn't need the best app, just all the best apps on it. <strong>Short-term Figma wins (migration costs are enormous); long-term depends on whether Stitch can build its own design system ecosystem tied to Material Design and Flutter.</strong> The $1.1B market growing 17% YoY confirms: for design teams, using AI is no longer optional — it's existential.</p></div>"
    },
    "cover": images.get("stitch_google", "") or images.get("stitch_techradar", ""),
    "sources": [
        {
            "title": {"zh": "Google Blog: 用 Stitch 引入「Vibe Design」", "en": "Google Blog: Introducing 'Vibe Design' with Stitch"},
            "url": "https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/",
            "image": images.get("stitch_google", "")
        },
        {
            "title": {"zh": "TechRadar: Google 推出用自然语言设计高保真 UI 的新工具", "en": "TechRadar: Google Unveils New Vibe Design Tool"},
            "url": "https://www.techradar.com/pro/google-unveils-new-vibe-design-tool-to-help-anyone-design-a-high-fidelity-ui-using-natural-language",
            "image": images.get("stitch_techradar", "")
        },
        {
            "title": {"zh": "Muzli: Google 刚刚推出「Vibe Design」，这对 UI 设计师意味着什么", "en": "Muzli: What Google's Vibe Design Means for UI Designers"},
            "url": "https://muz.li/blog/google-just-introduced-vibe-design-heres-what-it-means-for-ui-designers/",
            "image": images.get("stitch_muzli", "")
        },
        {
            "title": {"zh": "Figma: 2026 年 UX 设计师 AI 工具 Top 9", "en": "Figma: Top 9 AI Tools for UX Designers in 2026"},
            "url": "https://www.figma.com/resource-library/ai-tools-for-ux-designers/",
            "image": images.get("figma_ux", "")
        },
        {
            "title": {"zh": "IntelMarketResearch: 生成式 AI 设计市场展望", "en": "IntelMarketResearch: Generative AI in Design Market Outlook"},
            "url": "https://www.intelmarketresearch.com/generative-ai-in-design-market-25269",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-03-26",
    "section": "tech",
    "title": {
        "zh": "NVIDIA NemoClaw 正式发布：AI Agent 的企业级开源运行时 · ByteDance DeerFlow 2.0 开源多 Agent 框架 · Gumloop 获 Benchmark 领投 5000 万美元：让每个员工成为 AI Agent 构建者",
        "en": "NVIDIA NemoClaw Launches: Enterprise Open-Source Runtime for AI Agents · ByteDance DeerFlow 2.0 Open-Sources Multi-Agent Framework · Gumloop Raises $50M from Benchmark: Making Every Employee an AI Agent Builder"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>NVIDIA 正式发布 NemoClaw：企业级 AI Agent 开源平台</strong> — NVIDIA 在 GTC 2026 上正式推出 NemoClaw，一个面向企业的开源 AI Agent 平台。据 Wired 报道，NVIDIA 已经向 Salesforce、Cisco、Google、Adobe、CrowdStrike 等巨头进行了预推介。NemoClaw 基于 OpenClaw 框架，叠加了企业级的隐私和安全控制，CEO Jensen Huang 表示其目标是让自主 Agent「更可信、可扩展、对全世界可用」。Forbes 分析指出这是 NVIDIA 从「AI 芯片公司」向「AI 软件标准」转型的关键一步——当企业在 NemoClaw 上构建 Agent 工作流时，整个技术栈（Nemotron 模型 + NIM 微服务）都天然优化于 NVIDIA 的 CUDA 生态。<strong>非 NVIDIA 客户也可以使用——这是一个「开源中立性」的策略选择。</strong><br><small>来源：<a href=\"https://www.cnbc.com/2026/03/10/nvidia-open-source-ai-agent-platform-nemoclaw-wired-agentic-tools-openclaw-clawdbot-moltbot.html\">CNBC</a> | <a href=\"https://www.forbes.com/sites/jonmarkman/2026/03/11/nvidia-moves-beyond-chips-with-an-open-source-platform-for-ai-agents/\">Forbes</a> | <a href=\"https://finance.yahoo.com/news/nvidia-launches-nemoclaw-platform-for-ai-agents-200851962.html\">Yahoo Finance</a></small></li><li><strong>ByteDance 开源 DeerFlow 2.0：多 Agent 协作框架</strong> — 字节跳动发布 DeerFlow 2.0，一个开源的多 Agent 系统框架。与单一大模型处理所有任务不同，DeerFlow 2.0 让每个 AI Agent 在独立的隔离环境中运行任务，通过协调机制完成复杂工作流。这代表了行业从「一个模型干所有事」到「多 Agent 协作」的架构转变。结合 Anaconda 与 NVIDIA 在 GPU 环境和开放模型上的深度整合（覆盖从 GPU 加速 Python 环境到 Agentic AI 的全栈），<strong>开源 Agent 基础设施正在快速成熟。</strong><br><small>来源：<a href=\"https://radicaldatascience.wordpress.com/2026/03/17/ai-news-briefs-bulletin-board-for-march-2026/\">Radical Data Science</a> | <a href=\"https://github.com/bytedance/deer-flow\">GitHub</a></small></li><li><strong>Gumloop 获 Benchmark 领投 5000 万美元 B 轮：让非技术员工构建 AI Agent</strong> — 无代码 AI Agent 平台 Gumloop 完成由 Benchmark 领投、Greylock 和 First Round Capital 跟投的 5000 万美元 B 轮融资。Gumloop 的平台允许零编程经验的企业员工用自然语言创建自主 AI Agent，处理重复任务、数据综合和决策建议。CEO Aisha Patel 表示：「工作的未来不是用 AI 取代员工，而是让每个员工都有能力创建增强自己生产力的 AI Agent。」在企业实际测试中，Gumloop 击败了多个竞品——至少有一家客户在六个月试用后放弃了所有竞品方案，全面转向 Gumloop。<br><small>来源：<a href=\"https://www.indexbox.io/blog/gumloop-secures-50m-series-b-funding-led-by-benchmark-to-expand-ai-agent-platform/\">IndexBox</a> | <a href=\"https://cryptorank.io/news/feed/239ad-gumloop-benchmark-ai-agent-builder\">CryptoRank</a></small></li><li><strong>AI Agent 安全成为独立赛道：Manifold 获 800 万美元种子轮</strong> — 专注 AI Agent 安全的初创公司 Manifold 在本周融资 800 万美元。随着企业大规模部署自主 Agent，如何确保 Agent 的行为可控、数据不泄露、权限不被滥用，正在成为一个独立的技术和商业赛道。<br><small>来源：<a href=\"https://qubit.capital/blog/us-seed-weekly-funding-roundup-week-4-march-2026\">Qubit Capital</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>NVIDIA 从芯片到软件标准</strong>：NemoClaw 的真正意图不是做一个 Agent 平台，而是让 NVIDIA 的 CUDA 生态成为 AI Agent 时代的默认运行时</li><li><strong>多 Agent 协作成为主流架构</strong>：DeerFlow 2.0 代表了从「单一大模型」到「多 Agent 协作」的技术共识</li><li><strong>AI Agent 的「iPhone 时刻」</strong>：当 Gumloop 让非技术人员也能构建 Agent 时，Agent 的渗透率将出现指数级增长</li><li><strong>安全赛道独立化</strong>：Manifold 的 800 万美元融资证明 Agent 安全已从附属功能变成独立市场</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>这周的 AI Agent 领域出现了一个非常清晰的产业链分层：NVIDIA 做运行时基础设施（NemoClaw）、ByteDance 做协作框架（DeerFlow 2.0）、Gumloop 做终端用户界面、Manifold 做安全保障。这不是巧合——这是 Agent 生态系统正式进入「基础设施成熟期」的信号。</strong></p><p>先说最重要的一步棋：NVIDIA 的 NemoClaw。表面上这是一个「让企业安全地运行 AI Agent」的工具，但 Forbes 的分析一针见血——这是 NVIDIA 从「卖 GPU 的」到「定义 AI 软件标准的」的战略转型。Jensen Huang 的如意算盘是：当你在 NemoClaw 上构建 Agent 工作流，你自然会用 Nemotron 模型（NVIDIA 的）和 NIM 微服务（也是 NVIDIA 的），整个技术栈都锁定在 CUDA 生态里。<strong>「开源」和「非 NVIDIA 客户也能用」是糖衣，CUDA 锁定是药丸。</strong>这和 Google 开源 Android 的策略如出一辙——平台免费，生态收费。</p><p>但这里有一个有趣的张力。ByteDance 的 DeerFlow 2.0 也是开源的多 Agent 框架，且不绑定任何硬件生态。当 NVIDIA 试图用 NemoClaw 统一 Agent 基础设施时，字节跳动在另一个维度上推动「硬件无关」的 Agent 协作标准。再加上 OpenClaw 本身的社区力量（GitHub 上最多星标的项目），<strong>Agent 基础设施层正在出现一场「开源标准」vs「企业标准」的角力。</strong></p><p>Gumloop 的 5000 万美元融资是另一个值得深思的信号。Benchmark 是硅谷最挑剔的 VC 之一——它一次基金只投很少的项目。Benchmark 押注 Gumloop，说明它看到了一个被低估的趋势：<strong>AI Agent 的最大市场不是开发者，而是非技术员工。</strong>想想看，全球有几亿知识工作者每天在做重复性的数据整理、报告生成、流程审批——如果 Gumloop 真的能让他们自己构建 Agent 来处理这些任务，这就是一个比「AI 编程助手」大得多的市场。CEO Aisha Patel 的那句话说得好：「不是用 AI 取代员工，而是让每个员工成为 AI Agent 的构建者。」</p><p>最后把这些点连起来看。昨天我们讨论了白宫 AI 框架从联邦层面统一监管，今天我们看到 NVIDIA 从技术层面统一 Agent 运行时。<strong>2026 年的主线叙事正在从「AI 模型能力竞赛」转向「AI 基础设施标准之争」。</strong>谁定义了 Agent 的运行方式、安全标准、和协作协议，谁就掌握了下一个十年的平台权力。Manifold 拿到 800 万美元做 Agent 安全，证明这不只是技术问题——当自主 Agent 开始在企业中大规模运行时，「谁为 Agent 的行为负责」将成为法律、保险和合规行业的核心议题。<strong>我的预测：到 2026 年底，至少会有一起因 AI Agent 自主行为导致的重大企业损失事件，这将是 Agent 安全赛道的「催化剂时刻」。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>NVIDIA Launches NemoClaw: Enterprise Open-Source AI Agent Platform</strong> — Announced at GTC 2026, NemoClaw builds on OpenClaw with enterprise privacy/security controls. Pre-pitched to Salesforce, Cisco, Google, Adobe, CrowdStrike. Forbes calls it NVIDIA's strategic shift from chip company to AI software standard — the full stack (Nemotron + NIM) locks into CUDA. Open to non-NVIDIA customers as a neutrality play.<br><small>Source: <a href=\"https://www.cnbc.com/2026/03/10/nvidia-open-source-ai-agent-platform-nemoclaw-wired-agentic-tools-openclaw-clawdbot-moltbot.html\">CNBC</a> | <a href=\"https://www.forbes.com/sites/jonmarkman/2026/03/11/nvidia-moves-beyond-chips-with-an-open-source-platform-for-ai-agents/\">Forbes</a></small></li><li><strong>ByteDance Open-Sources DeerFlow 2.0: Multi-Agent Collaboration Framework</strong> — Each agent runs in isolated environments, coordinating through a unified workflow. Represents the shift from single-model to multi-agent architecture.<br><small>Source: <a href=\"https://github.com/bytedance/deer-flow\">GitHub</a></small></li><li><strong>Gumloop Raises $50M Series B from Benchmark for No-Code AI Agents</strong> — Non-technical employees build autonomous agents via natural language. CEO: 'The future is giving every employee tools to create AI agents.' One customer abandoned all competing tools after 6-month trial.<br><small>Source: <a href=\"https://www.indexbox.io/blog/gumloop-secures-50m-series-b-funding-led-by-benchmark-to-expand-ai-agent-platform/\">IndexBox</a></small></li><li><strong>Manifold Raises $8M for AI Agent Security</strong> — Dedicated agent security startup emerges as enterprises scale autonomous agent deployment.<br><small>Source: <a href=\"https://qubit.capital/blog/us-seed-weekly-funding-roundup-week-4-march-2026\">Qubit Capital</a></small></li></ul><h3>🔄 Trends</h3><ul><li>NVIDIA pivots from chips to software standard with NemoClaw</li><li>Multi-agent collaboration becomes consensus architecture</li><li>Non-technical agent building could be AI's 'iPhone moment'</li><li>Agent security emerges as independent market</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>This week's agent landscape reveals a clear stack forming: NVIDIA (runtime), ByteDance (framework), Gumloop (end-user interface), Manifold (security). This isn't coincidence — it signals agent infrastructure entering maturity.</strong> NemoClaw's 'open source for all' is the sugar coating; CUDA ecosystem lock-in is the real play — same strategy as Google open-sourcing Android. ByteDance's DeerFlow 2.0 pushes hardware-agnostic agent standards, creating tension with NVIDIA's approach. Gumloop's Benchmark-led round signals the biggest agent market isn't developers — it's hundreds of millions of knowledge workers doing repetitive tasks. Connecting to yesterday's White House framework: 2026's narrative is shifting from 'AI model capability race' to 'AI infrastructure standards war.' <strong>Prediction: by year-end, at least one major enterprise loss event caused by autonomous agent behavior will catalyze the agent security market.</strong></p></div>"
    },
    "cover": images.get("nemoclaw_cnbc", "") or images.get("nemoclaw_forbes", ""),
    "sources": [
        {
            "title": {"zh": "CNBC: NVIDIA 计划推出开源 AI Agent 平台 NemoClaw", "en": "CNBC: Nvidia Plans Open-Source AI Agent Platform NemoClaw"},
            "url": "https://www.cnbc.com/2026/03/10/nvidia-open-source-ai-agent-platform-nemoclaw-wired-agentic-tools-openclaw-clawdbot-moltbot.html",
            "image": images.get("nemoclaw_cnbc", "")
        },
        {
            "title": {"zh": "Forbes: NVIDIA 从芯片走向开源 AI Agent 平台", "en": "Forbes: Nvidia Moves Beyond Chips With Open-Source AI Agent Platform"},
            "url": "https://www.forbes.com/sites/jonmarkman/2026/03/11/nvidia-moves-beyond-chips-with-an-open-source-platform-for-ai-agents/",
            "image": images.get("nemoclaw_forbes", "")
        },
        {
            "title": {"zh": "ByteDance DeerFlow 2.0: 开源多 Agent 框架", "en": "ByteDance DeerFlow 2.0: Open-Source Multi-Agent Framework"},
            "url": "https://github.com/bytedance/deer-flow",
            "image": images.get("deerflow", "")
        },
        {
            "title": {"zh": "IndexBox: Gumloop 获 Benchmark 领投 5000 万美元 B 轮", "en": "IndexBox: Gumloop Secures $50M Series B Led by Benchmark"},
            "url": "https://www.indexbox.io/blog/gumloop-secures-50m-series-b-funding-led-by-benchmark-to-expand-ai-agent-platform/",
            "image": images.get("gumloop", "")
        },
        {
            "title": {"zh": "Qubit Capital: Manifold 获 800 万美元 AI Agent 安全融资", "en": "Qubit Capital: Manifold Raises $8M for AI Agent Security"},
            "url": "https://qubit.capital/blog/us-seed-weekly-funding-roundup-week-4-march-2026",
            "image": ""
        }
    ]
}

# Load existing issues and prepend
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\nDone! Inserted 2 new issues. Total: {len(issues)}")
