#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rex Daily update for 2026-03-15"""
import json, urllib.request, urllib.error, re, ssl

ctx = ssl.create_default_context()

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            html = r.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', html)
        if not m:
            m = re.search(r'content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html)
        return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images
og = {}
urls = {
    "meta_theweek": "https://www.theweek.in/news/biz-tech/2026/03/14/meta-plans-major-layoffs-as-its-ai-costs-increase-report.html",
    "meta_yahoo": "https://finance.yahoo.com/news/exclusive-meta-planning-sweeping-layoffs-001705452.html",
    "meta_slashdot": "https://tech.slashdot.org/story/26/03/14/012226/meta-plans-sweeping-layoffs-as-ai-costs-mount",
    "arcticleaf": "https://www.arcticleaf.com/blog/learning-center/ai-in-design-from-inspiration-to-execution/",
    "siri_toms": "https://www.tomsguide.com/ai/apple-intelligence/apples-big-siri-overhaul-looks-set-for-spring-2026-heres-what-itll-be-able-to-do",
    "siri_cnbc": "https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html",
    "siri_delayed": "https://www.androidheadlines.com/2026/02/apple-siri-ai-overhaul-delayed-batch-rollout-ios-27.html",
    "uxdesign_apple": "https://uxdesign.cc/the-first-fruit-of-the-google-apple-ai-pact-efec0ff52a03",
    "medium_daily": "https://medium.com/@stephen.stanley777/ai-daily-update-14-03-2026-8cbcbce8e279",
    "figma_ux": "https://www.figma.com/resource-library/ai-tools-for-ux-designers/",
    "uxinstitute": "https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/",
}
for k, u in urls.items():
    og[k] = get_og_image(u)
    print(f"og[{k}] = {og[k][:80] if og[k] else '(none)'}")

design_issue = {
    "date": "2026-03-15",
    "section": "design",
    "title": {
        "zh": "93%设计师已用 AI · 设计行业的「效率陷阱」· 当 AI 从加速器变成替代者",
        "en": "93% of Designers Now Use AI · The Design Industry's 'Efficiency Trap' · When AI Shifts from Accelerator to Replacement"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>2026 年调查：93% 的设计师在工作流中使用 AI 工具，70% 认为 AI 提升了创意构思效率</strong> — Arctic Leaf 的深度报告揭示了一个已经发生但尚未被充分讨论的现实：AI 工具在设计行业的渗透率已经达到 93%。但报告的关键洞察不是数字本身——而是 AI 正在被用于哪些环节：图片放大、布局变体生成、边缘案例检测、资产批量处理。这些都是「执行层」任务。设计师的角色正在向「判断力、同理心和商业逻辑」转移。<br><small>来源：<a href=\"https://www.arcticleaf.com/blog/learning-center/ai-in-design-from-inspiration-to-execution/\">Arctic Leaf: AI in Design 2026</a></small></li><li><strong>Figma 更新 UX 工具指南：AI 连接工作流成为新标准，从构思到交付一条线</strong> — Figma 最新发布的 2026 UX 工具指南把 Figma Make、UX Pilot、Maze 等工具定义为「AI 连接工作流」的核心节点。关键变化是：AI 不再是单独的工具，而是嵌入在每个设计阶段——从 prompt 生成 UI，到 AI 驱动的 UX 评审，再到预测性热力图。设计团队的工作方式正在从「工具切换」变成「AI 流水线」。<br><small>来源：<a href=\"https://www.figma.com/resource-library/ai-tools-for-ux-designers/\">Figma: Top AI Tools for UX 2026</a></small></li><li><strong>UX Design Institute 发布 9 大 AI 工具排行：Maze 和 Contentsquare 的 AI 功能让用户研究时间缩短 60%</strong> — UX Design Institute 的 2026 排行聚焦一个被忽视的领域：AI 在用户研究和可用性测试中的应用。Maze 的 AI 功能可以从原型测试直接生成洞察报告，Contentsquare 的行为分析 AI 能预测用户行为模式。这意味着「用户研究」这个曾经需要专人数周完成的环节，正在被压缩到几小时。<br><small>来源：<a href=\"https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/\">UX Design Institute: Top 9 AI Tools 2026</a></small></li><li><strong>LinkedIn 热议：「AI 会取代平面设计师吗？」仍是 2026 年最热门职业搜索问题</strong> — 数据显示这个问题的搜索量在 2026 年 Q1 持续上升。AI 设计岗位薪资范围 $58K-$220K，市场需求强劲，但传统平面设计岗位持续萎缩。行业正在分化：掌握 AI 工具的设计师薪资上涨，纯执行型设计师面临严重挤压。<br><small>来源：<a href=\"https://www.linkedin.com/posts/ai-era-blog-post_futureofwork-ai-uxdesign-activity-7429089906062417921-NHpQ\">LinkedIn: AI's Impact on Graphic Design</a> | <a href=\"https://www.ziprecruiter.com/Jobs/Ai-Designer\">ZipRecruiter: AI Designer Jobs</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 渗透率 93%</strong>：设计行业已经不存在「要不要用 AI」的讨论，只有「怎么用」</li><li><strong>用户研究自动化</strong>：AI 正在压缩设计流程中最「人力密集」的环节</li><li><strong>设计师二元分化</strong>：AI 熟练型 vs 纯执行型，薪资差距在加速拉大</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>93% 这个数字看起来是好消息，但它隐藏着一个危险的叙事：当所有人都在用 AI「提效」时，效率本身就不再是竞争优势——它变成了入场券。</strong></p><p>让我把今天的设计新闻和昨天的 Meta 裁员放在一起看。Meta 计划裁掉 20% 的员工，Zuckerberg 的原话是「AI 让更小的团队完成以前更大团队才能做的事」。把这句话翻译成设计行业的语言就是：一个用 AI 工具的设计师可以做三个传统设计师的活。Arctic Leaf 的报告用更学术的方式说了同一件事——AI 处理图片放大、布局变体、资产批量处理，设计师「聚焦判断力和商业逻辑」。这话说得漂亮，但潜台词是：<strong>那些只做图片放大、布局变体、资产批量处理的设计师，已经没有存在的必要了。</strong></p><p>93% 的设计师在用 AI——这个数字本身就是一个效率陷阱。当一个行业的几乎所有从业者都获得了同一个效率工具时，结果不是每个人都更轻松，而是产出标准被拉高、人员需求被降低。想象一下：如果 AI 让每个设计师的产出翻倍，公司的反应不是「太好了，大家都能早下班」，而是「太好了，我们只需要一半的设计师」。这正是 Meta 正在做的事，只不过 Meta 做得更激进、更公开。</p><p>UX Design Institute 的报告让我更加确信这个趋势。用户研究——这个曾经被认为是「不可替代的人类工作」——现在被 Maze 和 Contentsquare 的 AI 压缩到几小时。用户研究员这个角色，两年前还被认为是设计团队里最安全的岗位（因为「需要人类同理心」），现在也面临重新定义。不是说 AI 能完全取代深度用户访谈，但 80% 的常规可用性测试？AI 已经够用了。</p><p><strong>我的判断：2026 年设计行业正在经历一场无声的结构性重组。</strong>表面上看，93% 的设计师都在用 AI，一片繁荣。但水面下，团队在缩小，初级岗位在消失，中间层在被压缩。LinkedIn 上「AI 会取代设计师吗」搜索量上升不是因为人们杞人忧天——而是因为他们身边已经有人被替代了。$58K-$220K 的 AI 设计师薪资区间说明市场在分化：顶端的人比以前更值钱，但底部的空间在快速收缩。</p><p>给设计师的建议：不要只学「怎么用 AI 工具」，要学「AI 做不了什么」。判断力、商业洞察、跨领域整合能力、对用户动机的深层理解——这些是 AI 工具清单上永远不会出现的技能。93% 的渗透率意味着 AI 使用能力已经是基本功，不是差异化因素。真正的差异化在于：你能不能在 AI 给你节省的时间里，做出 AI 做不出的东西。</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>2026 Survey: 93% of Designers Use AI Tools, 70% Say It Boosts Ideation</strong> — Arctic Leaf's report reveals AI tool penetration at 93% in design. Key insight: AI handles execution tasks (upscaling, layout variations, edge cases), pushing designers toward judgment, empathy, and business logic.<br><small>Source: <a href=\"https://www.arcticleaf.com/blog/learning-center/ai-in-design-from-inspiration-to-execution/\">Arctic Leaf</a></small></li><li><strong>Figma Updates UX Tool Guide: AI-Connected Workflows as New Standard</strong> — Figma Make, UX Pilot, Maze defined as core nodes in an AI-connected workflow. AI embedded at every design stage — from prompt-to-UI to predictive heatmaps.<br><small>Source: <a href=\"https://www.figma.com/resource-library/ai-tools-for-ux-designers/\">Figma</a></small></li><li><strong>UX Design Institute: Maze & Contentsquare AI Cut User Research Time by 60%</strong> — AI in user research and usability testing compresses weeks-long processes to hours.<br><small>Source: <a href=\"https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/\">UX Design Institute</a></small></li><li><strong>\"Will AI Replace Designers?\" Still #1 Career Search in 2026</strong> — AI designer jobs pay $58K-$220K with strong demand, but traditional graphic design roles shrink. Industry bifurcation accelerates.<br><small>Source: <a href=\"https://www.linkedin.com/posts/ai-era-blog-post_futureofwork-ai-uxdesign-activity-7429089906062417921-NHpQ\">LinkedIn</a></small></li></ul><h3>🔄 Trends</h3><ul><li>93% AI penetration: the question is no longer \"whether\" but \"how\"</li><li>User research automation: AI compresses the most labor-intensive design phase</li><li>Designer bifurcation: AI-proficient vs execution-only, pay gap widening fast</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>93% sounds like good news, but it hides a dangerous narrative: when everyone has the same efficiency tool, efficiency stops being competitive advantage — it becomes table stakes.</strong></p><p>Connect today's design data with yesterday's Meta layoffs (20% cuts because \"AI lets smaller teams do more\"). Arctic Leaf's report says AI handles upscaling, layout variants, asset batching while designers \"focus on judgment.\" The subtext: designers who only did those execution tasks are already unnecessary. When 93% adoption doubles everyone's output, companies don't let people leave early — they need half the designers. UX research, once considered \"safe\" due to requiring human empathy, is being compressed to hours by Maze and Contentsquare. <strong>The design industry is undergoing silent structural reorganization. Teams shrink, junior roles disappear, middle layer gets compressed. The real differentiator isn't knowing AI tools (that's baseline now) — it's what you can do with the time AI saves you that AI can't do itself.</strong></p></div>"
    },
    "cover": og.get("arcticleaf", "") or og.get("figma_ux", ""),
    "sources": [
        {
            "title": {"zh": "Arctic Leaf: AI in Design 2026", "en": "Arctic Leaf: AI in Design 2026"},
            "url": "https://www.arcticleaf.com/blog/learning-center/ai-in-design-from-inspiration-to-execution/",
            "image": og.get("arcticleaf", "")
        },
        {
            "title": {"zh": "Figma: 2026 UX AI 工具指南", "en": "Figma: Top AI Tools for UX 2026"},
            "url": "https://www.figma.com/resource-library/ai-tools-for-ux-designers/",
            "image": og.get("figma_ux", "")
        },
        {
            "title": {"zh": "UX Design Institute: 9 大 AI 工具", "en": "UX Design Institute: Top 9 AI Tools"},
            "url": "https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/",
            "image": og.get("uxinstitute", "")
        },
        {
            "title": {"zh": "LinkedIn: AI 对设计行业的冲击", "en": "LinkedIn: AI's Impact on Design"},
            "url": "https://www.linkedin.com/posts/ai-era-blog-post_futureofwork-ai-uxdesign-activity-7429089906062417921-NHpQ",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-03-15",
    "section": "tech",
    "title": {
        "zh": "Meta 计划裁员 20% · AI 烧钱时代的人力代价 · Apple Siri 大改延期 · 科技巨头的 AI 焦虑症",
        "en": "Meta Plans 20% Layoffs · The Human Cost of AI Spending · Apple Siri Overhaul Delayed · Big Tech's AI Anxiety"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Meta 计划大规模裁员：可能裁掉 20% 以上员工（约 16,000 人），AI 基础设施成本是主因</strong> — Reuters 独家报道，Meta 正在规划自 2022 年以来最大规模的裁员。三位知情人士透露，裁员比例可能超过 20%——以 Meta 截至 2025 年底 79,000 名员工计算，这意味着约 16,000 人将失去工作。直接原因：AI 基础设施投入巨大，需要削减人力成本来平衡。更深层的逻辑：Zuckerberg 认为 AI 能让更小的团队完成更多工作，所以裁的不只是「省钱」，而是「换血」。同期，Amazon 裁 16,000 人（10%），Oracle 计划裁 20,000-30,000 人扩建 AI 数据中心。<br><small>来源：<a href=\"https://finance.yahoo.com/news/exclusive-meta-planning-sweeping-layoffs-001705452.html\">Reuters/Yahoo Finance</a> | <a href=\"https://www.theweek.in/news/biz-tech/2026/03/14/meta-plans-major-layoffs-as-its-ai-costs-increase-report.html\">The Week</a></small></li><li><strong>Apple Siri AI 大改延期：Gemini 驱动的新 Siri 遇测试障碍，全面上线推迟至 2026 年底甚至更晚</strong> — Apple 与 Google 的多年合作协议（Gemini 驱动 Apple Foundation Models）原计划在 iOS 26.4（2026 春季）推出全面改版的 Siri，但 Android Headlines 报道称因性能瓶颈，Apple 改为分阶段发布策略。首批功能包括 App Intents（Siri 代替用户操作应用）和 Playlist Playground，但核心的上下文理解和跨应用智能可能要等到 iOS 27。讽刺的是，Apple 每年付 Google 约 10 亿美元使用 Gemini，但连 Siri 的基本体验都还没追上 ChatGPT 的语音模式。<br><small>来源：<a href=\"https://www.tomsguide.com/ai/apple-intelligence/apples-big-siri-overhaul-looks-set-for-spring-2026-heres-what-itll-be-able-to-do\">Tom's Guide</a> | <a href=\"https://www.androidheadlines.com/2026/02/apple-siri-ai-overhaul-delayed-batch-rollout-ios-27.html\">Android Headlines</a> | <a href=\"https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html\">CNBC</a></small></li><li><strong>NYT 报道：Meta 下一代 AI 模型发布延迟，落后于 Google、OpenAI 和 Anthropic</strong> — 与裁员消息同步曝光的还有 Meta 的 AI 模型进展问题。NYT 称 Meta 已推迟其下一代大语言模型的发布，原因是性能未达预期，落后于竞争对手。这与 Zuckerberg「全力 All-in AI」的公开叙事形成巨大反差——花了最多的钱，裁了最多的人，但模型还是落后了。<br><small>来源：<a href=\"https://tech.slashdot.org/story/26/03/14/012226/meta-plans-sweeping-layoffs-as-ai-costs-mount\">Slashdot/NYT</a></small></li><li><strong>Morgan Stanley 警告：2026 上半年 AI 将迎来重大突破，「大多数人没准备好」</strong> — Morgan Stanley 发布报告称一个「massive AI breakthrough」即将到来，可能从根本上改变多个行业的运作方式。报告没有指明具体是哪家公司或哪项技术，但暗示与推理能力和 agent 架构相关。在投行语境里，这种级别的预警通常意味着他们的客户已经在布局。<br><small>来源：<a href=\"https://finance.yahoo.com/news/morgan-stanley-warns-ai-breakthrough-072000084.html\">Yahoo Finance/Morgan Stanley</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 烧钱 → 裁人闭环</strong>：Meta、Amazon、Oracle 同步裁员，AI 基础设施投资直接转嫁为人力成本削减</li><li><strong>Apple 的 AI 困境</strong>：花 10 亿/年买 Gemini，Siri 还是追不上，分阶段发布 = 承认失败</li><li><strong>钱花了，模型没出来</strong>：Meta 的 AI 模型延迟说明砸钱不等于领先</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>本周科技行业的主旋律可以用一句话概括：AI 的账单到了。</strong></p><p>Meta 裁 20%、Amazon 裁 16,000、Oracle 裁 20,000-30,000——这不是巧合，这是一个行业性的结构调整。过去两年，每家科技巨头都在喊「All-in AI」，疯狂建数据中心、买 GPU、招 AI 工程师。现在账单到了：基础设施投入了数百亿，但 AI 的商业回报还远没有到覆盖成本的阶段。怎么办？裁掉「非 AI」岗位来平衡财报。这是一个残酷但清晰的逻辑：<strong>公司不是在裁员，是在用人类员工的工资来补贴 AI 的电费。</strong></p><p>Meta 的情况尤其讽刺。Zuckerberg 用「AI 让小团队做大事」来合理化裁员，但同时 NYT 报道他的 AI 模型开发延迟，落后于 Google、OpenAI 和 Anthropic。这说明什么？<strong>花最多钱的人不一定跑得最快。</strong>Meta 在 AI 基础设施上的投入是天文数字，但砸钱不等于能力。OpenAI 有先发优势和人才密度，Anthropic 有安全研究的深度积累，Google 有 Gemini 和 TPU 的垂直整合——Meta 有什么？一个延迟发布的模型和一轮 16,000 人的裁员。</p><p>Apple 的 Siri 故事同样值得深思。他们做了一个看起来很聪明的决定——不自己从头训练基础模型，花钱买 Google 的 Gemini。但问题是：即使用了市面上最好的模型之一，Siri 的改版还是延期了。这说明 AI 产品化的瓶颈不在模型层面，而在工程整合、用户体验和系统架构层面。Apple 擅长的恰恰是这些，但在 AI 的语境下，它的方法论似乎失效了。分阶段发布不是「谨慎」，是承认他们没法一次做好。当 ChatGPT 的语音模式已经能流畅地帮人点外卖、Google Gemini 能在搜索中直接给出结构化答案时，Siri 还在「计划中」——这个差距不是功能层面的，是时代层面的。</p><p>Morgan Stanley 的「重大突破」预警很有意思。投行不会无缘无故发这种报告——他们的客户需要提前布局。如果这个突破与 agent 架构相关（很多线索指向这个方向），那它可能进一步加速今天所有新闻里描述的趋势：更少的人，更多的 AI agent，更大的效率差距。<strong>2026 年的科技行业正在经历一场「AI 达尔文主义」——不是最大的公司生存，也不是花钱最多的公司生存，而是最快把 AI 转化为实际产品能力的公司生存。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Meta Plans 20%+ Layoffs (~16,000 Jobs) as AI Infrastructure Costs Soar</strong> — Reuters exclusive: Meta's biggest cuts since 2022. Zuckerberg says AI enables smaller teams. Amazon (16K), Oracle (20-30K) making parallel cuts.<br><small>Source: <a href=\"https://finance.yahoo.com/news/exclusive-meta-planning-sweeping-layoffs-001705452.html\">Reuters/Yahoo Finance</a></small></li><li><strong>Apple's Gemini-Powered Siri Overhaul Delayed to Late 2026</strong> — Performance roadblocks force phased rollout. Apple pays Google ~$1B/year for Gemini but can't ship a full Siri upgrade. First features (App Intents) in iOS 26.4, full AI Siri possibly iOS 27.<br><small>Source: <a href=\"https://www.tomsguide.com/ai/apple-intelligence/apples-big-siri-overhaul-looks-set-for-spring-2026-heres-what-itll-be-able-to-do\">Tom's Guide</a> | <a href=\"https://www.androidheadlines.com/2026/02/apple-siri-ai-overhaul-delayed-batch-rollout-ios-27.html\">Android Headlines</a></small></li><li><strong>Meta's Next AI Model Delayed, Falling Behind Google/OpenAI/Anthropic</strong> — NYT reports Meta's next-gen LLM underperforms rivals despite massive spending. Spends most, lags behind.<br><small>Source: <a href=\"https://tech.slashdot.org/story/26/03/14/012226/meta-plans-sweeping-layoffs-as-ai-costs-mount\">Slashdot/NYT</a></small></li><li><strong>Morgan Stanley: Massive AI Breakthrough Coming in H1 2026</strong> — Report warns most of the world isn't ready. Hints at reasoning and agent architecture advances.<br><small>Source: <a href=\"https://finance.yahoo.com/news/morgan-stanley-warns-ai-breakthrough-072000084.html\">Yahoo Finance</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI spending → layoffs loop: Meta, Amazon, Oracle cut simultaneously</li><li>Apple's AI dilemma: $1B/year on Gemini, Siri still can't keep up</li><li>Money ≠ leadership: Meta's delayed model proves spending doesn't equal capability</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>The AI bill has arrived. Meta cuts 20%, Amazon 16K, Oracle 20-30K — not coincidence, but industry-wide structural adjustment.</strong></p><p>Companies subsidize AI's electricity bills with human salaries. Meta's case is especially ironic: Zuckerberg justifies cuts with \"AI enables smaller teams\" while NYT reports his AI model development is delayed and behind rivals. Spending the most doesn't mean leading. Apple's Siri delay is equally telling — even with Google's best model, productization bottlenecks persist. The gap between Siri's \"planned\" features and ChatGPT's voice mode isn't functional, it's generational. Morgan Stanley's breakthrough warning suggests agent architectures may accelerate all these trends further. <strong>2026 tech is experiencing \"AI Darwinism\" — survival goes not to the biggest spender, but to whoever converts AI into actual product capability fastest.</strong></p></div>"
    },
    "cover": og.get("meta_theweek", "") or og.get("meta_yahoo", ""),
    "sources": [
        {
            "title": {"zh": "Reuters: Meta 计划裁员 20%", "en": "Reuters: Meta Plans 20% Layoffs"},
            "url": "https://finance.yahoo.com/news/exclusive-meta-planning-sweeping-layoffs-001705452.html",
            "image": og.get("meta_yahoo", "")
        },
        {
            "title": {"zh": "Tom's Guide: Apple Siri 大改版计划", "en": "Tom's Guide: Apple Siri Overhaul"},
            "url": "https://www.tomsguide.com/ai/apple-intelligence/apples-big-siri-overhaul-looks-set-for-spring-2026-heres-what-itll-be-able-to-do",
            "image": og.get("siri_toms", "")
        },
        {
            "title": {"zh": "CNBC: Apple 选择 Gemini 驱动 Siri", "en": "CNBC: Apple Picks Gemini for Siri"},
            "url": "https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html",
            "image": og.get("siri_cnbc", "")
        },
        {
            "title": {"zh": "Morgan Stanley: AI 重大突破即将到来", "en": "Morgan Stanley: AI Breakthrough Coming"},
            "url": "https://finance.yahoo.com/news/morgan-stanley-warns-ai-breakthrough-072000084.html",
            "image": ""
        }
    ]
}

# Load existing issues and prepend new ones
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

issues = [design_issue, tech_issue] + issues

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("Done! Added 2 issues for 2026-03-15")
