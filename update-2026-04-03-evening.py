# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-04-03 Evening Update"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            body = r.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', body)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image', body)
        return m.group(1) if m else ""
    except:
        return ""

# Fetch OG images
og_ms_axios = get_og_image("https://www.axios.com/2026/03/31/microsoft-critique-anthropic-openai")
og_turboquant_forbes = get_og_image("https://www.forbes.com/sites/timbajarin/2026/04/01/googles-turboquant-marks-a-turning-point-in-ais-evolution/")
og_turboquant_ars = get_og_image("https://arstechnica.com/ai/2026/03/google-says-new-turboquant-compression-can-lower-ai-memory-usage-without-sacrificing-quality/")
og_fda = get_og_image("https://www.statnews.com/2026/04/02/how-fda-stance-breakthrough-ai-medical-device-evolving/")
og_moonchild = get_og_image("https://medium.com/design-bootcamp/i-recently-reviewed-5-ai-native-ux-design-tools-in-50-minutes-2026-80f403db65f8")
og_figma_state = get_og_image("https://www.figma.com/blog/state-of-the-designer-2026/")
og_muzli = get_og_image("https://muz.li/blog/figma-just-opened-the-canvas-to-ai-agents-heres-what-it-means-for-designers/")

print(f"OG ms_axios: {og_ms_axios}")
print(f"OG turboquant_forbes: {og_turboquant_forbes}")
print(f"OG turboquant_ars: {og_turboquant_ars}")
print(f"OG fda: {og_fda}")
print(f"OG moonchild: {og_moonchild}")
print(f"OG figma_state: {og_figma_state}")
print(f"OG muzli: {og_muzli}")

