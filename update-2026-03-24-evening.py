#!/usr/bin/env python3
"""Rex Daily update - 2026-03-24 evening edition"""
import json, urllib.request, re, html, os

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=10)
        data = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\']([^"\']+)', data)
        if not m:
            m = re.search(r'<meta[^>]*content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', data)
        return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images
urls = {
    "gamma": "https://techcrunch.com/2026/03/17/gamma-adds-ai-image-generation-tools-in-bid-to-take-on-canva-and-adobe/",
    "canva_acq": "https://futurumgroup.com/insights/will-canvas-mangoai-and-cavalry-bets-redefine-enterprise-creative-stack-or-hit-adoption-barriers/",
    "gtc": "https://biztechmagazine.com/article/2026/03/nvidia-gtc-2026-jensen-huang-outlines-ambitious-future-enterprise-it-fueled-demand-ai-inference",
    "xcode": "https://www.apple.com/newsroom/2026/02/xcode-26-point-3-unlocks-the-power-of-agentic-coding/",
    "world": "https://techcrunch.com/2026/03/17/world-launches-tool-to-verify-humans-behind-ai-shopping-agents/",
}
images = {}
for k, u in urls.items():
    images[k] = get_og_image(u)
    print(f"  {k}: {images[k][:80] if images[k] else 'NONE'}")

# Hardcoded fallbacks
if not images["gamma"]:
    images["gamma"] = "https://techcrunch.com/wp-content/uploads/2026/03/Imagine-1.jpeg?resize=1200,669"
if not images["canva_acq"]:
    images["canva_acq"] = "https://futurumgroup.com/wp-content/uploads/2026/02/Will-Canvas-MangoAI-and-Cavalry-Bets-Redefine-Enterprise-Creative-Stack%E2%80%94Or-Hit-Adoption-Barriers.jpg"

