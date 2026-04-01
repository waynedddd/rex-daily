# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Update - 2026-04-01"""
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

# Fetch og:images
design_urls = [
    "https://mlq.ai/news/figma-launches-beta-for-ai-agents-to-edit-canvas-directly-using-design-systems/",
    "https://designlab.com/blog/the-brief-3-27-26",
    "https://zeroheight.com/blog/ai-in-design-systems-whats-changing-in-2026/",
]
tech_urls = [
    "https://9to5mac.com/2026/03/24/openai-just-killed-its-sora-ai-video-creation-app/",
    "https://www.latimes.com/business/story/2026-03-31/more-than-half-of-u-s-says-ai-is-likely-to-harm-them",
    "https://www.aol.com/articles/openai-google-workers-back-anthropic-130521128.html",
]

print("Fetching og:images...")
design_images = [get_og_image(u) for u in design_urls]
tech_images = [get_og_image(u) for u in tech_urls]
print(f"Design images: {design_images}")
print(f"Tech images: {tech_images}")

design_issue = {
    "date": "2026-04-01",
    "section": "design",
    "title": {
        "zh": "Figma MCP 开放测试：AI Agent 直接在画布上设计 · 设计系统成为 Agent 的「操作手册」· 设计师角色从「执行者」变为「系统架构师」",
        "en": "Figma MCP Open Beta: AI Agents Design Directly on Canvas · Design Systems Become Agent Playbooks · Designers Shift from Executors to System Architects"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Figma MCP 服务器开放测试：AI Agent 可以直接编辑画布</strong> — Figma 于 3 月 24 日正式开放 MCP（Model Context Protocol）服务器 Beta 版，允许 AI Agent 直接在 Figma 画布上创建和编辑设计。<strong>核心突破：Agent 不再是「生成一张图交给设计师」，而是直接在 Figma 里操作组件、应用设计系统变量、使用 Auto Layout。</strong>首批上线 9 个社区构建的 Skills，包括 /figma-generate-design（从代码库生成组件）、/apply-design-system（自动应用设计系统）、/sync-figma-token（同步设计 Token）。Skills 以 Markdown 文件形式存在，团队可以快速定制，无需工程资源。<br><small>来源：<a href=\"https://mlq.ai/news/figma-launches-beta-for-ai-agents-to-edit-canvas-directly-using-design-systems/\">MLQ.ai</a></small></li><li><strong>设计系统的新角色：从「文档」变成「Agent 的操作手册」</strong> — Figma MCP 最深远的影响是重新定义了设计系统的价值。以前设计系统是给人看的文档，现在是 AI Agent 的执行规范。<strong>Zeroheight 的分析指出，2026 年设计系统的核心竞争力从「覆盖率」转向「机器可读性」——你的设计系统能被 Agent 理解和执行吗？</strong>Token 命名规范、组件 API 清晰度、状态定义完整性——这些以前是「nice to have」的细节，现在直接决定 AI 输出质量。<br><small>来源：<a href=\"https://zeroheight.com/blog/ai-in-design-systems-whats-changing-in-2026/\">Zeroheight</a></small></li><li><strong>Designlab：AI Agent 进入 Figma 对设计教育意味着什么？</strong> — Designlab 在最新一期 The Brief 中分析了 Figma MCP 对设计师培训的影响。<strong>核心观点：设计教育需要从「教工具操作」转向「教系统思维」。</strong>当 Agent 可以执行 80% 的画布操作时，设计师的核心能力不再是「会用 Figma」，而是「能设计出让 Agent 高效执行的系统」。这和软件工程从「写代码」到「设计架构」的演变惊人相似。Designlab 借此推出了 AI for UX Design 课程的限时优惠（4 月 1 日截止）。<br><small>来源：<a href=\"https://designlab.com/blog/the-brief-3-27-26\">Designlab</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>MCP 成为设计工具的新标准</strong>：Figma 开放 MCP 意味着任何 AI Agent 都能接入设计工作流</li><li><strong>设计系统从人读到机读</strong>：Agent 时代，设计系统的质量直接决定 AI 输出质量</li><li><strong>设计师角色升级</strong>：从「在画布上操作」到「为 Agent 设计操作规范」</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Figma MCP 开放测试是 2026 年设计行业最重要的基础设施事件——不是因为 AI 能画画了，而是因为设计工作流的「操作系统」变了。</strong></p><p>让我解释为什么这比上周报道的 figr.design、Google Stitch 那些 AI 原生工具更重要。那些工具本质上还是「AI 替你画」——你说话，它出图，你看了不满意再说一遍。Figma MCP 做的事完全不同：<strong>它让 AI Agent 成为你设计团队的「初级设计师」，在你们已有的设计系统和工作流里干活。</strong>这不是「AI 工具」，这是「AI 同事」。</p><p>关键在 Skills 的设计。Figma 把 Skills 做成 Markdown 文件，这个决策看似简单，实则深思熟虑。Markdown 意味着：1）任何设计师都能写，不需要工程师；2）可以版本控制（Git）；3）可以在团队间共享和复用。<strong>这本质上把「设计团队的隐性知识」——那些存在于 Slack 消息、Notion 文档、甚至老员工脑子里的「我们这里这样做」——变成了 Agent 可执行的指令。</strong>如果你的设计系统够好、Skills 写得够清楚，一个 AI Agent 加入团队第一天就能产出符合规范的设计稿。想想看，一个新入职的设计师需要多久才能做到这一点？</p><p>但这也暴露了一个残酷的现实：大部分团队的设计系统其实是一团糟。Token 命名混乱、组件状态不完整、文档过时——以前这些问题的后果是「新人上手慢一点」，现在的后果是「AI 输出全是垃圾」。Zeroheight 的分析说得对，设计系统的竞争力从「覆盖率」转向「机器可读性」。<strong>我大胆预测：未来 12 个月，「Design System Engineer」将成为设计团队最抢手的角色——不是设计师，不是前端，而是能让设计系统同时对人和 AI 都可用的跨界人才。</strong></p><p>把这和上周的趋势连起来看：figr.design 让设计师退订 Figma，Google Stitch 免费竞争，Figma 的回应不是降价，而是开放 MCP——「你们去做 AI 画图工具吧，我来做 AI 设计的操作系统」。这和 NVIDIA NVLink Fusion 的逻辑一模一样：<strong>不争终端产品，争基础设施标准。</strong>如果所有 AI Agent 都通过 MCP 接入 Figma，那无论你用 Claude、GPT 还是 Gemini 来设计，Figma 都是赢家。这可能是 Dylan Field 面对 AI 原生竞争者的最聪明的一步棋。</p><p>对设计师的实际建议：现在就开始审查你的设计系统。不是为了看起来好看，而是问自己：「如果一个 AI Agent 只看我的 Token、组件和文档，它能做出符合我们品牌的设计吗？」如果答案是否定的，你的设计系统欠了一笔「机器可读性」的技术债。越早还，越主动。</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Figma MCP Server Open Beta: AI Agents Can Edit Canvas Directly</strong> — Figma launched the open beta of its MCP (Model Context Protocol) server on March 24, enabling AI agents to create and edit designs directly on the Figma canvas. <strong>Key breakthrough: agents no longer \"generate an image and hand it to a designer\"—they operate components, apply design system variables, and use Auto Layout natively in Figma.</strong> Nine community-built Skills launched alongside, including /figma-generate-design, /apply-design-system, and /sync-figma-token. Skills are Markdown files that teams can customize without engineering resources.<br><small>Source: <a href=\"https://mlq.ai/news/figma-launches-beta-for-ai-agents-to-edit-canvas-directly-using-design-systems/\">MLQ.ai</a></small></li><li><strong>Design Systems' New Role: From Documentation to Agent Playbooks</strong> — Figma MCP redefines design system value. Previously human-readable docs, design systems now serve as AI agent execution specs. <strong>Zeroheight's analysis: in 2026, design system competitiveness shifts from \"coverage\" to \"machine readability\"—can your agent understand and execute your system?</strong> Token naming, component API clarity, and state completeness now directly determine AI output quality.<br><small>Source: <a href=\"https://zeroheight.com/blog/ai-in-design-systems-whats-changing-in-2026/\">Zeroheight</a></small></li><li><strong>Designlab: What AI Agents in Figma Mean for Design Education</strong> — Designlab's latest Brief analyzes Figma MCP's impact on training. <strong>Core argument: design education must shift from \"teaching tool operations\" to \"teaching systems thinking.\"</strong> When agents handle 80% of canvas operations, the designer's core skill becomes designing systems that agents can execute efficiently—mirroring software engineering's evolution from coding to architecture.<br><small>Source: <a href=\"https://designlab.com/blog/the-brief-3-27-26\">Designlab</a></small></li></ul><h3>🔄 Trends</h3><ul><li>MCP becomes the new standard for design tools: any AI agent can plug into design workflows</li><li>Design systems shift from human-readable to machine-readable</li><li>Designer role upgrade: from \"operating on canvas\" to \"designing operation specs for agents\"</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Figma MCP open beta is 2026's most important design infrastructure event—not because AI can draw, but because the \"operating system\" of design workflows has changed.</strong> This matters more than figr.design or Google Stitch because those tools are still \"AI draws for you.\" Figma MCP makes AI agents your team's \"junior designer,\" working within your existing design systems. The Skills-as-Markdown design is deceptively brilliant: any designer can write them, they're version-controllable, and they encode tribal knowledge into executable instructions. An AI agent with good Skills can produce on-brand designs on day one—something that takes a human designer weeks. But this exposes a brutal truth: most teams' design systems are a mess. Sloppy tokens, incomplete states, outdated docs—previously this meant slow onboarding; now it means garbage AI output. <strong>Prediction: \"Design System Engineer\" will be the hottest design team role in the next 12 months.</strong> Figma's strategy is clear: let others build AI drawing tools; Figma becomes the OS for AI design. Same logic as NVIDIA's NVLink: don't compete on endpoints, compete on infrastructure standards. If all AI agents connect through Figma MCP, Figma wins regardless of which model you use. Dylan Field's smartest move yet.</p></div>"
    },
    "cover": design_images[0] if design_images[0] else "https://mlq.ai/content/images/2026/03/figma-mcp-agents.png",
    "sources": [
        {
            "title": {"zh": "Figma MCP 服务器开放 Beta：AI Agent 直接编辑画布", "en": "Figma MCP Server Open Beta: AI Agents Edit Canvas Directly"},
            "url": "https://mlq.ai/news/figma-launches-beta-for-ai-agents-to-edit-canvas-directly-using-design-systems/",
            "image": design_images[0]
        },
        {
            "title": {"zh": "Designlab：AI Agent 现在可以在 Figma 中设计", "en": "Designlab: AI Agents Can Now Design in Figma"},
            "url": "https://designlab.com/blog/the-brief-3-27-26",
            "image": design_images[1]
        },
        {
            "title": {"zh": "Zeroheight：2026 年设计系统中的 AI 变革", "en": "Zeroheight: AI in Design Systems 2026"},
            "url": "https://zeroheight.com/blog/ai-in-design-systems-whats-changing-in-2026/",
            "image": design_images[2]
        }
    ]
}

