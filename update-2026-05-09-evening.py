#!/usr/bin/env python3
"""Rex Daily - 2026-05-09 Evening Edition"""
import json, ssl, urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            html = resp.read(50000).decode("utf-8", errors="ignore")
        for tag in ['og:image', 'twitter:image']:
            idx = html.find(f'property="{tag}"')
            if idx == -1:
                idx = html.find(f'name="{tag}"')
            if idx != -1:
                c = html.find('content="', idx)
                if c != -1:
                    c += 9
                    e = html.find('"', c)
                    return html[c:e]
    except Exception:
        pass
    return ""

# Load existing
with open("issues.json", "r") as f:
    issues = json.load(f)

design_issue = {
    "date": "2026-05-09",
    "section": "design",
    "title": {
        "zh": "Figma「State of the Designer 2026」报告揭示反直觉真相：91% 设计师说 AI 提升了设计质量，使用 AI 的设计师满意度高 25%——设计行业正在从「AI 焦虑」转向「AI 赋能」",
        "en": "Figma's State of the Designer 2026 Reveals a Counterintuitive Truth: 91% Say AI Improves Design Quality, AI-Adopters Are 25% More Satisfied — The Industry Shifts from AI Anxiety to AI Empowerment"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Figma 发布「State of the Designer 2026」年度报告：91% 设计师认为 AI 工具提升了设计质量，89% 表示工作效率提高</strong> — Figma 联合独立研究机构 NewtonX 调查了全球 906 名设计师（覆盖北美、亚太、欧洲、拉美、中东），用数据回答了设计行业最核心的焦虑：AI 到底是在帮设计师还是在取代他们？答案令人意外：<strong>积极使用 AI 工具的设计师，工作满意度比不用 AI 的高 25%</strong>。他们更有可能认为自己在驱动业务增长。报告还揭示了一个重要发现——当公司领导层重视设计卓越性（craft）时，设计师的满意度翻倍，团队士气和业务增速同步上升。<br><small>来源：<a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a></small></li><li><strong>Figma 同步发布「设计师招聘趋势报告」：AI 正在驱动设计招聘的新增长</strong> — 与裁员叙事相反，Figma 的最新研究表明 AI 实际上正在推动设计招聘的回暖。报告解释了为什么：当 AI 让非设计师也能生成原型时，<strong>「craft」（视觉精致度、情感化体验、有意识的设计判断）成为产品差异化的核心</strong>——这正是专业设计师不可替代的价值。58% 的设计师将 craft 定义为视觉精致度，35% 定义为情感和愉悦感。<br><small>来源：<a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a> / <a href=\"https://designlab.com/blog/ai-in-ux-product-design-trends-2026\">Designlab</a></small></li><li><strong>Figma 2026 资源库：从 Figma Make 到 Stitch，AI 工具全面渗透 UX 设计全链路</strong> — Figma 更新了 2026 年 AI 工具推荐清单，包括 Figma Make（prompt-to-code）、Figma Design 内置 AI、Uizard、Stitch、UX Pilot 等 9 款工具。<strong>Figma Make 的定位值得注意：它不是「AI 设计工具」，而是「prompt to code anything you can imagine」——直接跳过了设计到开发的传统 handoff 环节。</strong>这意味着 Figma 正在把自己从「设计工具」重新定义为「产品构建平台」。<br><small>来源：<a href=\"https://www.figma.com/resource-library/ai-tools-for-ux-designers/\">Figma Resource Library</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 不是在替代设计师，而是在重新定义「设计师」的含义</strong>：数据显示 AI 使用者更满意、产出更好、更有战略影响力</li><li><strong>「Craft」成为 AI 时代的护城河</strong>：当人人都能用 AI 生成原型时，视觉精致度、情感设计和有意识的判断成为专业设计师的核心价值</li><li><strong>Figma 的野心超越设计工具</strong>：Figma Make + Figma Sites + Figma Buzz = 一个从设计到上线的全栈 AI 产品构建平台</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Figma 这份报告的最大价值不在于那些振奋人心的数字——91% 的设计师说 AI 提升了设计质量，89% 说效率提高了——而在于它揭示了一个被行业叙事掩盖的结构性变化：AI 正在让好的设计师变得更好，同时让平庸的设计师更快地暴露出来。</strong></p><p>让我解释。报告中有一个关键数据：积极使用 AI 的设计师比不用 AI 的满意度高 25%。这不只是「工具让人开心」那么简单。深层逻辑是：<strong>AI 把设计师从重复性执行工作中解放出来后，那些真正有设计判断力的人终于有时间做他们擅长的事——思考用户体验、打磨视觉细节、做战略层面的设计决策。</strong>换句话说，AI 不是在替代设计师的工作，而是在放大设计师的能力差异。一个有十年经验的设计师用 AI 节省的时间会去做更深入的用户研究；一个只会推像素的设计师省下的时间……嗯，他可能只是更快地产出了更多平庸的设计。</p><p>更有意思的是 Figma 关于「craft」的发现。58% 的设计师把 craft 定义为视觉精致度，35% 把它定义为情感和愉悦感。<strong>注意这个分裂：把 craft 和「可见的、可感知的结果」联系在一起的设计师更快乐、更成功；而把 craft 定义为「解决难题」或「做取舍」的设计师相对不快乐。</strong>为什么？因为前者的 craft 是用户和领导能直接感受到的——一个精致的动效、一个让人会心一笑的交互——而后者的 craft 是隐形的。这个发现对设计管理者来说极其重要：<strong>如果你的团队定义的 craft 是「解决隐形的复杂问题」，你需要创造机制让这种贡献被看见，否则你最好的系统思考者会比最好的视觉设计师更容易流失。</strong></p><p>再说 Figma 的战略意图。今天看到的产品矩阵——Figma Design + Figma Make + Figma Sites + Figma Buzz + Figma Draw + Dev Mode——已经不是一个设计工具公司的配置，<strong>这是一个从创意到上线的全栈产品构建平台</strong>。Figma Make 的定位「prompt to code anything you can imagine」直接跳过了传统的设计→开发 handoff。如果这个产品成熟起来，它不只是在革其他设计工具的命，它在革整个前端开发工作流的命。联系今天早上科技板块讨论的 SaaS 替代潮——企业用 AI 替换整个 SaaS 工具栈——Figma 正在做同样的事情，只是从设计侧发起的：<strong>把设计、原型、代码、发布、品牌资产管理全部整合到一个 AI 驱动的平台里，让客户不再需要 Sketch + InVision + Zeplin + Webflow + Canva 这一堆工具。</strong></p><p><strong>最后一个观察。Figma 说「AI 正在驱动设计招聘回暖」，这和科技行业普遍的裁员叙事形成了刺眼的对比。我的判断是：两者都是对的，但描述的是不同层面的现象。被裁掉的是「执行层」的设计岗位——那些主要做 pixel-perfect 还原、套模板、出切图的角色。正在被招聘的是「策略层」的设计岗位——那些能定义体验方向、用 AI 工具加速实现、并用 craft 做差异化的人。这不是设计师数量的变化，是设计师角色分布的重组。对年轻设计师的建议：不要去学如何用 AI 更快地画 UI，去学如何用 AI 更快地理解用户、定义问题、验证假设。执行层的速度 AI 永远比你快，但洞察层的深度 AI 目前还远远不够。</strong></p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Figma Releases State of the Designer 2026: 91% Say AI Improves Design Quality, AI Adopters Are 25% More Satisfied</strong> — Surveying 906 designers globally with NewtonX, Figma answers the industry's core anxiety: is AI helping or replacing designers? The surprising answer: <strong>designers actively using AI are 25% more satisfied</strong> and more likely to feel they're driving business growth. When leadership prioritizes design excellence, satisfaction doubles.<br><small>Source: <a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a></small></li><li><strong>Figma's Design Hiring Report: AI Is Actually Driving Design Hiring Growth</strong> — Counter to layoff narratives, AI is fueling design recruitment. When AI lets anyone generate prototypes, <strong>craft — visual polish, emotional design, intentional judgment — becomes the core differentiator</strong>. 58% define craft as visual polish; 35% as emotion and delight.<br><small>Source: <a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a> / <a href=\"https://designlab.com/blog/ai-in-ux-product-design-trends-2026\">Designlab</a></small></li><li><strong>Figma 2026 AI Tool Stack: From Figma Make to UX Pilot, AI Permeates the Entire UX Pipeline</strong> — Figma's updated toolkit includes Figma Make ('prompt to code anything you can imagine'), built-in AI, Uizard, Stitch, UX Pilot. <strong>Figma Make's positioning skips traditional design-to-dev handoff entirely</strong> — redefining Figma from design tool to product-building platform.<br><small>Source: <a href=\"https://www.figma.com/resource-library/ai-tools-for-ux-designers/\">Figma Resource Library</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI isn't replacing designers — it's redefining what 'designer' means</strong>: Data shows AI users are happier, produce better work, and have more strategic impact</li><li><strong>Craft as AI-era moat</strong>: When everyone can AI-generate prototypes, visual polish, emotional design, and intentional judgment become professional designers' core value</li><li><strong>Figma's ambition transcends design tools</strong>: Make + Sites + Buzz = a full-stack AI product-building platform from concept to launch</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>The real value of Figma's report isn't the uplifting numbers — 91% say AI improves quality, 89% say efficiency is up — it's revealing a structural change hidden by industry narratives: AI is making good designers better while faster exposing mediocre ones.</strong></p><p>The key data point: AI-active designers are 25% more satisfied. The deeper logic: <strong>AI frees designers from repetitive execution, giving those with genuine design judgment time to do what they excel at — user research, visual refinement, strategic design decisions.</strong> A 10-year veteran uses saved time for deeper user research; a pixel-pusher just produces mediocre designs faster.</p><p>The craft finding is fascinating. 58% define craft as visual polish; 35% as emotion and delight. <strong>Designers who tie craft to visible, perceivable outcomes are happier and more successful; those who define it as 'solving hard problems' are relatively less so.</strong> Why? Because the former's craft is seen by users and leaders — a polished animation, a smile-inducing interaction — while the latter's is invisible. For design managers: <strong>if your team defines craft as 'solving invisible complexity,' you need mechanisms to make that contribution visible, or your best systems thinkers will churn faster than your best visual designers.</strong></p><p>Figma's strategic intent is clear. Today's product matrix — Design + Make + Sites + Buzz + Draw + Dev Mode — isn't a design tool company's lineup. <strong>It's a full-stack product-building platform from concept to launch.</strong> Figma Make's 'prompt to code' positioning directly bypasses traditional design-dev handoff. Connected to this morning's SaaS replacement wave discussion: <strong>Figma is consolidating the entire Sketch + InVision + Zeplin + Webflow + Canva stack into one AI-powered platform.</strong></p><p><strong>Final observation: Figma says 'AI is driving design hiring growth' — contrasting sharply with tech's layoff narrative. Both are true but describe different layers. Execution-layer design roles (pixel-perfect reproduction, template application) are being cut. Strategy-layer roles (defining experience direction, using AI to accelerate, differentiating through craft) are being hired. This isn't a change in designer quantity — it's a redistribution of designer roles. Young designers: don't learn to draw UI faster with AI. Learn to understand users, define problems, and validate hypotheses faster with AI. AI will always beat you at execution speed, but insight depth is where AI still falls far short.</strong></p></div>"
    },
    "cover": "",
    "sources": [
        {
            "url": "https://www.figma.com/blog/state-of-the-designer-2026/",
            "title": {
                "zh": "Figma「State of the Designer 2026」：设计师正在拥抱 AI 时代的不确定性",
                "en": "Figma State of the Designer 2026: Designers Are Leaning Into the Messy Middle"
            },
            "image": ""
        },
        {
            "url": "https://designlab.com/blog/ai-in-ux-product-design-trends-2026",
            "title": {
                "zh": "Designlab：2026 年 UX 与产品设计中的 AI 趋势",
                "en": "Designlab: The State of AI in UX & Product Design 2026"
            },
            "image": ""
        },
        {
            "url": "https://www.figma.com/resource-library/ai-tools-for-ux-designers/",
            "title": {
                "zh": "Figma 2026 年 UX 设计师 AI 工具推荐",
                "en": "Figma: Top AI Tools for UX Designers in 2026"
            },
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-05-09",
    "section": "tech",
    "title": {
        "zh": "Anthropic 给 Claude Agent 加了「做梦」功能 + Trump 政府因 Mythos 吓一跳后突然支持 AI 安全测试 + Microsoft AI 数据中心与清洁能源目标冲突——当 AI 开始自我进化，监管和基建同时告急",
        "en": "Anthropic Adds 'Dreaming' to Claude Agents + Trump's Mythos Scare Triggers AI Safety Testing U-Turn + Microsoft's AI Data Centers Clash with Clean Energy Goals — As AI Self-Evolves, Regulation and Infrastructure Scramble to Keep Up"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Anthropic 为 Claude Managed Agents 增加「做梦」（Dreaming）功能：AI Agent 现在可以在闲置时自我反思和优化</strong> — SD Times 报道（5月6日），Anthropic 为 Claude Managed Agents 推出三大更新：<strong>Dreaming（做梦）</strong>——Agent 在非活跃时段回顾历史 session、发现模式、自我改进；<strong>Outcomes（结果追踪）</strong>——量化 Agent 的实际工作成效；以及<strong>Multiagent Orchestration（多 Agent 编排）</strong>——让多个 Agent 协作完成复杂任务。Dreaming 是最有意思的：它借鉴了人类睡眠中大脑整理记忆的机制，让 AI Agent 在「空闲时间」主动学习和进化。<br><small>来源：<a href=\"https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/\">SD Times</a></small></li><li><strong>Trump 政府因「Mythos」事件突然转向支持 AI 安全测试：Ars Technica 深度分析为何一个 AI 模型让白宫改变了立场</strong> — Ars Technica 报道（5月6-7日），此前一直主张「减少 AI 监管」的 Trump 政府在一个名为「Mythos」的前沿 AI 模型暴露安全风险后，突然开始积极推动 AI 预发布安全测试。专家们分析了这种政策转向可能出错的所有方式：<strong>测试标准是否足够严格、测试是否会成为大公司的竞争壁垒、以及政府是否有技术能力真正评估前沿 AI 的风险。</strong>文章指出，Google、Microsoft、xAI 已经「自愿」接受审查，但这种自愿的可信度取决于审查的独立性。<br><small>来源：<a href=\"https://arstechnica.com/tech-policy/2026/05/everything-that-could-go-wrong-with-trumps-ai-safety-tests-according-to-experts/\">Ars Technica</a></small></li><li><strong>Microsoft AI 数据中心扩张与清洁能源目标发生正面冲突：TechCrunch 揭示 AI 基础设施的能源悖论</strong> — TechCrunch 报道（5月6日），Microsoft 为了支撑 AI 工作负载而大规模扩建数据中心，但这些数据中心的能耗正在与公司 2030 年碳负排放的承诺产生不可调和的矛盾。<strong>AI 训练和推理的电力需求增长速度远超可再生能源的部署速度</strong>——这不只是 Microsoft 的问题，整个 AI 行业都面临同样的困境。<br><small>来源：<a href=\"https://techcrunch.com/2026/05/06/microsofts-ai-data-center-push-is-colliding-with-its-clean-power-goals/\">TechCrunch</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI Agent 开始「自我进化」</strong>：Anthropic 的 Dreaming 功能标志着 AI 从「被动响应」到「主动学习」的范式转变</li><li><strong>AI 安全监管从「阻碍创新」变成「政治必需品」</strong>：当一个 AI 模型能吓到白宫时，安全测试就不再是可选项</li><li><strong>AI 基础设施遭遇物理世界瓶颈</strong>：算力需求 vs 能源供给 = AI 行业未来 5 年最大的结构性制约</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天这三条新闻看似各自独立，但它们共同指向一个事实：AI 的发展速度已经开始超过人类社会的适应速度——不是在技术层面，而是在制度、基础设施和认知层面。</strong></p><p>先说 Anthropic 的 Dreaming。这个功能的名字起得很巧妙，但它的含义比「给 AI 做梦」深刻得多。<strong>传统的 AI Agent 是「任务驱动」的——你给它一个指令，它执行，完了就停。Dreaming 让 Agent 在没有人类指令的情况下主动回顾过去的工作、发现模式、优化自己。</strong>这是一个从「工具」到「自主体」的微妙但重要的转变。想象一下：你的 AI 助手白天帮你处理邮件、安排会议，晚上它在「做梦」——回顾今天哪些回复效果好、哪些任务处理得低效、明天怎么做得更好。这听起来很有用，但它也意味着 AI 开始拥有一种形式的「经验」和「记忆」——不是人类那种记忆，但功能上是相似的。联系 Multiagent Orchestration——多个这样的「会做梦的 Agent」协作完成任务——你开始看到一个模糊的轮廓：<strong>AI 系统正在从「单兵工具」进化为「有记忆的协作组织」。</strong>这不是 AGI，但它比大多数人意识到的更接近我们对「智能」的直觉理解。</p><p>Trump 政府的 180 度转弯是今天最具黑色幽默的新闻。一个「让美国在 AI 上不受监管束缚」的政府，被一个 AI 模型（Mythos）的安全风险吓到后突然开始推动安全测试——<strong>这不是深思熟虑的政策制定，这是恐慌驱动的反应。</strong>Ars Technica 的专家分析指出了所有可能出错的地方，但我认为最核心的问题是：<strong>政府有能力审查前沿 AI 吗？</strong>这些模型的复杂度已经超过了大多数政府机构的技术理解能力。如果审查只是走流程——公司提交报告，政府盖章通过——那它不过是「安全剧场」。真正有意义的审查需要独立的技术团队、充足的计算资源、以及不受商业利益影响的判断力。目前没有任何一个政府机构具备这三个条件。这意味着短期内 AI 安全审查更可能是一种政治信号而非真正的技术保障。</p><p><strong>最后说 Microsoft 的能源困境。这是 AI 行业所有华丽叙事背后最不性感但最真实的限制：物理定律。AI 模型越大、训练越多、推理越频繁，耗电越多。Microsoft 2030 年碳负排放的承诺在 AI 数据中心的电表面前显得苍白无力。这不只是 ESG 报告上的数字问题——如果 AI 的电力需求超过电网的供应能力，那再强大的模型也运行不了。把今天三条新闻连起来看：AI Agent 在学习自我进化（Dreaming），政府在仓促地建立监管框架（Mythos），而整个系统的物理基础（电力）正在成为瓶颈。如果 2025 年的故事是「谁的模型更聪明」，2026 年的故事正在变成「谁能让聪明的模型在现实世界中持续、安全、负责任地运行」。这个问题比 benchmark 分数无聊得多，但重要一万倍。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Anthropic Adds 'Dreaming' to Claude Managed Agents: AI Agents Now Self-Reflect and Optimize During Idle Time</strong> — SD Times reports (May 6) Anthropic launched three updates: <strong>Dreaming</strong> — agents review past sessions during downtime to find patterns and self-improve; <strong>Outcomes</strong> — quantifying agent work effectiveness; and <strong>Multiagent Orchestration</strong> — coordinating multiple agents on complex tasks. Dreaming borrows from how human brains consolidate memories during sleep.<br><small>Source: <a href=\"https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/\">SD Times</a></small></li><li><strong>Trump Administration's Mythos Scare Triggers AI Safety Testing U-Turn: Ars Technica Analyzes the Policy Reversal</strong> — After a frontier model called 'Mythos' exposed safety risks, the previously anti-regulation Trump administration suddenly embraced pre-release AI safety testing. Experts analyze what could go wrong: <strong>test rigor, competitive barriers for startups, and whether government has the technical capability to evaluate frontier AI risks.</strong><br><small>Source: <a href=\"https://arstechnica.com/tech-policy/2026/05/everything-that-could-go-wrong-with-trumps-ai-safety-tests-according-to-experts/\">Ars Technica</a></small></li><li><strong>Microsoft's AI Data Center Expansion Collides with Clean Energy Goals</strong> — TechCrunch reports (May 6) that Microsoft's massive data center buildout for AI workloads is creating irreconcilable tension with its 2030 carbon-negative pledge. <strong>AI power demand is growing faster than renewable energy deployment</strong> — an industry-wide dilemma.<br><small>Source: <a href=\"https://techcrunch.com/2026/05/06/microsofts-ai-data-center-push-is-colliding-with-its-clean-power-goals/\">TechCrunch</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Agents Begin 'Self-Evolution'</strong>: Anthropic's Dreaming marks a paradigm shift from reactive response to proactive learning</li><li><strong>AI Safety Regulation: From Innovation Barrier to Political Necessity</strong>: When an AI model scares the White House, safety testing stops being optional</li><li><strong>AI Infrastructure Hits Physical-World Bottleneck</strong>: Compute demand vs energy supply = AI industry's biggest structural constraint for the next 5 years</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>These three stories seem independent but point to one fact: AI development speed now exceeds human society's adaptation speed — not technologically, but institutionally, infrastructurally, and cognitively.</strong></p><p>Dreaming is more profound than 'letting AI dream.' <strong>Traditional agents are task-driven: receive instruction, execute, stop. Dreaming lets agents proactively review past work, discover patterns, and optimize themselves without human instruction.</strong> This is a subtle but important shift from 'tool' to 'autonomous entity.' Combined with Multiagent Orchestration — multiple 'dreaming agents' collaborating — <strong>AI systems are evolving from 'individual tools' to 'organizations with memory.'</strong> Not AGI, but closer to our intuitive understanding of 'intelligence' than most realize.</p><p>Trump's 180-degree turn is darkly humorous. A government dedicated to 'freeing AI from regulatory shackles' got scared by one model (Mythos) and suddenly embraced safety testing — <strong>this isn't deliberate policy-making, it's panic-driven reaction.</strong> The core question: <strong>can government actually review frontier AI?</strong> Model complexity exceeds most government agencies' technical comprehension. Without independent technical teams, sufficient compute, and judgment free from commercial interests, AI safety review becomes 'security theater.'</p><p><strong>Microsoft's energy dilemma is the least glamorous but most real constraint behind AI's dazzling narratives: physics. Bigger models, more training, more inference = more power. Microsoft's 2030 carbon-negative pledge looks pale next to AI data center electricity meters. Connecting all three: AI agents are learning self-evolution (Dreaming), governments are hastily building regulatory frameworks (Mythos), and the physical foundation (power) is becoming a bottleneck. If 2025's story was 'whose model is smarter,' 2026's is becoming 'who can make smart models run sustainably, safely, and responsibly in the real world.' Far less exciting than benchmark scores, but ten thousand times more important.</strong></p></div>"
    },
    "cover": "",
    "sources": [
        {
            "url": "https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/",
            "title": {
                "zh": "Anthropic 为 Claude Managed Agents 新增「做梦」、结果追踪和多 Agent 编排功能",
                "en": "New in Claude Managed Agents: Dreaming, Outcomes, and Multiagent Orchestration"
            },
            "image": ""
        },
        {
            "url": "https://arstechnica.com/tech-policy/2026/05/everything-that-could-go-wrong-with-trumps-ai-safety-tests-according-to-experts/",
            "title": {
                "zh": "Ars Technica：Trump 政府 AI 安全测试的所有潜在问题",
                "en": "Ars Technica: Everything That Could Go Wrong with Trump's AI Safety Tests"
            },
            "image": ""
        },
        {
            "url": "https://techcrunch.com/2026/05/06/microsofts-ai-data-center-push-is-colliding-with-its-clean-power-goals/",
            "title": {
                "zh": "TechCrunch：Microsoft AI 数据中心扩张与清洁能源目标冲突",
                "en": "TechCrunch: Microsoft's AI Data Center Push Is Colliding with Its Clean Power Goals"
            },
            "image": ""
        }
    ]
}

# Fetch og:images
for issue in [design_issue, tech_issue]:
    for src in issue["sources"]:
        img = get_og_image(src["url"])
        if img:
            src["image"] = img
            if not issue["cover"]:
                issue["cover"] = img

# Insert at front
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("Done! Added 2 evening issues for 2026-05-09")
