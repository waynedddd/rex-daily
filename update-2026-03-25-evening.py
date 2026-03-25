# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest — 2026-03-25 Evening Edition"""

import json
import urllib.request
import re
import html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', data, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data, re.I)
        return html.unescape(m.group(1)) if m else ""
    except Exception:
        return ""

# Fetch og:images
urls = {
    "figma_mcp": "https://abduzeedo.com/figma-ai-agents-now-write-directly-design-canvas",
    "figma_reddit": "https://www.reddit.com/r/FigmaDesign/comments/1s308wy/ai_agents_can_finally_write_to_figma_what_you/",
    "rgd": "https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
    "jff": "https://www.jff.org/newsroom/press-releases/worker-anxiety-over-ai-is-growing-and-employers-arent-preparing-employees-for-whats-next-new-survey-finds/",
    "jensen": "https://www.youtube.com/watch?v=vif8NQcjVf0",
    "samsung": "https://technologymagazine.com/news/samsung-to-invest-us73bn-in-ai-chip-development-in-2026",
    "normal": "https://www.normalcomputing.com/blog/normal-computing-corp",
    "businessinsider": "https://www.businessinsider.com/ai-productivity-gains-jobs-tech-economy-jim-paulsen-2026-3",
}

images = {}
for k, u in urls.items():
    images[k] = get_og_image(u)
    print(f"og:image [{k}]: {images[k][:80] if images[k] else '(none)'}...")

# Design issue
design_cover = images.get("figma_mcp") or "https://abduzeedo.com/sites/default/files/figma-ai-agents-canvas.jpg"

