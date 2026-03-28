# -*- coding: utf-8 -*-
"""Rex Daily Update - 2026-03-28 Evening"""
import json, urllib.request, re

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

urls = {
    "figma_mcp_medium": "https://medium.com/@Rythmuxdesigner/figma-mcp-code-connect-the-complete-guide-to-ai-powered-design-to-code-workflows-5c759a6027f8",
    "figma_mcp_builder": "https://www.builder.io/blog/figma-mcp-server",
    "figma_releasebot": "https://releasebot.io/updates/figma",
    "rgd_ai_design": "https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
    "muzli_vibe": "https://muz.li/blog/best-ai-design-tools-for-ui-ux-designers-in-2026/",
    "softbank_bridge": "https://group.softbank/en/news/press/20260327",
    "softbank_kandou": "https://www.ad-hoc-news.de/boerse/news/ueberblick/softbank-s-strategic-bet-on-ai-infrastructure-amid-financial-scrutiny/68971205",
    "openai_sbenergy": "https://www.mobileworldlive.com/ai-cloud/openai-softbank-team-on-1b-investment-in-sb-energy/",
    "aifunding": "https://aifundingtracker.com/top-50-ai-startups/",
}

print("Fetching og:images...")
images = {}
for key, url in urls.items():
    img = get_og_image(url)
    images[key] = img
    print(f"  {key}: {img[:80] if img else '(none)'}")

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

