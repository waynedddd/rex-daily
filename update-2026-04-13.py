# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-04-13"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=8)
        content = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', content, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', content, re.I)
        return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images
urls = {
    "figma_report": "https://www.figma.com/blog/state-of-the-designer-2026/",
    "figma_report_dl": "https://www.figma.com/reports/state-of-the-designer-2026/",
    "anthropic_report": "https://resources.anthropic.com/2026-agentic-coding-trends-report",
    "meta_axios": "https://www.axios.com/2026/04/08/meta-muse-alexandr-wang",
    "meta_fortune": "https://fortune.com/2026/04/08/meta-unveils-muse-spark-mark-zuckerberg-ai-push/",
    "meta_cnbc": "https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html",
    "meta_reuters": "https://www.reuters.com/sustainability/sustainable-finance-reporting/meta-unveils-first-ai-model-superintelligence-team-2026-04-08/",
}

images = {}
for k, u in urls.items():
    images[k] = get_og_image(u)
    print(f"  {k}: {images[k][:80] if images[k] else '(none)'}")

# Load existing issues
with open("issues.json", "r") as f:
    issues = json.load(f)

design_issue = {
    "date": "2026-04-13",
    "section": "design",
    "title": {
        "zh": "Figma 发布《设计师现状 2026》报告：89% 因 AI 工作更快，拥抱 AI 的设计师满意度高 25% · Anthropic 发布 Agentic Coding 趋势报告：从写代码到管理 AI 工程团队",
        "en": "Figma 'State of the Designer 2026': 89% Work Faster with AI, AI Adopters 25% Happier · Anthropic Agentic Coding Trends Report: From Writing Code to Managing AI Engineering Teams"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Figma 发布《State of the Designer 2026》年度报告——AI 正在重塑设计师的自我认知</strong> — Figma 基于全球 906 名设计师的调查发布了年度报告。核心数据：<strong>89% 的设计师表示 AI 工具让他们工作更快，80% 表示协作更顺畅</strong>。更值得关注的是：<strong>积极拥抱 AI 工具的设计师，工作满意度比不用 AI 的同行高出 25%</strong>。报告强调「craft（手艺）」是幸福感和商业成果的关键——AI 不是在削弱手艺，而是在<strong>释放设计师去关注更高层面的决策</strong>。报告还探讨了设计师在 AI 时代应磨练的技能，以及「什么定义了卓越设计」这一根本问题。<br><small>来源：<a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a>、<a href=\"https://www.createwith.com/tool/figma/updates/figma-unveils-state-of-the-designer-2026-report-insights\">CreateWith</a></small></li><li><strong>Anthropic 发布《2026 Agentic Coding Trends Report》——软件开发从「写代码」变成「管理写代码的 AI」</strong> — Anthropic 发布了一份重磅趋势报告，基于 Rakuten、CRED、TELUS、Zapier 等企业的实际案例，总结了 8 大趋势：<strong>工程师角色转变、多 Agent 协调、人机协作模式演进、以及 Agentic Coding 从工程团队向全组织扩展</strong>。数据显示，Claude Code 的 79% 使用场景偏向自动化（而非辅助），意味着 AI 正在从「pair programming」走向「独立完成任务」。报告预测：<strong>AI Agent 质量控制将成为标配——用 AI 审查 AI 生成的代码</strong>，解决人类产能无法覆盖大规模 AI 产出的问题。<br><small>来源：<a href=\"https://resources.anthropic.com/2026-agentic-coding-trends-report\">Anthropic</a></small></li><li><strong>AI 设计工具 2026 全景图：Flowstep、Figma Make、Cursor 三足鼎立</strong> — Startup Stash 的横评测试了 8 款主流 AI 设计工具，发现它们并非在解决同一个问题。<strong>Flowstep（$15/月）专注 PM 和创始人的快速原型、Figma Make（$20/月）强调品牌一致性的 prompt-to-UI、Cursor（$20/月）则是工程师用代码做 UI 的首选</strong>。Claude 则作为设计研究和文档工具被独立归类——不做图，但帮你想清楚为什么这样做图。这种分化意味着<strong>「AI 设计工具」不再是一个统一品类，而是在按角色和工作流细分</strong>。<br><small>来源：<a href=\"https://blog.startupstash.com/8-best-ai-tools-for-designers-in-2026-tested-and-compared-8b9f0c30fd0d\">Startup Stash</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 不是在取代设计师，而是在重新定义「好设计师」的标准</strong>：Figma 报告显示，拥抱 AI 的设计师更快、更满意、更有创造力</li><li><strong>Agentic Coding 正在改变设计-开发的交接方式</strong>：当 AI Agent 可以独立完成开发，设计师的交付物从「设计稿」变成「意图描述」</li><li><strong>AI 设计工具市场开始分化</strong>：不再是「谁最好」，而是「谁最适合你的角色和工作流」</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天的两份报告放在一起读，画面就清晰了：设计和开发的边界正在以前所未有的速度消融——但消融的方式和大多数人想象的不一样。</strong></p><p>先说 Figma 的《State of the Designer 2026》。89% 更快、80% 协作更好——这些数字漂亮，但真正的 killer insight 是那个 25% 的满意度差距。<strong>拥抱 AI 的设计师不只是效率更高，他们更快乐。</strong>为什么？因为 AI 接管了设计工作中最无聊的部分——重复性的变体生成、规范检查、资产导出——而把「思考为什么要这样设计」的空间还给了设计师。这和制造业自动化的逻辑一模一样：<strong>机器接管了流水线，但工程师的价值反而上升了，因为他们的工作从「操作机器」变成了「设计流水线本身」</strong>。Figma 强调 craft 是幸福感的关键，这不是鸡汤——这是在说：在 AI 时代，<strong>你的手艺不再体现在像素推移的精确度上，而是体现在判断力、品味和系统性思考上</strong>。</p><p>再看 Anthropic 的 Agentic Coding 报告。79% 的 Claude Code 使用偏向自动化而非辅助——这个数字让我停下来想了想。<strong>这意味着大多数使用 Claude Code 的开发者不是在「和 AI 结对编程」，而是在「给 AI 布置任务然后去做别的事」。</strong>从「pair programming」到「task delegation」，这是质变。Rakuten、Zapier 这些案例说明：大型工程团队正在把 AI Agent 当作「初级工程师」来管理——分配任务、审查产出、提供反馈。报告预测的「AI 审查 AI 代码」更有意思——<strong>当 AI 产出的代码量超过人类审查能力时，唯一的解法就是用另一个 AI 来审查</strong>。这是一个自我强化的飞轮：AI 写代码 → AI 审代码 → 人类只负责决策和方向。</p><p>把这两份报告放在一起看，一个清晰的未来浮现了：<strong>设计师的交付物正在从「设计稿」变成「意图描述」，开发者的工作正在从「写代码」变成「管理 AI 工程师」</strong>。两者都在向上移动——从执行层到决策层。这验证了我一直以来的判断：<strong>AI 时代最稀缺的不是执行能力（AI 够用了），而是判断力——知道该做什么、为什么做、做到什么程度。</strong></p><p>Startup Stash 的工具横评也佐证了这一点。Flowstep 给 PM、Figma Make 给设计师、Cursor 给工程师、Claude 给「想清楚为什么」——<strong>AI 设计工具不再是一个品类，而是按思维模式分化</strong>。这意味着未来最强的不是精通某一个工具的人，而是能在多个 AI 工具之间流畅切换、把不同工具的产出串成完整故事的人。</p><p><strong>我的预判：Figma 的下一步一定是把 Agentic Coding 能力直接集成到设计工具里——设计师在 Figma 里完成设计，AI Agent 自动生成生产级代码，设计师审查并调整。这将在 2026 Config 大会上以某种形式出现。Anthropic 的 Agentic Coding 报告实际上是 Claude Code 的销售文档——但它提出的「AI 审查 AI」框架会成为行业标准。最大胆预测：到 2026 年底，「AI Agent 管理」将成为设计师和工程师共同的核心技能——不是写 prompt，而是定义验收标准、审查 AI 产出、以及在 AI 犯错时知道如何纠正。</strong></p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Figma Releases 'State of the Designer 2026' — AI Is Reshaping How Designers See Themselves</strong> — Based on a global survey of 906 designers, Figma's annual report reveals: <strong>89% say AI tools make them work faster, 80% say collaboration is smoother</strong>. The standout finding: <strong>designers who actively embrace AI are 25% more likely to be satisfied at work</strong>. The report emphasizes \"craft\" as the key to both happiness and business outcomes — AI isn't weakening craft, it's <strong>freeing designers to focus on higher-level decisions</strong>.<br><small>Source: <a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a>, <a href=\"https://www.createwith.com/tool/figma/updates/figma-unveils-state-of-the-designer-2026-report-insights\">CreateWith</a></small></li><li><strong>Anthropic Publishes '2026 Agentic Coding Trends Report' — Software Dev Shifts from Writing Code to Managing AI Engineers</strong> — Based on case studies from Rakuten, CRED, TELUS, and Zapier, the report identifies 8 major trends: <strong>evolving engineering roles, multi-agent coordination, human-AI collaboration patterns, and agentic coding expanding beyond engineering</strong>. 79% of Claude Code usage leans toward automation over assistance. Prediction: <strong>AI quality control of AI-generated code becomes standard</strong>.<br><small>Source: <a href=\"https://resources.anthropic.com/2026-agentic-coding-trends-report\">Anthropic</a></small></li><li><strong>AI Design Tools 2026 Landscape: Flowstep, Figma Make, Cursor Lead Different Segments</strong> — Startup Stash tested 8 AI design tools and found they solve different problems: <strong>Flowstep for PM rapid prototyping, Figma Make for brand-consistent prompt-to-UI, Cursor for engineer-driven UI coding</strong>. Claude stands alone as design research/documentation. The market is segmenting by role and workflow, not converging.<br><small>Source: <a href=\"https://blog.startupstash.com/8-best-ai-tools-for-designers-in-2026-tested-and-compared-8b9f0c30fd0d\">Startup Stash</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI redefines what makes a \"good designer\" — embrace AI = faster + happier + more creative</li><li>Agentic coding transforms design-dev handoff: deliverables shift from mockups to intent descriptions</li><li>AI design tools segment by role rather than competing head-to-head</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Read today's two reports together and the picture is clear: the design-development boundary is dissolving faster than anyone expected — but not in the way most people imagined.</strong></p><p>Figma's 25% satisfaction gap is the killer insight. Designers who embrace AI aren't just more efficient — they're happier. AI absorbs the boring parts (variant generation, spec checking, asset export) and returns the \"why are we designing this?\" space to designers. Like manufacturing automation: <strong>machines took the assembly line, but engineers became MORE valuable because their job shifted from operating machines to designing the assembly line itself.</strong></p><p>Anthropic's 79% automation stat stopped me cold. Most Claude Code users aren't pair-programming with AI — they're delegating tasks and walking away. From pair programming to task delegation is a qualitative shift. The predicted \"AI reviewing AI code\" creates a self-reinforcing flywheel: AI writes → AI reviews → humans handle decisions and direction only.</p><p>Together: <strong>designers' deliverables are shifting from mockups to intent descriptions; developers' work from writing code to managing AI engineers. Both roles are moving upward — from execution to judgment.</strong> The scarcest skill in the AI era isn't execution (AI handles that) — it's judgment: knowing what to build, why, and when to stop.</p><p><strong>Predictions: Figma will integrate agentic coding directly into its design tool — design in Figma, AI generates production code, designer reviews. This appears at Config 2026. Anthropic's \"AI reviewing AI\" framework becomes industry standard. Boldest: by year-end, \"AI Agent management\" becomes a core skill for both designers and engineers — not prompt writing, but defining acceptance criteria, reviewing AI output, and knowing how to correct AI mistakes.</strong></p></div>"
    },
    "cover": images.get("figma_report", "") or images.get("figma_report_dl", ""),
    "sources": [
        {
            "title": {"zh": "Figma 年度设计师现状报告 2026", "en": "Figma State of the Designer 2026 Report"},
            "url": "https://www.figma.com/blog/state-of-the-designer-2026/",
            "image": images.get("figma_report", "")
        },
        {
            "title": {"zh": "Anthropic 2026 Agentic Coding 趋势报告", "en": "Anthropic 2026 Agentic Coding Trends Report"},
            "url": "https://resources.anthropic.com/2026-agentic-coding-trends-report",
            "image": images.get("anthropic_report", "")
        },
        {
            "title": {"zh": "2026 年 8 款最佳 AI 设计工具横评", "en": "8 Best AI Tools for Designers in 2026, Tested and Compared"},
            "url": "https://blog.startupstash.com/8-best-ai-tools-for-designers-in-2026-tested-and-compared-8b9f0c30fd0d",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-04-13",
    "section": "tech",
    "title": {
        "zh": "Meta 发布 Muse Spark：Alexandr Wang 的 140 亿美元赌注交出第一份答卷 · 计划开源 · Anthropic Mythos 限制发布引发安全讨论 · OpenAI 新模型 Spud 即将登场",
        "en": "Meta Launches Muse Spark: Alexandr Wang's $14B Bet Delivers First Result · Open-Source Plans · Anthropic Mythos Limited Release Sparks Safety Debate · OpenAI's 'Spud' Model Imminent"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Meta 发布 Muse Spark——Alexandr Wang 加入后的第一个重磅模型，计划开源</strong> — Meta 在 4 月 8 日正式发布了 Muse Spark，这是去年花 143 亿美元从 Scale AI 挖来 Alexandr Wang 后，Meta Superintelligence Labs 交出的第一份答卷。<strong>Muse Spark 在图像和视频处理相关 benchmark 上表现突出</strong>，将用于驱动 Meta AI app 的 Vibes AI 视频功能。更关键的是：<strong>Meta 计划以开源许可证发布 Muse Spark</strong>，延续其开源 AI 策略。背景是去年 Llama 4 发布后反响平淡，Zuckerberg 大幅调整了 AI 战略——Muse Spark 是这次战略调整后的第一枪。CNBC 的分析指出，核心问题是：<strong>Muse Spark 能为 Meta 赚钱吗？</strong><br><small>来源：<a href=\"https://www.axios.com/2026/04/08/meta-muse-alexandr-wang\">Axios</a>、<a href=\"https://fortune.com/2026/04/08/meta-unveils-muse-spark-mark-zuckerberg-ai-push/\">Fortune</a>、<a href=\"https://www.cnbc.com/2026/04/09/metas-long-awaited-ai-model-is-finally-here-but-can-it-make-money.html\">CNBC</a>、<a href=\"https://www.reuters.com/sustainability/sustainable-finance-reporting/meta-unveils-first-ai-model-superintelligence-team-2026-04-08/\">Reuters</a></small></li><li><strong>Anthropic Mythos 限制发布——仅向少数科技公司开放，聚焦网络安全防御</strong> — Axios 报道，Anthropic 本周详细介绍了 Mythos 模型，称其<strong>能力强大到需要限制初始发布范围——仅向少数科技公司提供，专注于网络安全防御应用</strong>。这呼应了上期报道的财长 Bessent 召集华尔街 CEO 讨论 AI 风险的事件。Anthropic 正在走一条「能力极强但发布极谨慎」的路线——用安全叙事来建立信任，同时暗示 Mythos 的能力远超竞争对手。<br><small>来源：<a href=\"https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks\">Axios</a></small></li><li><strong>OpenAI 新模型 Spud 即将登场——被认为是「重大飞跃」</strong> — Axios 透露，OpenAI 正在对代号为 Spud 的新模型做最后调试，业内人士认为该模型代表了<strong>一次重大的能力跃升</strong>。这是继 Sora 独立版关停后，OpenAI 在模型层面的最新动作。三大 AI 公司（Meta Muse Spark、Anthropic Mythos、OpenAI Spud）几乎在同一周展示新模型——<strong>2026 Q2 的模型战已经打响</strong>。<br><small>来源：<a href=\"https://www.axios.com/2026/04/08/meta-muse-alexandr-wang\">Axios</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>2026 Q2 模型大战：三巨头几乎同时亮牌</strong>——Meta Muse Spark（已发布）、Anthropic Mythos（限制发布）、OpenAI Spud（即将发布）</li><li><strong>开源 vs 安全的路线分化</strong>：Meta 坚持开源、Anthropic 极度谨慎、OpenAI 介于两者之间</li><li><strong>AI 模型的商业化压力加大</strong>：CNBC 直接问「Muse Spark 能赚钱吗？」——投资者对纯技术突破的耐心在减少</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>本周科技板块最值得关注的不是某一个模型的发布，而是三巨头几乎同时亮牌这件事本身——以及它们选择的路线分化所透露的战略意图。</strong></p><p>Meta 的 Muse Spark 是 Alexandr Wang 的第一次公开考试。143 亿美元、数亿美元的工程师薪资包——这是硅谷史上最贵的 AI 人才交易之一。Muse Spark 在图像和视频处理上表现突出，这不是偶然——<strong>Meta 的核心业务是社交媒体，视觉内容是其命脉</strong>。Zuckerberg 的策略很清楚：不跟 OpenAI 和 Anthropic 在通用智能上硬拼，而是在视觉 AI 上建立差异化优势，然后用开源策略扩大影响力。但 CNBC 那个「能赚钱吗」的问题一针见血——<strong>Meta 的 AI 投入已经超过 500 亿美元，投资者需要看到回报路径，不只是 benchmark 上的数字</strong>。Muse Spark 驱动 Vibes AI 视频功能可能是答案的一部分——如果 Meta 能让每个 Instagram/Facebook 用户用 AI 生成高质量视频内容，广告收入的天花板将大幅提高。</p><p>Anthropic 的 Mythos 策略更耐人寻味。「太强大了所以限制发布」——这个叙事既是真实的安全考量，也是绝妙的营销。<strong>通过限制发布，Anthropic 同时达成了三个目标：建立安全品牌形象、制造稀缺性（只有少数公司能用）、以及暗示能力远超竞争对手</strong>。上期报道的 Bessent 召集华尔街 CEO 开会现在有了更完整的背景——Mythos 的网络安全能力可能意味着：一个 AI 模型能在数小时内发现金融系统中人类需要数月才能找到的漏洞。这种能力如果被善用是防御盾牌，被恶用就是核武器。Anthropic 选择从网络安全防御切入，是聪明的——<strong>先让模型成为「防御英雄」，再逐步扩展到其他场景</strong>。</p><p>OpenAI 的 Spud 是最大的悬念。Axios 用了「significant leap forward（重大飞跃）」的措辞——在 AI 媒体报道中，这个词不常用，通常意味着确实有让业内人惊讶的东西。结合 OpenAI 最近的布局（关停 Sora 独立版、发布就业政策白皮书、IPO 准备），Spud 可能是 OpenAI 在 IPO 前用来证明技术领先地位的「压箱货」。</p><p><strong>三条路线的分化才是真正的故事：Meta 选择开源（规模优先）、Anthropic 选择限制发布（安全优先）、OpenAI 择机而动（商业优先）。</strong>这不仅仅是商业策略的差异——这是三种不同的 AI 发展哲学在实践中的碰撞。Meta 赌「让所有人都能用」能建立最大的生态、Anthropic 赌「负责任的部署」能赢得监管和企业信任、OpenAI 赌「在正确的时机展示正确的能力」能同时取悦投资者和用户。</p><p><strong>我的预判：Muse Spark 的开源版本将在 2-3 周内发布，引发新一轮开源多模态 AI 的生态竞争。Anthropic Mythos 的限制发布策略将催生一个新市场——「AI 安全审计服务」，帮助企业评估是否准备好使用 Mythos 级别的 AI。OpenAI 的 Spud 发布时间将紧贴 Meta 开源 Muse Spark 之后——用封闭模型的能力优势来对冲开源的声势。最大胆预测：到 Q3，三巨头的路线分化将引发第一次严肃的「AI 监管路线之争」——政府该鼓励开源还是限制发布？Meta 和 Anthropic 将站在辩论的两端。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Meta Launches Muse Spark — Alexandr Wang's $14.3B Bet Delivers Its First Major Model, Open-Source Plans Confirmed</strong> — Meta officially released Muse Spark on April 8, the first model from its Superintelligence Labs after hiring Scale AI's Alexandr Wang in a $14.3B deal. <strong>Muse Spark excels in image and video processing benchmarks</strong> and will power Meta AI's Vibes AI video feature. Crucially: <strong>Meta plans to release it under an open-source license</strong>. The model follows Llama 4's disappointing reception and represents Zuckerberg's strategic reset. CNBC's key question: <strong>Can Muse Spark make money?</strong><br><small>Source: <a href=\"https://www.axios.com/2026/04/08/meta-muse-alexandr-wang\">Axios</a>, <a href=\"https://fortune.com/2026/04/08/meta-unveils-muse-spark-mark-zuckerberg-ai-push/\">Fortune</a>, <a href=\"https://www.cnbc.com/2026/04/09/metas-long-awaited-ai-model-is-finally-here-but-can-it-make-money.html\">CNBC</a>, <a href=\"https://www.reuters.com/sustainability/sustainable-finance-reporting/meta-unveils-first-ai-model-superintelligence-team-2026-04-08/\">Reuters</a></small></li><li><strong>Anthropic Mythos Limited Release — Restricted to Select Companies for Cybersecurity Defense</strong> — Anthropic detailed its Mythos model this week, describing it as <strong>so powerful that initial release is limited to a handful of tech companies for cybersecurity defense</strong>. This connects to last issue's report on Treasury Secretary Bessent summoning Wall Street CEOs over AI risks. Anthropic's approach: extreme capability paired with extreme caution.<br><small>Source: <a href=\"https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks\">Axios</a></small></li><li><strong>OpenAI's 'Spud' Model Imminent — Believed to Represent a 'Significant Leap Forward'</strong> — Axios reports OpenAI is finalizing a new model codenamed Spud, considered a major capability jump. Three AI giants showing new models in the same week: <strong>the Q2 2026 model war has begun</strong>.<br><small>Source: <a href=\"https://www.axios.com/2026/04/08/meta-muse-alexandr-wang\">Axios</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Q2 2026 model war: three giants show cards simultaneously — Muse Spark (released), Mythos (limited), Spud (imminent)</li><li>Open-source vs safety route divergence: Meta open-sources, Anthropic restricts, OpenAI calibrates</li><li>AI monetization pressure intensifies: investors want revenue paths, not just benchmarks</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>The real story isn't any single model — it's three giants showing cards simultaneously, and their diverging strategies revealing deep philosophical differences about AI development.</strong></p><p>Meta's Muse Spark is Alexandr Wang's first public exam. $14.3B, hundred-million-dollar engineer packages — one of Silicon Valley's most expensive AI talent deals. Muse Spark's strength in visual processing isn't accidental: <strong>Meta's core business is social media; visual content is its lifeblood.</strong> Zuckerberg's strategy: don't compete head-on with OpenAI/Anthropic on general intelligence; build differentiated advantage in visual AI, then use open-source to expand influence. But CNBC's \"can it make money\" question cuts deep — <strong>with $50B+ in AI spending, investors need a revenue path, not just benchmark numbers.</strong></p><p>Anthropic's Mythos strategy is masterful narrative-building. \"Too powerful to release broadly\" simultaneously achieves three goals: <strong>builds safety brand, creates scarcity, and implies capability superiority.</strong> The cybersecurity angle is smart — establish the model as a \"defense hero\" first, then gradually expand.</p><p>OpenAI's Spud is the biggest wildcard. \"Significant leap forward\" isn't typical AI media hyperbole — it usually means something genuinely surprised insiders. Likely OpenAI's pre-IPO showcase piece.</p><p><strong>The route divergence IS the story: Meta bets on open-source (scale-first), Anthropic on restricted release (safety-first), OpenAI on strategic timing (commercial-first). Three different AI development philosophies colliding in practice.</strong></p><p><strong>Predictions: Muse Spark open-source drops in 2-3 weeks, triggering open-source multimodal competition. Anthropic's restricted approach spawns a new \"AI safety audit\" services market. OpenAI's Spud release timed to counter Meta's open-source momentum. Boldest: by Q3, their route divergence triggers the first serious \"AI regulation philosophy\" debate — should governments encourage open-source or restrict releases? Meta and Anthropic will be on opposite sides.</strong></p></div>"
    },
    "cover": images.get("meta_fortune", "") or images.get("meta_cnbc", ""),
    "sources": [
        {
            "title": {"zh": "Meta 发布 Muse Spark：Alexandr Wang 领导下的首个 AI 模型", "en": "Meta Debuts Muse Spark, First AI Model Under Alexandr Wang"},
            "url": "https://www.axios.com/2026/04/08/meta-muse-alexandr-wang",
            "image": images.get("meta_axios", "")
        },
        {
            "title": {"zh": "Meta Muse Spark 能赚钱吗？", "en": "Can Meta's New AI Model Muse Spark Make Money?"},
            "url": "https://www.cnbc.com/2026/04/09/metas-long-awaited-ai-model-is-finally-here-but-can-it-make-money.html",
            "image": images.get("meta_cnbc", "")
        },
        {
            "title": {"zh": "Anthropic Mythos 限制发布聚焦网络安全", "en": "Anthropic Mythos Preview Limited to Cybersecurity Risks"},
            "url": "https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks",
            "image": ""
        },
        {
            "title": {"zh": "Meta 发布超级智能团队首个 AI 模型", "en": "Meta Unveils First AI Model from Superintelligence Team"},
            "url": "https://www.reuters.com/sustainability/sustainable-finance-reporting/meta-unveils-first-ai-model-superintelligence-team-2026-04-08/",
            "image": images.get("meta_reuters", "")
        }
    ]
}

# Insert new issues at the front
issues.insert(0, design_issue)
issues.insert(0, tech_issue)

with open("issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("Done! issues.json updated with 2 new entries for 2026-04-13")