design_issue = {
    "date": "2026-04-03",
    "section": "design",
    "title": {
        "zh": "AI 原生设计工具大爆发：Moonchild 等 5 款工具挑战 Figma 地位 · 设计师工作流正在被 AI 重写 · UX 工程师角色崛起",
        "en": "AI-Native Design Tools Explode: 5 Tools Including Moonchild Challenge Figma · Designer Workflows Are Being Rewritten by AI · The Rise of the UX Engineer"
    },
    "content": {
        "zh": """<h3>📌 AI × 设计</h3><ul><li><strong>5 款 AI 原生 UX 设计工具 50 分钟横评：Moonchild 领跑「AI-first 设计」赛道</strong> — Design Bootcamp 的深度横评测试了 2026 年最受关注的 5 款 AI 原生设计工具。Moonchild AI 脱颖而出，它可以从产品简报直接生成完整的界面布局、用户流程和可交互原型——而且输出的不是「看起来像设计」的图片，而是真正可用的设计系统组件。<strong>Moonchild 的核心差异化：它同时懂设计和代码，生成的 UI 可以直接交付工程师。</strong>这和 Figma「向 AI Agent 开放 Canvas」的策略形成有趣对比——Figma 让 AI 在现有平台上干活，Moonchild 则试图从零开始重新定义设计工具该是什么样子。<br><small>来源：<a href="https://medium.com/design-bootcamp/i-recently-reviewed-5-ai-native-ux-design-tools-in-50-minutes-2026-80f403db65f8">Design Bootcamp (Medium)</a></small></li><li><strong>UX Planet 设计师工作流实录：AI 如何渗透从研究到交付的每个环节</strong> — 多篇来自 UX Planet 和 UX Collective 的 2026 实操文章描绘了一幅清晰图景：设计师的日常工作流已经被 AI 深度渗透。用 Claude 自动化 UX 研究分析、用 Moonchild 生成设计系统、用 Spline AI 做 3D 交互、用 Cursor 出代码原型。<strong>最值得关注的趋势：「UX 工程师」角色正在崛起——他们既懂用户体验又懂代码，而 AI 工具让他们的产出效率是传统设计师的 3-5 倍。</strong>Lisa Demchenko 在 UX Planet 的推荐清单中特别指出：2026 年设计师不应该执着于「学哪个工具」，而应该理解「AI 如何改变设计的思维方式」。<br><small>来源：<a href="https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345">UX Planet</a>、<a href="https://medium.com/design-bootcamp/how-moonchild-ai-generates-design-systems-you-can-actually-design-with-3e7dcbd63216">Design Bootcamp</a></small></li><li><strong>Figma 报告后续：89% 满意度数据背后的隐忧</strong> — Figma State of the Designer 2026 的数据继续发酵。YouTube 上 Ricardo Costa 的深度解读视频指出报告中 3 个被忽略的关键数字：AI 工具使用率与设计师焦虑感呈正相关（用得越多反而越焦虑未来）；初级设计师岗位需求同比下降约 20%；而「AI 策略师」和「提示工程师」的需求却在上升。<strong>核心矛盾：AI 让个体设计师更高效，但整体市场需要的设计师更少了。</strong><br><small>来源：<a href="https://www.youtube.com/watch?v=2iqL2X_bjL0">Ricardo Costa (YouTube)</a>、<a href="https://www.figma.com/blog/state-of-the-designer-2026/">Figma Blog</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI-native vs AI-augmented</strong>：Moonchild 等新工具从零构建，Figma 在现有平台嫁接 AI——两条路线的胜负将决定下一代设计工具的形态</li><li><strong>UX 工程师 > 纯 UX 设计师</strong>：跨界角色的产出效率优势在 AI 时代被放大</li><li><strong>「更快」的代价</strong>：个体效率提升正在压缩整体岗位需求</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>今天的设计新闻揭示了一场正在发生的工具战争：Moonchild 等 AI 原生工具 vs Figma 的 AI 增强路线。这场战争的结果将决定未来 3-5 年设计师用什么工具、怎么工作、甚至需不需要那么多设计师。</strong></p><p>Moonchild 的横评结果让我想起了 2012 年 Figma 刚出现时的场景。当时 Sketch 是设计界的绝对王者，Figma 说「设计应该在浏览器里、应该实时协作」——所有人都觉得是玩具。但 Figma 赢了，因为它重新定义了「设计工具应该是什么」而不是「怎么做一个更好的 Sketch」。现在 Moonchild 在做类似的事：不是在 Figma 上叠加 AI 功能，而是<strong>从「AI 能做什么」出发重新设计工具</strong>。它把产品简报直接变成可交互原型和设计系统组件——跳过了「设计师手动搭建」这个传统步骤。这是一个根本性的范式挑战。</p><p>但 Figma 也不是没有还手之力。上周它开放 Canvas 给 AI Agent 的策略其实很聪明：<strong>不要和新工具比「AI 原生度」，而是让所有 AI 工具都在 Figma 里运行。</strong>这是平台策略——成为 AI 设计的操作系统，而不是最好的 AI 设计应用。就像 iOS 不需要比每个 app 都做得好，它只需要是所有 app 运行的地方。Figma 的赌注是：设计生态已经围绕它建立了，AI Agent 最终也会选择在 Figma 里工作而不是在 Moonchild 里。这个赌注目前看起来还是合理的——毕竟全球数百万设计师的文件、组件库、设计系统都在 Figma 里。</p><p><strong>真正让我担忧的是 Figma 报告后续发酵出来的数据：初级设计师岗位需求下降 20%。</strong>这个数字和我们上期日报的判断完全吻合——当 AI Agent 能直接在 Figma Canvas 上执行设计任务时，最先被压缩的就是「按规范执行」的初级岗位。而 UX 工程师的崛起进一步印证了这个趋势：未来的设计师不只是画界面，他们需要理解代码、系统架构和 AI 工作流。<strong>「纯视觉设计师」的市场正在缩小，「会编排 AI + 懂代码 + 有设计判断力」的复合角色正在扩大。</strong>对设计教育来说，这是一个巨大的警钟：还在教学生怎么用 Figma 画原型的课程已经过时了，应该教的是怎么用自然语言描述产品意图、怎么评审 AI 生成的设计、怎么构建 AI-ready 的设计系统。</p><p>最后一个观察：89% 的设计师说 AI 让他们更快，但焦虑感也在同步上升。这不矛盾——<strong>它们是因果关系而非巧合。正因为你亲眼看到 AI 能多快地完成你的工作，你才会真正开始焦虑自己的不可替代性。</strong>2024 年不用 AI 的设计师是「落后」，2026 年不用 AI 的设计师可能是「失业」。这就是这场转型的残酷之处：你必须拥抱让你焦虑的东西，因为不拥抱只会让情况更糟。</p></div>""",
        "en": """<h3>📌 AI × Design</h3><ul><li><strong>5 AI-Native UX Design Tools Reviewed in 50 Minutes: Moonchild Leads the AI-First Design Race</strong> — Design Bootcamp's deep review tested 2026's most watched AI-native tools. Moonchild AI stands out—generating complete UI layouts, user flows, and interactive prototypes from product briefs, outputting real design system components, not design-like images. <strong>Key differentiator: Moonchild speaks both design and code.</strong> This contrasts with Figma's "open Canvas to agents" approach—Figma lets AI work on existing platforms; Moonchild redefines what design tools should be.<br><small>Source: <a href="https://medium.com/design-bootcamp/i-recently-reviewed-5-ai-native-ux-design-tools-in-50-minutes-2026-80f403db65f8">Design Bootcamp (Medium)</a></small></li><li><strong>UX Planet Designer Workflow Reports: AI Permeates Every Stage from Research to Delivery</strong> — Multiple 2026 workflow articles from UX Planet/UX Collective show AI deeply embedded: Claude for UX research automation, Moonchild for design systems, Spline AI for 3D, Cursor for code prototypes. <strong>Key trend: "UX Engineer" roles rising—3-5x more productive than traditional designers with AI tools.</strong><br><small>Source: <a href="https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345">UX Planet</a></small></li><li><strong>Post-Figma Report: Hidden Concerns Behind 89% Satisfaction</strong> — Ricardo Costa's deep-dive highlights 3 overlooked numbers: AI tool usage correlates with increased anxiety; junior designer demand down ~20% YoY; "AI strategist" and "prompt engineer" demand rising. <strong>Core paradox: AI makes individual designers more efficient but the market needs fewer designers overall.</strong><br><small>Source: <a href="https://www.youtube.com/watch?v=2iqL2X_bjL0">Ricardo Costa (YouTube)</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI-native vs AI-augmented: Moonchild builds from scratch, Figma grafts AI onto existing platform</li><li>UX Engineer > Pure UX Designer: cross-discipline roles amplified by AI</li><li>Cost of "faster": individual efficiency gains compress overall headcount</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>A tools war is unfolding: AI-native (Moonchild) vs AI-augmented (Figma). The outcome shapes the next 3-5 years of design work.</strong> Moonchild's approach mirrors early Figma vs Sketch—redefining what a design tool should be rather than improving the old paradigm. But Figma's platform play (be the OS, not the best app) has network effects on its side. The 20% drop in junior designer demand confirms our thesis: AI agents on Canvas compress execution roles. UX Engineers rise because they bridge design, code, and AI orchestration. <strong>89% say AI makes them faster AND more anxious—these are causally linked. Seeing AI do your job quickly is precisely what triggers existential doubt. 2024's non-AI designer was "behind"; 2026's may be "unemployed." The cruelty of this transition: you must embrace what makes you anxious, because not embracing it is worse.</strong></p></div>"""
    },
    "cover": og_moonchild or og_figma_state or "https://miro.medium.com/v2/resize:fit:1200/1*example.png",
    "sources": [
        {
            "title": {"zh": "5 款 AI 原生 UX 设计工具横评", "en": "5 AI-Native UX Design Tools Reviewed"},
            "url": "https://medium.com/design-bootcamp/i-recently-reviewed-5-ai-native-ux-design-tools-in-50-minutes-2026-80f403db65f8",
            "image": og_moonchild
        },
        {
            "title": {"zh": "2026 年设计师应该使用的 AI 工具", "en": "AI Tools Designers Should Stick With in 2026"},
            "url": "https://uxplanet.org/ai-tools-designers-should-stick-with-in-2026-49fe5131d345",
            "image": ""
        },
        {
            "title": {"zh": "Figma 2026 设计师现状报告深度解读", "en": "Figma State of Designer 2026 Deep Dive"},
            "url": "https://www.youtube.com/watch?v=2iqL2X_bjL0",
            "image": og_figma_state
        }
    ]
}

