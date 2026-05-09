# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily update for 2026-05-09"""
import json
import urllib.request
import re

def get_og_image(url):
    """Fetch og:image from a URL."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read(50000).decode('utf-8', errors='ignore')
            match = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html)
            if not match:
                match = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html)
            return match.group(1) if match else ""
    except:
        return ""

# Sources
design_sources = [
    ("https://designfest.framer.media/blogs/ai-tools-every-uiux-designer-should-try",
     "Designfest 发布 2026 年 10 款 AI 设计工具实战指南：设计不再是「画图」，而是「AI 增强工作流」",
     "Designfest's 10 AI Tools Every UI/UX Designer Should Try in 2026: Design Is Now AI-Augmented Workflows"),
    ("https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d",
     "Muzli 设计师实测：2026 年 UX 工作流中真正在用的 8 款 AI 工具",
     "Muzli Designer's Real Workflow: The 8 AI Tools I Actually Use in UX Design (2026)"),
    ("https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
     "加拿大设计师协会 RGD：AI 工具如何支持创意和负责任的设计工作流",
     "RGD: AI Tools for Designers in 2026 — Supporting Creativity and Responsible Workflows"),
]

tech_sources = [
    ("https://www.geekwire.com/2026/microsoft-releases-new-ai-models-to-further-expand-beyond-openai/",
     "Microsoft 发布 MAI 三件套自研模型，加速「去 OpenAI 化」",
     "Microsoft Releases MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2 — Expanding Beyond OpenAI"),
    ("https://www.euronews.com/next/2026/05/08/tech-giants-agree-to-us-government-ai-testing",
     "Google、Microsoft、xAI 正式接受美国政府 AI 预发布审查",
     "Google, Microsoft, xAI Agree to US Government Pre-Release AI Testing Programme"),
    ("https://finance.yahoo.com/sectors/technology/articles/layoffs-accelerate-may-2026-firms-040430218.html",
     "2026 年 5 月科技裁员加速：AI 重构正在吞噬 SaaS 岗位",
     "Layoffs Accelerate in May 2026 as AI Restructuring Reshapes the Tech Workforce"),
]

print("Fetching og:images...")
design_images = []
for url, _, _ in design_sources:
    img = get_og_image(url)
    design_images.append(img)
    print(f"  {url[:60]}... -> {img[:80] if img else '(none)'}")

tech_images = []
for url, _, _ in tech_sources:
    img = get_og_image(url)
    tech_images.append(img)
    print(f"  {url[:60]}... -> {img[:80] if img else '(none)'}")

design_cover = next((img for img in design_images if img), "")
tech_cover = next((img for img in tech_images if img), "")

# Build design issue
design_issue = {
    "date": "2026-05-09",
    "section": "design",
    "title": {
        "zh": "当「AI 增强工作流」成为 2026 设计行业的共识，真正的分歧出现了：AI 应该帮设计师做决策，还是只帮他们加速执行？——从三份实战报告看设计师与 AI 的关系重定义",
        "en": "When 'AI-Augmented Workflows' Become Design's 2026 Consensus, the Real Divide Emerges: Should AI Help Designers Decide, or Just Help Them Execute Faster? — Three Practitioner Reports Redefine the Designer-AI Relationship"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Designfest 发布 2026 年 10 款 AI 工具实战指南：「设计不再只是画图，而是 AI 增强工作流和数据驱动决策」</strong> — 这份来自 Designfest 的深度指南覆盖了从 Figma AI（多屏生成）到 UX Pilot AI（「研究到原型」一体化）到 Visily（AI 驱动的快速协作线框工具）的全链路。一个值得注意的判断：<strong>2026 年的 UI/UX 设计已经从「画图」进化为「AI 增强工作流 + 数据驱动决策」</strong>。文章按角色分类推荐——UI 设计师用 Figma AI + Visily，UX 研究员用 UX Pilot，前端开发用 Relume——这种「按角色而非按功能」的分类方式本身就反映了 AI 工具开始渗透设计团队的每个环节。<br><small>来源：<a href=\"https://designfest.framer.media/blogs/ai-tools-every-uiux-designer-should-try\">Designfest</a></small></li><li><strong>Muzli 设计师实测日记：「这是我 UX 工作流中真正在用的 8 款 AI 工具，以及我为什么用它们」</strong> — 来自 Muzli（Design Inspiration 社区）的实战分享，作者不是列工具清单，而是详细解释了每款工具在真实项目中的使用场景和理由。核心洞察：<strong>AI 工具的价值不在于功能多强大，而在于能否无缝嵌入现有工作流</strong>。文章还推荐了 Moonchild.ai 关于「如何构建有效的 AI 设计工具栈」的框架——这说明设计师社区已经从「试一试 AI」进入「系统化整合 AI」阶段。<br><small>来源：<a href=\"https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d\">Muzli / Medium</a></small></li><li><strong>加拿大设计师协会 RGD 发文：AI 工具应支持创意和负责任的工作流，而非替代设计判断</strong> — 专业设计师协会 RGD 发布了一份关于 AI 在设计中应用的立场文章，强调 AI 应该「放大创意」而非「替代创意」。文章呼吁设计师在采用 AI 工具时关注三个维度：<strong>创意主权（设计师保留最终决策权）、伦理使用（训练数据来源和版权）、以及客户透明度（告知客户 AI 的参与程度）</strong>。这是行业协会层面首次系统性地框定设计师与 AI 的关系。<br><small>来源：<a href=\"https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026\">RGD</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「AI 增强工作流」成为行业共识</strong>：从工具评测到行业协会声明，2026 年的设计行业已经不再争论「要不要用 AI」——焦点转向「AI 在工作流中的正确位置」</li><li><strong>从「试工具」到「建工具栈」</strong>：Moonchild.ai 的 AI 设计工具栈框架和 Muzli 的实战分享表明，设计师开始系统化地整合 AI，而非零散地试用</li><li><strong>职业协会介入 AI 伦理</strong>：RGD 的立场标志着设计行业开始在制度层面回应 AI 挑战——创意主权和客户透明度可能成为未来的行业标准</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天这三份报告表面上都在说同一件事——「AI 工具很有用」——但仔细看，它们之间有一个微妙而重要的分歧：AI 应该帮设计师做决策，还是只帮他们加速执行？</strong></p><p>Designfest 的指南代表了「加速执行」派：AI 生成多屏 UI、AI 快速出线框、AI 辅助前端代码。工具的价值衡量标准是「快了多少」——Figma AI 能在几秒内生成一个多屏 dashboard 起点，Visily 的 Smart Templates 能根据行业自动推荐 UX 模式。这是当前主流的 AI 设计叙事：<strong>AI 是一个涡轮增压器，让设计师跑得更快，但方向盘还在设计师手里</strong>。</p><p>但 Muzli 那篇实战分享暗示了一个更激进的方向。作者提到 UX Pilot AI 能从用户研究数据直接生成设计方案——这不只是「加速执行」，这是<strong>「辅助决策」</strong>。当 AI 能分析用户数据并推荐设计方案时，设计师的角色从「创造者」变成了「审核者」。这和我们昨天讨论的「前端开发者从写代码变成审查 AI 写的代码」是完全同构的转变。<strong>设计师和开发者正在经历同一场角色重定义，只是设计师还没有意识到自己走到了哪一步。</strong></p><p>RGD 的立场文章是今天最值得深思的一份。一个专业设计师协会公开讨论「创意主权」和「客户透明度」——这说明 AI 在设计中的应用已经从「技术话题」升级为「职业伦理话题」。RGD 提出的三个维度（创意主权、伦理使用、客户透明度）本质上是在回答一个问题：<strong>当 AI 参与了设计过程，这个设计还能算是「设计师的作品」吗？</strong>这个问题在摄影领域（AI 修图）、写作领域（AI 辅助写作）已经引发了激烈争论，现在轮到设计行业了。</p><p>把三份报告连起来看，我看到了一条清晰的演进路径：<strong>2024 年设计师问「AI 能做什么」→ 2025 年设计师问「我该用哪个 AI 工具」→ 2026 年设计师问「AI 在我的工作流中应该扮演什么角色」→ 2027 年（我的预测）设计师将问「如果 AI 能做 80% 的工作，我的 20% 是什么」</strong>。这条路径的终点不是设计师消失，而是「设计师」这个角色的含义发生根本性变化。就像「程序员」在 2026 年的含义和 2020 年完全不同——不再是「写代码的人」，而是「用 AI 构建软件的人」——「设计师」也将从「画界面的人」变成「定义体验策略并用 AI 实现的人」。</p><p><strong>最后一个观察：RGD 提出的「客户透明度」原则可能比我们想象的更有商业影响。想象一下，如果行业达成共识要求设计师标注 AI 的参与程度，那些高度依赖 AI 的设计服务的定价权会被压缩，而「人类主导」的设计服务可能获得溢价——就像「手工」和「机器制造」在奢侈品行业的价值差异。AI 工具越普及，「人的判断力」越稀缺，这个悖论将定义设计行业未来十年的定价逻辑。</strong></p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Designfest Publishes 2026 AI Tools Guide: 'Design Is No Longer Just Drawing — It's AI-Augmented Workflows and Data-Driven Decisions'</strong> — Comprehensive guide covering Figma AI (multi-screen generation), UX Pilot AI (research-to-prototype), Visily (AI-powered rapid wireframing), and more. Key verdict: <strong>2026 UI/UX design has evolved from 'drawing' to 'AI-augmented workflows + data-driven decision-making.'</strong> Tools are categorized by role — UI designers use Figma AI + Visily, UX researchers use UX Pilot, front-end devs use Relume — reflecting AI's penetration across every design team function.<br><small>Source: <a href=\"https://designfest.framer.media/blogs/ai-tools-every-uiux-designer-should-try\">Designfest</a></small></li><li><strong>Muzli Designer's Field Report: 'The 8 AI Tools I Actually Use in My UX Workflow, and Why'</strong> — From Muzli (Design Inspiration community), a practitioner shares not just tools but detailed use cases and reasoning. Core insight: <strong>AI tool value isn't about capability — it's about seamless workflow integration.</strong> Also recommends Moonchild.ai's framework for building an effective AI design tool stack, signaling the community has moved from 'trying AI' to 'systematically integrating AI.'<br><small>Source: <a href=\"https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d\">Muzli / Medium</a></small></li><li><strong>Canada's RGD Issues Position: AI Should Support Creativity and Responsible Workflows, Not Replace Design Judgment</strong> — Professional design association RGD publishes a framework for AI in design, emphasizing three dimensions: <strong>creative sovereignty (designers retain final decision-making), ethical use (training data provenance and copyright), and client transparency (disclosing AI involvement).</strong> The first systematic institutional framing of the designer-AI relationship.<br><small>Source: <a href=\"https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026\">RGD</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>'AI-Augmented Workflows' as Industry Consensus</strong>: From tool reviews to professional association statements, 2026's design industry no longer debates 'whether to use AI' — focus shifts to 'AI's proper place in the workflow'</li><li><strong>From 'Trying Tools' to 'Building Tool Stacks'</strong>: Moonchild.ai's framework and Muzli's field report show designers systematically integrating AI, not randomly experimenting</li><li><strong>Professional Associations Enter AI Ethics</strong>: RGD's stance marks institutional-level response to AI challenges — creative sovereignty and client transparency may become industry standards</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>These three reports appear to say the same thing — 'AI tools are useful' — but beneath the surface lies a subtle, important divergence: should AI help designers decide, or just help them execute faster?</strong></p><p>Designfest represents the 'accelerate execution' camp: AI generates multi-screen UIs, rapid wireframes, front-end code. Value is measured by 'how much faster.' <strong>AI as turbocharger — designers go faster, but hands stay on the steering wheel.</strong></p><p>Muzli's field report hints at something more radical. UX Pilot AI generating design solutions from user research data isn't just 'faster execution' — it's <strong>'assisted decision-making.'</strong> When AI analyzes user data and recommends design approaches, designers shift from 'creators' to 'reviewers.' This mirrors the front-end developer transformation we discussed yesterday. <strong>Designers and developers are undergoing the same role redefinition — designers just haven't realized how far down the path they've gone.</strong></p><p>RGD's position paper is today's most thought-provoking piece. A professional association publicly discussing 'creative sovereignty' and 'client transparency' signals AI in design has escalated from technical topic to professional ethics issue. Their three dimensions answer a fundamental question: <strong>when AI participates in design, can the result still be called 'the designer's work'?</strong></p><p><strong>Connecting all three: 2024 designers asked 'what can AI do' → 2025 'which AI tool should I use' → 2026 'what role should AI play in my workflow' → 2027 (my prediction) 'if AI does 80% of the work, what's my 20%?' The endpoint isn't designers disappearing — it's the fundamental meaning of 'designer' changing. Just as 'programmer' in 2026 no longer means 'person who writes code' but 'person who builds software with AI.'</strong></p><p><strong>Final observation: RGD's 'client transparency' principle may have more commercial impact than expected. If the industry reaches consensus on disclosing AI involvement, heavily AI-dependent design services face pricing pressure, while 'human-led' design gains a premium — like 'handmade' vs 'machine-made' in luxury goods. The more ubiquitous AI tools become, the scarcer 'human judgment' gets. This paradox will define design's pricing logic for the next decade.</strong></p></div>"
    },
    "cover": design_cover,
    "sources": []
}

for i, (url, zh, en) in enumerate(design_sources):
    design_issue["sources"].append({
        "url": url,
        "title": {"zh": zh, "en": en},
        "image": design_images[i]
    })

# Build tech issue
tech_issue = {
    "date": "2026-05-09",
    "section": "tech",
    "title": {
        "zh": "Microsoft「去 OpenAI 化」提速：MAI 自研模型三件套上线 + AI 预发布审查扩大到欧洲 + SaaS 裁员潮加速——AI 正在同时重写科技巨头的联盟关系和就业市场的规则",
        "en": "Microsoft's 'De-OpenAI' Accelerates: MAI In-House Model Trio Launches + AI Pre-Release Review Expands to Europe + SaaS Layoffs Surge — AI Is Simultaneously Rewriting Big Tech Alliances and Job Market Rules"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Microsoft 发布 MAI 三件套自研模型：MAI-Transcribe-1（语音转文字）、MAI-Voice-1（语音生成）、MAI-Image-2（文生图），正式开启「去 OpenAI 化」</strong> — GeekWire 和 Business Insider 报道，Microsoft AI CEO Mustafa Suleyman 领导的 MAI 超级智能团队发布了三款完全自研的基础模型。MAI-Transcribe-1 在 FLEURS 基准测试中排名全球第一；MAI-Voice-1 能在单 GPU 上一秒内生成一分钟音频；MAI-Image-2 已在 Bing 和 PowerPoint 中上线。<strong>这是 Suleyman 2025 年 11 月宣布要让 Microsoft「在 AI 上自给自足」后的第一个重大兑现。</strong>三款模型均通过 Microsoft Foundry 和 MAI Playground 提供，不依赖 OpenAI 的任何技术栈。<br><small>来源：<a href=\"https://www.geekwire.com/2026/microsoft-releases-new-ai-models-to-further-expand-beyond-openai/\">GeekWire</a> / <a href=\"https://www.businessinsider.com/microsoft-ai-models-azure-mai-transcribe-voice-image-foundry-openai-2026-4\">Business Insider</a></small></li><li><strong>AI 预发布政府审查从美国扩展到欧洲：Euronews 确认 Google、Microsoft、xAI 已正式接受 CAISI 评估</strong> — Euronews 报道（5月8日），美国商务部 CAISI 的 AI 预发布审查项目正式启动。Microsoft 首席负责 AI 官 Natasha Crampton 表示，CAISI 评估将帮助「提前发现 AI 网络攻击等风险」。OpenAI 也在与 CAISI 合作测试 GPT-5.5-Cyber。<strong>值得注意的是，Microsoft 同时与英国 AISI 签署了类似协议——这意味着 AI 安全审查正在跨国制度化。</strong>特朗普政府此前一直主张减少 AI 监管，但安全威胁的现实迫使其改变立场。<br><small>来源：<a href=\"https://www.euronews.com/next/2026/05/08/tech-giants-agree-to-us-government-ai-testing\">Euronews</a> / <a href=\"https://www.foxbusiness.com/technology/trump-admin-review-ai-models-from-google-microsoft-xai-ahead-public-release\">Fox Business</a></small></li><li><strong>2026 年 5 月科技裁员加速：Cloudflare、Upwork、Coinbase 等公司大规模裁员，AI 重构正在吞噬 SaaS 岗位</strong> — Yahoo Finance 报道，5 月裁员潮波及多个科技公司，原因直指 AI 对传统工作流的替代。一篇引发广泛讨论的 Substack 分析指出：<strong>在财报电话会议上谈论 AI 最多的 SaaS 公司，股价表现最差</strong>——因为它们谈的不是「AI 机会」，而是在掩饰 AI 对自身业务的结构性威胁。一家金融科技公司用内部 AI 系统替换了 Salesforce、砍掉了 1,200 个 SaaS 供应商、裁掉了 700 个全职岗位。<br><small>来源：<a href=\"https://finance.yahoo.com/sectors/technology/articles/layoffs-accelerate-may-2026-firms-040430218.html\">Yahoo Finance</a> / <a href=\"https://eventhorizoniq.substack.com/p/im-short-asana-salesforce-five9-docusign\">EventHorizon IQ</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>Microsoft-OpenAI 联盟正在从「共生」走向「竞争」</strong>：MAI 自研模型 + 2025 年 10 月解除排他性条款 = Microsoft 正在构建不依赖 OpenAI 的完整 AI 栈</li><li><strong>AI 安全审查跨国化</strong>：美国 CAISI + 英国 AISI + 即将跟进的欧盟 AI Act = 全球统一的 AI 预发布审查框架正在成型</li><li><strong>SaaS 行业进入「AI 替代潮」</strong>：企业用 AI 替换整个 SaaS 工具栈（而非在 SaaS 中添加 AI 功能）——这是 SaaS 行业最恐惧的场景</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天这三条新闻分别指向 AI 行业的三个深层结构变化：联盟瓦解、监管成型、就业重构。把它们放在一起看，2026 年的 AI 行业正在从「狂飙突进」进入「秩序重建」。</strong></p><p>先说最有戏剧性的一条：Microsoft 发布 MAI 三件套。表面看，这是一次产品发布；实质上，<strong>这是 Microsoft 向 OpenAI 发出的「独立宣言」</strong>。回顾时间线：2025 年 10 月，Microsoft 和 OpenAI 修改协议，允许双方「独立或与第三方合作追求 AGI」；11 月，Suleyman 组建超级智能团队，宣布要让 Microsoft「在 AI 上自给自足」；2026 年 4 月，MAI 三件套发布。从语音到图像到文字，Microsoft 现在有了一套完全不依赖 OpenAI 的多模态 AI 栈。这不是说 Microsoft 会立刻抛弃 OpenAI——Azure 的 ChatGPT 收入太大了——但 <strong>Microsoft 正在确保自己「有得选」</strong>。在商业世界里，能走但选择不走，和不得不留，是完全不同的谈判地位。</p><p>Suleyman 选择语音和图像作为首批发布的模型品类，而非 LLM，这个策略值得品味。<strong>他避开了 OpenAI 最强的领域（文本生成），瞄准了 OpenAI 相对薄弱、但商业价值巨大的领域（语音、图像）。</strong>MAI-Voice-1 能一秒生成一分钟音频、MAI-Transcribe-1 全球精度第一——这些能力直接服务于 Teams、Copilot、PowerPoint 等 Microsoft 的核心产品线。换句话说，Suleyman 不是在和 OpenAI 竞争 ChatGPT，他是在让 Microsoft 的产品矩阵摆脱对 OpenAI API 的依赖。这比直接竞争更聪明，也更危险——因为一旦 Microsoft 证明自研模型能支撑产品体验，OpenAI 对 Microsoft 的战略价值就会持续下降。</p><p>AI 预发布审查扩展到英国，这条新闻的意义被大多数人低估了。<strong>当同一家公司（Microsoft）同时接受美国 CAISI 和英国 AISI 的审查时，一个事实上的跨国 AI 监管框架正在形成</strong>——不是通过国际条约（那会花十年），而是通过企业的「自愿」合规。我打引号是因为这种「自愿」在商业层面是半强制的：如果你不接受审查，你的竞争对手接受了，你在政府采购和公众信任方面就处于劣势。加上欧盟 AI Act 已经生效，2026 年底我们可能会看到一个覆盖美英欧的 AI 安全审查网络。<strong>对创业公司来说，这既是壁垒（合规成本）也是机会（合规即信任），但毫无疑问，这会加速 AI 行业的巨头化——小公司根本没有资源同时满足多国审查。</strong></p><p><strong>最后说裁员。那篇 Substack 分析的核心洞察值得每个 SaaS 从业者读三遍：「在财报电话会议上谈论 AI 最多的公司，股价表现最差。」这不是巧合，这是因果——<strong>当 CEO 在财报里拼命强调「AI 是机会」时，市场听到的是「AI 正在摧毁我们的护城河」</strong>。一家金融科技公司替换 Salesforce + 砍掉 1,200 个 SaaS 供应商 + 裁 700 人——这个案例揭示了 AI 对 SaaS 的威胁模式：不是「在 SaaS 中加 AI」（这是 SaaS 公司自己的叙事），而是「用 AI 替换 SaaS」（这是客户的真实行为）。Asana、Salesforce、DocuSign、Atlassian——这些公司卖的都是结构化工作流（填表、路由工单、追踪任务），而 AI agent 正在让这些工作流变得不必要。设计师注意：你用的 Figma 暂时安全，因为它卖的是创作工具而非工作流自动化。但如果 Figma 的竞争对手找到了「AI agent 直接生成完整产品」的路径，Figma 的护城河也不是不可逾越的。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Microsoft Launches MAI In-House Model Trio: MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2 — Officially Beginning 'De-OpenAI' Strategy</strong> — GeekWire and Business Insider report that Mustafa Suleyman's MAI team released three fully in-house foundation models. MAI-Transcribe-1 ranks #1 globally on FLEURS benchmark; MAI-Voice-1 generates one minute of audio in under one second on a single GPU; MAI-Image-2 is live in Bing and PowerPoint. <strong>This is the first major delivery on Suleyman's November 2025 pledge to make Microsoft 'self-sufficient in AI.'</strong><br><small>Source: <a href=\"https://www.geekwire.com/2026/microsoft-releases-new-ai-models-to-further-expand-beyond-openai/\">GeekWire</a> / <a href=\"https://www.businessinsider.com/microsoft-ai-models-azure-mai-transcribe-voice-image-foundry-openai-2026-4\">Business Insider</a></small></li><li><strong>AI Pre-Release Government Review Expands from US to UK: CAISI Programme Officially Launches</strong> — Euronews reports (May 8) that CAISI pre-deployment evaluations are now active. Microsoft also signed a parallel agreement with UK's AISI. <strong>AI safety review is becoming cross-border institutional.</strong> Trump administration, previously anti-regulation, reversed course under pressure from real security threats.<br><small>Source: <a href=\"https://www.euronews.com/next/2026/05/08/tech-giants-agree-to-us-government-ai-testing\">Euronews</a> / <a href=\"https://www.foxbusiness.com/technology/trump-admin-review-ai-models-from-google-microsoft-xai-ahead-public-release\">Fox Business</a></small></li><li><strong>May 2026 Tech Layoffs Accelerate: AI Restructuring Swallows SaaS Jobs</strong> — Yahoo Finance reports wave of layoffs at Cloudflare, Upwork, Coinbase, and others. A viral Substack analysis reveals: <strong>SaaS companies that talk about AI most on earnings calls have the worst stock returns</strong> — because they're compensating for AI structurally destroying their business model. One fintech company replaced Salesforce, cut 1,200 SaaS vendors, and eliminated 700 FTE roles with an internal AI system.<br><small>Source: <a href=\"https://finance.yahoo.com/sectors/technology/articles/layoffs-accelerate-may-2026-firms-040430218.html\">Yahoo Finance</a> / <a href=\"https://eventhorizoniq.substack.com/p/im-short-asana-salesforce-five9-docusign\">EventHorizon IQ</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>Microsoft-OpenAI Alliance Shifting from Symbiosis to Competition</strong>: MAI in-house models + October 2025 exclusivity removal = Microsoft building a complete AI stack independent of OpenAI</li><li><strong>AI Safety Review Goes Cross-Border</strong>: US CAISI + UK AISI + incoming EU AI Act = global unified AI pre-release review framework forming</li><li><strong>SaaS Industry Enters 'AI Replacement Wave'</strong>: Enterprises replacing entire SaaS stacks with AI (not adding AI to SaaS) — the SaaS industry's most feared scenario</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>These three stories point to three deep structural shifts in AI: alliance dissolution, regulation formation, employment restructuring. Together, 2026's AI industry is transitioning from 'breakneck growth' to 'order reconstruction.'</strong></p><p>The MAI trio launch is surface-level a product release; substantively, <strong>it's Microsoft's 'declaration of independence' from OpenAI.</strong> Timeline: October 2025 exclusivity removal → November Suleyman forms superintelligence team pledging AI self-sufficiency → April 2026 MAI trio ships. Microsoft now has a complete multimodal AI stack independent of OpenAI. This doesn't mean they'll abandon OpenAI tomorrow — Azure's ChatGPT revenue is too large — but <strong>Microsoft is ensuring it 'has options.'</strong> In business, being able to leave but choosing to stay is a fundamentally different negotiating position than having to stay.</p><p>Suleyman's choice to launch voice and image models first (not LLMs) deserves attention. <strong>He avoided OpenAI's strongest domain (text generation) and targeted relatively weaker but commercially massive areas (voice, image).</strong> MAI-Voice-1 and MAI-Transcribe-1 directly serve Teams, Copilot, PowerPoint — Microsoft's core product lines. He's not competing with ChatGPT; he's making Microsoft's product matrix independent of OpenAI's API. Smarter and more dangerous — once Microsoft proves in-house models can power product experiences, OpenAI's strategic value to Microsoft continuously declines.</p><p>AI review expanding to the UK is underestimated. <strong>When the same company (Microsoft) submits to both US CAISI and UK AISI review, a de facto cross-border AI regulatory framework emerges</strong> — not through treaties (that takes a decade) but through corporate 'voluntary' compliance. For startups, this is both barrier (compliance cost) and opportunity (compliance as trust), but undeniably accelerates big-tech consolidation.</p><p><strong>The layoffs story's core insight deserves re-reading: 'SaaS companies that talk about AI most on earnings calls have the worst stock returns.' This isn't coincidence — it's causation. When CEOs desperately emphasize 'AI is an opportunity,' the market hears 'AI is destroying our moat.' One fintech replacing Salesforce + cutting 1,200 SaaS vendors + eliminating 700 roles reveals AI's real threat to SaaS: not 'adding AI to SaaS' (the vendor narrative) but 'replacing SaaS with AI' (the customer's actual behavior). Designers note: Figma is temporarily safe because it sells creative tools, not workflow automation. But if a competitor finds the 'AI agent generates complete products' path, Figma's moat isn't unbreachable either.</strong></p></div>"
    },
    "cover": tech_cover,
    "sources": []
}

for i, (url, zh, en) in enumerate(tech_sources):
    tech_issue["sources"].append({
        "url": url,
        "title": {"zh": zh, "en": en},
        "image": tech_images[i]
    })

# Load existing issues and prepend
issues_path = "/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json"
with open(issues_path, 'r', encoding='utf-8') as f:
    issues = json.load(f)

issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open(issues_path, 'w', encoding='utf-8') as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Inserted 2 new issues (design + tech) for 2026-05-09. Total issues: {len(issues)}")
