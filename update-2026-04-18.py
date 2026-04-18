# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily update — 2026-04-18"""
import json
import urllib.request
import re

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")[:50000]
            m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
            if not m:
                m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
            return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images
urls = {
    "figma_weave": "https://dev.to/spookuspookus/figma-made-a-huge-step-forward-in-ai-design-april-2026-1cin",
    "codex": "https://flowstep.ai/blog/ai-design-assistant/",
    "figma_make": "https://www.figma.com/solutions/ai-agent-workflow-builder/",
    "salesforce": "https://www.salesforce.com/news/stories/salesforce-headless-360-announcement/",
    "amazon": "https://arstechnica.com/tech-policy/2026/04/amazon-to-merge-with-globalstar-become-iphones-primary-satellite-provider/",
    "openai_cyber": "https://www.axios.com/2026/04/14/openai-model-cyber-program-release",
}

images = {}
for k, u in urls.items():
    images[k] = get_og_image(u)
    print(f"  {k}: {images[k][:80]}...")

with open("issues.json", "r") as f:
    data = json.load(f)

design_issue = {
    "date": "2026-04-18",
    "section": "design",
    "title": {
        "zh": "Figma 开放 AI Agent 直接写入画布 + Weave 工作流上线 · Flowstep 登顶 2026 AI 设计助手榜 · Figma Make 成为 PM 的 AI Agent 工作流构建器",
        "en": "Figma Opens Canvas to AI Agents via MCP Server + Launches Weave Workflows · Flowstep Tops 2026 AI Design Assistant Rankings · Figma Make Becomes PM's AI Agent Workflow Builder"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Figma 开放 MCP Server：AI Agent 现在可以直接在 Figma 画布上创建和修改设计</strong> — Figma 4 月中旬正式发布 MCP Server，允许 Claude Code、Cursor、Codex、Windsurf 等外部 AI 编程代理<strong>直接写入 Figma 文件——创建和修改真实的设计资产，使用你的组件库、变量和 tokens</strong>。同时上线的 Figma Weave 工作流功能让用户在可视化画布上构建可复用的生成式 AI 工作流，可用于批量生成图片、视频和插画集。此外，Figma 推出 Make Kits，让团队把代码、样式、变量和 tokens 带入 Make，使 AI 生成的原型能准确使用设计系统。<strong>这三件事加在一起，Figma 正在从「设计工具」变成「AI 设计基础设施」</strong>。<br><small>来源：<a href=\"https://dev.to/spookuspookus/figma-made-a-huge-step-forward-in-ai-design-april-2026-1cin\">Dev.to</a>、<a href=\"https://www.figma.com/solutions/ai-agent-workflow-builder/\">Figma</a></small></li><li><strong>Flowstep 登顶 2026 AI 设计助手排行榜</strong> — Flowstep 在多个 2026 年 AI 设计工具评测中位列第一，核心优势是：<strong>从文本描述直接生成完整 UI 设计稿，支持实时协作，可导出为 Figma 文件或生产代码</strong>。2026 年的 AI 设计工具市场已经分裂为两个阵营：面向产品团队的真实界面生产工具（如 Flowstep），和面向营销团队的快速内容生成工具（如 Canva）。<strong>前者的护城河在于设计系统集成和代码输出质量，后者的护城河在于用户基数和易用性</strong>。<br><small>来源：<a href=\"https://flowstep.ai/blog/ai-design-assistant/\">Flowstep</a>、<a href=\"https://blog.getbind.co/6-best-ai-tools-for-designers-in-2026/\">Bind AI</a></small></li><li><strong>Figma Make 定位为 PM 的 AI Agent 工作流构建器</strong> — Figma 官方将 Make 重新定位为<strong>面向 PM 的 AI Agent 工作流构建器</strong>，通过 prompt 描述逻辑、流程和边界场景，使用团队的 Figma 设计系统或代码组件生成可交互原型。PM 们已经在用 Make 构建从内部工具到产品 MVP 的无代码 Web 应用。Make 原型现在可以嵌入到 Figma Design、FigJam 和 Figma Slides 中。<strong>设计工具开始直接服务非设计师——产品经理成为新的核心用户群</strong>。<br><small>来源：<a href=\"https://www.figma.com/solutions/ai-agent-workflow-builder/\">Figma</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>Figma 三步棋变身 AI 设计基础设施</strong>：MCP Server（外部 AI 接入）+ Weave（AI 工作流）+ Make Kits（设计系统桥接）</li><li><strong>AI 设计工具市场两极分化</strong>：产品级工具（Flowstep/Figma）vs 内容级工具（Canva/Midjourney），护城河完全不同</li><li><strong>设计工具用户群在扩大</strong>：PM 用 Make 建原型，开发者用 MCP 写设计文件，设计师的「专属领地」正在消失</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Figma 这周的三连发（MCP Server + Weave + Make Kits）不是三个独立功能更新——它们是同一个战略意图的三个执行面：把 Figma 从「设计师的画布」变成「AI 时代的设计操作系统」。</strong></p><p>先说 MCP Server。昨天我们聊到 Anthropic 的设计工具让 Figma 股价跌了 6%，但 Figma 的回应不是对抗——<strong>而是「如果 AI 要做设计，那就让它在我的画布上做」</strong>。通过 MCP Server，Claude Code、Cursor、Codex 这些编程 AI 可以直接创建和修改 Figma 文件，而且是用你现有的组件库、变量和 tokens。这一招非常聪明：<strong>Anthropic 让用户可以跳过 Figma 直接生成设计，Figma 则让所有 AI 工具都成为 Figma 的「输入层」</strong>。不管你用哪个 AI 生成设计，最终都在 Figma 里编辑和协作。这是典型的平台策略——不跟应用层竞争，而是让自己成为所有应用的底层。</p><p>Weave 工作流和 Make Kits 则解决了一个更深层的问题：<strong>AI 生成的设计如何保持与设计系统的一致性</strong>。之前 AI 设计工具的最大痛点不是「生成不了」，而是「生成的东西和现有设计系统格格不入」——颜色不对、组件不匹配、间距不符合规范。Make Kits 把代码、样式、变量和 tokens 带入 AI 生成流程，意味着<strong>AI 不是在空白画布上凭想象画画，而是在你的设计系统约束下生成——就像一个新设计师第一天入职就完全掌握了公司的设计规范</strong>。这才是 AI 设计真正能用于生产的前提。</p><p>Flowstep 登顶则揭示了 AI 设计工具市场一个有趣的分裂。2026 年，<strong>市场已经很清楚地分成了两个阵营</strong>：Flowstep、Figma 这类工具服务的是需要生产真实界面的产品团队——它们的价值在于设计系统集成、代码输出质量、和团队协作能力；Canva、Midjourney 这类工具服务的是需要快速产出视觉内容的营销和创意团队——它们的价值在于易用性、模板丰富度和生成速度。这两个市场看起来都在增长，但<strong>真正的战场在中间地带：当 Figma Make 让 PM 也能建原型，当 Canva AI 2.0 也能生成网站，这两个阵营的边界正在模糊</strong>。</p><p><strong>把这周的设计新闻串成一条线：Anthropic 从上方切入（AI 模型直接生成设计），Figma 从下方加固（成为所有 AI 的底层画布），Canva 从侧面包抄（AI Agent + 工作上下文）。三家的策略截然不同，但共同指向一个结论：2026 年下半年，「谁拥有设计文件的最终编辑权」将成为比「谁能生成最好看的设计」更重要的竞争维度。Figma 目前在这个维度上领先——因为即使 AI 生成了设计，你还是要在 Figma 里修改、评审、交付。但如果 Anthropic 的设计工具直接输出可部署的代码，跳过了「设计文件」这个环节呢？这才是 Figma 真正需要担心的——不是 AI 能不能做设计，而是「设计文件」这个概念本身是否还有必要。</strong></p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Figma Opens MCP Server: AI Agents Can Now Create and Modify Designs Directly on the Figma Canvas</strong> — Figma officially launched its MCP Server in mid-April, allowing external AI coding agents like Claude Code, Cursor, Codex, and Windsurf to <strong>write directly to Figma files — creating and modifying real design assets using your components, variables, and tokens</strong>. Simultaneously, Figma Weave workflows let users build reusable generative AI workflows on a visual canvas for batch-generating images, videos, and illustration sets. Additionally, Figma released Make Kits to bring code, styles, variables, and tokens into Make, ensuring AI-generated prototypes accurately use design systems. <strong>Together, these three moves transform Figma from 'design tool' to 'AI design infrastructure'</strong>.<br><small>Source: <a href=\"https://dev.to/spookuspookus/figma-made-a-huge-step-forward-in-ai-design-april-2026-1cin\">Dev.to</a>, <a href=\"https://www.figma.com/solutions/ai-agent-workflow-builder/\">Figma</a></small></li><li><strong>Flowstep Tops 2026 AI Design Assistant Rankings</strong> — Flowstep ranked #1 across multiple 2026 AI design tool reviews, with core strengths in <strong>generating complete UI designs from text descriptions, real-time collaboration, and export to Figma files or production code</strong>. The 2026 AI design market has split into two camps: production-grade interface tools (like Flowstep) for product teams, and rapid content generation tools (like Canva) for marketing teams.<br><small>Source: <a href=\"https://flowstep.ai/blog/ai-design-assistant/\">Flowstep</a>, <a href=\"https://blog.getbind.co/6-best-ai-tools-for-designers-in-2026/\">Bind AI</a></small></li><li><strong>Figma Make Repositioned as PM's AI Agent Workflow Builder</strong> — Figma officially positions Make as an <strong>AI agent workflow builder for PMs</strong>, capturing logic, flows, and edge cases through prompts using the team's Figma design system or code components. PMs are building no-code web apps from internal tools to product MVPs. Make prototypes can now embed into Figma Design, FigJam, and Figma Slides. <strong>Design tools are expanding beyond designers — PMs become a core user group</strong>.<br><small>Source: <a href=\"https://www.figma.com/solutions/ai-agent-workflow-builder/\">Figma</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Figma's triple play transforms it into AI design infrastructure: MCP Server (external AI access) + Weave (AI workflows) + Make Kits (design system bridge)</li><li>AI design tool market polarizes: production-grade tools (Flowstep/Figma) vs content-grade tools (Canva/Midjourney) with entirely different moats</li><li>Design tool user base expanding: PMs build prototypes with Make, developers write to design files via MCP — designers' 'exclusive territory' is dissolving</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Figma's triple release this week (MCP Server + Weave + Make Kits) isn't three separate feature updates — they're three execution surfaces of one strategic intent: transforming Figma from 'designers' canvas' to 'the design operating system of the AI era.'</strong></p><p>Yesterday we discussed how Anthropic's design tool dropped Figma's stock 6%. But Figma's response isn't confrontation — <strong>it's 'if AI wants to design, let it design on my canvas.'</strong> Through MCP Server, Claude Code, Cursor, and Codex can directly create and modify Figma files using existing components, variables, and tokens. <strong>Anthropic lets users skip Figma to generate designs; Figma makes all AI tools its 'input layer.'</strong> Classic platform strategy: don't compete with the application layer, become everyone's foundation.</p><p>Weave and Make Kits solve a deeper problem: <strong>how AI-generated designs maintain consistency with design systems</strong>. The biggest pain point wasn't 'AI can't generate' but 'what it generates doesn't fit the existing design system.' Make Kits bring code, styles, variables, and tokens into the AI generation pipeline — <strong>AI doesn't draw on a blank canvas from imagination, it generates within your design system constraints</strong>.</p><p>Flowstep's #1 ranking reveals the market's clear bifurcation. Production tools (Flowstep/Figma) serve teams shipping real interfaces; content tools (Canva/Midjourney) serve teams producing visual content. <strong>The real battlefield is in between: as Figma Make lets PMs prototype and Canva AI 2.0 generates websites, the boundary between these camps is blurring.</strong></p><p><strong>This week's design narrative: Anthropic attacks from above (AI models generate designs directly), Figma fortifies from below (becoming every AI's underlying canvas), Canva flanks from the side (AI Agent + work context). Three different strategies, one shared conclusion: in H2 2026, 'who owns the final edit of the design file' matters more than 'who generates the prettiest design.' But if Anthropic's tool outputs deployable code directly, skipping the 'design file' step entirely? That's what Figma should really worry about — not whether AI can design, but whether 'design files' as a concept remain necessary.</strong></p></div>"
    },
    "cover": images.get("figma_weave", ""),
    "sources": [
        {
            "title": {
                "zh": "Figma 在 AI 设计领域迈出重要一步",
                "en": "Figma Made a Huge Step Forward in AI Design"
            },
            "url": "https://dev.to/spookuspookus/figma-made-a-huge-step-forward-in-ai-design-april-2026-1cin",
            "image": images.get("figma_weave", "")
        },
        {
            "title": {
                "zh": "2026 年 8 大 AI 设计助手工具",
                "en": "8 Best AI Design Assistant Tools in 2026"
            },
            "url": "https://flowstep.ai/blog/ai-design-assistant/",
            "image": images.get("codex", "")
        },
        {
            "title": {
                "zh": "Figma Make：面向 PM 的 AI Agent 工作流构建器",
                "en": "AI Agent Workflow Builder for PMs | Figma Make"
            },
            "url": "https://www.figma.com/solutions/ai-agent-workflow-builder/",
            "image": images.get("figma_make", "")
        },
        {
            "title": {
                "zh": "2026 年 6 大设计师 AI 工具",
                "en": "6 Best AI Tools for Designers in 2026"
            },
            "url": "https://blog.getbind.co/6-best-ai-tools-for-designers-in-2026/",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-04-18",
    "section": "tech",
    "title": {
        "zh": "Salesforce 发布 Headless 360：60+ MCP 工具让 AI Agent 直接操控企业平台 · Amazon 116 亿美元收购 Globalstar 成为 iPhone 卫星服务商 · OpenAI 推出 GPT-5.4 mini/nano + Codex 全面扩展",
        "en": "Salesforce Launches Headless 360: 60+ MCP Tools Let AI Agents Control Enterprise Platform · Amazon's $11.6B Globalstar Acquisition Makes It iPhone's Satellite Provider · OpenAI Ships GPT-5.4 mini/nano + Codex Expansion"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Salesforce 发布 Headless 360：把整个平台变成 AI Agent 的 API</strong> — Salesforce 本周在 TDX 2026 上发布 Headless 360，一个 API-first 架构，<strong>将 Customer 360、Data 360 和 Agentforce 的全部能力以 API、MCP 工具和 CLI 命令的形式暴露出来</strong>。超过 60 个新 MCP 工具和 30+ 预配置编程技能，让 Claude Code、Cursor、Codex、Windsurf 等编程 AI 可以直接操作 Salesforce 平台的数据、工作流和业务逻辑。AgentExchange 整合了 10,000 个 Salesforce 应用、2,600+ Slack 应用和 1,000+ Agentforce 代理。<strong>关键信号：Salesforce 不再为人设计界面——它为 AI Agent 设计 API</strong>。OpenAI COO Brad Lightcap 表示，像 Salesforce 这样的企业软件巨头在数据、分发和企业集成方面拥有结构性优势。<br><small>来源：<a href=\"https://www.salesforce.com/news/stories/salesforce-headless-360-announcement/\">Salesforce</a>、<a href=\"https://www.cio.com/article/4159536/salesforce-launches-headless-360-to-support-agent-first-enterprise-workflows.html\">CIO</a>、<a href=\"https://www.benzinga.com/markets/tech/26/04/51878250/salesforce-bets-on-ai-agents-with-headless-360-debut-amid-software-stocks-sell-off\">Benzinga</a></small></li><li><strong>Amazon 116 亿美元收购 Globalstar，成为 iPhone 和 Apple Watch 的主要卫星服务提供商</strong> — Amazon 宣布以 116 亿美元收购卫星运营商 Globalstar，同时与 Apple 签署协议，<strong>Amazon Leo（前 Kuiper）将成为 iPhone 和 Apple Watch 的主要卫星服务提供商</strong>。Apple 此前已向 Globalstar 投资超 10 亿美元用于紧急 SOS 卫星功能。Amazon 承诺将继续支持现有 Apple 设备，并于 2028 年部署自己的下一代 D2D 卫星系统，届时可提供语音、数据和消息服务。<strong>两大科技巨头在太空基础设施上的合作，可能重塑全球移动通信格局</strong>。<br><small>来源：<a href=\"https://arstechnica.com/tech-policy/2026/04/amazon-to-merge-with-globalstar-become-iphones-primary-satellite-provider/\">Ars Technica</a>、<a href=\"https://www.bloomberg.com/news/articles/2026-04-14/amazon-globalstar-deal-is-poised-to-boost-apple-s-satellite-ambitions\">Bloomberg</a>、<a href=\"https://sixcolors.com/link/2026/04/amazon-acquires-apples-satellite-partner/\">Six Colors</a></small></li><li><strong>OpenAI 发布 GPT-5.4 mini 和 nano + Codex「几乎可以做一切」</strong> — OpenAI 4 月 16 日发布 GPT-5.4 mini 和 nano 两个轻量模型，并将 Codex 升级为支持子代理（subagents）的全能编程平台。同时，OpenAI 推出 GPT-5.4-Cyber 分级访问计划，采用与 Anthropic Mythos 不同的策略——<strong>更开放的访问权限，但配备身份验证和使用限制</strong>。Axios 指出，与 Anthropic 限制 Mythos 仅向约 40 家组织开放不同，OpenAI 选择了更广泛的分发策略。这些模型发现安全漏洞的速度和能力正在引起政府官员和全球商业领袖的担忧。<br><small>来源：<a href=\"https://www.axios.com/2026/04/14/openai-model-cyber-program-release\">Axios</a>、<a href=\"https://thehackernews.com/2026/04/openai-launches-gpt-54-cyber-with.html\">The Hacker News</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>企业软件从「给人用的界面」变成「给 AI 用的 API」</strong>：Salesforce Headless 360 是这个转变的标志性事件</li><li><strong>太空互联网成为科技巨头新战场</strong>：Amazon-Apple 卫星联盟 vs SpaceX Starlink，移动通信即将脱离地面基站依赖</li><li><strong>AI 安全模型的分发策略分歧</strong>：OpenAI 走开放分级路线，Anthropic 走严格限制路线——谁的方法更有效？</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天三条科技新闻表面上毫不相关——企业 SaaS、太空卫星、AI 模型——但它们共享一个底层主题：基础设施层正在为 AI Agent 重新设计。</strong></p><p>Salesforce Headless 360 可能是本周最被低估的新闻。<strong>「Headless」这个词说明了一切：不需要头（UI），只需要身体（数据和逻辑）</strong>。当你有 60+ MCP 工具让 AI 直接操作 CRM 数据、触发工作流、执行业务逻辑时，传统的 Salesforce 管理员界面变成了什么？变成了人类的「后备方案」——当 AI 处理不了的时候才需要人打开界面。这不是 Salesforce 一家的判断：上周 Figma 开放 MCP 让 AI 直接写画布，这周 Salesforce 开放 MCP 让 AI 直接操作企业数据。<strong>MCP（Model Context Protocol）正在成为 AI 时代的「USB 接口」——一个让 AI Agent 插入任何软件平台的标准化协议</strong>。如果这个趋势持续下去，2026 年底我们会看到大量 SaaS 公司发布自己的 MCP 工具集，就像 2010 年代每家公司都在发布 REST API 一样。</p><p>Amazon 收购 Globalstar 并成为 iPhone 卫星服务商，这件事的战略深度远超表面。<strong>Apple 刚把自己最关键的硬件差异化功能（卫星通信）的底层基础设施交给了一个竞争对手</strong>。为什么？因为自建卫星网络太贵太慢——Apple 试过，投了超过 10 亿给 Globalstar，但 Globalstar 的卫星数量和覆盖范围远不够支撑真正的卫星通信服务。Amazon Leo（前 Kuiper）有 3,200+ 颗卫星的计划，才是能实现全球覆盖的规模。但这也意味着 <strong>Apple 在一个关键基础设施上对 Amazon 形成了依赖——就像 Apple 依赖三星的屏幕、台积电的芯片一样</strong>。科技巨头之间的关系越来越像冷战时期的超级大国：在某些领域激烈竞争，在另一些领域深度绑定。Amazon 2028 年部署下一代 D2D 卫星系统后，可能会向所有手机厂商提供卫星服务——Android 阵营也能获得类似 iPhone 的卫星功能。<strong>卫星通信将从 Apple 的独家优势变成行业标配</strong>。</p><p>OpenAI 与 Anthropic 在 AI 安全模型分发上的策略差异值得密切关注。<strong>Anthropic 的 Mythos 因为太强大而只对 40 家组织开放，OpenAI 的 GPT-5.4-Cyber 则走分级开放路线</strong>。这不仅是商业策略差异，更是 AI 安全哲学的根本分歧：Anthropic 认为能力过强的 AI 必须严格管控，OpenAI 认为广泛分发加上适当限制效果更好。有趣的是，两家都在做「AI 找安全漏洞」的生意，但采用了相反的分发策略。<strong>政府和企业正在因为这些模型的漏洞发现能力而紧张——Bloomberg 报道美国财政部长 Bessent 和美联储主席 Powell 已经向银行 CEO 们发出警告</strong>。当 AI 发现漏洞的速度超过人类修补漏洞的速度时，我们正在进入一个攻防严重不对称的安全新时代。</p><p><strong>把这三条线索和本周的设计新闻合在一起看：Figma 开放 MCP 给 AI 写画布、Salesforce 开放 MCP 给 AI 操作企业数据、Amazon 给 Apple 提供卫星基础设施、OpenAI/Anthropic 为 AI Agent 提供网络安全能力——所有这些都在做同一件事：为 AI Agent 铺路。2026 年的关键词不再是「AI 能做什么」，而是「AI 能接入什么」。谁的基础设施对 AI Agent 最友好，谁就能在下一轮平台竞争中占据有利位置。Salesforce 和 Figma 都选择了 MCP 作为接口标准，这可能是 Anthropic 在商业版图上最成功的布局——不是 Claude 模型本身，而是 MCP 协议正在成为 AI 时代的基础设施标准。</strong></p></div>"
    },
    "cover": images.get("salesforce", ""),
    "sources": [
        {
            "title": {
                "zh": "Salesforce 发布 Headless 360",
                "en": "Introducing Salesforce Headless 360"
            },
            "url": "https://www.salesforce.com/news/stories/salesforce-headless-360-announcement/",
            "image": images.get("salesforce", "")
        },
        {
            "title": {
                "zh": "Amazon 收购 Globalstar 成为 iPhone 卫星服务商",
                "en": "Amazon to Merge with Globalstar, Become iPhone's Primary Satellite Provider"
            },
            "url": "https://arstechnica.com/tech-policy/2026/04/amazon-to-merge-with-globalstar-become-iphones-primary-satellite-provider/",
            "image": images.get("amazon", "")
        },
        {
            "title": {
                "zh": "OpenAI 推出 AI 网络安全模型分级访问计划",
                "en": "OpenAI Rolls Out Tiered Access to Advanced AI Cyber Models"
            },
            "url": "https://www.axios.com/2026/04/14/openai-model-cyber-program-release",
            "image": images.get("openai_cyber", "")
        }
    ]
}

data.insert(0, tech_issue)
data.insert(0, design_issue)

with open("issues.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ issues.json updated with 2026-04-18 design + tech issues")