design_issue = {
    "date": "2026-03-25",
    "section": "design",
    "title": {
        "zh": "Figma 开放 MCP 写入权限：AI Agent 直接在画布上设计 · 85% 设计师认为 AI 将决定未来成败 · 设计工具从「人操作软件」到「Agent 操作画布」的范式跃迁",
        "en": "Figma Opens MCP Write Access: AI Agents Design Directly on Canvas · 85% of Designers Say AI Is Essential to Future Success · Design Tools Shift from 'Human Operates Software' to 'Agent Operates Canvas'"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Figma 发布 use_figma MCP 工具：AI Agent 获得画布读写权限</strong> — Figma 本周正式推出 use_figma MCP（Model Context Protocol）工具，让 Claude Code、Cursor、Copilot CLI、Augment 等编程 Agent 直接获得 Figma 设计文件的完整读写权限。Agent 现在可以创建组件、修改布局、同步 Design Token、生成无障碍标注——所有操作都直接发生在 Figma 画布上。配套推出的 Skills 系统（Markdown 格式的指令文件）让团队可以教 Agent 遵循自己的设计规范，社区已发布 9 个预置 Skill，包括 /figma-generate-design、/apply-design-system 和 /sync-figma-token。Reddit 设计社区的反应两极分化：一些人兴奋于「终于不用手动维护设计系统了」，另一些人担忧「Design System 设计师是不是要失业了」。<br><small>来源：<a href=\"https://abduzeedo.com/figma-ai-agents-now-write-directly-design-canvas\">Abduzeedo</a> | <a href=\"https://www.reddit.com/r/FigmaDesign/comments/1s308wy/ai_agents_can_finally_write_to_figma_what_you/\">Reddit r/FigmaDesign</a></small></li><li><strong>Figma 统计：85% 设计师和开发者认为 AI 对未来成功至关重要</strong> — Figma 发布的 2026 设计统计报告揭示了行业现状：85% 的设计师和开发者认为 AI 将对他们的未来成功至关重要；38% 的设计师在发现阶段使用 AI 做用户研究，40% 用于数据分析；35% 的创意机构已将 AI 用于设计和品牌工作。但同时，91% 的开发者和 92% 的设计师认为设计-开发交接流程仍需改善——而这恰恰是 MCP 工具试图解决的核心痛点。<br><small>来源：<a href=\"https://www.figma.com/resource-library/design-statistics/\">Figma Design Statistics 2026</a></small></li><li><strong>RGD 报告：AI 设计工具从「替代」转向「融入」</strong> — 加拿大注册平面设计师协会（RGD）的分析指出，2026 年 AI 设计工具的核心转变是从「替代设计师」的叙事转向「融入现有工作流」：Adobe Firefly 嵌入专业软件的探索阶段，Mixboard 进入 Moodboard 环节，UX Pilot 做可用性预测。工具在变，但设计师的控制权被刻意保留。文章特别强调了伦理考量——AI 工具在训练数据、许可和治理方面差异巨大，设计师有责任审查条款。<br><small>来源：<a href=\"https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026\">RGD</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>从 API 集成到 MCP 协议</strong>：Figma 的 MCP 意味着 AI Agent 不再需要定制插件——它们通过标准协议获得原生级画布操作能力</li><li><strong>Skills 系统 = 设计规范的 AI 化</strong>：用 Markdown 文件教 Agent 遵循品牌规范，本质上是把 Design System 从「人读文档」变成「AI 读指令」</li><li><strong>设计-开发鸿沟正在被 Agent 桥接</strong>：92% 的设计师认为交接需改善，MCP 的解法是让同一个 Agent 同时操作 Figma 和代码</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Figma 的 use_figma MCP 工具不只是一个功能更新——它标志着设计工具行业从「AI 辅助人类」到「AI 独立操作」的关键转折点。</strong></p><p>让我先说清楚这件事为什么重要。在此之前，AI 在设计工具中的角色基本是「建议者」：Figma Make 生成初稿供你修改，Firefly 生成素材供你选择，UX Pilot 给你可用性建议供你采纳。人类始终是操作者，AI 是助手。但 use_figma MCP 改变了这个关系——<strong>AI Agent 现在是操作者。</strong>它不是给你建议，它直接在画布上创建组件、调整布局、同步 Token。Claude Code 可以读取你的设计文件，理解你的组件库，然后按照 Skill 文件中定义的品牌规范生成新界面。这不是「AI 辅助设计」，这是「AI 执行设计」。</p><p>更深层的变化在于 Skills 系统。Figma 没有把 Agent 的能力锁在自己的产品逻辑里——它用 Markdown 文件让团队自定义 Agent 的行为。这意味着什么？你的 Design System 不再只是一份给人类看的文档——它变成了一份给 AI 执行的指令集。社区发布的 /apply-design-system Skill 就是最好的例子：Agent 读取你的 Design System 文档，然后在画布上严格按规范生成组件。<strong>Abduzeedo 说得很精准：「一个读过你所有组件文档的新设计师」——只不过这个「设计师」不会忘记规范、不会犯低级错误、不需要 onboarding。</strong></p><p>把这条新闻和昨天讨论的 Anthropic Computer Use 放在一起看，一个清晰的分层正在形成。Computer Use 是「通用操作层」——Claude 像人一样点击鼠标操作任何软件，包括没有 API 的旧工具。MCP 是「原生协议层」——Agent 通过标准接口获得深度操作能力，速度更快、精度更高、不需要「看屏幕」。两者互补：MCP 覆盖支持它的现代工具（Figma、VS Code），Computer Use 覆盖一切旧软件。<strong>设计工具的未来不是「一个超级 AI 设计产品」，而是「一个 Agent 通过不同协议操作所有设计工具」。</strong></p><p>Reddit 上「Design System 设计师是不是要失业了」的担忧值得认真对待。短期答案是：不会，因为 Agent 需要人类定义规范（写 Skill 文件）、审核输出、做创意决策。但中长期看，「维护 Design System」这个职能确实在被压缩——Agent 可以自动检测不一致、自动修复偏差、自动生成新组件。Figma 的统计数据说 85% 的设计师认为 AI 对未来成功至关重要，但 RGD 的报告也强调了控制权的保留。我的判断是：<strong>2026 年下半年，「能写好 Skill 文件、能定义 Agent 工作流的设计师」将成为新的稀缺人才——不是会不会用 AI，而是会不会「管理」AI。</strong></p><p>最后一个值得注意的信号：Figma 的 MCP 工具支持 Claude Code、Cursor、Copilot CLI 等多个 Agent，而不是绑定单一 AI 供应商。这和 Anthropic Computer Use 的「通用操作」哲学一脉相承——<strong>设计工具平台正在从「集成特定 AI」转向「开放给所有 AI Agent」</strong>。对设计师来说，这意味着你的竞争力不在于「用哪个 AI」，而在于「怎么用 AI」。</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Figma Launches use_figma MCP Tool: AI Agents Get Full Canvas Read/Write Access</strong> — Figma's new MCP (Model Context Protocol) tool gives coding agents like Claude Code, Cursor, and Copilot CLI direct read/write access to Figma design files. Agents can create components, modify layouts, sync design tokens, and generate accessibility annotations directly on the canvas. A companion Skills system (Markdown instruction files) lets teams teach agents to follow their design specifications.<br><small>Source: <a href=\"https://abduzeedo.com/figma-ai-agents-now-write-directly-design-canvas\">Abduzeedo</a> | <a href=\"https://www.reddit.com/r/FigmaDesign/comments/1s308wy/ai_agents_can_finally_write_to_figma_what_you/\">Reddit</a></small></li><li><strong>85% of Designers Say AI Is Essential to Future Success</strong> — Figma's 2026 design statistics report: 85% of designers/developers see AI as essential; 38% use AI for user research in discovery; 92% say design-dev handoff still needs improvement — exactly what MCP aims to solve.<br><small>Source: <a href=\"https://www.figma.com/resource-library/design-statistics/\">Figma</a></small></li><li><strong>RGD Report: AI Design Tools Shift from Replacement to Integration</strong> — Canadian designers' association notes 2026's key shift: AI tools are embedding into existing workflows (Firefly in exploration, Mixboard in moodboarding, UX Pilot in validation) rather than replacing designers. Ethical considerations around training data and licensing emphasized.<br><small>Source: <a href=\"https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026\">RGD</a></small></li></ul><h3>🔄 Trends</h3><ul><li>From API plugins to MCP protocol: agents gain native canvas operations via standard interface</li><li>Skills system = AI-readable design systems: Markdown files turn brand specs into agent instructions</li><li>Design-dev gap being bridged by agents that operate both Figma and code</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Figma's use_figma MCP tool marks the pivot from 'AI assists humans' to 'AI operates independently.'</strong> Agents now create components, sync tokens, and modify layouts directly on canvas — not suggesting, but executing. The Skills system turns design systems from human-readable docs into AI-executable instructions. Combined with yesterday's Anthropic Computer Use, a clear two-layer architecture emerges: MCP for modern tools (fast, precise), Computer Use for everything else. <strong>The future isn't one AI design product — it's one agent operating all design tools through different protocols. The new scarce talent? Designers who can write Skill files and manage AI workflows.</strong></p></div>"
    },
    "cover": design_cover,
    "sources": [
        {
            "title": {"zh": "Abduzeedo: Figma AI Agent 直接在设计画布上写入", "en": "Abduzeedo: Figma AI Agents Now Write Directly to the Design Canvas"},
            "url": "https://abduzeedo.com/figma-ai-agents-now-write-directly-design-canvas",
            "image": images.get("figma_mcp", "")
        },
        {
            "title": {"zh": "Reddit: AI Agent 终于可以写入 Figma 了", "en": "Reddit: AI Agents Can Finally Write to Figma"},
            "url": "https://www.reddit.com/r/FigmaDesign/comments/1s308wy/ai_agents_can_finally_write_to_figma_what_you/",
            "image": images.get("figma_reddit", "")
        },
        {
            "title": {"zh": "Figma: 2026 年设计统计数据（79+ 项）", "en": "Figma: 79+ Design Statistics for 2026"},
            "url": "https://www.figma.com/resource-library/design-statistics/",
            "image": ""
        },
        {
            "title": {"zh": "RGD: 2026 年 AI 工具如何放大设计创造力", "en": "RGD: Amplifying Creativity with AI Tools for Designers in 2026"},
            "url": "https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
            "image": images.get("rgd", "")
        }
    ]
}

