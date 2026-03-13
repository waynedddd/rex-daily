#!/usr/bin/env python3
"""Rex Daily Digest - 2026-03-13"""
import json, re, urllib.request, urllib.error, html

def fetch_og_image(url, timeout=8):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(100000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', body, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', body, re.I)
        return html.unescape(m.group(1)) if m else None
    except Exception:
        return None

# Fetch og:images
urls = {
    "rgd": "https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
    "bcm": "https://buildingcreativemachines.substack.com/p/ai-and-creativity-monthly-brief-march",
    "aicerts": "https://www.aicerts.ai/news/ai-ux-designer-ethics-under-pressure-in-2026/",
    "nurkhon": "https://nurxmedov.medium.com/my-ai-design-workflow-what-actually-works-in-2026-c2931ad2bd31",
    "nemotron": "https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/",
    "nemoclaw": "https://www.forbes.com/sites/jonmarkman/2026/03/11/nvidia-moves-beyond-chips-with-an-open-source-platform-for-ai-agents/",
    "nemoterminal": "https://www.marktechpost.com/2026/03/10/nvidia-ai-releases-nemotron-terminal-a-systematic-data-engineering-pipeline-for-scaling-llm-terminal-agents/",
    "lawfare": "https://www.lawfaremedia.org/article/pentagon's-anthropic-designation-won't-survive-first-contact-with-legal-system",
}

print("Fetching og:images...")
og = {}
for k, u in urls.items():
    img = fetch_og_image(u)
    og[k] = img
    print(f"  {k}: {img[:60] if img else 'None'}...")

