#!/usr/bin/env python3
"""Rex Daily update for 2026-05-11"""
import json, os, sys
from urllib.request import urlopen, Request
from html.parser import HTMLParser
import re

# --- OG image fetcher ---
class OGImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.og_image = ""
    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            d = dict(attrs)
            if d.get("property") == "og:image" or d.get("name") == "og:image":
                self.og_image = d.get("content", "")

def get_og_image(url, timeout=10):
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=timeout) as resp:
            html = resp.read(50000).decode("utf-8", errors="ignore")
        p = OGImageParser()
        p.feed(html)
        return p.og_image
    except:
        return ""

# --- Fetch OG images ---
urls_design = [
    "https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/",
    "https://www.flatlineagency.com/blog/ai-design-tools-for-brands-2026/",
    "https://aitoolanalysis.com/claude-design-review/",
]
urls_tech = [
    "https://openai.com/index/introducing-gpt-5-5/",
    "https://press.airstreet.com/p/state-of-ai-may-2026",
    "https://www.latimes.com/business/story/2026-05-08/data-center-startup-fermi-promised-nuclear-power-for-ai-but-it-couldnt-sign-single-client",
    "https://www.cnbc.com/2026/05/07/openai-rolls-out-new-gpt-5point5-cyber-to-vetted-cybersecurity-teams.html",
]

print("Fetching OG images...")
og = {}
for u in urls_design + urls_tech:
    img = get_og_image(u)
    og[u] = img
    print(f"  {u[:60]}... -> {img[:80] if img else '(none)'}")

