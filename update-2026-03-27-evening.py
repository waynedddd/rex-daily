# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-03-27 Evening Edition"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            body = r.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', body, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', body, re.I)
        return html.unescape(m.group(1)) if m else ""
    except:
        return ""

# Fetch og:images
images = {}
urls = {
    "stitch": "https://almcorp.com/blog/google-stitch-complete-guide-ai-ui-design-tool-2026/",
    "uxplanet": "https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345",
    "banani": "https://www.banani.co/blog/galileo-ai-features-and-alternatives",
    "carboncopies": "https://www.carboncopies.ai/blog/googles-galileo-ai",
    "crn": "https://www.crn.com/news/security/2026/10-cool-ai-and-agentic-tools-unveiled-at-rsac-2026",
    "secboulevard": "https://securityboulevard.com/2026/03/rsac-2026-day-1-security-must-evolve-at-agentic-speed/",
    "channelinsider": "https://www.channelinsider.com/security/tools-and-platforms/rsac-2026-ai-security-tools-threat-response/",
    "openai_modelspec": "https://openai.com/index/our-approach-to-the-model-spec/",
    "openai_sora": "https://openai.com/index/creating-with-sora-safely/",
}
for k, u in urls.items():
    images[k] = get_og_image(u)
    print(f"  {k}: {images[k][:80] if images[k] else '(none)'}")