# Tech issue
tech_cover = images.get("jensen") or images.get("samsung") or ""

tech_issue = {
    "date": "2026-03-25",
    "section": "tech",
    "title": {
        "zh": "全球 31% 劳动者对 AI 感到恐惧：ADP 38000 人调查揭示情绪逆转 · Jensen Huang × Lex Fridman：NVIDIA 4 万亿、AI 扩展定律与太空数据中心 · Samsung 730 亿美元豪赌 AI 芯片 · AI 生产力悖论：华尔街老将质疑「效率叙事」",
        "en": "31% of Global Workers Scared of AI: ADP 38K Survey Reveals Sentiment Reversal · Jensen Huang × Lex Fridman: NVIDIA $4T, AI Scaling Laws & Data Centers in Space · Samsung's $73B AI Chip Bet · AI Productivity Paradox: Wall Street Veteran Questions the Efficiency Narrative"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>ADP 调查：31% 全球劳动者对 AI「感到恐惧」，情绪从乐观转向悲观</strong> — ADP Research 对全球 38,000 名劳动者的调查显示，约 31% 的受访者报告对 AI 感到「害怕、焦虑或不安全」。JFF（Jobs for the Future）3 月 11 日发布的配套调查更加直白：一年前劳动者对 AI 持净正面态度，现在翻转为净负面——更多人认为 AI 在求职、积累财富和生活质量方面弊大于利。56% 的受访者表示雇主从未就 AI 工具的使用征询过他们的意见；认为自己有足够培训和资源使用 AI 的比例从 45% 骤降至 36%。CNBC 的报道则揭示了一个反直觉的现象：<strong>高收入者比低收入者更担心 AI 对就业的威胁</strong>——金融、信息和商业服务领域的人员流动率显著下降，表明人们正在「抓紧」现有职位。<br><small>来源：<a href=\"https://www.jff.org/newsroom/press-releases/worker-anxiety-over-ai-is-growing-and-employers-arent-preparing-employees-for-whats-next-new-survey-finds/\">JFF</a> | <a href=\"https://www.cnbc.com/2026/02/25/top-earners-are-more-afraid-for-their-employment-than-lower-income-as-ai-threat-increases.html\">CNBC</a></small></li><li><strong>Jensen Huang × Lex Fridman 长访谈：NVIDIA 4 万亿、AI 扩展定律、太空数据中心</strong> — NVIDIA CEO Jensen Huang 在 Lex Fridman Podcast #494 中进行了 2.5 小时深度对话。核心要点：NVIDIA 市值 4 万亿美元的底层逻辑；AI 扩展定律（Scaling Laws）的现状和最大阻碍；NVIDIA 的护城河（不仅是芯片，是整个 CUDA 生态）；以及一个惊人的讨论——太空数据中心的可行性。Huang 还回应了「NVIDIA 是否会值 10 万亿美元」的问题。这次访谈是理解 AI 基础设施投资逻辑的必看内容。<br><small>来源：<a href=\"https://www.youtube.com/watch?v=vif8NQcjVf0\">Lex Fridman Podcast #494</a></small></li><li><strong>Samsung 宣布 730 亿美元 AI 芯片投资，剑指 SK Hynix 和 NVIDIA 供应链</strong> — Samsung 在 3 月 18 日的年度股东大会上宣布，2026 年将投入超过 110 万亿韩元（约 730 亿美元）用于芯片产能扩张和研发——创历史纪录。核心目标：从 SK Hynix 手中夺回 AI 高带宽内存（HBM）的领导地位。Samsung 已与 AMD 签署 HBM4 供应协议，副董事长兼 CEO 全英贤（Jun Young-hyun）指出 Agentic AI 的崛起正在推动内存和服务器级存储的「爆发式订单增长」。<br><small>来源：<a href=\"https://technologymagazine.com/news/samsung-to-invest-us73bn-in-ai-chip-development-in-2026\">Technology Magazine</a></small></li><li><strong>AI 生产力悖论：华尔街老将质疑「效率叙事」</strong> — Business Insider 报道，资深投资策略师 Jim Paulsen 对 AI 推动生产力增长的主流叙事提出质疑。他指出，科技巨头近期大量裁员并引用「AI 带来的效率提升」作为理由——但这些公司的实际生产力数据并未显示出与投入相称的增长。OpenAI 同期宣布计划在年底前将员工从 4,500 人增加到 8,000 人（Reuters 3/21 报道），形成了一个有趣的对比：<strong>AI 公司自己在疯狂招人，却告诉其他行业 AI 可以减少人力需求。</strong><br><small>来源：<a href=\"https://www.businessinsider.com/ai-productivity-gains-jobs-tech-economy-jim-paulsen-2026-3\">Business Insider</a> | <a href=\"https://www.reuters.com/business/openai-nearly-double-workforce-8000-by-end-2026-ft-reports-2026-03-21/\">Reuters</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>劳动者情绪逆转</strong>：从 2025 年的谨慎乐观到 2026 年的净负面——AI 焦虑不再是少数人的问题</li><li><strong>AI 基础设施军备赛加剧</strong>：Samsung 730 亿 vs NVIDIA 生态 vs 新创芯片（Normal Computing 的热力学计算）</li><li><strong>「AI 提升效率」叙事遭遇现实检验</strong>：科技公司裁员归因 AI，但自己却在扩招</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天这四条新闻拼在一起，构成了 2026 年 AI 产业最核心的悖论图景：基础设施在狂奔，生产力叙事在动摇，劳动者在恐惧，而资本在加倍下注。</strong></p><p>先从 ADP/JFF 的调查说起。31% 的全球劳动者「害怕」AI——这个数字本身不算惊人，惊人的是趋势方向：一年前净正面，现在净负面。更关键的是 56% 的人说雇主从未征询过他们的意见。这揭示了一个管理层面的系统性失败：<strong>企业在部署 AI 时把员工当成需要被「效率化」的对象，而不是需要被赋能的伙伴。</strong>CNBC 报道的「高收入者更恐惧」现象也很值得玩味——金融和商业服务的人员流动率下降，意味着人们不敢跳槽、不敢冒险，因为他们知道自己的岗位可能是下一个被 AI 优化掉的。这不是健康的劳动市场。</p><p>然后是 Jensen Huang 在 Lex Fridman 播客上的 2.5 小时长谈。这次访谈的核心信息是：<strong>NVIDIA 的护城河不是芯片——是 CUDA 生态系统。</strong>全世界几乎所有 AI 模型都建立在 CUDA 上，这种软件锁定比任何硬件优势都更持久。Huang 讨论「太空数据中心」不是在开玩笑——当 AI 训练的能耗需求持续指数增长，地球上的能源供给和散热能力确实可能成为瓶颈。Samsung 730 亿美元的投入正是在这个背景下：AI 计算需求正在以超越摩尔定律的速度增长，HBM 内存成为了新的卡脖子环节。</p><p>但最讽刺的是 Jim Paulsen 的观察。科技巨头们一边裁员一边说「AI 让我们更高效了」，一边又在疯狂扩招 AI 人才。OpenAI 要在年底前从 4,500 扩到 8,000 人——几乎翻倍。如果 AI 真的如宣传的那样能大幅提升效率，为什么制造 AI 的公司自己需要这么多人？答案其实很简单：<strong>AI 目前的主要经济效应不是「提升效率」——而是「重新分配劳动」。</strong>不是做事的人变少了，而是做不同事的人变了。传统岗位在被压缩，AI 相关岗位在爆发，中间的转型成本由普通劳动者承担。</p><p>把这四条新闻和昨天的设计板块（Figma MCP、Anthropic Computer Use）联系起来看，一个更完整的图景浮现了。在「AI 直接操作工具」的时代，劳动者的恐惧不是没有道理的——当 AI Agent 可以直接在 Figma 上设计、在代码编辑器里编程、在任何桌面应用上操作时，「执行层」的人力需求确实在萎缩。但同时，定义「做什么」和「怎么做」的策略层需求在增加。<strong>Samsung 赌 730 亿美元在硬件上，NVIDIA 赌 CUDA 生态在平台上，而普通劳动者需要赌的，是从「执行者」转型为「编排者」的速度。</strong>ADP 调查中 36% 的「有足够 AI 培训」比例告诉我们：大多数人还没准备好。</p><p>Palantir CEO Alex Karp 上周说的话虽然刻薄但值得思考：在 AI 时代只有两种人会成功——「做手艺活的」和「神经不典型的」。翻译成设计领域的语言：<strong>会动手做出好设计的匠人，和能看到别人看不到的 pattern 的策略师——这两种人 AI 短期内替代不了。中间那一大片「按流程执行」的角色，压力最大。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>ADP Survey: 31% of Global Workers 'Scared' of AI, Sentiment Flips Negative</strong> — ADP Research surveyed 38,000 workers globally; ~31% report fear/anxiety/insecurity about AI. JFF's companion survey shows net-positive AI sentiment from 2025 has flipped to net-negative. 56% say employers never consulted them about AI deployment. High earners more anxious than lower-income workers.<br><small>Source: <a href=\"https://www.jff.org/newsroom/press-releases/worker-anxiety-over-ai-is-growing-and-employers-arent-preparing-employees-for-whats-next-new-survey-finds/\">JFF</a> | <a href=\"https://www.cnbc.com/2026/02/25/top-earners-are-more-afraid-for-their-employment-than-lower-income-as-ai-threat-increases.html\">CNBC</a></small></li><li><strong>Jensen Huang × Lex Fridman: NVIDIA $4T, Scaling Laws, Data Centers in Space</strong> — 2.5-hour deep dive covering NVIDIA's moat (CUDA ecosystem, not just chips), AI scaling law bottlenecks, and the feasibility of space-based data centers for AI training.<br><small>Source: <a href=\"https://www.youtube.com/watch?v=vif8NQcjVf0\">Lex Fridman Podcast #494</a></small></li><li><strong>Samsung Announces Record $73B AI Chip Investment</strong> — Targeting SK Hynix's HBM leadership with massive capex. New HBM4 deal with AMD. CEO cites agentic AI as driving explosive memory demand.<br><small>Source: <a href=\"https://technologymagazine.com/news/samsung-to-invest-us73bn-in-ai-chip-development-in-2026\">Technology Magazine</a></small></li><li><strong>AI Productivity Paradox: Wall Street Veteran Questions Efficiency Narrative</strong> — Jim Paulsen notes tech giants cite AI productivity gains while laying off workers, yet OpenAI plans to nearly double headcount to 8,000. The question: if AI boosts efficiency so much, why do AI companies need more humans?<br><small>Source: <a href=\"https://www.businessinsider.com/ai-productivity-gains-jobs-tech-economy-jim-paulsen-2026-3\">Business Insider</a> | <a href=\"https://www.reuters.com/business/openai-nearly-double-workforce-8000-by-end-2026-ft-reports-2026-03-21/\">Reuters</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Worker sentiment reversal: cautious optimism → net negative on AI's impact</li><li>AI infrastructure arms race intensifies: Samsung $73B vs NVIDIA CUDA moat vs next-gen chips</li><li>'AI boosts efficiency' narrative meets reality: tech companies lay off citing AI, then hire more AI talent</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>These four stories form 2026's central AI paradox: infrastructure sprints ahead, productivity narrative wobbles, workers fear, capital doubles down.</strong> The ADP/JFF sentiment flip is significant — not the number but the direction. 56% of workers say employers never consulted them about AI; only 36% feel adequately trained. Meanwhile Jensen Huang explains NVIDIA's real moat is CUDA's software lock-in, Samsung bets $73B on HBM, and Jim Paulsen points out the elephant: AI companies themselves are hiring furiously while telling everyone else AI reduces headcount. <strong>AI's primary economic effect in 2026 isn't 'efficiency gains' — it's labor redistribution. The transition cost falls on workers who weren't consulted and weren't trained.</strong></p></div>"
    },
    "cover": tech_cover,
    "sources": [
        {
            "title": {"zh": "JFF: 劳动者对 AI 的焦虑正在增长", "en": "JFF: Worker Anxiety Over AI Is Growing"},
            "url": "https://www.jff.org/newsroom/press-releases/worker-anxiety-over-ai-is-growing-and-employers-arent-preparing-employees-for-whats-next-new-survey-finds/",
            "image": images.get("jff", "")
        },
        {
            "title": {"zh": "Lex Fridman Podcast #494: Jensen Huang 谈 NVIDIA 与 AI 革命", "en": "Lex Fridman Podcast #494: Jensen Huang on NVIDIA and the AI Revolution"},
            "url": "https://www.youtube.com/watch?v=vif8NQcjVf0",
            "image": images.get("jensen", "")
        },
        {
            "title": {"zh": "Technology Magazine: Samsung 730 亿美元 AI 芯片投资", "en": "Technology Magazine: Samsung to Invest $73B in AI Chip Development"},
            "url": "https://technologymagazine.com/news/samsung-to-invest-us73bn-in-ai-chip-development-in-2026",
            "image": images.get("samsung", "")
        },
        {
            "title": {"zh": "Business Insider: 华尔街老将质疑 AI 生产力叙事", "en": "Business Insider: Wall Street Veteran Questions AI Productivity Myth"},
            "url": "https://www.businessinsider.com/ai-productivity-gains-jobs-tech-economy-jim-paulsen-2026-3",
            "image": images.get("businessinsider", "")
        },
        {
            "title": {"zh": "Reuters: OpenAI 计划年底前将员工翻倍至 8000 人", "en": "Reuters: OpenAI to Nearly Double Workforce to 8,000 by End-2026"},
            "url": "https://www.reuters.com/business/openai-nearly-double-workforce-8000-by-end-2026-ft-reports-2026-03-21/",
            "image": ""
        }
    ]
}

# Load existing issues.json and prepend
with open("issues.json", "r", encoding="utf-8") as f:
    issues = json.load(f)

# Remove today's evening duplicates if re-running (keep morning entries)
# We identify evening entries by checking if title contains our specific keywords
new_design_title_fragment = "Figma 开放 MCP"
new_tech_title_fragment = "31% 劳动者"
issues = [i for i in issues if not (i.get("date") == "2026-03-25" and (
    new_design_title_fragment in i.get("title", {}).get("zh", "") or
    new_tech_title_fragment in i.get("title", {}).get("zh", "")
))]

# Prepend new issues (design first, then tech)
issues = [design_issue, tech_issue] + issues

with open("issues.json", "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! issues.json now has {len(issues)} entries.")
print(f"Design cover: {design_cover[:80]}...")
print(f"Tech cover: {tech_cover[:80]}...")
