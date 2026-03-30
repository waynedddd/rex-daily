# -*- coding: utf-8 -*-
"""Rex Daily Update - 2026-03-30 Evening"""
import json, urllib.request, re

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        resp = urllib.request.urlopen(req, timeout=10)
        data = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', data, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data, re.I)
        return m.group(1) if m else ""
    except:
        return ""

ISSUES_PATH = "issues.json"

with open(ISSUES_PATH, "r", encoding="utf-8") as f:
    issues = json.load(f)

# --- DESIGN ISSUE (Evening) ---
design_sources = [
    {
        "title": {"zh": "Figma: 2026 设计师现状报告", "en": "Figma: State of the Designer 2026"},
        "url": "https://www.figma.com/blog/state-of-the-designer-2026/",
    },
    {
        "title": {"zh": "Figma 2026 更新悄然重新定义设计-开发交付", "en": "Figma's 2026 Updates Quietly Redefine Design-Dev Handoff"},
        "url": "https://medium.com/@Rythmuxdesigner/figmas-2026-updates-quietly-redefine-design-dev-handoff-and-not-everyone-s-ready-98307f2ea2a8",
    },
    {
        "title": {"zh": "UserTesting: AI 与 2026 设计现状", "en": "UserTesting: AI and State of Design 2026"},
        "url": "https://www.usertesting.com/resources/podcast/craft-ai-and-figma-state-of-design",
    },
    {
        "title": {"zh": "Design.com 达到 $33.5M ARR，同比增长 81%", "en": "Design.com Soars to $33.5M ARR With 81% YoY Growth"},
        "url": "https://news.designrush.com/designcom-ai-platform-hits-33m-arr-with-rapid-growth",
    },
]

for s in design_sources:
    s["image"] = get_og_image(s["url"])

design_cover = get_og_image("https://www.figma.com/blog/state-of-the-designer-2026/") or get_og_image("https://medium.com/@Rythmuxdesigner/figmas-2026-updates-quietly-redefine-design-dev-handoff-and-not-everyone-s-ready-98307f2ea2a8")

