# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import json, urllib.request, re, html

def get_og_image(url, timeout=8):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read(50000).decode("utf-8", errors="ignore")
            m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', data, re.I)
            if not m:
                m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data, re.I)
            return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images for sources
urls = {
    "techcrunch_claude_design": "https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/",
    "adplist": "https://adplist.substack.com/p/steal-these-30-design-ideas-for-2026",
    "nytimes_mythos": "https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html",
    "techcrunch_mythos": "https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/",
    "arstechnica_gemma": "https://arstechnica.com/ai/2026/04/google-announces-gemma-4-open-ai-models-switches-to-apache-2-0-license/",
    "google_gemma": "https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/",
    "cnbc_cursor": "https://www.cnbc.com/2026/04/19/cursor-ai-2-billion-funding-round.html",
    "engadget_nsa": "https://www.engadget.com/ai/the-nsa-is-reportedly-using-anthropics-new-model-mythos-211502787.html",
}

print("Fetching og:images...")
images = {}
for k, u in urls.items():
    img = get_og_image(u)
    images[k] = img
    print(f"  {k}: {img[:80] if img else '(none)'}")

# Build new issues
design_issue = {
    "date": "2026-04-21",
    "section": "design",
    "title": {
        "zh": "Claude Design 深度解析：Anthropic 如何从对话直达设计交付 · AI-First 设计师生存指南：30 个 2026 年可执行策略 · Figma MCP 让 Claude 直接读取设计文件",
        "en": "Claude Design Deep Dive: Anthropic's Path from Conversation to Design Delivery · AI-First Designer Survival Guide: 30 Actionable Strategies for 2026 · Figma MCP Lets Claude Read Design Files Directly"
    },
    "content": {
        "zh": """<h3>📌 AI × 设计</h3><ul><li><strong>Claude Design 深度解析：不是 Canva 竞品，而是设计的「新入口」</strong> — TechCrunch 的深度报道揭示了 Claude Design 的定位逻辑：Anthropic 明确表示它旨在「补充而非取代」Canva 等工具。Claude Design 由 Opus 4.7 驱动，支持从对话生成原型、幻灯片、单页文档等视觉产出。它的核心创新不在于生成质量，而在于<strong>把「设计」变成了一种对话行为——你不需要学习任何工具，只需要描述你想要什么</strong>。这延续了 Anthropic 从 Claude Cowork（1 月）到 Agentic Plugins（2 月）的产品线扩展路径。发布当天 Figma 股价下跌 4.26%，Adobe 和 Wix 也出现下滑。<br><small>来源：<a href="https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/">TechCrunch</a></small></li><li><strong>2026 AI-First 设计师生存指南：30 个可执行策略</strong> — ADPList 的 Felix Lee 发布了一份详尽的 AI 设计实战指南，核心观点鲜明：<strong>「当每个设计师都用相同的工具时，品味成为差异化因素」</strong>。指南建议连接 Figma MCP 让 Claude 直接读取设计文件（组件、token、间距），使用 Cursor 辅助前端开发，以及利用 AI 快速应用 Duolingo 等产品的设计模式。最关键的一句话：「AI 能写生产代码，但它不能为改变行为的设计而战。2026 年赢的设计师不会是用 AI 最多的人。」<br><small>来源：<a href="https://adplist.substack.com/p/steal-these-30-design-ideas-for-2026">ADPList / Felix Lee</a></small></li><li><strong>Figma MCP 生态初成：AI Agent 直接读取设计文件</strong> — Figma 的 MCP（Model Context Protocol）Server 已经让 Claude 等 AI 模型可以直接读取 Figma 设计文件——包括组件、设计 token、间距和结构。<strong>这意味着 AI 不再需要截图或描述来理解设计，而是可以像设计师一样「打开文件、看懂结构」</strong>。这是 Figma 应对 Claude Design 的核心防线：你可以用任何 AI 生成设计，但如果你的设计系统在 Figma 里，AI 必须通过 Figma 来理解它。<br><small>来源：<a href="https://adplist.substack.com/p/steal-these-30-design-ideas-for-2026">ADPList</a>、<a href="https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/">TechCrunch</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>设计入口的范式转移</strong>：从打开 Figma/Canva 到开口说话——Claude Design 把设计的起点从「工具」变成了「对话」</li><li><strong>Figma 的 MCP 防线</strong>：用设计系统数据锁定把 AI 变成自己的客户端，而非竞争对手</li><li><strong>品味 > 工具</strong>：当 AI 让每个人都能生成 80 分设计，区分 80 分和 95 分的不是工具，而是审美判断力</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Claude Design 发布第四天，尘埃初定。比起发布日的股价震荡和标题党，现在是时候认真分析这件事的结构性影响了。</strong></p><p>首先，TechCrunch 的报道里最重要的信息不是产品功能，而是 Anthropic 的定位声明：「补充而非取代」。这句话很值得玩味。<strong>表面上看是公关话术，但结合 Anthropic 的产品路径来看，它说的是真的——至少现在是</strong>。Claude Design 的目标用户不是每天在 Figma 里推像素的设计师，而是那些「有想法但不会设计」的人：PM、创始人、市场团队。它解决的不是「设计做得更好」的问题，而是「设计做得出来」的问题。这和 Canva 当年切入的市场几乎一致——Canva 让非设计师能做出及格的视觉，Claude Design 让非设计师能做出及格的原型。</p><p>但 Felix Lee 的指南提出了一个更深刻的问题：<strong>当生成能力被民主化后，设计师的价值到底在哪？</strong>他的答案是「品味」——当每个人都用相同的工具，审美判断力成为唯一的差异化因素。我基本同意，但想补充一点：品味不是天生的，它是<strong>大量观看、分析和批判性思考的结果</strong>。AI 能帮你生成 50 个方向，但选择哪个、为什么选、怎么调——这些需要的是对用户行为和文化语境的深度理解，不是 prompt 能教的。</p><p>Figma MCP 的布局是这周最被低估的新闻。<strong>让 Claude 直接读取 Figma 设计文件（组件、token、间距），这不是一个技术细节，而是一个战略棋步</strong>。它在说：「你可以用 Claude Design 生成初稿，但如果你的设计系统在 Figma 里，Claude 必须通过 Figma 来理解它。」这把 Figma 从「设计编辑器」重新定位为「设计数据的 single source of truth」。如果这个策略成功，Figma 不需要赢在生成能力——它只需要赢在「所有 AI 都需要读取 Figma 数据」这个事实上。</p><p><strong>把三件事串起来：2026 年的设计行业正在形成一个新的分层——AI 负责生成（Claude Design、Google Stitch），Figma 负责结构和规范（MCP、设计系统），设计师负责判断和取舍（品味、用户洞察）。这个分层听起来合理，但有一个致命问题：如果 AI 的判断能力持续进步（我认为会），中间的 Figma 层和顶部的设计师层都会被持续压缩。12 个月后回来看这段分析，可能会觉得我太保守了。</strong></p></div>""",
        "en": """<h3>📌 AI × Design</h3><ul><li><strong>Claude Design Deep Dive: Not a Canva Competitor, but a New 'Entry Point' for Design</strong> — TechCrunch's in-depth report reveals Claude Design's positioning: Anthropic explicitly states it aims to "complement rather than replace" tools like Canva. Powered by Opus 4.7, it supports generating prototypes, slides, and one-pagers from conversation. Its core innovation isn't generation quality but <strong>turning 'design' into a conversational act—you don't need to learn any tool, just describe what you want</strong>. Figma dropped 4.26% on launch day, with Adobe and Wix also declining.<br><small>Source: <a href="https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/">TechCrunch</a></small></li><li><strong>2026 AI-First Designer Survival Guide: 30 Actionable Strategies</strong> — Felix Lee's comprehensive guide on ADPList argues: <strong>"When every designer uses the same tools, taste becomes the differentiator."</strong> Key recommendations include connecting Figma MCP so Claude reads design files directly, using Cursor for frontend dev, and applying AI to replicate design patterns from products like Duolingo. The crucial line: "AI can write production code, but it can't fight for the design that changes behavior."<br><small>Source: <a href="https://adplist.substack.com/p/steal-these-30-design-ideas-for-2026">ADPList / Felix Lee</a></small></li><li><strong>Figma MCP Ecosystem Takes Shape: AI Agents Read Design Files Directly</strong> — Figma's MCP Server now lets Claude and other AI models read Figma files—components, design tokens, spacing, structure. <strong>AI no longer needs screenshots to understand design; it can 'open files and read structure' like a designer</strong>. This is Figma's core defense: your design system lives in Figma, so AI must go through Figma to understand it.<br><small>Source: <a href="https://adplist.substack.com/p/steal-these-30-design-ideas-for-2026">ADPList</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>Paradigm shift in design entry points</strong>: From opening Figma/Canva to speaking—Claude Design changes design's starting point from 'tool' to 'conversation'</li><li><strong>Figma's MCP defense</strong>: Using design system data lock-in to make AI its client, not its competitor</li><li><strong>Taste > Tools</strong>: When AI lets everyone generate 80-point designs, what separates 80 from 95 isn't tools—it's aesthetic judgment</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>Four days after Claude Design launched, the dust is settling. Time to analyze structural impact instead of stock price reactions.</strong></p><p>TechCrunch's most important detail isn't the product features—it's Anthropic's positioning: "complement, not replace." <strong>On the surface it's PR; but looking at Anthropic's product trajectory, they mean it—for now</strong>. Claude Design targets people who "have ideas but can't design": PMs, founders, marketing teams. It solves "making design possible" not "making design better."</p><p>Felix Lee's guide raises a deeper question: <strong>when generation is democratized, where does designer value lie?</strong> His answer: taste. I mostly agree, but add: taste isn't innate—it's the product of extensive observation, analysis, and critical thinking. AI generates 50 directions; choosing which, why, and how to refine requires deep understanding of user behavior and cultural context.</p><p>Figma MCP is this week's most underrated story. <strong>Letting Claude read Figma files (components, tokens, spacing) isn't a technical detail—it's a strategic chess move</strong>. It says: "Generate with Claude Design, but if your design system is in Figma, Claude must go through Figma to understand it." This repositions Figma from 'design editor' to 'single source of truth for design data.'</p><p><strong>Connecting all three: 2026's design industry is forming new layers—AI handles generation, Figma handles structure/standards, designers handle judgment/taste. Sounds reasonable, but if AI's judgment keeps improving (I think it will), both Figma's layer and the designer layer will keep getting compressed.</strong></p></div>"""
    },
    "cover": images.get("techcrunch_claude_design", ""),
    "sources": [
        {
            "title": {"zh": "Anthropic 发布 Claude Design：从对话到视觉交付", "en": "Anthropic Launches Claude Design for Creating Quick Visuals"},
            "url": "https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/",
            "image": images.get("techcrunch_claude_design", "")
        },
        {
            "title": {"zh": "2026 设计师必看：30 个 AI 设计实战策略", "en": "Steal These 30 Design Ideas for 2026"},
            "url": "https://adplist.substack.com/p/steal-these-30-design-ideas-for-2026",
            "image": images.get("adplist", "")
        },
        {
            "title": {"zh": "Claude Design 评测：直接对话生成完整设计", "en": "Claude Design Review: The AI Tool Coming for Figma"},
            "url": "https://www.youtube.com/watch?v=3LroZixa4Pw",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-04-21",
    "section": "tech",
    "title": {
        "zh": "Anthropic Mythos：「太危险而不能公开」的 AI 模型只给 40 家公司用 · Google Gemma 4 开源发布改用 Apache 2.0 · Cursor AI 完成 20 亿美元融资",
        "en": "Anthropic Mythos: The 'Too Dangerous to Release' AI Model Shared with 40 Companies · Google Gemma 4 Launches Under Apache 2.0 · Cursor AI Closes $2B Round"
    },
    "content": {
        "zh": """<h3>📌 AI × 科技</h3><ul><li><strong>Anthropic Mythos：AI 军备竞赛的新高度，还是精心策划的营销？</strong> — Anthropic 于 4 月 7 日发布了 Claude Mythos Preview，声称这是其「最强大」的模型，但<strong>「太危险而不能公开发布」</strong>。它只提供给包括 Apple、Amazon、Microsoft 在内的 40 多家公司，用于发现和修补关键软件的安全漏洞。NYT 报道称 Anthropic 认为 Mythos 标志着「AI 网络安全威胁的新时代」。更劲爆的是，Engadget 报道 NSA 已经在使用 Mythos。Fortune 分析指出，这个「太危险不发布」的叙事，与 OpenAI 2019 年 GPT-2 时期的策略如出一辙——巧合的是，当时 Dario Amodei 还在 OpenAI 工作。<strong>Anthropic $800B 估值的融资谈判正在进行中，Mythos 的戏剧性发布时机值得玩味</strong>。<br><small>来源：<a href="https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html">NYT</a>、<a href="https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/">TechCrunch</a>、<a href="https://fortune.com/2026/04/10/anthropic-too-dangerous-to-release-ai-model-means-for-its-upcoming-ipo/">Fortune</a></small></li><li><strong>Google Gemma 4 开源发布：改用 Apache 2.0 许可证，目标本地 AI</strong> — Google 发布了 Gemma 4 系列开源模型，提供四种尺寸（包括 E2B、E4B 小模型到 31B），基于 Gemini 3 底层技术，改进了推理、数学和指令遵循能力。<strong>最重要的变化是从 Google 自定义许可证切换到 Apache 2.0</strong>，消除了开发者最大的顾虑。Gemma 31B 在 Arena 排行榜上位列开源第三（仅次于 GLM-5 和 Kimi 2.5）。模型可从 Hugging Face、Kaggle 和 Ollama 下载。<br><small>来源：<a href="https://arstechnica.com/ai/2026/04/google-announces-gemma-4-open-ai-models-switches-to-apache-2-0-license/">Ars Technica</a>、<a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/">Google Blog</a></small></li><li><strong>Cursor AI 完成 20 亿美元融资，AI 编程工具估值狂飙</strong> — 据 CNBC 报道，AI 代码编辑器 Cursor 完成了 20 亿美元融资。这使其成为 AI 编程工具赛道估值最高的创业公司之一。<strong>从 1.5 亿到 20 亿美元的编程 AI 创业公司融资，说明资本市场已经把「AI 写代码」从概念验证升级为确定性趋势</strong>。结合 Anthropic 的 Claude Code、GitHub Copilot、Google 的 Gemini Code Assist，AI 编程赛道正在从工具竞争进入平台竞争阶段。<br><small>来源：<a href="https://www.cnbc.com/2026/04/19/cursor-ai-2-billion-funding-round.html">CNBC</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「太危险」成为新营销</strong>：Anthropic 的 Mythos 策略和 OpenAI 当年的 GPT-2 如出一辙——制造稀缺性和恐惧感来提升品牌影响力</li><li><strong>开源 AI 的许可证之战结束</strong>：Google 从自定义许可证转向 Apache 2.0，承认了开发者社区对真正开源的需求</li><li><strong>AI 编程从工具到平台</strong>：Cursor $2B 融资标志着 AI 编程赛道的估值锚点大幅上移</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>本周 AI 科技圈最有意思的不是某个产品发布，而是三家公司用三种完全不同的策略在争夺同一样东西：开发者的信任和依赖。</strong></p><p>先说 Anthropic 的 Mythos。让我直说：<strong>「太危险而不能公开」这个叙事，我闻到了浓浓的营销味</strong>。不是说 Mythos 不强——它可能确实很强。但把它发布时间放在 $800B 估值融资谈判的窗口期，只给 40 家大公司用（包括 Apple、Amazon、Microsoft），再加上 NSA 使用的消息「恰好」泄露……Fortune 说得对，这和 2019 年 OpenAI 的 GPT-2 策略如出一辙。当时 OpenAI 说 GPT-2「太危险不发布」，结果几个月后就全部公开了。<strong>但我也要承认：即使是营销，这个策略之所以有效，是因为底层有一个真实的趋势——AI 模型的网络安全能力确实在指数级增长</strong>。一个能发现关键软件漏洞的 AI 模型，同时也是一个能利用这些漏洞的 AI 模型。Anthropic 把 Mythos 定位为「防御者」，但每个安全专家都知道，攻防一体。</p><p>Google Gemma 4 走了完全相反的路线。<strong>不制造神秘感，而是拥抱透明——Apache 2.0 许可证是对开源社区的一个真诚信号</strong>。之前 Google 的自定义许可证让很多开发者望而却步，现在这个障碍没了。四种尺寸覆盖从手机端到工作站的全场景，这说明 Google 押注的不是「最强模型」，而是「最广泛部署」。Arena 排行榜上开源第三的成绩也不错，虽然被 GLM-5 和 Kimi 2.5（都是中国模型）压了一头——<strong>这个排名本身就是 2026 年 AI 格局的缩影：中国开源模型在性能上已经和 Google 并驾齐驱</strong>。</p><p>Cursor 的 $2B 融资则是另一个维度的信号。<strong>AI 编程赛道已经从「有没有用」进入了「谁能成为平台」的阶段</strong>。Cursor 的估值逻辑不是「一个更好的代码编辑器」，而是「开发者工作流的新操作系统」。当 Anthropic 有 Claude Code、GitHub 有 Copilot、Google 有 Gemini Code Assist 时，Cursor 用独立第三方的身份做差异化——它可以接入任何模型，不被任何一家 AI 公司绑定。这和 Figma 在设计领域的定位很像：不做模型，做工作流。</p><p><strong>把三件事连起来看：Anthropic 用「稀缺性+恐惧」建立品牌溢价（$800B 估值），Google 用「开放+普及」抢占部署广度，Cursor 用「中立+工作流」建立开发者粘性。三种策略都有道理，但我押注的是后两种——因为 AI 行业的历史反复证明，「太危险不发布」的模型最终都会发布，而真正建立壁垒的是生态系统和用户习惯。12 个月后 Mythos 大概率会公开，但 Gemma 生态和 Cursor 的用户群不会消失。</strong></p></div>""",
        "en": """<h3>📌 AI × Tech</h3><ul><li><strong>Anthropic Mythos: New Heights of AI Arms Race, or Calculated Marketing?</strong> — Anthropic released Claude Mythos Preview on April 7, calling it their "most powerful" model but <strong>"too dangerous for public release."</strong> Available only to 40+ companies including Apple, Amazon, Microsoft for finding security vulnerabilities in critical software. NYT reports Anthropic sees Mythos as marking "a new era of AI cybersecurity threats." Engadget reports the NSA is already using it. Fortune notes this "too dangerous" narrative mirrors OpenAI's 2019 GPT-2 playbook—when Dario Amodei was still at OpenAI. <strong>With Anthropic's $800B valuation talks underway, Mythos's dramatic timing is worth noting</strong>.<br><small>Source: <a href="https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html">NYT</a>, <a href="https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/">TechCrunch</a>, <a href="https://fortune.com/2026/04/10/anthropic-too-dangerous-to-release-ai-model-means-for-its-upcoming-ipo/">Fortune</a></small></li><li><strong>Google Gemma 4 Open Source Launch: Apache 2.0 License, Targeting Local AI</strong> — Google released Gemma 4 open models in four sizes (E2B to 31B), built on Gemini 3 technology with improved reasoning and math. <strong>The most significant change: switching from Google's custom license to Apache 2.0</strong>, removing developers' biggest concern. Gemma 31B ranks #3 among open models on Arena (behind GLM-5 and Kimi 2.5). Available on Hugging Face, Kaggle, and Ollama.<br><small>Source: <a href="https://arstechnica.com/ai/2026/04/google-announces-gemma-4-open-ai-models-switches-to-apache-2-0-license/">Ars Technica</a>, <a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/">Google Blog</a></small></li><li><strong>Cursor AI Closes $2B Funding Round</strong> — CNBC reports AI code editor Cursor completed a $2 billion funding round, making it one of the highest-valued AI coding startups. <strong>The leap from $150M to $2B in coding AI funding signals capital markets have upgraded "AI writes code" from proof of concept to certainty</strong>.<br><small>Source: <a href="https://www.cnbc.com/2026/04/19/cursor-ai-2-billion-funding-round.html">CNBC</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>"Too dangerous" as marketing</strong>: Anthropic's Mythos strategy mirrors OpenAI's 2019 GPT-2—manufacturing scarcity and fear to build brand</li><li><strong>Open-source license wars end</strong>: Google's Apache 2.0 switch acknowledges developer demand for truly open models</li><li><strong>AI coding: tools to platforms</strong>: Cursor's $2B marks a massive upward shift in AI coding valuations</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>This week's most interesting AI story isn't any single launch—it's three companies using completely different strategies to compete for the same thing: developer trust and dependency.</strong></p><p>On Mythos: let me be direct—<strong>the "too dangerous for public release" narrative smells strongly of marketing</strong>. Not that Mythos isn't powerful—it probably is. But dropping it during $800B valuation talks, limiting it to 40 big companies, with NSA usage "conveniently" leaking... Fortune is right: this is the 2019 GPT-2 playbook. <strong>But I'll concede: even as marketing, this works because there's a real trend underneath—AI's cybersecurity capabilities are growing exponentially</strong>.</p><p>Gemma 4 takes the opposite approach. <strong>No mystique, just transparency—Apache 2.0 is a sincere signal to the open-source community</strong>. Four sizes covering phone to workstation scenarios shows Google bets on "widest deployment" not "strongest model." Being #3 behind GLM-5 and Kimi 2.5—both Chinese models—<strong>is itself a snapshot of 2026's AI landscape: Chinese open models now match Google</strong>.</p><p>Cursor's $2B signals another dimension. <strong>AI coding has moved from "does it work" to "who becomes the platform."</strong> Cursor's valuation logic isn't "better code editor" but "new OS for developer workflows." Like Figma in design: don't make models, own the workflow.</p><p><strong>Connecting all three: Anthropic uses scarcity + fear for brand premium ($800B), Google uses openness + ubiquity for deployment breadth, Cursor uses neutrality + workflow for developer stickiness. All three make sense, but I'm betting on the latter two—because AI history repeatedly shows "too dangerous to release" models eventually get released, while ecosystems and user habits endure.</strong></p></div>"""
    },
    "cover": images.get("nytimes_mythos") or images.get("techcrunch_mythos", ""),
    "sources": [
        {
            "title": {"zh": "Anthropic 称新 AI 模型 Mythos 是网络安全「清算时刻」", "en": "Anthropic Claims Mythos Is a Cybersecurity 'Reckoning'"},
            "url": "https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html",
            "image": images.get("nytimes_mythos", "")
        },
        {
            "title": {"zh": "Google 发布 Gemma 4 开源模型，改用 Apache 2.0 许可证", "en": "Google Announces Gemma 4, Switches to Apache 2.0 License"},
            "url": "https://arstechnica.com/ai/2026/04/google-announces-gemma-4-open-ai-models-switches-to-apache-2-0-license/",
            "image": images.get("arstechnica_gemma", "")
        },
        {
            "title": {"zh": "Cursor AI 完成 20 亿美元融资", "en": "Cursor AI Closes $2 Billion Funding Round"},
            "url": "https://www.cnbc.com/2026/04/19/cursor-ai-2-billion-funding-round.html",
            "image": images.get("cnbc_cursor", "")
        }
    ]
}

# Read existing issues.json
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

# Insert new issues at beginning
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

# Write back
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("\n✅ issues.json updated with 2 new issues for 2026-04-21")
print(f"Total issues: {len(issues)}")
