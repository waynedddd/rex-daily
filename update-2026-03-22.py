# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-03-22"""
import json, re, urllib.request, urllib.error, ssl

def fetch_og_image(url, timeout=8):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            html = r.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
        return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images for sources
design_urls = [
    "https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/",
    "https://www.theregister.com/2026/03/19/google_stitch_vibe_design_update/",
    "https://www.figma.com/reports/state-of-the-designer-2026/",
    "https://www.figma.com/blog/state-of-the-designer-2026/",
]
tech_urls = [
    "https://www.axios.com/2026/03/11/perplexity-personal-computer-mac",
    "https://www.theregister.com/2026/03/12/perplexity_extends_cloud_computer_to_enterprise/",
    "https://www.artificialintelligence-news.com/news/visa-prepares-payment-systems-for-ai-agent-initiated-transactions/",
    "https://fortune.com/2026/03/13/elon-musk-morgan-stanley-ai-leap-2026/",
]

print("Fetching og:images...")
all_urls = design_urls + tech_urls
og = {}
for u in all_urls:
    img = fetch_og_image(u)
    og[u] = img
    print(f"  {u[:60]}... -> {'✓' if img else '✗'}")

design_issue = {
    "date": "2026-03-22",
    "section": "design",
    "title": {
        "zh": "Google 造了个新词「Vibe Design」· Stitch 大改版：语音输入+无限画布+实时 AI 评审 · Figma《设计师现状 2026》：89% 设计师因 AI 提速，但 Craft 才是幸福感来源",
        "en": "Google Coins 'Vibe Design' · Stitch Gets Voice, Infinite Canvas & AI Critique · Figma State of the Designer 2026: 89% Work Faster with AI, but Craft Is What Makes Designers Happy"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Google 发布「Vibe Design」概念，Stitch 迎来史上最大改版</strong> — Google Labs 本周正式提出「Vibe Design」概念（对标 Vibe Coding），并对 Stitch 进行全面重构：新增 AI 原生无限画布、语音输入驱动设计、实时 AI 设计评审（「帮我看看这个落地页」「给我三种菜单方案」）。Stitch 不再只是一个从文字生成 UI 的工具，而是进化为一个可以从粗略想法到可点击原型的全流程 AI 设计平台。Google Labs 产品经理 Rustin Banks 表示：「过去一年，AI 从根本上改变了我们构建软件的方式——现在轮到设计了。」<br><small>来源：<a href=\"https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/\">Google 官方博客</a> | <a href=\"https://www.theregister.com/2026/03/19/google_stitch_vibe_design_update/\">The Register</a></small></li><li><strong>Figma 发布《设计师现状 2026》报告：AI 让 89% 的设计师工作更快，但 Craft 才是核心</strong> — Figma 调研了全球 906 名设计师，核心发现：89% 表示 AI 让他们工作更快，80% 表示协作更顺畅。但报告最有意思的结论不是 AI 的效率提升——而是<strong>Craft（手艺/精工）是设计师幸福感和商业成果的关键驱动力。</strong>报告指出，能保持高 Craft 标准的设计师对职业前景更乐观，他们把 AI 当作放大器而非替代品。在 AI 做掉越来越多执行层工作的 2026 年，Figma 的立场很明确：<strong>AI 提速度，Craft 定高度。</strong><br><small>来源：<a href=\"https://www.figma.com/reports/state-of-the-designer-2026/\">Figma State of the Designer 2026</a> | <a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a></small></li><li><strong>Muzli 本周热门：从 Vibe Design 到 MCP-First 工作流</strong> — 设计社区本周话题集中在两个方向：一是 Google 的 Vibe Design 概念引发的「设计也能 Vibe 吗？」大讨论；二是 MCP（Model Context Protocol）驱动的 Design-to-Code 工作流逐渐成形——设计文件不再只是视觉稿，而是可以直接被 AI 理解和转码的结构化上下文。<br><small>来源：<a href=\"https://muz.li/blog/best-ai-design-tools-for-ui-ux-designers-in-2026/\">Muzli</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「Vibe Design」成为新叙事</strong>：继 Vibe Coding 之后，Google 正式将「凭感觉设计」概念化</li><li><strong>Craft 回归</strong>：AI 效率越高，设计师的手艺和判断力反而越值钱</li><li><strong>语音+AI 正在成为设计交互的新范式</strong>：Stitch 的语音驱动设计暗示了未来工具交互的方向</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Google 本周干了一件很 Google 的事：它没有发明什么新技术，但发明了一个新词——「Vibe Design」。而这个词可能比任何技术更新都更有影响力。</strong></p><p>先回顾一下背景。「Vibe Coding」这个概念在 2025 年由 Andrej Karpathy 提出后，迅速改变了开发者社区对 AI 编程的心理预期——你不需要精确描述每一行代码该怎么写，你只需要「给个 vibe」，AI 帮你实现。这个叙事之所以成功，不是因为技术有多强（GPT-4 时代的代码生成就已经很强了），而是因为它<strong>降低了人们尝试 AI 的心理门槛</strong>：「Vibe」意味着「不完美也可以」「先出来再说」「过程可以松弛」。</p><p>现在 Google 把同样的叙事搬到了设计领域。Stitch 的语音输入+无限画布+实时 AI 评审，技术上并不是革命性突破——Figma Make 也能从 prompt 生成 UI，Motiff 也有 AI 评审功能。但「Vibe Design」这个框架做到了三件事：第一，它给非设计师一个心理许可——「我不会设计，但我可以 vibe」；第二，它把 Stitch 从一个工具定位拉升到了一个运动/范式的高度；第三，它直接攻击了 Figma 的核心叙事。</p><p>怎么理解这第三点？看看 Figma 同期发布的《设计师现状 2026》报告就明白了。Figma 的核心论点是「Craft 才是设计师的护城河」——89% 因 AI 提速，但 Craft 定高度。这是一个<strong>面向专业设计师的防御性叙事</strong>：别慌，AI 只是工具，你的手艺才是核心价值。而 Google 的「Vibe Design」是一个<strong>面向所有人的进攻性叙事</strong>：谁都能设计，不需要手艺，给个感觉就行。</p><p>这两个叙事的冲突，本质上是设计工具市场的路线之争：<strong>Figma 赌设计师的专业壁垒会持续存在，Google 赌这个壁垒会被 AI 抹平。</strong>有意思的是，他们可能都对——但在不同的市场里对。对于需要品牌一致性、设计系统、复杂交互的企业级产品，Craft 确实不可替代。但对于 landing page、MVP 原型、内部工具这些「够用就行」的场景，Vibe Design 足矣。这就像 Canva 和 Photoshop 的关系——Canva 没有杀死 Photoshop，但它让 90% 的人不再需要 Photoshop。</p><p>我的预测：<strong>「Vibe Design」会在 2026 年下半年成为设计领域最热的 buzzword，但真正受冲击的不是高端设计师，而是那些做「还行但没啥特色」的中端设计工作的人。</strong>Figma 报告里有一个数据没有被充分讨论：80% 的设计师说 AI 让协作更好了——但协作更好可能也意味着「需要更少的设计师来完成同样的工作」。当 AI 处理了 80% 的执行层，而 Vibe Design 又让非设计师能自己搞定简单需求，<strong>中间层的设计师正在被两头挤压</strong>。Figma 的「Craft」叙事是对的，但它只对那些真正有 Craft 的人有用——这是一个残酷的筛选。</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Google Introduces 'Vibe Design' with Major Stitch Overhaul</strong> — Google Labs coined 'Vibe Design' (parallel to Vibe Coding) and rebuilt Stitch with AI-native infinite canvas, voice-driven design input, and real-time AI design critiques. Stitch evolves from a text-to-UI generator into a full-flow AI design platform.<br><small>Source: <a href=\"https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/\">Google Blog</a> | <a href=\"https://www.theregister.com/2026/03/19/google_stitch_vibe_design_update/\">The Register</a></small></li><li><strong>Figma State of the Designer 2026: 89% Work Faster with AI, Craft Is Key</strong> — Survey of 906 designers reveals AI speeds up work for 89% and improves collaboration for 80%. But the real insight: designers who maintain high craft standards are happier and produce better business outcomes. Figma's thesis: AI accelerates, Craft elevates.<br><small>Source: <a href=\"https://www.figma.com/reports/state-of-the-designer-2026/\">Figma Report</a></small></li></ul><h3>🔄 Trends</h3><ul><li>'Vibe Design' emerges as new narrative — Google formalizes 'design by feeling'</li><li>Craft renaissance: the more AI handles execution, the more human judgment appreciates</li><li>Voice + AI becoming new design interaction paradigm</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Google didn't invent new technology this week — it invented a new word: 'Vibe Design.' And that word may matter more than any technical update.</strong></p><p>The narrative conflict is clear: Figma's 'Craft is your moat' (defensive, pro-designer) vs Google's 'Anyone can Vibe Design' (offensive, democratizing). Both are right — in different markets. Enterprise products need craft; landing pages and MVPs just need vibes. Like Canva vs Photoshop: Canva didn't kill Photoshop, but made 90% of people not need it. <strong>Prediction: 'Vibe Design' becomes 2026's hottest design buzzword, but the real casualties aren't top designers — they're mid-tier designers squeezed between AI execution and non-designer self-service.</strong></p></div>"
    },
    "cover": og.get(design_urls[0], ""),
    "sources": [
        {
            "title": {"zh": "Google 官方博客：用 Stitch 引入「Vibe Design」", "en": "Google Blog: Introducing 'Vibe Design' with Stitch"},
            "url": "https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/",
            "image": og.get(design_urls[0], "")
        },
        {
            "title": {"zh": "The Register: Google 推出语音驱动「Vibe Design」工具", "en": "The Register: Google Offers Voice-Driven 'Vibe Design' Tool"},
            "url": "https://www.theregister.com/2026/03/19/google_stitch_vibe_design_update/",
            "image": og.get(design_urls[1], "")
        },
        {
            "title": {"zh": "Figma《设计师现状 2026》报告", "en": "Figma State of the Designer 2026 Report"},
            "url": "https://www.figma.com/reports/state-of-the-designer-2026/",
            "image": og.get(design_urls[2], "")
        },
        {
            "title": {"zh": "Figma Blog: AI 推动设计手艺更进一步", "en": "Figma Blog: AI Pushes Craft Further"},
            "url": "https://www.figma.com/blog/state-of-the-designer-2026/",
            "image": og.get(design_urls[3], "")
        }
    ]
}

