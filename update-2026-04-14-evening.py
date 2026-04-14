#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rex Daily evening update for 2026-04-14"""
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
urls = {
    "flowstep": "https://flowstep.ai/blog/best-ai-ui-design-tools/",
    "wdi": "https://www.webdesign-inspiration.com/article/7-ai-tools-that-are-actually-changing-ui-ux-design-in-2026/",
    "startupstash": "https://blog.startupstash.com/8-best-ai-tools-for-designers-in-2026-tested-and-compared-8b9f0c30fd0d",
    "fortune": "https://fortune.com/2026/04/07/spacex-openai-anthropic-reopen-ipo-market-crunchbase/",
    "msn_anthropic": "https://www.msn.com/en-us/money/markets/anthropic-tops-openai-on-revenue-with-30b-run-rate-while-spacex-plans-june-investor-roadshow-ahead-of-mega-ipos/ar-AA20k7gA",
    "airstreet": "https://press.airstreet.com/p/state-of-ai-april-2026-newsletter",
}

print("Fetching og:images...")
images = {}
for k, u in urls.items():
    img = get_og_image(u)
    images[k] = img
    print(f"  {k}: {img[:80] if img else '(none)'}")

# Build new issues
design_issue = {
    "date": "2026-04-14",
    "section": "design",
    "title": {
        "zh": "Flowstep 崛起挑战 Figma Make：AI 设计工具进入「堆栈时代」· 7 款工具各有定位 · 设计师的新核心能力是工具编排",
        "en": "Flowstep Rises to Challenge Figma Make: AI Design Tools Enter the 'Stack Era' · 7 Tools Find Their Niches · Tool Orchestration Becomes the Designer's Core Skill"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计（晚间更新）</h3><ul><li><strong>Flowstep 强势崛起：从文本到可编辑 UI 只需几秒，直接挑战 Figma Make</strong> — Flowstep 在多个 2026 AI 设计工具横评中位列前三。其核心卖点是<strong>无限画布上从文本/PRD 直接生成可编辑 UI，支持 Figma 复制粘贴和代码导出</strong>。StartupStash 的实测比较显示，Flowstep 在速度和可编辑性上与 Figma Make 各有胜负——Flowstep 更快更灵活，Figma Make 胜在品牌一致性和生态整合。值得注意的是，Flowstep 使用 Anthropic 的 AI 模型优化代码生成，<strong>这意味着 Anthropic 的影响力正在从开发工具（Claude Code）扩展到设计工具基础设施</strong>。定价 $15/月起，对比 Figma Make 的 $20/月，价格战已经开始。<br><small>来源：<a href=\"https://flowstep.ai/blog/best-ai-ui-design-tools/\">Flowstep Blog</a>、<a href=\"https://blog.startupstash.com/8-best-ai-tools-for-designers-in-2026-tested-and-compared-8b9f0c30fd0d\">StartupStash</a></small></li><li><strong>「7 款真正在改变 UI/UX 设计的 AI 工具」——从单一工具到工具矩阵的转变已成共识</strong> — Web Design Inspiration 的深度评测覆盖 Flowstep、Figma AI、Adobe Firefly、Khroma、Relume、Jasper 和 Maze。关键洞察：<strong>这些工具不是在竞争同一个市场，而是各自占据设计工作流的不同环节</strong>——Flowstep/Figma Make 做 UI 生成、Firefly 做视觉资产、Khroma 做配色、Relume 做信息架构、Jasper 做 UX 文案、Maze 做用户测试。文章明确指出：<strong>「Building a Stack That Works Together」是 2026 设计师的核心命题</strong>。<br><small>来源：<a href=\"https://www.webdesign-inspiration.com/article/7-ai-tools-that-are-actually-changing-ui-ux-design-in-2026/\">Web Design Inspiration</a></small></li><li><strong>UX Design Institute：AI 不是取代 UX 研究，而是让研究从原型到验证更快闭环</strong> — UX Design Institute 2026 年度工具报告重点推荐 Maze（AI 辅助用户测试）和 Contentsquare（AI 行为分析），指出 AI 在 UX 领域的最大价值不是生成界面，而是<strong>加速「设计→测试→洞察」的反馈循环</strong>。Maze 的 AI 功能能从原型直接生成测试方案并分析用户行为数据，把传统需要 1-2 周的用户测试压缩到几天。<br><small>来源：<a href=\"https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/\">UX Design Institute</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 设计工具的竞争格局从「谁最好」变成「谁在栈里占据最关键位置」</strong></li><li><strong>Anthropic 的 AI 基础设施正在渗透设计工具层</strong>：Flowstep 用 Claude 做代码生成，这是 Anthropic B2B 生态的新扩展</li><li><strong>UX 研究 AI 化是下一个爆发点</strong>：Maze + Contentsquare 正在重新定义用户测试的速度和成本</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天早上我说「单一工具时代结束了」，晚间的新闻完美印证了这一点——但我想把这个判断推得更远。</strong></p><p>Flowstep 的崛起是一个信号，但不是你想的那种信号。大多数人看到 Flowstep vs Figma Make 会想「又一个竞争者」，但真正的故事是：<strong>Flowstep 底层用的是 Anthropic 的模型来生成代码</strong>。这意味着什么？Anthropic 正在悄悄成为 AI 设计工具的「Intel Inside」——你用的工具前端是 Flowstep、Banani 还是别的什么，底层的智能引擎越来越多地来自 Claude。今天早上的报告里我提到 Anthropic 在企业 AI 支出上即将超越 OpenAI，而现在我们看到这种优势正在从开发者工具（Claude Code）延伸到设计工具基础设施。<strong>如果 Anthropic 能同时成为「开发者首选 AI」和「设计工具首选底层模型」，它的护城河将比任何单一产品都深。</strong></p><p>Web Design Inspiration 那篇文章的标题用了「Actually Changing」——这个措辞很有意思，暗示市场上大部分 AI 设计工具是噪音。它选出的 7 款工具恰好覆盖了设计工作流的完整环节：<strong>信息架构（Relume）→ UI 生成（Flowstep/Figma AI）→ 视觉资产（Firefly）→ 配色（Khroma）→ 文案（Jasper）→ 用户测试（Maze）</strong>。把它们连起来看，你会发现一个惊人的现实：<strong>2026 年的设计师不再是「用 Figma 的人」，而是「编排 6-7 个 AI 工具的人」</strong>。这就像 2015 年的开发者从「会写代码」变成「会用 Git + Docker + CI/CD + 云服务的人」一样——<strong>工具编排能力（tool orchestration）正在取代传统的设计执行力，成为设计师的核心竞争力</strong>。</p><p>UX 研究这条线值得特别关注。Maze 做的事情看起来不够性感——不是生成漂亮 UI，而是加速用户测试——但我认为<strong>这才是 AI 在设计领域最具颠覆性的应用</strong>。为什么？因为 UI 生成只是把执行成本降低了，而用户测试 AI 化把<strong>决策反馈循环压缩了一个数量级</strong>。以前做一轮用户测试需要 1-2 周（招募→测试→分析），现在 Maze 能在几天内完成全部流程。这意味着设计团队可以从「一个季度做 2-3 轮用户测试」变成「一个月做 8-10 轮微测试」。当测试成本趋近于零时，<strong>设计流程本身会发生结构性变化——从「先设计再验证」变成「边设计边验证」，设计和研究的边界将彻底模糊</strong>。</p><p><strong>综合早间和晚间的内容，我今天最核心的判断是：2026 年 Q2 将是 AI 设计工具从「单品竞争」转向「生态位竞争」的转折点。赢家不是功能最多的工具，而是在工具栈中占据最不可替代位置的工具。Figma 的不可替代性在协作和交付、Flowstep 的在速度和灵活性、Maze 的在验证闭环。而 Anthropic 正在成为这个工具栈的隐形基础设施层——这可能是比任何单一设计工具都重要的战略位置。</strong></p></div>",
        "en": "<h3>📌 AI × Design (Evening Update)</h3><ul><li><strong>Flowstep Rises as a Serious Figma Make Challenger: Text-to-Editable UI in Seconds</strong> — Flowstep ranks in the top 3 across multiple 2026 AI design tool reviews. Core proposition: <strong>generate editable UI from text/PRDs on an infinite canvas with Figma copy-paste and code export</strong>. StartupStash testing shows Flowstep wins on speed and flexibility; Figma Make wins on brand consistency and ecosystem. Notably, Flowstep uses Anthropic's AI model for code generation — <strong>Anthropic's influence extends from dev tools (Claude Code) into design tool infrastructure</strong>. At $15/mo vs Figma Make's $20/mo, the price war has begun.<br><small>Source: <a href=\"https://flowstep.ai/blog/best-ai-ui-design-tools/\">Flowstep Blog</a>, <a href=\"https://blog.startupstash.com/8-best-ai-tools-for-designers-in-2026-tested-and-compared-8b9f0c30fd0d\">StartupStash</a></small></li><li><strong>'7 AI Tools Actually Changing UI/UX Design' — The Tool Stack Thesis Goes Mainstream</strong> — Web Design Inspiration's review covers Flowstep, Figma AI, Adobe Firefly, Khroma, Relume, Jasper, and Maze. Key insight: <strong>these tools don't compete in one market — they each own a different stage of the design workflow</strong>. The article explicitly states: <strong>'Building a Stack That Works Together' is the 2026 designer's core challenge.</strong><br><small>Source: <a href=\"https://www.webdesign-inspiration.com/article/7-ai-tools-that-are-actually-changing-ui-ux-design-in-2026/\">Web Design Inspiration</a></small></li><li><strong>UX Design Institute: AI's Biggest Design Value Is Accelerating the Research Feedback Loop</strong> — The 2026 tool report highlights Maze (AI-assisted user testing) and Contentsquare (AI behavioral analytics), arguing AI's biggest UX value isn't generating interfaces but <strong>compressing the design→test→insight feedback loop</strong> from weeks to days.<br><small>Source: <a href=\"https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/\">UX Design Institute</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI design tool competition shifts from 'who's best' to 'who holds the most critical stack position'</li><li>Anthropic's AI infrastructure penetrates the design tool layer via Flowstep</li><li>UX research AI is the next breakout: Maze + Contentsquare redefine testing speed and cost</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>This morning I said 'the single-tool era is over.' Tonight's news proves it — but I want to push this further.</strong></p><p>Flowstep's rise isn't just 'another competitor.' The real story: <strong>Flowstep runs on Anthropic's model for code generation</strong>. Anthropic is quietly becoming the 'Intel Inside' of AI design tools. Combined with this morning's enterprise spending data, Anthropic's advantage is extending from developer tools (Claude Code) into design tool infrastructure. <strong>If Anthropic becomes both 'developer's preferred AI' and 'design tool's preferred foundation model,' its moat deepens beyond any single product.</strong></p><p>The 7-tool review reveals something striking: connect the dots and you see a complete workflow — <strong>IA (Relume) → UI generation (Flowstep/Figma AI) → visual assets (Firefly) → color (Khroma) → copy (Jasper) → user testing (Maze)</strong>. The 2026 designer isn't 'a Figma user' but 'an orchestrator of 6-7 AI tools.' <strong>Tool orchestration is replacing design execution as the designer's core competency</strong> — just as developers shifted from 'writing code' to 'managing Git + Docker + CI/CD + cloud.'</p><p>The UX research angle deserves special attention. Maze's work isn't glamorous — it's not generating beautiful UIs — but <strong>it may be AI's most disruptive design application</strong>. UI generation reduces execution cost; AI-powered testing compresses the <strong>decision feedback loop by an order of magnitude</strong>. When testing costs approach zero, design itself structurally changes — from 'design then validate' to 'design while validating.'</p><p><strong>Today's core thesis: Q2 2026 marks the shift from single-product competition to ecosystem-position competition in AI design tools. Winners aren't the most feature-rich but the most irreplaceable in the stack. Figma's irreplaceability is collaboration/delivery; Flowstep's is speed/flexibility; Maze's is the validation loop. And Anthropic is becoming the invisible infrastructure layer — potentially the most strategic position of all.</strong></p></div>"
    },
    "cover": images.get("flowstep") or images.get("wdi") or "https://www.webdesign-inspiration.com/article/wp-content/uploads/2026/04/czr2sgaxy3q.jpg",
    "sources": [
        {
            "title": {"zh": "7 款最佳 AI UI 设计工具：2026 对比", "en": "7 Best AI UI Design Tools: 2026 Comparison"},
            "url": "https://flowstep.ai/blog/best-ai-ui-design-tools/",
            "image": images.get("flowstep", "")
        },
        {
            "title": {"zh": "2026 年 8 款最佳设计师 AI 工具实测对比", "en": "8 Best AI Tools For Designers in 2026, Tested And Compared"},
            "url": "https://blog.startupstash.com/8-best-ai-tools-for-designers-in-2026-tested-and-compared-8b9f0c30fd0d",
            "image": images.get("startupstash", "")
        },
        {
            "title": {"zh": "7 款真正在改变 UI/UX 设计的 AI 工具", "en": "7 AI Tools That Are Actually Changing UI/UX Design in 2026"},
            "url": "https://www.webdesign-inspiration.com/article/7-ai-tools-that-are-actually-changing-ui-ux-design-in-2026/",
            "image": images.get("wdi", "")
        },
        {
            "title": {"zh": "2026 年 UX 设计 9 大 AI 工具", "en": "The Top 9 AI Tools for UX Design in 2026"},
            "url": "https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-04-14",
    "section": "tech",
    "title": {
        "zh": "Anthropic 年化收入突破 $300 亿超越 OpenAI · SpaceX 6 月路演拉开 AI 超级 IPO 序幕 · Q1 全球 AI 风投 $3000 亿创历史纪录",
        "en": "Anthropic ARR Surges Past $30B Overtaking OpenAI · SpaceX June Roadshow Opens AI Mega-IPO Season · Q1 Global AI VC Hits Record $300B"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技（晚间更新）</h3><ul><li><strong>Anthropic 年化收入突破 $300 亿，超越 OpenAI——All-In Podcast 深度解读</strong> — 据 MSN/Bloomberg 报道，<strong>Anthropic 的年化收入率已突破 $300 亿，较去年的 $90 亿增长超 3 倍，正式超越 OpenAI</strong>。All-In Podcast 最新一期（标题：「Anthropic's $30B Ramp」）深度讨论了这一里程碑。这与今天早间报道的 Ramp 企业支出数据形成完美闭环：<strong>Anthropic 不仅在企业份额上追平 OpenAI（30.6% vs 35.2%），其绝对收入规模也已经反超</strong>。驱动力来自三方面：Claude Code 的企业级采用爆发、Anthropic API 成为 AI 应用基础设施（如 Flowstep 等设计工具的底层引擎）、以及安全优先品牌定位带来的企业信任溢价。<br><small>来源：<a href=\"https://www.msn.com/en-us/money/markets/anthropic-tops-openai-on-revenue-with-30b-run-rate-while-spacex-plans-june-investor-roadshow-ahead-of-mega-ipos/ar-AA20k7gA\">MSN/Bloomberg</a>、<a href=\"https://www.youtube.com/watch?v=DVBJQQCjgXU\">All-In Podcast</a></small></li><li><strong>SpaceX 秘密 IPO 备案引爆 AI 超级 IPO 预期——OpenAI、Anthropic 紧随其后</strong> — Fortune/Bloomberg 报道，<strong>SpaceX 已秘密提交 IPO 备案，计划 6 月进行投资者路演</strong>。市场预期这将拉开「AI 超级 IPO 年」的序幕——OpenAI（$852B 估值）和 Anthropic 均在考虑上市。EY 数据显示 2025 年全球 IPO 总融资已增长 39%，2026 管线更乐观。关键背景：<strong>Anthropic 以 $300 亿 ARR 超越 OpenAI 的消息在 IPO 窗口打开前释出，时机耐人寻味——这可能是 Anthropic IPO 叙事的预热</strong>。<br><small>来源：<a href=\"https://fortune.com/2026/04/07/spacex-openai-anthropic-reopen-ipo-market-crunchbase/\">Fortune</a>、<a href=\"https://www.bloomberg.com/news/newsletters/2026-04-02/spacex-s-record-listing-could-lead-to-a-year-of-big-ai-ipos\">Bloomberg</a></small></li><li><strong>Q1 2026 全球 AI 风投创纪录：$3000 亿涌入 6000 家初创公司</strong> — Crunchbase 最新数据显示，<strong>2026 年 Q1 全球投资者向约 6000 家初创公司投入了约 $3000 亿，同比和环比均增长超过 150%</strong>。这不是正常增长，这是资本狂潮。Air Street Press 的「State of AI: April 2026」报告补充了关键细节：中国 AI 实验室（智谱 GLM-5、DeepSeek 等）在非 NVIDIA 芯片上训练大模型、Anthropic 揭露三家中国 AI 实验室大规模蒸馏 Claude、Meta 发布 4 款自研 AI 芯片挑战 NVIDIA。<br><small>来源：<a href=\"https://fortune.com/2026/04/07/spacex-openai-anthropic-reopen-ipo-market-crunchbase/\">Fortune/Crunchbase</a>、<a href=\"https://press.airstreet.com/p/state-of-ai-april-2026-newsletter\">Air Street Press</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>Anthropic 完成从挑战者到领先者的身份转换</strong>：收入超越 OpenAI + 企业份额追平 = 市场叙事已经翻转</li><li><strong>AI 超级 IPO 窗口正在打开</strong>：SpaceX → OpenAI → Anthropic 的上市节奏将定义 2026 下半年的科技资本市场</li><li><strong>AI 资本泡沫还是范式转移？</strong>：$3000 亿 Q1 风投 + 150% 增长率 = 历史上最激进的科技投资周期</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天的早间和晚间报道合在一起，讲述了一个完整的故事：Anthropic 正在从 AI 行业的「有原则的挑战者」变成「有原则的领跑者」——而这个转变的速度超出了所有人的预期。</strong></p><p>让我把今天的数据串起来。早上：Ramp 数据显示 Anthropic 企业支出份额 30.6% vs OpenAI 35.2%，73% 新客户选 Anthropic。晚上：Anthropic ARR $300 亿，正式超越 OpenAI。设计板块：Flowstep 底层用 Anthropic 模型。把这三条线连起来，你看到的是：<strong>Anthropic 正在同时赢得三场战争——企业客户心智、绝对收入规模、以及 AI 基础设施的隐形渗透</strong>。OpenAI 的 $852B 估值建立在「AI 平台垄断者」的叙事上，但 Anthropic 的 $300B ARR 证明了一个不同的、而且更有说服力的叙事：「AI 行业的高通/ARM」——不需要拥有终端产品，只需要成为每个产品背后的智能引擎。</p><p>SpaceX IPO 的时机值得深思。SpaceX 本身和 AI 关系不大（虽然 xAI 是 Musk 的），但它的 IPO 将<strong>重新打开大型科技 IPO 的闸门</strong>。如果 SpaceX IPO 成功（市场预期它将是有史以来最大的 VC 支持的 IPO），OpenAI 和 Anthropic 都会加速上市节奏。但这里有一个微妙的博弈：<strong>Anthropic 在 IPO 前释放「ARR 超越 OpenAI」的消息，显然是为了抢占叙事高地</strong>——当投资者需要在 OpenAI 和 Anthropic 之间选择时，「收入已经超越」是一个极其有力的锚点。OpenAI 的 $852B 估值 vs Anthropic 可能的上市估值，将是 2026 下半年最精彩的资本市场叙事对决。</p><p>$3000 亿 Q1 风投是一个让人既兴奋又担忧的数字。150% 的同比增长不是正常的市场扩张，这是泡沫期的特征。但 AI 泡沫和之前的泡沫有一个关键区别：<strong>AI 公司真的在产生收入</strong>。Anthropic $300 亿 ARR、OpenAI 可能 $250-280 亿 ARR——这不是 2000 年那种「先烧钱再想盈利模型」的故事。AI 泡沫如果存在，它更像是估值泡沫（$852B 是否合理？）而非收入泡沫。Air Street Press 报告提到的中国 AI 实验室在华为芯片上训练 745B 参数模型（智谱 GLM-5）和 Anthropic 揭露大规模模型蒸馏，则提醒我们：<strong>AI 竞赛不只是硅谷的游戏，地缘政治因素正在深刻影响技术路线和商业策略</strong>。</p><p><strong>我的预判：SpaceX 6 月路演成功后，Anthropic 将在 Q3 正式启动 IPO 流程，估值目标 $800-1000 亿，直接与 OpenAI 的 $852B 形成对标。Anthropic 的 IPO 叙事将强调「收入超越 OpenAI + 安全领导力 + AI 基础设施渗透（从 Claude Code 到设计工具）」。OpenAI 将被迫在 Anthropic IPO 前加速自己的上市进程，否则叙事将被 Anthropic 完全主导。最大胆预测：到 2026 年底，「Anthropic vs OpenAI」的市场叙事将从「挑战者 vs 领先者」完全翻转为「基础设施型 AI 公司 vs 消费型 AI 公司」——而历史告诉我们，在科技行业，基础设施公司通常比消费公司活得更久、更赚钱（参考 AWS vs 任何一个 SaaS 独角兽）。</strong></p></div>",
        "en": "<h3>📌 AI × Tech (Evening Update)</h3><ul><li><strong>Anthropic ARR Surges Past $30B, Overtaking OpenAI</strong> — MSN/Bloomberg reports <strong>Anthropic's annualized revenue rate has surged past $30 billion, more than tripling from $9 billion last year, officially surpassing OpenAI</strong>. All-In Podcast's latest episode deep-dived into this milestone. This completes the loop with this morning's Ramp enterprise spending data: <strong>Anthropic is not only catching up in enterprise share (30.6% vs 35.2%) but has overtaken in absolute revenue</strong>. Drivers: Claude Code enterprise adoption, Anthropic API as AI infrastructure (powering tools like Flowstep), and trust premium from safety-first positioning.<br><small>Source: <a href=\"https://www.msn.com/en-us/money/markets/anthropic-tops-openai-on-revenue-with-30b-run-rate-while-spacex-plans-june-investor-roadshow-ahead-of-mega-ipos/ar-AA20k7gA\">MSN/Bloomberg</a>, <a href=\"https://www.youtube.com/watch?v=DVBJQQCjgXU\">All-In Podcast</a></small></li><li><strong>SpaceX Confidential IPO Filing Sparks AI Mega-IPO Expectations</strong> — Fortune/Bloomberg report <strong>SpaceX has filed confidentially for IPO with a June investor roadshow planned</strong>. This could open the floodgates for OpenAI ($852B valuation) and Anthropic. Timing of Anthropic's $30B ARR disclosure before the IPO window is telling.<br><small>Source: <a href=\"https://fortune.com/2026/04/07/spacex-openai-anthropic-reopen-ipo-market-crunchbase/\">Fortune</a>, <a href=\"https://www.bloomberg.com/news/newsletters/2026-04-02/spacex-s-record-listing-could-lead-to-a-year-of-big-ai-ipos\">Bloomberg</a></small></li><li><strong>Q1 2026 Global AI VC Hits Record $300B Across 6,000 Startups</strong> — Crunchbase data shows <strong>~$300 billion invested in ~6,000 startups globally in Q1, up 150%+ YoY and QoQ</strong>. Air Street Press adds context: Chinese labs training on Huawei chips (Zhipu GLM-5, 745B MoE), Anthropic exposing industrial-scale Claude distillation by three Chinese labs, Meta releasing 4 custom AI chips.<br><small>Source: <a href=\"https://fortune.com/2026/04/07/spacex-openai-anthropic-reopen-ipo-market-crunchbase/\">Fortune/Crunchbase</a>, <a href=\"https://press.airstreet.com/p/state-of-ai-april-2026-newsletter\">Air Street Press</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Anthropic completes challenger-to-leader transition: revenue overtake + enterprise share parity</li><li>AI mega-IPO window opening: SpaceX → OpenAI → Anthropic defines H2 2026 capital markets</li><li>$300B Q1 VC: bubble or paradigm shift? AI companies generate real revenue, but valuations may be stretched</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Today's morning and evening reports together tell a complete story: Anthropic is transitioning from 'principled challenger' to 'principled leader' — faster than anyone expected.</strong></p><p>Connect today's data: Morning — Ramp shows 30.6% vs 35.2% enterprise share, 73% new customer win rate. Evening — $30B ARR, officially surpassing OpenAI. Design section — Flowstep uses Anthropic's model. Three connected threads: <strong>Anthropic is simultaneously winning enterprise mindshare, absolute revenue, and invisible infrastructure penetration</strong>. OpenAI's $852B valuation rests on 'AI platform monopolist' narrative; Anthropic's $30B ARR proves a different, more compelling one: 'AI industry's Qualcomm/ARM' — powering every product without owning the endpoint.</p><p>SpaceX IPO timing matters. It reopens the mega-tech IPO floodgates. <strong>Anthropic releasing '$30B ARR surpasses OpenAI' before the IPO window is deliberate narrative positioning</strong> — when investors choose between OpenAI and Anthropic, 'already surpassed in revenue' is a powerful anchor.</p><p>$300B Q1 VC at 150% growth is bubble-territory by any historical standard. But AI bubbles differ from past ones: <strong>AI companies generate real revenue</strong>. Anthropic $30B, OpenAI ~$25-28B — this isn't 2000-era 'burn first, monetize later.' The bubble, if it exists, is in valuations, not revenue.</p><p><strong>Predictions: After SpaceX's June roadshow succeeds, Anthropic formally initiates IPO in Q3 targeting $80-100B valuation, directly benchmarking against OpenAI's $852B. Anthropic's IPO narrative: 'revenue overtake + safety leadership + AI infrastructure penetration.' OpenAI accelerates its own IPO to avoid ceding the narrative entirely. Boldest: by year-end, the 'Anthropic vs OpenAI' market narrative fully inverts from 'challenger vs leader' to 'infrastructure AI vs consumer AI' — and history shows infrastructure companies outlast and out-earn consumer ones (see: AWS vs any SaaS unicorn).</strong></p></div>"
    },
    "cover": images.get("msn_anthropic") or images.get("fortune") or "",
    "sources": [
        {
            "title": {"zh": "Anthropic 年化收入突破 $300 亿超越 OpenAI", "en": "Anthropic Tops OpenAI on Revenue with $30B Run-Rate"},
            "url": "https://www.msn.com/en-us/money/markets/anthropic-tops-openai-on-revenue-with-30b-run-rate-while-spacex-plans-june-investor-roadshow-ahead-of-mega-ipos/ar-AA20k7gA",
            "image": images.get("msn_anthropic", "")
        },
        {
            "title": {"zh": "SpaceX、OpenAI、Anthropic 或将重启 IPO 市场", "en": "SpaceX, OpenAI, Anthropic Could Reopen the IPO Market"},
            "url": "https://fortune.com/2026/04/07/spacex-openai-anthropic-reopen-ipo-market-crunchbase/",
            "image": images.get("fortune", "")
        },
        {
            "title": {"zh": "State of AI：2026 年 4 月通讯", "en": "State of AI: April 2026 Newsletter"},
            "url": "https://press.airstreet.com/p/state-of-ai-april-2026-newsletter",
            "image": images.get("airstreet", "")
        },
        {
            "title": {"zh": "All-In Podcast：Anthropic 的 $300 亿狂飙", "en": "All-In Podcast: Anthropic's $30B Ramp"},
            "url": "https://www.youtube.com/watch?v=DVBJQQCjgXU",
            "image": ""
        }
    ]
}

# Load existing issues.json and prepend
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r", encoding="utf-8") as f:
    issues = json.load(f)

issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("Done! Inserted 2 new issues (design + tech evening) at the top of issues.json")
print(f"Total issues: {len(issues)}")
