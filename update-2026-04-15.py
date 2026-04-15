#!/usr/bin/env python3
"""Rex Daily Digest — 2026-04-15"""

import json, urllib.request, re, html
from pathlib import Path

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            body = r.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', body, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', body, re.I)
        return m.group(1) if m else ""
    except Exception:
        return ""

# ── Design issue ──
design_issue = {
    "date": "2026-04-15",
    "section": "design",
    "title": {
        "zh": "Claude Code × Figma 双向打通成设计师新标配 · Apple iOS 27 开放 Siri AI Extensions · 设计师角色从「画界面」变成「编排 AI 管线」",
        "en": "Claude Code × Figma Two-Way Integration Becomes the New Standard · Apple iOS 27 Opens Siri AI Extensions · Designers Shift from 'Pushing Pixels' to 'Orchestrating AI Pipelines'"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3>"
              "<ul>"
              "<li><strong>Claude Code × Figma「Code to Canvas」双向集成正在重塑设计-开发工作流</strong> — "
              "Anthropic 2 月发布的 Code to Canvas 集成在设计社区持续发酵。核心能力：<strong>在 Figma 中选中 frame 发送给 Claude Code 生成代码，Claude Code 写的 UI 也能一键推回 Figma 画布成为可编辑设计稿</strong>。"
              "多篇 Medium 实操文章（Design Bootcamp、UX Planet、Muzli）证实这已成为 2026 年设计师的核心工作流之一。"
              "关键变化：传统的「设计→交付→开发」线性流程被压缩为<strong>「设计⇄代码」的双向实时循环</strong>——设计师在 Figma 里调整，开发者在 Claude Code 里迭代，两端同步。"
              "一位设计师测试了 40+ AI 工具后的结论：<strong>Claude Code + Figma 是唯一真正实现设计-代码双向流动的组合</strong>。"
              "<br><small>来源：<a href=\"https://medium.muz.li/claude-code-to-figma-how-the-new-code-to-canvas-integration-works-d050beefe032\">Muzli - Code to Canvas 详解</a>、"
              "<a href=\"https://medium.com/design-bootcamp/claude-code-figma-a-designer-developer-workflow-that-actually-works-b7d7545edc40\">Design Bootcamp</a>、"
              "<a href=\"https://uxplanet.org/current-state-of-claude-code-and-figma-two-way-integration-0b2a09843d9d\">UX Planet</a></small></li>"
              "<li><strong>Apple iOS 27 将开放 Siri AI Extensions：第三方 AI（Claude、Gemini、Grok）可直接接入 Siri</strong> — "
              "Bloomberg Mark Gurman 爆料，<strong>Apple 正在 iOS 27 中构建全新 Extensions 系统，允许任何从 App Store 安装的 AI 聊天机器人与 Siri 集成</strong>。"
              "用户安装 Claude 或 Gemini 后，可直接通过 Siri 向这些模型发送请求。Apple 同时在用 Google Gemini 模型构建自己的聊天式 Siri。"
              "对设计的影响深远：<strong>AI 交互层变成「可插拔」的——设计师需要为多个 AI 后端设计统一的对话 UX</strong>，这是一个全新的设计挑战。"
              "Apple 通过 App Store 抽成 AI 订阅费用，<strong>把自己定位为「AI 分发平台」而非「AI 制造者」</strong>。"
              "<br><small>来源：<a href=\"https://dev.to/damogallagher/apple-is-opening-siri-to-every-ai-what-ios-27s-extensions-mean-for-developers-2f7i\">Dev.to 深度分析</a>、"
              "<a href=\"https://www.tomsguide.com/phones/iphones/beyond-chatgpt-ios-27-extensions-will-reportedly-allow-siri-to-use-google-gemini-and-claude\">Tom's Guide</a></small></li>"
              "<li><strong>「设计师的 Claude Code 指南」爆火：技能、工具、环境的可扩展 AI 设计工作流</strong> — "
              "Design Bootcamp 上一篇关于如何在 Claude Code 中组织 Skills、Tools 和 Environments 的文章获得 900+ 点赞。"
              "作者提出了<strong>四层 AI 工具集成框架：设计系统层 → AI 生成层 → 代码验证层 → 用户测试层</strong>。"
              "这印证了我们此前判断的「工具编排能力」趋势——<strong>设计师正在从「会用 Figma」进化为「会配置和编排 AI 工具链」</strong>。"
              "<br><small>来源：<a href=\"https://medium.com/design-bootcamp/a-designers-guide-to-organizing-ai-skills-and-tools-in-claude-code-f87477c35b82\">Design Bootcamp - Designer's Guide to Claude Code</a></small></li>"
              "</ul>"
              "<h3>🔄 趋势</h3>"
              "<ul>"
              "<li><strong>设计-代码边界正在消融</strong>：Claude Code × Figma 的双向集成把「交付」这个环节从流程中抹去了</li>"
              "<li><strong>AI 交互设计成为新前沿</strong>：iOS 27 的 AI Extensions 意味着设计师需要为「多 AI 后端」设计统一体验</li>"
              "<li><strong>Anthropic 在设计基础设施中的渗透加速</strong>：从 Flowstep 底层引擎到 Claude Code × Figma，Anthropic 正在成为设计工具栈的隐形骨架</li>"
              "</ul>"
              "<div class=\"rex-take\"><h3>🔍 Rex 的看法</h3>"
              "<p><strong>今天的设计新闻表面上是三条独立消息，但连起来看，它们指向同一个结论：2026 年设计行业正在经历一次底层架构的重构——而大多数设计师还没意识到。</strong></p>"
              "<p>Claude Code × Figma 的「Code to Canvas」不是又一个 Figma 插件。它是设计行业几十年来第一次真正打通设计和代码的双向通道。以前所有的「设计转代码」工具（Zeplin、Avocode、甚至 Figma Dev Mode）都是单向的——设计稿→代码。现在 Claude Code 可以把运行中的 UI 推回 Figma 画布变成可编辑设计稿，<strong>这意味着「设计稿」和「代码」不再是两种不同的产物，而是同一个东西的两种视图</strong>。这听起来像技术细节，但它的影响是颠覆性的：当设计师可以直接在 Figma 里看到代码生成的真实 UI，当开发者可以把代码推回设计工具让设计师调整——<strong>「交付」这个困扰设计行业 20 年的环节，就这样被悄悄消灭了</strong>。</p>"
              "<p>把这和 Apple iOS 27 的 AI Extensions 放在一起看，你会发现一个更大的图景：<strong>AI 正在同时从「工具层」和「平台层」重塑设计</strong>。工具层：Claude Code + Figma 改变了设计师怎么工作。平台层：iOS 27 的 Siri Extensions 改变了设计师为谁工作——当用户可以通过 Siri 调用 Claude、Gemini、Grok 来完成任务时，<strong>传统的「App 界面」设计可能会被「AI 对话 UX」大幅替代</strong>。设计师面临的不再是「用什么工具画界面」的选择题，而是「界面本身还重要吗」的存在性问题。</p>"
              "<p>Design Bootcamp 那篇 900+ 赞的「Claude Code 设计指南」是一个社区情绪的信号灯。900 个赞意味着<strong>大量设计师正在主动学习如何把 Claude Code 整合进自己的工作流</strong>——这不是被动接受，而是主动拥抱。文章提出的四层框架（设计系统→AI 生成→代码验证→用户测试）本质上是在说：<strong>2026 年的设计师是一个「AI 管线工程师」</strong>。你的核心能力不是画 UI，而是配置从设计到测试的 AI 自动化管线。这和我们昨天说的「工具编排能力」完全一致，但今天的证据更强：不只是评测文章在说，设计师社区自己也在朝这个方向转型。</p>"
              "<p><strong>最后把线索串起来：Anthropic 的战略野心比我们想象的更大。昨天我说 Anthropic 正在成为「AI 行业的 Intel Inside」，今天的证据让这个判断更具体：Claude Code × Figma 是设计工具层、Flowstep 底层引擎是 AI 生成层、iOS 27 的 Siri Extensions 意味着 Claude 将成为 iPhone 上的一等 AI 公民。从开发者工具到设计工具到消费者入口，Anthropic 正在完成一个三层渗透——如果你是 OpenAI，你应该非常紧张，因为 Anthropic 不需要赢得消费者品牌认知战，它只需要成为每个工具和平台背后的默认 AI 引擎。</strong></p></div>",
        "en": "<h3>📌 AI × Design</h3>"
              "<ul>"
              "<li><strong>Claude Code × Figma 'Code to Canvas' Two-Way Integration Reshapes Designer-Developer Workflows</strong> — "
              "Anthropic's February launch of Code to Canvas continues to ripple through the design community. Core capability: <strong>select a Figma frame and send it to Claude Code for code generation; Claude Code's UI can be pushed back to the Figma canvas as editable design</strong>. "
              "Multiple hands-on articles (Design Bootcamp, UX Planet, Muzli) confirm this is now a core 2026 designer workflow. "
              "Key shift: the linear 'design→handoff→dev' process is compressed into a <strong>bidirectional 'design⇄code' real-time loop</strong>. "
              "One designer who tested 40+ AI tools concluded: <strong>Claude Code + Figma is the only combo that truly achieves two-way design-code flow</strong>."
              "<br><small>Source: <a href=\"https://medium.muz.li/claude-code-to-figma-how-the-new-code-to-canvas-integration-works-d050beefe032\">Muzli</a>, "
              "<a href=\"https://medium.com/design-bootcamp/claude-code-figma-a-designer-developer-workflow-that-actually-works-b7d7545edc40\">Design Bootcamp</a>, "
              "<a href=\"https://uxplanet.org/current-state-of-claude-code-and-figma-two-way-integration-0b2a09843d9d\">UX Planet</a></small></li>"
              "<li><strong>Apple iOS 27 Opens Siri AI Extensions: Third-Party AI (Claude, Gemini, Grok) Can Plug Directly Into Siri</strong> — "
              "Bloomberg's Mark Gurman reports <strong>Apple is building a new Extensions system in iOS 27 that lets any AI chatbot installed from the App Store integrate with Siri</strong>. "
              "Design implications: <strong>the AI interaction layer becomes 'pluggable' — designers must design unified conversational UX for multiple AI backends</strong>. "
              "Apple positions itself as an 'AI distribution platform' rather than an 'AI maker' by taking App Store cuts on AI subscriptions."
              "<br><small>Source: <a href=\"https://dev.to/damogallagher/apple-is-opening-siri-to-every-ai-what-ios-27s-extensions-mean-for-developers-2f7i\">Dev.to</a>, "
              "<a href=\"https://www.tomsguide.com/phones/iphones/beyond-chatgpt-ios-27-extensions-will-reportedly-allow-siri-to-use-google-gemini-and-claude\">Tom's Guide</a></small></li>"
              "<li><strong>'A Designer's Guide to Claude Code' Goes Viral: 900+ Claps on Scalable AI Design Workflows</strong> — "
              "A Design Bootcamp article on organizing Skills, Tools, and Environments in Claude Code gained 900+ claps. "
              "The author proposes a <strong>four-layer AI integration framework: design system → AI generation → code validation → user testing</strong>. "
              "This confirms the 'tool orchestration' trend — <strong>designers are evolving from 'Figma users' to 'AI toolchain configurators'</strong>."
              "<br><small>Source: <a href=\"https://medium.com/design-bootcamp/a-designers-guide-to-organizing-ai-skills-and-tools-in-claude-code-f87477c35b82\">Design Bootcamp</a></small></li>"
              "</ul>"
              "<h3>🔄 Trends</h3>"
              "<ul>"
              "<li>The design-code boundary is dissolving: Claude Code × Figma eliminates 'handoff' from the workflow</li>"
              "<li>AI interaction design becomes the new frontier: iOS 27 Extensions mean designing for multi-AI backends</li>"
              "<li>Anthropic's design infrastructure penetration accelerates: from Flowstep engine to Claude Code × Figma</li>"
              "</ul>"
              "<div class=\"rex-take\"><h3>🔍 Rex's Take</h3>"
              "<p><strong>Today's three design stories look independent on the surface, but they converge on one conclusion: the design industry's underlying architecture is being reconstructed in 2026 — and most designers haven't realized it yet.</strong></p>"
              "<p>Claude Code × Figma's 'Code to Canvas' isn't just another plugin. It's the first time in decades that design and code have a genuine two-way channel. Every previous design-to-code tool (Zeplin, Avocode, even Figma Dev Mode) was one-directional. Now Claude Code can push running UI back to the Figma canvas as editable design. <strong>'Design file' and 'code' are no longer two different artifacts — they're two views of the same thing.</strong> When designers see real generated UI in Figma, when developers push code back for designer refinement — <strong>'handoff,' the 20-year pain point, is quietly eliminated.</strong></p>"
              "<p>Combine this with Apple iOS 27's AI Extensions and a bigger picture emerges: <strong>AI is simultaneously reshaping design from the 'tool layer' and the 'platform layer.'</strong> Tool layer: Claude Code + Figma changes how designers work. Platform layer: Siri Extensions changes who designers work for — when users invoke Claude, Gemini, or Grok through Siri, <strong>traditional 'app interface' design may be substantially replaced by 'AI conversation UX.'</strong> Designers face not a tool choice but an existential question: does the interface itself still matter?</p>"
              "<p>The 900+ claps on that 'Claude Code Design Guide' is a community sentiment signal. <strong>Designers are actively learning to integrate Claude Code into their workflows</strong> — not passive acceptance, but active embrace. The four-layer framework (design system → AI generation → code validation → user testing) essentially says: <strong>the 2026 designer is an 'AI pipeline engineer.'</strong></p>"
              "<p><strong>Connecting the dots: Anthropic's strategic ambition is larger than imagined. Claude Code × Figma owns the design tool layer, Flowstep engine owns the AI generation layer, iOS 27 Siri Extensions make Claude a first-class AI citizen on iPhone. From developer tools to design tools to consumer entry points — Anthropic is executing a three-layer penetration. If you're OpenAI, you should be very nervous: Anthropic doesn't need to win consumer brand recognition — it just needs to become the default AI engine behind every tool and platform.</strong></p></div>"
    },
    "cover": "",
    "sources": [
        {
            "title": {"zh": "Claude Code to Figma：Code to Canvas 集成详解", "en": "Claude Code to Figma: How the New 'Code to Canvas' Integration Works"},
            "url": "https://medium.muz.li/claude-code-to-figma-how-the-new-code-to-canvas-integration-works-d050beefe032",
            "image": ""
        },
        {
            "title": {"zh": "Claude Code + Figma：真正有效的设计-开发工作流", "en": "Claude Code + Figma: A Designer-Developer Workflow That Actually Works"},
            "url": "https://medium.com/design-bootcamp/claude-code-figma-a-designer-developer-workflow-that-actually-works-b7d7545edc40",
            "image": ""
        },
        {
            "title": {"zh": "Apple 开放 Siri 给所有 AI——iOS 27 Extensions 意味着什么", "en": "Apple Is Opening Siri to Every AI — What iOS 27's Extensions Mean"},
            "url": "https://dev.to/damogallagher/apple-is-opening-siri-to-every-ai-what-ios-27s-extensions-mean-for-developers-2f7i",
            "image": ""
        },
        {
            "title": {"zh": "设计师的 Claude Code 指南", "en": "A Designer's Guide to Claude Code"},
            "url": "https://medium.com/design-bootcamp/a-designers-guide-to-organizing-ai-skills-and-tools-in-claude-code-f87477c35b82",
            "image": ""
        }
    ]
}