tech_issue = {
    "date": "2026-03-22",
    "section": "tech",
    "title": {
        "zh": "AI Agent 本周全面提速 · Perplexity「个人电脑」让 AI 住进你的 Mac · Visa 测试 AI 自主支付 · Morgan Stanley 警告：一场 AI 突破正在临近，世界还没准备好",
        "en": "AI Agents Accelerate This Week · Perplexity 'Personal Computer' Brings AI Home · Visa Tests AI-Initiated Payments · Morgan Stanley Warns: An AI Breakthrough Is Imminent"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Perplexity 发布「个人电脑」：AI Agent 正式入住你的本地机器</strong> — Perplexity 在其首届开发者大会 Ask Conference 上发布「Personal Computer」——一个运行在本地 Mac（如 Mac mini）上的 AI Agent 系统，可以完全访问本地文件和应用，类似于 Anthropic 的 Computer Use 但更注重安全性：所有操作需用户确认，内置审计追踪。同时发布了 Computer for Enterprise（云端版），可编排 19 个 AI 模型并行工作、创建子 Agent、自动化工具使用。Perplexity 的定位很有趣：它没有自研前沿模型，而是做<strong>模型编排层</strong>——用一个统一入口调度 OpenAI、Anthropic、Google 等多家模型。<br><small>来源：<a href=\"https://www.axios.com/2026/03/11/perplexity-personal-computer-mac\">Axios</a> | <a href=\"https://www.theregister.com/2026/03/12/perplexity_extends_cloud_computer_to_enterprise/\">The Register</a></small></li><li><strong>Visa 推出「Agentic Ready」计划：AI Agent 可以替你付款了</strong> — Visa 在欧洲启动「Agentic Ready」试点项目，与 Commerzbank 和 DZ Bank 合作测试 AI Agent 发起的自主支付。这意味着 AI 不只是帮你查信息、写邮件——它可以在预设规则内直接替你花钱。Visa 的 Intelligent Commerce（VIC）全球倡议提供 API、标准和合作伙伴生态，为 AI Agent 的安全支付能力铺路。Mastercard 也在推类似的 Agent Pay 方案。支付行业正在成为 AI Agent 自主行动的第一个大规模试验场。<br><small>来源：<a href=\"https://www.artificialintelligence-news.com/news/visa-prepares-payment-systems-for-ai-agent-initiated-transactions/\">AI News</a></small></li><li><strong>Morgan Stanley 警告：2026 上半年将出现重大 AI 突破，大多数人没准备好</strong> — Morgan Stanley 发布重磅报告，预测 AI 能力将在 2026 上半年实现变革性飞跃，驱动因素是美国顶级 AI 实验室史无前例的算力积累。多家 AI 公司高管私下暗示：即将发布的模型性能提升将超出预期。报告还提到 AI 研究者关于「递归自我改进」（recursive self-improvement）的预测。同时警告美国到 2028 年可能面临 9-18 GW 电力缺口，相当于 AI 数据中心需求的 12-25%。<br><small>来源：<a href=\"https://fortune.com/2026/03/13/elon-musk-morgan-stanley-ai-leap-2026/\">Fortune</a></small></li><li><strong>微软考虑对亚马逊和 OpenAI 提起诉讼</strong> — 据 FT 报道，微软正在考虑对亚马逊和 OpenAI 采取法律行动，原因是双方新达成的 500 亿美元云服务协议可能违反了微软独家托管 OpenAI 模型的 Azure 合约。这是 AI 云基础设施领域最大的商业冲突之一，暗示 AI 平台的利益格局正在因巨额资金而发生裂变。<br><small>来源：<a href=\"https://www.ft.com/content/e814f4c3-4fb5-4e2e-90a6-470044436b39\">Financial Times</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI Agent 从「做事」到「花钱」</strong>：Visa 的试点标志着 Agent 自主权的新边界</li><li><strong>模型编排 > 模型自研</strong>：Perplexity 押注的不是最强模型，而是最好的模型调度</li><li><strong>AI 基建的商业摩擦加剧</strong>：微软 vs 亚马逊/OpenAI 预示着云+AI 的利益重构</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>这周的科技新闻有一条暗线值得注意：AI Agent 不再只是帮你写东西、查东西——它开始涉及你的钱包和你的电脑。这是一个质变。</strong></p><p>先说 Perplexity 的「个人电脑」。这个产品的意义不在于技术多先进，而在于它代表了一种新的 AI 架构思路：<strong>不做最强的模型，做最好的模型路由器。</strong>Perplexity 编排 19 个前沿模型并行工作，针对不同子任务选择最优模型——这本质上是在说，未来的 AI 体验不取决于哪家模型最强，而取决于谁能最聪明地调度多个模型。这和上周 GTC 上 NVIDIA 发布 NemoClaw Agent 平台的逻辑一脉相承：Agent 的价值在于编排能力，不在于单点智能。</p><p>但更让我关注的是 Visa 的「Agentic Ready」计划。当 AI Agent 可以替你支付账单、采购物品、管理订阅时，我们面对的不再是「AI 辅助决策」而是「AI 自主行动」——包括涉及真金白银的行动。Visa 和 Mastercard 同时在推这个方向，意味着这不是概念验证，而是产业共识。但问题来了：<strong>当 AI Agent 在预设规则内花你的钱时，谁为错误买单？</strong>如果 Agent 误判了一个「符合规则」的交易，银行赔？Visa 赔？用户自己承担？现行的金融监管体系完全没有覆盖这个场景。Commerzbank 和 DZ Bank 的试点之所以重要，不是因为技术，而是因为它们正在为「AI Agent 的金融责任」建立第一批法律先例。</p><p>再看 Morgan Stanley 的警告。「大多数人没准备好」这句话在投行报告里出现，通常意味着两件事：一是他们真的觉得变化很大，二是他们想让客户赶紧加仓 AI 股票。但抛开营销话术，报告里提到的「递归自我改进」值得认真对待。如果下一代模型真的能在某些维度实现自我迭代优化，那 AI 能力的提升将不再是线性的——而是指数级的。这和 Perplexity 的多模型编排放在一起看更有意思：当单个模型能自我改进，而编排层能同时调度多个自我改进的模型……这个复合效应可能比我们任何人能预测的都要快。</p><p>最后说微软和 OpenAI 的裂痕。500 亿美元的 Amazon 云交易可能违反微软的独家协议——这不是小事。如果微软真的起诉，这将是 AI 时代第一场因平台排他性引发的巨型商业诉讼。更深层的信号是：<strong>OpenAI 正在试图摆脱对微软的依赖，而微软正在试图锁定这种依赖。</strong>当一个 AI 公司的战略自由度和一个云厂商的锁定策略发生冲突，我们看到的不只是一场官司——而是 AI 产业权力结构的第一次正面碰撞。谁赢了这场官司，就决定了未来五年 AI 云服务市场的游戏规则。</p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Perplexity Launches 'Personal Computer': AI Agent Lives on Your Mac</strong> — Local AI agent system running on Mac mini with full file/app access, plus enterprise cloud version orchestrating 19 AI models in parallel. Perplexity bets on model orchestration over model creation.<br><small>Source: <a href=\"https://www.axios.com/2026/03/11/perplexity-personal-computer-mac\">Axios</a> | <a href=\"https://www.theregister.com/2026/03/12/perplexity_extends_cloud_computer_to_enterprise/\">The Register</a></small></li><li><strong>Visa 'Agentic Ready': AI Agents Can Now Spend Your Money</strong> — European pilot with Commerzbank and DZ Bank tests AI-initiated autonomous payments within predefined rules. Payments becomes the first major testbed for AI agent autonomy.<br><small>Source: <a href=\"https://www.artificialintelligence-news.com/news/visa-prepares-payment-systems-for-ai-agent-initiated-transactions/\">AI News</a></small></li><li><strong>Morgan Stanley Warns: Major AI Breakthrough Imminent, World Isn't Ready</strong> — Report predicts transformative AI leap in H1 2026 driven by unprecedented compute accumulation. Mentions recursive self-improvement potential and warns of 9-18 GW US power shortage by 2028.<br><small>Source: <a href=\"https://fortune.com/2026/03/13/elon-musk-morgan-stanley-ai-leap-2026/\">Fortune</a></small></li><li><strong>Microsoft Considers Suing Amazon and OpenAI Over $50B Cloud Deal</strong> — The deal may violate Microsoft's exclusive Azure hosting contract. First major commercial collision over AI platform exclusivity.<br><small>Source: <a href=\"https://www.ft.com/content/e814f4c3-4fb5-4e2e-90a6-470044436b39\">Financial Times</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI agents move from 'doing things' to 'spending money' — Visa's pilot marks new autonomy frontier</li><li>Model orchestration > model creation: Perplexity bets on routing, not raw intelligence</li><li>AI infrastructure commercial friction intensifies: Microsoft vs Amazon/OpenAI</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>This week's hidden thread: AI agents are no longer just assistants — they're touching your wallet and your computer. That's a qualitative shift.</strong></p><p>Perplexity's 19-model orchestration represents a new architecture bet: the best AI experience won't come from the strongest model, but the smartest model router. Visa's 'Agentic Ready' is more significant than it sounds — when AI spends real money autonomously, who's liable for mistakes? Current financial regulation has zero coverage here. And Microsoft vs OpenAI/Amazon isn't just a lawsuit — it's the first direct collision over AI platform power structure. <strong>Whoever wins defines the rules of AI cloud services for the next five years.</strong></p></div>"
    },
    "cover": og.get(tech_urls[0], ""),
    "sources": [
        {
            "title": {"zh": "Axios: Perplexity 发布基于 Mac 的 AI Agent", "en": "Axios: Perplexity Launches Mac-Based AI Agent"},
            "url": "https://www.axios.com/2026/03/11/perplexity-personal-computer-mac",
            "image": og.get(tech_urls[0], "")
        },
        {
            "title": {"zh": "The Register: Perplexity 将云端 Computer 扩展至企业", "en": "The Register: Perplexity Extends Cloud Computer to Enterprise"},
            "url": "https://www.theregister.com/2026/03/12/perplexity_extends_cloud_computer_to_enterprise/",
            "image": og.get(tech_urls[1], "")
        },
        {
            "title": {"zh": "AI News: Visa 为 AI Agent 自主支付做好准备", "en": "AI News: Visa Prepares for AI Agent-Initiated Transactions"},
            "url": "https://www.artificialintelligence-news.com/news/visa-prepares-payment-systems-for-ai-agent-initiated-transactions/",
            "image": og.get(tech_urls[2], "")
        },
        {
            "title": {"zh": "Fortune: Morgan Stanley 警告 AI 突破即将到来", "en": "Fortune: Morgan Stanley Warns AI Breakthrough Is Coming"},
            "url": "https://fortune.com/2026/03/13/elon-musk-morgan-stanley-ai-leap-2026/",
            "image": og.get(tech_urls[3], "")
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

print(f"\n✅ Done! Added 2 issues (design + tech) for 2026-03-22. Total issues: {len(issues)}")
