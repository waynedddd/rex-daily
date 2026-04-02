# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Update - 2026-04-02"""
import json
import urllib.request
import re
import ssl

def get_og_image(url):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            html = resp.read().decode("utf-8", errors="ignore")[:50000]
            m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
            if not m:
                m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
            return m.group(1) if m else ""
    except:
        return ""

# URLs
design_urls = [
    "https://blog.adobe.com/en/publish/2025/11/25/introducing-project-graph-creative-workflows-reimagined",
    "https://medium.com/@fadimantium/2026-the-year-of-the-node-based-editor-941f0f15d467",
    "https://tech.yahoo.com/ai/apple-intelligence/articles/creatives-ai-2026-according-adobe-090000538.html",
]
tech_urls = [
    "https://fortune.com/2026/04/01/inflationary-surge-ai-hype-fed-reserve-bank/",
    "https://www.nytimes.com/2026/04/01/technology/ai-companies-fund-raising-records.html",
    "https://www.businessinsider.com/read-oracle-layoff-email-employees-job-cuts-2026-3",
]

print("Fetching og:images...")
design_images = [get_og_image(u) for u in design_urls]
tech_images = [get_og_image(u) for u in tech_urls]
print(f"Design images: {design_images}")
print(f"Tech images: {tech_images}")

