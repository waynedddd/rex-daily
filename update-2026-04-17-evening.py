# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Issues update — 2026-04-17 evening"""
import json
import urllib.request
import re

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=8)
        html = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
        return m.group(1) if m else ""
    except Exception:
        return ""

# Fetch og:images
urls = {
    "techcrunch_canva": "https://techcrunch.com/2026/04/16/canvas-ai-assistant-can-now-call-various-tools-to-make-designs-for-you/",
    "pymnts_anthropic": "https://www.pymnts.com/artificial-intelligence-2/2026/anthropics-new-design-tool-rivals-adobe-and-figma/",
    "9to5_skills": "https://9to5google.com/2026/04/14/gemini-in-chrome-skills/",
    "ctol_anthropic": "https://www.ctol.digital/news/anthropic-800b-opus-4-7-mythos-openai-ai-race/",
    "decoder_anthropic": "https://the-decoder.com/anthropic-prepares-opus-4-7-and-ai-design-tool-vcs-offer-up-to-800-billion-dollars/",
    "dwarkesh": "https://www.youtube.com/watch?v=Hrbq66XqtCo",
}

print("Fetching og:images...")
images = {}
for k, u in urls.items():
    img = get_og_image(u)
    images[k] = img
    print(f"  {k}: {img[:80] if img else '(none)'}")

