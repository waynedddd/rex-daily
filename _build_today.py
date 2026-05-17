#!/usr/bin/env python3
"""Build today's Rex Daily issues and prepend to issues.json"""
import json, os, ssl, urllib.request, re, html
from urllib.error import URLError

SSL_CTX = ssl.create_default_context()
SSL_CTX.load_verify_locations("/usr/local/lib/python3.14/site-packages/certifi/cacert.pem")

def fetch_og_image(url, timeout=8):
    """Fetch og:image from a URL, return '' on failure."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as resp:
            body = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', body, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', body, re.I)
        return html.unescape(m.group(1)) if m else ""
    except Exception:
        return ""

# Fetch og:images for sources
print("Fetching og:images...")
og_cache = {}
urls_to_fetch = [
    "https://www.figma.com/blog/state-of-the-designer-2026/",
    "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
    "https://flowstep.ai/blog/banani-alternative/",
    "https://motiff.com/",
    "https://www.forbes.com/sites/jonmarkman/2026/05/04/anthropics-900b-funding-round-set-to-surpass-openai/",
    "https://www.axios.com/2026/04/21/anthropic-outspends-openai-biggest-lobbying-quarter",
    "https://www.nytimes.com/2026/05/13/technology/ai-lobbying-washington-openai-anthropic.html",
    "https://techcrunch.com/2026/04/14/anthropics-rise-is-giving-some-openai-investors-second-thoughts/",
]
for u in urls_to_fetch:
    img = fetch_og_image(u)
    og_cache[u] = img
    print(f"  {u[:60]}... -> {'✓' if img else '✗'}")

# === DESIGN ISSUE ===
design_issue = {
    "date": "2026-05-14",
    "section": "design",
    "title": {
        "zh": "Figma「State of the Designer 2026」报告出炉：AI 正在推动设计招聘回暖，但行业情绪两极分化——Craft 成为 AI 时代的新货币",
        "en": "Figma's State of the Designer 2026: AI Is Driving Design Hiring Back Up, but the Industry Is Split — Craft Becomes the New Currency in the AI Era"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Figma 发布「State of the Designer 2026」年度报告：AI 正在推动设计招聘回暖，91% 的设计师认为清晰的目标比 AI 工具更重要</strong> — Figma 的最新年度报告揭示了一个出人意料的数据：AI 并没有取代设计师，反而推动了设计招聘需求的回升。但行业情绪高度分裂——36% 的设计师认为行业在变好，35% 认为在变差。报告的核心观点：当任何人都可以用 AI prompt 出一个原型时，「Craft（手艺）」成为了真正的差异化因素。<br><small>来源：<a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a> / <a href=\"https://www.figma.com/reports/state-of-the-designer-2026/\">Figma 完整报告</a></small></li><li><strong>2026 年 AI UI 设计工具大混战：Flowstep、Motiff、Banani 等新玩家涌入 prompt-to-UI 赛道，向 Figma Make 发起正面挑战</strong> — toools.design 的深度测评对比了 9 款 AI 设计工具：Flowstep 主打多屏工作流和一键复制到 Figma，Motiff 以生产级 React/HTML 代码导出为卖点，Banani 则强调文本到原型的风格定制。这些工具的定价在 $15-20/月之间，远低于传统设计工具。prompt-to-UI 赛道正在从「概念验证」进入「日常工具」阶段。<br><small>来源：<a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">toools.design</a> / <a href=\"https://flowstep.ai/blog/banani-alternative/\">Flowstep Blog</a></small></li><li><strong>LinkedIn 设计圈热议 Figma 报告：「挣扎中的设计师」和「兴奋中的设计师」的分水岭是什么？</strong> — Tom Scott 在 LinkedIn 上的分析引发广泛讨论：成功适应 AI 时代的设计师已经「彻底改变了工作方式和对设计的思考」，而挣扎中的设计师则「作品集为展示而优化，思考深度经不起追问」。核心洞察：系统级思维和产品思维的重要性正在超越视觉执行能力。<br><small>来源：<a href=\"https://www.linkedin.com/posts/tomscottt_figmas-report-on-the-state-of-the-designer-activity-7430526489084833792-hmwN\">Tom Scott (LinkedIn)</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 推动设计招聘回暖，但招的不再是「Figma 操作员」</strong>：企业需要的是能在 AI 工具生态中做系统级决策的设计师，纯执行层的价值在快速缩水</li><li><strong>Prompt-to-UI 工具进入「百花齐放」阶段</strong>：Flowstep、Motiff、Banani 等以 $15-20/月的价格挑战 Figma，但真正的差异化不在生成质量，而在与现有工作流的融合度</li><li><strong>「Craft」的定义正在被重新书写</strong>：不再是像素级的精致，而是洞察力、系统思维和在 AI 输出之上叠加判断力的能力</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Figma 的「State of the Designer 2026」报告里最有意思的数字不是 AI 相关的——是那个 36% vs 35% 的情绪分裂。这不是一个行业在衰退，也不是一个行业在繁荣。这是一个行业在分裂。</strong></p><p>让我把几条线索串起来。Figma 说 AI 正在推动设计招聘回暖——但 Tom Scott 在 LinkedIn 上的观察揭示了另一面：招聘回暖的受益者和被淘汰者之间，分水岭不是「会不会用 AI 工具」，而是「有没有真正的产品思维」。他说的那句话值得每个设计师贴在显示器上：<strong>「挣扎中的设计师，思考深度经不起追问」。</strong>这意味着，AI 并没有淘汰设计师这个职业——它淘汰的是那些一直在用「视觉包装」掩盖「思考缺失」的设计师。</p><p>再看 prompt-to-UI 工具的爆发。Flowstep $15/月、Motiff $20/月、Banani $20/月——这些工具的价格和一杯精品咖啡差不多。当一个非设计师可以用 $15/月的工具在 30 秒内生成一套还不错的 UI 时，「我会做好看的界面」就不再是一个有价值的职业卖点了。<strong>但这恰恰是 Figma 报告中「Craft」概念变得重要的原因：真正的 Craft 不是像素级的精致（AI 已经可以做到），而是理解为什么这个界面应该长这样，而不是那样。</strong></p><p>这里有一个有趣的悖论。prompt-to-UI 工具越强大，「系统级设计思维」就越值钱。因为当任何人都能生成界面时，真正的挑战变成了：<strong>在 50 个 AI 生成的方案中选出正确的那一个，并能清晰解释为什么。</strong>这需要对用户行为、商业逻辑和技术约束的深度理解——恰恰是 AI 最不擅长的领域。</p><p>我的预测：<strong>2026 年下半年，我们会看到设计师角色的正式分化。</strong>一类是「AI Design Orchestrator」——精通多种 AI 工具、负责整合和决策的高级角色，薪资将大幅上涨。另一类是传统的 UI 设计师，如果不转型，将被 $15/月的工具和会用 prompt 的 PM 逐渐替代。Figma 的报告数据已经在暗示这个分化：那 36% 觉得行业在变好的设计师，很可能就是前一类；而 35% 觉得在变差的，大概率是后一类。<strong>这不是悲观主义，这是现实主义。设计行业不会消亡——但「设计师」这个词的含义正在被重新定义。</strong></p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Figma Releases 'State of the Designer 2026' Report: AI Is Driving Design Hiring Recovery, 91% of Designers Say Clear Goals Matter More Than AI Tools</strong> — Figma's annual report reveals a surprising finding: AI isn't replacing designers but driving renewed hiring demand. Yet the industry is deeply split — 36% say the profession is improving, 35% say it's declining. Core insight: when anyone can prompt their way to a prototype, 'Craft' becomes the true differentiator.<br><small>Source: <a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a> / <a href=\"https://www.figma.com/reports/state-of-the-designer-2026/\">Full Report</a></small></li><li><strong>2026's AI UI Design Tool Explosion: Flowstep, Motiff, Banani and Others Storm the Prompt-to-UI Space, Challenging Figma Make Head-On</strong> — A deep-dive comparison of 9 AI design tools shows Flowstep excelling at multi-screen workflows with instant Figma export, Motiff offering production-ready React/HTML code, and Banani focusing on text-to-prototype style customization. Pricing at $15-20/month, far below traditional design tools. The prompt-to-UI space is moving from proof-of-concept to daily tool.<br><small>Source: <a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">toools.design</a> / <a href=\"https://flowstep.ai/blog/banani-alternative/\">Flowstep Blog</a></small></li><li><strong>LinkedIn Design Community Debates Figma Report: What Separates Struggling Designers from Thriving Ones?</strong> — Tom Scott's analysis went viral: designers thriving in the AI era have 'completely changed how they work and think about design,' while struggling designers have 'portfolios optimized for polished presentations' with 'thinking that, when probed, turns out to have been done largely by a PM.' Systems thinking and product thinking now outweigh visual execution skills.<br><small>Source: <a href=\"https://www.linkedin.com/posts/tomscottt_figmas-report-on-the-state-of-the-designer-activity-7430526489084833792-hmwN\">Tom Scott (LinkedIn)</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Driving Design Hiring — But Not for 'Figma Operators'</strong>: companies want designers who make system-level decisions across AI tool ecosystems; pure execution value is shrinking fast</li><li><strong>Prompt-to-UI Tools Enter the 'Cambrian Explosion'</strong>: Flowstep, Motiff, Banani challenge Figma at $15-20/month, but true differentiation lies in workflow integration, not generation quality</li><li><strong>'Craft' Is Being Redefined</strong>: no longer pixel perfection but insight, systems thinking, and the ability to layer judgment on top of AI output</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>The most interesting number in Figma's 'State of the Designer 2026' report isn't AI-related — it's the 36% vs 35% sentiment split. This isn't an industry in decline or boom. It's an industry fracturing.</strong></p><p>Let me connect the dots. Figma says AI is driving design hiring back — but Tom Scott's LinkedIn analysis reveals the other side: the divide between those benefiting and those being left behind isn't 'can you use AI tools,' it's 'do you have genuine product thinking.' His quote deserves to be on every designer's monitor: <strong>'Struggling designers have thinking that, when probed, turns out to have been done largely by a PM.'</strong> AI isn't eliminating the design profession — it's eliminating designers who've been using visual polish to mask shallow thinking.</p><p>Now look at the prompt-to-UI explosion. Flowstep at $15/month, Motiff at $20/month, Banani at $20/month — these cost about the same as a specialty coffee. When a non-designer can generate decent UI in 30 seconds for $15/month, 'I make pretty interfaces' stops being a viable career proposition. <strong>But this is precisely why 'Craft' in Figma's report matters: real craft isn't pixel perfection (AI already does that) — it's understanding why an interface should look this way and not that way.</strong></p><p>Here's the fascinating paradox: the more powerful prompt-to-UI tools become, the more valuable 'systems-level design thinking' gets. Because when anyone can generate interfaces, the real challenge becomes: <strong>choosing the right one from 50 AI-generated options, and clearly explaining why.</strong> That requires deep understanding of user behavior, business logic, and technical constraints — exactly what AI is worst at.</p><p><strong>My prediction: H2 2026 will see formal bifurcation of the designer role. One track: 'AI Design Orchestrator' — senior roles mastering multiple AI tools, responsible for integration and decision-making, with rising salaries. The other: traditional UI designers who, without transformation, will be gradually replaced by $15/month tools and prompt-savvy PMs. Figma's data already hints at this split: those 36% who feel optimistic are likely the first group; the 35% feeling pessimistic, the second. This isn't pessimism — it's realism. The design industry won't die, but the meaning of 'designer' is being rewritten.</strong></p></div>"
    },
    "cover": og_cache.get("https://www.figma.com/blog/state-of-the-designer-2026/", ""),
    "sources": [
        {
            "url": "https://www.figma.com/blog/state-of-the-designer-2026/",
            "title": {"zh": "Figma Blog: State of the Designer 2026", "en": "State of the Designer 2026: Designers Are Leaning Into the Messy Middle"},
            "image": og_cache.get("https://www.figma.com/blog/state-of-the-designer-2026/", "")
        },
        {
            "url": "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
            "title": {"zh": "9 款最佳 AI UI/UX 设计工具深度测评 (2026)", "en": "9 Best AI Tools for UI/UX Designers in 2026: Deep Dive"},
            "image": og_cache.get("https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026", "")
        },
        {
            "url": "https://www.linkedin.com/posts/tomscottt_figmas-report-on-the-state-of-the-designer-activity-7430526489084833792-hmwN",
            "title": {"zh": "Tom Scott 解读 Figma 设计师报告：行业正在分裂", "en": "Tom Scott: Figma's State of the Designer 2026 — The Industry Is Split"},
            "image": ""
        },
        {
            "url": "https://flowstep.ai/blog/banani-alternative/",
            "title": {"zh": "8 款 Banani 替代品：AI UI 设计工具对比", "en": "8 Best Banani Alternatives for AI UI Design"},
            "image": og_cache.get("https://flowstep.ai/blog/banani-alternative/", "")
        }
    ]
}

# === TECH ISSUE ===
tech_issue = {
    "date": "2026-05-14",
    "section": "tech",
    "title": {
        "zh": "Anthropic 估值冲击 9000 亿美元超越 OpenAI、硅谷 AI 游说支出创纪录、Google I/O 前夕 Gemini Omni 截图泄露——AI 权力格局正在重新洗牌",
        "en": "Anthropic Eyes $900B Valuation to Surpass OpenAI, Silicon Valley AI Lobbying Hits Record, Gemini Omni Leaked Ahead of Google I/O — The AI Power Map Is Being Redrawn"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Anthropic 正在谈判以 9000 亿美元估值融资，将超越 OpenAI 成为全球最高估值 AI 公司</strong> — 据 Bloomberg 和 Forbes 报道，Anthropic 给投资者 48 小时窗口提交认购意向，估值可能超过 9000 亿美元——超过 OpenAI 3 月融资时的 8520 亿美元。Anthropic 的年化收入从 2024 年 12 月的 10 亿美元飙升至 2026 年 3 月的 300 亿美元，主要由 Claude Code 等编码工具驱动。但 OpenAI 公开质疑 Anthropic 的收入统计口径，称其使用了毛收入而非净收入计算方式。<br><small>来源：<a href=\"https://www.forbes.com/sites/jonmarkman/2026/05/04/anthropics-900b-funding-round-set-to-surpass-openai/\">Forbes</a> / <a href=\"https://techcrunch.com/2026/04/14/anthropics-rise-is-giving-some-openai-investors-second-thoughts/\">TechCrunch</a></small></li><li><strong>硅谷 AI 游说支出创历史新高：Anthropic Q1 花 160 万美元超过 OpenAI 的 100 万美元，Meta 以 710 万美元领跑</strong> — Axios 报道，Anthropic 2026 Q1 游说支出同比增长 344%（从 36 万到 160 万美元），OpenAI 增长 78.6%。Anthropic 的游说重点是与五角大楼就技术使用红线进行博弈——特朗普政府官员指责 Anthropic「太 woke」。纽约时报 5 月 13 日的深度报道进一步揭示，OpenAI 在 DC 租下两层办公楼，Anthropic 4 月在华盛顿开设首个办公室。<br><small>来源：<a href=\"https://www.axios.com/2026/04/21/anthropic-outspends-openai-biggest-lobbying-quarter\">Axios</a> / <a href=\"https://www.nytimes.com/2026/05/13/technology/ai-lobbying-washington-openai-anthropic.html\">New York Times</a></small></li><li><strong>Google I/O（5 月 19-20 日）前夕密集放料：Gemini Omni 截图泄露、Android 上 Gemini 获得跨应用自动化能力、「Googlebooks」AI 笔记本电脑曝光</strong> — Google I/O 还有 5 天，但信号已经密集释放：Gemini Omni 的泄露截图显示它可能整合视频编辑到聊天界面；Android 上的 Gemini Intelligence 获得了多步骤跨应用自动化和主动填表能力；最大胆的是代号「Googlebooks」的 Android 笔记本电脑——从操作系统层面内置 Gemini，支持通过 prompt 生成自定义 widget。<br><small>来源：<a href=\"https://www.youtube.com/watch?v=qBeGwnrxtrE\">ziobuddalabs (YouTube)</a></small></li><li><strong>Meta AI 推出 Muse Spark 驱动的语音对话：支持自然打断、对话中切换语言、边聊天边生成图片、通过摄像头实时分析环境</strong> — Meta 发布了 AI 语音对话的重大更新：Muse Spark 引擎让对话支持自然中断和语言切换，同时能在对话过程中生成图片并通过手机摄像头分析周围环境。这是迄今为止最接近「真人助手」体验的 AI 语音交互。<br><small>来源：<a href=\"https://www.youtube.com/watch?v=qBeGwnrxtrE\">ziobuddalabs (YouTube)</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 估值战进入「万亿美元」射程</strong>：Anthropic 9000 亿 vs OpenAI 8520 亿，两家公司的估值之和已超过全球大多数国家的 GDP——但盈利模型仍然高度不确定</li><li><strong>AI 公司从「技术竞赛」转向「政治竞赛」</strong>：游说支出暴增 300%+，DC 办公室纷纷开张，AI 监管的博弈正在从硅谷的会议室移到华盛顿的走廊</li><li><strong>Google I/O 前的「地毯式轰炸」暗示大招</strong>：在正式大会前发布 Gemini Android 自动化、泄露 Gemini Omni、曝光 AI 笔记本——Google 可能在准备一个「平台级」而非「功能级」的发布</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Anthropic 估值冲击 9000 亿美元这件事，表面上是融资新闻，底下是一场关于「AI 公司到底值多少钱」的认知战争。</strong></p><p>先看数字的荒谬性。Anthropic 的年化收入 300 亿美元，如果按 9000 亿估值算，PS 比（市销率）是 30 倍。作为对比，巅峰时期的 Salesforce PS 比大约 12 倍，最疯狂的 SaaS 泡沫期也就 25 倍左右。而且 OpenAI 还公开质疑 Anthropic 用的是毛收入口径——如果按净收入算，实际数字可能大幅缩水。<strong>但这不重要。因为在 2026 年的 AI 融资市场里，估值不是财务指标，是信仰指标。</strong>投资者买的不是 Anthropic 今天的收入，是「Claude 可能成为 AGI 时代的操作系统」这个叙事。</p><p>更值得关注的是游说支出的爆炸。Anthropic Q1 游说支出同比增长 344%，这个数字比它任何模型的性能提升都惊人。为什么？因为 Anthropic 正在两条战线同时作战：一边要说服五角大楼自己的技术可以用于国防（以获取政府合同），一边又要维持自己「安全优先」的品牌形象（以保持 B 轮投资者的信任）。<strong>被特朗普政府指责「太 woke」这件事，对 Anthropic 来说是真正的战略威胁——不是因为政治立场，而是因为美国政府合同（尤其是国防和情报领域）是 AI 公司最大的潜在收入来源之一。</strong></p><p>把这些和 Google I/O 前的密集放料放在一起看，你会发现 2026 年 5 月可能是 AI 产业格局重塑的关键月份。Google 在 I/O 前释放 Gemini Omni 泄露、Android 自动化、AI 笔记本——这不是正常的预热，这是战略性的信息释放，目的是在 Anthropic 融资窗口期分散市场注意力。<strong>如果 Google 在 5 月 19 日宣布 Gemini 深度集成 Android + Chrome + Workspace 的「全平台 AI」策略，那 Anthropic 的 9000 亿估值叙事就会面临一个根本性的挑战：在 Google 拥有 30 亿+ 设备分发渠道的情况下，一个没有自有平台的 AI 公司，凭什么值这么多？</strong></p><p>Meta 的 Muse Spark 语音对话虽然没有上头条，但可能是本周最有产品洞察力的发布。<strong>「边聊天边生成图片、通过摄像头分析环境」——这不是一个 AI 功能，这是一个新的交互范式。</strong>当 AI 助手能同时理解你说的话和你看到的东西，传统的「点击-输入-等待」交互模式就开始显得过时了。设计师们注意：下一代产品的核心交互可能不再是屏幕上的按钮，而是语音 + 视觉的多模态流。</p><p><strong>总结：本周的新闻画了一幅清晰的图——AI 竞争正在从三个维度同时展开：技术（模型能力）、资本（估值和融资）、政治（游说和监管）。任何只关注其中一个维度的分析都是不完整的。Anthropic 可能有最好的模型，但如果游说失败失去政府合同，或者 Google 在平台层面完成包围，9000 亿美元估值就是空中楼阁。这场游戏的赢家，不一定是技术最强的，而是在三个维度上最平衡的。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Anthropic in Talks for $900B Valuation Round, Would Surpass OpenAI as World's Highest-Valued AI Company</strong> — Per Bloomberg and Forbes, Anthropic gave investors a 48-hour window to submit allocation interest at a valuation potentially exceeding $900 billion — surpassing OpenAI's $852B from March. Anthropic's annualized revenue surged from $1B in December 2024 to $30B by March 2026, driven by Claude Code and coding tools. However, OpenAI disputes Anthropic's revenue methodology, claiming it uses gross rather than net revenue accounting.<br><small>Source: <a href=\"https://www.forbes.com/sites/jonmarkman/2026/05/04/anthropics-900b-funding-round-set-to-surpass-openai/\">Forbes</a> / <a href=\"https://techcrunch.com/2026/04/14/anthropics-rise-is-giving-some-openai-investors-second-thoughts/\">TechCrunch</a></small></li><li><strong>Silicon Valley AI Lobbying Hits Record: Anthropic Spends $1.6M in Q1 Beating OpenAI's $1M, Meta Leads at $7.1M</strong> — Anthropic's Q1 2026 lobbying spend surged 344% YoY (from $360K to $1.6M), while OpenAI's grew 78.6%. Anthropic's lobbying focus: battling the Pentagon over technology use red lines — with Trump administration officials accusing the company of being 'woke.' NYT's May 13 deep-dive reveals OpenAI leased two floors in DC; Anthropic opened its first Washington office in April.<br><small>Source: <a href=\"https://www.axios.com/2026/04/21/anthropic-outspends-openai-biggest-lobbying-quarter\">Axios</a> / <a href=\"https://www.nytimes.com/2026/05/13/technology/ai-lobbying-washington-openai-anthropic.html\">New York Times</a></small></li><li><strong>Pre-Google I/O (May 19-20) Carpet Bombing: Gemini Omni Screenshot Leaked, Gemini Gets Cross-App Automation on Android, 'Googlebooks' AI Laptop Revealed</strong> — Five days before I/O, signals are dense: leaked Gemini Omni screenshots suggest video editing integrated into chat; Gemini Intelligence on Android gains multi-step cross-app automation and proactive autofill; the boldest reveal is codename 'Googlebooks' — Android laptops with Gemini baked into the OS, supporting prompt-generated custom widgets.<br><small>Source: <a href=\"https://www.youtube.com/watch?v=qBeGwnrxtrE\">ziobuddalabs (YouTube)</a></small></li><li><strong>Meta AI Launches Muse Spark-Powered Voice Conversations: Natural Interruptions, Mid-Conversation Language Switching, Image Generation While Talking, Real-Time Camera Analysis</strong> — Meta's major AI voice update: Muse Spark engine enables natural conversation interruption and language switching, generates images during conversation, and analyzes surroundings through phone camera in real-time. The closest thing yet to a 'human assistant' voice AI experience.<br><small>Source: <a href=\"https://www.youtube.com/watch?v=qBeGwnrxtrE\">ziobuddalabs (YouTube)</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Valuations Enter 'Trillion-Dollar' Range</strong>: Anthropic $900B vs OpenAI $852B — combined valuation exceeds most countries' GDP, yet profitability models remain highly uncertain</li><li><strong>AI Companies Shift from 'Tech Race' to 'Political Race'</strong>: lobbying spend up 300%+, DC offices opening, AI regulation battles moving from Silicon Valley boardrooms to Washington corridors</li><li><strong>Pre-Google I/O 'Carpet Bombing' Signals Something Big</strong>: releasing Gemini Android automation, leaking Gemini Omni, and revealing AI laptops before the main event — Google may be preparing a 'platform-level' rather than 'feature-level' announcement</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Anthropic's push toward a $900B valuation is, on the surface, a funding story. Underneath, it's a cognitive war about what AI companies are actually worth.</strong></p><p>The absurdity of the numbers: Anthropic at $30B annualized revenue with a $900B valuation means a 30x price-to-sales ratio. For comparison, peak Salesforce was around 12x; the craziest SaaS bubble peaked at roughly 25x. And OpenAI publicly disputes Anthropic's revenue methodology. <strong>But this doesn't matter. In 2026's AI funding market, valuation isn't a financial metric — it's a faith metric.</strong> Investors aren't buying Anthropic's current revenue; they're buying the narrative that Claude might become the operating system of the AGI era.</p><p>The lobbying spend explosion deserves more attention. Anthropic's Q1 lobbying grew 344% YoY — more impressive than any model benchmark improvement. Why? Anthropic is fighting on two fronts simultaneously: convincing the Pentagon its tech is suitable for defense (to win government contracts) while maintaining its 'safety-first' brand (to keep Series B investors' trust). <strong>Being called 'too woke' by the Trump administration is a genuine strategic threat — not because of politics, but because US government contracts (especially defense and intelligence) represent one of AI companies' largest potential revenue streams.</strong></p><p>Combined with Google's pre-I/O carpet bombing, May 2026 may be the pivotal month for AI industry power restructuring. Google releasing Gemini Omni leaks, Android automation, and AI laptops before I/O isn't normal pre-event hype — it's strategic information warfare designed to distract markets during Anthropic's funding window. <strong>If Google announces deep Gemini integration across Android + Chrome + Workspace as a 'full-platform AI' strategy on May 19, Anthropic's $900B valuation narrative faces a fundamental challenge: with Google owning 3B+ device distribution channels, what justifies this valuation for an AI company without its own platform?</strong></p><p>Meta's Muse Spark voice conversations didn't make headlines but may be the week's most product-insightful launch. <strong>'Generating images while talking, analyzing surroundings through camera' — this isn't an AI feature, it's a new interaction paradigm.</strong> When an AI assistant simultaneously understands what you're saying and what you're seeing, the traditional 'click-type-wait' interaction model starts looking obsolete. Designers take note: the next generation of products may center not on on-screen buttons but on voice + vision multimodal flows.</p><p><strong>Bottom line: this week's news paints a clear picture — AI competition is unfolding across three dimensions simultaneously: technology (model capabilities), capital (valuations and funding), and politics (lobbying and regulation). Any analysis focusing on just one dimension is incomplete. Anthropic may have the best models, but if lobbying fails and government contracts are lost, or Google completes a platform-level encirclement, $900B is a castle in the sky. The winner of this game won't necessarily be the technically strongest — but the most balanced across all three dimensions.</strong></p></div>"
    },
    "cover": og_cache.get("https://www.forbes.com/sites/jonmarkman/2026/05/04/anthropics-900b-funding-round-set-to-surpass-openai/", ""),
    "sources": [
        {
            "url": "https://www.forbes.com/sites/jonmarkman/2026/05/04/anthropics-900b-funding-round-set-to-surpass-openai/",
            "title": {"zh": "Anthropic 9000 亿美元融资轮将超越 OpenAI", "en": "Anthropic's $900 Billion Funding Round Set To Surpass OpenAI"},
            "image": og_cache.get("https://www.forbes.com/sites/jonmarkman/2026/05/04/anthropics-900b-funding-round-set-to-surpass-openai/", "")
        },
        {
            "url": "https://www.axios.com/2026/04/21/anthropic-outspends-openai-biggest-lobbying-quarter",
            "title": {"zh": "Anthropic 游说支出超越 OpenAI 创历史新高", "en": "Anthropic Outspends OpenAI in Biggest-Ever Lobbying Quarter"},
            "image": og_cache.get("https://www.axios.com/2026/04/21/anthropic-outspends-openai-biggest-lobbying-quarter", "")
        },
        {
            "url": "https://www.nytimes.com/2026/05/13/technology/ai-lobbying-washington-openai-anthropic.html",
            "title": {"zh": "纽约时报：硅谷 AI 游说战达到白热化", "en": "Silicon Valley's A.I. Lobbying Blitz Reaches a Fever Pitch"},
            "image": og_cache.get("https://www.nytimes.com/2026/05/13/technology/ai-lobbying-washington-openai-anthropic.html", "")
        },
        {
            "url": "https://techcrunch.com/2026/04/14/anthropics-rise-is-giving-some-openai-investors-second-thoughts/",
            "title": {"zh": "TechCrunch: Anthropic 的崛起让 OpenAI 投资者犹豫了", "en": "Anthropic's Rise Is Giving Some OpenAI Investors Second Thoughts"},
            "image": og_cache.get("https://techcrunch.com/2026/04/14/anthropics-rise-is-giving-some-openai-investors-second-thoughts/", "")
        }
    ]
}

# Load existing issues and prepend
issues_path = os.path.join(os.path.dirname(__file__), "issues.json")
with open(issues_path, "r", encoding="utf-8") as f:
    existing = json.load(f)

# Prepend new issues (design first, then tech)
existing = [design_issue, tech_issue] + existing

with open(issues_path, "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Total issues: {len(existing)}")
print(f"New design issue: {design_issue['title']['zh'][:50]}...")
print(f"New tech issue: {tech_issue['title']['zh'][:50]}...")