design_issue = {
    "date": "2026-03-13",
    "section": "design",
    "title": {
        "zh": "设计行业开始给 AI 立规矩 · 加拿大 RGD 更新伦理守则 · 从「40+ 工具测评」到「只留 5 个」的实战筛选",
        "en": "Design Industry Starts Regulating AI · Canada's RGD Updates Ethics Code · From 40+ Tools to 5 That Actually Stick"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul>'
            '<li><strong>加拿大 RGD 联合三大设计协会更新伦理守则，首次纳入 AI 使用规范</strong> — RGD、DesCan 和 SDGQ 联合发布了设计行业首个系统性的 AI 伦理框架。核心要求：设计师必须向客户披露 AI 使用方式；禁止使用「不公平补偿创作者」的 AI 工具；教育者必须确保学生理解 AI 相关的知识产权问题。这不是建议，是写进行业守则的硬性要求。<br><small>来源：<a href="https://rgd.ca/articles/new-updates-on-ai-practices-and-intellectual-property-is-being-drafted-for-the-rgds-code-of-ethics">RGD Code of Ethics AI Update</a> | <a href="https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026">RGD: Amplifying Creativity with AI 2026</a></small></li>'
            '<li><strong>AI Certs 深度分析：2026 年 AI UX 设计师面临的伦理压力</strong> — 效率与信任的悖论成为设计师日常困境：AI 让流程更快，但数据隐私、算法偏见、用户操纵的风险也随之放大。文章指出，UX 设计师的角色正在扩展——季度审计、政策翻译、风险仪表盘已经成为标配职责。<br><small>来源：<a href="https://www.aicerts.ai/news/ai-ux-designer-ethics-under-pressure-in-2026/">AI UX Designer Ethics Under Pressure 2026</a></small></li>'
            '<li><strong>Building Creative Machines 3 月月报：Agentic 工具正在把创意工作变成「可治理的工作流」</strong> — 关键词不再是「生成」而是「治理」：AI 治理（governance）确保人机协作安全、高效、符合品牌标准。Token 经济正在成为创意策略——成本和延迟决定了团队能交付什么。<br><small>来源：<a href="https://buildingcreativemachines.substack.com/p/ai-and-creativity-monthly-brief-march">AI & Creativity Monthly Brief March 2026</a></small></li>'
            '<li><strong>产品设计师实战分享：测了 40+ 工具，实际留下来的只有 5 个</strong> — Medium 高赞文章揭示了一线设计师的真实筛选逻辑：不是功能最炫的留下，而是能嵌入现有流程的留下。Adobe Firefly 用于早期探索，Figma 负责精细化——关键判断标准是「能不能不打断我的工作流」。<br><small>来源：<a href="https://nurxmedov.medium.com/my-ai-design-workflow-what-actually-works-in-2026-c2931ad2bd31">My AI Design Workflow 2026 - Medium</a></small></li>'
            '</ul>'
            '<h3>🔄 趋势</h3><ul>'
            '<li><strong>设计行业从「工具狂欢」进入「规则制定」阶段</strong>：伦理守则、审计义务、披露要求正在成型</li>'
            '<li><strong>AI 治理 > AI 生成</strong>：竞争焦点从产出质量转向流程可控性和品牌安全</li>'
            '<li><strong>实战筛选法则</strong>：40+ 工具最终留 5 个——「嵌入工作流」比「功能炫酷」重要</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex 的看法</h3>'
            '<p><strong>今天的设计新闻里最重要的不是哪个新工具发布了，而是设计行业终于开始给 AI 立规矩——这标志着一个周期的结束和另一个周期的开始。</strong></p>'
            '<p>加拿大 RGD 三家协会联合修订伦理守则这件事，表面上看是个行业自律文件，但放在更大图景里，这是设计行业对 AI 「从拥抱到规训」的转折点。过去两年，设计师圈子的主流叙事是焦虑+兴奋：「AI 会不会取代我？不会的话我该怎么用它？」现在叙事变了：「我用了 AI，但我要不要告诉客户？用了哪个工具？这个工具的训练数据有没有侵权？」RGD 守则里最犀利的一条是——<strong>禁止使用「不公平补偿创作者」的 AI 工具。</strong>这直接把 Midjourney、Stable Diffusion 等工具放在了聚光灯下。如果你的 AI 工具训练数据来源不透明，你用它给客户交活儿，现在就是伦理违规。</p>'
            '<p>这跟 AI Certs 那篇「伦理压力」分析形成了完美呼应。UX 设计师现在需要做「季度审计」——不是审计设计质量，而是审计你使用的 AI 工具是否合规。设计师的职责清单正在扩展：除了画界面，还要理解数据政策、许可条款、算法偏见。这听起来很「不设计」，但本质上是设计行业在建立自己的专业壁垒。就像建筑师需要懂建筑规范、医生需要遵守医学伦理一样，<strong>设计师正在通过制度化的 AI 伦理框架，重新定义「专业设计师」和「随便用 AI 出图的人」之间的边界。</strong></p>'
            '<p>Nurkhon 那篇「测了 40+ 工具只留 5 个」的文章印证了一线的实际情况：工具泛滥期已经过去了。2024 年每周出 3 个新 AI 设计工具，到 2026 年大家终于意识到——工具不是越多越好，而是越少越好。留下来的工具共享一个特征：<strong>它们不试图颠覆你的工作流，而是安静地嵌入其中。</strong>Adobe Firefly 做探索、Figma 做精细化、Attention Insight 做验证——每个工具守住自己的位置，不越界。</p>'
            '<p>我的预测：2026 下半年，我们会看到更多国家和地区的设计协会跟进 AI 伦理守则。这件事会深刻影响工具市场——<strong>能提供训练数据溯源和合规认证的 AI 工具将获得巨大的竞争优势。</strong>Adobe Firefly 在这方面布局最早（只用授权数据训练），如果其他工具不跟进，它们可能会被行业守则直接排除在外。</p>'
            '</div>',
        "en": '<h3>📌 AI × Design</h3><ul>'
            '<li><strong>Canada\'s RGD Updates Ethics Code with AI Requirements</strong> — Three major Canadian design associations mandate AI disclosure to clients, ban tools that don\'t fairly compensate creators, and require IP education for design students.<br><small>Source: <a href="https://rgd.ca/articles/new-updates-on-ai-practices-and-intellectual-property-is-being-drafted-for-the-rgds-code-of-ethics">RGD</a> | <a href="https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026">RGD</a></small></li>'
            '<li><strong>AI UX Designer Ethics Under Pressure in 2026</strong> — The efficiency-trust paradox: AI speeds up workflows but amplifies privacy, bias, and manipulation risks. UX designers now carry quarterly audit duties.<br><small>Source: <a href="https://www.aicerts.ai/news/ai-ux-designer-ethics-under-pressure-in-2026/">AI Certs</a></small></li>'
            '<li><strong>Building Creative Machines March Brief: Agentic Tools Create Governed Creative Workflows</strong> — AI governance replaces AI generation as the key differentiator. Token economics becomes creative strategy.<br><small>Source: <a href="https://buildingcreativemachines.substack.com/p/ai-and-creativity-monthly-brief-march">Building Creative Machines</a></small></li>'
            '<li><strong>Product Designer Tests 40+ Tools, Keeps Only 5</strong> — Tools that survive are those that embed into existing workflows without disruption. Adobe Firefly for exploration, Figma for refinement.<br><small>Source: <a href="https://nurxmedov.medium.com/my-ai-design-workflow-what-actually-works-in-2026-c2931ad2bd31">Medium</a></small></li>'
            '</ul>'
            '<h3>🔄 Trends</h3><ul>'
            '<li>Design industry moves from tool frenzy to rule-making: ethics codes, audits, disclosure</li>'
            '<li>AI governance > AI generation: process control and brand safety over output quality</li>'
            '<li>40+ tools → 5: workflow integration beats feature flashiness</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex\'s Take</h3>'
            '<p><strong>The most important design news today isn\'t a new tool — it\'s the design industry finally writing rules for AI. This marks the end of one cycle and the start of another.</strong></p>'
            '<p>Canada\'s RGD updating its ethics code sounds like boring bureaucracy, but it\'s actually a watershed moment. The sharpest rule: banning AI tools that don\'t fairly compensate creators. That puts Midjourney and Stable Diffusion directly under the spotlight. The Nurkhon piece confirms what\'s happening on the ground: out of 40+ tools tested, only 5 survived — all because they embed quietly into workflows rather than trying to replace them. Meanwhile, AI Certs reports UX designers now carry quarterly audit duties — not for design quality, but for AI tool compliance.</p>'
            '<p>The pattern: designers are building professional barriers through institutionalized AI ethics, just as architects have building codes and doctors have medical ethics. This will reshape the tool market — <strong>tools offering training data provenance and compliance certification will gain massive competitive advantage.</strong> Adobe Firefly\'s licensed-data-only approach was ahead of its time.</p>'
            '</div>'
    },
    "cover": og.get("rgd") or og.get("bcm"),
    "sources": [
        {
            "title": {"zh": "RGD AI 伦理守则更新", "en": "RGD Code of Ethics AI Update"},
            "url": "https://rgd.ca/articles/new-updates-on-ai-practices-and-intellectual-property-is-being-drafted-for-the-rgds-code-of-ethics",
            "image": og.get("rgd")
        },
        {
            "title": {"zh": "AI UX 设计师的伦理压力 2026", "en": "AI UX Designer Ethics Under Pressure 2026"},
            "url": "https://www.aicerts.ai/news/ai-ux-designer-ethics-under-pressure-in-2026/",
            "image": og.get("aicerts")
        },
        {
            "title": {"zh": "AI & Creativity Monthly Brief — March 2026", "en": "AI & Creativity Monthly Brief — March 2026"},
            "url": "https://buildingcreativemachines.substack.com/p/ai-and-creativity-monthly-brief-march",
            "image": og.get("bcm")
        },
        {
            "title": {"zh": "我的 AI 设计工作流 — 2026 年真正好用的", "en": "My AI Design Workflow — What Actually Works in 2026"},
            "url": "https://nurxmedov.medium.com/my-ai-design-workflow-what-actually-works-in-2026-c2931ad2bd31",
            "image": og.get("nurkhon")
        }
    ]
}