design_issue = {
    "date": "2026-03-28",
    "section": "design",
    "title": {
        "zh": "Figma MCP 打通设计与代码的「神经链路」· AI 设计工具从替代走向增强 · 设计师的新核心竞争力：判断力而非执行力",
        "en": "Figma MCP Creates 'Neural Link' Between Design and Code · AI Design Tools Shift from Replacement to Augmentation · Designer's New Edge: Judgment Over Execution"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计（晚间版）</h3><ul><li><strong>Figma MCP 开放测试：设计与代码之间的「神经链路」正式打通</strong> — Figma 在 3 月下旬推出的 MCP（Model Context Protocol）服务器进入开放测试阶段，这是设计行业的一个里程碑时刻。AI 代理现在可以直接读取 Figma 设计文件的语义结构、基于你的真实组件库生成代码、甚至将渲染好的 UI 推回 Figma 画布作为可编辑帧。这不是又一个「设计转代码」的导出工具——<strong>这是一个双向协议，让 Cursor、VS Code Copilot、Claude Code 等 AI 编码工具与 Figma 形成真正的「神经链路」。</strong>设计师在 Figma 中改一个按钮，AI 代码端同步更新；开发者用 AI 生成的 UI 直接推回设计稿审查。<strong>设计交付（Design Handoff）这个概念，可能要被彻底淘汰了。</strong><br><small>来源：<a href=\"https://releasebot.io/updates/figma\">Figma Release Notes</a> | <a href=\"https://www.builder.io/blog/figma-mcp-server\">Builder.io</a> | <a href=\"https://medium.com/@Rythmuxdesigner/figma-mcp-code-connect-the-complete-guide-to-ai-powered-design-to-code-workflows-5c759a6027f8\">Medium</a></small></li><li><strong>AI 设计工具的「增强 vs 替代」分水岭</strong> — 加拿大注册平面设计师协会（RGD）发布了一份深度分析，标题耐人寻味：「用 AI 工具增强创造力」。文章指出，2026 年的 AI 设计工具正在经历一次关键转向——从「替代设计师」的叙事转向「嵌入式增强」。Adobe Firefly 被用于早期视觉探索而非最终输出；Mixboard 进入了 moodboard 阶段；Figma Make 成为工作流的一部分而非全部。<strong>这些工具的共同特征是：它们被设计来「融入」现有工作流，而不是「取代」它。</strong>RGD 同时提醒设计师审查每个 AI 工具的训练数据、授权条款和隐私政策——AI 伦理正在从「可选项」变成「必修课」。<br><small>来源：<a href=\"https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026\">RGD</a> | <a href=\"https://muz.li/blog/best-ai-design-tools-for-ui-ux-designers-in-2026/\">Muzli</a></small></li><li><strong>2026 设计工具生态：判断力成为新的核心竞争力</strong> — Medium 上设计师 Punit Chawla 的文章引发行业共鸣：「我测试了 40+ AI 设计工具后发现，这些工具正在把设计工作从「制作屏幕」变成「更快做出决策」。」Aura Build 用自然语言生成落地页，Figma Make 用提示词生成 UI 组件——当执行层被 AI 压缩到接近零成本时，<strong>设计师的价值不再是「能不能做出来」，而是「知不知道该做什么」。</strong>这与早间报道的创造力研究形成呼应：AI 消灭的不是设计这个职业，而是「只会执行」这个工种。<br><small>来源：<a href=\"https://medium.com/design-bootcamp/5-new-ai-design-tools-to-try-in-2026-bba38068b142\">Medium Design Bootcamp</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>MCP 协议 = 设计开发协作的新基础设施</strong>：双向读写取代单向导出，设计交付正在被重新定义</li><li><strong>AI 设计工具的「增强范式」胜出</strong>：嵌入式 > 替代式，融入工作流 > 取代工作流</li><li><strong>设计师竞争力迁移</strong>：从工具技能（Figma/Sketch）到判断能力（用户洞察/审美/业务理解）</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Figma MCP 的推出，标志着设计行业一个持续了 20 年的痛点——「设计交付」——正式进入死亡倒计时。</strong></p><p>让我先解释为什么 MCP 比你想的更重要。过去，设计到代码的工作流本质上是一条单行道：设计师在 Figma 画完，用 Zeplin 或 Inspect 导出标注，开发者照着标注写代码，写完后两边对照像素差异，发现不对再改——这个循环每一轮都在烧时间和耐心。MCP 把这条单行道变成了双车道高速公路。AI 代理不只是「看」设计稿然后猜着写代码——它理解你的设计系统（通过 Code Connect），知道 <code>Button/Primary</code> 对应的不是一段随机 CSS，而是你团队实际维护的 React 组件。反过来，开发者用 AI 生成的 UI 可以直接推回 Figma 画布成为可编辑帧——设计师可以在 Figma 里直接审查、修改 AI 生成的界面。</p><p>这意味着什么？<strong>「设计交付」这个环节——连同它衍生出的所有工具（Zeplin、Abstract、InVision Inspect）和所有流程（标注、走查、视觉还原度检查）——正在被协议层的创新直接消解。</strong>当 AI 可以双向读写设计和代码时，你不需要「交付」任何东西，因为设计和代码已经是同一个东西的两个视图。</p><p>但更深层的变化是对设计师角色的重塑。RGD 的分析和 Punit Chawla 的文章都指向同一个结论：<strong>2026 年的 AI 设计工具不是在替代设计师，而是在重新定义「设计师」这个词的含义。</strong>当 Figma Make 可以从一句话生成完整的 UI 组件，当 Aura Build 可以从对话生成落地页，「会用 Figma」不再是一个有意义的技能——就像「会用 Word」不是一个有意义的写作技能一样。</p><p>那什么是有意义的？三件事：<strong>第一是判断力</strong>——AI 给你 10 个方案，你能在 3 秒内判断哪个对、为什么对、怎么改更好。这种判断来自对用户的深度理解，不是来自 Figma 教程。<strong>第二是品味</strong>——当所有人都能用 AI 生成「还行」的设计时，真正区分好设计和伟大设计的不是工具，而是使用者的审美标准。品味不是天赋，它是大量优秀作品的内化。<strong>第三是系统思维</strong>——MCP 让设计和代码成为一体，这意味着理解组件架构、设计系统、前端性能约束的设计师会比只懂视觉的设计师有压倒性优势。</p><p>把今天的晚间消息和早间的创造力研究结合来看，一个清晰的画面浮现：<strong>AI 正在同时拆解和重组设计这个职业。</strong>拆解的是执行层——标注、像素推移、基础 UI 搭建这些「手工活」正在被 MCP 和 AI 生成工具消解。重组的是价值层——设计师的核心价值正在从「做出来」迁移到「想清楚」和「判断对」。RGD 提到的 AI 伦理审查也是这个重组的一部分：当 AI 可以大规模生成设计资产时，谁来判断这些资产的训练数据是否合规、输出是否符合品牌调性、是否侵犯了某人的视觉风格——这些判断需要的不是技术能力，而是职业素养和行业知识。</p><p>对 Wayne 关心的「AI × 设计」主题来说，Figma MCP 可能是 2026 年最值得关注的单一事件。它不只是一个功能更新——<strong>它是设计工具从「画板」进化为「协议」的标志。</strong>当设计变成一种可以被 AI 读写的协议时，设计的定义本身就在改变。</p></div>",
        "en": "<h3>📌 AI × Design (Evening)</h3><ul><li><strong>Figma MCP Open Beta: The 'Neural Link' Between Design and Code</strong> — Figma's MCP (Model Context Protocol) server entered open beta in late March, marking a milestone for the design industry. AI agents can now read Figma's semantic design structure, generate code using real component libraries, and push rendered UI back to Figma as editable frames. This is a bidirectional protocol connecting Cursor, VS Code Copilot, and Claude Code directly with Figma. <strong>Design Handoff as a concept may be officially dead.</strong><br><small>Source: <a href=\"https://releasebot.io/updates/figma\">Figma Release Notes</a> | <a href=\"https://www.builder.io/blog/figma-mcp-server\">Builder.io</a> | <a href=\"https://medium.com/@Rythmuxdesigner/figma-mcp-code-connect-the-complete-guide-to-ai-powered-design-to-code-workflows-5c759a6027f8\">Medium</a></small></li><li><strong>AI Design Tools: The Augmentation Paradigm Wins</strong> — RGD's analysis shows 2026 AI design tools are shifting from 'replacing designers' to 'embedded augmentation.' Adobe Firefly for early exploration, Mixboard for moodboarding, Figma Make as workflow component — all designed to integrate into existing workflows, not replace them. RGD also urges designers to review training data and licensing of each AI tool.<br><small>Source: <a href=\"https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026\">RGD</a> | <a href=\"https://muz.li/blog/best-ai-design-tools-for-ui-ux-designers-in-2026/\">Muzli</a></small></li><li><strong>2026 Design Ecosystem: Judgment as the New Core Competency</strong> — Designer Punit Chawla's viral post: 'After testing 40+ AI design tools, these tools are shifting design from making screens to making decisions faster.' When execution approaches zero cost, the designer's value shifts from 'can you build it' to 'do you know what to build.'<br><small>Source: <a href=\"https://medium.com/design-bootcamp/5-new-ai-design-tools-to-try-in-2026-bba38068b142\">Medium Design Bootcamp</a></small></li></ul><h3>🔄 Trends</h3><ul><li>MCP protocol = new infrastructure for design-dev collaboration: bidirectional read/write replaces one-way export</li><li>AI design tools: augmentation paradigm wins over replacement paradigm</li><li>Designer competency migration: from tool skills to judgment, taste, and systems thinking</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Figma MCP marks the beginning of the end for 'Design Handoff' — a 20-year-old pain point finally entering its death countdown.</strong> MCP turns the one-way design-to-code street into a bidirectional highway. AI agents don't just 'look' at designs and guess code — they understand your design system via Code Connect, knowing that <code>Button/Primary</code> maps to your team's actual React component. Developers can push AI-generated UI back to Figma as editable frames. This dissolves the entire handoff ecosystem — Zeplin, Abstract, pixel-perfect audits — at the protocol level. The deeper shift: when Figma Make generates UI from prompts and Aura Build creates landing pages from conversation, 'knowing Figma' stops being a meaningful skill. What matters now: <strong>judgment</strong> (picking the right solution from 10 AI options in 3 seconds), <strong>taste</strong> (the aesthetic standard that separates good from great), and <strong>systems thinking</strong> (understanding component architecture and design systems). AI is simultaneously dismantling and rebuilding the design profession — execution is being compressed, but the value of 'thinking clearly' and 'judging correctly' is rising. Figma MCP isn't just a feature update — it's design tools evolving from 'canvas' to 'protocol.'</p></div>"
    },
    "cover": images.get("figma_mcp_builder") or images.get("figma_mcp_medium") or "",
    "sources": [
        {
            "title": {"zh": "Figma Release Notes: MCP 设计开发协作", "en": "Figma Release Notes: MCP Design-Dev Collaboration"},
            "url": "https://releasebot.io/updates/figma",
            "image": images.get("figma_releasebot", "")
        },
        {
            "title": {"zh": "Builder.io: Figma MCP 设计转代码完整指南", "en": "Builder.io: Design to Code with Figma MCP Server"},
            "url": "https://www.builder.io/blog/figma-mcp-server",
            "image": images.get("figma_mcp_builder", "")
        },
        {
            "title": {"zh": "RGD: 2026 年用 AI 工具增强设计创造力", "en": "RGD: Amplifying Creativity with AI Tools in 2026"},
            "url": "https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
            "image": images.get("rgd_ai_design", "")
        },
        {
            "title": {"zh": "Medium: 2026 年值得尝试的 5 个 AI 设计工具", "en": "Medium: 5 New AI Design Tools to Try in 2026"},
            "url": "https://medium.com/design-bootcamp/5-new-ai-design-tools-to-try-in-2026-bba38068b142",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-03-28",
    "section": "tech",
    "title": {
        "zh": "SoftBank 签署 $400 亿过桥贷款加注 OpenAI · AI 基建军备竞赛：SoftBank 投资 Kandou AI 解决数据传输瓶颈 · 2026 Q1 AI 融资创纪录：$1890 亿单月集中度达 83%",
        "en": "SoftBank Signs $40B Bridge Loan to Double Down on OpenAI · AI Infra Arms Race: Kandou AI Investment Tackles Data Bottleneck · Q1 2026 AI Funding Record: $189B Month with 83% Concentration"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技（晚间版）</h3><ul><li><strong>SoftBank 签署 $400 亿过桥贷款，全力加注 OpenAI</strong> — SoftBank 于 3 月 27 日宣布签署总额 $400 亿美元的过桥贷款协议，主要用于对 OpenAI 的后续投资。此前 2 月 27 日，SoftBank 已通过 Vision Fund 2 与 OpenAI 签署 $300 亿追加投资协议，使其对 OpenAI 的总投资达到 $646 亿，持股约 13%。<strong>这是风险投资史上最大的单一标的押注——一家公司把赌桌上超过 $600 亿的筹码推向同一个名字。</strong>SoftBank 表示将通过现有资产和其他融资措施分阶段偿还贷款。<br><small>来源：<a href=\"https://group.softbank/en/news/press/20260327\">SoftBank Group</a> | <a href=\"https://www.japantimes.co.jp/business/2026/02/28/tech/openai-investment-softbank/\">Japan Times</a></small></li><li><strong>SoftBank 投资 Kandou AI：瞄准 AI 基础设施的「最后一英里」</strong> — SoftBank 同时投资了半导体初创公司 Kandou AI，该公司专注于 AI 硬件的高速低功耗数据连接技术（SerDes）。这看似是一笔小投资，但瞄准了一个关键瓶颈：<strong>当 GPU 集群越来越大时，芯片之间的数据传输效率成为整个系统的瓶颈。</strong>Kandou 的专利信号技术可以让铜缆连接上的数据传输效率大幅提升。这紧随 SoftBank 宣布的 $330 亿俄亥俄州 AI 基础设施项目之后。但市场对 SoftBank 的激进支出表达了担忧——其信用违约互换（CDS）正在扩大。<br><small>来源：<a href=\"https://www.ad-hoc-news.de/boerse/news/ueberblick/softbank-s-strategic-bet-on-ai-infrastructure-amid-financial-scrutiny/68971205\">Ad Hoc News</a></small></li><li><strong>2026 年 2 月创下史上最高单月创业融资纪录：$1890 亿</strong> — AI Funding Tracker 的数据显示，2026 年 2 月全球创业融资达到 $1890 亿——有史以来最高的单月纪录。但最惊人的数字是集中度：<strong>83% 的资金流向了三家公司：OpenAI（$1100 亿）、Anthropic（$300 亿，Series G，估值 $3800 亿）和 Waymo（$160 亿）。</strong>ElevenLabs 以 $50 亿估值 $5 亿 Series D 成为语音 AI 史上最大融资。xAI 与 SpaceX 的合并进一步重塑了 AI 版图。<strong>AI 融资已经不是「增长」——它是「集中」，资本正在以前所未有的速度涌向少数几个赢家。</strong><br><small>来源：<a href=\"https://aifundingtracker.com/top-50-ai-startups/\">AI Funding Tracker</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>SoftBank 的「All-in OpenAI」策略</strong>：$646 亿总投资 + $400 亿过桥贷款，史上最大单一标的风投押注</li><li><strong>AI 基建从 GPU 扩展到连接层</strong>：Kandou AI 的 SerDes 技术解决芯片间数据传输瓶颈</li><li><strong>AI 融资的「赢者通吃」效应</strong>：83% 集中度，中小 AI 公司的融资窗口正在关闭</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>SoftBank 在 48 小时内连签两笔 AI 投资——$400 亿过桥贷款给 OpenAI，加上 Kandou AI 的基础设施布局——这不是投资行为，这是一场国家级别的产业赌博。</strong></p><p>先看数字。SoftBank 对 OpenAI 的总投资已达 $646 亿，持股约 13%。为了完成这笔投资，它需要签署 $400 亿的过桥贷款——这意味着 SoftBank 手头没有足够的现金，需要借钱来完成投资。孙正义正在用杠杆押注 AI，就像他 2000 年用杠杆押注互联网一样。区别在于，那次他押对了阿里巴巴；这次他把所有筹码推向了 OpenAI。<strong>如果 OpenAI 成为下一个 Google，SoftBank 的 13% 股份可能价值万亿级别。但如果 AI 行业进入估值修正周期——而 Reflection AI 的故事已经暗示了这种可能——SoftBank 的资产负债表将承受巨大压力。</strong>市场已经在用 CDS 定价这个风险了。</p><p>Kandou AI 的投资则揭示了一个容易被忽略的真相：<strong>AI 基础设施的瓶颈正在从「算力」转向「连接」。</strong>当 NVIDIA 的 Vera Rubin 平台把单个 GPU 的性能推到极限时，真正制约系统性能的不再是单颗芯片有多快，而是芯片之间的数据搬运有多高效。想象一个有 10 万颗 GPU 的数据中心——如果芯片之间的数据传输跟不上计算速度，你就是在用法拉利发动机配自行车轮子。Kandou 的 SerDes 技术就是在解决这个「最后一英里」问题。SoftBank 同时投资 OpenAI（需求端）和 Kandou（供给端基础设施），说明它在押注整个 AI 产业链，而不只是某个模型公司。</p><p>但最让我不安的是那个 83% 的集中度数字。$1890 亿的单月融资，83% 流向三家公司——这不是一个健康生态系统的信号。它意味着两件事：第一，<strong>资本认为 AI 领域的赢家已经确定</strong>，剩下的公司只是在争夺残羹；第二，<strong>中小 AI 公司的融资窗口正在关闭</strong>。当 OpenAI 一次融 $1100 亿、Anthropic 一次融 $300 亿时，LP 的 AI 配额已经被填满了——留给 Series A/B 阶段 AI 初创公司的钱越来越少。</p><p>把今天的三条消息和早间的 Reflection AI 故事放在一起，AI 产业的资本结构图变得非常清晰：<strong>顶层是 OpenAI 和 Anthropic 这样的「超级巨头」，吸走了 80%+ 的资本；中间层是像 ElevenLabs 这样找到垂直赛道的「利基赢家」；底层是 Reflection AI 这样估值虚高但尚未交付的「泡沫候选人」。</strong>中间地带——那些「还行但不卓越」的通用 AI 公司——正在被挤压到不存在。这和早间创造力研究的结论形成了一个有趣的平行：AI 正在消灭创意行业的「中间层」，而 AI 产业本身的资本结构也在经历同样的「中间压缩」。在一个赢者通吃的世界里，不管你是设计师还是 AI 公司，「还行」都不再是一个可持续的位置。</p></div>",
        "en": "<h3>📌 AI × Tech (Evening)</h3><ul><li><strong>SoftBank Signs $40B Bridge Loan, Goes All-In on OpenAI</strong> — SoftBank announced a $40B bridge facility on March 27, primarily for follow-on OpenAI investments. Combined with the $30B definitive agreement from February 27, total OpenAI investment reaches $64.6B (~13% stake). The largest single-target VC bet in history. Repayment through existing assets and other financing.<br><small>Source: <a href=\"https://group.softbank/en/news/press/20260327\">SoftBank Group</a> | <a href=\"https://www.japantimes.co.jp/business/2026/02/28/tech/openai-investment-softbank/\">Japan Times</a></small></li><li><strong>SoftBank Invests in Kandou AI: Targeting AI Infra's 'Last Mile'</strong> — SoftBank invested in semiconductor startup Kandou AI, which specializes in energy-efficient high-speed data connectivity (SerDes) for AI hardware. When GPU clusters scale, inter-chip data transport becomes the bottleneck. This follows SoftBank's $33B Ohio AI infrastructure project. Markets express concern through widening CDS spreads.<br><small>Source: <a href=\"https://www.ad-hoc-news.de/boerse/news/ueberblick/softbank-s-strategic-bet-on-ai-infrastructure-amid-financial-scrutiny/68971205\">Ad Hoc News</a></small></li><li><strong>February 2026: $189B Record Month, 83% Concentrated in 3 Companies</strong> — AI Funding Tracker data: OpenAI ($110B), Anthropic ($30B at $380B valuation), Waymo ($16B) captured 83% of the record $189B month. ElevenLabs raised $500M at $5B (voice AI's largest round). xAI-SpaceX merger reshapes the landscape. Capital is concentrating at unprecedented speed.<br><small>Source: <a href=\"https://aifundingtracker.com/top-50-ai-startups/\">AI Funding Tracker</a></small></li></ul><h3>🔄 Trends</h3><ul><li>SoftBank's 'All-in OpenAI' strategy: $64.6B total + $40B bridge loan — largest single-target VC bet ever</li><li>AI infra bottleneck shifting from compute to connectivity (SerDes, inter-chip data transport)</li><li>AI funding's winner-take-all effect: 83% concentration closing the window for mid-tier AI companies</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>SoftBank signing two AI investments in 48 hours — $40B bridge loan for OpenAI plus Kandou AI infrastructure — isn't investing, it's an industrial-scale gamble.</strong> Total OpenAI investment: $64.6B at ~13% stake, funded partly through bridge loans (meaning SoftBank doesn't have the cash and is borrowing to invest). Masayoshi Son is leveraging into AI like he leveraged into the internet in 2000 — that time he got Alibaba right. If OpenAI becomes the next Google, 13% could be worth trillions. But if AI enters a valuation correction — and Reflection AI's story hints at this possibility — SoftBank's balance sheet faces enormous pressure. Markets are already pricing this risk via widening CDS. Kandou AI reveals an overlooked truth: AI infrastructure bottlenecks are shifting from compute to connectivity. A 100K-GPU data center is only as fast as its inter-chip data transport — Ferrari engine on bicycle wheels. SoftBank investing in both OpenAI (demand) and Kandou (supply infrastructure) shows full-stack industry chain betting. The 83% concentration figure is the most alarming signal: $189B flowing to 3 companies means LPs' AI allocations are being consumed by mega-rounds, leaving less for Series A/B startups. <strong>AI's capital structure mirrors the creativity research: the 'middle tier' is being compressed out of existence. Whether you're a designer or an AI company, 'good enough' is no longer a sustainable position.</strong></p></div>"
    },
    "cover": images.get("softbank_bridge") or images.get("aifunding") or "",
    "sources": [
        {
            "title": {"zh": "SoftBank: $400 亿过桥贷款协议", "en": "SoftBank: $40B Bridge Facility Agreement"},
            "url": "https://group.softbank/en/news/press/20260327",
            "image": images.get("softbank_bridge", "")
        },
        {
            "title": {"zh": "Ad Hoc News: SoftBank 投资 Kandou AI 布局基础设施", "en": "Ad Hoc News: SoftBank's Strategic Bet on Kandou AI"},
            "url": "https://www.ad-hoc-news.de/boerse/news/ueberblick/softbank-s-strategic-bet-on-ai-infrastructure-amid-financial-scrutiny/68971205",
            "image": images.get("softbank_kandou", "")
        },
        {
            "title": {"zh": "AI Funding Tracker: 2026 年 Top 50 AI 融资排名", "en": "AI Funding Tracker: Top 50 AI Funded Startups 2026"},
            "url": "https://aifundingtracker.com/top-50-ai-startups/",
            "image": images.get("aifunding", "")
        },
        {
            "title": {"zh": "Japan Times: OpenAI 获 $1100 亿投资", "en": "Japan Times: OpenAI Gets $110B Investment"},
            "url": "https://www.japantimes.co.jp/business/2026/02/28/tech/openai-investment-softbank/",
            "image": ""
        }
    ]
}

# Insert new issues at front
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("Done! Added 2 evening issues for 2026-03-28.")