tech_issue = {
    "date": "2026-04-01",
    "section": "tech",
    "title": {
        "zh": "OpenAI 砍掉 Sora 专注超级应用 · 55% 美国人认为 AI 弊大于利 · OpenAI/Google 员工联名支持 Anthropic 对抗五角大楼",
        "en": "OpenAI Kills Sora for Super App Focus · 55% Americans Say AI Will Harm Them · OpenAI/Google Workers Back Anthropic vs Pentagon"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>OpenAI 砍掉 Sora，Disney 10 亿美元交易泡汤</strong> — OpenAI 于 3 月 24 日宣布关停 Sora 视频生成应用，分两阶段执行：App 和网页版 4 月 26 日关闭，API 9 月 24 日关闭。<strong>这直接终结了三个月前与 Disney 签署的 10 亿美元合作——Disney 角色进入 Sora 用户生成视频。</strong>Sora 上线六个月，据 Appfigures 估计仅产生约 210 万美元应用内购收入。TechCrunch 评价其为「你手机里最诡异的 App」，因为 deepfake 防护极易被绕过。OpenAI 将资源转向「超级应用」战略——整合 ChatGPT、Codex 和 Atlas 浏览器。研究团队则转向机器人领域的世界模拟研究。<br><small>来源：<a href=\"https://9to5mac.com/2026/03/24/openai-just-killed-its-sora-ai-video-creation-app/\">9to5Mac</a>、<a href=\"https://www.reuters.com/technology/openai-set-discontinue-sora-video-platform-app-wsj-reports-2026-03-24/\">Reuters</a>、<a href=\"https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/\">The Decoder</a></small></li><li><strong>55% 美国人认为 AI 弊大于利，比去年增长 11 个百分点</strong> — LA Times 3 月 31 日报道，最新民调显示 55% 的美国人认为 AI 对日常生活弊大于利，<strong>这一比例较去年 4 月上升了 11 个百分点。</strong>结合 Pew Research 3 月 12 日发布的数据：50% 美国成年人对 AI 在日常生活中的增加「更担忧而非兴奋」；43% 认为 AI 对自己的伤害大于帮助。同时，21% 的美国工人表示工作中使用 AI（较 2024 年的 16% 上升），64% 的美国青少年使用过 AI 聊天机器人。<strong>公众情绪和实际使用之间的鸿沟正在扩大——人们一边用着 AI，一边对它越来越恐惧。</strong><br><small>来源：<a href=\"https://www.latimes.com/business/story/2026-03-31/more-than-half-of-u-s-says-ai-is-likely-to-harm-them\">LA Times</a>、<a href=\"https://www.pewresearch.org/short-reads/2026/03/12/key-findings-about-how-americans-view-artificial-intelligence/\">Pew Research</a></small></li><li><strong>OpenAI 和 Google 员工联名支持 Anthropic 对抗五角大楼</strong> — AOL/Reuters 报道，OpenAI 和 Google 的 AI 研究员联名声明支持 Anthropic 拒绝向军方无限制开放 Claude 的立场。<strong>这在 AI 行业形成了罕见的「竞争对手联合」局面——三大 AI 公司的员工站在同一边，反对五角大楼的「供应链风险」报复。</strong>Fortune 的深度分析指出，这场争端揭示了 AI 治理中「工业俘获」的风险：少数公司和官员决定了 AI 的构建和部署方式，而安全性取决于他们之间的激励和竞争关系。<br><small>来源：<a href=\"https://www.aol.com/articles/openai-google-workers-back-anthropic-130521128.html\">AOL/Reuters</a>、<a href=\"https://fortune.com/2026/03/05/anthropic-openai-feud-pentagon-dispute-ai-safety-dilemma-personalities/\">Fortune</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>OpenAI 从「什么都做」转向「超级应用」</strong>：砍掉 Sora 是 OpenAI 战略聚焦的信号</li><li><strong>AI 公众信任危机加深</strong>：使用率上升 + 信任度下降 = 一个不稳定的方程</li><li><strong>AI 安全的行业共识正在形成</strong>：竞争对手员工联名，五角大楼成了 AI 行业的公敌</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天三条新闻画出了一幅 AI 行业的全景图：产品层在收缩，公众信任在崩塌，而行业内部正在形成一种前所未有的团结。</strong></p><p>先说 Sora 之死。六个月，210 万美元收入，10 亿美元 Disney 合作泡汤——这不是产品失败，这是战略试错。OpenAI 试图成为「AI 时代的 TikTok」，结果发现自己既搞不定内容审核（deepfake 防护形同虚设），也搞不定用户增长（人们用 ChatGPT 是因为它有用，用 Sora 只是因为好奇）。<strong>Sam Altman 现在在做的事是 Meta 在 2022 年做过的：砍掉元宇宙式的登月项目，回归核心产品。</strong>「超级应用」战略——ChatGPT + Codex + Atlas 浏览器——本质上是 WeChat 模式：一个入口，所有功能。这在中国被证明有效，但美国用户对超级应用的接受度一直存疑。不过至少方向对了：OpenAI 的护城河不在视频生成（那是个红海），而在对话交互（那是它的蓝海）。</p><p>55% 美国人认为 AI 弊大于利，这个数字必须放在上下文中看。一年前是 44%，11 个百分点的增长不是渐进式的——是加速的。<strong>更有意思的数据是：21% 的工人在用 AI 工作（较去年增长 31%），64% 的青少年用过 AI 聊天机器人。使用率在涨，恐惧也在涨。</strong>这和社交媒体的轨迹完全一致：人们一边骂 Instagram 毁了青少年心理健康，一边每天花 2 小时刷 Reels。「明知有害，但停不下来」——这不是理性决策，这是成瘾行为的特征。上周 Stanford 那篇谄媚 AI 的研究现在有了更大的画布：AI 不只是在让个体用户变得更自私，它正在制造一个社会级别的信任危机。</p><p>最后，OpenAI 和 Google 员工联名支持 Anthropic 这件事，表面上看是「行业团结」，实际上是 AI 公司集体意识到了一个生存威胁：<strong>如果政府可以通过「供应链风险」标签惩罚任何拒绝合作的 AI 公司，那今天是 Anthropic，明天可能是 OpenAI，后天是 Google。</strong>这不是利他主义，这是「唇亡齿寒」。把它和加州上周的行政令放在一起看，一个更大的格局浮现了：AI 行业正在形成一个松散但有效的联盟，抵抗政府对 AI 公司的政治性控制。这可能是 AI 行业从「内部混战」走向「对外统一战线」的转折点。对 Wayne 来说，值得关注的是：这种联盟能持续多久？当 Anthropic 和 OpenAI 在模型层血拼的同时在政策层握手，这种「竞合关系」的平衡点在哪里？</p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>OpenAI Kills Sora, Disney's $1B Deal Collapses</strong> — OpenAI announced Sora's shutdown on March 24 in two stages: app/web closing April 26, API closing September 24. <strong>This directly ends the $1B Disney partnership signed three months ago.</strong> Sora generated ~$2.1M in six months. TechCrunch called it \"the creepiest app on your phone\" due to easily bypassed deepfake guardrails. OpenAI pivots to a \"super app\" strategy—merging ChatGPT, Codex, and Atlas browser. Research shifts to world simulation for robotics.<br><small>Source: <a href=\"https://9to5mac.com/2026/03/24/openai-just-killed-its-sora-ai-video-creation-app/\">9to5Mac</a>, <a href=\"https://www.reuters.com/technology/openai-set-discontinue-sora-video-platform-app-wsj-reports-2026-03-24/\">Reuters</a></small></li><li><strong>55% of Americans Say AI Will Do More Harm Than Good, Up 11 Points</strong> — LA Times reports the latest poll shows 55% of Americans believe AI will harm daily life more than help, <strong>up 11 percentage points from April 2025.</strong> Meanwhile, 21% of workers use AI at work (up from 16%), and 64% of teens have used AI chatbots. <strong>The gap between usage and trust is widening—people fear AI more even as they use it more.</strong><br><small>Source: <a href=\"https://www.latimes.com/business/story/2026-03-31/more-than-half-of-u-s-says-ai-is-likely-to-harm-them\">LA Times</a>, <a href=\"https://www.pewresearch.org/short-reads/2026/03/12/key-findings-about-how-americans-view-artificial-intelligence/\">Pew Research</a></small></li><li><strong>OpenAI and Google Workers Back Anthropic Against Pentagon</strong> — AI researchers from OpenAI and Google jointly support Anthropic's refusal to give the military unrestricted Claude access. <strong>A rare \"competitor solidarity\" moment—employees from the three biggest AI companies united against the Pentagon's retaliatory \"supply chain risk\" label.</strong> Fortune analysis warns of \"industrial capture\" risk in AI governance.<br><small>Source: <a href=\"https://www.aol.com/articles/openai-google-workers-back-anthropic-130521128.html\">AOL/Reuters</a>, <a href=\"https://fortune.com/2026/03/05/anthropic-openai-feud-pentagon-dispute-ai-safety-dilemma-personalities/\">Fortune</a></small></li></ul><h3>🔄 Trends</h3><ul><li>OpenAI pivots from \"do everything\" to \"super app\": Sora's death signals strategic focus</li><li>AI public trust crisis deepens: rising usage + falling trust = unstable equation</li><li>Industry consensus on AI safety forming: competitor employees unite, Pentagon becomes AI industry's common adversary</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Today's three stories paint a panoramic view of AI: products contracting, public trust collapsing, and unprecedented industry unity forming.</strong> Sora's death ($2.1M revenue, $1B Disney deal destroyed) isn't product failure—it's strategic course correction. OpenAI tried to be \"AI TikTok\" and failed at content moderation and retention. The super app pivot (ChatGPT + Codex + Atlas) follows the WeChat model. The 55% anti-AI sentiment (up 11 points) must be read alongside rising usage: 21% of workers using AI, 64% of teens on chatbots. People fear AI more while using it more—the same pattern as social media. Combined with last week's Stanford sycophancy study, AI is creating a society-level trust crisis. The OpenAI/Google employee solidarity with Anthropic isn't altruism—it's survival instinct. If the Pentagon can punish any AI company via \"supply chain risk\" labels, today's Anthropic is tomorrow's OpenAI. <strong>The bigger picture: AI industry is forming a loose alliance against political control, shifting from internal competition to united external front. How long this \"compete on models, cooperate on policy\" balance holds is the key question.</strong></p></div>"
    },
    "cover": tech_images[0] if tech_images[0] else "https://9to5mac.com/wp-content/uploads/sites/6/2026/03/openai-sora-shutdown.jpg",
    "sources": [
        {
            "title": {"zh": "OpenAI 关停 Sora 视频应用", "en": "OpenAI Kills Sora Video App"},
            "url": "https://9to5mac.com/2026/03/24/openai-just-killed-its-sora-ai-video-creation-app/",
            "image": tech_images[0]
        },
        {
            "title": {"zh": "55% 美国人认为 AI 弊大于利", "en": "55% Americans Say AI Will Harm Them"},
            "url": "https://www.latimes.com/business/story/2026-03-31/more-than-half-of-u-s-says-ai-is-likely-to-harm-them",
            "image": tech_images[1]
        },
        {
            "title": {"zh": "OpenAI/Google 员工联名支持 Anthropic", "en": "OpenAI/Google Workers Back Anthropic"},
            "url": "https://www.aol.com/articles/openai-google-workers-back-anthropic-130521128.html",
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

print("Done! Added 2 issues for 2026-04-01")