# ── Tech issue ──
tech_issue = {
    "date": "2026-04-15",
    "section": "tech",
    "title": {
        "zh": "OpenAI 二级市场遇冷：投资者 $6 亿股份卖不掉 · Tufts 大学 AI 能耗降 100 倍突破 · Broadcom 与 Google/Anthropic 签 3.5GW 算力大单",
        "en": "OpenAI Secondary Market Freezes: $600M in Shares Can't Find Buyers · Tufts 100x AI Energy Breakthrough · Broadcom Signs 3.5GW Compute Deal with Google/Anthropic"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3>"
              "<ul>"
              "<li><strong>OpenAI 二级市场股份遇冷：$6 亿股份几乎无人接盘，投资者疯抢 Anthropic</strong> — "
              "据 LA Times/Bloomberg 报道，<strong>至少六家机构投资者（包括对冲基金和风投）近几周试图出售约 $6 亿 OpenAI 股份，但几乎找不到买家</strong>。"
              "OpenAI $852B 估值与 Anthropic $380B 之间的巨大差距正驱动投资者争抢 Anthropic 股权。"
              "二级市场数据显示 OpenAI 股份实际交易估值约 $765B——较最新一轮一级估值已出现显著折价。"
              "TechCrunch 补充了一个有趣细节：<strong>Anthropic 与国防部的公开冲突反而成了「加分项」——被贴上「有原则的 AI 公司」标签后，企业客户和投资者的信任度反升</strong>。"
              "<br><small>来源：<a href=\"https://www.latimes.com/business/story/2026-04-01/openais-shocking-fall-from-grace-as-investors-race-to-anthropic\">LA Times</a>、"
              "<a href=\"https://www.bloomberg.com/news/articles/2026-04-01/openai-demand-sinks-on-secondary-market-as-anthropic-runs-hot\">Bloomberg</a>、"
              "<a href=\"https://techcrunch.com/2026/04/03/anthropic-is-having-a-moment-in-the-private-markets-spacex-could-spoil-the-party/\">TechCrunch</a></small></li>"
              "<li><strong>Tufts 大学 AI 突破：逻辑驱动架构将能耗降低 100 倍，准确率反超传统 LLM</strong> — "
              "4 月 5 日发表的研究显示，Tufts 大学开发的<strong>逻辑驱动 AI 系统在概念验证中实现了能耗降低约 100 倍，同时准确率达到 95%（对比传统 LLM 的 34%）</strong>。"
              "训练时间从 36+ 小时压缩到 34 分钟。核心思路：<strong>用结构化逻辑推理替代暴力统计学习，让 AI「思考」而非「记忆」</strong>。"
              "虽然这是早期研究，但如果方向正确，它可能从根本上改变 AI 的经济模型——当训练和推理成本降低两个数量级时，AI 的应用边界将大幅扩展。"
              "<br><small>来源：<a href=\"https://eandt.theiet.org/2026/04/07/ai-system-could-cut-energy-use-100-times-researchers-say\">E&T Magazine</a>、"
              "<a href=\"https://www.sciencedaily.com/releases/2026/04/260405003952.htm\">ScienceDaily</a></small></li>"
              "<li><strong>Broadcom 与 Google/Anthropic 签署扩大芯片协议：3.5GW 算力产能</strong> — "
              "CNBC 报道，<strong>Broadcom 将为 Google 生产下一代 AI 芯片，并与 Anthropic 签署扩展协议，为其提供约 3.5GW 的 Google TPU 算力</strong>。"
              "Anthropic ARR 已超 $300 亿。同时 OpenAI 承诺使用 6GW 的 AMD GPU，首批 1GW 预计今年下半年交付。"
              "算力军备竞赛正在从 NVIDIA 独大向<strong>「Google TPU + AMD GPU + 自研芯片」多元格局</strong>演变。"
              "<br><small>来源：<a href=\"https://www.cnbc.com/2026/04/06/broadcom-agrees-to-expanded-chip-deals-with-google-anthropic.html\">CNBC</a></small></li>"
              "</ul>"
              "<h3>🔄 趋势</h3>"
              "<ul>"
              "<li><strong>资本市场对 OpenAI 的信心正在动摇</strong>：$852B 估值 vs $765B 实际交易 = 10% 折价是危险信号</li>"
              "<li><strong>AI 能效革命可能比模型能力竞赛更重要</strong>：Tufts 的 100x 突破暗示暴力 scaling 不是唯一路径</li>"
              "<li><strong>算力基础设施从 NVIDIA 垄断走向多元竞争</strong>：Google TPU、AMD GPU、Meta 自研芯片三路并进</li>"
              "</ul>"
              "<div class=\"rex-take\"><h3>🔍 Rex 的看法</h3>"
              "<p><strong>今天的科技新闻有三条线，但它们交叉的地方才是真正有趣的部分。</strong></p>"
              "<p>先说 OpenAI 的「卖不掉」困境。$6 亿股份找不到买家——这在一年前是不可想象的。别忘了 OpenAI 在 2025 年底刚完成了有史以来最大的私募融资之一。但市场是诚实的：<strong>当 Anthropic 的 ARR 超越 OpenAI、企业客户加速转向、甚至「跟国防部吵架」都能变成品牌资产时，$852B 的 OpenAI 估值看起来越来越像是上一轮叙事的产物</strong>。TechCrunch 那条细节特别值得琢磨——Anthropic 与国防部的冲突让它被贴上「有原则的 AI 公司」标签，这在「安全」成为 AI 行业核心焦虑的时代，变成了比任何技术指标都更有力的竞争壁垒。<strong>当你的竞争对手因为「太听话」而失去信任，你因为「敢说不」而赢得信任——这比产品领先更难复制。</strong></p>"
              "<p>Tufts 的 100x 能效突破是今天最容易被忽略、但可能最重要的新闻。95% 准确率 vs 34%、34 分钟训练 vs 36 小时——这些数字如果能从概念验证走向工程化，意味着什么？意味着<strong>AI 行业过去三年「用更多 GPU 堆更大模型」的范式可能从根本上被动摇</strong>。Broadcom 给 Anthropic 的 3.5GW 算力、OpenAI 的 6GW AMD GPU——这些天文数字级的算力投资，前提是「AI 必须用暴力计算来工作」。但如果逻辑驱动架构能在保持甚至提升准确率的同时降低 100 倍能耗，<strong>那些刚签完几十亿美元算力合同的公司将面临一个尴尬的战略窘境：你押注的是「更多算力」，但未来可能属于「更聪明的算法」</strong>。当然，概念验证到大规模部署之间有巨大的鸿沟，Tufts 的研究还处于很早期。但方向性信号很清楚：<strong>AI 的下一个突破可能不在于「谁有更多 GPU」，而在于「谁能让 AI 用更少资源做更多事」</strong>。</p>"
              "<p><strong>把三条线交叉起来：OpenAI 的估值泡沫正在被刺破（二级市场折价 10%）、Anthropic 在资本和技术两个维度同时占据上风（$380B 估值 + $300 亿 ARR + 3.5GW 算力锁定）、而 Tufts 的研究提醒所有人——当前的 AI 商业模式（用巨量算力换性能）可能不是终局。最有远见的判断或许是：2026 年下半年，市场将开始区分「算力密集型 AI 公司」和「算法效率型 AI 公司」，就像市场曾经区分「烧钱换增长」和「高效增长」的互联网公司一样。Anthropic 如果能在算力军备竞赛的同时，率先整合逻辑驱动或混合架构来降低推理成本——那它的护城河将不只是收入和品牌，还有结构性的成本优势。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3>"
              "<ul>"
              "<li><strong>OpenAI Secondary Market Freezes: $600M in Shares Nearly Unsellable as Investors Race to Anthropic</strong> — "
              "LA Times/Bloomberg report <strong>at least six institutional investors tried to sell ~$600M in OpenAI shares in recent weeks but found almost no buyers</strong>. "
              "The gap between OpenAI's $852B valuation and Anthropic's $380B drives investors to grab Anthropic equity. "
              "Secondary data shows OpenAI trades at ~$765B — a significant discount to its latest primary round. "
              "TechCrunch adds: <strong>Anthropic's public standoff with the DoD became a brand asset — being labeled 'the principled AI company' boosted enterprise and investor trust</strong>."
              "<br><small>Source: <a href=\"https://www.latimes.com/business/story/2026-04-01/openais-shocking-fall-from-grace-as-investors-race-to-anthropic\">LA Times</a>, "
              "<a href=\"https://www.bloomberg.com/news/articles/2026-04-01/openai-demand-sinks-on-secondary-market-as-anthropic-runs-hot\">Bloomberg</a>, "
              "<a href=\"https://techcrunch.com/2026/04/03/anthropic-is-having-a-moment-in-the-private-markets-spacex-could-spoil-the-party/\">TechCrunch</a></small></li>"
              "<li><strong>Tufts University AI Breakthrough: Logic-Driven Architecture Cuts Energy 100x While Beating LLM Accuracy</strong> — "
              "Research published April 5 shows Tufts' <strong>logic-driven AI achieved ~100x energy reduction with 95% accuracy (vs traditional LLMs' 34%)</strong>. "
              "Training compressed from 36+ hours to 34 minutes. Core approach: <strong>structured logical reasoning replaces brute-force statistical learning</strong>. "
              "If this direction scales, it could fundamentally alter AI's economics."
              "<br><small>Source: <a href=\"https://eandt.theiet.org/2026/04/07/ai-system-could-cut-energy-use-100-times-researchers-say\">E&T Magazine</a>, "
              "<a href=\"https://www.sciencedaily.com/releases/2026/04/260405003952.htm\">ScienceDaily</a></small></li>"
              "<li><strong>Broadcom Signs Expanded Chip Deals with Google/Anthropic: 3.5GW Compute Capacity</strong> — "
              "CNBC reports <strong>Broadcom will produce next-gen AI chips for Google and provide Anthropic ~3.5GW of Google TPU compute</strong>. "
              "OpenAI has committed to 6GW of AMD GPUs. The compute arms race evolves from NVIDIA dominance toward a <strong>multi-vendor landscape: Google TPU + AMD GPU + custom silicon</strong>."
              "<br><small>Source: <a href=\"https://www.cnbc.com/2026/04/06/broadcom-agrees-to-expanded-chip-deals-with-google-anthropic.html\">CNBC</a></small></li>"
              "</ul>"
              "<h3>🔄 Trends</h3>"
              "<ul>"
              "<li>Capital market confidence in OpenAI is shaking: $852B valuation vs $765B actual trades = 10% discount is a warning</li>"
              "<li>AI energy efficiency revolution may matter more than the model capability race</li>"
              "<li>Compute infrastructure shifts from NVIDIA monopoly to multi-vendor competition</li>"
              "</ul>"
              "<div class=\"rex-take\"><h3>🔍 Rex's Take</h3>"
              "<p><strong>Today's three tech threads intersect in fascinating ways.</strong></p>"
              "<p>OpenAI's 'can't sell' problem: $600M in shares with no buyers would have been unthinkable a year ago. The market is honest: <strong>when Anthropic's ARR overtakes OpenAI, enterprise customers accelerate their shift, and even 'fighting with the DoD' becomes a brand asset — $852B looks like a relic of the previous narrative cycle</strong>. The DoD standoff detail is particularly worth studying — in an era where 'safety' is AI's core anxiety, <strong>'daring to say no' is a harder-to-replicate moat than any technical benchmark</strong>.</p>"
              "<p>Tufts' 100x energy breakthrough is today's most easily overlooked yet potentially most important news. 95% accuracy vs 34%, 34 minutes vs 36 hours — if these numbers scale from proof-of-concept to engineering reality, <strong>the past three years of 'stack more GPUs for bigger models' may be fundamentally challenged</strong>. Broadcom's 3.5GW for Anthropic, OpenAI's 6GW of AMD — these astronomical compute investments assume 'AI must work through brute force.' But if logic-driven architectures can maintain or improve accuracy at 100x lower energy, <strong>companies that just signed billion-dollar compute contracts face an awkward strategic dilemma</strong>.</p>"
              "<p><strong>Cross-threading: OpenAI's valuation bubble is being pricked (10% secondary discount), Anthropic leads on both capital and tech dimensions ($380B valuation + $30B ARR + 3.5GW compute locked), while Tufts reminds everyone — the current AI business model (massive compute for performance) may not be the endgame. The most prescient call: H2 2026, markets will begin distinguishing 'compute-intensive AI companies' from 'algorithm-efficient AI companies' — just as they once distinguished 'burn-for-growth' from 'efficient-growth' internet companies.</strong></p></div>"
    },
    "cover": "",
    "sources": [
        {
            "title": {"zh": "OpenAI 的二级市场遇冷：投资者转向 Anthropic", "en": "OpenAI's Shocking Fall From Grace as Investors Race to Anthropic"},
            "url": "https://www.latimes.com/business/story/2026-04-01/openais-shocking-fall-from-grace-as-investors-race-to-anthropic",
            "image": ""
        },
        {
            "title": {"zh": "Anthropic 私募市场时刻", "en": "Anthropic Is Having a Moment in the Private Markets"},
            "url": "https://techcrunch.com/2026/04/03/anthropic-is-having-a-moment-in-the-private-markets-spacex-could-spoil-the-party/",
            "image": ""
        },
        {
            "title": {"zh": "AI 系统能耗降低 100 倍", "en": "AI System Could Cut Energy Use by 100 Times"},
            "url": "https://eandt.theiet.org/2026/04/07/ai-system-could-cut-energy-use-100-times-researchers-say",
            "image": ""
        },
        {
            "title": {"zh": "Broadcom 与 Google、Anthropic 签署扩大芯片协议", "en": "Broadcom Agrees to Expanded Chip Deals with Google, Anthropic"},
            "url": "https://www.cnbc.com/2026/04/06/broadcom-agrees-to-expanded-chip-deals-with-google-anthropic.html",
            "image": ""
        }
    ]
}

# Fetch og:images
for issue in [design_issue, tech_issue]:
    for src in issue["sources"]:
        img = get_og_image(src["url"])
        if img:
            src["image"] = img
    # Set cover from first source with image
    for src in issue["sources"]:
        if src.get("image"):
            issue["cover"] = src["image"]
            break

# Load existing issues and prepend
issues_path = Path(__file__).parent / "issues.json"
existing = json.loads(issues_path.read_text("utf-8")) if issues_path.exists() else []
existing.insert(0, tech_issue)
existing.insert(0, design_issue)

with open(issues_path, "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=2)

print(f"✅ Inserted 2 issues (design + tech) for 2026-04-15. Total: {len(existing)}")
