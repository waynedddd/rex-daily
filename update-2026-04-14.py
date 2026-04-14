#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rex Daily update for 2026-04-14"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=8)
        content = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', content, re.IGNORECASE)
        return html.unescape(m.group(1)) if m else ""
    except:
        return ""

# Fetch og:images
design_urls = {
    "stitch": "https://muz.li/blog/google-just-introduced-vibe-design-heres-what-it-means-for-ui-designers/",
    "unite": "https://www.unite.ai/best-ai-ux-ui-design-tools/",
    "livemint": "https://www.livemint.com/ai/artificial-intelligence/google-stitch-vibe-design-ai-tool-week-product-development-11774702986888.html",
}
tech_urls = {
    "bi": "https://www.businessinsider.com/anthropic-may-soon-pass-openai-measure-ai-business-spending-ramp-2026-4",
    "axios": "https://www.axios.com/2026/03/18/ai-enterprise-revenue-anthropic-openai",
    "bloomberg_cyber": "https://www.bloomberg.com/news/videos/2026-04-13/bloomberg-tech-4-13-2026-video",
    "bloomberg_openai": "https://www.bloomberg.com/news/audio/2026-04-01/bloomberg-tech-openai-tops-850-billion-valuation-podcast-mngjjaem",
}

print("Fetching og:images...")
imgs = {}
for k, u in {**design_urls, **tech_urls}.items():
    imgs[k] = get_og_image(u)
    print(f"  {k}: {imgs[k][:60] if imgs[k] else '(none)'}")