design_issue = {
    "date": "2026-04-02",
    "section": "design",
    "title": {
        "zh": "2026 是节点编辑器之年：Adobe Project Graph 重新定义创意工作流 · AI 设计工具从「生成器」进化为「创意系统」· 设计师的新核心技能：编排而非操作",
        "en": "2026: Year of the Node-Based Editor — Adobe Project Graph Redefines Creative Workflows · AI Design Tools Evolve from Generators to Creative Systems · Designers' New Core Skill: Orchestration Over Operation"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Adobe Project Graph：从「工具」到「创意操作系统」的范式转移</strong> — Adobe 的 Project Graph 正在从 MAX 2025 的概念预览走向实际落地。这是一个基于节点的可视化系统，允许设计师将 AI 模型（Firefly、Gemini、OpenAI）、Adobe 工具和特效像乐高一样连接起来，构建可复用、可共享的创意工作流。<strong>核心理念：设计师不再是「使用工具的人」，而是「设计工具的人」——你构建的不是一张图，而是一个创意系统。</strong>这些工作流可以跨 Creative Cloud 应用移植，甚至可以分享给团队成员一键使用。<br><small>来源：<a href=\"https://blog.adobe.com/en/publish/2025/11/25/introducing-project-graph-creative-workflows-reimagined\">Adobe Blog</a></small></li><li><strong>2026：节点编辑器之年</strong> — Medium 上一篇引发广泛讨论的文章指出，2026 年节点编辑器正在成为创意 AI 工具的默认交互范式。<strong>不只是 Adobe——Runway、Weavy 等平台都在向节点化方向演进。</strong>作者认为这代表了一种根本性转变：从「对话式 AI」（你说，它做）到「系统式 AI」（你搭建管道，AI 在管道里运行）。这和上周 Figma MCP 的逻辑一脉相承：最终赢的不是最会画画的 AI，而是让设计师最高效地编排 AI 的平台。<br><small>来源：<a href=\"https://medium.com/@fadimantium/2026-the-year-of-the-node-based-editor-941f0f15d467\">Medium</a></small></li><li><strong>Adobe 的开放策略：引入 Runway、Flux、Nano Banana 等第三方模型</strong> — Adobe 近期将 Runway、Flux 和 Nano Banana 等第三方 AI 模型集成进自家应用，这是一个巨大的战略转向。<strong>Adobe 从「只用自家 Firefly」变成了「AI 模型的应用商店」。</strong>VP Deepa Subramaniam 认为创意工作流正在走向「更灵活、更模糊」的方向——不是一个工具干所有事，而是多个 AI 模型像工具箱里的不同工具，按需组合。<br><small>来源：<a href=\"https://tech.yahoo.com/ai/apple-intelligence/articles/creatives-ai-2026-according-adobe-090000538.html\">Yahoo Tech</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>从对话到编排</strong>：AI 设计工具的交互范式从「prompt → output」变成「node → pipeline → system」</li><li><strong>平台开放化</strong>：Adobe 引入竞品模型，Figma 开放 MCP——大平台都在争当「创意 AI 的操作系统」</li><li><strong>设计师角色再升级</strong>：从「画图」到「搭系统」，编排能力成为核心竞争力</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>如果说上周 Figma MCP 是设计行业的「基础设施事件」，这周 Adobe Project Graph 和节点编辑器的崛起就是那个事件的回响——而且可能更深远。</strong></p><p>让我把这些点连起来。Figma MCP 解决的是「AI Agent 怎么在现有设计系统里干活」——本质上是自动化执行层。Project Graph 解决的是一个更上游的问题：「设计师怎么构建自己的 AI 创意管道」——这是在赋能创作层。两者不是竞争关系，而是设计工作流的两个不同层次：Figma 管执行规范，Adobe 管创意系统。如果你同时用好这两个，你就拥有了一个从概念到交付的完整 AI 增强工作流。</p><p>节点编辑器为什么是正确的范式？因为对话式 AI（prompt → output）有一个致命缺陷：<strong>不可复现。</strong>你今天写的 prompt 明天可能得到完全不同的结果。而节点化工作流是确定性的：输入 A 经过节点 1、2、3，永远输出 B。这对专业设计师至关重要——客户不在乎你的 AI 有多「创意」，他们在乎你能不能稳定输出符合品牌规范的资产。Project Graph 让设计师把自己的「创意方法论」固化为可执行的系统，这本质上是在把隐性知识变成显性知识——和 Figma MCP 的 Skills-as-Markdown 思路完全一致。</p><p>Adobe 引入第三方模型这步棋尤其值得关注。还记得 2024 年 Adobe 对 AI 生成内容的态度吗？「只用自家 Firefly，保证版权安全」。现在呢？Runway、Flux、Nano Banana 全进来了。<strong>这不是 Adobe「开放」了，这是 Adobe 意识到 Firefly 单打独斗打不过——用户需要不同模型的不同能力，就像画家需要不同品牌的颜料。</strong>Adobe 的新定位很清楚：不做最好的 AI 模型，做最好的 AI 模型聚合器和编排器。这和微软在操作系统层面做的事完全一样：不做最好的应用，做应用运行的平台。</p><p><strong>我的预测：18 个月内，「会用 Midjourney 生成图片」这个技能的市场价值会接近零，而「能用 Project Graph 搭建自动化创意管道」这个技能会成为高级设计师的标配。</strong>原因很简单：前者任何人都能做，后者需要理解设计系统、品牌规范、生产流程和 AI 模型的特性——这是真正的专业壁垒。如果你是设计师，现在就应该开始学节点编辑器的思维方式。不一定是 Project Graph——ComfyUI、Runway 的节点系统都可以——重要的是理解「编排」这个概念。因为 AI 时代的设计师，本质上是创意管道的架构师。</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Adobe Project Graph: From Tool to Creative Operating System</strong> — Adobe's Project Graph is moving from MAX 2025 concept preview to reality. This node-based visual system lets designers connect AI models (Firefly, Gemini, OpenAI), Adobe tools, and effects like building blocks to create reusable, shareable creative workflows. <strong>Core idea: designers shift from \"tool users\" to \"tool builders\"—you create creative systems, not just images.</strong><br><small>Source: <a href=\"https://blog.adobe.com/en/publish/2025/11/25/introducing-project-graph-creative-workflows-reimagined\">Adobe Blog</a></small></li><li><strong>2026: Year of the Node-Based Editor</strong> — A widely-discussed Medium article argues node editors are becoming the default interaction paradigm for creative AI. <strong>Not just Adobe—Runway, Weavy are all going node-based.</strong> This represents a fundamental shift from \"conversational AI\" (you talk, it makes) to \"systematic AI\" (you build pipelines, AI runs within them).<br><small>Source: <a href=\"https://medium.com/@fadimantium/2026-the-year-of-the-node-based-editor-941f0f15d467\">Medium</a></small></li><li><strong>Adobe's Open Strategy: Third-Party Models Enter Creative Cloud</strong> — Adobe recently integrated Runway, Flux, and Nano Banana into its apps—a major strategic shift from \"Firefly only\" to \"AI model marketplace.\" <strong>VP Deepa Subramaniam sees creative workflows heading toward more flexible, modular approaches.</strong><br><small>Source: <a href=\"https://tech.yahoo.com/ai/apple-intelligence/articles/creatives-ai-2026-according-adobe-090000538.html\">Yahoo Tech</a></small></li></ul><h3>🔄 Trends</h3><ul><li>From conversation to orchestration: AI design interaction shifts from prompt→output to node→pipeline→system</li><li>Platform openness: Adobe adds competitor models, Figma opens MCP—big platforms compete to be \"the OS for creative AI\"</li><li>Designer role upgrade: from drawing to system building; orchestration becomes core competency</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>If Figma MCP was last week's infrastructure event, Adobe Project Graph and the rise of node editors are its echo—and potentially more profound.</strong> Figma MCP automates execution (AI agents working within design systems). Project Graph empowers creation (designers building AI creative pipelines). Together, they form a complete AI-augmented workflow from concept to delivery. Node editors are the right paradigm because conversational AI has a fatal flaw: non-reproducibility. Today's prompt may yield different results tomorrow. Node workflows are deterministic—critical for professional output. Adobe opening to third-party models (Runway, Flux, Nano Banana) signals a strategic retreat from \"Firefly only\" to \"best AI model aggregator\"—same logic as Microsoft: don't make the best apps, make the platform apps run on. <strong>Prediction: within 18 months, \"generating images with Midjourney\" will be a near-zero-value skill, while \"building automated creative pipelines with Project Graph\" becomes table stakes for senior designers.</strong> The moat is understanding design systems + brand specs + production flows + model characteristics. If you're a designer, start learning node-based thinking now.</p></div>"
    },
    "cover": design_images[0] if design_images[0] else "",
    "sources": [
        {
            "title": {"zh": "Adobe Project Graph：重新定义创意工作流", "en": "Adobe Project Graph: Creative Workflows Reimagined"},
            "url": "https://blog.adobe.com/en/publish/2025/11/25/introducing-project-graph-creative-workflows-reimagined",
            "image": design_images[0]
        },
        {
            "title": {"zh": "2026：节点编辑器之年", "en": "2026: The Year of the Node-Based Editor"},
            "url": "https://medium.com/@fadimantium/2026-the-year-of-the-node-based-editor-941f0f15d467",
            "image": design_images[1]
        },
        {
            "title": {"zh": "Adobe 谈创意人如何在 2026 年使用 AI", "en": "How Creatives Will Use AI in 2026, According to Adobe"},
            "url": "https://tech.yahoo.com/ai/apple-intelligence/articles/creatives-ai-2026-according-adobe-090000538.html",
            "image": design_images[2]
        }
    ]
}

