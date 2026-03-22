# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily update - 2026-03-22 evening edition"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            text = r.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', text, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', text, re.I)
        return html.unescape(m.group(1)) if m else ""
    except:
        return ""

# Sources
sources_design = [
    {
        "title": {"zh": "Adobe 与 NVIDIA 宣布战略合作：下一代 Firefly 与 Agentic 创意工作流", "en": "Adobe and NVIDIA Announce Strategic Partnership for Next-Gen Firefly and Agentic Workflows"},
        "url": "https://news.adobe.com/news/2026/03/adobe-and-nvidia-announce-strategic-partnership",
    },
    {
        "title": {"zh": "Adobe Firefly 合作模型指南：从单一工具到创意 AI 聚合平台", "en": "Adobe Firefly Partner Models: The 2026 Field Guide"},
        "url": "https://www.feisworld.com/blog/adobe-firefly-partner-models-guide",
    },
    {
        "title": {"zh": "Creative Bloq: Adobe 认为创意人 2026 年将如何使用 AI", "en": "Creative Bloq: How Adobe Thinks Creatives Will Use AI in 2026"},
        "url": "https://www.creativebloq.com/tech/from-firefly-to-graph-how-adobe-thinks-creatives-will-use-ai-in-2026",
    },
    {
        "title": {"zh": "Adobe Firefly vs Midjourney 2026 对比", "en": "Adobe Firefly vs Midjourney 2026 Comparison"},
        "url": "https://weandthecolor.com/adobe-firefly-vs-midjourney-in-2026-which-one-is-actually-worth-it-for-designers/208554",
    },
]

sources_tech = [
    {
        "title": {"zh": "Axios: 微软发布 Copilot Cowork，基于 Anthropic 技术构建", "en": "Axios: Microsoft Launches Copilot Cowork Built on Anthropic Tech"},
        "url": "https://www.axios.com/2026/03/09/microsoft-copilot-cowork-anthropic",
    },
    {
        "title": {"zh": "TechCrunch: Anthropic 的 Claude 两周内发现 Firefox 22 个漏洞", "en": "TechCrunch: Anthropic's Claude Found 22 Firefox Vulnerabilities in Two Weeks"},
        "url": "https://techcrunch.com/2026/03/06/anthropics-claude-found-22-vulnerabilities-in-firefox-over-two-weeks/",
    },
    {
        "title": {"zh": "Amazon 推出 Health AI：Prime 会员免费 24/7 虚拟医疗", "en": "Amazon Launches Health AI Agent with Free 24/7 Virtual Care for Prime"},
        "url": "https://www.aboutamazon.com/news/retail/amazon-health-ai-agent-one-medical",
    },
    {
        "title": {"zh": "Forbes: 微软梦想数字同事，然后授权了 Anthropic 的技术", "en": "Forbes: Microsoft Dreamed of a Digital Coworker, Then Licensed Anthropic's"},
        "url": "https://www.forbes.com/sites/janakirammsv/2026/03/10/microsoft-dreamed-of-a-digital-coworker-then-it-licensed-anthropics/",
    },
]

# Fetch og:images
for s in sources_design + sources_tech:
    s["image"] = get_og_image(s["url"])
    print(f"  og:image for {s['url'][:60]}... -> {s['image'][:80] if s['image'] else '(none)'}")

design_cover = sources_design[0]["image"] or ""
tech_cover = sources_tech[0]["image"] or ""