# --- Build issues ---
design_issue = {
    "date": "2026-05-11",
    "section": "design",
    "title": {
        "zh": "Anthropic 发布 Claude Design 正面挑战 Figma + 实测 30 分钟烧光 Pro 配额 + 2026 品牌设计工具版图重组——当 AI 巨头开始做设计工具，设计行业的「平台战争」进入新阶段",
        "en": "Anthropic Launches Claude Design to Challenge Figma + Pro Quota Burns Out in 30 Minutes + 2026 Brand Design Tool Landscape Reshuffles — When AI Giants Build Design Tools, the Platform War Enters a New Phase"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Anthropic 推出 Claude Design：用自然语言生成原型、幻灯片和 one-pager——定位「给非设计师的设计工具」</strong> — Anthropic 于 4 月 17 日正式发布 Claude Design，一个内置于 Claude 的对话式 AI 设计工具。用户可以用自然语言描述需求，Claude Design 会生成可编辑的原型、演示文稿、产品页面等视觉内容。<strong>Anthropic 明确表示这是为创始人、产品经理和非设计背景的人设计的</strong>——不是要替代 Figma，而是填补「有想法但不会画」的缺口。Claude Design 有独立的使用配额，与常规对话分开计算。<br><small>来源：<a href=\"https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/\">TechCrunch</a></small></li><li><strong>实测评价：Claude Design 的 Pro 配额 30 分钟就能烧光，设计质量「够用但不够精」</strong> — AI Tool Analysis 的深度评测揭示了 Claude Design 的现实困境：Pro 计划用户的设计配额在 30 分钟密集使用后就会耗尽。评测指出，Claude Design 在快速原型和概念验证上表现出色，但在视觉精致度和复杂交互设计上仍然远不如 Figma。<strong>核心问题是：它的输出质量取决于 prompt 质量——对于不了解设计原则的非设计师来说，这反而形成了一个新的「隐形门槛」。</strong><br><small>来源：<a href=\"https://aitoolanalysis.com/claude-design-review/\">AI Tool Analysis</a></small></li><li><strong>Flatline Agency 发布 2026 品牌设计工具年度报告：Figma、Claude Design、Framer、Canva AI 2.0、Midjourney 五强争锋</strong> — 报告指出，截至 2026 年 4 月，品牌和电商团队最需要关注的五款 AI 设计工具各有分工：Figma 仍是 UI/UX 标准，Claude Design 填补概念验证空白，Framer 主打设计到上线的一体化，Canva AI 2.0 服务非设计师的批量生产需求，Midjourney 专攻高质量视觉创意。<strong>关键洞察：没有一个工具能通吃全链路，但「工具栈整合」正在成为团队效率的核心变量。</strong><br><small>来源：<a href=\"https://www.flatlineagency.com/blog/ai-design-tools-for-brands-2026/\">Flatline Agency</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 巨头切入设计赛道</strong>：Anthropic（Claude Design）、Google（Stitch）、Microsoft（Designer）纷纷推出设计工具，设计不再是设计公司的专属领域</li><li><strong>「设计民主化」的双刃剑</strong>：非设计师能更快产出视觉内容，但 prompt 质量成为新的隐形门槛——「会提问题」比「会画画」更重要</li><li><strong>工具栈整合 vs 单一平台</strong>：Figma 走全栈路线，其他工具各占一个生态位——团队的选择取决于是要「一个平台搞定一切」还是「最佳组合拳」</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Anthropic 做 Claude Design，Google 做 Stitch，Microsoft 做 Designer——三大 AI 巨头在同一个季度里都推出了自己的设计工具。这不是巧合，这是一个信号：设计正在从「专业工具领域」变成「AI 平台的标配功能」。</strong></p><p>让我解释为什么这件事比表面上看起来重要得多。过去十年，设计工具市场的竞争逻辑是「专业 vs 更专业」——Sketch vs Figma vs Adobe XD，比的是谁更懂设计师的工作流。但 Claude Design 的定位彻底改变了竞争维度：<strong>它不是给设计师用的，它是给「所有需要视觉输出但不会设计」的人用的。</strong>这意味着设计工具的 TAM（Total Addressable Market）从全球 300 万设计师扩大到了全球 3 亿知识工作者。</p><p>但 AI Tool Analysis 的评测揭示了一个被 Anthropic 市场宣传掩盖的关键矛盾：<strong>Claude Design 30 分钟烧光 Pro 配额的事实，暴露了一个根本性的商业模式问题。</strong>设计是一个需要反复迭代的过程——你不会一次 prompt 就得到满意的结果，你需要 5 次、10 次、20 次的调整。每次调整都消耗配额。如果一个 $20/月 的 Pro 用户 30 分钟就用完了设计配额，那要么 Anthropic 提高价格（赶走价格敏感用户），要么降低模型推理成本（牺牲输出质量），要么接受设计功能是一个高成本的获客工具而非利润中心。我的判断：<strong>Claude Design 目前是 Anthropic 的「特洛伊木马」——用设计功能把非技术用户拉进 Claude 生态，然后在其他场景（写作、分析、代码）上变现。</strong></p><p>更有意思的是 Flatline Agency 的五强版图分析。它清楚地展示了 2026 年设计工具市场的「分层结构」：<strong>Figma 是「专业设计师的操作系统」，Claude Design 是「非设计师的快速原型」，Canva AI 2.0 是「营销团队的批量生产线」，Framer 是「设计师的独立发布平台」，Midjourney 是「创意探索的灵感引擎」。</strong>注意这个分层——它不是按功能分的，是按<strong>用户身份</strong>分的。每个工具服务的是不同的人群，解决的是不同层面的问题。</p><p>把这个趋势和上周讨论的「中间层塌陷」联系起来看：<strong>Claude Design 等工具正在加速这个塌陷。</strong>当一个产品经理可以用 Claude Design 在 30 分钟内产出一个「80 分」的原型时，他还需要一个初级设计师帮他画线框图吗？当 Canva AI 2.0 可以让营销实习生批量产出社交媒体素材时，还需要一个平面设计师做日常出图吗？答案越来越明确：<strong>不需要。</strong>但与此同时，当 AI 产出的设计越来越同质化时，能做出真正差异化体验的高级设计师的价值反而在上升。Figma 的 Make + Sites + Design 全栈战略正是在服务这个群体——他们不需要 AI 帮他们想，他们需要 AI 帮他们更快地实现自己已经想好的东西。</p><p><strong>我的预测：到 2026 年底，「AI 设计工具」这个品类会消失——不是因为失败了，而是因为设计功能会成为每个 AI 平台的内置能力，就像今天的拼写检查一样普遍。真正的竞争将不再是「哪个 AI 工具能生成更好的设计」，而是「哪个平台能提供更完整的从想法到上线的工作流」。在这个竞争中，Figma 和 Anthropic 最终会变成合作伙伴而非竞争者——Figma 提供专业设计引擎，Claude 提供自然语言理解和推理能力，两者通过 MCP 协议连接。事实上，Figma MCP Server 已经在做这件事了。</strong></p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Anthropic Launches Claude Design: Natural Language Prototyping for Non-Designers</strong> — Anthropic officially released Claude Design on April 17, a conversational AI design tool built into Claude. Users describe needs in natural language and get editable prototypes, presentations, and one-pagers. <strong>Anthropic explicitly positioned it for founders, PMs, and non-designers</strong> — not to replace Figma, but to fill the gap between 'having an idea' and 'knowing how to visualize it.'<br><small>Source: <a href=\"https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/\">TechCrunch</a></small></li><li><strong>Reality Check: Claude Design Burns Through Pro Quota in 30 Minutes</strong> — AI Tool Analysis's in-depth review reveals Claude Design's practical limitation: Pro plan design quota depletes in 30 minutes of intensive use. The tool excels at rapid prototyping but falls short on visual polish and complex interactions compared to Figma. <strong>Core paradox: output quality depends on prompt quality — creating a new 'invisible barrier' for the very non-designers it targets.</strong><br><small>Source: <a href=\"https://aitoolanalysis.com/claude-design-review/\">AI Tool Analysis</a></small></li><li><strong>Flatline Agency's 2026 Brand Design Tool Report: Five-Way Contest Between Figma, Claude Design, Framer, Canva AI 2.0, and Midjourney</strong> — Each tool owns a distinct workflow niche: Figma remains the UI/UX standard, Claude Design fills concept validation gaps, Framer handles design-to-launch, Canva AI 2.0 serves non-designer mass production, Midjourney leads creative exploration. <strong>Key insight: no single tool covers the full pipeline, but 'tool stack consolidation' is becoming the core efficiency variable.</strong><br><small>Source: <a href=\"https://www.flatlineagency.com/blog/ai-design-tools-for-brands-2026/\">Flatline Agency</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Giants Entering the Design Arena</strong>: Anthropic (Claude Design), Google (Stitch), Microsoft (Designer) all launched design tools — design is becoming a standard AI platform feature</li><li><strong>Design Democratization's Double Edge</strong>: Non-designers can produce visuals faster, but prompt quality creates a new invisible barrier</li><li><strong>Tool Stack Integration vs. Single Platform</strong>: Figma pursues full-stack while others carve niches — teams choose between 'one platform for everything' or 'best-of-breed combinations'</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Anthropic built Claude Design, Google built Stitch, Microsoft built Designer — three AI giants shipped design tools in the same quarter. This isn't coincidence; it's a signal: design is shifting from 'specialized tool domain' to 'standard AI platform feature.'</strong></p><p>Why this matters more than it seems: for the past decade, design tool competition was about 'professional vs. more professional' — Sketch vs. Figma vs. Adobe XD. Claude Design changes the competitive dimension entirely: <strong>it's not for designers, it's for everyone who needs visual output but can't design.</strong> This expands the TAM from 3 million designers to 300 million knowledge workers globally.</p><p>But AI Tool Analysis's review reveals a key contradiction hidden by Anthropic's marketing: <strong>burning through Pro quota in 30 minutes exposes a fundamental business model problem.</strong> Design requires iterative refinement — 5, 10, 20 prompt adjustments, each consuming quota. My take: <strong>Claude Design is currently Anthropic's 'Trojan horse' — using design features to pull non-technical users into the Claude ecosystem, then monetizing through other use cases (writing, analysis, code).</strong></p><p>Flatline Agency's five-way landscape analysis clearly shows 2026's design tool 'stratification': <strong>Figma is 'the designer's OS,' Claude Design is 'non-designer rapid prototyping,' Canva AI 2.0 is 'marketing's production line,' Framer is 'designers' indie publishing platform,' Midjourney is 'the creative exploration engine.'</strong> Note: stratification is by user identity, not by feature.</p><p><strong>My prediction: by late 2026, 'AI design tool' as a category will disappear — not from failure, but because design becomes a built-in capability of every AI platform, like spell-check today. The real competition shifts to 'which platform delivers the most complete idea-to-launch workflow.' Figma and Anthropic will ultimately become partners, not competitors — Figma providing the professional design engine, Claude providing NLU and reasoning, connected via MCP protocol. Figma MCP Server is already making this happen.</strong></p></div>"
    },
    "cover": og.get(urls_design[0], ""),
    "sources": [
        {
            "url": "https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/",
            "title": {"zh": "Anthropic 推出 Claude Design：快速创建视觉内容的新产品", "en": "Anthropic Launches Claude Design for Creating Quick Visuals"},
            "image": og.get(urls_design[0], "")
        },
        {
            "url": "https://aitoolanalysis.com/claude-design-review/",
            "title": {"zh": "Claude Design 评测 2026：Pro 配额 30 分钟烧光", "en": "Claude Design Review 2026: Pro Quotas Burn Out in 30 Minutes"},
            "image": og.get(urls_design[2], "")
        },
        {
            "url": "https://www.flatlineagency.com/blog/ai-design-tools-for-brands-2026/",
            "title": {"zh": "2026 年品牌 AI 设计工具：重塑创意工作流的 5 款工具", "en": "AI Design Tools for Brands: 5 Tools Shaping Creative Workflows in 2026"},
            "image": og.get(urls_design[1], "")
        }
    ]
}