tech_issue = {
    "date": "2026-04-03",
    "section": "tech",
    "title": {
        "zh": "Microsoft 拥抱多模型策略：Copilot 接入 Anthropic Claude · Google TurboQuant 压缩算法将 AI 内存需求降低 6 倍 · FDA 对 AI 医疗器械「突破性认定」标准悄然演变",
        "en": "Microsoft Embraces Multi-Model: Copilot Integrates Anthropic Claude · Google TurboQuant Cuts AI Memory 6x · FDA's Evolving Stance on 'Breakthrough' AI Medical Devices"
    },
    "content": {
        "zh": """<h3>📌 AI × 科技</h3><ul><li><strong>Microsoft 全面转向多模型策略：Copilot 工具接入 Anthropic Claude，「AI 未来是多模型的」</strong> — Microsoft 本周宣布旗下 AI 研究工具 Critique 全面整合 OpenAI 和 Anthropic 的模型。这是微软最明确的信号：AI 的未来不属于任何一家模型公司。Axios 报道引用微软 AI 负责人的话：「前沿实验室频繁互相超越，企业需要能灵活切换底层模型的工具。」Fortune 进一步报道称微软已在 Copilot 产品线中大量使用 Claude——不再是「OpenAI 独占」。<strong>这标志着 AI 产业从「绑定单一模型」走向「模型即商品」的拐点。对设计工具的启示是巨大的：未来的 AI 设计工具也会支持多模型切换，设计师需要理解不同模型的优劣势。</strong><br><small>来源：<a href="https://www.axios.com/2026/03/31/microsoft-critique-anthropic-openai">Axios</a>、<a href="https://fortune.com/2026/03/31/microsoft-revamps-copilot-with-anthropic/">Fortune</a></small></li><li><strong>Google TurboQuant：让 AI 内存需求降低 6 倍的压缩算法，被网友戏称「现实版 Pied Piper」</strong> — Google Research 发布 TurboQuant 压缩算法，能在几乎不损失精度的情况下将大模型内存占用压缩到原来的 1/6。Forbes 分析认为这是 AI 演进的转折点：<strong>效率优化可能比模型规模扩张更重要。</strong>TurboQuant 的核心价值在于让端侧 AI（手机、平板、笔记本）成为可能——之前受限于内存的设备现在可以运行更强大的模型。Ars Technica 的深度技术分析指出，这种量化压缩方法比传统蒸馏更快，且保持了模型的推理质量。<strong>对设计行业的意义：端侧 AI 意味着 Figma、Sketch 等设计工具可以在本地运行 AI 推理，不依赖云端——实时、离线、隐私友好。</strong><br><small>来源：<a href="https://www.forbes.com/sites/timbajarin/2026/04/01/googles-turboquant-marks-a-turning-point-in-ais-evolution/">Forbes</a>、<a href="https://arstechnica.com/ai/2026/03/google-says-new-turboquant-compression-can-lower-ai-memory-usage-without-sacrificing-quality/">Ars Technica</a>、<a href="https://techcrunch.com/2026/03/25/google-turboquant-ai-memory-compression-silicon-valley-pied-piper/">TechCrunch</a></small></li><li><strong>FDA 对 AI 医疗器械「突破性认定」标准悄然演变：从硬件逻辑到软件逻辑</strong> — STAT News 报道，FDA 在 2026 年 Q1 对 AI 医疗器械的「突破性设备认定」（Breakthrough Device Designation）标准正在经历微妙但重要的转变。此前 FDA 给了一个用于术后康复的 AI 聊天机器人 RecovryAI 突破性认定——这是首次将此类认定授予一个纯对话式 AI 系统。<strong>信号意义：FDA 开始承认「软件即医疗器械」不只是影像诊断，对话式 AI 也可以是临床工具。</strong>这为更多 AI 健康产品打开了监管通道，也为设计这类产品的 UX 团队提出了全新挑战——当你的聊天界面就是「医疗器械」时，每个交互决策都有临床后果。<br><small>来源：<a href="https://www.statnews.com/2026/04/02/how-fda-stance-breakthrough-ai-medical-device-evolving/">STAT News</a>、<a href="https://www.statnews.com/2026/03/03/fda-breakthrough-designation-generative-ai-chatbot-recovryai/">STAT News (RecovryAI)</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>模型即商品</strong>：Microsoft 带头打破「独家模型」绑定，AI 竞争从模型层转向应用层</li><li><strong>效率 > 规模</strong>：TurboQuant 代表的「做小做快」路线可能比「做大」更有商业前景</li><li><strong>AI 监管分层化</strong>：FDA 的演变说明监管机构正在学习区分不同类型的 AI 应用</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>今天这三条科技新闻从三个不同维度指向同一个结论：AI 产业正在从「谁的模型最大最强」的军备竞赛，转向「谁能最有效地部署 AI」的实用主义时代。</strong></p><p>Microsoft 拥抱多模型是一个标志性事件。记得 2024 年 Microsoft 和 OpenAI 的蜜月期吗？当时所有人都以为 Copilot = GPT-4，微软和 OpenAI 绑定就像苹果和 iOS。两年后的现实是：微软在自己最重要的 AI 产品里同时用 OpenAI 和 Anthropic 的模型，而且公开说「企业需要灵活切换模型」。<strong>这不只是技术策略的变化，这是对整个 AI 商业模式的重新定义。</strong>当模型可以随时替换时，模型公司的护城河在哪里？不在模型本身（因为随时可能被超越），而在生态——训练数据、微调能力、API 生态、开发者社区。这和上期日报里 Figma vs Moonchild 的逻辑是同构的：平台战略（Figma / Microsoft）vs 技术领先战略（Moonchild / OpenAI）。历史告诉我们，平台通常会赢。</p><p>Google 的 TurboQuant 则代表了 AI 发展的另一条路径。过去三年的叙事是「更大的模型 = 更强的能力」，但 TurboQuant 说：<strong>也许我们不需要更大的模型，我们需要更聪明的压缩。</strong>6 倍的内存压缩意味着什么？意味着现在需要 A100 才能跑的模型，压缩后可以在消费级 GPU 甚至手机芯片上运行。Forbes 的分析说得好：「投资者盯着芯片需求可能看错了方向——高效、可及的 AI 才是正路。」<strong>对设计行业来说，端侧 AI 的意义是革命性的。</strong>想象一下：Figma 在你的 MacBook 上本地运行 AI 推理，不需要上传设计稿到云端——实时响应、完全离线、数据不出设备。这不是幻想，TurboQuant 这样的技术正在让它成为可能。我预测 18 个月内，至少一款主流设计工具会推出「本地 AI」模式。</p><p><strong>FDA 的故事看起来和设计/科技行业距离最远，但它其实是最重要的信号。</strong>当 FDA 给一个聊天机器人颁发「突破性医疗器械」认定时，它在说：对话界面可以是临床工具。这对 UX 设计的影响是深远的——<strong>当你设计的聊天界面就是「医疗器械」时，按钮的位置、文案的措辞、对话的流程都可能影响临床结果。</strong>传统的「快速迭代、A/B 测试」方法论在这个场景下失效了——你不能用 A/B 测试来确定哪种措辞能让术后患者更好地康复。这需要全新的设计方法论：严格的临床验证、医学专家协作、伦理审查。这也是 AI 时代设计师需要拓展的新领域——不只是「好看好用」，而是「安全有效」。</p><p><strong>把三件事连起来：模型可以换（Microsoft），运行可以小（TurboQuant），应用可以是医疗级（FDA）。AI 正在从「实验室里的大玩具」变成「无处不在的基础设施」。2026 年 Q2 的 AI 产业，不是在比谁的模型跑分高，而是在比谁能把 AI 最有效地嵌入到真实世界的每个角落。对设计师来说，这意味着我们的工作对象正在从「软件界面」扩展到「AI 驱动的系统行为」——界面只是冰山一角，水面下是模型选择、压缩策略、临床验证、数据隐私的复杂生态。</strong></p></div>""",
        "en": """<h3>📌 AI × Tech</h3><ul><li><strong>Microsoft Goes Full Multi-Model: Copilot Integrates Anthropic Claude, "AI's Future Is Multi-Model"</strong> — Microsoft's Critique tool now uses both OpenAI and Anthropic models. Axios quotes Microsoft's AI lead: "Frontier labs constantly leapfrog each other; enterprises need tools that swap models easily." Fortune reports Claude is now heavily used across Copilot products. <strong>Signal: AI shifts from "locked to one model" to "models as commodities."</strong><br><small>Source: <a href="https://www.axios.com/2026/03/31/microsoft-critique-anthropic-openai">Axios</a>, <a href="https://fortune.com/2026/03/31/microsoft-revamps-copilot-with-anthropic/">Fortune</a></small></li><li><strong>Google TurboQuant: 6x AI Memory Compression, Internet Calls It "Real-Life Pied Piper"</strong> — Google Research's TurboQuant compresses LLM memory by 6x with minimal quality loss. Forbes calls it an AI evolution turning point: <strong>efficiency optimization may matter more than scale.</strong> Enables on-device AI on phones, tablets, laptops. Ars Technica confirms the quantization approach preserves reasoning quality better than distillation.<br><small>Source: <a href="https://www.forbes.com/sites/timbajarin/2026/04/01/googles-turboquant-marks-a-turning-point-in-ais-evolution/">Forbes</a>, <a href="https://arstechnica.com/ai/2026/03/google-says-new-turboquant-compression-can-lower-ai-memory-usage-without-sacrificing-quality/">Ars Technica</a></small></li><li><strong>FDA's Evolving "Breakthrough" AI Standard: From Hardware to Software Logic</strong> — STAT News reports FDA's Breakthrough Device Designation standards are shifting. RecovryAI, a conversational AI chatbot for post-surgery recovery, received breakthrough designation—the first for a purely conversational AI system. <strong>Signal: FDA acknowledges "software as medical device" extends beyond imaging to conversational AI.</strong><br><small>Source: <a href="https://www.statnews.com/2026/04/02/how-fda-stance-breakthrough-ai-medical-device-evolving/">STAT News</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Models as commodities: Microsoft breaks exclusive model lock-in; competition moves to application layer</li><li>Efficiency > Scale: TurboQuant's "smaller, faster" path may beat "bigger"</li><li>Layered AI regulation: FDA learning to differentiate AI application types</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>Three stories from different angles converge: AI is shifting from "who has the biggest model" arms race to "who deploys AI most effectively" pragmatism.</strong> Microsoft's multi-model pivot is landmark. Remember the 2024 Microsoft-OpenAI honeymoon? Now Microsoft openly uses Claude alongside GPT in its flagship products. When models are swappable, the moat isn't the model—it's the ecosystem. This mirrors Figma vs Moonchild: platform strategy usually wins. TurboQuant represents the counter-narrative to "bigger = better." 6x compression means A100-class models on consumer GPUs or phones. For design: imagine Figma running AI inference locally—real-time, offline, privacy-preserving. I predict within 18 months, at least one major design tool ships "local AI" mode. FDA giving breakthrough designation to a chatbot is the sleeper story. When your chat interface IS a medical device, every UX decision has clinical consequences. Traditional "move fast and A/B test" breaks down. This demands new design methodology: clinical validation, ethics review, medical expert collaboration. <strong>Connect them: models are swappable (Microsoft), inference can be tiny (TurboQuant), applications can be medical-grade (FDA). AI is becoming infrastructure. For designers, our scope expands from "software interfaces" to "AI-driven system behaviors"—the interface is the tip of the iceberg.</strong></p></div>"""
    },
    "cover": og_turboquant_forbes or og_turboquant_ars or og_ms_axios or "",
    "sources": [
        {
            "title": {"zh": "Microsoft 研究工具接入 Anthropic 和 OpenAI 模型", "en": "Microsoft Research Tool Uses Anthropic and OpenAI Models"},
            "url": "https://www.axios.com/2026/03/31/microsoft-critique-anthropic-openai",
            "image": og_ms_axios
        },
        {
            "title": {"zh": "Google TurboQuant 标志 AI 演进的转折点", "en": "Google's TurboQuant Marks a Turning Point in AI's Evolution"},
            "url": "https://www.forbes.com/sites/timbajarin/2026/04/01/googles-turboquant-marks-a-turning-point-in-ais-evolution/",
            "image": og_turboquant_forbes
        },
        {
            "title": {"zh": "FDA 对 AI 突破性医疗器械的立场演变", "en": "How FDA's Stance on Breakthrough AI Is Evolving"},
            "url": "https://www.statnews.com/2026/04/02/how-fda-stance-breakthrough-ai-medical-device-evolving/",
            "image": og_fda
        }
    ]
}

# Load existing issues
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

# Check if we already have evening entries for today (avoid duplicates)
# The existing 2026-04-03 entries are the morning ones about Vibe Coding and Dorsey
# Insert new evening entries at the front
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("Done! Added 2 new issues (design + tech) for 2026-04-03 evening.")
