# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-04-04"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=10)
        data = resp.read(100000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', data, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data, re.I)
        return html.unescape(m.group(1)) if m else ""
    except:
        return ""

# Fetch og:images
urls = {
    "malewicz": "https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627",
    "moonchild": "https://medium.com/design-bootcamp/how-moonchild-ai-generates-design-systems-you-can-actually-design-with-3e7dcbd63216",
    "figma_leaving": "https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745",
    "nyt_jobs": "https://www.nytimes.com/2026/04/03/business/economists-once-dismissed-the-ai-job-threat-but-not-anymore.html",
    "nyt_funding": "https://www.nytimes.com/2026/04/01/technology/ai-companies-fund-raising-records.html",
    "nyt_sv": "https://www.nytimes.com/2026/04/02/technology/ai-silicon-valley-tech-work.html",
    "crunchbase": "https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/",
}

print("Fetching og:images...")
images = {}
for k, u in urls.items():
    img = get_og_image(u)
    images[k] = img
    print(f"  {k}: {img[:80] if img else '(none)'}")

design_issue = {
    "date": "2026-04-04",
    "section": "design",
    "title": {
        "zh": "Malewicz 宣告「Dashboard 和 Design System 的终结」引爆设计圈 · Moonchild AI 生成可直接用于设计的 Design System · 设计师「逃离 Figma」浪潮背后：AI 正在重新定义设计工具的价值",
        "en": "Malewicz Declares 'The End of Dashboards and Design Systems' · Moonchild AI Generates Usable Design Systems · The 'Great Figma Transition': AI Redefines What Design Tools Are Worth"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul><li><strong>Michal Malewicz 万字雄文：Dashboard 和 Design System 的时代结束了——设计正在「悄悄地重新变得人性化」</strong> — 知名设计师 Michal Malewicz 在 Medium 发表的文章《The End of Dashboards and Design Systems》获得 6500+ 点赞和 265 条评论，在设计社区引发了本周最大规模的讨论。核心论点：<strong>AI 让传统 Dashboard 变得多余——当用户可以直接用自然语言询问数据，为什么还需要一堆图表？</strong>更大胆的是，他认为 Design System 作为「组件库 + 规范文档」的形态也在消亡——因为 AI 可以在运行时动态生成符合品牌规范的界面，不再需要人类预先定义每一个组件。Malewicz 的结论：设计正在从「制造像素」回归到「理解人」，<strong>interface 的未来是对话式的、个性化的、动态生成的</strong>。<br><small>来源：<a href="https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627">Michal Malewicz (Medium)</a></small></li><li><strong>Moonchild AI：第一个能生成「可直接设计用」的 Design System 的 AI 工具</strong> — Design Bootcamp 对 Moonchild AI 的深度评测引发关注。与之前的 AI 设计工具不同，Moonchild 不是生成单个页面或组件，而是<strong>生成完整的 Design System——包括色板、字体系统、间距规则、组件库——并且可以直接在 Figma 中使用</strong>。这和上期日报讨论的「Design System 是 AI 时代新基础设施」形成了有趣的对照：Malewicz 说 Design System 要死了，Moonchild 却在用 AI 生成更好的 Design System。谁对？也许两者都对——<strong>人类手动维护的 Design System 在消亡，AI 动态生成的 Design System 在崛起。</strong><br><small>来源：<a href="https://medium.com/design-bootcamp/how-moonchild-ai-generates-design-systems-you-can-actually-design-with-3e7dcbd63216">Design Bootcamp (Medium)</a></small></li><li><strong>「设计师逃离 Figma」：The Great Transition 背后的真实动因</strong> — Bootcamp 的一篇文章（2600+ 赞，116 条评论）深入分析了设计师离开 Figma 的趋势。核心原因不是 Figma 变差了，而是<strong>设计工作本身变了</strong>：当 AI 可以直接生成代码和界面，Figma 作为「视觉设计稿制作工具」的核心价值主张正在被削弱。部分设计师转向 Cursor + Claude 直接生产前端代码，部分转向 Framer 这样的「设计即发布」平台。<strong>Figma 的回应是 Figma Make——试图从「设计工具」转型为「AI 设计平台」。</strong>但问题是：如果设计师已经可以用自然语言直接生成产品，还需要在 Figma 里「画」吗？<br><small>来源：<a href="https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745">Bootcamp (Medium)</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>Dashboard → 对话</strong>：数据可视化的主要交互方式正在从「看图」变成「问答」</li><li><strong>Design System 的悖论</strong>：人工维护的在消亡，AI 生成的在崛起</li><li><strong>设计工具的身份危机</strong>：Figma、Sketch 的核心价值——「像素级设计稿」——正在被 AI 绕过</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Malewicz 的文章之所以引爆了设计圈，不是因为他说了什么新鲜事——而是因为他说出了很多设计师心里有但不敢说的话：我们花了十年时间精心打磨 Design System、建造完美的 Dashboard、在 Figma 里推像素……然后 AI 来了，说「这些我都能自动生成，而且可能比你做得更快」。</strong></p><p>但 Malewicz 真正精彩的洞察不是「XX 要死了」这种标题党——是他后面那句「设计正在悄悄地重新变得人性化」。想想看：过去五年，设计行业最热门的技能是什么？Design System 管理、组件规范化、Design Token、像素级还原。这些本质上都是<strong>机械性工作</strong>——把人变成组件流水线上的工人。AI 接管这些工作，反而是一种解放：<strong>设计师终于可以回到设计的本质——理解人、洞察需求、定义问题——而不是在 Figma 里复制粘贴组件。</strong></p><p>Moonchild AI 的出现完美验证了这个趋势。它不是在帮设计师「更快地画 UI」——它是在帮设计师「跳过画 UI 这个步骤」。当 AI 可以在 5 分钟内生成一套完整的 Design System，你作为设计师的价值到底在哪里？答案很清楚：<strong>在审美判断上，在品牌理解上，在知道什么「感觉对」上。</strong>这些是 AI 目前最弱的地方，也是设计师最应该发力的地方。</p><p>「设计师逃离 Figma」这件事最值得关注的不是逃离本身——而是他们逃向了哪里。答案是：<strong>Cursor、Claude Code、Framer——都是「直接生产」的工具，而不是「制作中间产物」的工具。</strong>这和上期我们讨论的 Vibe Coding 趋势完全一致：设计师不想再做设计稿然后交给开发还原，他们想直接生产最终产品。Figma Make 是 Figma 对这个趋势的回应，但坦白说，我对它持谨慎态度。Figma 的 DNA 是「协作设计工具」——它的整个架构和交互范式都围绕「多人在画布上操作像素」。要转型成「AI 设计平台」，需要的不是在现有产品上加 AI 功能，而是从底层重新思考「设计」的定义。</p><p><strong>我的预测：2026 年底之前，设计行业会出现一个清晰的分层——「AI 设计师」和「人类设计师」不是两种人，而是同一个人的两种工作模式。80% 的时间用 AI 工具快速生产（Cursor、Moonchild、Figma Make），20% 的时间做 AI 做不好的事情：用户研究、概念探索、审美决策、创意方向。那些只会「在 Figma 里画 UI」的设计师，日子会越来越难过；但那些能「定义什么值得画」的设计师，会比以往更有价值。Malewicz 说得对：设计正在回归人性化。讽刺的是，这要感谢 AI。</strong></p></div>',
        "en": '<h3>📌 AI × Design</h3><ul><li><strong>Michal Malewicz: The End of Dashboards and Design Systems — Design Is "Quietly Becoming Human Again"</strong> — Malewicz\'s article (6.5K+ claps, 265 comments) sparked the biggest design community debate this week. Core argument: <strong>AI makes traditional dashboards redundant—why browse charts when you can ask questions in natural language?</strong> More boldly: design systems as "component libraries + spec docs" are dying because AI can dynamically generate brand-compliant interfaces at runtime. His conclusion: design is returning from "manufacturing pixels" to "understanding people."<br><small>Source: <a href="https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627">Michal Malewicz (Medium)</a></small></li><li><strong>Moonchild AI: First Tool That Generates Usable Design Systems</strong> — Unlike previous AI design tools that generate single pages, Moonchild generates complete design systems—palettes, type scales, spacing rules, component libraries—directly usable in Figma. <strong>Interesting paradox with Malewicz\'s thesis: human-maintained design systems are dying; AI-generated ones are rising.</strong><br><small>Source: <a href="https://medium.com/design-bootcamp/how-moonchild-ai-generates-design-systems-you-can-actually-design-with-3e7dcbd63216">Design Bootcamp (Medium)</a></small></li><li><strong>"Designers Leaving Figma": The Great Transition</strong> — Bootcamp analysis (2.6K+ claps) explores why designers are migrating away: <strong>it\'s not that Figma got worse—it\'s that design work itself changed.</strong> When AI generates code and interfaces directly, Figma\'s value proposition as a "visual mockup tool" weakens. Designers are moving to Cursor + Claude for direct frontend production, or Framer for "design = publish." Figma\'s response: Figma Make. The question: if you can describe products in natural language, why "draw" in Figma?<br><small>Source: <a href="https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745">Bootcamp (Medium)</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Dashboard → Conversation: data visualization shifting from "viewing charts" to "asking questions"</li><li>Design System Paradox: manually maintained ones dying, AI-generated ones rising</li><li>Design tool identity crisis: core value of pixel-perfect mockups being bypassed by AI</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Malewicz\'s article exploded because he said what designers think but fear to say: we spent a decade perfecting design systems, building dashboards, pushing pixels in Figma—then AI arrived and said "I can auto-generate all of that, probably faster."</strong> But his real insight isn\'t "X is dead"—it\'s "design is quietly becoming human again." For five years, the hottest design skills were design system management, component specs, design tokens, pixel-perfect implementation—essentially mechanical work. AI taking over these tasks is liberation: designers can finally return to design\'s essence—understanding people, insight, problem-definition—instead of copy-pasting components. Moonchild AI validates this perfectly: it doesn\'t help designers "draw UI faster"—it helps them skip drawing entirely. When AI generates a complete design system in 5 minutes, your value is in aesthetic judgment, brand understanding, and knowing what "feels right"—AI\'s weakest areas. The "Figma exodus" is telling not because designers are leaving, but where they\'re going: Cursor, Claude Code, Framer—"direct production" tools, not "intermediate artifact" tools. This aligns perfectly with the vibe coding trend. <strong>My prediction: by end of 2026, a clear split emerges—80% of design time using AI for rapid production, 20% doing what AI can\'t: user research, concept exploration, aesthetic decisions, creative direction. Designers who can only "draw UI in Figma" will struggle; those who can "define what\'s worth building" will be more valuable than ever. Malewicz is right: design is becoming human again. Ironically, thanks to AI.</strong></p></div>'
    },
    "cover": images.get("malewicz", ""),
    "sources": [
        {
            "title": {"zh": "Dashboard 和 Design System 的终结", "en": "The End of Dashboards and Design Systems"},
            "url": "https://michalmalewicz.medium.com/the-end-of-dashboards-and-design-systems-5d98ec9de627",
            "image": images.get("malewicz", "")
        },
        {
            "title": {"zh": "Moonchild AI 如何生成可用的 Design System", "en": "How Moonchild AI Generates Design Systems You Can Design With"},
            "url": "https://medium.com/design-bootcamp/how-moonchild-ai-generates-design-systems-you-can-actually-design-with-3e7dcbd63216",
            "image": images.get("moonchild", "")
        },
        {
            "title": {"zh": "设计师为什么在离开 Figma", "en": "Why Are Designers Leaving Figma: The Great Transition"},
            "url": "https://medium.com/design-bootcamp/why-are-designers-leaving-figma-the-great-transition-1a63d8b03745",
            "image": images.get("figma_leaving", "")
        }
    ]
}

tech_issue = {
    "date": "2026-04-04",
    "section": "tech",
    "title": {
        "zh": "NYT 深度报道：经济学家不再否认 AI 就业威胁 · Q1 2026 AI 融资 2970 亿美元粉碎历史记录 · 硅谷自己也在被 AI 改变：年轻毕业生失业率攀升，但华尔街奖金创新高",
        "en": "NYT: Economists No Longer Dismiss the AI Job Threat · Q1 2026 AI Funding Hits $297B, Shattering Records · Silicon Valley Is Being Changed by AI Too: Youth Unemployment Rises While Wall Street Bonuses Hit Records"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul><li><strong>NYT 重磅：经济学家不再否认 AI 就业威胁——从「AI 洗白」到「真的在发生」</strong> — 纽约时报 4 月 3 日发表的深度报道引发广泛讨论。此前，经济学界的主流共识是「AI 取代工作」只是炒作——年轻毕业生失业率上升可以归因于经济周期，公司以 AI 为由裁员是「AI-washing」。<strong>但现在，越来越多的经济学家开始改变立场。</strong>关键转折点：当 Block 裁员 4000 人（上期日报报道）、Atlassian 裁员 1600 人并明确「citing AI shift」时，「AI-washing」这个解释开始显得苍白。文章引用多位顶级经济学家的观点，核心共识正在从「不用担心」转向「需要认真对待」。<br><small>来源：<a href="https://www.nytimes.com/2026/04/03/business/economists-once-dismissed-the-ai-job-threat-but-not-anymore.html">New York Times</a></small></li><li><strong>Q1 2026 AI 融资粉碎一切记录：2970 亿美元，OpenAI 独占 1220 亿</strong> — 据 Crunchbase 数据，2026 年第一季度全球 AI 公司融资总额达到 2970 亿美元。头部集中度惊人：OpenAI 1220 亿美元（总融资已达史上最高）、Anthropic 300 亿美元（估值 3800 亿）、xAI 200 亿美元、Waymo 160 亿美元。新面孔也不甘示弱：Yann LeCun 的 AMI 拿下 10.3 亿美元种子轮（欧洲最大种子轮记录），李飞飞的 World Labs 融资 10 亿美元。<strong>仅基础模型公司的融资（889 亿美元）就已经超过了 2025 年全年。</strong>早期阶段融资增长 40%，种子轮增长 30%——AI 泡沫？也许。但资本在用真金白银投票。<br><small>来源：<a href="https://www.nytimes.com/2026/04/01/technology/ai-companies-fund-raising-records.html">New York Times</a>、<a href="https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/">Crunchbase</a>、<a href="https://smartchunks.com/openai-anthropic-foundational-ai-funding-q1-2026/">SmartChunks</a></small></li><li><strong>NYT：AI 先改变了硅谷自己——年轻毕业生遭殃，但华尔街奖金创新高</strong> — 4 月 2 日的另一篇 NYT 报道描绘了一幅矛盾的画面：硅谷曾经预言 AI 会取代放射科医生、律师、银行家——但最先被改变的是硅谷自己。<strong>年轻技术工作者的失业率正在攀升</strong>，但总体就业数据变化不大。更讽刺的是，华尔街奖金正在创历史新高——帮 AI 公司做融资的银行家赚得盆满钵满，而 AI 本来应该「取代」的就是这些人。<strong>结论：AI 目前最大的经济影响不是「取代所有人」，而是「重新分配谁赚钱」。</strong><br><small>来源：<a href="https://www.nytimes.com/2026/04/02/technology/ai-silicon-valley-tech-work.html">New York Times</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>经济学界共识转变</strong>：从「AI 取代工作是炒作」到「我们需要认真对待」——转折点可能就在 2026 年 Q1</li><li><strong>AI 融资的「赢家通吃」格局</strong>：前四名占了 2970 亿中的 1900 亿（64%），集中度空前</li><li><strong>AI 的讽刺效应</strong>：目前最大的受益者恰恰是 AI 本应取代的人（投行、律师、咨询师）</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>今天这三篇 NYT 报道如果放在一起看，你会看到一个绝妙的讽刺：AI 公司在 Q1 融了 2970 亿美元，创造了史上最大的资本狂欢；同时，经济学家终于承认 AI 正在威胁就业；而最讽刺的是，这波融资本身创造的最大赢家是华尔街银行家——AI 本来应该「取代」的白领精英。</strong></p><p>先拆解融资数据。2970 亿美元是什么概念？这比 2024 年全球 VC 在所有行业的总融资额还多。仅 OpenAI 一家的 1220 亿美元就超过了多数国家的年度军费预算。但真正让我警觉的不是总量——是集中度。前四家公司（OpenAI、Anthropic、xAI、Waymo）拿走了 64% 的资金。<strong>这不是「AI 行业在增长」，这是「4 家公司在吞噬所有资本」。</strong>历史上这种极端集中的融资格局通常意味着两件事之一：要么这些公司真的在建造下一个操作系统级别的基础设施，要么我们正在见证 2000 年互联网泡沫级别的资本错配。也许两者兼有。</p><p>NYT 的就业威胁报道最有价值的细节是「AI-washing」这个概念的消亡。六个月前，当 Block 裁员时，经济学家还可以说「这是管理层拿 AI 当借口」。但当 Atlassian 也裁了 1600 人并明确说是 AI 导致的，当年轻毕业生的就业数据持续恶化，「AI-washing」这个解释的说服力就消失了。<strong>经济学界的共识转变是一个滞后指标——他们承认问题时，问题通常已经存在一段时间了。</strong>但他们的立场变化会影响政策制定者，进而可能推动就业保护立法。我预测：2026 年下半年，至少一个主要经济体会出台针对 AI 驱动裁员的监管措施——可能是强制性的「AI 影响评估」或者裁员缓冲期。</p><p>最讽刺的故事是第三条：华尔街奖金创新高。帮 AI 公司做 IPO 准备、融资结构设计、估值建模的投行团队赚得最多——<strong>而 AI 原本最先应该取代的知识工作者就是这些人。</strong>这不是巧合，这是 AI 颠覆的典型路径：在真正取代一个行业之前，先让这个行业因为「AI 概念」而短暂繁荣。2000 年泡沫前，最赚钱的也是帮互联网公司做 IPO 的投行。当 OpenAI 或 Anthropic 真正 IPO 的那天，可能也是华尔街 AI 红利的巅峰。</p><p><strong>把今天的设计新闻和科技新闻连起来看，一个共同主题浮现：AI 正在消灭「中间层」。在设计领域，中间层是「按规范做执行」的初中级设计师；在企业管理领域，中间层是上期 Dorsey 说的中层管理者；在经济领域，中间层是年轻的知识工作者入门岗位。AI 不是在消灭所有工作——它在消灭那些「按照规则处理信息」的工作。如果你的工作核心是「接收规范 → 执行 → 交付」，不管你是设计师、项目经理还是初级分析师，你都在 AI 的射程之内。如果你的工作核心是「定义规范」或者「判断规范是否正确」——你反而在升值。2970 亿美元的赌注说明资本认为这个趋势是真的。经济学家也终于同意了。</strong></p></div>',
        "en": '<h3>📌 AI × Tech</h3><ul><li><strong>NYT: Economists No Longer Dismiss the AI Job Threat</strong> — The NYT\'s April 3 deep-dive sparked widespread debate. The prior consensus—AI job displacement was hype, companies were "AI-washing" layoffs—is crumbling. <strong>When Block cuts 4,000 and Atlassian cuts 1,600 explicitly "citing AI shift," the AI-washing explanation falls apart.</strong> Multiple top economists are now shifting from "don\'t worry" to "take this seriously."<br><small>Source: <a href="https://www.nytimes.com/2026/04/03/business/economists-once-dismissed-the-ai-job-threat-but-not-anymore.html">New York Times</a></small></li><li><strong>Q1 2026 AI Funding Shatters All Records: $297B, OpenAI Takes $122B</strong> — Per Crunchbase: OpenAI $122B (most capitalized private company ever), Anthropic $30B ($380B valuation), xAI $20B, Waymo $16B. New entrants: Yann LeCun\'s AMI ($1.03B seed—Europe\'s largest ever), Fei-Fei Li\'s World Labs ($1B). <strong>Foundational AI funding alone ($88.9B) exceeded all of 2025.</strong> Early-stage up 40%, seed up 30%.<br><small>Source: <a href="https://www.nytimes.com/2026/04/01/technology/ai-companies-fund-raising-records.html">New York Times</a>, <a href="https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/">Crunchbase</a></small></li><li><strong>NYT: AI Changed Silicon Valley First—Youth Unemployment Rises, But Wall Street Bonuses Hit Records</strong> — AI was supposed to replace radiologists, lawyers, bankers—instead it\'s disrupting Silicon Valley\'s own young workforce first. <strong>Youth tech unemployment rising, while Wall Street bonuses (from AI company deals) hit all-time highs.</strong> AI\'s biggest economic impact isn\'t "replacing everyone"—it\'s redistributing who profits.<br><small>Source: <a href="https://www.nytimes.com/2026/04/02/technology/ai-silicon-valley-tech-work.html">New York Times</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Economist consensus shift: from "AI job threat is hype" to "we need to take this seriously"—tipping point may be Q1 2026</li><li>AI funding\'s winner-take-all: top 4 companies took 64% of $297B</li><li>AI\'s ironic effect: biggest current beneficiaries are the white-collar elites AI was supposed to replace (bankers, consultants)</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Three NYT reports together paint a brilliant irony: AI companies raised $297B in Q1 creating history\'s largest capital frenzy; economists finally admit AI threatens jobs; and the biggest winners from this funding wave are Wall Street bankers—the exact white-collar elite AI was supposed to replace.</strong> The concentration is alarming: four companies took 64% of all funding. This isn\'t "AI industry growing"—it\'s "4 companies consuming all capital." History shows such extreme concentration means either these companies are building the next OS-level infrastructure, or we\'re witnessing dot-com-level capital misallocation. Perhaps both. The economist consensus shift is a lagging indicator—by the time they acknowledge the problem, it\'s been happening. But their stance change will influence policymakers. I predict: H2 2026, at least one major economy will introduce AI-driven layoff regulations. The Wall Street irony is textbook: before disrupting an industry, AI first creates a boom from the "AI concept" itself. In 2000, the most profitable firms were those doing internet IPOs. <strong>Connecting today\'s design and tech news reveals a common theme: AI is eliminating the "middle layer"—junior designers executing specs, middle managers routing information, entry-level knowledge workers. If your core job is "receive rules → execute → deliver," you\'re in AI\'s crosshairs regardless of title. If your job is "define the rules" or "judge whether rules are right"—you\'re appreciating. $297B in bets says capital believes this. Economists finally agree.</strong></p></div>'
    },
    "cover": images.get("nyt_funding", "") or images.get("nyt_jobs", ""),
    "sources": [
        {
            "title": {"zh": "经济学家不再否认 AI 就业威胁", "en": "Economists Once Dismissed the A.I. Job Threat, but Not Anymore"},
            "url": "https://www.nytimes.com/2026/04/03/business/economists-once-dismissed-the-ai-job-threat-but-not-anymore.html",
            "image": images.get("nyt_jobs", "")
        },
        {
            "title": {"zh": "AI 公司 Q1 融资粉碎记录", "en": "A.I. Companies Shatter Fund-Raising Records"},
            "url": "https://www.nytimes.com/2026/04/01/technology/ai-companies-fund-raising-records.html",
            "image": images.get("nyt_funding", "")
        },
        {
            "title": {"zh": "AI 先改变了硅谷自己", "en": "A.I. Could Change the World. But First It Is Changing Silicon Valley"},
            "url": "https://www.nytimes.com/2026/04/02/technology/ai-silicon-valley-tech-work.html",
            "image": images.get("nyt_sv", "")
        }
    ]
}

# Load existing issues and prepend new ones
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Added 2 issues (design + tech) for 2026-04-04. Total issues: {len(issues)}")