design_issue = {
    "date": "2026-03-30",
    "section": "design",
    "title": {
        "zh": "Figma 设计师报告：89% 因 AI 工作更快但焦虑未减 · 设计-开发交付被悄然重构 · AI 设计平台 Design.com 年收入破 3300 万",
        "en": "Figma Report: 89% Work Faster With AI But Anxiety Persists · Design-Dev Handoff Quietly Redefined · AI Platform Design.com Hits $33.5M ARR"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul><li><strong>Figma「2026 设计师现状」报告：89% 说 AI 让他们更快，但不安全感并没减少</strong> — Figma 发布了年度 State of the Designer 报告，数据很有意思：<strong>89% 的设计师表示 AI 工具让他们工作更快，80% 表示协作更好，使用 AI 的设计师工作满意度高出 25%。</strong>但报告的另一面是：尽管效率提升了，设计师群体的焦虑感并没有下降。问题不在于「AI 能不能帮我」，而在于「AI 会不会替代我」。报告的核心洞察是——<strong>真正拥抱 AI 的设计师反而更乐观，因为他们看到了 AI 提升的是低价值重复劳动，而非创意判断力。</strong>Figma 的招聘数据也显示，设计需求在各行业持续上升，尤其是在那些通过用户体验来建立竞争壁垒的公司。<br><small>来源：<a href="https://www.figma.com/blog/state-of-the-designer-2026/">Figma Blog</a></small></li><li><strong>Figma 2026 更新悄然重构设计到开发的交付链</strong> — Figma 的一系列 2026 更新正在安静但深刻地改变设计师和开发者的协作方式：<strong>Git 连接的 Figma 文件、实时代码同步（Beta）、AI 辅助的设计-代码翻译。</strong>Medium 上一篇分析文章的标题很到位：「不是所有人都准备好了」。传统的「设计师画图→开发者还原→来回对稿」的流程正在被「设计即代码」取代。对于习惯了旧流程的团队来说，这不只是工具升级——这是工作流范式的转变。Figma 的策略很清晰：从设计工具进化为设计-开发一体化平台。<br><small>来源：<a href="https://medium.com/@Rythmuxdesigner/figmas-2026-updates-quietly-redefine-design-dev-handoff-and-not-everyone-s-ready-98307f2ea2a8">Medium</a></small></li><li><strong>AI 设计平台 Design.com 年收入 $33.5M，同比增长 81%</strong> — 澳大利亚 AI 设计平台 Design.com 第二年就达到 $33.5M ARR。它的定位很明确：面向创业者的一站式 AI 设计平台，从 logo 到网站全部免费，高级功能每月仅需几美元。<strong>这个数据说明：AI 设计工具的市场不只是在抢专业设计师的饭碗——它在创造一个全新的「非设计师设计」市场。</strong>当设计的门槛降到几美元/月时，「每个创业者都是设计师」不再是口号。<br><small>来源：<a href="https://news.designrush.com/designcom-ai-platform-hits-33m-arr-with-rapid-growth">DesignRush</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 让设计师更快但未减少焦虑</strong>：效率提升和存在感危机并行</li><li><strong>设计-开发边界持续模糊</strong>：Figma 从设计工具进化为设计-开发一体化平台</li><li><strong>AI 设计民主化创造新市场</strong>：Design.com 的增长证明非设计师需求巨大</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Figma 的 State of the Designer 2026 报告表面上是一份乐观的行业画像，但如果你仔细看，它其实揭示了设计行业正在经历的一次身份危机。</strong></p><p>89% 的设计师说 AI 让他们更快了。太好了。但「更快」从来不是设计的核心价值——「更对」才是。Figma 报告中最有趣的数据不是效率提升，而是<strong>使用 AI 的设计师满意度比不使用的高 25%</strong>。这说明了什么？不是 AI 工具本身让人快乐，而是<strong>对 AI 的掌控感减轻了焦虑</strong>。那些主动拥抱 AI 的设计师发现，AI 接管的是他们本来就不喜欢做的事——像素对齐、样式迁移、重复迭代。而他们擅长的——理解用户需求、做出审美判断、在模糊中找到方向——AI 暂时做不了。关键词是「暂时」。</p><p>Figma 的 Git 连接和实时代码同步则代表了另一个更根本的变化。过去十年，设计和开发是两个平行宇宙：设计师在 Figma 里画，开发者在 VS Code 里写，中间靠 Zeplin 或 Inspect 这样的「翻译层」连接。现在 Figma 说：<strong>翻译层不需要了，设计文件就是代码的源头。</strong>这对设计师意味着什么？如果你的产出直接变成代码，那你不再只是「画图的人」——你是「定义产品行为的人」。权力上移了。但条件是你得懂代码逻辑，至少是组件化思维和状态管理。不懂的设计师会发现自己被排除在新工作流之外。</p><p>Design.com 的 $33.5M ARR 数据则提供了行业的另一个维度。81% 的同比增长证明了一件事：<strong>AI 设计工具的最大市场不在专业设计师——在数千万不会设计但需要设计产出的创业者。</strong>这不是抢设计师的活，这是扩大了「设计」这个概念的覆盖面。就像 iPhone 没有杀死摄影师，但它让每个人都成了摄影师。Canva 做了同样的事，Design.com 在用 AI 进一步降低门槛。</p><p>把这三条新闻串起来，我看到一个清晰的分层正在形成：<strong>底层是「AI 生成设计」（Design.com 们）——门槛极低，面向非设计师；中层是「AI 增强设计」（Figma Make、Google Stitch）——设计师使用 AI 加速工作流；顶层是「设计即决策」（Figma 的设计-开发一体化）——设计师从执行者进化为产品定义者。</strong>设计师的焦虑来源于不知道自己在哪层。但答案很明确：如果你只会推像素，你会被底层的 AI 工具挤压；如果你能做判断和决策，你会被中层和顶层的工具赋能。Figma 报告里那 25% 的满意度差距，本质上就是这两种设计师之间的分野。</p><p>给 Wayne 的建议：关注 Figma 的 Git 连接和 Live Code Sync Beta。这不是一个小功能——它标志着 Figma 从「设计工具」到「产品开发前端」的转型。如果你的团队还在用截图+标注的方式交付设计稿，现在是时候升级了。</p></div>',
        "en": '<h3>📌 AI × Design</h3><ul><li><strong>Figma State of the Designer 2026: 89% Say AI Makes Them Faster, But Anxiety Persists</strong> — Figma\'s annual report reveals: <strong>89% of designers say AI tools speed up their work, 80% report better collaboration, and AI-using designers are 25% more satisfied at work.</strong> Yet anxiety hasn\'t decreased. The insight: <strong>designers who embrace AI are more optimistic because they see it automating low-value repetitive tasks, not creative judgment.</strong> Figma\'s hiring data also shows design demand rising across industries.<br><small>Source: <a href="https://www.figma.com/blog/state-of-the-designer-2026/">Figma Blog</a></small></li><li><strong>Figma 2026 Updates Quietly Redefine Design-Dev Handoff</strong> — Figma\'s 2026 updates are deeply changing designer-developer collaboration: <strong>Git-connected Figma files, live code sync (Beta), AI-assisted design-to-code translation.</strong> The traditional "design→handoff→back-and-forth" workflow is being replaced by "design is code." Figma\'s strategy: evolve from design tool to design-development unified platform.<br><small>Source: <a href="https://medium.com/@Rythmuxdesigner/figmas-2026-updates-quietly-redefine-design-dev-handoff-and-not-everyone-s-ready-98307f2ea2a8">Medium</a></small></li><li><strong>AI Design Platform Design.com Hits $33.5M ARR With 81% YoY Growth</strong> — Australia-based Design.com reached $33.5M ARR in its second year. Its positioning: all-in-one AI design for entrepreneurs, free basics with premium at a few dollars/month. <strong>The data shows AI design tools\' biggest market isn\'t professional designers — it\'s millions of non-designers who need design output.</strong><br><small>Source: <a href="https://news.designrush.com/designcom-ai-platform-hits-33m-arr-with-rapid-growth">DesignRush</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI makes designers faster but doesn\'t reduce anxiety — efficiency gains and existential crisis run parallel</li><li>Design-dev boundary continues blurring: Figma evolves from design tool to design-dev unified platform</li><li>AI design democratization creates new markets: Design.com\'s growth proves massive non-designer demand</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Figma\'s State of the Designer 2026 appears optimistic but reveals a design industry identity crisis.</strong> 89% say AI makes them faster — great, but "faster" was never design\'s core value; "right" is. The most telling stat: AI-using designers are 25% more satisfied. This isn\'t about the tools — it\'s about control reducing anxiety. Those who embrace AI discover it handles what they disliked (pixel alignment, style migration, repetitive iteration) while their strengths (user insight, aesthetic judgment, navigating ambiguity) remain uniquely human. For now. Figma\'s Git-connected files and live code sync represent something more fundamental: eliminating the translation layer between design and development. Design files become code\'s source of truth. This elevates designers from "people who draw" to "people who define product behavior" — but only if they understand component thinking and state management. Design.com\'s $33.5M ARR growth reveals the industry\'s other dimension: AI design\'s biggest market is millions of non-designers needing design output, expanding "design" coverage like iPhone expanded "photography." <strong>A clear stratification is forming: base layer = AI-generated design (Design.com, for non-designers); middle = AI-augmented design (Figma Make, Stitch, for designers); top = design-as-decision (Figma\'s dev integration, designers as product definers). The 25% satisfaction gap between AI-adopting and non-adopting designers is really the divide between these two design futures.</strong></p></div>'
    },
    "cover": design_cover,
    "sources": design_sources,
}