design_issue = {
    "date": "2026-04-14",
    "section": "design",
    "title": {
        "zh": "Google Stitch 推出「Vibe Design」：Agent Manager 并行探索多方向 · AI 设计工具按角色分化加速 · Figma Make 嵌入无处不在",
        "en": "Google Stitch Launches 'Vibe Design': Agent Manager for Parallel Explorations · AI Design Tools Segment by Role · Figma Make Embeds Everywhere"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul><li><strong>Google Stitch 更新「Vibe Design」——Agent Manager 让设计探索从串行变并行</strong> — Google Stitch（前身为 Galileo AI）推出重大更新，核心功能包括：<strong>Vibe Design（自然语言描述 → 多屏 UI）、DESIGN.md（从公司 URL 自动提取品牌规范）、以及 Agent Manager（同时生成 3 个设计方向）</strong>。这意味着设计师的工作从「一个方案做到底再改」变成了「同时探索多个方向再选最好的」——这是设计方法论层面的变革，不只是效率提升。Stitch 的免费策略也在给 Figma 施压。<br><small>来源：<a href="https://www.livemint.com/ai/artificial-intelligence/google-stitch-vibe-design-ai-tool-week-product-development-11774702986888.html">Mint</a>、<a href="https://muz.li/blog/google-just-introduced-vibe-design-heres-what-it-means-for-ui-designers/">Muzli</a>、<a href="https://tech-insider.org/google-stitch-ai-design-tool-march-2026-update/">Tech Insider</a></small></li><li><strong>AI 设计工具 2026 全景：从「谁最强」到「谁最适合你」</strong> — Unite.AI 的横评测试了 7 款主流 AI UX/UI 工具：<strong>Banani 专注 prompt-to-UI 的快速原型、Google Stitch 强调多屏流程生成、Visily 面向非设计师的低代码 UI、Lovable 聚焦完整产品流程和交互模型</strong>。值得注意的是，这些工具不再互相竞争同一个市场——它们在按使用者角色和工作流阶段分化。PM 用一种、设计师用一种、工程师用另一种。<strong>「AI 设计工具」作为统一品类正在消失，取而代之的是按思维模式分化的工具谱系。</strong><br><small>来源：<a href="https://www.unite.ai/best-ai-ux-ui-design-tools/">Unite.AI</a>、<a href="https://www.banani.co/blog/galileo-ai-features-and-alternatives">Banani</a></small></li><li><strong>Figma Make 原型嵌入扩展到 Design、FigJam 和 Slides</strong> — Figma 宣布 Figma Make 原型现在可以嵌入到 Figma Design、FigJam 和 Figma Slides 中，同时推出新的编辑工具。此外，Figma Make 已面向政府部门开放（Figma for Government）。这意味着 AI 生成的原型不再是独立产物，而是<strong>嵌入到设计师已有工作流的每个环节中</strong>——从设计文件到白板到演示文稿。<br><small>来源：<a href="https://www.figma.com/solutions/ai-design-generator/">Figma</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>从「单方案迭代」到「多方向并行探索」</strong>：Google Stitch 的 Agent Manager 代表了 AI 对设计方法论的根本改变</li><li><strong>AI 设计工具按角色和工作阶段分化</strong>：不再是「谁最好」的问题，而是「谁最适合你当前的任务」</li><li><strong>AI 原型嵌入主流工具</strong>：Figma Make 的嵌入策略让 AI 生成物成为工作流的自然组成部分</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>今天设计板块最值得关注的不是某个工具的新功能，而是一个正在发生的范式转移：AI 正在改变设计师「怎么想」，而不只是「怎么做」。</strong></p><p>Google Stitch 的 Agent Manager 看似只是一个产品功能，但它背后的逻辑极其深远。传统设计流程是线性的——你有一个想法，做一个方案，展示给利益相关者，收到反馈，改，再改。Agent Manager 把这个过程变成了并行的：<strong>你描述一个设计意图，AI 同时生成 3 个方向，你的工作从「创造方案」变成了「选择和引导方向」</strong>。这和上期报道的 Anthropic Agentic Coding 趋势报告完全呼应——无论是写代码还是做设计，人类的角色都在从执行者变成决策者和策展人。</p><p>但我想指出一个大家可能忽略的风险：<strong>并行探索听起来美好，但如果设计师缺乏判断力，3 个 AI 方向可能都是平庸的变体</strong>。AI 能扩大探索空间，但不能替你定义什么是「好的方向」。DESIGN.md 的概念也很聪明——把品牌规范变成 AI 可读的格式——但品牌不只是颜色和字体，它是一种感觉、一种态度。<strong>目前没有任何 AI 工具能真正理解「品牌气质」</strong>，它们只能做到视觉一致性，而非情感一致性。</p><p>Unite.AI 的工具全景图佐证了我上期的观察：AI 设计工具市场正在快速分化。Banani 给需要快速出图的人、Stitch 给想探索多屏流程的人、Visily 给不会设计的 PM、Lovable 给想直接做产品原型的人。这种分化意味着<strong>「全能型 AI 设计工具」是个伪命题——就像你不会期望一把瑞士军刀替代厨师的全套刀具</strong>。未来最有效率的设计师不是精通某一个工具的人，而是能在 3-4 个 AI 工具之间流畅切换、把不同工具的产出编织成连贯叙事的人。</p><p>Figma Make 的嵌入策略值得单独说。<strong>Figma 的真正护城河不是 AI 功能本身——Google Stitch 免费且能力强——而是生态位</strong>。当 AI 原型可以嵌入到 Design、FigJam、Slides 的每一个环节时，Figma 实际上在说：「你可以用任何 AI 生成设计，但你最终还是要回到 Figma 来协作、交付和展示。」这是一个平台策略，不是功能策略。Google Stitch 的免费和强大会蚕食 Figma 的早期设计环节，但 Figma 把 AI 原型变成生态的一部分——这是防守中的进攻。</p><p><strong>我的预判：Google Stitch 的 Agent Manager 概念会在 3-6 个月内被 Figma Make 复制——Figma 不会在「并行探索」上缺席太久。但真正的战场不在功能层面，而在「谁拥有设计师的工作流」。Figma 的嵌入策略和 Stitch 的免费策略会形成一种微妙的共生——设计师用 Stitch 快速探索，然后把结果带回 Figma 精修和交付。最大胆预测：到 2026 年底，主流设计工作流将是「AI 工具矩阵」而非「单一工具」——像开发者用 VS Code + GitHub + CI/CD 一样，设计师将用 Stitch/Banani（探索） + Figma（精修/协作） + Lovable/Cursor（原型到代码）的组合。单一工具时代结束了。</strong></p></div>',
        "en": '<h3>📌 AI × Design</h3><ul><li><strong>Google Stitch Launches \'Vibe Design\' — Agent Manager Enables Parallel Design Exploration</strong> — Google Stitch (formerly Galileo AI) ships a major update: <strong>Vibe Design (natural language → multi-screen UI), DESIGN.md (auto-extract brand specs from company URL), and Agent Manager (generate 3 design directions simultaneously)</strong>. This shifts design methodology from sequential iteration to parallel exploration. Stitch\'s free pricing also pressures Figma.<br><small>Source: <a href="https://www.livemint.com/ai/artificial-intelligence/google-stitch-vibe-design-ai-tool-week-product-development-11774702986888.html">Mint</a>, <a href="https://muz.li/blog/google-just-introduced-vibe-design-heres-what-it-means-for-ui-designers/">Muzli</a>, <a href="https://tech-insider.org/google-stitch-ai-design-tool-march-2026-update/">Tech Insider</a></small></li><li><strong>AI Design Tools 2026 Landscape: From \'Who\'s Best\' to \'Who Fits You\'</strong> — Unite.AI tested 7 major AI UX/UI tools: <strong>Banani for prompt-to-UI prototyping, Google Stitch for multi-screen flows, Visily for non-designer low-code UI, Lovable for full product flows</strong>. These tools no longer compete in one market — they segment by user role and workflow stage. <strong>\"AI design tool\" as a unified category is dissolving into a spectrum organized by thinking mode.</strong><br><small>Source: <a href="https://www.unite.ai/best-ai-ux-ui-design-tools/">Unite.AI</a>, <a href="https://www.banani.co/blog/galileo-ai-features-and-alternatives">Banani</a></small></li><li><strong>Figma Make Prototypes Now Embed in Design, FigJam, and Slides</strong> — Figma announced Make prototypes can now embed across Figma Design, FigJam, and Slides, plus new editing tools. Figma Make also launches for Government. AI-generated prototypes become <strong>native parts of existing workflows</strong> rather than standalone outputs.<br><small>Source: <a href="https://www.figma.com/solutions/ai-design-generator/">Figma</a></small></li></ul><h3>🔄 Trends</h3><ul><li>From sequential iteration to parallel exploration: Stitch Agent Manager changes design methodology</li><li>AI design tools segment by role and workflow stage, not feature competition</li><li>AI prototypes embed into mainstream tools: Figma Make becomes workflow-native</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Today\'s design news isn\'t about any single feature — it\'s a paradigm shift: AI is changing how designers think, not just how they execute.</strong></p><p>Stitch\'s Agent Manager looks like a product feature, but the logic runs deep. Traditional design is linear: idea → mockup → feedback → revise. Agent Manager makes it parallel: <strong>describe intent, get 3 directions, your job shifts from creating solutions to choosing and guiding directions.</strong> This echoes Anthropic\'s Agentic Coding trends — whether coding or designing, humans are moving from executor to curator.</p><p>But here\'s the risk most overlook: <strong>parallel exploration is only as good as the designer\'s judgment. Without taste, 3 AI directions may just be 3 mediocre variants.</strong> DESIGN.md is clever — brand specs in AI-readable format — but brands aren\'t just colors and fonts; they\'re feelings. No AI tool truly understands \"brand soul\" yet.</p><p>The tool landscape confirms last issue\'s observation: the market is fragmenting fast. <strong>A \"do-everything AI design tool\" is a myth — like expecting a Swiss Army knife to replace a chef\'s knife set.</strong> The most effective designers will fluently switch between 3-4 AI tools, weaving outputs into coherent narratives.</p><p>Figma Make\'s embed strategy deserves its own analysis. <strong>Figma\'s moat isn\'t AI features — Google Stitch is free and capable — it\'s ecosystem position.</strong> By embedding AI prototypes into Design, FigJam, and Slides, Figma says: \"Generate anywhere, but you\'ll collaborate and deliver here.\" This is platform strategy, not feature strategy.</p><p><strong>Predictions: Figma copies Agent Manager-style parallel exploration within 3-6 months. But the real battle is workflow ownership, not features. Stitch\'s free model and Figma\'s ecosystem create symbiosis — designers explore in Stitch, refine in Figma. Boldest: by year-end, the standard design workflow becomes a \"tool matrix\" — Stitch/Banani (explore) + Figma (refine/collaborate) + Lovable/Cursor (prototype-to-code). The single-tool era is over.</strong></p></div>'
    },
    "cover": imgs.get("stitch") or imgs.get("livemint") or "",
    "sources": [
        {
            "title": {"zh": "Google Stitch 推出 Vibe Design 消除设计瓶颈", "en": "Google Stitch Eliminates Design Bottlenecks with Vibe Design"},
            "url": "https://www.livemint.com/ai/artificial-intelligence/google-stitch-vibe-design-ai-tool-week-product-development-11774702986888.html",
            "image": imgs.get("livemint", "")
        },
        {
            "title": {"zh": "Google 推出「Vibe Design」对 UI 设计师意味着什么", "en": "Google Just Introduced Vibe Design — What It Means for UI Designers"},
            "url": "https://muz.li/blog/google-just-introduced-vibe-design-heres-what-it-means-for-ui-designers/",
            "image": imgs.get("stitch", "")
        },
        {
            "title": {"zh": "2026 年 7 款最佳 AI UX/UI 设计工具", "en": "7 Best AI UX and UI Design Tools (April 2026)"},
            "url": "https://www.unite.ai/best-ai-ux-ui-design-tools/",
            "image": imgs.get("unite", "")
        },
        {
            "title": {"zh": "Figma AI 设计生成器", "en": "Figma AI Design Generator"},
            "url": "https://www.figma.com/solutions/ai-design-generator/",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-04-14",
    "section": "tech",
    "title": {
        "zh": "Anthropic 企业支出即将超越 OpenAI：Ramp 数据显示差距仅 4.6% · 73% 新企业 AI 采购选择 Anthropic · 监管机构警告 AI 网络安全进入新纪元",
        "en": "Anthropic Closing In on OpenAI in Enterprise Spending: Ramp Shows 4.6% Gap · 73% of New AI Buyers Choose Anthropic · Regulators Warn of New AI Cyber Risk Era"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul><li><strong>Anthropic 企业 AI 支出即将超越 OpenAI——Ramp 数据揭示戏剧性逆转</strong> — Ramp（企业信用卡和财务自动化平台）最新数据显示，<strong>Anthropic 现占企业 AI 工具支出的 30.6%，OpenAI 为 35.2%——差距仅 4.6 个百分点且在快速缩小</strong>。更惊人的数据：<strong>在首次购买 AI 工具的企业中，73% 选择了 Anthropic</strong>，这意味着新增市场已经被 Anthropic 主导。Business Insider 报道，Claude Code 是 Anthropic 企业增长的主要驱动力，而 2 月份 Anthropic 拒绝五角大楼合同、OpenAI 接手的事件反而为 Anthropic 带来了意外的声誉红利——Claude 一度在 App Store 超越 ChatGPT。Ramp AI Index 显示，<strong>OpenAI 2 月份出现了有记录以来最大的单月份额下降（1.5%）</strong>。<br><small>来源：<a href="https://www.businessinsider.com/anthropic-may-soon-pass-openai-measure-ai-business-spending-ramp-2026-4">Business Insider</a>、<a href="https://ramp.com/leading-indicators/ai-index-march-2026">Ramp AI Index</a>、<a href="https://www.axios.com/2026/03/18/ai-enterprise-revenue-anthropic-openai">Axios</a></small></li><li><strong>OpenAI 二级市场需求降温，估值 $852B 后投资者态度分化</strong> — Bloomberg 报道，OpenAI 完成 $1220 亿融资、估值达 $8520 亿后，<strong>其在二级市场的需求正在下降，而 Anthropic 的二级市场却在升温</strong>。这反映了投资者对 OpenAI 的「全面押注」策略（消费级产品、浏览器、硬件设备）产生了疑虑。WSJ 报道 OpenAI 正考虑战略收缩，从广泛的消费级赌注转向聚焦企业市场——这恰恰是 Anthropic 正在快速蚕食的领地。<br><small>来源：<a href="https://www.bloomberg.com/news/articles/2026-04-01/openai-demand-sinks-on-secondary-market-as-anthropic-runs-hot">Bloomberg</a>、<a href="https://www.bloomberg.com/opinion/newsletters/2026-04-01/openai-is-almost-public">Bloomberg</a></small></li><li><strong>监管机构警告：AI 网络安全风险进入新纪元</strong> — Bloomberg Tech 4 月 13 日报道，<strong>美国监管机构和华尔街 CEO 正在密集讨论 AI 带来的新型网络安全威胁</strong>。这接续了上周 Anthropic Mythos 因「能力过强」限制发布的事件，以及财长 Bessent 召集华尔街 CEO 开会的背景。核心担忧：<strong>AI 模型的攻击能力和防御能力正在同时以指数级增长，现有的网络安全框架可能已经过时</strong>。Intel 加入 Musk 的 Terafab 项目（联合 Tesla、SpaceX、xAI）也在这个背景下发生——AI 算力竞赛和安全竞赛正在合流。<br><small>来源：<a href="https://www.bloomberg.com/news/videos/2026-04-13/bloomberg-tech-4-13-2026-video">Bloomberg Tech 4/13</a>、<a href="https://www.youtube.com/watch?v=zuO-R4gk5DM">Bloomberg Tech 4/10</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>Anthropic 正在赢得企业 AI 市场的「心智份额」</strong>：73% 新客户选择率意味着增量市场已经翻转</li><li><strong>OpenAI 面临战略十字路口</strong>：$852B 估值 vs 二级市场降温 vs 企业市场被蚕食，「什么都做」的策略正在被质疑</li><li><strong>AI 安全从技术问题变成金融系统性风险</strong>：华尔街 CEO 和监管机构同时行动，说明 AI 风险已经进入金融监管视野</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Ramp 的数据讲了一个比任何融资新闻都深刻的故事：在企业 AI 市场，品牌叙事比技术 benchmark 更重要——而 Anthropic 正在赢得叙事战。</strong></p><p>先看数字。30.6% vs 35.2%，差距 4.6 个百分点。如果你只看这个数字，你会觉得「还好，OpenAI 还是领先」。但 73% 的新客户选择率才是真正的 killer metric——<strong>这意味着存量市场 OpenAI 还在吃老本，但增量市场已经被 Anthropic 拿走了</strong>。按这个速度，Anthropic 在企业 AI 支出上超越 OpenAI 不是「是否」的问题，而是「Q2 还是 Q3」的问题。</p><p>为什么会这样？技术层面，Claude Code 确实好用——上期报道的 Agentic Coding 趋势报告显示 79% 的使用偏向自动化，这说明开发者真的在把 Claude Code 当「AI 工程师」用。但更深层的原因是叙事：<strong>Anthropic 2 月份拒绝五角大楼合同的决定，是一次教科书级的品牌定位</strong>。它同时向企业客户传递了三个信息：「我们有原则」「我们的 AI 足够强以至于需要谨慎部署」「选择我们 = 选择负责任的 AI」。结果？Claude 超越 ChatGPT 登上 App Store 榜首，Microsoft 公开表态支持。OpenAI 接手五角大楼合同在短期内赚了钱，长期却输了企业级信任。</p><p>OpenAI $852B 估值和二级市场降温的反差更耐人寻味。<strong>$852B 是基于「AI 将统治一切」的宏大叙事，但 Ramp 的数据显示，在最重要的企业市场，OpenAI 正在失去增量</strong>。WSJ 说 OpenAI 考虑从消费级赌注收缩到聚焦企业——但这恰恰是 Anthropic 的主场。OpenAI 的困境是：消费级产品（ChatGPT）带来了用户量但利润率低，企业级市场利润率高但正在被 Anthropic 蚕食。Sora 关停、浏览器项目进展缓慢、硬件野心未见成果——<strong>$852B 的估值需要一个比「ChatGPT 月活很高」更强的故事来支撑</strong>。</p><p>AI 网络安全风险进入监管视野这条线也在加速发展。上期报道了 Anthropic Mythos 限制发布和 Bessent 召集华尔街 CEO，本周 Bloomberg 直接用了「New Era of Cyber Risk」的标题。Intel 加入 Musk 的 Terafab 项目（联合 Tesla、SpaceX、xAI）意味着算力基础设施竞争正在从「谁有最多 GPU」变成「谁有最安全的 AI 算力」。<strong>AI 安全不再只是 AI 公司的 PR 策略——它正在成为金融监管和国家安全的核心议题</strong>。这对整个行业的影响是：安全合规成本将大幅上升，小公司更难进入企业 AI 市场，而 Anthropic「安全优先」的品牌定位将获得越来越多的制度红利。</p><p><strong>我的预判：Anthropic 将在 Q2 内超越 OpenAI 成为企业 AI 支出第一名——Ramp Q2 报告将确认这一逆转。OpenAI 的 IPO 路径将因企业市场份额下降而变得更复杂——投资人会问：如果企业市场被 Anthropic 拿走了，$852B 怎么撑得住？OpenAI 的应对将是加速发布 Spud 模型并在企业功能上大幅追赶。最大胆预测：到 Q3，美国将出现第一个针对「高能力 AI 模型」的正式监管框架草案——Anthropic Mythos 的限制发布模式将成为行业参考标准，而 Meta 的开源策略将面临新的合规压力。AI 安全不再是可选的 PR 装饰——它正在变成市场准入门槛。</strong></p></div>',
        "en": '<h3>📌 AI × Tech</h3><ul><li><strong>Anthropic Closing In on OpenAI in Enterprise AI Spending — Ramp Data Reveals Dramatic Reversal</strong> — Ramp\'s latest data shows <strong>Anthropic at 30.6% of enterprise AI spending vs OpenAI\'s 35.2% — a gap of just 4.6 points and shrinking fast</strong>. The stunning figure: <strong>73% of companies buying AI tools for the first time choose Anthropic</strong>. Claude Code drives the surge. Anthropic\'s February Pentagon contract refusal unexpectedly boosted its reputation — Claude briefly topped ChatGPT on the App Store. <strong>OpenAI saw its largest single-month share decline ever (1.5%) in February.</strong><br><small>Source: <a href="https://www.businessinsider.com/anthropic-may-soon-pass-openai-measure-ai-business-spending-ramp-2026-4">Business Insider</a>, <a href="https://ramp.com/leading-indicators/ai-index-march-2026">Ramp AI Index</a>, <a href="https://www.axios.com/2026/03/18/ai-enterprise-revenue-anthropic-openai">Axios</a></small></li><li><strong>OpenAI Secondary Market Demand Cools Post-$852B Valuation</strong> — Bloomberg reports <strong>OpenAI secondary market demand is declining while Anthropic\'s heats up</strong>. Investors question OpenAI\'s \"bet on everything\" strategy (consumer products, browsers, hardware). WSJ reports OpenAI is considering narrowing focus to enterprise — exactly where Anthropic dominates new customer acquisition.<br><small>Source: <a href="https://www.bloomberg.com/news/articles/2026-04-01/openai-demand-sinks-on-secondary-market-as-anthropic-runs-hot">Bloomberg</a></small></li><li><strong>Regulators Warn of New Era of AI Cyber Risk</strong> — Bloomberg Tech reports <strong>US regulators and Wall Street CEOs in intensive discussions on AI-driven cybersecurity threats</strong>. This follows Anthropic Mythos\'s restricted release and Treasury Secretary Bessent\'s Wall Street CEO summit. Core concern: <strong>AI offensive and defensive capabilities are growing exponentially, existing cybersecurity frameworks may be obsolete</strong>. Intel joining Musk\'s Terafab project (Tesla, SpaceX, xAI) signals the AI compute race and security race are converging.<br><small>Source: <a href="https://www.bloomberg.com/news/videos/2026-04-13/bloomberg-tech-4-13-2026-video">Bloomberg Tech 4/13</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Anthropic winning enterprise AI \"mindshare\": 73% new customer rate means the incremental market has flipped</li><li>OpenAI at a strategic crossroads: $852B valuation vs cooling secondary market vs enterprise erosion</li><li>AI safety moves from tech concern to financial systemic risk: regulators and Wall Street CEOs acting simultaneously</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Ramp\'s data tells a deeper story than any funding headline: in enterprise AI, brand narrative matters more than technical benchmarks — and Anthropic is winning the narrative war.</strong></p><p>30.6% vs 35.2% looks close, but 73% new customer acquisition rate is the killer metric — <strong>OpenAI lives on legacy adoption; Anthropic owns the growth</strong>. At this pace, the crossover is a Q2-vs-Q3 question, not an if.</p><p>Why? Claude Code is genuinely good — 79% automation-leaning usage proves developers treat it as an AI engineer. But deeper: <strong>Anthropic\'s Pentagon contract refusal was textbook brand positioning</strong>, simultaneously signaling principles, capability (\"too powerful for careless deployment\"), and responsible AI. OpenAI took the contract money; Anthropic took the trust. Claude topped ChatGPT on the App Store; Microsoft publicly backed Anthropic.</p><p>The $852B valuation vs secondary market cooling reveals OpenAI\'s dilemma: <strong>the valuation needs a story stronger than \"ChatGPT has high MAU.\"</strong> Consumer products bring volume but thin margins; enterprise brings margins but Anthropic is eating it. Sora shut down, browser stalled, hardware unrealized.</p><p><strong>Predictions: Anthropic overtakes OpenAI in enterprise spending in Q2 — Ramp\'s next report confirms the crossover. OpenAI\'s IPO path gets complicated as investors question the $852B thesis. OpenAI responds by rushing Spud and enterprise features. Boldest: by Q3, the US produces its first formal regulatory framework draft for \"high-capability AI models\" — Anthropic\'s restricted release becomes the reference standard, Meta\'s open-source faces new compliance pressure. AI safety is no longer optional PR — it\'s becoming a market entry requirement.</strong></p></div>'
    },
    "cover": imgs.get("bi") or "",
    "sources": [
        {
            "title": {"zh": "Anthropic 即将在企业 AI 支出上超越 OpenAI", "en": "Anthropic May Soon Pass OpenAI in Business AI Spending"},
            "url": "https://www.businessinsider.com/anthropic-may-soon-pass-openai-measure-ai-business-spending-ramp-2026-4",
            "image": imgs.get("bi", "")
        },
        {
            "title": {"zh": "Ramp AI Index 2026 年 3 月更新", "en": "Ramp AI Index March 2026 Update"},
            "url": "https://ramp.com/leading-indicators/ai-index-march-2026",
            "image": ""
        },
        {
            "title": {"zh": "Anthropic 在关键收入指标上逆转 OpenAI", "en": "Anthropic Turns the Tables on OpenAI in Critical Revenue Category"},
            "url": "https://www.axios.com/2026/03/18/ai-enterprise-revenue-anthropic-openai",
            "image": imgs.get("axios", "")
        },
        {
            "title": {"zh": "监管机构警告 AI 网络安全新纪元", "en": "Regulators Warn of New Era of Cyber Risk From AI"},
            "url": "https://www.bloomberg.com/news/videos/2026-04-13/bloomberg-tech-4-13-2026-video",
            "image": imgs.get("bloomberg_cyber", "")
        }
    ]
}

# Load existing issues
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

# Insert new issues at the front
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

# Write back
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("✅ issues.json updated with 2 new entries for 2026-04-14")
