# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-04-02 Evening Update"""
import json
import urllib.request
import re
import ssl

def fetch_og_image(url):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            html = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html)
        if not m:
            m = re.search(r'content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html)
        return m.group(1) if m else ""
    except Exception as e:
        print(f"  og:image fetch failed for {url}: {e}")
        return ""

# Fetch og:images
urls = {
    "figma_state": "https://www.figma.com/blog/state-of-the-designer-2026/",
    "figma_agents": "https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/",
    "creativebloq": "https://www.creativebloq.com/art/digital-art/digital-art-trends-2026-reveal-how-creatives-are-responding-to-ai-pressure",
    "morgan_stanley": "https://fortune.com/2026/03/13/elon-musk-morgan-stanley-ai-leap-2026/",
    "apple_google": "https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html",
    "google_spending": "https://www.nytimes.com/2026/02/04/business/google-earnings-ai.html",
}

images = {}
for key, url in urls.items():
    print(f"Fetching og:image for {key}...")
    images[key] = fetch_og_image(url)
    print(f"  -> {images[key][:80] if images[key] else 'none'}")

design_issue = {
    "date": "2026-04-02",
    "section": "design",
    "title": {
        "zh": "Figma 2026 设计师报告：89% 认为 AI 加速工作 · Canvas 向 AI Agent 全面开放 · 数字艺术家「逃离屏幕」转向传统媒介",
        "en": "Figma State of Designer 2026: 89% Say AI Speeds Up Work · Canvas Opens to AI Agents · Digital Artists Flee Screens for Traditional Media"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Figma「2026 设计师现状」报告：乐观与焦虑并存</strong> — Figma 发布年度 State of the Designer 报告，数据令人玩味：89% 的设计师认为 AI 工具让他们工作更快，80% 表示协作更好，但报告同时承认「AI 对产品设计的影响可能让人感到不稳定」。<strong>最关键的数据：主动使用 AI 工具的设计师，工作满意度比不用的高 25%。</strong>这不是因为 AI 让工作更轻松——而是因为掌握新工具带来了掌控感。报告揭示了一个行业分水岭：不是「AI 会不会取代设计师」，而是「用 AI 的设计师会不会取代不用的设计师」。<br><small>来源：<a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a></small></li><li><strong>Figma Canvas 向 AI Agent 全面开放：设计的「API 时刻」</strong> — Figma 宣布 AI Agent 现在可以直接在 Canvas 上创建和编辑组件、应用变量、使用设计系统构建设计——不只是读取文件，而是真正「在 Figma 里干活」。Cursor、Claude Code 等开发工具可以通过 MCP 直接操作 Figma 画布。<strong>Canvas 从「设计师的交付物」变成了「Agent 和设计师共同工作的活文档」。</strong>这和 Codex to Figma（2 月发布）形成完整闭环：代码 → Figma → 代码，AI Agent 在中间自由穿梭。<br><small>来源：<a href=\"https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/\">Figma Blog</a>、<a href=\"https://muz.li/blog/figma-just-opened-the-canvas-to-ai-agents-heres-what-it-means-for-designers/\">Muzli</a></small></li><li><strong>数字艺术家「逃离屏幕」：AI 压力下的反向迁移</strong> — Creative Bloq 的 2026 数字艺术趋势报告揭示了一个出人意料的现象：大量 2D 数字艺术家正在转向传统媒介（油画、雕塑），同时也有人涌向 3D、AR/VR 和游戏引擎（Unreal Engine 5、Unity、Godot）。<strong>背后逻辑很简单：AI 最先「压平」的是 2D 数字艺术这个赛道，而传统媒介和 3D 交互领域是 AI 最难渗透的。</strong>不少艺术家在建立「多收入流」——插画、概念设计之外增加传统艺术销售作为保险。<br><small>来源：<a href=\"https://www.creativebloq.com/art/digital-art/digital-art-trends-2026-reveal-how-creatives-are-responding-to-ai-pressure\">Creative Bloq</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 工具满意度 ≠ 工作安全感</strong>：设计师在用 AI 加速的同时，也在焦虑 AI 替代</li><li><strong>Canvas as Platform</strong>：Figma 的策略越来越清晰——不做最好的 AI 设计，做 AI 设计的操作系统</li><li><strong>创意人的「对冲策略」</strong>：用 AI 提效主业，用传统技能建立 AI 不可替代的护城河</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天这三条新闻如果只看表面，是三个不相关的故事。但把它们放在一起，你会看到 2026 年设计行业的完整心理画像：一边在拥抱，一边在逃离，核心驱动力是同一个——对 AI 重塑创意工作的深层焦虑。</strong></p><p>先看 Figma 的数据。89% 的设计师说 AI 让他们更快，80% 说协作更好。这些数字漂亮得让人想起 2023 年每家公司 PPT 里的「数字化转型满意度」。但真正有意思的是那个 25% 的满意度差距——用 AI 的设计师比不用的满意度高 25%。这个数据的另一面是：<strong>不用 AI 的设计师不只是「效率低」，他们在心理上已经开始感受到被边缘化的压力。</strong>当你的同事用 AI 一天出 20 个方案而你还在手动推像素，焦虑不是来自 AI 本身，而是来自同行的效率差距。这才是真正的行业分裂线。</p><p>Figma 向 AI Agent 开放 Canvas 这步棋，放在上周 Adobe Project Graph 和节点编辑器趋势的背景下看更有味道。Adobe 选择了「设计师搭建 AI 管道」的路线——设计师是导演，AI 是演员。Figma 选择了另一条路：「AI Agent 直接在 Canvas 上干活」——设计师是验收者，AI 是执行者。<strong>这两种范式都在赌设计师的未来角色，但赌的方向不同。Adobe 赌设计师还会亲自动手（只是用更强的工具），Figma 赌设计师会变成审核者和决策者（让 Agent 干脏活）。</strong>我个人更看好 Figma 的路线，因为它更符合生产力工具的历史规律：Excel 没有让财务总监学写公式，它让分析师学会了，财务总监只看结果。同理，Figma Canvas 上的 Agent 不会取代设计总监，它会取代初级设计师的执行工作，而设计总监会在 Agent 的输出上做判断和修正。</p><p>最让我唏嘘的是 Creative Bloq 那篇数字艺术家「逃离屏幕」的报道。2D 数字艺术家转向油画和雕塑——这不是「复古潮流」，<strong>这是一群人在用最古老的技能建立 AI 无法入侵的最后堡垒。</strong>而另一群人冲向 3D 和游戏引擎，是因为这些领域的「手工成本」足够高，AI 短期内还无法自动化。两个方向，同一个逻辑：逃向 AI 够不到的地方。但问题是，AI 够不到的地方会越来越少。ComfyUI 已经在做 3D 生成了，Midjourney V7 的 3D 能力也在进化。传统油画或许安全，但市场有多大？</p><p><strong>把三件事连起来：Figma 报告说 89% 的设计师更快了——但更快不等于更安全；Canvas 向 Agent 开放——执行层正在被接管；数字艺术家逃离屏幕——已经有人在用脚投票。2026 年的设计行业不是「AI 取代设计师」这种简单叙事，而是一场更微妙的重组：会编排 AI 的设计师在上升，只会执行的在下沉，而最聪明的那一批在同时做两手准备——用 AI 提效当下，用「人类独有的手艺」对冲未来。</strong></p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Figma State of Designer 2026: Optimism Meets Anxiety</strong> — 89% say AI makes them faster, 80% report better collaboration, but the report acknowledges AI's impact \"can feel destabilizing.\" <strong>Key data: designers actively using AI are 25% more satisfied at work.</strong> The divide isn't AI vs. humans—it's AI-using designers vs. non-AI designers.<br><small>Source: <a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a></small></li><li><strong>Figma Opens Canvas to AI Agents: Design's \"API Moment\"</strong> — AI agents can now create/edit components, apply variables, and build designs directly on Figma's canvas. Cursor, Claude Code work through MCP. <strong>Canvas transforms from deliverable to live artifact where agents and designers collaborate.</strong> Combined with Codex to Figma (Feb), this creates a complete code↔design loop.<br><small>Source: <a href=\"https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/\">Figma Blog</a>, <a href=\"https://muz.li/blog/figma-just-opened-the-canvas-to-ai-agents-heres-what-it-means-for-designers/\">Muzli</a></small></li><li><strong>Digital Artists \"Flee the Screen\": AI Pressure Drives Reverse Migration</strong> — Creative Bloq reports 2D digital artists are moving to traditional media (painting, sculpture) and 3D/AR/VR/game engines. <strong>Logic: AI flattened 2D digital art first; traditional and 3D interactive are hardest to penetrate.</strong><br><small>Source: <a href=\"https://www.creativebloq.com/art/digital-art/digital-art-trends-2026-reveal-how-creatives-are-responding-to-ai-pressure\">Creative Bloq</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI tool satisfaction ≠ job security: designers accelerate while anxious</li><li>Canvas as Platform: Figma's strategy—be the OS for AI design, not the best AI designer</li><li>Creative hedging: AI for efficiency now, traditional skills as AI-proof moat</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Three seemingly unrelated stories paint the complete psychological portrait of design in 2026: embracing and fleeing simultaneously, driven by the same deep anxiety about AI reshaping creative work.</strong> The 25% satisfaction gap reveals the real divide—non-AI designers aren't just slower, they're feeling marginalized. Figma's Canvas-to-Agents vs. Adobe's Project Graph represent two competing bets: Adobe bets designers will still orchestrate hands-on (better tools); Figma bets designers become reviewers (agents do execution). I favor Figma's approach—it follows the Excel pattern: the CFO doesn't write formulas, they review outputs. Digital artists fleeing to painting and sculpture aren't following a retro trend—they're building the last AI-proof fortress. But AI-proof zones keep shrinking. <strong>2026's design industry isn't \"AI replaces designers\"—it's a subtler reorganization: AI orchestrators rise, pure executors sink, and the smartest hedge both ways.</strong></p></div>"
    },
    "cover": images.get("figma_state", ""),
    "sources": [
        {
            "title": {"zh": "Figma 2026 设计师现状报告", "en": "Figma State of the Designer 2026"},
            "url": "https://www.figma.com/blog/state-of-the-designer-2026/",
            "image": images.get("figma_state", "")
        },
        {
            "title": {"zh": "Figma Canvas 向 AI Agent 开放", "en": "Figma Opens Canvas to AI Agents"},
            "url": "https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/",
            "image": images.get("figma_agents", "")
        },
        {
            "title": {"zh": "数字艺术趋势 2026：创意人如何应对 AI 压力", "en": "Digital Art Trends 2026: How Creatives Respond to AI Pressure"},
            "url": "https://www.creativebloq.com/art/digital-art/digital-art-trends-2026-reveal-how-creatives-are-responding-to-ai-pressure",
            "image": images.get("creativebloq", "")
        }
    ]
}

tech_issue = {
    "date": "2026-04-02",
    "section": "tech",
    "title": {
        "zh": "Morgan Stanley 警告 AI 超级突破「数月内到来」· Apple 选择 Google Gemini 驱动新 Siri · Google 计划 AI 支出翻倍",
        "en": "Morgan Stanley Warns AI Mega-Breakthrough 'Months Away' · Apple Picks Google Gemini for New Siri · Google Plans to Double AI Spending"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Morgan Stanley 警告：超级 AI 突破「数月内到来」，多数人没准备好</strong> — Morgan Stanley 在 3 月发布重磅报告，预测 2026 年上半年将出现「震撼级」AI 突破。报告指出 GPT-5.4 在专家级基准测试中已接近人类水平，计算规模的持续扩张正在产生真正的质变。<strong>但核心瓶颈不是算法——是电力。报告预测 9-18GW 的电力缺口，以及芯片供应和制度准备的严重滞后。</strong>Morgan Stanley 同时认为 AI 将成为「强大的通缩力量」，这和上期日报中美联储的「AI 推高通胀」形成有趣对比：华尔街和央行在同一个问题上给出了完全相反的结论。<br><small>来源：<a href=\"https://fortune.com/2026/03/13/elon-musk-morgan-stanley-ai-leap-2026/\">Fortune</a>、<a href=\"https://daily1bite.com/en/blog/dev-life/morgan-stanley-ai-leap-2026\">Daily1Bite</a></small></li><li><strong>Apple 选择 Google Gemini 驱动新一代 Siri</strong> — CNBC 1 月独家报道，Apple 已与 Google 达成协议，将 Gemini 集成到 Siri 和 Apple Intelligence 中。此前 Apple 与 OpenAI 合作将 ChatGPT 接入 Siri 处理复杂查询，现在 Google 也加入了。<strong>Apple 的策略很清楚：不自己做最强的 AI 模型，而是做「AI 模型的策展人」——按场景选择最合适的模型。</strong>The Information 进一步披露，Apple 甚至可以「蒸馏」Google 的大型 Gemini 模型，将其能力压缩到设备端运行。同时，OpenAI 正在与 Jony Ive 合作开发 AI 硬件设备，可能 2026 年亮相——前 Apple 设计灵魂人物转投 OpenAI 阵营，这个叙事太有戏剧性了。<br><small>来源：<a href=\"https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html\">CNBC</a>、<a href=\"https://www.theinformation.com/newsletters/ai-agenda/apple-can-distill-googles-big-gemini-model\">The Information</a></small></li><li><strong>Google 计划 AI 支出翻倍：从「追赶者」到「领跑者」</strong> — NYT 报道 Google 计划将 AI 相关支出翻倍，标志着其从 2024 年的 AI 「早期失误」中强势反弹。Gemini 系列模型在多项基准测试中已超越竞争对手。<strong>LinkedIn 数据显示 AI 在过去三年创造了约 130 万个新工作岗位。</strong>Reuters 的 2026 AI 主题预测同样强调，AI 基础设施投资正在从「概念验证」进入「大规模部署」阶段。<br><small>来源：<a href=\"https://www.nytimes.com/2026/02/04/business/google-earnings-ai.html\">NYT</a>、<a href=\"https://www.reuters.com/technology/artificial-intelligence/artificial-intelligencer-top-ai-themes-that-will-shape-2026-2026-01-15/\">Reuters</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 突破的瓶颈在硬件不在算法</strong>：电力、芯片、数据中心是真正的制约因素</li><li><strong>大厂的「AI 模型外交」</strong>：Apple 同时接入 OpenAI 和 Google，不站队、只择优</li><li><strong>从追赶到军备竞赛</strong>：Google 翻倍投入，AI 基建从 PoC 进入大规模部署</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>如果说上期日报讲的是 AI 经济的「泡沫侧」——2970 亿美元融资、通胀警告、裁员——今天这几条新闻讲的是同一枚硬币的另一面：AI 能力的「质变侧」。而最有趣的张力在于：Morgan Stanley 和美联储在同一个月给出了截然相反的结论。</strong></p><p>Morgan Stanley 说 AI 是「强大的通缩力量」——技术进步降低生产成本、提高效率、最终压低物价。美联储说 AI 是「通胀推手」——对 AI 的狂热预期推高投资、薪资和基础设施成本。谁对？<strong>答案是都对，但时间尺度不同。短期（1-2 年），美联储是对的——AI 投资热潮正在推高一切成本；长期（3-5 年），Morgan Stanley 可能是对的——如果 AI 真的兑现了生产力承诺，通缩效应终将到来。问题是我们正好卡在这个「短期通胀、长期通缩」的交叉点上，两种力量同时在拉扯经济。</strong>这解释了为什么股市和实体经济的感受如此割裂：投资者看到的是 Morgan Stanley 的长期叙事，打工人感受到的是美联储描述的短期现实。</p><p>Apple 的「模型外交」策略值得玩味。先接 OpenAI，再接 Google Gemini，还保留蒸馏权利。<strong>这不是「选择困难症」，这是 Apple 有史以来最精明的平台策略之一：让 AI 模型提供商互相竞争，Apple 永远挑最好的那个。</strong>这和 Adobe 引入第三方模型的逻辑完全一致——昨天日报提到的「AI 模型聚合器」范式正在被最大的平台公司验证。Apple 手握 20 亿设备的分发渠道，任何 AI 模型公司都不敢得罪它。而 OpenAI 与 Jony Ive 合作 AI 硬件设备这条线更有意思：OpenAI 想绕开 Apple 做自己的终端——就像当年 Google 做 Pixel 绕开三星。但 Pixel 的市场份额说明了一切：做硬件和做软件是完全不同的游戏。</p><p>Google 翻倍 AI 投入这条消息放在 Q1 2970 亿融资的背景下看才有意义。Google 不需要融资——它有现金流。但当 OpenAI 拿走 1220 亿、Anthropic 拿走 300 亿时，Google 不可能不加码。<strong>这就是军备竞赛的逻辑：不是因为你需要这么多钱，而是因为你的对手拿了这么多钱。</strong>130 万个 AI 新工作岗位听起来很多，但对比一下：美国每月新增就业约 15-20 万。三年 130 万，平均每月约 3.6 万——大约占新增就业的 20%。这是一个有意义但不是颠覆性的数字。更重要的问题是：这 130 万岗位里有多少是「真正的新工作」，有多少只是把旧工作贴上了「AI」标签？</p><p><strong>我的判断：Morgan Stanley 的「数月内突破」预测可能是对的——但「突破」的定义取决于你站在哪里。如果你在实验室，GPT-5.4 在基准测试上的表现确实令人震撼。如果你在工厂车间或设计工作室，「突破」意味着你的日常工作真的被改变了——而这个传导过程至少还需要 12-18 个月。</strong>2026 年上半年的 AI 故事不会是「突然一切都变了」，而是「底层能力急剧跃升，但应用层、基础设施层和制度层都在拖后腿」。最赚钱的不是做 AI 模型的公司，是帮助企业「消化」AI 能力的公司。</p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Morgan Stanley Warns: AI Mega-Breakthrough 'Months Away'</strong> — March report predicts a \"shock-level\" AI breakthrough in H1 2026. GPT-5.4 approaches human-expert benchmarks. <strong>Core bottleneck isn't algorithms—it's power (9-18GW shortfall), chips, and institutional readiness.</strong> Interestingly, Morgan Stanley sees AI as deflationary, contradicting the Fed's inflation warning from our last issue.<br><small>Source: <a href=\"https://fortune.com/2026/03/13/elon-musk-morgan-stanley-ai-leap-2026/\">Fortune</a></small></li><li><strong>Apple Picks Google Gemini for New Siri</strong> — Apple integrates Gemini alongside OpenAI's ChatGPT in Siri. <strong>Strategy: don't build the best AI model—curate them.</strong> Apple can even \"distill\" Google's large Gemini for on-device use. Meanwhile, OpenAI develops AI hardware with Jony Ive for potential 2026 debut.<br><small>Source: <a href=\"https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html\">CNBC</a></small></li><li><strong>Google Plans to Double AI Spending</strong> — Google doubles down after early AI stumbles, with Gemini now leapfrogging rivals. LinkedIn data: AI created ~1.3M new jobs over 3 years. <strong>AI infrastructure moving from proof-of-concept to mass deployment.</strong><br><small>Source: <a href=\"https://www.nytimes.com/2026/02/04/business/google-earnings-ai.html\">NYT</a>, <a href=\"https://www.reuters.com/technology/artificial-intelligence/artificial-intelligencer-top-ai-themes-that-will-shape-2026-2026-01-15/\">Reuters</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI bottleneck shifts from algorithms to hardware: power, chips, data centers</li><li>Big Tech's \"AI model diplomacy\": Apple plays OpenAI and Google against each other</li><li>From catch-up to arms race: Google doubles spending, AI infra enters mass deployment</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Last issue covered AI economy's bubble side ($297B, inflation, layoffs). Today: the capability side—and the fascinating tension between Morgan Stanley (AI = deflation) and the Fed (AI = inflation).</strong> Both are right on different timescales: short-term (1-2yr) the Fed wins as AI investment inflates everything; long-term (3-5yr) Morgan Stanley may win if productivity gains materialize. We're stuck at the crossover point. Apple's model diplomacy—OpenAI + Gemini + distillation rights—is the smartest platform play: make AI providers compete while you control distribution across 2B devices. Google's doubling down follows arms race logic: not because you need the money, but because your rivals raised it. The 1.3M AI jobs over 3 years (~3.6K/month, ~20% of US monthly job growth) is meaningful but not revolutionary—and how many are genuinely new vs. relabeled? <strong>Morgan Stanley's \"months away\" breakthrough may be real in the lab, but application-layer impact needs 12-18 more months. The real money in 2026 isn't in making AI models—it's in helping organizations digest AI capabilities.</strong></p></div>"
    },
    "cover": images.get("morgan_stanley", ""),
    "sources": [
        {
            "title": {"zh": "Morgan Stanley 警告 AI 突破即将到来", "en": "Morgan Stanley Warns AI Breakthrough Coming in 2026"},
            "url": "https://fortune.com/2026/03/13/elon-musk-morgan-stanley-ai-leap-2026/",
            "image": images.get("morgan_stanley", "")
        },
        {
            "title": {"zh": "Apple 选择 Google Gemini 驱动 AI Siri", "en": "Apple Picks Google Gemini for AI-Powered Siri"},
            "url": "https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html",
            "image": images.get("apple_google", "")
        },
        {
            "title": {"zh": "Google 计划 AI 支出翻倍", "en": "Google Plans to Double AI Spending"},
            "url": "https://www.nytimes.com/2026/02/04/business/google-earnings-ai.html",
            "image": images.get("google_spending", "")
        }
    ]
}

# Load existing issues
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

# Insert new issues at front (design first, then tech)
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

# Write back
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Added 2 new issues. Total: {len(issues)} issues.")
