#!/usr/bin/env python3
"""Rex Daily update for 2026-05-13"""
import json
import urllib.request
import urllib.error
import ssl
import re
import os

# SSL fix
try:
    import certifi
    os.environ['SSL_CERT_FILE'] = certifi.where()
except ImportError:
    pass

def get_og_image(url, timeout=10):
    """Fetch og:image from a URL."""
    try:
        ctx = ssl.create_default_context()
        try:
            import certifi
            ctx.load_verify_locations(certifi.where())
        except:
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            html = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
        return m.group(1) if m else ""
    except Exception as e:
        print(f"  og:image failed for {url}: {e}")
        return ""

# Fetch og:images
print("Fetching og:images...")
og_muzli = get_og_image("https://muz.li/blog/vibe-design-in-2026-what-ai-generated-ui-means-for-your-work/")
og_anthropic_tc = get_og_image("https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/")
og_macrumors = get_og_image("https://www.macrumors.com/2026/04/17/anthropic-claude-design/")
og_sierra_tc = get_og_image("https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/")
og_sierra_fe = get_og_image("https://www.frontier-enterprise.com/sierra-gets-950-million-in-fresh-funding/")
og_sierra_tt = get_og_image("https://www.trendingtopics.eu/sierra-raises-950-million-bret-taylors-ai-agent-startup-now-valued-at-over-15-billion/")

print(f"  muzli: {og_muzli}")
print(f"  anthropic_tc: {og_anthropic_tc}")
print(f"  macrumors: {og_macrumors}")
print(f"  sierra_tc: {og_sierra_tc}")
print(f"  sierra_fe: {og_sierra_fe}")
print(f"  sierra_tt: {og_sierra_tt}")

design_cover = og_anthropic_tc or og_macrumors or og_muzli or ""
tech_cover = og_sierra_tc or og_sierra_tt or og_sierra_fe or ""