new_issues = [
    {
        "date": "2026-04-17",
        "section": "design",
        "title": {
            "zh": "Canva AI 2.0 发布：AI 助手可调用多工具自主完成设计 · Anthropic 发布 AI 设计工具直接对标 Adobe/Figma，股价当日下跌 · Google Chrome 推出 Gemini Skills 让 AI prompt 可复用",
            "en": "Canva AI 2.0: AI Assistant Now Calls Multiple Tools to Auto-Complete Designs · Anthropic's AI Design Tool Directly Targets Adobe/Figma, Stocks Drop · Chrome Launches Gemini Skills for Reusable AI Prompts"
        },
        "content": {
            "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Canva AI 2.0：AI 助手升级为「全能设计 Agent」，可自主调用多工具完成设计</strong> — Canva 4 月 16 日发布 AI 2.0 研究预览版，核心变化是：<strong>AI 助手不再只是回答问题，而是可以规划任务、调用多个工具、自主完成完整设计流程</strong>。你描述需求，AI 自动选择合适的生成工具——图片生成、排版、文案、甚至网站搭建——一次性输出可编辑设计稿。更激进的是，<strong>Canva AI 2.0 接入了 Slack、Gmail、Google Drive、Calendar 和 Zoom</strong>，允许 AI 读取邮件、对话、文件和会议数据来构建上下文。这不再是一个设计工具里的 AI 功能——<strong>这是一个有记忆、有上下文感知能力的设计 Agent</strong>。<br><small>来源：<a href=\"https://techcrunch.com/2026/04/16/canvas-ai-assistant-can-now-call-various-tools-to-make-designs-for-you/\">TechCrunch</a></small></li><li><strong>Anthropic 发布 AI 设计工具：从文字 prompt 生成网站和演示文稿，Figma 股价当日跌 6%</strong> — The Information 4 月 15 日报道，Anthropic 正准备随 Claude Opus 4.7 一同发布一款 AI 设计工具，<strong>可从自然语言 prompt 直接生成网站、落地页和演示文稿</strong>。消息一出，Figma 股价当日下跌 6%、Wix 跌 4.7%、Adobe 跌 2.7%。据报道 Anthropic 已与 Figma 合作，<strong>允许 AI 生成的代码转换为 Figma 可编辑设计文件</strong>。Decrypt 指出，这标志着 Anthropic 从「语言模型提供商」向「全栈 AI 工作室」的战略转型——Claude 不只是写文字，还要设计和部署完整产品。<br><small>来源：<a href=\"https://www.pymnts.com/artificial-intelligence-2/2026/anthropics-new-design-tool-rivals-adobe-and-figma/\">PYMNTS</a>、<a href=\"https://wisdmlabs.com/blog/anthropic-ai-design-tool-claude-opus-4-7-what-changed/\">WisdmLabs</a></small></li><li><strong>Google Chrome 推出 Gemini「Skills」：让 AI prompt 变成可保存、可复用的工作流</strong> — Google 4 月 14 日为 Chrome 桌面版 Gemini 推出「Skills」功能：用户可以<strong>将常用的 AI prompt 保存为 Skill，跨网页一键复用</strong>。例如你经常让 Gemini 在菜谱网站上推荐素食替代品，现在可以保存为一个 Skill，在任何菜谱页面一键执行。Chrome 同时上线了 Skills Library，提供学习、研究、购物、写作等分类的预制 Skill。设计意义：<strong>这是 Google 把 AI 交互从「聊天」推向「可编程工作流」的关键一步</strong>——用户不再只是和 AI 对话，而是在构建自己的 AI 工具库。<br><small>来源：<a href=\"https://arstechnica.com/google/2026/04/google-introduces-skills-in-chrome-to-make-gemini-prompts-instantly-reusable/\">Ars Technica</a>、<a href=\"https://9to5google.com/2026/04/14/gemini-in-chrome-skills/\">9to5Google</a>、<a href=\"https://techcrunch.com/2026/04/14/google-adds-ai-skills-to-chrome-to-help-you-save-favorite-workflows/\">TechCrunch</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 设计工具从「功能」进化为「Agent」</strong>：Canva AI 2.0 可自主规划和调用多工具，不再需要人类逐步指导</li><li><strong>Anthropic 直接进入设计市场</strong>：模型公司不再满足于做底层，开始自己做上层应用，Figma/Adobe 面临降维打击</li><li><strong>AI 交互正在被「可编程化」</strong>：Chrome Skills 把对话式 AI 变成可复用的工作流组件</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天三条设计新闻放在一起，画出了一条清晰的产业演进线：AI 设计正在从「辅助功能」→「自主 Agent」→「可编程工作流」三级跳。而这个跳跃正在同时发生在三个不同的层面。</strong></p><p>Canva AI 2.0 最让我在意的不是它能自动做设计——这已经不新鲜了——而是<strong>它接入了 Slack、Gmail、Calendar 和 Zoom</strong>。这意味着什么？意味着 Canva 的 AI 不只是在设计画布上工作，它在你的<strong>整个工作上下文</strong>里工作。它读你的邮件知道老板要什么、读你的日历知道 deadline 是什么时候、读你的 Slack 知道团队的讨论进展。然后它用这些上下文来做设计决策。这不再是一个「设计工具」，<strong>这是一个有你全部工作记忆的设计 Agent</strong>。对比昨天讨论的 Figma 开放 Agent API——Figma 让外部 AI 进入画布，Canva 让自己的 AI 走出画布进入你的工作流。两种路径，同一个终点：<strong>AI 设计师不再被限制在一个画布里，它需要理解你的完整工作语境</strong>。</p><p>Anthropic 做设计工具这件事，表面上看是一个产品扩张，实际上是 AI 行业权力结构的重大信号。<strong>模型公司开始自己做应用，是因为它们发现自己拥有最根本的竞争优势——模型能力——而应用层的壁垒比想象中薄得多。</strong>Figma 的护城河是什么？是设计师的习惯和协作网络。但如果 AI 可以直接从文字生成可编辑的 Figma 文件（Anthropic 已经和 Figma 合作实现了这一点），那设计师打开 Figma 的频率会不会下降？不是 Figma 变差了，而是<strong>「从零开始在 Figma 里设计」这个动作本身可能变得不必要了</strong>。Figma 当日跌 6% 不是恐慌——是市场在重新评估「设计工具」这个品类在 AI 时代还值多少钱。</p><p>Chrome Gemini Skills 看起来最「小」，但可能影响最深远。<strong>它本质上是在做一件事：让普通用户成为 AI 工具的「开发者」</strong>。以前你要用 AI 做一个重复性工作流，需要懂 API、写脚本、或者至少会用 Zapier。现在你只需要在 Chrome 里对 Gemini 说一次，然后保存为 Skill。这是「无代码 AI 编程」的最直觉化实现。把这和 Canva AI 2.0 对比：Canva 的路径是「AI 自动理解你的需求」，Chrome Skills 的路径是「你教会 AI 你的需求然后复用」。一个是智能推断，一个是用户编程——<strong>最终两者会合流：AI 先推断，用户校准后保存为 Skill，下次 AI 直接执行</strong>。</p><p><strong>把今天的新闻和昨天的 Figma Agent API、Flowstep 排名第一、Anthropic 渗透设计基础设施串起来看：设计行业正在经历一场「去中心化」——设计能力不再集中在 Figma 这样的专业工具里，而是分散到 Chrome 浏览器（Skills）、聊天界面（Canva AI）、甚至直接在 AI 模型里（Anthropic 设计工具）。设计工具的价值正在从「画布」转移到「上下文」——谁能获取最多的用户工作上下文（邮件、日历、代码库、设计系统），谁就能提供最好的 AI 设计体验。这场竞争 Canva 目前领先一步，但 Google（Chrome + Workspace）和 Anthropic（Claude + 全栈能力）都有后发优势。2026 年底，我们可能会回头看今天，意识到这是设计工具行业格局重塑的起点。</strong></p></div>",
            "en": "<h3>📌 AI × Design</h3><ul><li><strong>Canva AI 2.0: AI Assistant Upgrades to 'All-in-One Design Agent' That Autonomously Calls Multiple Tools</strong> — Canva launched AI 2.0 research preview on April 16. The core change: <strong>the AI assistant can now plan tasks, call multiple tools, and autonomously complete entire design workflows</strong>. Describe your needs, and AI automatically selects the right tools — image generation, layout, copy, even website building — producing editable designs in one go. More radically, <strong>Canva AI 2.0 integrates with Slack, Gmail, Google Drive, Calendar, and Zoom</strong>, letting AI read emails, conversations, files, and meeting data for context. This isn't an AI feature in a design tool — <strong>it's a design agent with memory and contextual awareness</strong>.<br><small>Source: <a href=\"https://techcrunch.com/2026/04/16/canvas-ai-assistant-can-now-call-various-tools-to-make-designs-for-you/\">TechCrunch</a></small></li><li><strong>Anthropic Launches AI Design Tool: Generate Websites and Presentations from Text Prompts, Figma Stock Drops 6%</strong> — The Information reported on April 15 that Anthropic is preparing to release an AI design tool alongside Claude Opus 4.7 that <strong>generates websites, landing pages, and presentations from natural language prompts</strong>. On the news, Figma dropped 6%, Wix 4.7%, Adobe 2.7%. Anthropic has reportedly partnered with Figma to <strong>convert AI-generated code into editable Figma design files</strong>. Decrypt notes this signals Anthropic's strategic shift from 'language model provider' to 'full-stack AI studio.'<br><small>Source: <a href=\"https://www.pymnts.com/artificial-intelligence-2/2026/anthropics-new-design-tool-rivals-adobe-and-figma/\">PYMNTS</a>, <a href=\"https://wisdmlabs.com/blog/anthropic-ai-design-tool-claude-opus-4-7-what-changed/\">WisdmLabs</a></small></li><li><strong>Google Chrome Launches Gemini 'Skills': Turning AI Prompts into Reusable Workflows</strong> — Google launched 'Skills' for Chrome desktop Gemini on April 14: <strong>save frequently used AI prompts as Skills, reusable across any webpage with one click</strong>. Chrome also debuted a Skills Library with pre-built prompts for learning, research, shopping, and writing. Design significance: <strong>Google is pushing AI interaction from 'chat' toward 'programmable workflows'</strong> — users aren't just talking to AI, they're building personal AI toolkits.<br><small>Source: <a href=\"https://arstechnica.com/google/2026/04/google-introduces-skills-in-chrome-to-make-gemini-prompts-instantly-reusable/\">Ars Technica</a>, <a href=\"https://9to5google.com/2026/04/14/gemini-in-chrome-skills/\">9to5Google</a>, <a href=\"https://techcrunch.com/2026/04/14/google-adds-ai-skills-to-chrome-to-help-you-save-favorite-workflows/\">TechCrunch</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI design tools evolve from 'features' to 'agents': Canva AI 2.0 autonomously plans and calls multiple tools</li><li>Anthropic enters the design market directly: model companies no longer content as infrastructure, now building applications — Figma/Adobe face disruption from above</li><li>AI interaction becomes 'programmable': Chrome Skills turns conversational AI into reusable workflow components</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Today's three design stories trace a clear industry evolution: AI design is making a triple jump from 'assistive feature' → 'autonomous agent' → 'programmable workflow.' And it's happening simultaneously at three different layers.</strong></p><p>What strikes me most about Canva AI 2.0 isn't the auto-design capability — that's old news — but <strong>its integration with Slack, Gmail, Calendar, and Zoom</strong>. The AI doesn't just work on the design canvas; it works within your <strong>entire work context</strong>. It reads your emails to know what the boss wants, your calendar for deadlines, your Slack for team discussions — then uses all that context for design decisions. Compare with yesterday's Figma Agent API: Figma lets external AI enter the canvas, Canva lets its AI leave the canvas and enter your workflow. Two paths, same destination: <strong>the AI designer can't be confined to a canvas — it needs to understand your full work context</strong>.</p><p>Anthropic building a design tool looks like product expansion but is actually a major signal about AI industry power structures. <strong>Model companies are building applications because they've realized they hold the ultimate competitive advantage — model capability — and the application layer's moat is thinner than imagined.</strong> If AI can generate editable Figma files directly from text (Anthropic has already partnered with Figma for this), will designers open Figma less often? Not because Figma got worse, but because <strong>'designing from scratch in Figma' itself may become unnecessary</strong>. Figma's 6% drop isn't panic — it's the market reassessing how much 'design tools' as a category are worth in the AI era.</p><p>Chrome Gemini Skills looks smallest but may have the deepest impact. <strong>It's essentially making every user an AI tool 'developer.'</strong> Before, repeating an AI workflow required APIs, scripts, or Zapier. Now you tell Gemini once and save it as a Skill. Compare with Canva AI 2.0: Canva's path is 'AI infers your needs,' Chrome Skills' path is 'you teach AI your needs then reuse.' One is intelligent inference, the other is user programming — <strong>ultimately they'll converge: AI infers, user calibrates and saves as Skill, AI executes next time</strong>.</p><p><strong>Connecting today's news with yesterday's Figma Agent API and Anthropic's infrastructure play: design capability is being 'decentralized' — no longer concentrated in professional tools like Figma, but distributed across Chrome browsers (Skills), chat interfaces (Canva AI), and AI models directly (Anthropic design tool). Design tools' value is shifting from 'canvas' to 'context' — whoever captures the most user work context (email, calendar, codebase, design system) delivers the best AI design experience. This may be the starting point of design tool industry restructuring.</strong></p></div>"
        },
        "cover": images.get("techcrunch_canva", ""),
        "sources": [
            {
                "title": {"zh": "Canva AI 助手现可调用多工具为你设计", "en": "Canva's AI Assistant Can Now Call Various Tools to Make Designs for You"},
                "url": "https://techcrunch.com/2026/04/16/canvas-ai-assistant-can-now-call-various-tools-to-make-designs-for-you/",
                "image": images.get("techcrunch_canva", "")
            },
            {
                "title": {"zh": "Anthropic 新 AI 设计工具对标 Adobe 和 Figma", "en": "Anthropic's New Design Tool Rivals Adobe and Figma"},
                "url": "https://www.pymnts.com/artificial-intelligence-2/2026/anthropics-new-design-tool-rivals-adobe-and-figma/",
                "image": images.get("pymnts_anthropic", "")
            },
            {
                "title": {"zh": "Google 为 Chrome Gemini 推出「Skills」可复用 prompt 功能", "en": "Google Announces 'Skills' for Gemini in Chrome to Quickly Run Custom Workflows"},
                "url": "https://9to5google.com/2026/04/14/gemini-in-chrome-skills/",
                "image": images.get("9to5_skills", "")
            },
            {
                "title": {"zh": "Google 在 Chrome 中推出 Skills 让 Gemini prompt 可复用", "en": "Google Introduces Skills in Chrome to Make Gemini Prompts Instantly Reusable"},
                "url": "https://arstechnica.com/google/2026/04/google-introduces-skills-in-chrome-to-make-gemini-prompts-instantly-reusable/",
                "image": ""
            }
        ]
    },
    {
        "date": "2026-04-17",
        "section": "tech",
        "title": {
            "zh": "Anthropic 发布 Claude Opus 4.7 + AI 设计工具，估值飙至 $8000 亿 · Jensen Huang 深度访谈：Nvidia 的护城河还能持续多久？· YC 宣布「机器人的 GPT 时刻已到来」",
            "en": "Anthropic Launches Claude Opus 4.7 + AI Design Tool, Valuation Soars to $800B · Jensen Huang Deep Dive: Will Nvidia's Moat Persist? · YC Declares 'The GPT Moment for Robotics Is Here'"
        },
        "content": {
            "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Anthropic 发布 Claude Opus 4.7 + AI 设计工具，估值一周内从 $3800 亿飙至 $8000 亿</strong> — Anthropic 本周发布了 Claude Opus 4.7 新旗舰模型和一款可从自然语言生成网站/演示文稿的 AI 设计工具。<strong>多家 VC 向 Anthropic 提出投资要约，估值最高达 $8000 亿</strong>——仅 2 个月前 2 月份融资轮估值还是 $3800 亿，翻了一倍多。二级市场平台 Caplight 上 Anthropic 已以 $6880 亿交易，3 个月涨了 75%。关键背景：Opus 4.7 并非 Anthropic 最强模型——Mythos 才是；Opus 4.7 和设计工具是商业层，Mythos 是前沿能力层。Ramp 的 4 月指数显示<strong>企业 AI 采用率首次突破 50%</strong>，Anthropic 以 30.6% 紧追 OpenAI 的 35.2%，在 VC 支持公司和金融行业中已经领先。Bloomberg 报道 OpenAI 目前有 9 亿周活跃用户、5000 万付费订阅。<br><small>来源：<a href=\"https://www.ctol.digital/news/anthropic-800b-opus-4-7-mythos-openai-ai-race/\">CTOL Digital</a>、<a href=\"https://the-decoder.com/anthropic-prepares-opus-4-7-and-ai-design-tool-vcs-offer-up-to-800-billion-dollars/\">The Decoder</a>、<a href=\"https://cryptobriefing.com/anthropic-releases-claude-opus-47-impacting-ai-model-market-standings/\">CryptoBriefing</a></small></li><li><strong>Jensen Huang 深度访谈：Nvidia 的护城河是否能持续？</strong> — Dwarkesh Patel 对 Jensen Huang 的 1 小时 43 分钟深度访谈在 24 小时内获得 28 万播放量。在访谈中 Huang 讨论了 <strong>Nvidia 在 AI 全栈（芯片→系统→软件→生态）的防御策略</strong>，以及物理 AI（机器人和自动驾驶）的未来。结合上周他在斯坦福的演讲中强调「美国 AI 领导力」和与国会议员 Ro Khanna 的讨论，Huang 似乎在为 Nvidia 构建一个超越纯硬件公司的叙事：<strong>Nvidia 不只卖芯片，它是 AI 时代的基础设施操作系统</strong>。<br><small>来源：<a href=\"https://www.youtube.com/watch?v=Hrbq66XqtCo\">Dwarkesh Patel YouTube</a>、<a href=\"https://www.youtube.com/watch?v=tofBqR5N1RI\">Stanford GSB</a></small></li><li><strong>Y Combinator 宣布「机器人的 GPT 时刻已到来」</strong> — YC 发布了一期重磅视频讨论「机器人的 GPT 时刻」，与 Jensen Huang 在 CES 2026 上的类似表态形成呼应。<strong>核心论点：物理 AI 的底层能力（感知、规划、执行）已经跨过可用门槛</strong>，就像 GPT-3.5 之于语言 AI。NVIDIA 的 Isaac Lab 可以同时模拟数千个机器人学习特定任务，Hugging Face 和 NVIDIA 联手将机器人智能开源化。Boston Dynamics 的 Atlas 商用版、NVIDIA 的 GR00T 和 Cosmos 平台开源——<strong>硬件成熟 + 软件民主化 = 机器人产业即将迎来类似 2023 年 LLM 爆发的拐点</strong>。<br><small>来源：<a href=\"https://www.youtube.com/watch?v=4EsUaur0nsQ\">Y Combinator YouTube</a>、<a href=\"https://fortune.com/2026/01/06/nvidia-jensen-huang-chatgpt-moment-for-robotics/\">Fortune</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>Anthropic 估值 2 个月翻倍</strong>：从模型公司到全栈 AI 工作室，市场在为「下一个平台公司」定价</li><li><strong>Nvidia 的叙事升级</strong>：从「卖铲子的」到「AI 时代的 Intel + Microsoft」</li><li><strong>物理 AI 拐点</strong>：YC、Nvidia、Boston Dynamics 同时释放信号，机器人产业进入加速期</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天的科技新闻有一个共同的底层主题：AI 行业正在从「谁的模型最强」的竞争，转向「谁能成为 AI 时代的平台公司」的竞争。而三个不同的玩家正在用三种不同的策略回答这个问题。</strong></p><p>Anthropic 的 $8000 亿估值看起来疯狂，但仔细算一下它的战略布局就会发现市场并非不理性。<strong>Opus 4.7 + AI 设计工具是商业变现层，Mythos 是前沿能力层（网络安全、代码分析），Claude Code + Figma 集成是开发者生态层</strong>。这三层叠在一起意味着 Anthropic 不只是在卖模型——它在构建一个从「创意」到「代码」到「安全」的全链路 AI 平台。和昨天的设计新闻串联起来看：Anthropic 的设计工具让 Figma 跌了 6%，但 Anthropic 同时和 Figma 合作——<strong>这不是要杀死 Figma，而是要让 Figma 成为 Anthropic 生态的一个「渲染层」</strong>。就像 Windows 没有杀死 Word Perfect，但让它变成了操作系统上的一个应用。Anthropic 正在做同样的事：让所有设计工具变成 Claude 生态上的应用。$8000 亿估值本质上是市场在为这个「AI 操作系统」故事付费。</p><p>Jensen Huang 的访谈透露了一个 Nvidia 不太愿意公开承认的焦虑：<strong>纯硬件护城河可能不够</strong>。这就是为什么他不断强调 Nvidia 是「全栈」公司——芯片、系统（DGX）、软件（CUDA、Isaac Lab、Cosmos）、生态（开发者社区）。但现实是 AMD、Intel、以及 Google TPU、Amazon Trainium、Meta MTIA 都在蚕食硬件份额。Nvidia 真正的护城河不是 GPU 性能——<strong>是 CUDA 生态锁定：全球 AI 开发者的代码、工具链、训练流程都深度绑定 CUDA</strong>。这和 x86 指令集锁定了 PC 时代一样。机器人和物理 AI 是 Nvidia 的第二增长曲线——如果它能用 Isaac Lab 和 GR00T 在机器人领域复制 CUDA 在 AI 训练领域的生态锁定，那 Nvidia 的故事还能讲 10 年。</p><p>YC 宣布「机器人的 GPT 时刻」是一个值得认真对待的信号——不是因为 YC 说了，而是因为<strong>底层条件确实已经齐备</strong>。2023 年 LLM 爆发的前提是什么？Transformer 架构成熟 + 训练数据充足 + 推理成本下降。机器人领域现在也在经历同样的三重突破：<strong>感知模型成熟（多模态 AI 可以理解物理世界）+ 模拟训练成熟（Isaac Lab 可以同时模拟数千机器人）+ 硬件成本下降（Atlas 商用版意味着价格开始亲民化）</strong>。但我对「GPT 时刻」这个说法保持一定保留：LLM 的 GPT 时刻之所以能爆发是因为<strong>边际成本接近零——服务一个新用户几乎不需要额外成本</strong>。机器人不一样——每台机器人是物理硬件，有制造成本、物流成本、维护成本。<strong>机器人的「GPT 时刻」可能更像「iPhone 时刻」——不是一夜之间人人都有，而是在特定场景（工厂、仓库、医院）先爆发，然后用 5-10 年渗透到消费市场</strong>。</p><p><strong>把三条线拉在一起：Anthropic 的策略是「成为 AI 操作系统」（控制从创意到部署的全链路），Nvidia 的策略是「成为 AI 基础设施的 Intel+Microsoft」（硬件+软件生态锁定），YC 的信号是「物理 AI 是下一个万亿级市场」。这三个判断其实不矛盾——它们指向同一个结论：2026 年 AI 行业的竞争焦点正在从「模型能力」转移到「平台控制力」。模型能力在收敛（Opus 4.7、GPT-5、Gemini 2 越来越接近），但平台控制力在分化。谁控制开发者生态（Nvidia CUDA）、谁控制应用入口（Anthropic 设计工具）、谁控制硬件标准（机器人领域尚无定论）——这些才是决定未来 10 年 AI 行业格局的真正变量。</strong></p></div>"
        },
        "cover": images.get("ctol_anthropic") or images.get("decoder_anthropic", ""),
        "sources": [
            {
                "title": {"zh": "Anthropic $8000 亿估值周：Opus 4.7、Mythos 与 AI 竞赛", "en": "Anthropic's $800 Billion Week: Opus 4.7, Mythos, and the AI Race"},
                "url": "https://www.ctol.digital/news/anthropic-800b-opus-4-7-mythos-openai-ai-race/",
                "image": images.get("ctol_anthropic", "")
            },
            {
                "title": {"zh": "Anthropic 准备 Opus 4.7 和 AI 设计工具，VC 估值高达 $8000 亿", "en": "Anthropic Prepares Opus 4.7 and AI Design Tool, VCs Offer Up to $800 Billion"},
                "url": "https://the-decoder.com/anthropic-prepares-opus-4-7-and-ai-design-tool-vcs-offer-up-to-800-billion-dollars/",
                "image": images.get("decoder_anthropic", "")
            },
            {
                "title": {"zh": "Jensen Huang 深度访谈：Nvidia 的护城河", "en": "Jensen Huang – Will Nvidia's Moat Persist?"},
                "url": "https://www.youtube.com/watch?v=Hrbq66XqtCo",
                "image": images.get("dwarkesh", "")
            },
            {
                "title": {"zh": "机器人的 GPT 时刻已到来", "en": "The GPT Moment for Robotics Is Here"},
                "url": "https://www.youtube.com/watch?v=4EsUaur0nsQ",
                "image": ""
            }
        ]
    }
]

with open("issues.json", "r") as f:
    data = json.load(f)

data = new_issues + data

with open("issues.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Done. Added {len(new_issues)} issues. Total: {len(data)}")