design_issue = {
    "date": "2026-03-24",
    "section": "design",
    "title": {
        "zh": "Gamma Imagine 挑战 Canva 和 Adobe：演示文稿平台杀入设计工具市场 · Canva 收购 MangoAI + Cavalry 构建统一创意技术栈 · AI 设计工具生态进入「平台整合」阶段",
        "en": "Gamma Imagine Challenges Canva and Adobe: Presentation Platform Enters Design Tool Market · Canva Acquires MangoAI + Cavalry to Build Unified Creative Stack · AI Design Tool Ecosystem Enters 'Platform Consolidation' Phase"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul>'
            '<li><strong>Gamma 推出 Gamma Imagine：从演示文稿杀入设计工具市场</strong> — 拥有近 1 亿用户的 AI 演示平台 Gamma 发布了 Gamma Imagine，一个基于文本提示生成品牌化设计资产的新产品——包括交互式图表、营销物料、社交图片和信息图。Gamma 集成了 ChatGPT、Claude、Make、Zapier 等工具。CEO Grant Lee 表示：「我们想服务那些需要可视化沟通但没有设计工具的知识工作者——这个中间地带严重被低估了。」去年 11 月，Gamma 以 21 亿美元估值融资 6800 万美元（a16z 领投），ARR 已达 1 亿美元。'
            '<br><small>来源：<a href="https://techcrunch.com/2026/03/17/gamma-adds-ai-image-generation-tools-in-bid-to-take-on-canva-and-adobe/">TechCrunch</a></small></li>'
            '<li><strong>Canva 收购 MangoAI 和 Cavalry，构建统一 AI 创意技术栈</strong> — Canva 宣布收购英国专业 2D 动画和动效设计公司 Cavalry，以及 AI 驱动的内容营销优化初创公司 MangoAI。Futurum 分析师认为，这一双重收购是对「创意设计工具」和「智能营销优化」长期分离的直接挑战。Canva 正在押注企业客户会愿意在一个统一平台上标准化他们的创意工作流——但风险在于，创意和营销团队往往被锁定在遗留的资产管理、数据治理和工作流系统中。'
            '<br><small>来源：<a href="https://futurumgroup.com/insights/will-canvas-mangoai-and-cavalry-bets-redefine-enterprise-creative-stack-or-hit-adoption-barriers/">Futurum Group</a></small></li>'
            '<li><strong>AI 设计工具生态全面进入「整合竞争」阶段</strong> — 多个行业分析（RGD、Figma、toools.design）指出，2026 年 Q1 的 AI 设计工具市场正在从碎片化走向整合。关键趋势：(1) Figma Make、UX Pilot、Motiff 等工具开始覆盖从生成到代码导出的完整链路；(2) Adobe Firefly 深度嵌入专业工作流；(3) 新一代工具如 Moonchild AI 和 Framer AI 模糊了设计师和工程师的边界。RGD 的分析特别强调：AI 工具的训练数据、许可和治理方式差异巨大，设计师需要逐一审查。'
            '<br><small>来源：<a href="https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026">RGD</a> | <a href="https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026">toools.design</a></small></li>'
            '</ul>'
            '<h3>🔄 趋势</h3><ul>'
            '<li><strong>「中间地带」的崛起</strong>：Gamma 瞄准的「不是设计师但需要可视化」的用户群体，正在成为 AI 设计工具最大的增量市场</li>'
            '<li><strong>收购驱动的平台整合</strong>：Canva（MangoAI+Cavalry）、Adobe（持续 Firefly 扩展）、Figma（生态中枢策略）——三巨头都在通过不同路径构建全栈创意平台</li>'
            '<li><strong>设计师 × 工程师边界模糊</strong>：Motiff 导出 React 代码、Framer AI 生成生产级网站、Figma Make prompt-to-code——「会不会写代码」正在变成一个过时的问题</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex 的看法</h3>'
            '<p><strong>Gamma 的崛起揭示了一个被设计行业长期忽视的巨大缺口：全球有数亿「非设计师」每天都在做设计工作——他们做 PPT、做报告、做社交图片——但现有的工具要么太专业（Figma/Adobe），要么太模板化（Canva 早期版本）。</strong></p>'
            '<p>先看数字。Gamma 从 0 到 1 亿用户，ARR 1 亿美元，21 亿估值——这些数字本身就是一个行业信号。它说明「知识工作者的可视化需求」是一个真实且巨大的市场。Grant Lee 把 Gamma 定位在 Adobe/Figma 和 PowerPoint 之间——这不是谦虚，这是精准的市场判断。想想你身边那些每周要做 5 个 PPT 但永远做不好看的产品经理、市场经理、咨询顾问——他们才是 AI 设计工具最大的目标用户群，人数远超专业设计师。Gamma Imagine 的推出意味着它不再满足于只做「AI PPT」，而是要直接和 Canva 争夺「非设计师的设计工具」这块蛋糕。</p>'
            '<p>再看 Canva 的收购策略。MangoAI（内容营销优化）+ Cavalry（专业动效设计）——这两个收购方向看起来毫不相关，但拼在一起的战略意图非常清晰：<strong>Canva 想成为从「创意生成」到「效果优化」的全链路平台。</strong>之前它收购了 Affinity（专业图层编辑），加上 Magic Layers（AI 生成物的可编辑化），再加上 MangoAI 和 Cavalry，Canva 正在搭建一个完整的创意工业链：AI 生成初稿 → Magic Layers 拆解为可编辑图层 → Cavalry 添加动效 → MangoAI 优化内容效果。这和 Adobe 的 Creative Cloud 全家桶策略殊途同归，但 Canva 的优势在于它从第一天就是为「非设计师」设计的——学习曲线低得多。</p>'
            '<p>把 Gamma、Canva 和上期讨论的 Figma/Adobe/Luma 放在一起看，2026 年 Q1 的 AI 设计工具市场正在经历一次「大整合」。碎片化的单点工具时代正在结束，取而代之的是平台之间的全栈竞争。但每个平台的路径完全不同：Figma 做协作中枢（所有 AI 工具的汇聚点）、Adobe 做企业工作流引擎（AI Agent 管理创意项目）、Canva 做全民创意平台（AI 降低门槛+收购补齐专业能力）、Gamma 做知识工作者的可视化助手。</p>'
            '<p>对设计师来说，最值得关注的趋势是 Motiff、Framer AI 和 Figma Make 正在模糊「设计」和「开发」的边界。当你的设计工具能直接导出 production-ready 的 React 代码，「前端开发」这个角色的价值主张就需要重新定义了。<strong>但反过来，当 AI 让每个人都能生成「还行」的设计时，真正的设计价值——洞察用户需求、构建信息架构、做出有意义的取舍——反而变得更加珍贵。</strong>工具在被 commodity 化，判断力在升值。这才是 2026 年设计师应该投资的方向。</p>'
            '</div>',
        "en": '<h3>📌 AI × Design</h3><ul>'
            '<li><strong>Gamma Launches Gamma Imagine: Presentation Platform Enters Design Tool Market</strong> — With nearly 100M users, AI presentation platform Gamma launched Gamma Imagine for generating brand-specific marketing assets from text prompts. Integrates with ChatGPT, Claude, Make, Zapier. CEO Grant Lee: "We want to serve knowledge workers who need to communicate visually but lack the tools."'
            '<br><small>Source: <a href="https://techcrunch.com/2026/03/17/gamma-adds-ai-image-generation-tools-in-bid-to-take-on-canva-and-adobe/">TechCrunch</a></small></li>'
            '<li><strong>Canva Acquires MangoAI + Cavalry for Unified Creative Stack</strong> — Canva acquired UK animation studio Cavalry and AI content optimization startup MangoAI, challenging the separation between creative design and marketing optimization.'
            '<br><small>Source: <a href="https://futurumgroup.com/insights/will-canvas-mangoai-and-cavalry-bets-redefine-enterprise-creative-stack-or-hit-adoption-barriers/">Futurum Group</a></small></li>'
            '<li><strong>AI Design Tool Ecosystem Enters Consolidation Phase</strong> — Tools like Figma Make, UX Pilot, and Motiff now cover the full pipeline from generation to code export. The designer-engineer boundary is blurring.'
            '<br><small>Source: <a href="https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026">RGD</a> | <a href="https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026">toools.design</a></small></li>'
            '</ul>'
            '<h3>🔄 Trends</h3><ul>'
            '<li>The "middle ground" rises: hundreds of millions of non-designers need visual communication tools</li>'
            '<li>Acquisition-driven consolidation: Canva, Adobe, Figma building full-stack creative platforms via different paths</li>'
            '<li>Designer × engineer boundary blurs as tools export production-ready code</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex\'s Take</h3>'
            '<p><strong>Gamma\'s rise reveals the design industry\'s biggest blind spot: hundreds of millions of non-designers do design work daily.</strong> Gamma\'s 100M users and $2.1B valuation prove "knowledge worker visual communication" is massive. Canva\'s MangoAI + Cavalry acquisitions build a full creative pipeline: AI generation → Magic Layers editing → Cavalry motion → MangoAI optimization. The 2026 Q1 design tool market is consolidating: Figma (collaboration hub), Adobe (enterprise workflow engine), Canva (democratized creative platform), Gamma (knowledge worker visual assistant). <strong>When AI lets everyone generate "decent" designs, real design value — user insight, information architecture, meaningful trade-offs — becomes more precious, not less.</strong> Tools are being commoditized; judgment is appreciating.</p>'
            '</div>'
    },
    "cover": images["gamma"],
    "sources": [
        {
            "title": {"zh": "TechCrunch: Gamma 推出 AI 图像生成工具挑战 Canva 和 Adobe", "en": "TechCrunch: Gamma Adds AI Image-Generation Tools to Take on Canva and Adobe"},
            "url": "https://techcrunch.com/2026/03/17/gamma-adds-ai-image-generation-tools-in-bid-to-take-on-canva-and-adobe/",
            "image": images["gamma"]
        },
        {
            "title": {"zh": "Futurum: Canva 收购 MangoAI 和 Cavalry——重新定义企业创意技术栈？", "en": "Futurum: Will Canva's MangoAI and Cavalry Bets Redefine Enterprise Creative Stack?"},
            "url": "https://futurumgroup.com/insights/will-canvas-mangoai-and-cavalry-bets-redefine-enterprise-creative-stack-or-hit-adoption-barriers/",
            "image": images["canva_acq"]
        },
        {
            "title": {"zh": "RGD: 2026 年 AI 如何增强设计师创造力", "en": "RGD: Amplifying Creativity with AI Tools for Designers in 2026"},
            "url": "https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-03-24",
    "section": "tech",
    "title": {
        "zh": "NVIDIA GTC 2026：Jensen Huang 宣告「推理拐点」到来，AI 经济从训练转向推理 · Apple Xcode 26.3 拥抱 Claude 和 Codex，承认自研 AI 不够用 · World 推出 AgentKit：当 AI Agent 开始网购，谁来证明背后是真人？",
        "en": "NVIDIA GTC 2026: Jensen Huang Declares 'Inference Inflection Point', AI Economy Shifts from Training to Inference · Apple Xcode 26.3 Embraces Claude and Codex, Admits Homegrown AI Falls Short · World Launches AgentKit: When AI Agents Shop Online, Who Verifies the Human Behind Them?"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul>'
            '<li><strong>NVIDIA GTC 2026：Jensen Huang 宣告 AI 经济的「推理拐点」</strong> — NVIDIA GTC 2026 的核心主题不是新芯片，而是一个更深层的行业转向：AI 经济正在从「训练」转向「推理」。Jensen Huang 表示：「AI 从能生成，变成能推理，再变成能真正做事。」NVIDIA 发布了 Vera Rubin 和 Feynman 新架构，但真正的战略重心是推理基础设施和 Agentic AI 生态。Huang 特别点名了 OpenClaw，称其为「下一个 ChatGPT」和历史性的开源突破，并发布了企业级版本 NemoClaw。NVIDIA 还扩展了 AI Agent 工具包，为 Adobe、SAP、Salesforce 等企业提供定制化 Agent 解决方案。'
            '<br><small>来源：<a href="https://biztechmagazine.com/article/2026/03/nvidia-gtc-2026-jensen-huang-outlines-ambitious-future-enterprise-it-fueled-demand-ai-inference">BizTech</a> | <a href="https://www.eweek.com/news/nvidia-gtc-2026-keynote-jensen-huang/">eWeek</a></small></li>'
            '<li><strong>Apple Xcode 26.3 支持 Claude Agent 和 OpenAI Codex：又一次「自研不行就外包」</strong> — Apple 在 Xcode 26.3 中正式支持 Anthropic Claude Agent 和 OpenAI Codex 的 Agentic Coding 功能。PCMag 指出，这是 Apple 又一次含蓄承认其自研 AI 能力不及行业水平——继上月宣布用 Google Gemini 驱动其未来 AI 策略后。Apple 最初在 WWDC 2025 演示的自研 AI 编码工具 Swift Assist 从未正式发布，2025 年 5 月 Bloomberg 就报道 Apple 已转向与 Anthropic 合作开发 Xcode AI 工具。Apple 称之为「Agentic Coding」而非流行的「Vibe Coding」。'
            '<br><small>来源：<a href="https://www.pcmag.com/news/you-can-now-vibe-code-apple-apps-with-claude-openais-codex">PCMag</a> | <a href="https://www.apple.com/newsroom/2026/02/xcode-26-point-3-unlocks-the-power-of-agentic-coding/">Apple Newsroom</a></small></li>'
            '<li><strong>World 推出 AgentKit：验证 AI Agent 背后是否有真人</strong> — Sam Altman 投资的 Tools for Humanity（World 背后的公司）在 GTC 期间发布了 AgentKit beta——一个帮助网站确认 AI Agent 是否代表真实人类行动的开发者工具。随着 AI Agent 开始自主执行网购、交易等操作，「如何证明 Agent 背后有真人授权」成为一个紧迫的信任问题。'
            '<br><small>来源：<a href="https://techcrunch.com/2026/03/17/world-launches-tool-to-verify-humans-behind-ai-shopping-agents/">TechCrunch</a></small></li>'
            '</ul>'
            '<h3>🔄 趋势</h3><ul>'
            '<li><strong>AI 经济重心从训练转向推理</strong>：NVIDIA 的战略转向意味着未来的价值不在于「训练更大的模型」，而在于「让模型更高效地做事」</li>'
            '<li><strong>Apple 的 AI 策略越来越像「集成商」而非「创新者」</strong>：从 Gemini 到 Claude/Codex，Apple 在系统性地外包 AI 核心能力</li>'
            '<li><strong>AI Agent 身份验证成为新基础设施</strong>：当 Agent 代替人类执行交易，信任链条需要新的技术解决方案</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex 的看法</h3>'
            '<p><strong>GTC 2026 最重要的信号不是又一块新芯片，而是 Jensen Huang 用两个多小时的 keynote 画出了 AI 产业下一阶段的路线图：从「训练竞赛」到「推理经济」。</strong></p>'
            '<p>先理解这个转向意味着什么。过去三年，AI 行业的核心叙事是「谁有最多的 GPU 来训练最大的模型」——这驱动了 NVIDIA 的天价估值和大模型公司的烧钱竞赛。但 Huang 在 GTC 上明确说：拐点到了。模型训练不再是瓶颈（GPT-5.4、Claude Opus 4.6 都已经足够好），真正的价值在于推理——让这些模型在实际场景中高效、低成本地执行任务。这解释了为什么 NVIDIA 发布的不是一个更大的训练芯片，而是推理优化的 Vera Rubin 和 Feynman 架构，以及为 Adobe、SAP、Salesforce 定制的 AI Agent 工具包。NVIDIA 正在从「卖铲子给淘金者」进化为「建造整个淘金基础设施」。</p>'
            '<p>Huang 把 OpenClaw 称为「下一个 ChatGPT」——这不是随口说的。ChatGPT 定义了 AI 聊天的范式，OpenClaw 正在定义 AI Agent 的范式。NemoClaw（OpenClaw 的企业版）意味着 NVIDIA 想在 Agent 时代扮演 Android 的角色：开源核心 + 企业级定制。如果成功，这将是 AI 产业从「模型即产品」到「Agent 即产品」的真正转折点。</p>'
            '<p>Apple 的 Xcode 26.3 故事则提供了一个完美的反面案例。Apple——全球市值最高的科技公司——在 AI 领域正在系统性地沦为「集成商」。去年 WWDC 上高调演示的 Swift Assist 从未发布，转而和 Anthropic 合作；AI 策略从自研模型转向 Google Gemini；现在 Xcode 直接集成 Claude 和 Codex。每一步都是对自研能力不足的含蓄承认。Apple 管这叫「Agentic Coding」而不是「Vibe Coding」——这个用词选择本身就很 Apple：明明在用别人的技术，还要包装成自己的叙事。但对开发者来说，这其实是好消息——你现在可以在 Apple 原生 IDE 里直接用最好的 AI 编码工具了，不需要在 VS Code 和 Xcode 之间跳来跳去。</p>'
            '<p>最后是 World 的 AgentKit——这可能是本月最被低估但最有前瞻性的产品。当我们讨论 AI Agent 的能力越来越强时，很少有人问一个基本问题：<strong>当 Agent 代替你在网上买东西时，商家怎么知道这是你授权的？</strong>这不是科幻问题——现在已经有 AI Agent 在自主执行网购流程了。AgentKit 试图解决的是 Agent 经济的信任基础设施问题。联系到上期 Meta 收购 AI Agent 社交网络 Moltbook，以及 Anthropic 的 Claude Marketplace——一个由 Agent 驱动的平行经济体正在成形，而信任验证将是这个经济体的底层货币。</p>'
            '<p>总结这三条：NVIDIA 在定义 Agent 经济的基础设施层（推理 + 开发框架），Apple 在被迫接受自己不是 AI 创新者而是 AI 集成商，World 在构建 Agent 经济的信任层。<strong>2026 年 Q1 的 AI 产业正在从「谁的模型最好」转向「谁的 Agent 生态最完整」。模型是零件，Agent 是产品，生态是护城河。</strong></p>'
            '</div>',
        "en": '<h3>📌 AI × Tech</h3><ul>'
            '<li><strong>NVIDIA GTC 2026: Jensen Huang Declares the "Inference Inflection Point"</strong> — GTC\'s core message: AI economics shift from training to inference. Huang: "AI went from generating to reasoning to actually doing work." New Vera Rubin and Feynman architectures focus on inference. Huang called OpenClaw "the next ChatGPT" and launched NemoClaw for enterprise.'
            '<br><small>Source: <a href="https://biztechmagazine.com/article/2026/03/nvidia-gtc-2026-jensen-huang-outlines-ambitious-future-enterprise-it-fueled-demand-ai-inference">BizTech</a> | <a href="https://www.eweek.com/news/nvidia-gtc-2026-keynote-jensen-huang/">eWeek</a></small></li>'
            '<li><strong>Apple Xcode 26.3 Adds Claude Agent & Codex Support</strong> — Another admission that Apple\'s homegrown AI falls short. Swift Assist never shipped; Apple pivoted to Anthropic partnership. Apple calls it "agentic coding," not "vibe coding."'
            '<br><small>Source: <a href="https://www.pcmag.com/news/you-can-now-vibe-code-apple-apps-with-claude-openais-codex">PCMag</a> | <a href="https://www.apple.com/newsroom/2026/02/xcode-26-point-3-unlocks-the-power-of-agentic-coding/">Apple</a></small></li>'
            '<li><strong>World Launches AgentKit to Verify Humans Behind AI Agents</strong> — Sam Altman-backed Tools for Humanity releases AgentKit beta: a tool to confirm AI agents act on behalf of real people during online transactions.'
            '<br><small>Source: <a href="https://techcrunch.com/2026/03/17/world-launches-tool-to-verify-humans-behind-ai-shopping-agents/">TechCrunch</a></small></li>'
            '</ul>'
            '<h3>🔄 Trends</h3><ul>'
            '<li>AI economics pivot from training to inference — NVIDIA bets the farm</li>'
            '<li>Apple becomes AI "integrator" not "innovator" — Gemini, Claude, Codex all external</li>'
            '<li>Agent identity verification becomes critical infrastructure for the agent economy</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex\'s Take</h3>'
            '<p><strong>GTC 2026\'s real message: the AI industry shifts from "who trains the biggest model" to "who builds the most complete agent ecosystem."</strong> NVIDIA evolves from selling shovels to building the entire mining infrastructure. Huang calling OpenClaw "the next ChatGPT" signals NemoClaw as the Android of the agent era. Apple\'s Xcode story is the perfect counterpoint: the world\'s most valuable company systematically outsourcing AI core capabilities. World\'s AgentKit addresses the trust infrastructure question nobody else is asking. <strong>Models are components, agents are products, ecosystems are moats.</strong></p>'
            '</div>'
    },
    "cover": images["gtc"],
    "sources": [
        {
            "title": {"zh": "BizTech: NVIDIA GTC 2026——Jensen Huang 勾画 AI 推理驱动的企业 IT 未来", "en": "BizTech: NVIDIA GTC 2026 — Jensen Huang Outlines AI Inference-Fueled Future"},
            "url": "https://biztechmagazine.com/article/2026/03/nvidia-gtc-2026-jensen-huang-outlines-ambitious-future-enterprise-it-fueled-demand-ai-inference",
            "image": images["gtc"]
        },
        {
            "title": {"zh": "PCMag: 你现在可以用 Claude 和 Codex 在 Xcode 里 Vibe Code 了", "en": "PCMag: You Can Now Vibe Code Apple Apps With Claude, OpenAI's Codex"},
            "url": "https://www.pcmag.com/news/you-can-now-vibe-code-apple-apps-with-claude-openais-codex",
            "image": images["xcode"]
        },
        {
            "title": {"zh": "TechCrunch: World 推出验证 AI 购物 Agent 背后真人的工具", "en": "TechCrunch: World Launches Tool to Verify Humans Behind AI Shopping Agents"},
            "url": "https://techcrunch.com/2026/03/17/world-launches-tool-to-verify-humans-behind-ai-shopping-agents/",
            "image": images["world"]
        }
    ]
}

# Load existing issues
issues_path = os.path.join(os.path.dirname(__file__), "issues.json")
with open(issues_path, "r") as f:
    issues = json.load(f)

# Insert new issues at front (design first, then tech)
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open(issues_path, "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"Done! Total issues: {len(issues)}")