new_issues = [
    {
        "date": "2026-05-13",
        "section": "design",
        "title": {
            "zh": "Claude Design + Vibe Design 浪潮：当 AI 从「辅助设计」变成「替代设计」，设计师的新战场在哪里？",
            "en": "Claude Design + the Vibe Design Wave: When AI Shifts from Assisting Design to Replacing It, Where Is the Designer's New Battlefield?"
        },
        "content": {
            "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Anthropic 推出 Claude Design：从代码库提取设计系统，直接对接 Claude Code 实现设计到生产的全链路</strong> — Claude Design 不是又一个「AI 生成 UI」的玩具。它的核心差异化在于两点：一是能从现有代码库中读取并提取设计系统（design system），确保生成的设计与已有产品一致；二是直接对接 Claude Code，实现从设计到可运行代码的无缝手交。Anthropic 明确表示这不是要替代 Canva 或 Figma，而是为不具备设计背景的 founder 和 PM 提供快速从想法到视觉表达的路径。<br><small>来源：<a href=\"https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/\">TechCrunch</a> / <a href=\"https://www.macrumors.com/2026/04/17/anthropic-claude-design/\">MacRumors</a></small></li><li><strong>「Vibe Design」正在成为 2026 年设计行业最具争议的趋势：非设计师用 AI 工具 30 秒生成高保真 UI</strong> — Muzli 的深度分析指出，「Vibe Design」是继「Vibe Coding」之后的又一个分水岭现象。Google Stitch（由收购的 Galileo AI 团队打造）可以从 prompt 直接生成高保真 UI；Claude Code + Figma MCP 可以读取 Figma 文件并生成生产级组件代码。核心问题不再是「AI 能不能做设计」，而是「当 AI 30 秒就能做出看起来不错的 UI 时，设计师的价值到底在哪里」。<br><small>来源：<a href=\"https://muz.li/blog/vibe-design-in-2026-what-ai-generated-ui-means-for-your-work/\">Muzli</a></small></li><li><strong>Claude Design 实战一周后的社区反馈：设计系统提取是杀手功能，但「从原型到生产」的gap仍然存在</strong> — Muzli 的跟进报道和 Scroll Agency 的实战指南都指出，Claude Design 的设计系统提取能力（从 GitHub repo 推断设计 token 和组件规范）是真正的差异化，但从原型到生产级代码的过程中，仍然需要专业工程介入。Lovable 和 v0 可以导入 Figma 设计但不能推断设计系统；Claude Design 原生做到了这一点。<br><small>来源：<a href=\"https://agence-scroll.com/en/blog/claude-design-anthropic-2026-guide\">Scroll Agency</a> / <a href=\"https://muz.li/blog/claude-design-one-week-in-hacks-best-practices-tips-from-real-world-use/\">Muzli</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 设计工具的竞争焦点从「生成质量」转向「系统级理解」</strong>：谁能读懂现有代码库和设计系统，谁就能真正嵌入企业工作流</li><li><strong>「Vibe Design」引发设计社区分裂</strong>：支持者认为这解放了创意；反对者认为这是对设计专业性的降维打击</li><li><strong>设计→代码管道正在被重构</strong>：Figma MCP + Claude Code 的组合意味着设计文件不再是终点，而是代码生成的输入</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Claude Design 的推出和「Vibe Design」趋势的爆发，标志着 AI 设计工具竞争进入了一个全新阶段——不再是「谁生成的 UI 更好看」，而是「谁能更深入地理解和融入现有的设计与工程系统」。</strong></p><p>让我解释为什么 Claude Design 的「设计系统提取」能力如此重要。过去一年里，我们见过太多 AI 设计工具的演示：输入 prompt，生成漂亮的 UI。但这些工具有一个致命问题——它们生成的是「孤立的漂亮画面」，而不是能嵌入现有产品的组件。一个成熟的产品有几十个颜色 token、上百个组件变体、严格的间距规范。如果 AI 工具不能理解这些，它生成的每一个界面都需要设计师手动对齐——省下的时间可能还不够返工。<strong>Claude Design 从代码库中推断设计系统的能力，直接解决了这个「最后一公里」问题。</strong>这不是增量改进，这是类别差异。</p><p>但更值得关注的是「Vibe Design」这个概念本身。Muzli 的文章把它定义得很精准：「一个没有设计背景的人，用 AI 工具在没有考虑周全的 brief 的情况下生成界面。」这听起来像是在描述一个问题，但它其实是在描述一个不可逆的现实。<strong>当 Google Stitch 免费向所有人开放、当 Claude Design 让任何人都能从想法直接跳到高保真原型，「设计」这个动作的门槛已经被不可逆地降低了。</strong>就像 Canva 降低了平面设计的门槛、WordPress 降低了网站建设的门槛一样——每次门槛降低，专业从业者的角色都会上移。</p><p>把这个和昨天 Figma State of the Designer 报告放在一起看，pattern 非常清晰：<strong>设计的执行层正在被极速压缩，但「知道该做什么」的判断层反而在升值。</strong>Figma 报告说满意度最高的设计师是「驱动业务影响力」的人；Claude Design 的目标用户是「不具备设计背景的 founder 和 PM」——这两个信号指向同一个结论：未来的设计师不是「用 Figma 做图的人」，而是「决定应该做什么图、为什么做、以及如何衡量效果的人」。</p><p><strong>我的预测：到 2026 年底，至少 30% 的 Y Combinator 初创公司将在没有专职设计师的情况下发布产品，使用 Claude Design + Lovable/v0 完成从概念到上线的全流程。但与此同时，那些拥有顶级设计团队的公司（Apple、Airbnb、Stripe）会更加重视设计投入——因为当「基础设计」变得免费，「卓越设计」的溢价反而更高。设计行业不是在消亡，是在分化：底部塌陷，顶部升值。Claude Design 加速的正是这个过程。</strong></p></div>",
            "en": "<h3>📌 AI × Design</h3><ul><li><strong>Anthropic Launches Claude Design: Extracts Design Systems from Codebases, Hands Off Directly to Claude Code for Full Design-to-Production Pipeline</strong> — Claude Design's core differentiation lies in two capabilities: reading and extracting design systems from existing codebases to ensure consistency, and direct handoff to Claude Code for seamless design-to-working-code transitions. Anthropic explicitly states this isn't meant to replace Canva or Figma, but to give founders and PMs without design backgrounds a fast path from idea to visual expression.<br><small>Source: <a href=\"https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/\">TechCrunch</a> / <a href=\"https://www.macrumors.com/2026/04/17/anthropic-claude-design/\">MacRumors</a></small></li><li><strong>'Vibe Design' Becomes 2026's Most Controversial Design Trend: Non-Designers Generate High-Fidelity UI in 30 Seconds with AI</strong> — Muzli's deep analysis identifies 'Vibe Design' as the next watershed moment after 'Vibe Coding.' Google Stitch generates high-fidelity UI from prompts; Claude Code + Figma MCP reads Figma files and generates production-quality component code. The question is no longer 'can AI design?' but 'when AI creates decent UI in 30 seconds, where exactly is the designer's value?'<br><small>Source: <a href=\"https://muz.li/blog/vibe-design-in-2026-what-ai-generated-ui-means-for-your-work/\">Muzli</a></small></li><li><strong>Claude Design One Week In: Design System Extraction Is the Killer Feature, but the Prototype-to-Production Gap Persists</strong> — Community feedback and agency guides note that Claude Design's ability to infer design tokens and component specs from GitHub repos is the real differentiator. Lovable and v0 can import Figma designs but can't infer design systems; Claude Design does this natively.<br><small>Source: <a href=\"https://agence-scroll.com/en/blog/claude-design-anthropic-2026-guide\">Scroll Agency</a> / <a href=\"https://muz.li/blog/claude-design-one-week-in-hacks-best-practices-tips-from-real-world-use/\">Muzli</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Design Tool Competition Shifts from 'Generation Quality' to 'Systems-Level Understanding'</strong>: Whoever can read existing codebases and design systems wins enterprise workflow integration</li><li><strong>'Vibe Design' Splits the Design Community</strong>: Supporters see creative liberation; critics see a reductive attack on design professionalism</li><li><strong>Design→Code Pipeline Being Rebuilt</strong>: Figma MCP + Claude Code means design files are no longer endpoints but inputs for code generation</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Claude Design's launch and the explosion of 'Vibe Design' mark AI design tools entering a new phase — no longer 'whose generated UI looks prettier' but 'who can more deeply understand and integrate into existing design and engineering systems.'</strong></p><p>Here's why Claude Design's design system extraction matters so much. Over the past year, we've seen countless AI design tool demos: input a prompt, get beautiful UI. But they all share a fatal flaw — they generate 'isolated pretty screens,' not components that fit into existing products. A mature product has dozens of color tokens, hundreds of component variants, strict spacing rules. If AI tools can't understand these, every generated screen requires manual alignment — saving no time at all. <strong>Claude Design's ability to infer design systems from codebases solves this 'last mile' problem.</strong> This isn't incremental improvement; it's a category difference.</p><p>But the concept of 'Vibe Design' is even more significant. Muzli defines it precisely: 'someone without a design background directing AI tools without a considered brief.' This sounds like describing a problem, but it's actually describing an irreversible reality. <strong>When Google Stitch is free for everyone and Claude Design lets anyone jump from idea to high-fidelity prototype, the barrier to 'designing' has been irreversibly lowered.</strong></p><p>Connecting this to yesterday's Figma State of the Designer report, the pattern is crystal clear: <strong>design's execution layer is being rapidly compressed, but the judgment layer — 'knowing what to build' — is appreciating in value.</strong> Future designers won't be 'people who make screens in Figma' but 'people who decide what screens to make, why, and how to measure their impact.'</p><p><strong>Prediction: by end of 2026, at least 30% of Y Combinator startups will ship products without a dedicated designer, using Claude Design + Lovable/v0 for the full concept-to-launch flow. But simultaneously, companies with elite design teams (Apple, Airbnb, Stripe) will invest even more in design — because when 'basic design' becomes free, 'exceptional design' commands an even higher premium. Design isn't dying; it's bifurcating: the bottom collapses, the top appreciates. Claude Design is accelerating exactly this process.</strong></p></div>"
        },
        "cover": design_cover,
        "sources": [
            {
                "url": "https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/",
                "title": {
                    "zh": "Anthropic 推出 Claude Design：快速创建视觉原型的 AI 新产品",
                    "en": "Anthropic Launches Claude Design, a New Product for Creating Quick Visuals"
                },
                "image": og_anthropic_tc
            },
            {
                "url": "https://muz.li/blog/vibe-design-in-2026-what-ai-generated-ui-means-for-your-work/",
                "title": {
                    "zh": "Vibe Design：AI 生成 UI 对设计师工作意味着什么",
                    "en": "Vibe Design in 2026: What AI-Generated UI Means for Your Work"
                },
                "image": og_muzli
            },
            {
                "url": "https://agence-scroll.com/en/blog/claude-design-anthropic-2026-guide",
                "title": {
                    "zh": "Claude Design 完全指南：从原型到生产的实战分析",
                    "en": "Claude Design (Anthropic): The Complete 2026 Guide"
                },
                "image": ""
            }
        ]
    },
    {
        "date": "2026-05-13",
        "section": "tech",
        "title": {
            "zh": "Sierra 融资 9.5 亿美元估值 150 亿——Bret Taylor 的 AI Agent 平台已服务 40% 财富 50 强，企业 AI Agent 赛道进入「寡头化」阶段",
            "en": "Sierra Raises $950M at $15B Valuation — Bret Taylor's AI Agent Platform Serves 40% of Fortune 50, Enterprise AI Agent Market Enters Oligopoly Phase"
        },
        "content": {
            "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Sierra 完成 9.5 亿美元 E 轮融资，估值超 150 亿美元，Tiger Global 和 GV 领投</strong> — 由前 Salesforce 联席 CEO、现 OpenAI 董事长 Bret Taylor 联合创立的 AI Agent 平台 Sierra，完成了迄今为止企业 AI Agent 赛道最大的一笔融资。Sierra 的 Agent OS 平台让企业可以无代码构建、部署和优化 AI Agent，覆盖客服、支付、个性化等场景。<strong>关键数据：从 4 个设计合作伙伴起步，目前已服务超过 40% 的财富 50 强企业；ARR 从 2025 年 11 月的 1 亿美元飙升到 2026 年 2 月的 1.5 亿美元——仅用 3 个月增长 50%。</strong><br><small>来源：<a href=\"https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/\">TechCrunch</a> / <a href=\"https://www.trendingtopics.eu/sierra-raises-950-million-bret-taylors-ai-agent-startup-now-valued-at-over-15-billion/\">Trending Topics</a></small></li><li><strong>Sierra 的 Agent OS 架构：Agent Studio（无代码构建）+ Voice（实时语音交互）+ Insights（优化分析）</strong> — Sierra 不只是卖一个 chatbot。Agent Studio 内置 Ghostwriter 功能，让企业无代码构建 AI Agent；Voice 模块支持实时语音交互；Insights 提供 Agent 表现的深度分析和优化建议。<strong>这套架构的野心是成为企业 AI Agent 的「操作系统」——就像 Salesforce 是 CRM 的操作系统一样。</strong><br><small>来源：<a href=\"https://www.tamradar.com/funding-rounds/sierra-series-e-950m\">TAMradar</a></small></li><li><strong>企业 AI Agent 市场 2024 年 25.8 亿美元，预计 2030 年达 245 亿美元（CAGR 47%）</strong> — Grand View Research 数据显示，企业 AI Agent 市场正以 47% 的年复合增长率爆发。Sierra、OpenAI Deployment Company、Anthropic 企业服务三巨头正在争夺这个即将爆发的市场。Sierra 的投资者阵容也说明了一切：Tiger Global（Stripe 投资者）、GV（Google Ventures）、Benchmark（Uber 投资者）、Sequoia Capital——全是顶级 growth-stage 基金。<br><small>来源：<a href=\"https://www.frontier-enterprise.com/sierra-gets-950-million-in-fresh-funding/\">Frontier Enterprise</a> / <a href=\"https://www.thesaasnews.com/news/sierra-raises-950m-at-15b-valuation\">The SaaS News</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI Agent 赛道进入「寡头化」阶段</strong>：Sierra（150 亿估值）、OpenAI Deployment Company（40 亿投资）、Anthropic 企业服务——三巨头格局初现</li><li><strong>从 chatbot 到 Agent OS</strong>：Sierra 的产品架构不是「更好的聊天机器人」，而是企业客户体验的操作系统</li><li><strong>ARR 增速成为 AI 公司的核心叙事</strong>：3 个月 50% 的 ARR 增长让 Sierra 在估值溢价上有了真实数据支撑</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Sierra 的 9.5 亿美元融资不只是又一个大额融资新闻——它是企业 AI Agent 赛道从「混战」进入「寡头化」的标志性事件。</strong></p><p>先看 Bret Taylor 的策略。他从 Salesforce 离开后创立 Sierra，本身就是一个信号：这个人比地球上大多数人都更了解企业软件的销售和部署。他没有去做通用 AI 模型，而是做了一个 Agent OS——一个让企业在任何 AI 模型之上构建、部署和优化 Agent 的平台。<strong>这个定位精准到可怕：它不和 OpenAI、Anthropic 竞争模型层，而是站在它们的肩膀上卖铲子。</strong>无论哪个模型赢得前沿竞赛，企业都需要一个平台来把模型能力转化为实际的客户体验——这就是 Sierra 的卡位。</p><p>40% 的财富 50 强是一个震撼的数字。美国最大的 50 家公司中有 20 家以上在用 Sierra 的平台。这意味着 Sierra 已经度过了「证明概念」阶段，进入了「规模扩张」阶段。<strong>ARR 从 1 亿到 1.5 亿只用了 3 个月——这个增速如果持续，Sierra 到 2026 年底的 ARR 可能突破 4 亿美元。</strong>对于一家成立不到 3 年的公司，这是 Salesforce 级别的早期增长曲线。</p><p>把这个放在更大的图景里看。昨天我们报道了 OpenAI 砸 40 亿成立 Deployment Company，收购 Tomoro 并洽谈三笔新收购。前天的 Anthropic 与 Blackstone/高盛合作做企业服务。<strong>现在加上 Sierra 的 9.5 亿——三条独立的新闻拼在一起，画出的是同一张图：企业 AI Agent 市场正在从「谁的模型更强」转向「谁的部署和集成更好」。</strong>Sierra 选择做模型无关的 Agent OS，OpenAI 选择自建部署团队，Anthropic 选择与金融巨头合作——三种不同的路径，同一个目的地。</p><p><strong>这三条路径最终谁赢？我押 Sierra 的模式有最大的结构性优势。原因很简单：模型无关性。当一家企业在 Sierra 上构建了 Agent，它可以在底层自由切换 GPT、Claude、Gemini。这种灵活性对企业 CTO 来说是最大的卖点——没有人愿意被锁定在单一模型供应商上。相比之下，OpenAI 的 Deployment Company 本质上是在卖「GPT 全家桶」，Anthropic 的企业服务是在卖「Claude 全家桶」。当企业买的是「全家桶」而不是「操作系统」，它们的迁移成本更低、议价权更强。这就是为什么 Sierra 能在有 OpenAI 和 Anthropic 的市场里拿到 150 亿估值——因为投资者看到了平台效应的潜力。</strong></p><p><strong>连接设计板块：Claude Design 让非设计师也能生成原型，Sierra 让企业无代码构建 AI Agent——两者的底层逻辑是一样的：AI 正在把专业技能的门槛不可逆地降低。但就像设计行业的分化一样，AI Agent 行业也会分化：大量低端的 chatbot 服务商会被淘汰，而像 Sierra 这样提供系统级解决方案的平台会吃掉大部分市场。2026 年的主题不是「AI 取代人」，而是「AI 平台取代工具」。</strong></p></div>",
            "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Sierra Closes $950M Series E at $15B+ Valuation, Led by Tiger Global and GV</strong> — Sierra, the AI Agent platform co-founded by former Salesforce co-CEO and current OpenAI Chairman Bret Taylor, has closed the largest funding round in the enterprise AI agent space. Its Agent OS platform enables no-code building, deployment, and optimization of AI agents across customer service, payments, and personalization. <strong>Key metrics: from 4 design partners to 40%+ of Fortune 50 companies; ARR surged from $100M (Nov 2025) to $150M (Feb 2026) — 50% growth in just 3 months.</strong><br><small>Source: <a href=\"https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/\">TechCrunch</a> / <a href=\"https://www.trendingtopics.eu/sierra-raises-950-million-bret-taylors-ai-agent-startup-now-valued-at-over-15-billion/\">Trending Topics</a></small></li><li><strong>Sierra's Agent OS Architecture: Agent Studio (No-Code) + Voice (Real-Time) + Insights (Analytics)</strong> — Sierra isn't selling a chatbot. Agent Studio with Ghostwriter enables no-code AI agent building; Voice supports real-time voice interactions; Insights provides deep analytics. <strong>The ambition: become the 'operating system' for enterprise AI agents — just as Salesforce is the OS for CRM.</strong><br><small>Source: <a href=\"https://www.tamradar.com/funding-rounds/sierra-series-e-950m\">TAMradar</a></small></li><li><strong>Enterprise AI Agent Market: $2.58B in 2024, Projected $24.5B by 2030 (47% CAGR)</strong> — Grand View Research data shows the enterprise AI agent market growing at 47% CAGR. Sierra, OpenAI Deployment Company, and Anthropic enterprise services are the three giants competing for this explosive market. Sierra's investor roster says it all: Tiger Global, GV, Benchmark, Sequoia Capital.<br><small>Source: <a href=\"https://www.frontier-enterprise.com/sierra-gets-950-million-in-fresh-funding/\">Frontier Enterprise</a> / <a href=\"https://www.thesaasnews.com/news/sierra-raises-950m-at-15b-valuation\">The SaaS News</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Agent Space Enters Oligopoly Phase</strong>: Sierra ($15B), OpenAI Deployment Co. ($4B), Anthropic Enterprise — a three-giant landscape is forming</li><li><strong>From Chatbot to Agent OS</strong>: Sierra's product isn't 'a better chatbot' but an operating system for enterprise customer experience</li><li><strong>ARR Growth Rate Becomes Core AI Company Narrative</strong>: 50% ARR growth in 3 months gives Sierra real data backing its valuation premium</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Sierra's $950M raise isn't just another big funding headline — it's the marker of the enterprise AI agent space moving from 'free-for-all' to 'oligopoly.'</strong></p><p>Look at Bret Taylor's strategy. Leaving Salesforce to build Sierra was itself a signal: this person understands enterprise software sales and deployment better than almost anyone alive. He didn't build a general AI model — he built an Agent OS, a platform for enterprises to build, deploy, and optimize agents on top of any AI model. <strong>This positioning is surgically precise: it doesn't compete with OpenAI or Anthropic at the model layer but stands on their shoulders selling shovels.</strong></p><p>40% of the Fortune 50 is a staggering number. This means Sierra has passed the 'proof of concept' stage and entered 'scale expansion.' <strong>ARR from $100M to $150M in 3 months — if sustained, Sierra could hit $400M ARR by end of 2026.</strong> For a company less than 3 years old, this is Salesforce-tier early growth.</p><p>Zooming out: yesterday we covered OpenAI spending $4B on its Deployment Company and acquiring Tomoro. Before that, Anthropic partnering with Blackstone/Goldman Sachs for enterprise services. <strong>Now add Sierra's $950M — three independent stories that paint the same picture: the enterprise AI agent market is shifting from 'whose model is stronger' to 'whose deployment and integration is better.'</strong></p><p><strong>Which path wins? I'd bet on Sierra's model-agnostic approach having the biggest structural advantage. When enterprises build agents on Sierra, they can freely switch between GPT, Claude, and Gemini underneath. This flexibility is the ultimate selling point for enterprise CTOs — nobody wants vendor lock-in. By contrast, OpenAI's Deployment Company is essentially selling 'the GPT bundle,' and Anthropic's enterprise service sells 'the Claude bundle.' When enterprises buy 'bundles' instead of 'operating systems,' their switching costs are lower and bargaining power stronger. That's why Sierra can command a $15B valuation in a market where OpenAI and Anthropic exist — investors see platform-effect potential.</strong></p><p><strong>Connecting to design: Claude Design lets non-designers generate prototypes; Sierra lets enterprises build AI agents without code. The underlying logic is identical: AI is irreversibly lowering the barrier to specialized skills. But just as the design industry is bifurcating, so will AI agents: commodity chatbot providers will be eliminated while platforms like Sierra offering systems-level solutions capture most of the market. 2026's theme isn't 'AI replaces people' — it's 'AI platforms replace tools.'</strong></p></div>"
        },
        "cover": tech_cover,
        "sources": [
            {
                "url": "https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/",
                "title": {
                    "zh": "Sierra 融资 9.5 亿美元：企业 AI Agent 竞争白热化",
                    "en": "Sierra Raises $950M as the Race to Own Enterprise AI Gets Serious"
                },
                "image": og_sierra_tc
            },
            {
                "url": "https://www.trendingtopics.eu/sierra-raises-950-million-bret-taylors-ai-agent-startup-now-valued-at-over-15-billion/",
                "title": {
                    "zh": "Sierra 融资 9.5 亿美元，Bret Taylor 的 AI Agent 公司估值超 150 亿",
                    "en": "Sierra Raises $950M: Bret Taylor's AI Agent Startup Valued Over $15B"
                },
                "image": og_sierra_tt
            },
            {
                "url": "https://www.frontier-enterprise.com/sierra-gets-950-million-in-fresh-funding/",
                "title": {
                    "zh": "Sierra 获 9.5 亿美元新融资，目标成为企业 AI Agent 全球标准",
                    "en": "Sierra Gets $950 Million in Fresh Funding"
                },
                "image": og_sierra_fe
            }
        ]
    }
]

# Load existing issues
issues_path = os.path.join(os.path.dirname(__file__), "issues.json")
with open(issues_path, "r", encoding="utf-8") as f:
    issues = json.load(f)

# Insert new issues at the front
issues = new_issues + issues

# Write back
with open(issues_path, "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Added {len(new_issues)} issues to issues.json (total: {len(issues)})")