tech_issue = {
    "date": "2026-04-02",
    "section": "tech",
    "title": {
        "zh": "Q1 全球 VC 投资 2970 亿美元破纪录，AI 占 81% · 美联储警告 AI 炒作正在推高通胀 · Oracle 凌晨 6 点邮件裁员 3 万人",
        "en": "Q1 Global VC Hits Record $297B with AI at 81% · Fed Warns AI Hype Is Fueling Inflation · Oracle Lays Off 30K via 6AM Email"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Q1 2026 全球风投创纪录 2970 亿美元，AI 占 81%</strong> — Crunchbase 数据显示，2026 年 Q1 全球创业公司融资 2970 亿美元，涉及 6000 笔交易，其中 AI 占 2390 亿美元（81%），远超 2025 年 Q1 的 55%。<strong>四笔史上最大风投交易中有三笔发生在本季度：OpenAI 1220 亿美元（估值 8520 亿）、Anthropic 300 亿美元（估值约 3800 亿）、xAI 200 亿美元、Waymo 160 亿美元。仅这四笔就占总融资的 63%。</strong>Crunchbase 独角兽榜单总值暴增 9000 亿美元。OpenAI 的融资加速了其 IPO 计划。<br><small>来源：<a href=\"https://www.nytimes.com/2026/04/01/technology/ai-companies-fund-raising-records.html\">NYT</a>、<a href=\"https://beamstart.com/news/q1-2026-shatters-venture-funding-17750437661128\">Crunchbase/BeamStart</a></small></li><li><strong>美联储经济学家警告：AI 炒作正在推高通胀，无论技术是否兑现</strong> — 圣路易斯联邦储备银行在 4 月 1 日发表的博客文章中指出，AI 乐观情绪可能充当「新闻冲击」（news shock），影响家庭和企业决策，进而推高通胀。<strong>关键洞察：你不需要等 AI 真正改变生产力，光是「相信 AI 会改变一切」这个预期本身就在改变经济行为——企业加大投资、推高薪资、争抢算力，最终传导为物价上涨。</strong>目前高度集中的科技公司已向 AI 基础设施投入约 7000 亿美元。Fortune 引用 Matt Shumer 2 月的病毒式帖子：他将 AI 的当前轨迹比作新冠疫情爆发前一个月。<br><small>来源：<a href=\"https://fortune.com/2026/04/01/inflationary-surge-ai-hype-fed-reserve-bank/\">Fortune</a>、<a href=\"https://www.stlouisfed.org/on-the-economy/2026/mar/can-ai-optimism-raise-inflation-what-standard-macro-model-says\">St. Louis Fed</a></small></li><li><strong>Oracle 凌晨 6 点邮件一刀切裁员 3 万人</strong> — Oracle 员工在 4 月 1 日凌晨 6 点收到来自「Oracle Leadership」的邮件，被告知「经过慎重考虑，我们决定在更广泛的组织变革中取消你的职位」。<strong>没有事先通知、没有 HR 电话、没有主管沟通——收到邮件当天就是最后工作日。</strong>邮件要求员工提供个人邮箱以接收离职文件，并禁止下载或复制任何 Oracle 机密信息。Business Insider 获取了邮件全文。社交媒体上的反应极其激烈，被称为「史上最冰冷的裁员方式」。<br><small>来源：<a href=\"https://www.businessinsider.com/read-oracle-layoff-email-employees-job-cuts-2026-3\">Business Insider</a>、<a href=\"https://timesofindia.indiatimes.com/technology/tech-news/oracle-layoffs-employees-receive-email-from-oracle-leadership-at-6am-saying-we-have-made-the-decision-to-eliminate-your-role-as/articleshow/129922918.cms\">Times of India</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 融资的「赢家通吃」格局</strong>：四家公司拿走 63% 的融资，剩下几千家创业公司分剩余</li><li><strong>AI 的宏观经济效应已经到来</strong>：不是 AI 本身改变了经济，是对 AI 的预期改变了经济</li><li><strong>AI 时代的裁员变得更「高效」也更残忍</strong>：自动化不只替代了工作，也替代了裁员的人情味</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天这三条新闻放在一起，画出了一幅令人不安的图景：钱在疯狂涌入 AI，央行在警告泡沫，而泡沫的第一批受害者已经出现。</strong></p><p>先看数字。Q1 2970 亿美元，AI 占 81%。一年前这个比例是 55%。四笔交易拿走 63%。这不是「AI 行业在增长」，这是「四家公司在虹吸全球风险资本」。OpenAI 一笔融资 1220 亿美元——这个数字超过了 2023 年全年全球风投总额。我们正在见证的不是健康的行业繁荣，而是资本在极少数公司身上的史无前例的集中。<strong>这和 2000 年互联网泡沫有一个关键区别：当年是几百家公司各拿一点，现在是四家公司拿走大部分。集中度更高意味着崩盘时的冲击更大，但也意味着这几家公司如果成功了，回报更惊人。</strong></p><p>美联储圣路易斯分行的分析非常精彩，揭示了一个反直觉的真相：<strong>AI 不需要「成功」就能影响经济——光是人们「相信」AI 会成功，就已经在改变消费、投资和价格。</strong>7000 亿美元的基础设施投资推高了芯片、电力、数据中心用地的价格；科技公司为 AI 人才开出天价薪酬推高了劳动力成本；企业「为了 AI 转型」的支出推高了 SaaS 价格。这些都是真实的通胀压力，和 AI 最终能不能提高生产力无关。把这和上周 55% 美国人认为 AI 弊大于利的数据放在一起：普通人的直觉可能是对的——AI 确实在让他们的生活更贵了，只不过不是通过「取代工作」，而是通过「推高物价」这个更隐蔽的渠道。</p><p>Oracle 的裁员方式是今天最让人心寒的新闻。3 万人，凌晨 6 点，一封邮件，当天生效。没有通知，没有沟通，没有过渡。<strong>讽刺的是，这种「高效」的裁员方式本身就是 AI 时代的隐喻：当你把人当成系统里的节点，关掉一个节点就像关掉一台服务器一样简单。</strong>更大的背景是：Oracle 在将资源转向 AI 基础设施——Larry Ellison 几个月前刚宣布了大规模 AI 数据中心扩建计划。所以我们看到的画面是：钱从传统业务的人身上抽出来，灌进 AI 的芯片里。这不是「AI 取代了 3 万个工作」——Oracle 裁的不是因为 AI 自动化了他们的岗位，而是因为公司要省钱去投 AI。人被牺牲了，不是因为机器比他们更能干，而是因为资本觉得机器的未来比他们的现在更值钱。</p><p><strong>把三件事连起来：2970 亿美元融资 → 美联储通胀警告 → 3 万人被裁。这就是 2026 年 AI 经济的完整链条：资本涌入 → 物价上涨 → 人被挤出。</strong>我不是在说 AI 不好，我是在说我们正处于一个「AI 的收益极度集中、AI 的成本极度分散」的阶段。如果你在那四家公司里，恭喜你；如果你在 Oracle 的裁员名单上，你刚刚为别人的 AI 梦想买了单。</p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Q1 2026 Global VC Hits Record $297B, AI Captures 81%</strong> — Crunchbase data shows Q1 2026 startup funding reached $297B across 6,000 deals, with AI claiming $239B (81%), up from 55% in Q1 2025. <strong>Three of the four largest VC deals ever closed this quarter: OpenAI $122B ($852B valuation), Anthropic $30B (~$380B valuation), xAI $20B, Waymo $16B—63% of total funding in just four rounds.</strong><br><small>Source: <a href=\"https://www.nytimes.com/2026/04/01/technology/ai-companies-fund-raising-records.html\">NYT</a>, <a href=\"https://beamstart.com/news/q1-2026-shatters-venture-funding-17750437661128\">Crunchbase</a></small></li><li><strong>Fed Economists Warn: AI Hype Is Fueling Inflation Whether or Not It Delivers</strong> — St. Louis Fed economists argue AI optimism acts as a \"news shock\" driving household and business decisions, pushing up inflation. <strong>Key insight: you don't need AI to improve productivity—the belief that it will is already changing economic behavior.</strong> $700B already invested in AI infrastructure.<br><small>Source: <a href=\"https://fortune.com/2026/04/01/inflationary-surge-ai-hype-fed-reserve-bank/\">Fortune</a></small></li><li><strong>Oracle Fires 30,000 via Ice-Cold 6AM Email</strong> — Oracle employees received termination emails at 6AM from \"Oracle Leadership\" with no prior notice, no HR call, no manager involvement. Same-day effective. <strong>Social media called it \"the coldest layoff in history.\"</strong><br><small>Source: <a href=\"https://www.businessinsider.com/read-oracle-layoff-email-employees-job-cuts-2026-3\">Business Insider</a>, <a href=\"https://timesofindia.indiatimes.com/technology/tech-news/oracle-layoffs-employees-receive-email-from-oracle-leadership-at-6am-saying-we-have-made-the-decision-to-eliminate-your-role-as/articleshow/129922918.cms\">Times of India</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI funding's winner-take-all: 4 companies took 63% of all VC</li><li>AI's macro effects arrived: expectations alone are changing the economy</li><li>AI-era layoffs: more \"efficient,\" more brutal</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>These three stories together paint a disturbing picture: money is flooding into AI, the central bank is warning of a bubble, and the first casualties are already here.</strong> $297B in Q1 with 81% going to AI—four deals taking 63%—isn't industry growth, it's capital concentration at unprecedented scale. The Fed's analysis reveals a counterintuitive truth: AI doesn't need to \"work\" to affect the economy—belief alone changes spending, investment, and prices. $700B in infrastructure is pushing up chips, power, land, and talent costs regardless of AI's actual productivity gains. Oracle's 30K layoffs via 6AM email is the cruelest metaphor: people treated as system nodes, shut off like servers. The bigger context: Oracle is redirecting resources to AI infrastructure. <strong>The complete chain of 2026's AI economy: $297B funding → Fed inflation warning → 30K fired. Capital floods in → prices rise → people get squeezed out.</strong> We're in a phase where AI's benefits are extremely concentrated and its costs extremely distributed.</p></div>"
    },
    "cover": tech_images[0] if tech_images[0] else "",
    "sources": [
        {
            "title": {"zh": "美联储警告 AI 炒作推高通胀", "en": "Fed Warns AI Hype Is Overheating the Economy"},
            "url": "https://fortune.com/2026/04/01/inflationary-surge-ai-hype-fed-reserve-bank/",
            "image": tech_images[0]
        },
        {
            "title": {"zh": "AI 公司 Q1 融资破纪录", "en": "AI Companies Shatter Fund-Raising Records"},
            "url": "https://www.nytimes.com/2026/04/01/technology/ai-companies-fund-raising-records.html",
            "image": tech_images[1]
        },
        {
            "title": {"zh": "Oracle 凌晨邮件裁员 3 万人", "en": "Oracle Lays Off 30K via 6AM Email"},
            "url": "https://www.businessinsider.com/read-oracle-layoff-email-employees-job-cuts-2026-3",
            "image": tech_images[2]
        }
    ]
}

# Load existing issues
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

# Insert new issues at the front
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

# Write back
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("Done! Added 2 issues for 2026-04-02")
