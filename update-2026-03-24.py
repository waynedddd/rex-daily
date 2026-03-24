#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rex Daily Digest update for 2026-03-24"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=8)
        data = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', data, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data, re.I)
        return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images
urls = {
    "luma_tc": "https://techcrunch.com/2026/03/05/exclusive-luma-launches-creative-ai-agents-powered-by-its-new-unified-intelligence-models/",
    "luma_yahoo": "https://finance.yahoo.com/news/luma-launches-luma-agents-powered-181500995.html",
    "canva_yahoo": "https://tech.yahoo.com/apps/articles/kind-magic-canva-launches-magic-160158018.html",
    "atlassian_reuters": "https://www.reuters.com/technology/atlassian-lay-off-about-1600-people-pivot-ai-2026-03-11/",
    "atlassian_guardian": "https://www.theguardian.com/technology/2026/mar/21/atlassian-cuts-layoffs-staff-now-looking-for-work-ai",
    "anthropic_marketplace": "https://siliconangle.com/2026/03/06/anthropic-launches-claude-marketplace-third-party-cloud-services/",
    "anthropic_enterprise": "https://techcrunch.com/2026/02/24/anthropic-launches-new-push-for-enterprise-agents-with-plugins-for-finance-engineering-and-design/",
}

images = {}
for k, u in urls.items():
    images[k] = get_og_image(u)
    print(f"  {k}: {images[k][:80] if images[k] else '(none)'}")

design_cover = images.get("luma_tc") or images.get("canva_yahoo") or ""
tech_cover = images.get("atlassian_guardian") or images.get("atlassian_reuters") or ""