new_issues = [
    {
        "date": "2026-03-22",
        "section": "design",
        "title": {
            "zh": "Adobe × NVIDIA 战略结盟：下一代 Firefly 模型+Agentic 创意工作流 · Adobe 变身「创意 AI 聚合器」：Firefly 不再只是图像工具，而是模型路由平台",
            "en": "Adobe × NVIDIA Strategic Alliance: Next-Gen Firefly Models + Agentic Creative Workflows · Adobe Becomes a 'Creative AI Aggregator': Firefly Evolves from Image Tool to Model Routing Platform"
        },
        "content": {
            "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Adobe 与 NVIDIA 宣布战略合作：加速下一代 Firefly 模型和 Agentic 创意工作流</strong> — Adobe 在本月正式与 NVIDIA 达成战略合作：利用 NVIDIA 的 Agent Toolkit 和 Nemotron 开放模型为 Adobe 的 Agentic 工作流提供动力，将 NVIDIA Omniverse 库集成到 Adobe 技术栈中以支持基于 OpenUSD 的 3D 数字孪生营销内容自动化，并通过 NVIDIA CUDA 加速 Frame.io 的云内容管理。这不是一个简单的技术集成——这是 Adobe 在宣告：<strong>未来的创意工作流不是人操作工具，而是 AI Agent 编排工具链。</strong><br><small>来源：<a href=\"https://news.adobe.com/news/2026/03/adobe-and-nvidia-announce-strategic-partnership\">Adobe 官方新闻</a></small></li><li><strong>Adobe Firefly 进化为「创意 AI 聚合平台」：集成 Google、OpenAI、Runway、ElevenLabs、FLUX 等第三方模型</strong> — Firefly 不再只是 Adobe 自家的图像生成模型。2026 年的 Firefly 已经集成了包括 Google Imagen、Ideogram、FLUX 在内的多家第三方合作模型，用户可以在同一个 Creative Cloud 订阅下按需调用不同模型。这意味着 Adobe 的战略定位已经从「最好的创意工具」变成了「创意 AI 的路由器和聚合器」——就像 Perplexity 在搜索领域做的事情一样。Adobe 原生模型仍然是唯一获得全额商业版权保障的选项（因为它 100% 基于 Adobe Stock 训练），但合作模型极大扩展了创意可能性。<br><small>来源：<a href=\"https://www.feisworld.com/blog/adobe-firefly-partner-models-guide\">Feisworld</a> | <a href=\"https://www.creativebloq.com/tech/from-firefly-to-graph-how-adobe-thinks-creatives-will-use-ai-in-2026\">Creative Bloq</a></small></li><li><strong>Firefly vs Midjourney 2026：Adobe 赢在结构性嵌入，不是图像质量</strong> — 一篇深度对比指出，Firefly 到 2028 年将主导专业设计市场——不是因为它生成的图像比 Midjourney 更好，而是因为 Adobe 让 Firefly 成为了专业创意工作流中不可分割的一部分。从 Photoshop 的 Generative Fill 到 Illustrator 的 AI 功能，从 Figma 集成到 Frame.io，Firefly 的胜算在于<strong>无处不在</strong>，而不是某一个维度的最优。<br><small>来源：<a href=\"https://weandthecolor.com/adobe-firefly-vs-midjourney-in-2026-which-one-is-actually-worth-it-for-designers/208554\">We and the Color</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>创意工具从「单一模型」到「模型聚合平台」</strong>：Adobe 和 Perplexity 的路线殊途同归</li><li><strong>Agentic 工作流进入创意领域</strong>：Adobe × NVIDIA 合作标志着 AI Agent 不只是写代码，还要做设计</li><li><strong>商业版权保障成为竞争壁垒</strong>：在 AI 生成内容泛滥的 2026 年，「可商用且无风险」是专业市场的硬需求</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Adobe 这个月做了一件比推出任何新功能都重要的事：它悄悄完成了从「创意工具公司」到「创意 AI 平台公司」的身份转变。而大多数设计师还没意识到这意味着什么。</strong></p><p>先看 NVIDIA 合作。表面上这是一个技术合作——CUDA 加速 Frame.io、Omniverse 支持 3D 数字孪生、Nemotron 模型驱动 Agentic 工作流。但真正的信号在「Agentic 工作流」这四个字里。Adobe 正在告诉市场：<strong>未来的创意生产不是设计师一个人操作 Photoshop，而是一群 AI Agent 在 Adobe 生态里协同工作，设计师负责审批和方向把控。</strong>这和上期我们聊的 Google「Vibe Design」是同一个方向，但 Adobe 的打法更老练——它不造新词，不搞概念营销，而是直接和 NVIDIA 签战略协议，用基础设施合作来锁定 Agentic 创意工作流的底层架构。</p><p>再看 Firefly 的合作模型策略。这个策略的精妙之处在于它完美解决了一个悖论：Adobe 自己的模型不一定是最好的（Midjourney 在艺术性上仍然领先），但 Adobe 不需要自己是最好的——它只需要成为你使用所有模型的入口。Google Imagen 擅长写实？调 Google 的。FLUX 擅长风格化？调 FLUX 的。但你始终在 Creative Cloud 里操作，始终用 Adobe 的订阅付费。<strong>这和 Perplexity 编排 19 个模型做搜索、微软用 Anthropic 技术做 Copilot Cowork 是完全一样的范式：不做最强的模型，做最好的模型路由器。</strong></p><p>但这里有一个值得警惕的细节。Adobe 原生 Firefly 模型是唯一提供完整商业版权保障的选项——因为它 100% 基于 Adobe Stock 训练。而合作模型（Google、FLUX 等）的版权状态是灰色的。这意味着对于需要法律确定性的商业项目，你只能用 Adobe 原生模型。<strong>Adobe 实际上在用「版权安全」这个杠杆，把专业客户锁定在自己的模型上，同时用合作模型吸引更多用户进入生态。</strong>先用免费的好东西把你拉进来，再用不可替代的安全保障把你留住——这是教科书级的平台策略。</p><p>最后把这期和上期的新闻连起来看，一个清晰的图景正在成形：<strong>2026 年设计工具市场正在分裂成三个层级。</strong>底层是 Google Stitch 和类似工具面向的「Vibe Design」市场——非设计师用语音和 prompt 快速出原型，够用就行。中层是 Figma 守住的「专业协作」市场——设计师用 AI 提速，但 Craft 和设计系统仍然是核心。顶层是 Adobe 正在构建的「Agentic 创意平台」——AI Agent 编排多模型和多工具，自动化大规模内容生产，设计师变成创意总监而非像素工人。这三个层级不是互相替代的关系，而是会长期共存。但资金和人才的流向很明确——<strong>从底层到顶层，从手动操作到 Agent 编排。</strong>Adobe 这个月的动作告诉我们：创意产业的「Agent 化」不是未来五年的事，而是现在进行时。</p></div>",
            "en": "<h3>📌 AI × Design</h3><ul><li><strong>Adobe × NVIDIA Strategic Partnership: Next-Gen Firefly Models and Agentic Creative Workflows</strong> — Adobe partners with NVIDIA to power agentic workflows with NVIDIA Agent Toolkit and Nemotron models, integrate Omniverse for 3D digital twin marketing content, and accelerate Frame.io with CUDA. The message: future creative workflows are AI agents orchestrating tool chains, not humans operating tools.<br><small>Source: <a href=\"https://news.adobe.com/news/2026/03/adobe-and-nvidia-announce-strategic-partnership\">Adobe News</a></small></li><li><strong>Adobe Firefly Evolves into Creative AI Aggregator</strong> — Firefly now integrates Google Imagen, Ideogram, FLUX, and other third-party models within Creative Cloud. Adobe's strategy shifts from 'best creative tool' to 'creative AI router and aggregator' — like Perplexity for search. Native Firefly remains the only fully indemnified option for commercial use.<br><small>Source: <a href=\"https://www.feisworld.com/blog/adobe-firefly-partner-models-guide\">Feisworld</a> | <a href=\"https://www.creativebloq.com/tech/from-firefly-to-graph-how-adobe-thinks-creatives-will-use-ai-in-2026\">Creative Bloq</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Creative tools shift from single models to model aggregation platforms</li><li>Agentic workflows enter the creative industry: Adobe × NVIDIA signals AI agents doing design</li><li>Commercial IP safety becomes a competitive moat in professional markets</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Adobe quietly completed its identity shift from 'creative tool company' to 'creative AI platform company' this month. Most designers haven't realized what this means.</strong></p><p>The NVIDIA partnership is about agentic workflows — AI agents orchestrating multi-model, multi-tool creative production. Firefly's partner model strategy is the same paradigm as Perplexity routing 19 models: don't build the strongest model, build the best model router. And Adobe's copyright indemnity on native Firefly creates a lock-in mechanism: free partner models pull you in, IP safety keeps you there. <strong>The 2026 design tool market is splitting into three tiers: Vibe Design (Google/Stitch), Professional Collaboration (Figma), and Agentic Creative Platforms (Adobe). Money and talent flow upward — from manual to agent-orchestrated.</strong></p></div>"
        },
        "cover": design_cover,
        "sources": sources_design
    },
    {
        "date": "2026-03-22",
        "section": "tech",
        "title": {
            "zh": "微软授权 Anthropic 技术构建 Copilot Cowork：曾经的威胁变成了供应商 · Claude Opus 4.6 两周发现 Firefox 22 个漏洞 · Amazon Health AI 面向 Prime 会员上线",
            "en": "Microsoft Licenses Anthropic Tech for Copilot Cowork: The Threat Becomes the Supplier · Claude Opus 4.6 Finds 22 Firefox Vulnerabilities in Two Weeks · Amazon Health AI Launches for Prime"
        },
        "content": {
            "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>微软授权 Anthropic 的 Claude Cowork 技术，推出 Copilot Cowork</strong> — 这可能是本月最戏剧性的 AI 商业新闻。Anthropic 的 Claude Cowork（能自主操控电脑完成多步骤任务的 AI Agent）曾直接导致微软股价蒸发 3570 亿美元——投资者担心第三方 AI Agent 会蚕食企业软件市场。微软的回应？不打它，授权它。微软与 Anthropic「密切合作」，将 Claude Cowork 背后的技术集成到 Microsoft 365 Copilot 中，推出 Copilot Cowork。这个 Agent 可以自主分析 Outlook 日历提出复杂日程调整、制作 PPT、拉取 Excel 数据、发邮件安排会议。微软表示 Copilot 将采用「多模态」策略——为每个任务选择最合适的模型，不再只绑定 OpenAI。<br><small>来源：<a href=\"https://www.axios.com/2026/03/09/microsoft-copilot-cowork-anthropic\">Axios</a> | <a href=\"https://www.forbes.com/sites/janakirammsv/2026/03/10/microsoft-dreamed-of-a-digital-coworker-then-it-licensed-anthropics/\">Forbes</a></small></li><li><strong>Claude Opus 4.6 两周发现 Firefox 22 个安全漏洞，14 个高危</strong> — Anthropic 与 Mozilla 合作，使用 Claude Opus 4.6 对 Firefox 代码库进行安全审计。两周内发现 22 个漏洞，其中 14 个为高危级别——几乎占 2025 年 Firefox 修复的所有高危漏洞的五分之一。大部分已在 Firefox 148 中修复。Mozilla 报告 AI 辅助分析额外发现了 90 个 bug，包括传统 fuzzing 工具无法捕获的逻辑错误。<br><small>来源：<a href=\"https://techcrunch.com/2026/03/06/anthropics-claude-found-22-vulnerabilities-in-firefox-over-two-weeks/\">TechCrunch</a></small></li><li><strong>Amazon 推出 Health AI Agent：Prime 会员可享免费 24/7 虚拟医疗服务</strong> — Amazon 在其网站和 App 上推出 Health AI Agent，与 One Medical 深度集成。Prime 会员可免费获得消息制虚拟问诊，AI 能处理症状评估、个性化健康建议、治疗方案推荐，并通过 Amazon Connect Health 自动化排期和文档等行政任务。Amazon 的策略很清晰：<strong>用 AI 降低医疗服务的边际成本，用 Prime 会员体系锁定用户。</strong><br><small>来源：<a href=\"https://www.aboutamazon.com/news/retail/amazon-health-ai-agent-one-medical\">About Amazon</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「敌人变供应商」成为 AI 产业常态</strong>：微软授权 Anthropic、微软同时依赖 OpenAI——多模型策略不是选择，而是必然</li><li><strong>AI 安全审计从辅助到主力</strong>：Claude 在 Firefox 上的表现证明 AI 发现漏洞的速度和深度正在超越传统方法</li><li><strong>AI Agent 进入医疗服务</strong>：Amazon 用 Prime 捆绑 AI 医疗，可能重塑初级保健市场</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>微软这个月的 Copilot Cowork 发布，表面上是一个产品发布，底下是 AI 产业权力关系最深刻的一次重组。让我展开说说为什么。</strong></p><p>回顾一下时间线：一月底，Anthropic 发布 Claude Cowork，股市直接抹掉了微软 3570 亿美元市值——投资者的逻辑是「如果 AI Agent 能自己操作电脑完成任务，谁还需要 Office 365？」两个月后，微软的回应来了：不是推出竞品来对抗 Anthropic，而是<strong>直接授权 Anthropic 的技术，用对手的武器武装自己</strong>。然后还把产品起了一模一样的名字——Copilot Cowork。这种「如果打不过就买」的策略在科技行业不新鲜，但在 AI 领域有一个独特的维度：<strong>微软同时是 OpenAI 最大的投资者和 Anthropic 的技术授权客户。</strong></p><p>这意味着什么？微软正在从「All in OpenAI」转向「多模型策略」——为每个任务选择最合适的模型。上期我们聊的 Perplexity 编排 19 个模型、Adobe 用多家合作模型做 Firefly 平台，现在微软也加入了。<strong>2026 年 Q1 的一个清晰信号是：没有任何一家公司愿意把命运绑在单一 AI 模型提供商上。</strong>这对 OpenAI 不是好消息——它最重要的客户和投资者正在积极对冲。这也解释了上期我们聊的微软考虑对 OpenAI/Amazon 云交易提起诉讼：微软既要保持对 OpenAI 的锁定（独家 Azure 托管），又要同时使用 Anthropic 的技术。这是一种极度矛盾的双线操作。</p><p>再说 Claude 找 Firefox 漏洞这件事。14 个高危漏洞在两周内被发现——这个数字相当于 Firefox 2025 年全年修复的高危漏洞的近五分之一。而且 Mozilla 后续用 AI 辅助分析又找到了 90 个传统 fuzzing 无法捕获的逻辑错误。这不是 AI 辅助安全审计，<strong>这是 AI 开始成为安全审计的主力</strong>。但让我不安的是另一面：如果 Claude 能在两周内找到 22 个漏洞，那些没有 Mozilla 那么透明、没有公开代码库的系统呢？商业软件里有多少漏洞是 AI 已经有能力发现、但没人在找的？AI 安全审计能力的不对称分布——大公司有，小公司没有——可能会成为下一个严重的安全鸿沟。</p><p>最后看 Amazon 的 Health AI。这个产品本身不复杂——AI 问诊、症状评估、转诊建议。但 Amazon 把它绑定在 Prime 会员体系里，这才是真正的杀招。美国初级保健面临严重短缺（预计 2030 年缺口 5.5 万名医生），而 Amazon 用 AI 把虚拟初诊的边际成本降到接近零，再用 Prime 的 2 亿会员基数做分发。<strong>Amazon 不是在做医疗 AI，它是在用 AI 重新定义「Prime 会员」的价值主张。</strong>当你的订阅不只包含快递、视频、音乐，还包含 24/7 免费医疗咨询时，Prime 的黏性又提高了一个数量级。这对 Teladoc 等远程医疗公司是巨大的威胁——它们还在收每次 50-75 美元的问诊费，而 Amazon 已经免费了。</p></div>",
            "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Microsoft Licenses Anthropic's Claude Cowork for Copilot Cowork</strong> — After Claude Cowork wiped $357B off Microsoft's market cap, Microsoft responded by licensing the very technology that threatened it. Copilot Cowork can autonomously handle complex tasks across Outlook, Excel, PowerPoint, and email. Microsoft signals a shift to multi-model strategy — 'right model for the job.'<br><small>Source: <a href=\"https://www.axios.com/2026/03/09/microsoft-copilot-cowork-anthropic\">Axios</a> | <a href=\"https://www.forbes.com/sites/janakirammsv/2026/03/10/microsoft-dreamed-of-a-digital-coworker-then-it-licensed-anthropics/\">Forbes</a></small></li><li><strong>Claude Opus 4.6 Discovers 22 Firefox Vulnerabilities in Two Weeks</strong> — Partnering with Mozilla, Anthropic found 22 bugs (14 high-severity) — nearly a fifth of all high-severity Firefox fixes in 2025. Mozilla's subsequent AI-assisted analysis uncovered 90 more bugs including logic errors missed by traditional fuzzing.<br><small>Source: <a href=\"https://techcrunch.com/2026/03/06/anthropics-claude-found-22-vulnerabilities-in-firefox-over-two-weeks/\">TechCrunch</a></small></li><li><strong>Amazon Launches Health AI Agent for Prime Members</strong> — Free 24/7 virtual care via AI on Amazon's website and app, integrated with One Medical. AI handles symptom assessment, personalized health advice, and administrative automation.<br><small>Source: <a href=\"https://www.aboutamazon.com/news/retail/amazon-health-ai-agent-one-medical\">About Amazon</a></small></li></ul><h3>🔄 Trends</h3><ul><li>'Frenemy becomes supplier' is the new AI industry norm: multi-model strategies are inevitable</li><li>AI security auditing moves from auxiliary to primary: Claude's Firefox results prove AI depth exceeds traditional methods</li><li>AI agents enter healthcare: Amazon bundles AI medicine with Prime, reshaping primary care economics</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Microsoft's Copilot Cowork launch looks like a product release on the surface, but underneath it's the deepest restructuring of AI industry power relationships this quarter.</strong></p><p>Microsoft is simultaneously OpenAI's biggest investor AND Anthropic's technology licensee. The multi-model strategy isn't optional anymore — no company in 2026 is willing to bet its future on a single AI provider. This is bad news for OpenAI: its most important customer is actively hedging. Claude's Firefox audit (22 vulns in 2 weeks, including 14 high-severity) marks AI becoming the primary tool for security research, not just an assistant. And Amazon's Health AI bundled with Prime isn't about healthcare — <strong>it's about redefining Prime's value proposition. When your subscription includes free 24/7 medical AI, Prime's stickiness increases by an order of magnitude, devastating to Teladoc and others still charging $50-75 per visit.</strong></p></div>"
        },
        "cover": tech_cover,
        "sources": sources_tech
    }
]

# Load existing issues
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

# Prepend new issues
issues = new_issues + issues

# Write back
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Added {len(new_issues)} issues. Total: {len(issues)}")
