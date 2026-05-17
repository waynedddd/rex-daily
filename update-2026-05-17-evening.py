#!/usr/bin/env python3
"""Rex Daily Digest - 2026-05-17 Evening"""
import json, ssl, urllib.request, re, os

def get_og_image(url):
    try:
        ctx = ssl.create_default_context()
        try:
            import certifi
            ctx.load_verify_locations(certifi.where())
        except: pass
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            html = r.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
        return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images
og = {}
urls_to_fetch = [
    "https://venturebeat.com/ai/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead",
    "https://fortune.com/2026/04/16/canva-ai-agentic-design-suite-coo-cliff-obrecht/",
    "https://www.cnbc.com/2026/05/12/google-races-put-gemini-at-center-of-android-before-apples-ai-reboot.html",
    "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
    "https://guptadeepak.com/tools/top-5-ai-design-tools-2026/",
    "https://www.flatlineagency.com/blog/ai-design-tools-for-brands-2026/",
]
for u in urls_to_fetch:
    og[u] = get_og_image(u)
    print(f"og:image {u[:60]}... => {og[u][:80] if og[u] else '(none)'}")

design_issue = {
    "date": "2026-05-17",
    "section": "design",
    "title": {
        "zh": "Canva AI 2.0 发布 Agentic 设计套件、AI 设计工具三国杀白热化——当 Figma Make、Canva Magic、Adobe Firefly 同时 all-in AI，设计工具市场正在经历什么？",
        "en": "Canva AI 2.0 Launches Agentic Design Suite, AI Design Tool War Intensifies — What Happens When Figma Make, Canva Magic, and Adobe Firefly All Go All-In on AI Simultaneously?"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul><li><strong>Canva 发布「AI 2.0」Agentic 设计套件：从画图工具进化为自主设计 Agent</strong> — Canva 在 2026 年 4 月发布了 AI 2.0 套件，核心转变是从「AI 辅助设计」升级为「Agentic 设计」——AI 不再只是帮你生成图片，而是能理解品牌规范、自主执行多步骤设计任务（如根据品牌指南批量生成多平台广告素材）。COO Cliff Obrecht 称 Canva 已「悄悄成为全球使用量最大的 AI 服务之一」。这标志着设计工具从「工具」到「Agent」的关键转折。<br><small>来源：<a href="https://fortune.com/2026/04/16/canva-ai-agentic-design-suite-coo-cliff-obrecht/">Fortune</a></small></li><li><strong>2026 AI 设计工具三国杀：Figma Make vs Canva AI vs Adobe Firefly——三条路线、三种哲学</strong> — 多个独立评测（toools.design、Guideflow、Phygital+、Figma 官方资源库）在 2026 年同时发布了 AI 设计工具对比分析，呈现出清晰的三分格局：<strong>Figma Make</strong>（$16/月，深度集成 Figma 生态，面向专业 UI/UX 设计师）、<strong>Canva Magic Design</strong>（免费起步，面向非设计师和营销团队，AI 2.0 加持下能力暴增）、<strong>Adobe Firefly</strong>（创意图像生成，深度集成 Photoshop/Illustrator 工作流）。新兴挑战者包括 UX Pilot（研究到原型一站式）、Flowstep（多屏用户旅程）、Motiff（代码导出）、Galileo AI（文本到 UI）。趋势明确：<strong>AI 设计工具不再是「一个万能产品」的竞争，而是「工具链组装」的竞争。</strong><br><small>来源：<a href="https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026">toools.design</a> / <a href="https://guptadeepak.com/tools/top-5-ai-design-tools-2026/">Guideflow</a> / <a href="https://www.flatlineagency.com/blog/ai-design-tools-for-brands-2026/">Flatline Agency</a> / <a href="https://www.figma.com/resource-library/ai-design-tools/">Figma Resource Library</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>设计工具从「工具」进化为「Agent」</strong>：Canva AI 2.0 的 Agentic 能力意味着设计工具开始自主决策，而不只是等待指令</li><li><strong>三分天下格局清晰</strong>：Figma（专业 UI/UX）、Canva（大众化设计）、Adobe（创意内容生成）各据一方</li><li><strong>工具链组装时代到来</strong>：设计师不再选一个工具，而是用 3-5 个专精工具组装工作流</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Canva 的 AI 2.0 发布被很多设计圈的人低估了——因为它不是 Figma，所以「专业设计师」倾向于忽略它。但这恰恰是 Canva 最危险的地方。</strong></p><p>先说 Agentic 设计是什么意思。传统 AI 设计工具的逻辑是「你给指令，AI 生成结果」——本质上是一个更高级的滤镜或模板引擎。Canva AI 2.0 的 Agentic 模式不同：你告诉它「我要为这个产品发布做一套跨 Instagram、LinkedIn、邮件的营销素材」，AI 会理解你的品牌指南（颜色、字体、调性）、自动适配各平台尺寸、生成文案、选择图片风格、输出一整套可编辑的设计稿。这不是辅助——<strong>这是自主执行。</strong>如果你是一个中小企业的营销人员，这意味着你不再需要设计师来做日常素材生产。</p><p>这对「专业设计师」意味着什么？先别慌。看看三国杀的格局就会发现，AI 设计工具的竞争其实是<strong>三个不同市场的竞争</strong>：Canva 攻占的是「设计民主化」市场——让非设计师能做出「够用」的设计；Figma Make 服务的是「专业 UI/UX」市场——AI 辅助专业设计师更快迭代；Adobe Firefly 占据的是「创意内容」市场——为广告、视频、品牌创意提供 AI 生成素材。<strong>这三个市场的用户画像几乎不重叠。</strong>真正应该担心的不是「AI 取代设计师」，而是「Canva 的 Agentic 能力会不会向上游蚕食 Figma 的领地」。</p><p>toools.design 和 Guideflow 的工具对比评测透露了一个更微妙的趋势：2026 年的设计师不再在问「哪个 AI 设计工具最好」，而是在问「我的工具链应该怎么组装」。一个典型的 2026 设计师工具链可能长这样：UX Pilot 做用户研究和信息架构 → Figma Make 做快速 UI 迭代 → Motiff 导出 React 代码 → Canva 做营销素材。每个环节用最合适的工具，而不是指望一个工具搞定一切。这和开发者的工具链逻辑（VS Code + Git + Docker + CI/CD）越来越像。</p><p>把这个趋势和上期日报的 Figma「State of the Designer 2026」报告连起来看，一个清晰的图景出现了：<strong>AI 正在同时降低设计的「门槛」和提高设计的「天花板」。</strong>Canva AI 2.0 降低门槛——任何人都能用 Agent 生成专业级营销素材；Figma Make + DESIGN.md + Code Connect 提高天花板——专业设计师能用 AI 工具链实现以前做不到的效率和精度。被挤压的是中间地带：那些「会用 Figma 画图但没有判断力」的执行层设计师。上下两端都在扩张，中间在塌缩。如果你是设计师，2026 年的选择很清楚：要么往上走成为「定义体验、组装工具链」的策略型设计师，要么面对 Canva Agent 能以十分之一的成本完成你 80% 工作的现实。</p></div>',
        "en": '<h3>📌 AI × Design</h3><ul><li><strong>Canva Launches "AI 2.0" Agentic Design Suite: From Drawing Tool to Autonomous Design Agent</strong> — Canva released its AI 2.0 suite in April 2026, marking a core shift from "AI-assisted design" to "agentic design" — AI no longer just generates images but understands brand guidelines and autonomously executes multi-step design tasks (e.g., batch-generating multi-platform ad creatives following brand rules). COO Cliff Obrecht says Canva has "quietly become one of the world\'s most-used AI services." This marks the critical pivot from "tool" to "agent."<br><small>Source: <a href="https://fortune.com/2026/04/16/canva-ai-agentic-design-suite-coo-cliff-obrecht/">Fortune</a></small></li><li><strong>2026 AI Design Tool Three-Way Battle: Figma Make vs Canva AI vs Adobe Firefly — Three Philosophies, Three Markets</strong> — Multiple independent reviews (toools.design, Guideflow, Phygital+, Figma Resource Library) published AI design tool comparisons revealing a clear three-way split: <strong>Figma Make</strong> ($16/mo, deep Figma ecosystem integration, pro UI/UX designers), <strong>Canva Magic Design</strong> (free tier, non-designers and marketing teams, massively boosted by AI 2.0), <strong>Adobe Firefly</strong> (creative image generation, deep Photoshop/Illustrator workflow integration). Emerging challengers include UX Pilot, Flowstep, Motiff, and Galileo AI. The trend is clear: <strong>AI design tool competition has shifted from "one product fits all" to "toolchain assembly."</strong><br><small>Source: <a href="https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026">toools.design</a> / <a href="https://guptadeepak.com/tools/top-5-ai-design-tools-2026/">Guideflow</a> / <a href="https://www.flatlineagency.com/blog/ai-design-tools-for-brands-2026/">Flatline Agency</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>Design tools evolve from "tools" to "agents"</strong>: Canva AI 2.0\'s agentic capabilities mean design tools now make autonomous decisions</li><li><strong>Three-way market split crystallizes</strong>: Figma (pro UI/UX), Canva (democratized design), Adobe (creative content generation)</li><li><strong>The toolchain assembly era arrives</strong>: Designers no longer pick one tool but assemble 3-5 specialized tools into workflows</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Canva\'s AI 2.0 release was underestimated by the design community — because it\'s not Figma, "professional designers" tend to dismiss it. But that\'s precisely what makes Canva dangerous.</strong></p><p>Agentic design means you tell the AI "create a cross-platform marketing suite for this product launch" and it understands your brand guidelines, auto-adapts to platform dimensions, generates copy, selects image styles, and outputs a complete editable design package. This isn\'t assistance — <strong>it\'s autonomous execution.</strong> For SMB marketers, this eliminates the need for designers for routine asset production.</p><p>The three-way battle reveals three different markets: Canva captures "design democratization," Figma Make serves "professional UI/UX," Adobe Firefly owns "creative content." <strong>These user profiles barely overlap.</strong> The real question isn\'t "AI replaces designers" but "will Canva\'s agentic capabilities encroach upstream into Figma\'s territory?"</p><p>The toolchain assembly trend is telling: a typical 2026 designer workflow might be UX Pilot for research → Figma Make for rapid UI iteration → Motiff for React code export → Canva for marketing assets. This mirrors developer toolchain logic (VS Code + Git + Docker + CI/CD).</p><p>Connecting to yesterday\'s Figma "State of the Designer" report: <strong>AI simultaneously lowers design\'s floor and raises its ceiling.</strong> Canva AI 2.0 lowers the floor; Figma Make + DESIGN.md + Code Connect raises the ceiling. What\'s being squeezed is the middle — execution-only designers without judgment. If you\'re a designer in 2026, the choice is clear: move up to become a strategy-and-toolchain designer, or face Canva Agents doing 80% of your work at one-tenth the cost.</p></div>'
    },
    "cover": og.get("https://fortune.com/2026/04/16/canva-ai-agentic-design-suite-coo-cliff-obrecht/", "") or "https://content.fortune.com/wp-content/uploads/2026/04/canva-ai-2.jpg",
    "sources": [
        {
            "url": "https://fortune.com/2026/04/16/canva-ai-agentic-design-suite-coo-cliff-obrecht/",
            "title": {"zh": "Fortune: Canva AI 2.0 Agentic 设计套件发布", "en": "Fortune: Canva Debuts Agentic AI Design Suite"},
            "image": og.get("https://fortune.com/2026/04/16/canva-ai-agentic-design-suite-coo-cliff-obrecht/", "")
        },
        {
            "url": "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
            "title": {"zh": "toools.design: 2026 年 UI/UX 设计师 AI 工具深度评测", "en": "toools.design: 9 Best AI Tools for UI/UX Designers in 2026"},
            "image": og.get("https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026", "")
        },
        {
            "url": "https://www.flatlineagency.com/blog/ai-design-tools-for-brands-2026/",
            "title": {"zh": "Flatline Agency: 2026 年品牌 AI 设计工具", "en": "Flatline Agency: AI Design Tools for Brands 2026"},
            "image": og.get("https://www.flatlineagency.com/blog/ai-design-tools-for-brands-2026/", "")
        },
        {
            "url": "https://guptadeepak.com/tools/top-5-ai-design-tools-2026/",
            "title": {"zh": "Guideflow: 2026 Top 5 AI 设计工具对比", "en": "Guideflow: Top 5 AI Design Tools 2026 Compared"},
            "image": og.get("https://guptadeepak.com/tools/top-5-ai-design-tools-2026/", "")
        }
    ]
}