design_issue = {
    "date": "2026-03-24",
    "section": "design",
    "title": {
        "zh": "Luma Agents 重新定义创意生产线：从「生成工具」到「AI 创意同事」· Canva Magic Layers 让平面图变回可编辑分层设计 · 创意 AI 的新战场不是图像质量，是工作流编排",
        "en": "Luma Agents Redefine Creative Production: From 'Generation Tools' to 'AI Creative Coworkers' · Canva Magic Layers Turns Flat Images into Editable Layered Designs · The New Battleground in Creative AI Isn't Image Quality — It's Workflow Orchestration"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Luma 发布 Luma Agents：基于「统一智能」架构的端到端创意 AI 协作者</strong> — Luma AI 在 3 月初推出了 Luma Agents，这不是又一个图像/视频生成工具，而是一个能从创意简报到最终交付全程参与的 AI 协作系统。核心技术是其 Uni-1 模型——「用语言思考，用像素想象和渲染」。Luma Agents 能跨文本、图像、视频和音频协调创意生产，保持完整的项目上下文。首批合作伙伴包括 Publicis Groupe 和 Serviceplan Group 等全球广告巨头。Luma 的 CEO Jain 表示：「因为这些模型既能理解又能生成，我们能构建一个系统来完成端到端的创意工作。」<br><small>来源：<a href=\"https://techcrunch.com/2026/03/05/exclusive-luma-launches-creative-ai-agents-powered-by-its-new-unified-intelligence-models/\">TechCrunch</a> | <a href=\"https://finance.yahoo.com/news/luma-launches-luma-agents-powered-181500995.html\">Business Wire</a></small></li><li><strong>Canva 推出 Magic Layers：AI 将平面图像拆解为可编辑分层</strong> — Canva 的 Magic Layers 功能用 AI 将任何扁平图像（JPG/PNG）自动分解为独立的可编辑图层。与传统矢量追踪不同，Magic Layers 能识别形状代表什么以及它们与图像其余部分的关系。用户还可以将 Magic Layers 与 Canva 的 AI 生成功能结合，直接生成可编辑的多层设计。拥有 Affinity 的 Canva 表示，这个工具「弥合了 AI 生成内容与真正创意控制之间的鸿沟」。<br><small>来源：<a href=\"https://tech.yahoo.com/apps/articles/kind-magic-canva-launches-magic-160158018.html\">Yahoo Tech</a></small></li><li><strong>Figma 发布 2026 AI 设计工具全景</strong> — Figma 更新了其 AI 工具资源库，梳理了 2026 年 UX 设计师的 AI 工具生态：Figma Make（prompt-to-code）、UX Pilot（AI 驱动的 UX 评审和预测热力图）、以及多个 AI 插件。Figma 的定位越来越清晰——不做最花哨的 AI 功能，而是成为所有 AI 工具的协作中枢。<br><small>来源：<a href=\"https://www.figma.com/resource-library/ai-tools-for-ux-designers/\">Figma</a> | <a href=\"https://www.figma.com/resource-library/ai-design-tools/\">Figma</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>创意 AI 从「生成」进化到「编排」</strong>：Luma Agents 和 Adobe 的 Agentic 工作流代表同一个方向——AI 不只是生成资产，而是管理整个创意项目</li><li><strong>「AI 生成 → 人工编辑」的鸿沟正在被弥合</strong>：Canva Magic Layers 和 Adobe Generative Fill 都在解决同一个痛点——AI 输出太「死」，无法精细调整</li><li><strong>设计工具三足鼎立格局更加清晰</strong>：Figma（专业协作中枢）、Canva（大众化创意平台）、Adobe（企业级 AI 工作流引擎）</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Luma Agents 的发布看似只是又一个 AI 创意工具的新闻，但它标志着创意 AI 产业一个真正重要的拐点：竞争焦点从「谁的模型生成质量最好」转向「谁能编排最完整的创意工作流」。</strong></p><p>先说 Luma 做了什么。大多数 AI 创意工具（Midjourney、Runway、甚至 Adobe Firefly）本质上都是「单点生成器」——你给 prompt，它吐出一张图或一段视频。Luma Agents 的野心完全不同：它要做的是一个能从创意简报出发，自主规划、生成、迭代、交付的完整系统。它的 Uni-1 模型同时理解语言和视觉，这不是把 LLM 和图像模型简单拼接在一起，而是一个真正的多模态统一架构。Publicis 和 Serviceplan 这两个全球广告集团作为首批合作伙伴，说明这不是 demo——这是已经在生产环境中跑的东西。</p><p>把这个消息和上期 Adobe × NVIDIA 的 Agentic 创意工作流放在一起看，一个清晰的行业共识正在成形：<strong>2026 年创意 AI 的价值不在于生成一张更好看的图，而在于能否接管整个创意生产流水线。</strong>Adobe 从企业软件端往上走（把 AI Agent 嵌入 Creative Cloud），Luma 从模型端往下走（让多模态模型直接编排创意项目）。他们殊途同归地指向同一个终局：创意总监设定方向，AI Agent 负责执行。</p><p>再看 Canva 的 Magic Layers。这个功能看起来很「小」，但它精准解决了 AI 创意工具最大的痛点之一：<strong>AI 生成的内容是一个黑箱——你要么接受，要么重新生成。</strong>Magic Layers 让 AI 生成的图像变得可编辑、可调整、可精细控制。这是 Canva 作为「大众化创意平台」的高明之处——它不追求最前沿的生成质量，而是让 AI 输出变得「可用」。联想到 Canva 2024 年收购了 Affinity（专业级图层编辑软件），Magic Layers 显然是两者整合的第一个成果。</p><p>最后，Figma 更新的 2026 AI 工具全景图值得注意的不是它列了什么工具，而是 Figma 自己的定位策略。Figma 没有在 AI 生成上和 Adobe、Midjourney 硬拼，它选择做「AI 工具的协作中枢」——所有 AI 工具生成的东西最终都要在 Figma 里被整合、评审、交付。这和它在 pre-AI 时代的策略一脉相承：不做最强的设计工具，做最好的设计协作平台。在 AI Agent 时代，这个定位可能更有价值——<strong>当 10 个 AI Agent 同时在生成设计方案时，你需要一个地方来协调和决策。Figma 想做那个地方。</strong></p><p>总结一下：2026 年 3 月的创意工具市场正在经历三个层面的分化。底层的生成能力已经被 commodity 化（Midjourney、FLUX、Firefly 都够好了）。中层的编辑控制成为新战场（Canva Magic Layers、Adobe Generative Fill）。顶层的工作流编排才是真正的制高点（Luma Agents、Adobe Agentic Workflows）。对设计师来说，真正需要担心的不是 AI 能不能画出好看的图——而是 AI 能不能在你不在的时候把整个项目从头做到尾。</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Luma Launches Luma Agents: End-to-End Creative AI Collaborators</strong> — Luma AI introduced Luma Agents, powered by its Uni-1 'Unified Intelligence' model that 'thinks in language and imagines in pixels.' These agents handle complete creative workflows from brief to delivery across text, image, video, and audio. Launch partners include Publicis Groupe and Serviceplan Group.<br><small>Source: <a href=\"https://techcrunch.com/2026/03/05/exclusive-luma-launches-creative-ai-agents-powered-by-its-new-unified-intelligence-models/\">TechCrunch</a> | <a href=\"https://finance.yahoo.com/news/luma-launches-luma-agents-powered-181500995.html\">Business Wire</a></small></li><li><strong>Canva Launches Magic Layers: AI Turns Flat Images into Editable Layers</strong> — Unlike traditional vector tracing, Magic Layers identifies what shapes represent and their relationships, bridging the gap between AI generation and creative control.<br><small>Source: <a href=\"https://tech.yahoo.com/apps/articles/kind-magic-canva-launches-magic-160158018.html\">Yahoo Tech</a></small></li><li><strong>Figma Maps the 2026 AI Design Tool Landscape</strong> — Figma positions itself as the collaboration hub for all AI design tools rather than competing on generation quality.<br><small>Source: <a href=\"https://www.figma.com/resource-library/ai-tools-for-ux-designers/\">Figma</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Creative AI shifts from generation to orchestration</li><li>The 'AI output → human edit' gap is closing (Canva Magic Layers, Adobe Generative Fill)</li><li>Three-way market: Figma (pro collaboration), Canva (democratized creation), Adobe (enterprise AI workflows)</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Luma Agents marks a genuine inflection point: creative AI competition shifts from 'who generates best' to 'who orchestrates the most complete workflow.'</strong> Adobe approaches from enterprise software (embedding agents in Creative Cloud), Luma from the model side (unified multimodal intelligence managing entire projects). They converge on the same endgame: creative directors set direction, AI agents execute. Canva's Magic Layers solves the biggest pain point in AI-generated content — the black box problem — making outputs editable. Figma's strategy of being the 'collaboration hub for AI tools' may prove most durable: when 10 AI agents generate designs simultaneously, you need a place to coordinate. <strong>Generation is commoditized. Editing control is the new battleground. Workflow orchestration is the real high ground.</strong></p></div>"
    },
    "cover": design_cover,
    "sources": [
        {
            "title": {"zh": "TechCrunch: Luma 发布基于统一智能模型的创意 AI Agent", "en": "TechCrunch: Luma Launches Creative AI Agents Powered by Unified Intelligence"},
            "url": "https://techcrunch.com/2026/03/05/exclusive-luma-launches-creative-ai-agents-powered-by-its-new-unified-intelligence-models/",
            "image": images.get("luma_tc", "")
        },
        {
            "title": {"zh": "Yahoo Tech: Canva 推出 Magic Layers，AI 将平面图像变为可编辑分层", "en": "Yahoo Tech: Canva Launches Magic Layers for AI-Editable Designs"},
            "url": "https://tech.yahoo.com/apps/articles/kind-magic-canva-launches-magic-160158018.html",
            "image": images.get("canva_yahoo", "")
        },
        {
            "title": {"zh": "Figma: 2026 年 UX 设计师的 AI 工具指南", "en": "Figma: Top AI Tools for UX Designers in 2026"},
            "url": "https://www.figma.com/resource-library/ai-tools-for-ux-designers/",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-03-24",
    "section": "tech",
    "title": {
        "zh": "Atlassian 裁员 1600 人「转型 AI」：当 AI 成为裁员的万能借口 · Anthropic 推出 Claude Marketplace 和企业插件生态 · Meta 收购 AI Agent 社交网络 Moltbook",
        "en": "Atlassian Cuts 1,600 Jobs in 'AI Pivot': When AI Becomes the Universal Layoff Excuse · Anthropic Launches Claude Marketplace & Enterprise Plugin Ecosystem · Meta Acquires AI Agent Social Network Moltbook"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Atlassian 裁员 1600 人，声称为 AI 转型「调整技能组合」</strong> — Atlassian 3 月 11 日宣布裁员约 1600 人（全球员工 10%），CEO Mike Cannon-Brookes 表示公司需要「更敏捷，更深入投资 AI，并最终实现盈亏平衡」。但《卫报》深度调查揭露了一个尴尬的矛盾：Cannon-Brookes 几个月前还在说 AI 不会取代工程师，现在却说 AI「改变了所需的技能组合和岗位数量」。被裁员工透露，公司此前已引入 AI「队友」来提升效率，一些员工甚至被要求必须使用 AI 工具。一位被裁的安全工程师直言：「处理简单 bug 时，我比 AI 更快。」<br><small>来源：<a href=\"https://www.reuters.com/technology/atlassian-lay-off-about-1600-people-pivot-ai-2026-03-11/\">Reuters</a> | <a href=\"https://www.theguardian.com/technology/2026/mar/21/atlassian-cuts-layoffs-staff-now-looking-for-work-ai\">The Guardian</a></small></li><li><strong>Anthropic 推出 Claude Marketplace 和企业级 Cowork 插件</strong> — Anthropic 在 3 月连续放出两个重磅企业功能：Claude Marketplace（有限预览）允许企业在一个入口采购所有 Claude 驱动的第三方工具，简化 AI 软件采购流程。同时，Cowork 插件扩展到金融、HR、工程和设计领域，AI Agent 不再只是聊天助手，而是直接嵌入投行分析、人力资源管理和工程协作等核心业务系统。Cox Automotive 等企业客户已经在使用。Replit 也宣布入驻 Marketplace。<br><small>来源：<a href=\"https://siliconangle.com/2026/03/06/anthropic-launches-claude-marketplace-third-party-cloud-services/\">SiliconAngle</a> | <a href=\"https://techcrunch.com/2026/02/24/anthropic-launches-new-push-for-enterprise-agents-with-plugins-for-finance-engineering-and-design/\">TechCrunch</a></small></li><li><strong>Meta 收购 AI Agent 社交网络 Moltbook</strong> — TechCrunch 报道，Meta 收购了因「AI Agent 假帖子」而爆红的社交网络 Moltbook。这个由 OpenClaw 技术构建的 Reddit 风格平台让 AI Agent 作为独立用户发帖互动，引发了关于「AI 社交」本质的广泛讨论。Meta 的收购意图很明确：在其 20% 裁员传闻的同时，它在押注 AI Agent 将成为社交网络的新参与者。<br><small>来源：<a href=\"https://techcrunch.com/2026/03/10/meta-acquired-moltbook-the-ai-agent-social-network-that-went-viral-because-of-fake-posts/\">TechCrunch</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「AI 裁员叙事」的泡沫化</strong>：越来越多公司用 AI 转型作为裁员的包装纸，但被裁岗位和 AI 能力之间的因果关系经不起推敲</li><li><strong>AI 企业生态从工具走向平台</strong>：Anthropic 的 Marketplace 和上期 Adobe 的模型聚合策略如出一辙——做入口，不做终端</li><li><strong>AI Agent 社交成为新实验场</strong>：Meta 收购 Moltbook 意味着大厂开始认真对待 AI Agent 作为社交参与者的可能性</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>这期三条新闻看起来各自独立，但连在一起看，它们画出了 2026 年 AI 产业最令人不安的一幅图景：AI 正在同时扮演裁员的理由、工作的替代者、和社交的参与者。</strong></p><p>先说 Atlassian。这是 2026 年 Q1 最值得细读的裁员案例，不是因为规模（1600 人不算最多），而是因为它暴露了「AI 转型裁员」叙事的空洞。《卫报》的调查抓到了一个关键矛盾：CEO 几个月前还在公开场合说「AI 不会取代好工程师」，转头就以「AI 改变了技能组合」为由裁掉 10% 的人。一位被裁的安全工程师说自己处理 bug 比 AI 快——这不是 AI 淘汰了人，这是公司需要削减成本，而「AI 转型」是 2026 年最好听的裁员借口。Metaintro 的分析一针见血：<strong>大科技公司正在系统性地使用 AI 作为裁员的万能解释，因为投资者奖励 AI 叙事。</strong>说「我们在 AI 上投资所以需要调整团队」比说「我们要降本增效」好听得多，股价反应也更好。</p><p>然后看 Anthropic 的 Claude Marketplace。表面上这是一个企业软件采购平台，但深层的战略意图和我们上期讨论的 Adobe Firefly 模型聚合策略一模一样：<strong>不做最好的终端产品，做所有 AI 产品的入口和交易平台。</strong>微软有 Copilot 生态，Google 有 Workspace AI 生态，现在 Anthropic 也在建自己的 Claude 生态。有意思的是 Marketplace 只对 Claude 驱动的应用开放——这创造了一个强大的激励：如果你是 AI 创业公司，集成 Claude 模型就能进入 Anthropic 的企业分发渠道。这和 Apple App Store 的逻辑如出一辙：用分发权换生态锁定。CIO.com 的分析指出了风险：当 AI Agent 跨越金融、HR、协作等核心企业系统时，身份管理、访问控制和数据泄露的集中风险急剧上升。但「CIO 们面临着必须在企业中用 AI 做点什么的巨大压力」——安全顾虑让位于 FOMO。</p><p>最后是 Meta 收购 Moltbook。这可能是本月最被低估的新闻。一个让 AI Agent 自主发帖的 Reddit 风格社交网络，因为「AI 假帖子」爆红，然后被 Meta——全球最大的社交网络公司——收购。联系到 Meta 同时在考虑 20% 的裁员，图景就很清楚了：<strong>Meta 在用 AI Agent 替代人类员工的同时，也在探索用 AI Agent 替代人类社交用户。</strong>当你的 feed 里既有 AI 生成的内容，又有 AI Agent 发的帖子，又有 AI 写的评论——「社交」网络里还有多少是「社交」的？</p><p>把这三条串起来看：Atlassian 用 AI 裁人（AI 作为裁员工具），Anthropic 让 AI 进入核心业务系统（AI 作为工作替代），Meta 让 AI 成为社交参与者（AI 作为人的替身）。这不是三个独立事件，这是同一个趋势的三个切面：<strong>AI 正在从「帮人做事」变成「代替人存在」。</strong>2026 年 Q1 结束时，我们需要认真思考一个问题：当公司可以用 AI 裁掉你的工作、用 AI Agent 完成你的任务、甚至用 AI 模拟你的社交参与时，人在这个系统里的不可替代性到底在哪里？Atlassian 那位被裁工程师的话值得反复品味：「处理简单 bug 时，我比 AI 更快。」——问题是，企业不再关心谁更快，它们只关心谁更便宜。</p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Atlassian Cuts 1,600 Jobs, Claims AI Pivot</strong> — CEO Cannon-Brookes said AI changed 'the mix of skills and number of roles required,' contradicting his own statements months earlier that AI wouldn't replace engineers. A laid-off security engineer noted: 'I was faster than AI for simple bugs.'<br><small>Source: <a href=\"https://www.reuters.com/technology/atlassian-lay-off-about-1600-people-pivot-ai-2026-03-11/\">Reuters</a> | <a href=\"https://www.theguardian.com/technology/2026/mar/21/atlassian-cuts-layoffs-staff-now-looking-for-work-ai\">The Guardian</a></small></li><li><strong>Anthropic Launches Claude Marketplace & Enterprise Cowork Plugins</strong> — A procurement platform for Claude-powered tools plus plugins for finance, HR, engineering, and design. Same 'be the gateway' strategy as Adobe's model aggregation.<br><small>Source: <a href=\"https://siliconangle.com/2026/03/06/anthropic-launches-claude-marketplace-third-party-cloud-services/\">SiliconAngle</a> | <a href=\"https://techcrunch.com/2026/02/24/anthropic-launches-new-push-for-enterprise-agents-with-plugins-for-finance-engineering-and-design/\">TechCrunch</a></small></li><li><strong>Meta Acquires AI Agent Social Network Moltbook</strong> — The viral OpenClaw-built Reddit-for-AI-agents platform gets acquired by Meta, signaling big tech's serious interest in AI agents as social participants.<br><small>Source: <a href=\"https://techcrunch.com/2026/03/10/meta-acquired-moltbook-the-ai-agent-social-network-that-went-viral-because-of-fake-posts/\">TechCrunch</a></small></li></ul><h3>🔄 Trends</h3><ul><li>'AI pivot' becomes the universal layoff justification — correlation ≠ causation</li><li>AI enterprise ecosystems shift from tools to platforms (Anthropic Marketplace = Claude's App Store)</li><li>AI agents as social participants: Meta bets on agent-populated networks</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Three seemingly unrelated stories paint 2026's most unsettling picture: AI simultaneously serves as the reason for layoffs, the replacement for workers, and the substitute for social participants.</strong> Atlassian's case exposes the 'AI pivot' narrative as hollow — investors reward the AI story, so companies use it to justify cost cuts. Anthropic's Marketplace mirrors Apple's App Store logic: distribution rights in exchange for ecosystem lock-in. Meta acquiring Moltbook while considering 20% layoffs reveals the endgame: <strong>replacing human employees AND human users with AI agents.</strong> The question for Q1 2026: when companies can use AI to cut your job, complete your tasks, and simulate your social presence, where exactly is human irreplaceability?</p></div>"
    },
    "cover": tech_cover,
    "sources": [
        {
            "title": {"zh": "Reuters: Atlassian 裁员约 1600 人，转向 AI", "en": "Reuters: Atlassian to Cut Roughly 1,600 Jobs in Pivot to AI"},
            "url": "https://www.reuters.com/technology/atlassian-lay-off-about-1600-people-pivot-ai-2026-03-11/",
            "image": images.get("atlassian_reuters", "")
        },
        {
            "title": {"zh": "卫报: 先来了 AI「队友」，然后是裁员——Atlassian 员工的新现实", "en": "The Guardian: First Came the AI 'Teammates', Then the Layoffs"},
            "url": "https://www.theguardian.com/technology/2026/mar/21/atlassian-cuts-layoffs-staff-now-looking-for-work-ai",
            "image": images.get("atlassian_guardian", "")
        },
        {
            "title": {"zh": "SiliconAngle: Anthropic 推出 Claude Marketplace", "en": "SiliconAngle: Anthropic Launches Claude Marketplace"},
            "url": "https://siliconangle.com/2026/03/06/anthropic-launches-claude-marketplace-third-party-cloud-services/",
            "image": images.get("anthropic_marketplace", "")
        },
        {
            "title": {"zh": "TechCrunch: Meta 收购 AI Agent 社交网络 Moltbook", "en": "TechCrunch: Meta Acquires AI Agent Social Network Moltbook"},
            "url": "https://techcrunch.com/2026/03/10/meta-acquired-moltbook-the-ai-agent-social-network-that-went-viral-because-of-fake-posts/",
            "image": ""
        }
    ]
}

# Load existing issues.json
with open("issues.json", "r", encoding="utf-8") as f:
    issues = json.load(f)

# Insert new issues at the front
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("issues.json", "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! issues.json now has {len(issues)} issues. Added 2 new issues for 2026-03-24.")