# --- TECH ISSUE (Evening) ---
tech_sources = [
    {
        "title": {"zh": "Meta 发布 TRIBE v2：预测大脑对视觉、听觉和语言的反应", "en": "Meta Releases TRIBE v2: Brain Encoding Model for fMRI Prediction"},
        "url": "https://www.marktechpost.com/2026/03/26/meta-releases-tribe-v2-a-brain-encoding-model-that-predicts-fmri-responses-across-video-audio-and-text-stimuli/",
    },
    {
        "title": {"zh": "JPMorgan 因 AI 推进启动员工「大规模再部署」计划", "en": "JPMorgan Plans Worker Redeployment Amid AI Push"},
        "url": "https://www.cnbc.com/2026/02/24/jpm-ceo-jamie-dimon-ai-reshaping-workforce-redeployment.html",
    },
    {
        "title": {"zh": "Figma AI 商业化：AI Credits 模式与平台扩张", "en": "Figma's Next Phase: AI Monetization and Platform-Wide Expansion"},
        "url": "https://finance.yahoo.com/news/figmas-next-phase-ai-monetization-154700003.html",
    },
    {
        "title": {"zh": "Anthropic 考虑最早 10 月 IPO", "en": "Claude AI Maker Anthropic Considers IPO as Soon as October"},
        "url": "https://www.reddit.com/r/ArtificialInteligence/comments/1s4ut8a/oneminute_daily_ai_news_3262026/",
    },
]