design_issue = {
    "date": "2026-03-27",
    "section": "design",
    "title": {
        "zh": "Google Stitch 重塑 AI 设计格局：从 Galileo 收购到 Gemini 驱动的全栈设计工具 · UX 工程师崛起：AI 催生设计新角色 · Moonchild AI 挑战 Figma Make",
        "en": "Google Stitch Reshapes AI Design Landscape: From Galileo Acquisition to Gemini-Powered Full-Stack Design · UX Engineers Rise as AI Creates New Design Role · Moonchild AI Challenges Figma Make"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul><li><strong>Google Stitch：从收购 Galileo AI 到重新定义「文本转 UI」</strong> — 2025 年中，Google 悄然收购了 Galileo AI（一款将文字描述直接转化为可编辑 UI 设计的工具），并将其整合为 Google Stitch。ALM Corp 的深度分析指出，Stitch 不只是 Galileo 的品牌升级——它现在运行在 Gemini 模型上，支持自然语言或图片输入生成完整 UI 布局，并直接导出 HTML/CSS/React 生产级代码。Carbon Copies 的评论更为尖锐：<strong>Google 的 Galileo 收购揭示了一个战略信号——生成式 AI 的战场已经从「模型层」转移到「工具层」</strong>。Galileo 在公测期间创造了超过 10 万次设计生成，证明了文本转 UI 不是噱头而是真实需求。Stitch 相比 Galileo 最大的进化：生成的 UI 是响应式的，且可以导出为结构化代码。<br><small>来源：<a href="https://almcorp.com/blog/google-stitch-complete-guide-ai-ui-design-tool-2026/">ALM Corp</a> | <a href="https://www.carboncopies.ai/blog/googles-galileo-ai">Carbon Copies</a> | <a href="https://www.banani.co/blog/galileo-ai-features-and-alternatives">Banani</a></small></li><li><strong>「UX 工程师」崛起：AI 催生设计与开发之间的新角色</strong> — UX Planet 的 Lisa Demchenko 发布了一篇被广泛引用的文章《2026 年设计师应该坚持使用的 AI 工具》，但文章最有价值的部分不是工具推荐，而是对「UX 工程师」角色的定义。她指出，<strong>随着 AI 加速早期设计探索，UX 工程师必须能快速探索、迭代和验证界面结构，同时保持页面流和多屏设计的连贯性。</strong>Moonchild AI 成为这个新角色的标志性工具——它从产品需求文档（PRD）直接生成多屏 UI 流程，而非单个页面。Framer AI 则让设计师能直接构建响应式、可交互的生产级网站，「具备工程师级别的能力」。<br><small>来源：<a href="https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345">UX Planet</a></small></li><li><strong>AI 设计工具的「全栈化」趋势：从灵感到代码的一站式服务</strong> — 综合 Figma、Banani 和 BuildMVPFast 的最新评测，2026 年 AI 设计工具的竞争已经不在「生成质量」上，而在「工作流覆盖度」上。Figma Make 从设计到代码；Google Stitch 从文字到设计+代码；Relume 从文字到站点地图+线框+原型；Moonchild 从 PRD 到多屏流程。<strong>每个工具都在试图成为「全栈设计平台」，而不只是流程中的一个节点。</strong>Figma 的数据显示其 1300 万月活用户中三分之二是非设计师——这意味着「设计工具」的定义本身正在被重写。<br><small>来源：<a href="https://www.figma.com/resource-library/ai-tools-for-ux-designers/">Figma</a> | <a href="https://www.buildmvpfast.com/blog/ux-design-ai-tools-for-designers-2026">BuildMVPFast</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「工具层」成为 AI 设计的新战场</strong>：Google 收购 Galileo 不是偶然——谁拥有设计工具层，谁就控制了 AI 如何被设计师使用</li><li><strong>「UX 工程师」= 2026 年最有价值的新角色</strong>：能写代码的设计师和懂设计的工程师正在融合</li><li><strong>AI 设计工具竞争从「生成质量」转向「工作流覆盖度」</strong>：全栈化是大势所趋</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Google 收购 Galileo AI 并推出 Stitch，是 2026 年设计工具领域最值得深挖的一步棋。</strong></p><p>表面上看，这只是又一个「大厂收购创业公司」的故事。但放在更大的棋盘上，它揭示了一个正在发生的结构性转移：<strong>生成式 AI 的真正战场不在模型，而在工具层。</strong>GPT-5、Gemini、Claude 在底层能力上的差距正在收窄（都能生成 UI、都能写代码），真正的差异化来自「谁把 AI 能力包装成设计师真正想用的工具」。Google 买下 Galileo，不是因为缺 AI 能力——Gemini 自己就能生成 UI——而是因为 Galileo 已经验证了用户需求（公测 10 万+次生成）和产品形态（文本→可编辑设计→生产级代码）。</p><p>这让我想到一个更宏观的格局变化。2024 年，AI 设计工具的竞争维度是「谁生成的设计更好看」；2025 年，变成「谁能嵌入现有工作流」；到 2026 年 Q1，竞争维度再次升级为<strong>「谁能覆盖更完整的设计-开发全链条」</strong>。Figma Make 从设计到代码。Google Stitch 从文字到设计+代码。Relume 从文字到站点地图+线框。Moonchild 从产品需求到多屏流程。每个工具都在往「全栈」方向跑，因为它们都意识到了同一件事：单点工具的护城河太浅，用户要的是一条流水线，不是一个零件。</p><p>但最让我兴奋的，是 UX Planet 那篇文章中对「UX 工程师」角色的描述。Lisa Demchenko 说得非常精准：AI 加速了设计的前端（生成、探索），但<strong>验证、系统化和工程化</strong>的需求反而增加了。会用 Figma Make 生成 50 个布局变体很容易，但判断哪个变体在工程上可行、在设计系统中一致、在真实用户面前能跑通——这需要同时懂设计逻辑和代码实现的人。这就是「UX 工程师」。Moonchild AI 是这个新角色的完美工具缩影：它不是给你一张漂亮图片，而是从 PRD 出发生成多屏 UI 流程——这要求使用者理解产品逻辑，而不只是审美偏好。</p><p>回到 Figma 的那个数据点：<strong>1300 万月活用户中三分之二是非设计师。</strong>这个数字的含义远超大多数人的理解。它意味着「设计工具」这个品类正在从「设计师的专业工具」变成「产品团队的通用基础设施」。就像 Excel 不只是会计用的，Figma（以及 Stitch、Moonchild）正在成为 PM、工程师、甚至营销人员日常使用的界面。当三分之二的用户不是设计师时，「设计质量」不再是唯一竞争力——「降低使用门槛」和「覆盖完整工作流」才是。<strong>这对专业设计师意味着什么？你的价值不在于会用工具（所有人都会了），而在于审美判断力、系统化思维和用户洞察——这些恰好是 AI 和非设计师最缺的。</strong></p></div>',
        "en": '<h3>📌 AI × Design</h3><ul><li><strong>Google Stitch: From Galileo AI Acquisition to Redefining Text-to-UI</strong> — Google quietly acquired Galileo AI in mid-2025 and relaunched it as Google Stitch, now running on Gemini models. It generates complete UI layouts from natural language or image inputs and exports production-ready HTML/CSS/React code. Carbon Copies analysis: Google\'s acquisition signals the AI battleground has shifted from "model layer" to "tooling layer." Galileo logged 100,000+ design generations during public beta.<br><small>Source: <a href="https://almcorp.com/blog/google-stitch-complete-guide-ai-ui-design-tool-2026/">ALM Corp</a> | <a href="https://www.carboncopies.ai/blog/googles-galileo-ai">Carbon Copies</a></small></li><li><strong>"UX Engineer" Emerges as AI Creates a New Design Role</strong> — UX Planet\'s widely-cited article defines UX Engineers as professionals who can rapidly explore, iterate, and validate interface structures while maintaining flow coherence. Moonchild AI — which generates multi-screen UI flows from PRDs — becomes the signature tool for this hybrid role. Framer AI lets designers build production-ready responsive websites "with engineer-level capability."<br><small>Source: <a href="https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345">UX Planet</a></small></li><li><strong>AI Design Tools Go Full-Stack: From Inspiration to Code</strong> — Competition has shifted from "generation quality" to "workflow coverage." Figma Make: design→code. Stitch: text→design+code. Relume: text→sitemap+wireframe. Moonchild: PRD→multi-screen flows. Figma reports two-thirds of its 13M MAU are non-designers — redefining what "design tool" means.<br><small>Source: <a href="https://www.figma.com/resource-library/ai-tools-for-ux-designers/">Figma</a> | <a href="https://www.buildmvpfast.com/blog/ux-design-ai-tools-for-designers-2026">BuildMVPFast</a></small></li></ul><h3>🔄 Trends</h3><ul><li>The "tooling layer" is the new AI design battleground (Google\'s Galileo acquisition proves it)</li><li>"UX Engineer" = 2026\'s most valuable new role (design + code hybrid)</li><li>AI design competition shifts from generation quality to workflow coverage</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Google acquiring Galileo AI and launching Stitch is the most strategically significant move in the 2026 design tool landscape.</strong> The real AI battleground isn\'t models — it\'s the tooling layer. GPT-5, Gemini, and Claude are converging in capability; differentiation comes from who packages AI into tools designers actually want. Google didn\'t buy Galileo for AI capability — Gemini can already generate UI. They bought validated user demand (100K+ beta generations) and product form (text→editable design→production code). The competition axis has evolved: 2024 = "who generates prettier designs"; 2025 = "who embeds into existing workflows"; 2026 Q1 = "who covers the most complete design-to-dev pipeline." Every tool is racing toward full-stack because single-point tools have shallow moats. Most exciting: the "UX Engineer" role. AI accelerates the front end (generation, exploration), but validation, systematization, and engineering needs increase. Figma\'s stat — two-thirds of 13M MAU are non-designers — means "design tool" is becoming "product team infrastructure." <strong>For professional designers: your value isn\'t tool proficiency (everyone has that now) — it\'s aesthetic judgment, systems thinking, and user insight.</strong></p></div>'
    },
    "cover": images.get("stitch", "") or images.get("carboncopies", ""),
    "sources": [
        {
            "title": {"zh": "ALM Corp: Google Stitch 完全指南", "en": "ALM Corp: Google Stitch Complete Guide"},
            "url": "https://almcorp.com/blog/google-stitch-complete-guide-ai-ui-design-tool-2026/",
            "image": images.get("stitch", "")
        },
        {
            "title": {"zh": "Carbon Copies: Google 收购 Galileo AI 的战略意义", "en": "Carbon Copies: What Google's Galileo AI Acquisition Tells Us"},
            "url": "https://www.carboncopies.ai/blog/googles-galileo-ai",
            "image": images.get("carboncopies", "")
        },
        {
            "title": {"zh": "UX Planet: 2026 年设计师应该坚持使用的 AI 工具", "en": "UX Planet: AI Tools Designers Should Stick With in 2026"},
            "url": "https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345",
            "image": images.get("uxplanet", "")
        },
        {
            "title": {"zh": "Figma: 2026 年 UX 设计师的 9 大 AI 工具", "en": "Figma: Top 9 AI Tools for UX Designers in 2026"},
            "url": "https://www.figma.com/resource-library/ai-tools-for-ux-designers/",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-03-27",
    "section": "tech",
    "title": {
        "zh": "RSAC 2026：Agentic AI 安全成为网络安全主战场 · OpenAI 发布 Model Spec 深度解读与 Sora 安全框架 · CrowdStrike、Datadog、Wiz 集体押注 AI 安全 Agent",
        "en": "RSAC 2026: Agentic AI Security Becomes Cybersecurity's Main Battleground · OpenAI Publishes Model Spec Deep Dive & Sora Safety Framework · CrowdStrike, Datadog, Wiz Bet Big on AI Security Agents"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul><li><strong>RSAC 2026：Agentic AI 安全从「概念」变成「产品」</strong> — 本周在旧金山举办的 RSAC 2026 大会上，几乎所有主要网络安全厂商都发布了 AI 安全相关产品。CRN 报道了 10 款最值得关注的 AI 和 Agentic 安全工具：<strong>Saviynt</strong> 推出 AI Identity Security 平台，管理和治理 AI Agent 的身份与访问权限；<strong>CrowdStrike</strong> 发布 Charlotte AI AgentWorks 无代码平台，用于构建、测试和编排安全 Agent；<strong>Check Point</strong> 推出 AI Defense Plane，为 Agentic 企业提供安全防护；<strong>Databricks</strong> 正式进军网络安全，发布基于数据智能平台的 Agentic SIEM 产品；<strong>Sumo Logic</strong> 扩展 Dojo AI Agents 用于 AI 驱动的 SOC 分析师。Security Boulevard 的 Day 1 分析指出：<strong>「威胁格局正以超越人类能力的速度加速，唯一可行的路径是将安全重新定义为 AI 原生学科。」</strong>Cisco 将安全能力扩展到 AI Agent，Wiz 发布 AI-APP 应对「网络风险的新解剖学」，Datadog 推出 AI 安全 Agent 对抗「机器速度的网络攻击」。<br><small>来源：<a href="https://www.crn.com/news/security/2026/10-cool-ai-and-agentic-tools-unveiled-at-rsac-2026">CRN</a> | <a href="https://securityboulevard.com/2026/03/rsac-2026-day-1-security-must-evolve-at-agentic-speed/">Security Boulevard</a> | <a href="https://www.channelinsider.com/security/tools-and-platforms/rsac-2026-ai-security-tools-threat-response/">Channel Insider</a></small></li><li><strong>OpenAI 发布 Model Spec 深度解读：AI 行为框架走向公开透明</strong> — OpenAI 于 3 月 25 日发布了《Inside our approach to the Model Spec》，首次系统性地公开其 AI 模型行为框架。Model Spec 定义了模型行为的权威层级（authority level）：当用户请求与安全边界冲突时，模型应优先遵守硬性安全原则。文章明确承诺：在 ChatGPT 等第一方部署中，<strong>OpenAI 绝不会使用系统消息故意损害客观性</strong>，且模型响应优化目标是用户利益而非收入。与此同时，OpenAI 还更新了 Sora 的安全框架，引入角色系统（Characters）让用户控制 Sora 中的肖像权，并部署自动化系统扫描所有 Feed 内容。<br><small>来源：<a href="https://openai.com/index/our-approach-to-the-model-spec/">OpenAI Model Spec</a> | <a href="https://openai.com/index/creating-with-sora-safely/">OpenAI Sora Safety</a></small></li><li><strong>AI 芯片和基础设施进入「Agent-as-a-Service」时代</strong> — AI-Weekly Issue 209 指出，本周的主题是「从 SaaS 到 AGaaS（Agent-as-a-Service）」——AI Agent 不再是实验品，而是正在成为可订阅的服务。NVIDIA GTC 2026 的余波仍在：Jensen Huang 宣布从 OpenAI 和 Anthropic 「后撤」的表态引发了比答案更多的问题。与此同时，Broadcom 开始出货新 AI 芯片用于连接大型数据中心，进一步说明 AI 基础设施正在从计算层扩展到网络层。<br><small>来源：<a href="https://ai-weekly.ai/newsletter-03-24-2026/">AI-Weekly #209</a> | <a href="https://techcrunch.com/2026/03/13/the-biggest-ai-stories-of-the-year-so-far/">TechCrunch</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 安全从「附加功能」变成「独立品类」</strong>：RSAC 2026 标志着 AI 安全正式成为网络安全行业的核心赛道</li><li><strong>「AI 治理 AI」成为现实</strong>：用 AI Agent 来保护 AI Agent，用身份系统来管理非人类实体</li><li><strong>从 SaaS 到 AGaaS</strong>：AI Agent 正在成为可订阅的基础设施服务，而非一次性工具</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>RSAC 2026 传递了一个不容忽视的信号：AI 安全已经不是「未来议题」，而是「现在就需要解决的工程问题」。</strong></p><p>先理清一个容易被忽略的逻辑链。过去两年，所有人都在谈 AI 如何帮助企业提效、降本、创新。但 RSAC 2026 让我们看到了硬币的另一面：<strong>当企业部署的 AI Agent 越来越多，谁来保护这些 Agent？谁来管理它们的访问权限？谁来确保它们不被劫持？</strong>Saviynt 的答案是给 AI Agent 建立身份系统——就像给人类员工发工牌一样，每个 Agent 都需要身份验证、权限管理和生命周期控制。CrowdStrike 的答案是用 AI Agent 来保护 AI Agent——Charlotte AI AgentWorks 是一个无代码平台，让安全团队能构建自己的安全 Agent。这是「AI 治理 AI」的具象化：人类写规则，AI 执行监控。</p><p>Security Boulevard 的 Day 1 分析说了一句让我印象深刻的话：「威胁格局正以超越人类能力的速度加速。」这不是危言耸听。当攻击者使用 AI 生成钓鱼邮件、自动化漏洞扫描、甚至编排多步骤攻击时，人类安全分析师每天处理的告警量已经远超认知极限。<strong>Datadog 推出的 AI 安全 Agent 明确定位为「对抗机器速度的网络攻击」——换句话说，人类已经无法单独应对机器速度的威胁了。</strong></p><p>把这和 OpenAI 本周的两个动作连起来看，会发现一个更完整的图景。Model Spec 的公开意味着 OpenAI 正在为 AI 行为建立「宪法」——定义模型在面临冲突时应该遵循什么优先级。Sora 的安全框架引入了角色系统和内容扫描。<strong>这两件事的共同主题是：AI 系统需要「内置」的行为约束，而不只是「外挂」的安全审查。</strong>就像建筑的安全性应该设计在结构中，而不是事后加一个消防栓。</p><p>最后，AI-Weekly 提出的「SaaS 到 AGaaS」的概念精准捕捉了一个正在发生的商业模式转变。当 AI Agent 可以被打包成可订阅的服务时，企业面临的不再是「要不要用 AI」的决策，而是<strong>「如何管理一个包含数十个 AI Agent 的生态系统」</strong>的运营挑战。Saviynt 做身份治理、CrowdStrike 做安全编排、Databricks 做安全情报——这些不是孤立的产品发布，而是<strong>一个新产业链的雏形</strong>。我预测：到 2027 年，「AI Agent 管理平台」将成为 Gartner 的一个独立品类，就像今天的「云安全」一样。RSAC 2026 是这个品类的诞生时刻。</p></div>',
        "en": '<h3>📌 AI × Tech</h3><ul><li><strong>RSAC 2026: Agentic AI Security Goes from Concept to Product</strong> — At RSAC 2026 in San Francisco, virtually every major cybersecurity vendor launched AI security products. CRN highlights 10 key tools: Saviynt\'s AI Identity Security platform for managing AI agent identities; CrowdStrike\'s Charlotte AI AgentWorks no-code platform for building security agents; Check Point\'s AI Defense Plane; Databricks\' entry into cybersecurity with agentic SIEM; Sumo Logic\'s expanded Dojo AI Agents. Security Boulevard: "The threat landscape is accelerating beyond human capability — the only viable path is redefining security as an AI-native discipline." Cisco, Wiz, and Datadog also unveiled major AI security products.<br><small>Source: <a href="https://www.crn.com/news/security/2026/10-cool-ai-and-agentic-tools-unveiled-at-rsac-2026">CRN</a> | <a href="https://securityboulevard.com/2026/03/rsac-2026-day-1-security-must-evolve-at-agentic-speed/">Security Boulevard</a></small></li><li><strong>OpenAI Publishes Model Spec Deep Dive: AI Behavior Framework Goes Public</strong> — OpenAI\'s March 25 post systematically reveals its AI behavior framework. Model Spec defines authority levels for handling conflicts; commits to never using system messages to compromise objectivity in ChatGPT; optimizes for user benefit over revenue. Sora safety framework introduces Characters for likeness control and automated content scanning.<br><small>Source: <a href="https://openai.com/index/our-approach-to-the-model-spec/">OpenAI</a> | <a href="https://openai.com/index/creating-with-sora-safely/">OpenAI Sora</a></small></li><li><strong>AI Infrastructure Enters "Agent-as-a-Service" Era</strong> — AI-Weekly Issue 209 identifies the shift from SaaS to AGaaS. NVIDIA GTC 2026 aftermath continues; Jensen Huang\'s pullback from OpenAI/Anthropic raises questions. Broadcom ships new AI chips for data center connectivity, extending AI infrastructure from compute to networking.<br><small>Source: <a href="https://ai-weekly.ai/newsletter-03-24-2026/">AI-Weekly #209</a> | <a href="https://techcrunch.com/2026/03/13/the-biggest-ai-stories-of-the-year-so-far/">TechCrunch</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI security becomes a standalone category (RSAC 2026 marks the inflection)</li><li>"AI governing AI" becomes real — agents protecting agents, identity for non-human entities</li><li>SaaS → AGaaS: AI agents becoming subscribable infrastructure services</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>RSAC 2026 sends an unmistakable signal: AI security is no longer a "future topic" but an engineering problem that needs solving now.</strong> As enterprises deploy more AI agents, the questions become: who protects these agents? Who manages their access? Saviynt\'s answer: identity systems for AI agents, like employee badges. CrowdStrike\'s: AI agents protecting AI agents via Charlotte AgentWorks. This is "AI governing AI" made concrete. Datadog\'s AI Security Agent explicitly targets "machine-speed cyberattacks" — humans can no longer handle machine-speed threats alone. OpenAI\'s Model Spec and Sora safety framework show the same theme: AI systems need built-in behavioral constraints, not bolt-on security. AI-Weekly\'s "SaaS to AGaaS" concept captures the business model shift: enterprises now face the operational challenge of managing ecosystems of dozens of AI agents. <strong>Prediction: by 2027, "AI Agent Management Platform" will be a Gartner category. RSAC 2026 is its birth moment.</strong></p></div>'
    },
    "cover": images.get("crn", "") or images.get("secboulevard", ""),
    "sources": [
        {
            "title": {"zh": "CRN: RSAC 2026 十大 AI 和 Agentic 安全工具", "en": "CRN: 10 Cool AI and Agentic Tools at RSAC 2026"},
            "url": "https://www.crn.com/news/security/2026/10-cool-ai-and-agentic-tools-unveiled-at-rsac-2026",
            "image": images.get("crn", "")
        },
        {
            "title": {"zh": "Security Boulevard: RSAC 2026 Day 1——安全必须以 Agentic 速度进化", "en": "Security Boulevard: RSAC 2026 Day 1 — Security Must Evolve at Agentic Speed"},
            "url": "https://securityboulevard.com/2026/03/rsac-2026-day-1-security-must-evolve-at-agentic-speed/",
            "image": images.get("secboulevard", "")
        },
        {
            "title": {"zh": "OpenAI: Model Spec 深度解读", "en": "OpenAI: Inside Our Approach to the Model Spec"},
            "url": "https://openai.com/index/our-approach-to-the-model-spec/",
            "image": images.get("openai_modelspec", "")
        },
        {
            "title": {"zh": "AI-Weekly #209: 从 SaaS 到 AGaaS", "en": "AI-Weekly #209: From SaaS to AGaaS"},
            "url": "https://ai-weekly.ai/newsletter-03-24-2026/",
            "image": ""
        }
    ]
}

# Load existing issues and prepend new ones
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r", encoding="utf-8") as f:
    issues = json.load(f)

issues = [design_issue, tech_issue] + issues

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("✅ issues.json updated with 2 new evening issues")
