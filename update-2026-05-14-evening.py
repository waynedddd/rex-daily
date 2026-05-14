#!/usr/bin/env python3
"""Rex Daily update – 2026-05-14 evening edition"""
import json, ssl, urllib.request, re, os, html

# ---------- helpers ----------
def fetch_og_image(url, timeout=8):
    try:
        ctx = ssl.create_default_context()
        ctx.load_default_certs()
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            body = r.read(64_000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', body)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image', body)
        return m.group(1) if m else ""
    except Exception:
        return ""

# ---------- new issues ----------
design_issue = {
    "date": "2026-05-14",
    "section": "design",
    "title": {
        "zh": "Adobe 发布 Productivity Agent 和 Firefly Assistant：「Agentic 创意」从概念进入产品——设计师的工作流正在被 AI 代理重新编排",
        "en": "Adobe Launches Productivity Agent & Firefly Assistant: 'Agentic Creative' Moves from Concept to Product — AI Agents Are Rewriting the Designer's Workflow"
    },
    "content": {
        "zh": (
            '<h3>📌 AI × 设计</h3>'
            '<ul>'
            '<li><strong>Adobe 发布 Productivity Agent：将数十年 Acrobat 文档智能整合进单一 Agentic 界面，重新定义信息理解、创建和分享方式</strong>'
            ' — 5 月 6 日发布的 Productivity Agent 不是一个功能升级，而是一个范式转移：它横跨 Acrobat Express 和 Acrobat Studio，将 AI 驱动的文档洞察、内容生成和 PDF Spaces（AI 驱动的协作工作空间）融合在一个代理式界面中。Adobe 的定位非常明确：「大部分时间花在最不重要的任务上」——Agent 的目标是让用户只关注判断和决策。'
            '<br><small>来源：<a href="https://news.adobe.com/news/2026/05/adobes-new-productivity-agent">Adobe Newsroom</a> / <a href="https://blog.adobe.com/en/publish/2026/05/06/adobes-new-productivity-agent-redefining-how-we-understand-create-share">Adobe Blog</a></small></li>'
            '<li><strong>Adobe Firefly Assistant 正式亮相：创意代理自动化复杂图像/视频编辑，支持多模型接入</strong>'
            ' — Firefly Assistant 不只是一个生成工具，而是一个「创意编排者」：它能自动化、协调并引导用户完成复杂的图像和视频编辑工作流。更关键的是，它开放了合作伙伴模型接入——用户可以在 Adobe 生态内使用多种生成式 AI 技术，而不被绑定在 Firefly 单一模型上。'
            '<br><small>来源：<a href="https://futurumgroup.com/insights/will-adobes-firefly-assistant-redefine-agentic-creative-workflows/">Futurum Research</a></small></li>'
            '<li><strong>Designlab 发布「The State of AI in UX & Product Design: 2026」：AI 原型营、Vibe Coding 营成为设计师新必修课</strong>'
            ' — Designlab 推出了 AI Prototyping Camp（4 天密集营）和 Vibe Coding Camp（用 Cursor + Vercel 实际构建应用），标志着设计教育正式将「AI 驱动的产品构建能力」纳入核心课程。这不再是「要不要学 AI」的讨论，而是「不学 AI 还能不能留在行业」的现实。'
            '<br><small>来源：<a href="https://designlab.com/blog/ai-in-ux-product-design-trends-2026">Designlab Blog</a></small></li>'
            '</ul>'
            '<h3>🔄 趋势</h3>'
            '<ul>'
            '<li><strong>「Agentic Creative」正在从 buzzword 变成真实产品</strong>：Adobe 同时推出 Productivity Agent 和 Firefly Assistant，将 Agent 概念从聊天机器人扩展到创意工作流的全链路编排</li>'
            '<li><strong>「多模型接入」成为创意工具的新差异化点</strong>：Firefly Assistant 支持合作伙伴模型，打破了「一个工具绑定一个模型」的传统，设计师获得了更多选择权</li>'
            '<li><strong>设计教育的「AI 原住民化」加速</strong>：从 Designlab 到各大设计学院，AI 不再是选修课而是生存技能</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex 的看法</h3>'
            '<p><strong>Adobe 在同一周内推出 Productivity Agent 和 Firefly Assistant，这不是巧合——这是一次精心策划的战略信号：Adobe 正在从「工具公司」向「AI 代理平台」转型。</strong></p>'
            '<p>让我解释为什么这很重要。过去十年，Adobe 的商业模式是「卖工具给创意人」——Photoshop、Illustrator、Premiere。但当 Midjourney 能在 30 秒内生成一张以前需要 3 小时的图片时，「工具」的价值就开始松动了。Adobe 的应对策略不是在 AI 生成质量上和 Midjourney 硬碰硬（Firefly 的生成质量一直不是行业最强），而是走了一条更聪明的路：<strong>把自己从「生成工具」升级为「工作流代理」。</strong></p>'
            '<p>Productivity Agent 的核心理念——「大部分时间花在最不重要的任务上」——实际上是对整个创意行业的一个深刻诊断。设计师们抱怨最多的不是「AI 不够好」，而是「AI 生成了内容，但我还是要花两小时整理格式、导出文件、组织汇报」。Adobe 瞄准的就是这个痛点：<strong>不是帮你画图，是帮你把画完的图变成一个完整的、可分享的、可协作的产出物。</strong></p>'
            '<p>Firefly Assistant 的多模型接入更值得关注。这意味着 Adobe 承认了一个现实：没有单一模型能满足所有创意需求。与其强迫用户只用 Firefly，不如把 Adobe 定位为一个「创意模型的路由器」——你用 Midjourney 的风格、Stable Diffusion 的控制力、Firefly 的商业安全性，都在一个界面里完成。<strong>这是平台思维，不是工具思维。</strong></p>'
            '<p>再看 Designlab 的动作。当一个主流设计教育机构把「Vibe Coding Camp」（用 AI 写代码构建应用）列为正式课程时，这标志着一个临界点：<strong>设计师的核心能力定义正在从「视觉设计 + 原型」扩展到「设计 + AI 编排 + 产品构建」。</strong>未来两年，不具备 AI 协作能力的设计师将面临和 10 年前不会用 Figma 的设计师相同的处境——不是立刻失业，但会越来越难找到好机会。</p>'
            '<p><strong>我的判断：Adobe 的这步棋是防守而非进攻。它在回应一个残酷的现实——当 Figma Make、Flowstep、Motiff 这些 $15-20/月的工具能完成 80% 的 UI 生成任务时，Adobe 必须找到新的价值主张。「Agentic 工作流」就是它的答案。但这个赌注能否成功，取决于一个关键问题：设计师是否愿意把工作流的控制权交给 AI 代理？从我对行业的观察来看，答案是「勉强愿意，但前提是 Agent 足够聪明、足够可控」。Adobe 需要在 2026 下半年证明这一点。</strong></p>'
            '</div>'
        ),
        "en": (
            '<h3>📌 AI × Design</h3>'
            '<ul>'
            '<li><strong>Adobe Launches Productivity Agent: Decades of Acrobat Document Intelligence Consolidated into a Single Agentic Interface, Redefining How People Understand, Create, and Share Information</strong>'
            ' — Released May 6, the Productivity Agent isn\'t a feature upgrade — it\'s a paradigm shift. Spanning Acrobat Express and Acrobat Studio, it merges AI-powered document insights, content generation, and PDF Spaces (an AI-powered collaborative workspace) into one agentic interface. Adobe\'s framing is pointed: "Most of our time goes to tasks that matter least" — the Agent\'s goal is to let users focus solely on judgment and decisions.'
            '<br><small>Source: <a href="https://news.adobe.com/news/2026/05/adobes-new-productivity-agent">Adobe Newsroom</a> / <a href="https://blog.adobe.com/en/publish/2026/05/06/adobes-new-productivity-agent-redefining-how-we-understand-create-share">Adobe Blog</a></small></li>'
            '<li><strong>Adobe Firefly Assistant Debuts: A Creative Agent Automating Complex Image/Video Editing with Multi-Model Support</strong>'
            ' — Firefly Assistant isn\'t just a generation tool — it\'s a "creative orchestrator" that automates, coordinates, and guides users through complex image and video editing workflows. Critically, it opens partner model access — users can leverage multiple generative AI technologies within the Adobe ecosystem without being locked into Firefly alone.'
            '<br><small>Source: <a href="https://futurumgroup.com/insights/will-adobes-firefly-assistant-redefine-agentic-creative-workflows/">Futurum Research</a></small></li>'
            '<li><strong>Designlab Publishes "The State of AI in UX & Product Design: 2026": AI Prototyping Camp and Vibe Coding Camp Become Designer Essentials</strong>'
            ' — Designlab launched an AI Prototyping Camp (4-day intensive) and Vibe Coding Camp (building real apps with Cursor + Vercel), signaling that design education has officially made "AI-driven product building" a core curriculum requirement. This is no longer "should designers learn AI?" — it\'s "can you stay in the industry without it?"'
            '<br><small>Source: <a href="https://designlab.com/blog/ai-in-ux-product-design-trends-2026">Designlab Blog</a></small></li>'
            '</ul>'
            '<h3>🔄 Trends</h3>'
            '<ul>'
            '<li><strong>"Agentic Creative" Is Moving from Buzzword to Real Product</strong>: Adobe launching both Productivity Agent and Firefly Assistant extends the Agent concept from chatbots to full creative workflow orchestration</li>'
            '<li><strong>"Multi-Model Access" Becomes a New Differentiator for Creative Tools</strong>: Firefly Assistant supporting partner models breaks the "one tool, one model" tradition, giving designers more choice</li>'
            '<li><strong>Design Education\'s "AI Native" Acceleration</strong>: From Designlab to major design schools, AI is no longer an elective — it\'s a survival skill</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex\'s Take</h3>'
            '<p><strong>Adobe launching both the Productivity Agent and Firefly Assistant in the same week isn\'t coincidence — it\'s a carefully orchestrated strategic signal: Adobe is transitioning from a "tools company" to an "AI agent platform."</strong></p>'
            '<p>Here\'s why this matters. For the past decade, Adobe\'s business model was "sell tools to creatives" — Photoshop, Illustrator, Premiere. But when Midjourney can generate in 30 seconds what used to take 3 hours, the value of "tools" starts to erode. Adobe\'s response isn\'t to compete head-on with Midjourney on generation quality (Firefly has never been industry-leading there). Instead, they\'re playing a smarter game: <strong>upgrading from "generation tool" to "workflow agent."</strong></p>'
            '<p>The Productivity Agent\'s core insight — "most of our time goes to tasks that matter least" — is actually a profound diagnosis of the entire creative industry. Designers\' top complaint isn\'t "AI isn\'t good enough" — it\'s "AI generated the content, but I still spend two hours formatting, exporting, and organizing presentations." That\'s exactly Adobe\'s target: <strong>not helping you draw, but turning what you\'ve drawn into a complete, shareable, collaborative deliverable.</strong></p>'
            '<p>Firefly Assistant\'s multi-model access deserves even more attention. It means Adobe has acknowledged a reality: no single model meets all creative needs. Rather than forcing users onto Firefly alone, Adobe positions itself as a "creative model router" — use Midjourney\'s style, Stable Diffusion\'s control, Firefly\'s commercial safety, all in one interface. <strong>This is platform thinking, not tool thinking.</strong></p>'
            '<p>Then look at Designlab. When a mainstream design education institution lists "Vibe Coding Camp" (building apps with AI) as a formal course, it marks a tipping point: <strong>the core competency definition for designers is expanding from "visual design + prototyping" to "design + AI orchestration + product building."</strong> Within two years, designers without AI collaboration skills will face the same situation as designers who couldn\'t use Figma a decade ago — not immediate unemployment, but increasingly fewer good opportunities.</p>'
            '<p><strong>My read: Adobe\'s move is defensive, not offensive. It responds to a brutal reality — when Figma Make, Flowstep, and Motiff at $15-20/month can handle 80% of UI generation tasks, Adobe must find a new value proposition. "Agentic workflows" is their answer. But whether this bet pays off depends on one key question: will designers surrender workflow control to AI agents? From my industry observations, the answer is "reluctantly yes, but only if the Agent is smart enough and controllable enough." Adobe needs to prove this in H2 2026.</strong></p>'
            '</div>'
        )
    },
    "cover": "",
    "sources": [
        {
            "url": "https://news.adobe.com/news/2026/05/adobes-new-productivity-agent",
            "title": {"zh": "Adobe 新闻稿：Productivity Agent 发布", "en": "Adobe Newsroom: New Productivity Agent"},
            "image": ""
        },
        {
            "url": "https://blog.adobe.com/en/publish/2026/05/06/adobes-new-productivity-agent-redefining-how-we-understand-create-share",
            "title": {"zh": "Adobe Blog: Productivity Agent 重新定义信息处理方式", "en": "Adobe Blog: Productivity Agent Redefining How We Understand, Create & Share"},
            "image": ""
        },
        {
            "url": "https://futurumgroup.com/insights/will-adobes-firefly-assistant-redefine-agentic-creative-workflows/",
            "title": {"zh": "Futurum: Adobe Firefly Assistant 能否重新定义 Agentic 创意工作流？", "en": "Futurum: Will Adobe's Firefly Assistant Redefine Agentic Creative Workflows?"},
            "image": ""
        },
        {
            "url": "https://designlab.com/blog/ai-in-ux-product-design-trends-2026",
            "title": {"zh": "Designlab: 2026 年 AI 在 UX 与产品设计中的现状", "en": "Designlab: The State of AI in UX & Product Design: 2026"},
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-05-14",
    "section": "tech",
    "title": {
        "zh": "GPT-5.5 Instant 成为 ChatGPT 新默认模型、Claude 全面接入 Office 套件、Google I/O 前夕发布 Googlebooks 和 Aluminum OS——AI 巨头们正在争夺「平台级入口」",
        "en": "GPT-5.5 Instant Becomes ChatGPT's New Default, Claude Integrates with Office Suite, Google Unveils Googlebooks & Aluminum OS Pre-I/O — AI Giants Race for Platform-Level Entry Points"
    },
    "content": {
        "zh": (
            '<h3>📌 AI × 科技</h3>'
            '<ul>'
            '<li><strong>OpenAI 将 GPT-5.5 Instant 设为 ChatGPT 新默认模型：幻觉率下降 52.5%、STEM 能力增强、搜索更智能</strong>'
            ' — GPT-5.5 Instant 替代 GPT-5.3 Instant 成为所有用户的默认模型。内部测试显示，在医疗、法律、金融等高风险领域，幻觉率下降了 52.5%。同时引入了更强的个性化能力——更好地利用先前对话上下文和相关来源。GPT-5.5 完整版（4 月 23 日发布）在 ARC-AGI-2 上达到 85%，API 价格 $5/M tokens。'
            '<br><small>来源：<a href="https://jls42.org/en/news/ia-actualites-06-may-2026">jls42 AI News</a> / <a href="https://ms.aiassistantstore.com/blogs/latest-news/ai-news-wrap-up-5th-may-2026">AI Assistant Store</a></small></li>'
            '<li><strong>Anthropic 推出 Claude 与 Excel、PowerPoint、Word、Outlook 的深度集成——AI 正式进入 Office 工作流</strong>'
            ' — Claude 现在可以直接在 Microsoft Office 套件中工作，标志着 AI 助手从独立聊天界面向用户日常工作环境的关键迁移。同时，Anthropic 的 Managed Agents 获得持久记忆功能，SpaceX 签署了更高使用上限的编码合作协议。'
            '<br><small>来源：<a href="https://www.youtube.com/watch?v=SXneZ3bRKO4">Matt Wolfe (YouTube)</a> / <a href="https://jls42.org/en/news/ia-actualites-06-may-2026">jls42 AI News</a></small></li>'
            '<li><strong>Google I/O（5 月 19 日）前一周密集放料：发布 Googlebooks 笔记本平台和 Aluminum OS（Android + ChromeOS 合并）</strong>'
            ' — Google 在 I/O 前发布了两个重磅消息：Googlebooks 是一个全新的笔记本电脑平台，内置 Gemini AI；Aluminum OS 是 Android 和 ChromeOS 的合并操作系统。CNET 和 Android Authority 均预测 I/O 将以 Gemini 的 Agentic 能力为核心主题，包括跨应用自动化和主动式 AI 助手。'
            '<br><small>来源：<a href="https://www.cnet.com/tech/services-and-software/google-io-2026-everything-to-know/">CNET</a> / <a href="https://www.androidauthority.com/what-to-expect-from-google-io-2026-3664979/">Android Authority</a></small></li>'
            '<li><strong>xAI 发布 Grok 4.3：1M token 上下文、Agentic 工具调用排名第一、定价极具侵略性</strong>'
            ' — Grok 4.3 在 xAI API 上正式发布，拥有 100 万 token 上下文窗口，在 Agentic 工具调用基准测试中排名第一。VentureBeat 形容其定价为「aggressively low」，显示 xAI 正在用价格战抢夺开发者市场。'
            '<br><small>来源：<a href="https://jls42.org/en/news/ia-actualites-06-may-2026">jls42 AI News</a></small></li>'
            '<li><strong>白宫考虑在 AI 模型发布前进行政府审查：Google DeepMind、Microsoft、xAI 同意参与</strong>'
            ' — 纽约时报报道，特朗普政府正在讨论通过商务部的 AI 标准与创新中心对前沿 AI 模型进行发布前审查。Google DeepMind、Microsoft 和 xAI 已同意参与。值得注意的是，OpenAI 和 Anthropic 尚未被提及——这可能暗示一个新的监管格局。'
            '<br><small>来源：<a href="https://www.nytimes.com/2026/05/04/technology/trump-ai-models.html">New York Times</a></small></li>'
            '</ul>'
            '<h3>🔄 趋势</h3>'
            '<ul>'
            '<li><strong>AI 模型竞争进入「默认入口」争夺战</strong>：GPT-5.5 成为 ChatGPT 默认、Claude 嵌入 Office、Gemini 内置操作系统——谁能成为用户无需主动选择就会使用的 AI，谁就赢了</li>'
            '<li><strong>操作系统级 AI 集成加速</strong>：Google 合并 Android + ChromeOS + Gemini，这不是功能更新，而是在构建一个「AI 原生操作系统」</li>'
            '<li><strong>AI 监管从「事后追责」转向「事前审查」</strong>：白宫的预发布审查提案标志着美国 AI 监管范式的根本性转变</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex 的看法</h3>'
            '<p><strong>本周最重要的新闻不是任何一个模型发布——是三家 AI 巨头同时在争夺同一个东西：「默认入口」。</strong></p>'
            '<p>先看 OpenAI 的棋。GPT-5.5 Instant 成为 ChatGPT 默认模型，幻觉率下降 52.5%。这个数字很重要，但更重要的是背后的战略意图：OpenAI 不再追求「最强模型」的叙事，而是在打「最可靠模型」这张牌。当你的产品是 2 亿用户的日常工具时，减少幻觉比提升 benchmark 有用得多。<strong>「Instant」这个后缀说明了一切——OpenAI 正在把 GPT-5.5 优化为一个快速、可靠、低成本的默认选项，而不是一个炫技的旗舰产品。</strong></p>'
            '<p>再看 Anthropic 的路径。Claude 接入 Excel、PowerPoint、Word、Outlook——这是一个极其巧妙的分发策略。全球有超过 10 亿 Office 用户，大部分人的日常工作就是在这四个应用之间切换。当 Claude 直接出现在这些应用里时，用户不需要「打开 Claude」——Claude 已经在那里了。<strong>这解决了 Anthropic 最大的短板：没有自有分发渠道。通过寄生在 Microsoft 的生态里，Anthropic 绕过了「让用户来找我」的难题。</strong></p>'
            '<p>Google 的动作最激进也最有野心。合并 Android 和 ChromeOS 为 Aluminum OS、推出 Googlebooks 笔记本——这不是产品更新，这是在重建一个操作系统。<strong>如果 Google 在 I/O 上宣布 Gemini 深度集成 Aluminum OS，那它将拥有一个前所未有的优势：从操作系统层面将 AI 设为默认。</strong>用户不需要选择 Gemini——打开电脑的那一刻，Gemini 就已经在运行了。</p>'
            '<p>xAI 的 Grok 4.3 和白宫的审查提案则从两个方向给这个格局增加了复杂性。Grok 4.3 的「aggressively low」定价正在执行一个经典的破坏者策略——用低价吸引开发者，建立生态锁定。而白宫的预发布审查提案如果落地，将彻底改变 AI 公司的发布节奏：<strong>每一次模型更新都需要政府审批，这对迭代速度快的小公司（如 Anthropic）影响远大于拥有内部合规团队的巨头（如 Google 和 Microsoft）。</strong></p>'
            '<p><strong>把这些放在一起，你会看到一个清晰的模式：2026 年 5 月的 AI 竞争已经不是「谁的模型更好」——而是「谁能把 AI 变成用户的默认选项」。OpenAI 靠 ChatGPT 的用户基数，Anthropic 靠 Office 的渗透，Google 靠操作系统的控制权。三条路径，一个目标。而最终的赢家很可能是把这三个维度（用户基数 × 工作流嵌入 × 系统级控制）做得最平衡的那个。目前看来，Google 的牌面最强——但执行力是另一回事。</strong></p>'
            '</div>'
        ),
        "en": (
            '<h3>📌 AI × Tech</h3>'
            '<ul>'
            '<li><strong>OpenAI Makes GPT-5.5 Instant the New ChatGPT Default: 52.5% Fewer Hallucinations, Stronger STEM, Smarter Search</strong>'
            ' — GPT-5.5 Instant replaces GPT-5.3 Instant as the default for all ChatGPT users. Internal testing shows a 52.5% reduction in hallucination claims on high-risk prompts (medical, legal, financial). It also introduces stronger personalization with better use of prior context. The full GPT-5.5 (released April 23) scored 85% on ARC-AGI-2, with API pricing at $5/M tokens.'
            '<br><small>Source: <a href="https://jls42.org/en/news/ia-actualites-06-may-2026">jls42 AI News</a> / <a href="https://ms.aiassistantstore.com/blogs/latest-news/ai-news-wrap-up-5th-may-2026">AI Assistant Store</a></small></li>'
            '<li><strong>Anthropic Launches Deep Claude Integration with Excel, PowerPoint, Word, and Outlook — AI Officially Enters the Office Workflow</strong>'
            ' — Claude now works directly within the Microsoft Office suite, marking a critical migration of AI assistants from standalone chat interfaces into users\' daily work environments. Simultaneously, Anthropic\'s Managed Agents gain persistent memory, and SpaceX signed an expanded coding partnership.'
            '<br><small>Source: <a href="https://www.youtube.com/watch?v=SXneZ3bRKO4">Matt Wolfe (YouTube)</a> / <a href="https://jls42.org/en/news/ia-actualites-06-may-2026">jls42 AI News</a></small></li>'
            '<li><strong>Google Drops Bombshells One Week Before I/O (May 19): Googlebooks Laptop Platform and Aluminum OS (Android + ChromeOS Merger)</strong>'
            ' — Google released two major pre-I/O announcements: Googlebooks, a new laptop platform with built-in Gemini AI; and Aluminum OS, a merged Android + ChromeOS operating system. CNET and Android Authority predict I/O will center on Gemini\'s agentic capabilities, including cross-app automation and proactive AI assistance.'
            '<br><small>Source: <a href="https://www.cnet.com/tech/services-and-software/google-io-2026-everything-to-know/">CNET</a> / <a href="https://www.androidauthority.com/what-to-expect-from-google-io-2026-3664979/">Android Authority</a></small></li>'
            '<li><strong>xAI Launches Grok 4.3: 1M Token Context, #1 Agentic Tool Calling, Aggressively Low Pricing</strong>'
            ' — Grok 4.3 goes live on the xAI API with a 1-million-token context window and tops agentic tool-calling benchmarks. VentureBeat describes its pricing as "aggressively low," signaling xAI\'s price-war approach to capturing the developer market.'
            '<br><small>Source: <a href="https://jls42.org/en/news/ia-actualites-06-may-2026">jls42 AI News</a></small></li>'
            '<li><strong>White House Considers Pre-Release Government Vetting of AI Models: Google DeepMind, Microsoft, xAI Agree to Participate</strong>'
            ' — The NYT reports the Trump administration is discussing pre-release review of frontier AI models through the Commerce Department\'s AI Standards and Innovation Center. Google DeepMind, Microsoft, and xAI have agreed. Notably, OpenAI and Anthropic are not yet mentioned — potentially signaling a new regulatory landscape.'
            '<br><small>Source: <a href="https://www.nytimes.com/2026/05/04/technology/trump-ai-models.html">New York Times</a></small></li>'
            '</ul>'
            '<h3>🔄 Trends</h3>'
            '<ul>'
            '<li><strong>AI Competition Enters the "Default Entry Point" Battle</strong>: GPT-5.5 as ChatGPT default, Claude embedded in Office, Gemini baked into the OS — whoever becomes the AI users don\'t have to actively choose, wins</li>'
            '<li><strong>OS-Level AI Integration Accelerates</strong>: Google merging Android + ChromeOS + Gemini isn\'t a feature update — it\'s building an "AI-native operating system"</li>'
            '<li><strong>AI Regulation Shifts from "Post-Hoc Accountability" to "Pre-Release Review"</strong>: The White House pre-release vetting proposal marks a fundamental shift in US AI regulatory approach</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex\'s Take</h3>'
            '<p><strong>This week\'s most important news isn\'t any single model launch — it\'s three AI giants simultaneously fighting for the same thing: "default entry point."</strong></p>'
            '<p>Look at OpenAI\'s play. GPT-5.5 Instant becomes ChatGPT\'s default with 52.5% fewer hallucinations. The number matters, but the strategy matters more: OpenAI has stopped chasing the "most powerful model" narrative and is playing the "most reliable model" card instead. When your product is a daily tool for 200 million users, reducing hallucinations beats improving benchmarks. <strong>"Instant" says it all — OpenAI is optimizing GPT-5.5 as a fast, reliable, low-cost default, not a showcase flagship.</strong></p>'
            '<p>Anthropic\'s path is cleverer. Claude in Excel, PowerPoint, Word, Outlook — this is an exceptionally smart distribution strategy. Over 1 billion Office users worldwide spend their days switching between these four apps. When Claude appears directly inside them, users don\'t need to "open Claude" — Claude is already there. <strong>This solves Anthropic\'s biggest weakness: no owned distribution channel. By embedding in Microsoft\'s ecosystem, Anthropic bypasses the "make users come to us" challenge.</strong></p>'
            '<p>Google\'s moves are the most aggressive and ambitious. Merging Android and ChromeOS into Aluminum OS, launching Googlebooks laptops — this isn\'t a product update, it\'s rebuilding an operating system. <strong>If Google announces deep Gemini integration with Aluminum OS at I/O, it will have an unprecedented advantage: making AI the default at the OS level.</strong> Users don\'t need to choose Gemini — the moment they open their computer, Gemini is already running.</p>'
            '<p>xAI\'s Grok 4.3 and the White House vetting proposal add complexity from two directions. Grok 4.3\'s "aggressively low" pricing executes a classic disruptor strategy — low prices to attract developers and build ecosystem lock-in. The White House pre-release review, if implemented, would fundamentally change AI companies\' release cadence: <strong>every model update requiring government approval would hurt fast-iterating smaller companies (like Anthropic) far more than giants with internal compliance teams (like Google and Microsoft).</strong></p>'
            '<p><strong>Zoom out and the pattern is clear: May 2026\'s AI competition is no longer "whose model is better" — it\'s "who can make AI the user\'s default." OpenAI leverages ChatGPT\'s user base, Anthropic leverages Office\'s penetration, Google leverages OS-level control. Three paths, one goal. The eventual winner will likely be whoever balances all three dimensions (user base × workflow embedding × system-level control) most effectively. Right now, Google\'s hand looks strongest — but execution is another matter entirely.</strong></p>'
            '</div>'
        )
    },
    "cover": "",
    "sources": [
        {
            "url": "https://jls42.org/en/news/ia-actualites-06-may-2026",
            "title": {"zh": "AI 新闻速递：GPT-5.5 Instant、Grok 4.3、Anthropic 企业合作", "en": "AI News: GPT-5.5 Instant, Grok 4.3, Anthropic Enterprise"},
            "image": ""
        },
        {
            "url": "https://www.cnet.com/tech/services-and-software/google-io-2026-everything-to-know/",
            "title": {"zh": "CNET: Google I/O 2026 全面前瞻", "en": "CNET: Google I/O 2026 — Everything to Know"},
            "image": ""
        },
        {
            "url": "https://www.androidauthority.com/what-to-expect-from-google-io-2026-3664979/",
            "title": {"zh": "Android Authority: Google I/O 2026 前瞻——Gemini、Android、Aluminum OS", "en": "Android Authority: What to Expect from Google I/O 2026"},
            "image": ""
        },
        {
            "url": "https://www.nytimes.com/2026/05/04/technology/trump-ai-models.html",
            "title": {"zh": "纽约时报：白宫考虑在 AI 模型发布前进行审查", "en": "NYT: White House Considers Vetting A.I. Models Before Release"},
            "image": ""
        }
    ]
}

# ---------- fetch og:image for sources & cover ----------
for issue in [design_issue, tech_issue]:
    for src in issue["sources"]:
        if not src["image"]:
            src["image"] = fetch_og_image(src["url"])
    # use first source image as cover if available
    if not issue["cover"]:
        for src in issue["sources"]:
            if src["image"]:
                issue["cover"] = src["image"]
                break

# ---------- load, prepend, write ----------
issues_path = os.path.join(os.path.dirname(__file__), "issues.json")
with open(issues_path, "r", encoding="utf-8") as f:
    issues = json.load(f)

# Insert new issues at front (design first, then tech)
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open(issues_path, "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"✅ Inserted 2 new issues (design + tech) for 2026-05-14 evening. Total: {len(issues)}")