for s in tech_sources:
    s["image"] = get_og_image(s["url"])

tech_cover = get_og_image("https://www.marktechpost.com/2026/03/26/meta-releases-tribe-v2-a-brain-encoding-model-that-predicts-fmri-responses-across-video-audio-and-text-stimuli/") or get_og_image("https://www.cnbc.com/2026/02/24/jpm-ceo-jamie-dimon-ai-reshaping-workforce-redeployment.html")

tech_issue = {
    "date": "2026-03-30",
    "section": "tech",
    "title": {
        "zh": "Meta TRIBE v2 用 AI 预测人脑反应 · JPMorgan「大规模再部署」AI 取代的员工 · Anthropic 考虑今年 IPO · Figma AI Credits 商业化试水",
        "en": "Meta TRIBE v2 Predicts Brain Responses With AI · JPMorgan Mass Redeploys AI-Displaced Workers · Anthropic Eyes IPO · Figma AI Credits Monetization"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul><li><strong>Meta 发布 TRIBE v2：用 AI 预测人脑对任何视觉、声音和语言的反应</strong> — Meta 3 月 26 日发布了 TRIBE v2，一个在 1000+ 小时 fMRI 数据（来自 720+ 受试者）上训练的基础模型。<strong>它能预测人脑对几乎任何视觉、听觉和语言刺激的神经反应。</strong>这不是又一个语言模型——这是 AI 试图理解人类认知本身。潜在应用场景包括：更精准的脑机接口、个性化广告测试（不需要真人受试者）、以及认知障碍的早期诊断。如果 AI 能准确预测你看到某张图时大脑的活动模式，那「了解用户」这件事将从问卷调查进化到神经层面。<br><small>来源：<a href="https://www.marktechpost.com/2026/03/26/meta-releases-tribe-v2-a-brain-encoding-model-that-predicts-fmri-responses-across-video-audio-and-text-stimuli/">MarkTechPost</a></small></li><li><strong>JPMorgan CEO 戴蒙：AI 已在替代员工，银行启动「大规模再部署」</strong> — Jamie Dimon 在投资者会议上坦言：JPMorgan 已经有员工因 AI 被替代，银行正在执行「大规模再部署」计划将他们转移到新岗位。CFO Jeremy Barnum 透露，<strong>JPMorgan 今年生成式 AI 的用例翻了一倍，主要集中在客服和技术部门。</strong>Dimon 的原话值得注意：「表面上看总人数没变，但岗位构成正在发生巨大变化。」这是全球最大银行对 AI 取代白领工作的最直白承认。更令人深思的是 Dimon 的警告：AI 可能让「整个职业消失」，社会需要开始认真思考这个问题。<br><small>来源：<a href="https://www.cnbc.com/2026/02/24/jpm-ceo-jamie-dimon-ai-reshaping-workforce-redeployment.html">CNBC</a></small></li><li><strong>Anthropic 考虑最早 10 月 IPO</strong> — 据 Reddit 上的每日 AI 新闻汇总和多方信源，Claude 的开发商 Anthropic 正在考虑最早于今年 10 月进行 IPO。这将是继 OpenAI 之后，第二家走向公开市场的前沿 AI 实验室。<strong>Anthropic 的 IPO 对行业的信号意义大于商业意义：它意味着「安全优先」的 AI 路线也能获得资本市场的认可。</strong><br><small>来源：<a href="https://www.reddit.com/r/ArtificialInteligence/comments/1s4ut8a/oneminute_daily_ai_news_3262026/">Reddit AI Daily</a></small></li><li><strong>Figma 推出 AI Credits 商业化模式：AI 功能从免费试用进入付费时代</strong> — Figma 在 2025 年为所有座位引入了 AI Credits 机制，3 月起正式调整定价。这意味着 Figma Make 等 AI 功能不再是「无限免费」——用完 Credits 需要额外付费。<strong>Figma 2026 财年收入预期 $13.6-13.7 亿，高于分析师预估的 $12.9 亿，AI 是增长的核心驱动力。</strong>这对设计行业的影响很直接：AI 功能正从「吸引用户」的免费赠品变成「创造收入」的付费产品。<br><small>来源：<a href="https://finance.yahoo.com/news/figmas-next-phase-ai-monetization-154700003.html">Yahoo Finance</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 开始理解人脑</strong>：Meta TRIBE v2 标志着 AI 从模仿人类语言到预测人类认知的跨越</li><li><strong>AI 取代白领已是事实</strong>：JPMorgan 是第一个公开承认并系统应对的巨头</li><li><strong>AI 公司加速商业化</strong>：Anthropic IPO + Figma AI Credits，AI 从烧钱进入赚钱阶段</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>今晚这四条新闻如果用一句话串起来，就是：AI 正在从「做事」进化到「理解人」，而这个转变的经济后果正在快速显现。</strong></p><p>Meta 的 TRIBE v2 是今天最容易被低估的新闻。表面上看，这是一个学术项目——用 fMRI 数据训练模型预测大脑活动。但想想它的含义：<strong>如果 AI 能预测你看到一个界面时大脑的注意力分布，那传统的用户测试、A/B 测试、甚至设计评审的逻辑都要重写。</strong>不需要招募 20 个测试用户花两周做可用性测试——AI 可以在你出稿的瞬间告诉你哪里会被注意、哪里会被忽略、哪里会引发困惑。这和今天早上我们讨论的 Google Stitch 预测性热力图是同一条技术路线，但 TRIBE v2 走得更远——它不是基于统计规律的预测，而是基于真实神经数据的模拟。当然，从实验室到产品还有很长的路，但方向已经很清楚了。</p><p>Jamie Dimon 的「大规模再部署」表态则给出了最真实的经济注脚。注意他的措辞：不是「AI 可能会影响工作」，而是「已经有员工被替代了」。生成式 AI 用例翻倍，客服和技术部门首当其冲。<strong>更深层的信号是 Dimon 说的「表面上总人数没变，但岗位构成正在巨变」——这意味着 AI 对就业的影响不会以大规模裁员的形式出现（那样太难看），而是以「静默重组」的形式发生。</strong>你不会看到「JPMorgan 裁员 5000 人」的标题，你会看到的是：客服团队从 5000 人变成 2000 人+AI，同时「AI 运营」和「AI 治理」岗位新增 500 个。净减少的 2500 个工作岗位被「再部署」这个体面的词汇消化了。Dimon 对社会发出的警告——「整个职业可能消失」——是少见的来自 CEO 的坦诚。</p><p>Anthropic 的 IPO 考量和 Figma 的 AI Credits 商业化则代表了另一个拐点：<strong>AI 行业正在从「烧钱抢用户」过渡到「证明商业模式」。</strong>Anthropic 如果 10 月 IPO，意味着它需要向公开市场证明收入和增长——这必然会影响其产品策略（更多商业化功能、更积极的定价）。Figma 的 AI Credits 则是设计工具行业的第一个明确信号：AI 增强功能不是免费的午餐。当 Figma 预期收入 $13.6-13.7 亿，高于分析师预估 $7 亿时，市场在说：「我们愿意为 AI 设计功能付费。」</p><p>把四条新闻放在一起，2026 年 Q1 的 AI 叙事有了一个清晰的转折：<strong>技术层面从模仿语言到理解认知（TRIBE v2），经济层面从替代蓝领到替代白领（JPMorgan），商业层面从免费到付费（Figma Credits、Anthropic IPO）。</strong>如果你是设计师，你面对的不只是工具变了——整个行业的经济逻辑在变。设计的价值不再由「你能画多少图」衡量，而是由「你能做多少正确的判断」衡量。这和 Figma 报告里那个 25% 的满意度差距，说的是同一件事。</p></div>',
        "en": '<h3>📌 AI × Tech</h3><ul><li><strong>Meta Releases TRIBE v2: AI That Predicts Human Brain Responses</strong> — Meta released TRIBE v2 on March 26, a foundation model trained on 1,000+ hours of fMRI data from 720+ subjects. <strong>It predicts neural responses to virtually any visual, auditory, and language stimuli.</strong> Potential applications: more precise brain-computer interfaces, personalized ad testing without human subjects, and early cognitive disorder diagnosis.<br><small>Source: <a href="https://www.marktechpost.com/2026/03/26/meta-releases-tribe-v2-a-brain-encoding-model-that-predicts-fmri-responses-across-video-audio-and-text-stimuli/">MarkTechPost</a></small></li><li><strong>JPMorgan CEO Dimon: AI Already Displacing Workers, Bank Launches "Massive Redeployment"</strong> — Dimon admitted at investor meeting: employees have already been displaced by AI, with "huge redeployment plans" underway. <strong>Generative AI use cases doubled this year, focused on customer service and tech.</strong> His warning: "entire professions" could disappear, society needs to start thinking about this seriously.<br><small>Source: <a href="https://www.cnbc.com/2026/02/24/jpm-ceo-jamie-dimon-ai-reshaping-workforce-redeployment.html">CNBC</a></small></li><li><strong>Anthropic Considers IPO as Soon as October</strong> — Claude\'s developer is reportedly considering an IPO as early as October 2026. <strong>Signal: the "safety-first" AI approach can also earn capital market validation.</strong><br><small>Source: <a href="https://www.reddit.com/r/ArtificialInteligence/comments/1s4ut8a/oneminute_daily_ai_news_3262026/">Reddit AI Daily</a></small></li><li><strong>Figma AI Credits: AI Features Enter Pay-to-Use Era</strong> — Figma\'s AI Credits pricing adjusts in March. <strong>2026 revenue forecast: $1.36-1.37B, beating analyst estimate of $1.29B, with AI as core growth driver.</strong> AI features transitioning from free acquisition tools to revenue-generating products.<br><small>Source: <a href="https://finance.yahoo.com/news/figmas-next-phase-ai-monetization-154700003.html">Yahoo Finance</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI begins understanding the brain: Meta TRIBE v2 marks leap from mimicking language to predicting cognition</li><li>White-collar AI displacement is reality: JPMorgan is first major institution to openly acknowledge and systematically respond</li><li>AI companies accelerate monetization: Anthropic IPO + Figma AI Credits signal shift from burning cash to proving business models</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Tonight\'s four stories share one thread: AI is evolving from "doing things" to "understanding people," and the economic consequences are materializing fast.</strong> Meta\'s TRIBE v2 is today\'s most underrated news. If AI can predict brain activity when viewing an interface, traditional user testing, A/B testing, and design reviews need rewriting. This aligns with Google Stitch\'s predictive heatmaps but goes further — neural data simulation vs. statistical prediction. JPMorgan\'s "massive redeployment" gives the economic footnote. Note the framing: not "AI might affect jobs" but "employees have already been displaced." The deeper signal: AI\'s employment impact won\'t appear as dramatic layoffs but as "silent restructuring" — teams shrink while AI operations roles grow, with "redeployment" absorbing the net loss. Anthropic\'s IPO consideration and Figma\'s AI Credits represent a turning point: <strong>AI shifts from "burn cash for users" to "prove the business model."</strong> Figma\'s $1.36-1.37B forecast beating estimates by $700M says the market will pay for AI design features. Across all four: <strong>technology moves from mimicking language to understanding cognition (TRIBE v2), economics from blue-collar to white-collar displacement (JPMorgan), business from free to paid (Figma Credits, Anthropic IPO).</strong> Design\'s value is no longer measured by output volume but by judgment quality.</p></div>'
    },
    "cover": tech_cover,
    "sources": tech_sources,
}

# Insert at beginning
issues = [design_issue, tech_issue] + issues

with open(ISSUES_PATH, "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"Done. Total issues: {len(issues)}")