tech_issue = {
    "date": "2026-05-11",
    "section": "tech",
    "title": {
        "zh": "GPT-5.5 发布主攻 Agentic 任务 + OpenAI 推出网络安全专用模型 + Microsoft 自研 MAI 三模型宣告「去 OpenAI 化」+ Air Street 报告：独家平台绑定时代终结——AI 行业的权力重组正在加速",
        "en": "GPT-5.5 Launches for Agentic Tasks + OpenAI Ships Cybersecurity-Specific Model + Microsoft's In-House MAI Models Signal Independence from OpenAI + Air Street Report: The Era of Exclusive Platform Bets Is Over — AI's Power Redistribution Accelerates"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>OpenAI 发布 GPT-5.5：从聊天机器人到「自主代理」的关键一步</strong> — OpenAI 于 4 月 23 日发布 GPT-5.5，定位为面向高级 agentic 任务的模型。与 GPT-5.4 相比，GPT-5.5 在规划、工具使用和多步推理上有显著提升。ARC-AGI-1 验证得分达到 95.0%，ARC-AGI-2 达到 85.0%（超过 Opus 4.7 的 75.8%）。<strong>值得注意的是 Gemini 3.1 Pro 在 ARC-AGI-1 上以 98.0% 的得分超过了 GPT-5.5——Google 在抽象推理上依然领先。</strong><br><small>来源：<a href=\"https://openai.com/index/introducing-gpt-5-5/\">OpenAI</a></small></li><li><strong>OpenAI 推出 GPT-5.5-Cyber：首个垂直行业专用变体，向审核过的网络安全团队限量开放</strong> — CNBC 5 月 7 日报道，OpenAI 发布了 GPT-5.5 的网络安全专用版本，训练时刻意放宽了安全类任务的限制。这是 OpenAI 首次为特定垂直领域定制模型变体，<strong>标志着 AI 模型从「通用大模型」向「行业专用模型」的转型开始加速</strong>。同期，Anthropic 的 Claude Mythos Preview 也在吸引华尔街和政府机构的关注。<br><small>来源：<a href=\"https://www.cnbc.com/2026/05/07/openai-rolls-out-new-gpt-5point5-cyber-to-vetted-cybersecurity-teams.html\">CNBC</a></small></li><li><strong>Microsoft 自研三大 AI 基础模型（MAI-Transcribe-1、MAI-Voice-1、MAI-Image-2），「去 OpenAI 化」信号明确</strong> — Microsoft 发布三款自研 AI 模型，分别覆盖语音转文字、语音生成和图像生成，全部独家上线 Foundry 平台。MAI-Transcribe-1 支持 25 种语言，速度是 Azure Fast 的 2.5 倍。<strong>更关键的是 Microsoft Foundry 现在同时提供 OpenAI、Anthropic Opus 4.7 和 Google 的模型——Microsoft 正在从「OpenAI 独家合作伙伴」变成「所有前沿模型的中立平台」。</strong><br><small>来源：<a href=\"https://www.businessinsider.com/microsoft-ai-models-azure-mai-transcribe-voice-image-foundry-openai-2026-4\">Business Insider</a> / <a href=\"https://www.zacks.com/stock/news/2895639/msft-deepens-ai-strategy-with-new-foundational-models-whats-ahead\">Zacks</a></small></li><li><strong>Air Street Capital「State of AI: May 2026」报告：独家平台绑定时代正式终结</strong> — 知名 AI 投资机构 Air Street Capital 在 5 月月报中指出：Microsoft 不再受单一供应商约束，在 Foundry 上积极上线所有前沿模型；Anthropic 也将 Claude 部署在 AWS、Google Cloud 和 Azure 三大云上。<strong>报告的核心判断：「多元化是唯一可防御的基础设施策略」——独家绑定的时代已经结束。</strong><br><small>来源：<a href=\"https://press.airstreet.com/p/state-of-ai-may-2026\">Air Street Press</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 模型从通用走向行业专用</strong>：GPT-5.5-Cyber 是第一个明确的信号——未来每个垂直行业都会有自己的「定制 AI」</li><li><strong>平台绑定时代终结</strong>：Microsoft 同时上线 OpenAI、Anthropic、Google 模型；Anthropic 同时部署在三大云——AI 平台正在变成「模型超市」</li><li><strong>Microsoft「去 OpenAI 化」加速</strong>：自研 MAI 模型 + Foundry 平台多模型策略 = Microsoft 正在降低对 OpenAI 的依赖</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>把本周几条新闻放在一起，你会看到 AI 行业正在经历一次深层的「权力重组」——不是谁的模型更好的问题，而是谁控制分发渠道、谁拥有客户关系、谁掌握基础设施的问题。</strong></p><p>先说 GPT-5.5。OpenAI 的 benchmark 数字很好看：ARC-AGI-1 达到 95.0%，ARC-AGI-2 达到 85.0%。但真正的故事不在数字里——<strong>在于 OpenAI 选择了「agentic」作为 GPT-5.5 的核心定位。</strong>这是一个战略选择：聊天（chat）市场已经被免费版 ChatGPT 和开源模型吃掉了大部分，利润微薄。但 agentic 任务——让 AI 自主规划、调用工具、完成多步骤工作流——是一个全新的、高价值的市场。一个能帮企业自动化复杂工作流的 AI agent 的价值，远高于一个聊天机器人。GPT-5.5-Cyber 就是这个战略的第一个落地：<strong>把通用模型调教成垂直行业的自动化专家。</strong></p><p>但这里有一个 OpenAI 可能不愿意面对的现实：Gemini 3.1 Pro 在 ARC-AGI-1 上以 98.0% 对 95.0% 赢了 GPT-5.5。这不是一个小差距——<strong>在抽象推理这个被认为是 AGI 核心能力的维度上，Google 依然领先。</strong>联系上 LA Times 那篇「Google 的内部挣扎正在把 AI 编程赛道拱手让给 Anthropic 和 OpenAI」的报道，你会看到一个有趣的矛盾：Google 有最强的模型，但在产品化和市场执行上一塌糊涂。这就像一个有天赋的运动员输给了一个训练更刻苦的对手。</p><p>再说 Microsoft。自研 MAI 三模型 + Foundry 平台多模型策略，这两件事放在一起的含义很清楚：<strong>Microsoft 正在从「OpenAI 的独家分销商」变成「AI 行业的 App Store」。</strong>Air Street Capital 的报告一针见血：「独家平台绑定时代终结，多元化是唯一可防御的策略。」翻译成大白话就是：Microsoft 不再把赌注全压在 OpenAI 上了。Foundry 同时提供 GPT-5.5、Opus 4.7 和 Gemini——客户爱用哪个用哪个，Microsoft 只关心「他们是不是在我的平台上用」。这对 OpenAI 的影响是深远的：<strong>如果 Microsoft 既是你最大的投资人又是你最大的竞争对手，你的日子不会好过。</strong></p><p><strong>最后把设计和科技板块连起来看。Claude Design 的推出和 Microsoft Foundry 的多模型策略其实是同一个大趋势的两个表现：「AI 能力的商品化」。当 Anthropic 把「设计」变成 Claude 的一个免费内置功能，当 Microsoft 把所有前沿模型放在同一个货架上供客户挑选——AI 的差异化正在从「模型能力」转向「生态系统和工作流」。就像智能手机市场：最终胜出的不是芯片最强的手机（那应该是某个安卓旗舰），而是生态系统最完整的 iPhone。AI 行业正在进入同样的阶段。谁能把模型能力、开发者工具、行业解决方案和分发渠道整合成一个无缝体验，谁就赢了。从这个角度看，Microsoft 的位置比任何人都好——它有 Azure 的基础设施、Office 的用户基础、GitHub 的开发者社区和 Foundry 的模型超市。OpenAI 有最好的品牌和消费者用户，但没有企业分发渠道。Anthropic 有最好的安全叙事和技术口碑，但商业化还在早期。Google 有最强的模型，但连自己的产品线都整合不好。这场仗远没有结束。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>OpenAI Launches GPT-5.5: The Critical Step from Chatbot to Autonomous Agent</strong> — Released April 23, GPT-5.5 targets advanced agentic tasks with significant improvements in planning, tool use, and multi-step reasoning. ARC-AGI-1 verified score reaches 95.0%, ARC-AGI-2 reaches 85.0%. <strong>Notable: Gemini 3.1 Pro beats GPT-5.5 on ARC-AGI-1 with 98.0% — Google still leads in abstract reasoning.</strong><br><small>Source: <a href=\"https://openai.com/index/introducing-gpt-5-5/\">OpenAI</a></small></li><li><strong>OpenAI Ships GPT-5.5-Cyber: First Industry-Specific Model Variant for Cybersecurity</strong> — CNBC reports (May 7) OpenAI released a cybersecurity-tuned GPT-5.5 variant with relaxed safety restrictions for security tasks. <strong>This signals acceleration of the shift from 'general-purpose AI' to 'industry-specific AI.'</strong><br><small>Source: <a href=\"https://www.cnbc.com/2026/05/07/openai-rolls-out-new-gpt-5point5-cyber-to-vetted-cybersecurity-teams.html\">CNBC</a></small></li><li><strong>Microsoft Launches Three In-House AI Models, Signaling Independence from OpenAI</strong> — Microsoft released MAI-Transcribe-1, MAI-Voice-1, and MAI-Image-2, exclusively on its Foundry platform. <strong>More critically, Foundry now offers OpenAI, Anthropic Opus 4.7, and Google models simultaneously — Microsoft is becoming 'the neutral platform for all frontier models.'</strong><br><small>Source: <a href=\"https://www.businessinsider.com/microsoft-ai-models-azure-mai-transcribe-voice-image-foundry-openai-2026-4\">Business Insider</a> / <a href=\"https://www.zacks.com/stock/news/2895639/msft-deepens-ai-strategy-with-new-foundational-models-whats-ahead\">Zacks</a></small></li><li><strong>Air Street Capital 'State of AI: May 2026': The Era of Exclusive Platform Bets Is Officially Over</strong> — Microsoft aggressively ships every frontier model on Foundry; Anthropic deploys Claude across AWS, Google Cloud, and Azure. <strong>Core thesis: 'Diversification is the only defensible infrastructure play.'</strong><br><small>Source: <a href=\"https://press.airstreet.com/p/state-of-ai-may-2026\">Air Street Press</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Models: From General-Purpose to Industry-Specific</strong>: GPT-5.5-Cyber is the first clear signal — every vertical will get its own 'custom AI'</li><li><strong>End of Platform Lock-In</strong>: Microsoft offers OpenAI + Anthropic + Google simultaneously; Anthropic deploys across three clouds — AI platforms becoming 'model supermarkets'</li><li><strong>Microsoft's 'De-OpenAI-ification' Accelerates</strong>: In-house MAI models + multi-model Foundry = systematic reduction of OpenAI dependency</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Connect this week's stories and you see AI undergoing a deep 'power redistribution' — not about whose model is better, but who controls distribution, who owns customer relationships, who holds infrastructure.</strong></p><p>GPT-5.5's numbers look good: 95.0% on ARC-AGI-1, 85.0% on ARC-AGI-2. But the real story is OpenAI choosing 'agentic' as GPT-5.5's core positioning — a strategic bet that the chat market has been commoditized by free ChatGPT and open-source models. <strong>Agentic tasks — AI autonomously planning, using tools, completing multi-step workflows — represent a new, high-value market.</strong> GPT-5.5-Cyber is the first landing: turning general models into vertical automation experts.</p><p>But there's a reality OpenAI may not want to face: Gemini 3.1 Pro beat GPT-5.5 on ARC-AGI-1 (98.0% vs 95.0%). <strong>On abstract reasoning — considered the core AGI capability — Google still leads.</strong> Yet LA Times reports Google's internal fragmentation is handing the AI coding race to Anthropic and OpenAI. An interesting paradox: Google has the strongest model but can't execute on product and market. Like a gifted athlete losing to a harder-working competitor.</p><p>Microsoft's move is clearest: in-house MAI models + multi-model Foundry = <strong>transitioning from 'OpenAI's exclusive distributor' to 'AI industry's App Store.'</strong> Air Street Capital nails it: 'The era of exclusive platform bets is over.' Translation: Microsoft no longer bets everything on OpenAI. Foundry offers GPT-5.5, Opus 4.7, and Gemini — customers pick whatever they want, Microsoft only cares they're on its platform.</p><p><strong>Connecting design and tech sections: Claude Design's launch and Foundry's multi-model strategy are two expressions of the same mega-trend — 'commoditization of AI capabilities.' When Anthropic makes 'design' a free built-in Claude feature, when Microsoft puts all frontier models on the same shelf — differentiation shifts from 'model capability' to 'ecosystem and workflow.' Like smartphones: the winner wasn't the phone with the best chip (some Android flagship), but the one with the most complete ecosystem (iPhone). AI is entering the same phase. Whoever integrates model capability, developer tools, industry solutions, and distribution into one seamless experience wins. From this angle, Microsoft's position is stronger than anyone's — Azure infrastructure, Office user base, GitHub developer community, Foundry model supermarket. OpenAI has the best brand but no enterprise distribution. Anthropic has the best safety narrative but early-stage commercialization. Google has the strongest models but can't even integrate its own product lines. This fight is far from over.</strong></p></div>"
    },
    "cover": og.get(urls_tech[0], ""),
    "sources": [
        {
            "url": "https://openai.com/index/introducing-gpt-5-5/",
            "title": {"zh": "OpenAI 发布 GPT-5.5", "en": "Introducing GPT-5.5"},
            "image": og.get(urls_tech[0], "")
        },
        {
            "url": "https://www.cnbc.com/2026/05/07/openai-rolls-out-new-gpt-5point5-cyber-to-vetted-cybersecurity-teams.html",
            "title": {"zh": "OpenAI 推出 GPT-5.5-Cyber 网络安全专用模型", "en": "OpenAI Rolls Out GPT-5.5-Cyber to Vetted Cybersecurity Teams"},
            "image": og.get(urls_tech[3], "")
        },
        {
            "url": "https://www.businessinsider.com/microsoft-ai-models-azure-mai-transcribe-voice-image-foundry-openai-2026-4",
            "title": {"zh": "Microsoft 发布自研 AI 模型：与 OpenAI 的竞争加剧", "en": "Microsoft Releases New AI Models: Competition with OpenAI Intensifies"},
            "image": ""
        },
        {
            "url": "https://press.airstreet.com/p/state-of-ai-may-2026",
            "title": {"zh": "State of AI：2026 年 5 月", "en": "State of AI: May 2026"},
            "image": og.get(urls_tech[1], "")
        }
    ]
}

# --- Load existing issues.json and prepend ---
issues_path = os.path.join(os.path.dirname(__file__), "issues.json")
with open(issues_path, "r", encoding="utf-8") as f:
    issues = json.load(f)

# Remove any existing 2026-05-11 entries
issues = [i for i in issues if i.get("date") != "2026-05-11"]

# Prepend new issues (design first, then tech)
issues = [design_issue, tech_issue] + issues

with open(issues_path, "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ issues.json updated: {len(issues)} total issues")
print("Design issue cover:", design_issue["cover"][:80] if design_issue["cover"] else "(none)")
print("Tech issue cover:", tech_issue["cover"][:80] if tech_issue["cover"] else "(none)")