tech_issue = {
    "date": "2026-05-17",
    "section": "tech",
    "title": {
        "zh": "Anthropic 首次超越 OpenAI 成为美国企业 AI 采用率第一、Google I/O 2026 明日开幕——当 Claude 在企业市场逆袭，AI 行业的权力重心正在转移",
        "en": "Anthropic Surpasses OpenAI in US Business AI Adoption for the First Time, Google I/O 2026 Opens Tomorrow — As Claude Stages an Enterprise Comeback, AI's Center of Power Is Shifting"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul><li><strong>Anthropic 首次超越 OpenAI，成为美国企业 AI 采用率第一名：Ramp 数据显示 Anthropic 达到 34.4% 市场份额</strong> — 根据 Ramp 2026 年 5 月 AI 指数报告，Anthropic 在 2026 年 4 月首次超过 OpenAI，成为美国企业中采用率最高的 AI 服务商。Anthropic 的企业采用率达到 34.4%，而 OpenAI 增长放缓。VentureBeat 深度分析指出，Anthropic 的逆袭得益于三个因素：Claude 在复杂推理和代码任务上的优势、Claude for Enterprise 的安全合规特性对大企业的吸引力、以及 OpenAI 频繁的产品线调整导致企业客户信任度下降。但 VentureBeat 同时警告了三大威胁：Google Gemini 的企业级追赶、OpenAI 的反击策略、以及开源模型（Llama、Mistral）的蚕食。<br><small>来源：<a href="https://venturebeat.com/ai/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead">VentureBeat</a> / <a href="https://www.linkedin.com/pulse/ai-news-highlights-from-15th-may-2026-ai-insiders-news-exn6e">LinkedIn AI Insiders</a></small></li><li><strong>Google I/O 2026 明日（5月19日）开幕：Gemini 模型升级 + Android XR 眼镜 + Aluminium OS 是三大焦点</strong> — Google I/O 2026 将于北京时间 5 月 20 日凌晨 4:30 开始主题演讲。CNBC 报道称 Google 正在「抢在 Apple AI 重启之前，把 Gemini 打造为 Android 的核心 AI 层」。Android 总裁 Sameer Samat 接受采访时强调了 Gemini Intelligence 的 agentic 能力——AI 不再是一个 App，而是操作系统级基础设施。CNET 梳理了过去一年 Google 的 AI 发布节奏，预测 I/O 将带来重大 Gemini 模型升级和更多 AI Agent 能力。<br><small>来源：<a href="https://www.cnbc.com/2026/05/12/google-races-put-gemini-at-center-of-android-before-apples-ai-reboot.html">CNBC</a> / <a href="https://www.cnet.com/tech/services-and-software/google-i-o-2026-ai-releases-over-the-past-year/">CNET</a> / <a href="https://io.google/">Google I/O 官网</a></small></li><li><strong>AI 创业融资持续火热：5 月 7 家 AI Agent 创业公司融资总额超 $26.6 亿</strong> — Fundup AI 和 Mean CEO 的融资追踪数据显示，2026 年 5 月 AI Agent 领域持续吸引大量投资。Microsoft 宣布在亚洲投入 $175 亿用于 AI 和云基础设施建设（2026-2029），这是其有史以来最大的亚洲投资。AI Agent 作为投资主题已从概念验证阶段进入规模化部署阶段。<br><small>来源：<a href="https://fundup.ai/recently-funded-startups">Fundup AI</a> / <a href="https://blog.mean.ceo/ai-startup-funding-news-may-2026/">Mean CEO Blog</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 企业市场格局翻转</strong>：Anthropic 首超 OpenAI，Claude 在企业级场景的竞争力被数据验证</li><li><strong>Google 的 AI 平台战打响</strong>：I/O 2026 是 Google 将 Gemini 从「产品」变成「平台基础设施」的关键节点</li><li><strong>AI Agent 投资从概念进入规模化</strong>：融资数据显示市场信心从 LLM 模型转向 Agent 应用层</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Anthropic 超越 OpenAI 这件事，比它的数据本身更有意思的是它发生的时间——恰好在 Google I/O 2026 开幕的前两天。AI 行业的权力重心正在发生自 ChatGPT 发布以来最大的一次结构性转移。</strong></p><p>先说 Ramp 的数据。34.4% 的企业采用率意味着什么？意味着在美国使用 AI 服务的企业中，超过三分之一选择了 Anthropic 作为主要供应商。这个数字在一年前是不可想象的——2025 年初，OpenAI 在企业市场的领先优势看起来几乎不可撼动。那发生了什么？<strong>我认为核心转折点有三个：第一，Claude 的代码和推理能力在 Opus 4 系列中实现了质的飞跃，尤其在复杂企业场景（法律文档分析、金融建模、代码审计）中的表现远超 GPT-4.5/5 系列；第二，Anthropic 的安全叙事终于从「限制」变成了「卖点」——大企业最怕的不是 AI 不够强，而是 AI 出事后谁负责，Claude for Enterprise 的 Constitutional AI 框架给了企业一个「可解释、可审计」的安全承诺；第三，OpenAI 过去一年的产品线过于复杂——GPT-4o、GPT-4.5、o1、o3、o4-mini、GPT-5、Sora、DALL·E 4、ChatGPT Pro、Enterprise、Team……企业客户面对这么多选择时反而无所适从。</strong></p><p>但 VentureBeat 提到的三大威胁很现实。明天的 Google I/O 就是威胁之一：如果 Google 发布新的 Gemini 模型并大幅降低企业 API 价格（Google 有云基础设施成本优势），Anthropic 的企业客户可能会被价格战削弱。另一个威胁是开源模型——Llama 4 和 Mistral Large 2 的能力已经接近商业模型，对那些有自建能力的大企业来说，为什么要付费给 Anthropic？第三个威胁最微妙：OpenAI 的反击。Sam Altman 不会坐视市场份额流失，预计下半年会有针对性的企业产品调整。</p><p>把 Anthropic 的逆袭和明天的 Google I/O 放在一起看，你会发现 AI 行业正在从「模型竞赛」进入「生态竞赛」。<strong>Anthropic 赢了企业采用率，但它没有操作系统、没有硬件、没有搜索引擎、没有云平台。Google 有所有这些，明天 I/O 上 Gemini Intelligence 变成 Android 系统层意味着 Google 在分发渠道上拥有绝对优势。OpenAI 有 ChatGPT 的消费者品牌认知和 Apple/Microsoft 的合作关系（虽然 Apple 那边已经出了问题）。</strong>三家公司各有一块别人没有的拼图：Anthropic 有企业信任、Google 有平台生态、OpenAI 有消费者品牌。2026 年下半年的竞争将围绕「谁能先补齐短板」展开。</p><p>AI Agent 融资数据提供了另一个视角。$26.6 亿流入 AI Agent 创业公司，加上 Microsoft $175 亿的亚洲 AI 基础设施投资——<strong>资本市场已经不再问「AI 是否有用」，而是在押注「AI Agent 将成为企业软件的新形态」。</strong>这和上期日报 SAP 发布「自治企业」平台的时机完美吻合：当 SAP 这种传统企业软件巨头都在 all-in AI Agent 时，你知道这不是炒作——这是行业共识。问题不再是「是否」，而是「多快」。明天 Google I/O 的主题演讲将是这个共识的又一次确认。</p></div>',
        "en": '<h3>📌 AI × Tech</h3><ul><li><strong>Anthropic Surpasses OpenAI for First Time in US Business AI Adoption: Ramp Data Shows 34.4% Market Share</strong> — According to Ramp\'s May 2026 AI Index, Anthropic overtook OpenAI in April 2026 as the most-adopted AI service among US businesses, reaching 34.4% adoption. VentureBeat\'s deep analysis attributes this to three factors: Claude\'s superiority in complex reasoning and code tasks, Claude for Enterprise\'s security compliance appeal to large companies, and OpenAI\'s frequent product line changes eroding enterprise trust. However, VentureBeat warns of three threats: Google Gemini\'s enterprise push, OpenAI\'s counterattack, and open-source model erosion.<br><small>Source: <a href="https://venturebeat.com/ai/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead">VentureBeat</a> / <a href="https://www.linkedin.com/pulse/ai-news-highlights-from-15th-may-2026-ai-insiders-news-exn6e">LinkedIn AI Insiders</a></small></li><li><strong>Google I/O 2026 Opens Tomorrow (May 19): Gemini Model Upgrades + Android XR Glasses + Aluminium OS Are Three Key Focuses</strong> — Google I/O 2026 keynote starts May 19 at 1:30 PM PT. CNBC reports Google is "racing to establish Gemini as Android\'s core AI layer before Apple\'s AI reboot." Android President Sameer Samat emphasized Gemini Intelligence\'s agentic capabilities — AI is no longer an app but OS-level infrastructure.<br><small>Source: <a href="https://www.cnbc.com/2026/05/12/google-races-put-gemini-at-center-of-android-before-apples-ai-reboot.html">CNBC</a> / <a href="https://www.cnet.com/tech/services-and-software/google-i-o-2026-ai-releases-over-the-past-year/">CNET</a> / <a href="https://io.google/">Google I/O</a></small></li><li><strong>AI Startup Funding Stays Hot: 7 AI Agent Startups Raised $2.66B+ in May</strong> — Fundup AI and Mean CEO tracking data shows continued massive investment in AI Agent startups. Microsoft announced its largest-ever Asia investment of $17.5B for AI and cloud infrastructure (2026-2029). AI Agent investment has shifted from proof-of-concept to at-scale deployment.<br><small>Source: <a href="https://fundup.ai/recently-funded-startups">Fundup AI</a> / <a href="https://blog.mean.ceo/ai-startup-funding-news-may-2026/">Mean CEO Blog</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>Enterprise AI market flips</strong>: Anthropic overtakes OpenAI, Claude\'s enterprise competitiveness validated by data</li><li><strong>Google\'s AI platform war begins</strong>: I/O 2026 is the critical node where Gemini transforms from "product" to "platform infrastructure"</li><li><strong>AI Agent investment goes from concept to scale</strong>: Funding data shows market confidence shifting from LLM models to Agent applications</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>The timing of Anthropic overtaking OpenAI — two days before Google I/O 2026 — is more telling than the data itself. AI\'s center of power is undergoing its biggest structural shift since ChatGPT\'s launch.</strong></p><p>Ramp\'s 34.4% enterprise adoption figure was unimaginable a year ago. Three turning points drove this: 1) Claude\'s reasoning and code capabilities leapt ahead in the Opus 4 series for complex enterprise scenarios; 2) Anthropic\'s safety narrative transformed from "limitation" to "selling point" — enterprises fear post-incident liability most, and Constitutional AI provides an "explainable, auditable" safety promise; 3) OpenAI\'s product proliferation confused enterprise buyers.</p><p>But VentureBeat\'s three threats are real. Tomorrow\'s Google I/O is one: if Google releases upgraded Gemini models with aggressive enterprise API pricing, Anthropic\'s base could erode. Open-source models (Llama 4, Mistral Large 2) are another. OpenAI\'s counterattack is the third.</p><p><strong>Each company holds a puzzle piece the others lack: Anthropic has enterprise trust, Google has platform ecosystem, OpenAI has consumer brand.</strong> H2 2026 competition will center on "who fills their gaps first." The $2.66B flowing into AI Agent startups, plus Microsoft\'s $17.5B Asia investment, confirms the market consensus: <strong>AI Agent is the new enterprise software form factor.</strong> Tomorrow\'s Google I/O keynote will be another confirmation of this consensus.</p></div>'
    },
    "cover": og.get("https://venturebeat.com/ai/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead", "") or "https://venturebeat.com/wp-content/uploads/2026/05/anthropic-openai.jpg",
    "sources": [
        {
            "url": "https://venturebeat.com/ai/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead",
            "title": {"zh": "VentureBeat: Anthropic 在企业 AI 采用率上首超 OpenAI", "en": "VentureBeat: Anthropic Finally Beat OpenAI in Business AI Adoption"},
            "image": og.get("https://venturebeat.com/ai/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead", "")
        },
        {
            "url": "https://www.cnbc.com/2026/05/12/google-races-put-gemini-at-center-of-android-before-apples-ai-reboot.html",
            "title": {"zh": "CNBC: Google 抢在 Apple 之前把 Gemini 打造为 Android 核心", "en": "CNBC: Google Races to Put Gemini at Center of Android Before Apple's AI Reboot"},
            "image": og.get("https://www.cnbc.com/2026/05/12/google-races-put-gemini-at-center-of-android-before-apples-ai-reboot.html", "")
        },
        {
            "url": "https://www.cnet.com/tech/services-and-software/google-i-o-2026-ai-releases-over-the-past-year/",
            "title": {"zh": "CNET: Google I/O 2026 AI 发布汇总", "en": "CNET: Google I/O 2026 AI Releases Over the Past Year"},
            "image": ""
        },
        {
            "url": "https://fundup.ai/recently-funded-startups",
            "title": {"zh": "Fundup AI: 2026 年 5 月最新融资创业公司", "en": "Fundup AI: Recently Funded Startups May 2026"},
            "image": ""
        }
    ]
}

# Load existing issues
issues_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "issues.json")
with open(issues_path, "r", encoding="utf-8") as f:
    issues = json.load(f)

# Insert new issues at front (design first, then tech)
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open(issues_path, "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Added 2 issues (design + tech) for 2026-05-17 evening. Total issues: {len(issues)}")
