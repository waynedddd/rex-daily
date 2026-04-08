# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-04-08"""
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

# Fetch og:images
urls_to_fetch = [
    "https://thenextweb.com/news/slack-slackbot-30-ai-features-agentic",
    "https://fortune.com/2026/04/01/salesforce-reinvents-slack-ai-age-takes-aim-at-microsoft-copilot/",
    "https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/",
    "https://medium.com/ux-planet/claude-skills-for-product-designers-a453a7a8faa7",
    "https://www.designwhine.com/ai-for-ux-design-in-2026-messy-reality/",
    "https://medium.com/design-bootcamp/how-to-automate-your-ux-research-with-claude-cowork-with-prompts-249443c83723",
    "https://medium.com/user-experience-design-1/how-top-companies-are-using-ai-in-their-design-workflows-d10ec40fb6af",
]

og_images = {}
for url in urls_to_fetch:
    print(f"Fetching og:image for {url}...")
    og_images[url] = get_og_image(url)
    print(f"  -> {og_images[url][:80] if og_images[url] else '(none)'}")

# New issues to prepend
new_issues = [
    {
        "date": "2026-04-08",
        "section": "design",
        "title": {
            "zh": "AI 设计工具的「混乱现实」：从炒作到真实工作流 · Claude + Cowork 自动化 UX 研究实操指南 · 头部公司如何在设计流程中使用 AI",
            "en": "The Messy Reality of AI for UX Design · Claude + Cowork UX Research Automation Guide · How Top Companies Use AI in Design Workflows"
        },
        "content": {
            "zh": "<h3>\U0001f4cc AI × 设计</h3><ul><li><strong>DesignWhine 深度报告：「AI 用于 UX 设计的混乱现实」</strong> — DesignWhine 发布了一篇极为务实的长文，标题直接点破了 2026 年 AI 设计工具的真相：<strong>炒作期已过，但落地的混乱才刚开始</strong>。文章指出，大多数设计团队并没有像 Medium 热文描述的那样「用 AI 实现 10x 效率」——现实是工具碎片化严重，每个 AI 工具擅长一小块，但<strong>没有任何一个工具能覆盖完整的设计流程</strong>。设计师变成了「AI 工具协调员」，花大量时间在不同工具之间搬运数据和调整格式。真正受益的是已经有成熟设计系统的团队——AI 工具在有约束的环境里表现远好于从零开始。<br><small>来源：<a href=\"https://www.designwhine.com/ai-for-ux-design-in-2026-messy-reality/\">DesignWhine</a></small></li><li><strong>Design Bootcamp 热文：Claude + Cowork 自动化 UX 研究实操指南（含 Prompt）</strong> — 263 赞的实战文章详细拆解了如何用 Claude 和 Cowork 平台自动化 UX 研究的全流程——从用户访谈转录、主题聚类、到洞察提炼和报告生成。<strong>核心观点：AI 不是替代 UX 研究员，而是把研究中 70% 的苦力活（转录、编码、归类）自动化，让研究员专注于「问对问题」和「提炼洞察」。</strong>文章附带了完整的 Prompt 模板，具有很强的可操作性。这反映了一个趋势：Claude 正在从「编码工具」扩展为「设计研究工具」。<br><small>来源：<a href=\"https://medium.com/design-bootcamp/how-to-automate-your-ux-research-with-claude-cowork-with-prompts-249443c83723\">Design Bootcamp</a></small></li><li><strong>UX Collective：头部公司如何在设计工作流中使用 AI——交互、动效和营销全覆盖</strong> — UX Collective（668 赞）详细调研了头部公司的 AI 设计实践。关键发现：<strong>AI 在设计领域的应用正在从「生成 UI」扩展到「交互设计、动效设计和营销素材」三大方向</strong>。文章提到几个具体案例：某 SaaS 公司用 AI 生成动效原型后，设计师审核和微调的时间从 3 天缩短到 4 小时；营销团队用 AI 批量生成品牌一致的社交媒体素材，效率提升 5 倍。但文章也指出，<strong>AI 生成的交互动效「默认值」偏保守，缺乏品牌个性</strong>——设计师的价值恰恰在于打破 AI 的「安全区」。<br><small>来源：<a href=\"https://medium.com/user-experience-design-1/how-top-companies-are-using-ai-in-their-design-workflows-d10ec40fb6af\">UX Collective</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>从炒作到落地的「幻灭低谷」</strong>：AI 设计工具进入 Gartner 曲线的低谷期——期望值回调，但实际价值开始沉淀</li><li><strong>Claude 扩展到设计领域</strong>：从编码工具到 UX 研究自动化，Claude 正在成为设计师的通用 AI 助手</li><li><strong>AI 设计的真正瓶颈是整合</strong>：不是单个工具不够强，而是工具之间的数据流和上下文传递断裂</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天的设计新闻终于不是在吹 AI 工具多厉害了——而是开始讨论「为什么 AI 设计工具用起来这么累」。这是一个重要的信号：行业正在从炒作期进入务实期。</strong></p><p>DesignWhine 的「混乱现实」报告是我今年读到的最诚实的 AI 设计评测。让我翻译一下它的核心信息：<strong>2026 年的 AI 设计工具就像 2010 年的移动 App 生态——每个工具都解决一个具体问题，但没人解决「整合」问题。</strong>你用 Moonchild 生成 UI，用 Claude Code 写代码，用 Figma Make 做原型，用 Midjourney 做视觉素材——四个工具，四种格式，四套上下文。设计师花在工具切换上的时间可能已经抵消了 AI 带来的效率提升。</p><p>这就是为什么 Claude + Cowork 的 UX 研究自动化文章如此有价值。它不是在炫耀 AI 的能力，而是在展示一个<strong>有约束的、可落地的工作流</strong>——用 Claude 处理 UX 研究中最耗时的苦力活（转录、编码、归类），把 70% 的时间释放给高价值的思考工作。这恰好印证了上一期 NN/g 报告的结论：<strong>窄范围 AI 工具在具体任务上的表现远好于「万能 AI」。</strong>当你让 Claude 做一件事——分析访谈记录——它做得很好。当你让它「帮我设计一个完整的产品」——它做得很差。</p><p>UX Collective 的调研揭示了另一个有趣的现象：<strong>AI 生成的设计有一个「安全区」问题——所有输出都趋向于平庸的中间值。</strong>动效太规矩，配色太安全，布局太标准。这不是 bug，这是 AI 模型训练数据的统计学必然——它学的是「平均最佳实践」，不是「突破性创意」。这意味着设计师的价值不在于生成，而在于<strong>编辑和突破</strong>——把 AI 的 80 分起点推向 95 分。</p><p>把三条新闻连起来看，我看到一个清晰的模式：<strong>AI 设计工具的价值不在于替代设计师，而在于压缩「苦力时间」（研究转录、素材生成、原型搭建），释放「思考时间」（定义问题、判断方向、突破创意）。</strong>但目前最大的障碍是工具碎片化——谁能先解决 AI 设计工具之间的整合问题，谁就拿到了下一阶段的入场券。</p><p><strong>我的预判：2026 年下半年会出现「AI 设计编排层」——一个不自己生成设计，而是协调 Moonchild、Claude Code、Figma Make 等工具协同工作的中间件。Figma 最有可能成为这个编排层，但前提是它从「设计工具」真正转型为「设计平台」。另一个预判：Claude 在设计领域的渗透会加速——从 UX 研究到设计批评到可用性评估，Claude 正在成为设计师的「AI 同事」而非「AI 工具」。</strong></p></div>",
            "en": "<h3>\U0001f4cc AI × Design</h3><ul><li><strong>DesignWhine Deep Dive: The Messy, Magnificent Reality of AI for UX Design in 2026</strong> — DesignWhine published a brutally honest long-form piece cutting through the noise: <strong>the hype cycle is over, but the messy reality of implementation has just begun</strong>. Most design teams aren't achieving the \"10x efficiency\" promised by Medium hot takes — the reality is severe tool fragmentation where each AI tool excels at one piece but <strong>no single tool covers the complete design workflow</strong>. Designers have become \"AI tool coordinators,\" spending significant time shuttling data between tools. Teams with mature design systems benefit most — AI tools perform far better within constraints than starting from scratch.<br><small>Source: <a href=\"https://www.designwhine.com/ai-for-ux-design-in-2026-messy-reality/\">DesignWhine</a></small></li><li><strong>Design Bootcamp: Claude + Cowork UX Research Automation Guide (With Prompts)</strong> — A 263-clap practical guide breaking down how to automate UX research using Claude and Cowork — from interview transcription, thematic clustering, to insight extraction and report generation. <strong>Core thesis: AI doesn't replace UX researchers, it automates 70% of grunt work (transcription, coding, categorization), freeing researchers to focus on asking the right questions and extracting insights.</strong> Includes complete prompt templates. This reflects Claude's expansion from \"coding tool\" to \"design research tool.\"<br><small>Source: <a href=\"https://medium.com/design-bootcamp/how-to-automate-your-ux-research-with-claude-cowork-with-prompts-249443c83723\">Design Bootcamp</a></small></li><li><strong>UX Collective: How Top Companies Use AI in Design Workflows — Interactions, Motion & Marketing</strong> — UX Collective (668 claps) surveyed how leading companies apply AI in design. Key finding: <strong>AI in design is expanding from \"generating UI\" to three directions: interaction design, motion design, and marketing assets</strong>. One SaaS company cut motion prototype review time from 3 days to 4 hours; marketing teams achieved 5x efficiency in brand-consistent social media assets. But the article notes <strong>AI-generated motion defaults are conservative and lack brand personality</strong> — designers' value lies in breaking AI's \"safe zone.\"<br><small>Source: <a href=\"https://medium.com/user-experience-design-1/how-top-companies-are-using-ai-in-their-design-workflows-d10ec40fb6af\">UX Collective</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Trough of disillusionment: AI design tools enter Gartner's trough — expectations adjust down, but real value starts crystallizing</li><li>Claude expands into design: from coding tool to UX research automation, becoming designers' general AI assistant</li><li>Integration is the real bottleneck: individual tools are strong enough, but data flow between them is broken</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Today's design news finally stops cheerleading AI tools and starts asking \"why are AI design tools so exhausting to use?\" This is an important signal: the industry is moving from hype to pragmatism.</strong></p><p>DesignWhine's \"messy reality\" report is the most honest AI design assessment I've read this year. Let me translate its core message: <strong>2026's AI design tools are like the 2010 mobile app ecosystem — every tool solves a specific problem, but nobody solves the \"integration\" problem.</strong> You use Moonchild for UI generation, Claude Code for development, Figma Make for prototyping, Midjourney for visual assets — four tools, four formats, four contexts. The time designers spend on tool-switching may already offset AI's efficiency gains.</p><p>This is why the Claude + Cowork UX research automation article is so valuable. It's not showing off AI capabilities but demonstrating a <strong>constrained, implementable workflow</strong> — using Claude for the most time-consuming grunt work in UX research, freeing 70% of time for high-value thinking. This confirms NN/g's finding: <strong>narrow-scope AI tools dramatically outperform \"universal AI.\"</strong></p><p>UX Collective's survey reveals another fascinating phenomenon: <strong>AI-generated design has a \"safe zone\" problem — all outputs converge toward mediocre averages.</strong> Motion too conservative, colors too safe, layouts too standard. This isn't a bug but a statistical inevitability of training data — it learns \"average best practices,\" not \"breakthrough creativity.\" Designers' value isn't in generation but in <strong>editing and breaking through</strong> — pushing AI's 80-point starting point to 95.</p><p><strong>My prediction: H2 2026 will see an \"AI design orchestration layer\" emerge — middleware that doesn't generate design itself but coordinates Moonchild, Claude Code, and Figma Make. Figma is best positioned but must truly transform from \"design tool\" to \"design platform.\" Also: Claude's penetration in design will accelerate — from UX research to design critique to usability evaluation, becoming designers' \"AI colleague\" rather than \"AI tool.\"</strong></p></div>"
        },
        "cover": og_images.get("https://www.designwhine.com/ai-for-ux-design-in-2026-messy-reality/", ""),
        "sources": [
            {
                "title": {
                    "zh": "AI 用于 UX 设计的混乱现实（2026）",
                    "en": "The Messy, Magnificent Reality of AI for UX Design in 2026"
                },
                "url": "https://www.designwhine.com/ai-for-ux-design-in-2026-messy-reality/",
                "image": og_images.get("https://www.designwhine.com/ai-for-ux-design-in-2026-messy-reality/", "")
            },
            {
                "title": {
                    "zh": "如何用 Claude + Cowork 自动化 UX 研究",
                    "en": "How to Automate Your UX Research With Claude + Cowork"
                },
                "url": "https://medium.com/design-bootcamp/how-to-automate-your-ux-research-with-claude-cowork-with-prompts-249443c83723",
                "image": og_images.get("https://medium.com/design-bootcamp/how-to-automate-your-ux-research-with-claude-cowork-with-prompts-249443c83723", "")
            },
            {
                "title": {
                    "zh": "头部公司如何在设计工作流中使用 AI",
                    "en": "How Top Companies Are Using AI in Their Design Workflows"
                },
                "url": "https://medium.com/user-experience-design-1/how-top-companies-are-using-ai-in-their-design-workflows-d10ec40fb6af",
                "image": og_images.get("https://medium.com/user-experience-design-1/how-top-companies-are-using-ai-in-their-design-workflows-d10ec40fb6af", "")
            }
        ]
    },
    {
        "date": "2026-04-08",
        "section": "tech",
        "title": {
            "zh": "Salesforce 将 Slackbot 改造为「AI Agent 操作系统」：30 项新功能正面对标 Microsoft Copilot · Google TurboQuant：ICLR 2026 极限压缩算法重新定义 AI 效率 · AI 企业战争：Slack vs Teams vs Copilot 的三角博弈",
            "en": "Salesforce Transforms Slackbot into 'Agentic OS' with 30 AI Features vs Microsoft Copilot · Google TurboQuant: Extreme Compression at ICLR 2026 · Enterprise AI War: Slack vs Teams vs Copilot"
        },
        "content": {
            "zh": "<h3>\U0001f4cc AI × 科技</h3><ul><li><strong>Salesforce 重磅升级 Slack：30 项 AI 功能把 Slackbot 变成「Agent 操作系统」</strong> — 3 月 31 日旧金山发布会上，Marc Benioff 公布了 Slackbot 有史以来最大的更新——<strong>30+ 项 AI 驱动能力，包括会议转录、桌面监控、自主任务执行</strong>。Salesforce 的野心很明确：把 Slack 从聊天工具变成「Agentic 操作系统」——一个用户与 AI Agent、企业应用和同事交互的统一界面。技术底层选择了 Anthropic Claude（因为 FedRAMP 合规要求），并支持 MCP 协议连接第三方 Agent。<strong>这是对 Microsoft Copilot 的正面宣战</strong>——Slack 的论点是「通信优先的界面比文档优先的界面更适合承载 AI Agent」。但 Salesforce 股价今年已跌 30%，「SaaSpocalypse」的焦虑弥漫——Benioff 必须证明 AI 是 Salesforce 的武器而非掘墓人。<br><small>来源：<a href=\"https://thenextweb.com/news/slack-slackbot-30-ai-features-agentic\">The Next Web</a>、<a href=\"https://fortune.com/2026/04/01/salesforce-reinvents-slack-ai-age-takes-aim-at-microsoft-copilot/\">Fortune</a></small></li><li><strong>Google TurboQuant 论文亮相 ICLR 2026：极限压缩让大模型「瘦身」不掉智商</strong> — Google Research 发布了 TurboQuant——一种将在 ICLR 2026 大会上展示的模型压缩算法。核心突破：<strong>在极端量化条件下（低至 2-bit）保持模型性能的最优方案</strong>。这对 AI 民主化意义重大——压缩后的大模型可以在消费级硬件（手机、笔记本、树莓派）上运行，打破 GPU 集群的算力垄断。TurboQuant 不是增量优化，而是在压缩效率的理论极限上取得突破。这与 Gemma 4 的 Apache 2.0 开源形成组合拳——<strong>Google 的策略越来越清晰：用「免费 + 高效」的开源方案蚕食 OpenAI 和 Anthropic 的付费模型市场</strong>。<br><small>来源：<a href=\"https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/\">Google Research Blog</a></small></li><li><strong>AI 企业战争升级：Slack「Agent OS」 vs Microsoft Copilot vs Google Workspace AI</strong> — 本周的 Slack 更新标志着企业 AI 进入三巨头混战阶段。Microsoft Copilot 嵌入 Office 全家桶，以「文档 + 数据」为核心；Slack 以「通信 + Agent」为核心，主打 MCP 协议开放性；Google 则在底层发力（Gemma 4 开源 + TurboQuant 压缩），走「基础设施 + 开源生态」路线。三种截然不同的企业 AI 哲学正在碰撞——<strong>未来两个季度将决定哪种范式胜出</strong>。值得注意的是，Salesforce 选择 Anthropic Claude 而非 GPT 作为 Slack AI 的底层，Cursor 用了月之暗面的 Kimi K2.5——<strong>「最佳 AI」不再等于 OpenAI</strong>，市场正在多极化。<br><small>来源：<a href=\"https://startupfortune.com/salesforce-stuffs-30-ai-skills-into-slackbot-in-bold-copilot-mirror-move/\">StartupFortune</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>企业 AI 的「操作系统」之争</strong>：Slack、Teams、Google Workspace 都在争夺「AI Agent 运行环境」的定位</li><li><strong>模型压缩 = AI 民主化</strong>：TurboQuant + Gemma 4 让大模型脱离 GPU 集群，走向消费级设备</li><li><strong>AI 供应商多极化</strong>：OpenAI 不再是唯一选择，Anthropic 和开源模型正在分流企业客户</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Salesforce 这次 Slack 更新的规模之大，让我想到了一个词：「生死一搏」。在股价暴跌 30%、SaaSpocalypse 叙事笼罩下，Benioff 不是在做产品迭代——他是在赌 Salesforce 的未来。</strong></p><p>让我把 Slack 的「Agentic OS」放在更大的格局下看。上期我们讨论了 OpenAI 提出「机器人税」——那是 AI 行业面对社会后果的标志。而 Slack 的更新则是 AI 行业面对<strong>商业后果</strong>的标志。Salesforce 是「SaaSpocalypse」的典型受害者——当 AI 可以直接帮用户完成 CRM 任务时，谁还需要一个复杂的 Salesforce 界面？Benioff 的回应是：<strong>如果 AI 要取代 SaaS，那就让 Slack 成为 AI 的「家」</strong>。30 项 AI 功能、MCP 协议支持、Anthropic Claude 底层——这不是功能更新，这是平台转型。</p><p>但我对这个策略有两个疑虑。第一，<strong>「桌面监控」这个功能让人不寒而栗</strong>——一个 AI Agent 在后台监控你的桌面活动并自主执行任务？这在隐私敏感的欧洲市场几乎不可能推广。Salesforce 选择 Claude 是因为 FedRAMP 合规，但 FedRAMP 解决的是政府安全标准，不是员工隐私问题。这个功能如果处理不好，可能变成 Slack 的「PR 灾难」。</p><p>第二，<strong>Slack 的「通信优先 > 文档优先」论点听起来合理，但忽略了一个事实：企业的核心资产是数据和文档，不是聊天记录。</strong>Microsoft Copilot 可以直接访问 Excel、Word、PowerPoint 和 SharePoint 中的企业数据——这是 Slack 做不到的。MCP 协议可以连接第三方应用，但连接的深度和 Microsoft 365 原生集成完全不是一个量级。</p><p>Google 的策略才是我最感兴趣的。TurboQuant + Gemma 4 Apache 2.0 的组合拳，本质上是在说：<strong>「你不需要为 AI 付高价——我们给你免费的模型和极致的压缩技术，在你自己的硬件上跑。」</strong>这对 OpenAI 和 Anthropic 的付费模型是釜底抽薪式的威胁。想想看：如果一个 2-bit 量化的 Gemma 4 可以在 MacBook Pro 上以可接受的质量运行，谁还愿意每月给 OpenAI 交 $200 的 API 费用？</p><p><strong>把今天的设计和科技新闻连起来，我看到一个大趋势的两个面向：AI 工具的「碎片化困境」正在从设计领域蔓延到企业级应用</strong>——设计师在 Moonchild、Claude Code、Figma Make 之间切换，企业用户在 Slack、Teams、Google Workspace 之间纠结。<strong>整合将是 2026 年下半年最值钱的能力——不管是设计工具的编排层，还是企业 AI 的统一平台。</strong></p><p><strong>我的预判：Slack 的「Agentic OS」会在北美企业市场获得初步认可，但桌面监控功能会在欧洲遭遇 GDPR 阻力。Google 的 TurboQuant + Gemma 4 开源策略将在 Q3 显著冲击付费 API 模型的定价——预计 OpenAI 和 Anthropic 会在年中被迫降价 30-50%。而 AI 供应商多极化的趋势不可逆——2026 年底，没有任何一家 AI 公司的市场份额会超过 40%。</strong></p></div>",
            "en": "<h3>\U0001f4cc AI × Tech</h3><ul><li><strong>Salesforce Massively Upgrades Slack: 30 AI Features Transform Slackbot into 'Agentic Operating System'</strong> — At a San Francisco event on March 31, Marc Benioff unveiled Slackbot's biggest-ever update — <strong>30+ AI capabilities including meeting transcription, desktop monitoring, and autonomous task execution</strong>. Salesforce's ambition: transform Slack from a chat tool into an \"agentic operating system\" — a unified surface for users to interact with AI agents, enterprise apps, and colleagues. Built on Anthropic Claude (chosen for FedRAMP compliance) with MCP protocol support for third-party agents. <strong>This is a direct assault on Microsoft Copilot</strong> — Slack argues \"communication-first interfaces are better homes for AI agents than document-first ones.\" But with Salesforce stock down 30% this year amid \"SaaSpocalypse\" fears, Benioff must prove AI is Salesforce's weapon, not its gravedigger.<br><small>Source: <a href=\"https://thenextweb.com/news/slack-slackbot-30-ai-features-agentic\">The Next Web</a>, <a href=\"https://fortune.com/2026/04/01/salesforce-reinvents-slack-ai-age-takes-aim-at-microsoft-copilot/\">Fortune</a></small></li><li><strong>Google TurboQuant at ICLR 2026: Extreme Compression Redefines AI Efficiency</strong> — Google Research released TurboQuant, a model compression algorithm to be presented at ICLR 2026. Core breakthrough: <strong>maintaining model performance under extreme quantization (down to 2-bit)</strong>. This matters for AI democratization — compressed models can run on consumer hardware (phones, laptops, Raspberry Pi), breaking GPU cluster monopoly. Combined with Gemma 4's Apache 2.0 release, <strong>Google's strategy is clear: use \"free + efficient\" open-source to erode OpenAI and Anthropic's paid model market</strong>.<br><small>Source: <a href=\"https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/\">Google Research Blog</a></small></li><li><strong>Enterprise AI War Escalates: Slack 'Agent OS' vs Microsoft Copilot vs Google Workspace AI</strong> — This week's Slack update marks enterprise AI entering a three-way battle. Microsoft Copilot embeds in Office with \"documents + data\" at its core; Slack centers on \"communication + agents\" with MCP openness; Google plays infrastructure (Gemma 4 open-source + TurboQuant compression). <strong>The next two quarters will determine which paradigm wins.</strong> Notable: Salesforce chose Anthropic Claude over GPT for Slack AI, Cursor uses Moonshot's Kimi K2.5 — <strong>\"best AI\" no longer equals OpenAI</strong>, the market is multipolarizing.<br><small>Source: <a href=\"https://startupfortune.com/salesforce-stuffs-30-ai-skills-into-slackbot-in-bold-copilot-mirror-move/\">StartupFortune</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Enterprise AI's \"operating system\" war: Slack, Teams, Google Workspace all competing to be the AI agent runtime</li><li>Model compression = AI democratization: TurboQuant + Gemma 4 free models from GPU clusters to consumer devices</li><li>AI vendor multipolarization: OpenAI no longer the default, Anthropic and open-source splitting enterprise clients</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>The scale of Salesforce's Slack update brings one word to mind: \"all-in.\" With stock down 30% and SaaSpocalypse narrative looming, Benioff isn't iterating — he's betting Salesforce's future.</strong></p><p>Let me contextualize Slack's \"Agentic OS.\" Last issue we discussed OpenAI's \"robot tax\" — marking the industry facing social consequences. Slack's update marks the industry facing <strong>commercial consequences</strong>. Salesforce is the poster child for SaaSpocalypse — when AI can directly handle CRM tasks, who needs a complex Salesforce interface? Benioff's response: <strong>if AI will replace SaaS, make Slack AI's \"home.\"</strong></p><p>Two concerns. First, <strong>desktop monitoring is chilling</strong> — an AI agent watching your screen and autonomously executing tasks? Nearly impossible to deploy in privacy-sensitive European markets. FedRAMP solves government security, not employee privacy. If mishandled, this becomes Slack's PR disaster.</p><p>Second, <strong>Slack's \"communication-first > document-first\" argument ignores a fact: enterprises' core assets are data and documents, not chat logs.</strong> Microsoft Copilot accesses Excel, Word, PowerPoint, and SharePoint natively — a depth Slack's MCP connections can't match.</p><p>Google's strategy fascinates me most. TurboQuant + Gemma 4 Apache 2.0 essentially says: <strong>\"You don't need to pay premium for AI — here's free models and extreme compression, run them on your own hardware.\"</strong> If a 2-bit quantized Gemma 4 runs acceptably on a MacBook Pro, who pays $200/month for OpenAI APIs?</p><p><strong>Connecting design and tech news: AI's \"fragmentation problem\" is spreading from design tools to enterprise applications.</strong> Designers switch between Moonchild, Claude Code, Figma Make; enterprises agonize over Slack, Teams, Google Workspace. <strong>Integration will be 2026 H2's most valuable capability.</strong></p><p><strong>Predictions: Slack's Agentic OS gains traction in North America but hits GDPR resistance in Europe. Google's TurboQuant + Gemma 4 strategy will significantly pressure paid API pricing by Q3 — expect OpenAI and Anthropic to cut prices 30-50% by mid-year. AI vendor multipolarization is irreversible — by year-end, no single AI company will hold over 40% market share.</strong></p></div>"
        },
        "cover": og_images.get("https://thenextweb.com/news/slack-slackbot-30-ai-features-agentic", ""),
        "sources": [
            {
                "title": {
                    "zh": "Slack 最大 AI 更新：Slackbot 变身桌面 Agent",
                    "en": "Slack's Biggest AI Update Turns Slackbot into a Desktop Agent"
                },
                "url": "https://thenextweb.com/news/slack-slackbot-30-ai-features-agentic",
                "image": og_images.get("https://thenextweb.com/news/slack-slackbot-30-ai-features-agentic", "")
            },
            {
                "title": {
                    "zh": "Google TurboQuant：用极限压缩重新定义 AI 效率",
                    "en": "TurboQuant: Redefining AI Efficiency with Extreme Compression"
                },
                "url": "https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/",
                "image": og_images.get("https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/", "")
            },
            {
                "title": {
                    "zh": "Salesforce 为 Slackbot 塞入 30 项 AI 技能",
                    "en": "Salesforce Stuffs 30 AI Skills into Slackbot"
                },
                "url": "https://startupfortune.com/salesforce-stuffs-30-ai-skills-into-slackbot-in-bold-copilot-mirror-move/",
                "image": ""
            }
        ]
    }
]

# Read existing issues.json and prepend
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r", encoding="utf-8") as f:
    existing = json.load(f)

updated = new_issues + existing

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w", encoding="utf-8") as f:
    json.dump(updated, f, ensure_ascii=False, indent=2)

print(f"\nDone! Prepended {len(new_issues)} issues. Total: {len(updated)}")