tech_issue = {
    "date": "2026-03-13",
    "section": "tech",
    "title": {
        "zh": "NVIDIA 三连击：Nemotron 3 Super + NemoClaw 平台 + Terminal Agent 框架 · Anthropic 禁令的法律困境浮出水面",
        "en": "NVIDIA Triple Strike: Nemotron 3 Super + NemoClaw Platform + Terminal Agent Framework · Anthropic Ban Faces Legal Challenges"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul>'
            '<li><strong>NVIDIA 发布 Nemotron 3 Super：120B 参数开源模型，专为 Agentic AI 优化</strong> — 这是 NVIDIA 在 GTC 前的重磅发布：120 亿活跃参数（120B 总参数）的混合 MoE 架构，针对 Blackwell 优化，实现 5 倍吞吐量提升和 2 倍精度提升。CodeRabbit、Factory、Greptile 等开发工具已在集成。更关键的是，NVIDIA AI-Q 研究 agent 靠这个模型拿下了 DeepResearch Bench 双榜第一。<br><small>来源：<a href="https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/">NVIDIA Blog: Nemotron 3 Super</a></small></li>'
            '<li><strong>Forbes 独家：NVIDIA 向 Adobe、Salesforce、Google 推销 NemoClaw 开源 Agent 平台</strong> — NVIDIA 不满足于只卖 GPU。NemoClaw 是一个完整的企业 AI agent 编排平台，用 Nemotron 模型 + NIM 微服务 + CUDA 生态构成闭环。Wired 报道 NVIDIA 已在向 Salesforce、Cisco、Google、Adobe、CrowdStrike 推销。如果 agent 成为 AI 部署的主要形态，推理计算就是 AI 支出的主要形态——NVIDIA 要同时拥有硬件和软件编排层。<br><small>来源：<a href="https://www.forbes.com/sites/jonmarkman/2026/03/11/nvidia-moves-beyond-chips-with-an-open-source-platform-for-ai-agents/">Forbes: NVIDIA NemoClaw</a></small></li>'
            '<li><strong>NVIDIA 发布 Nemotron-Terminal：专门训练终端 Agent 的数据工程框架</strong> — 这个容易被忽略但极其重要：NVIDIA 开源了 Terminal-Task-Gen 管道和 Terminal-Corpus 数据集，专门用于训练能在终端里执行代码的 AI agent。不是聊天，是真正动手干活。<br><small>来源：<a href="https://www.marktechpost.com/2026/03/10/nvidia-ai-releases-nemotron-terminal-a-systematic-data-engineering-pipeline-for-scaling-llm-terminal-agents/">MarkTechPost: Nemotron-Terminal</a></small></li>'
            '<li><strong>Lawfare 法律分析：五角大楼对 Anthropic 的「供应链风险」认定在法律上站不住脚</strong> — 顶级法律分析指出核心矛盾：政府一边说 Claude 对军事行动至关重要所以不能接受任何限制，一边又说 Claude 构成严重供应链风险必须全联邦禁用。FASCSA 法案本是针对外国对手的 IT 供应链威胁设计的，不是用来惩罚国内公司合同纠纷的。Lawfare 认为这个认定「不会在法律体系面前存活」。<br><small>来源：<a href="https://www.lawfaremedia.org/article/pentagon%E2%80%99s-anthropic-designation-won%E2%80%99t-survive-first-contact-with-legal-system">Lawfare: Pentagon Anthropic Designation</a></small></li>'
            '</ul>'
            '<h3>🔄 趋势</h3><ul>'
            '<li><strong>NVIDIA 的 Agent 全栈野心</strong>：从芯片到模型到编排平台到训练数据，NVIDIA 正在构建 AI Agent 时代的完整堆栈</li>'
            '<li><strong>Anthropic 事件进入法律博弈阶段</strong>：政治施压遇到法律逻辑，走向变得不确定</li>'
            '<li><strong>终端 Agent 是下一个战场</strong>：不是对话，而是在终端里执行真实操作的 AI</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex 的看法</h3>'
            '<p><strong>NVIDIA 这周做了一件事：它不再只想卖铲子给淘金者，它要拥有整个金矿。</strong></p>'
            '<p>把 Nemotron 3 Super、NemoClaw、Nemotron-Terminal 三件事放在一起看，NVIDIA 的战略意图清晰得令人不安：<strong>它要成为 AI Agent 时代的「Intel Inside + Windows + Office」。</strong>Nemotron 3 Super 是模型层——120B 参数、MoE 架构、Blackwell 优化，直接对标 Llama 和 Mistral 但多了一层硬件绑定。NemoClaw 是平台层——企业用它编排 agent 工作流，一旦上了 NemoClaw，整个推理堆栈就锁定在 NVIDIA CUDA 生态里。Nemotron-Terminal 是能力层——训练 agent 不只是对话，而是在终端里真正执行命令、操作系统、部署代码。</p>'
            '<p>这三层加起来的意思是：你的 AI agent 用 NVIDIA 的模型、在 NVIDIA 的平台上编排、用 NVIDIA 的数据管道训练、跑在 NVIDIA 的 GPU 上。这是一个闭环。而且它用了一个聪明的策略——全部开源。听起来开放，但当你的整个 agent 基础设施都深度绑定 CUDA，「开源」只是一种更优雅的锁定方式。</p>'
            '<p>Anthropic 这边，Lawfare 的分析终于把法律牌摆上了桌面。政府的核心困境是一个逻辑自杀：<strong>你不能同时说一个产品「对国防至关重要」和「构成供应链风险」。</strong>如果 Claude 真的危险到要全联邦禁用，那五角大楼之前为什么要在机密网络上部署它？如果 Claude 只是合同谈判没谈拢，那 FASCSA（一部为应对中国、俄罗斯供应链渗透设计的法案）凭什么用来对付一家美国公司？Lawfare 的结论很直接：这个认定在法庭上撑不住。</p>'
            '<p>把这两条线连起来看更有趣：NVIDIA 在 Anthropic 被禁的真空中加速推 NemoClaw，向五角大楼的合作伙伴（Adobe、Salesforce、CrowdStrike）提供替代方案。OpenAI 拿到了 Anthropic 空出的国防合同。<strong>Anthropic 的伦理坚持客观上为竞争对手清了场——这是 2026 年 AI 行业最残酷的商业课。</strong>但如果 Lawfare 的判断正确，这个故事还没结束。法律博弈可能需要数月，而在这段时间里，市场格局已经重新划分。</p>'
            '</div>',
        "en": '<h3>📌 AI × Tech</h3><ul>'
            '<li><strong>NVIDIA Launches Nemotron 3 Super: 120B Open Model for Agentic AI</strong> — Hybrid MoE architecture with 12B active params, 5x throughput improvement on Blackwell. Powers NVIDIA AI-Q to #1 on DeepResearch Bench.<br><small>Source: <a href="https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/">NVIDIA Blog</a></small></li>'
            '<li><strong>Forbes: NVIDIA Pitches NemoClaw Agent Platform to Adobe, Salesforce, Google</strong> — A full enterprise AI agent orchestration platform. Nemotron models + NIM microservices + CUDA ecosystem = vertical integration of AI inference.<br><small>Source: <a href="https://www.forbes.com/sites/jonmarkman/2026/03/11/nvidia-moves-beyond-chips-with-an-open-source-platform-for-ai-agents/">Forbes</a></small></li>'
            '<li><strong>NVIDIA Releases Nemotron-Terminal for Training Terminal Agents</strong> — Open-source data pipeline for AI agents that actually execute code, not just chat about it.<br><small>Source: <a href="https://www.marktechpost.com/2026/03/10/nvidia-ai-releases-nemotron-terminal-a-systematic-data-engineering-pipeline-for-scaling-llm-terminal-agents/">MarkTechPost</a></small></li>'
            '<li><strong>Lawfare: Pentagon\'s Anthropic Designation Won\'t Survive Legal Challenge</strong> — The government can\'t simultaneously claim Claude is "vital to military ops" and a "grave supply chain risk." FASCSA was built for foreign adversaries, not domestic contract disputes.<br><small>Source: <a href="https://www.lawfaremedia.org/article/pentagon%E2%80%99s-anthropic-designation-won%E2%80%99t-survive-first-contact-with-legal-system">Lawfare</a></small></li>'
            '</ul>'
            '<h3>🔄 Trends</h3><ul>'
            '<li>NVIDIA\'s full-stack agent ambition: chips + models + orchestration + training data</li>'
            '<li>Anthropic saga enters legal phase: political pressure meets legal logic</li>'
            '<li>Terminal agents: AI that executes, not just converses</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex\'s Take</h3>'
            '<p><strong>NVIDIA no longer just sells shovels to gold miners — it wants to own the entire mine.</strong> Nemotron 3 Super (model) + NemoClaw (platform) + Nemotron-Terminal (training data) = a closed loop where your AI agents use NVIDIA models, orchestrated on NVIDIA\'s platform, trained with NVIDIA\'s pipeline, running on NVIDIA\'s GPUs. The "open source" label is elegant lock-in — when your entire agent infrastructure is CUDA-bound, openness is just a prettier form of capture.</p>'
            '<p>On Anthropic, Lawfare exposes the government\'s logical suicide: you can\'t call a product "vital to national defense" AND "a supply chain risk" simultaneously. FASCSA was designed for Chinese/Russian supply chain threats, not domestic contract disputes. This designation likely won\'t survive court. But while legal battles play out over months, NVIDIA fills the vacuum with NemoClaw, and OpenAI takes Anthropic\'s defense contracts. <strong>Anthropic\'s ethical stand cleared the field for competitors — 2026\'s cruelest business lesson.</strong></p>'
            '</div>'
    },
    "cover": og.get("nemotron") or og.get("nemoclaw"),
    "sources": [
        {
            "title": {"zh": "NVIDIA Nemotron 3 Super: 5x 吞吐量的 Agentic AI 模型", "en": "NVIDIA Nemotron 3 Super: 5x Throughput for Agentic AI"},
            "url": "https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/",
            "image": og.get("nemotron")
        },
        {
            "title": {"zh": "NVIDIA NemoClaw 开源 Agent 平台 - Forbes", "en": "NVIDIA NemoClaw Open-Source Agent Platform - Forbes"},
            "url": "https://www.forbes.com/sites/jonmarkman/2026/03/11/nvidia-moves-beyond-chips-with-an-open-source-platform-for-ai-agents/",
            "image": og.get("nemoclaw")
        },
        {
            "title": {"zh": "Nemotron-Terminal: 终端 Agent 数据工程管道", "en": "Nemotron-Terminal: Data Pipeline for Terminal Agents"},
            "url": "https://www.marktechpost.com/2026/03/10/nvidia-ai-releases-nemotron-terminal-a-systematic-data-engineering-pipeline-for-scaling-llm-terminal-agents/",
            "image": og.get("nemoterminal")
        },
        {
            "title": {"zh": "五角大楼对 Anthropic 的认定经不起法律考验 - Lawfare", "en": "Pentagon's Anthropic Designation Won't Survive Legal System - Lawfare"},
            "url": "https://www.lawfaremedia.org/article/pentagon%E2%80%99s-anthropic-designation-won%E2%80%99t-survive-first-contact-with-legal-system",
            "image": og.get("lawfare")
        }
    ]
}

# Load existing issues and prepend
issues_path = "/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json"
with open(issues_path, "r") as f:
    existing = json.load(f)

new_issues = [design_issue, tech_issue] + existing

with open(issues_path, "w") as f:
    json.dump(new_issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ issues.json updated: {len(new_issues)} total issues (2 new)")
