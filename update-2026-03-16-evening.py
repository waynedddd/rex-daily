# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-03-16 Evening Update"""
import json
import urllib.request
import re

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        resp = urllib.request.urlopen(req, timeout=10)
        data = resp.read(60000).decode('utf-8', errors='ignore')
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', data, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data, re.I)
        return m.group(1) if m else ""
    except:
        return ""

# Sources
design_sources = [
    {
        "title": {"zh": "NVIDIA GTC 2026: The Creative OS — 以人类想象力为中心的 AI", "en": "NVIDIA GTC 2026: The Creative OS — AI Built With Human Imagination at the Center"},
        "url": "https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-s81778/",
    },
    {
        "title": {"zh": "Forbes: AMI 世界模型、Meta Vibes 创意编辑工具与 AI 创意生态", "en": "Forbes: AMI World Models, Meta Vibes Creative Editing & AI Creative Ecosystem"},
        "url": "https://www.forbes.com/sites/charliefink/2026/03/12/ami-world-model-startup-raises-1-billion-500-million-robotics-raise-youtube-crowned/",
    },
    {
        "title": {"zh": "NVIDIA GTC 2026 官方：AI 的下一步", "en": "NVIDIA GTC 2026: Live Updates on What's Next in AI"},
        "url": "https://blogs.nvidia.com/blog/gtc-2026-news/",
    },
]

tech_sources = [
    {
        "title": {"zh": "TechCrunch: Yann LeCun 的 AMI Labs 融资 10.3 亿美元构建世界模型", "en": "TechCrunch: Yann LeCun's AMI Labs Raises $1.03B to Build World Models"},
        "url": "https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/",
    },
    {
        "title": {"zh": "纽约时报: 前 Meta AI 首席科学家的初创公司估值 35 亿美元", "en": "NYT: Former Meta AI Chief's Startup Valued at $3.5 Billion"},
        "url": "https://www.nytimes.com/2026/03/10/technology/ami-labs-yann-lecun-funding.html",
    },
    {
        "title": {"zh": "MLQ: Meta 准备下一代 Mango 和 Avocado AI 模型", "en": "MLQ: Meta Readies Next-Gen Mango and Avocado AI Models"},
        "url": "https://mlq.ai/news/meta-readies-nextgeneration-mango-and-avocado-ai-models-for-2026-launch/",
    },
    {
        "title": {"zh": "NVIDIA GTC 2026 实时更新", "en": "NVIDIA GTC 2026: Live Updates"},
        "url": "https://blogs.nvidia.com/blog/gtc-2026-news/",
    },
]

# Fetch og:images
print("Fetching og:images...")
for s in design_sources + tech_sources:
    img = get_og_image(s["url"])
    s["image"] = img
    print(f"  {s['url'][:60]}... -> {'found' if img else 'none'}")

design_cover = next((s["image"] for s in design_sources if s["image"]), "")
tech_cover = next((s["image"] for s in tech_sources if s["image"]), "")

design_issue = {
    "date": "2026-03-16",
    "section": "design",
    "title": {
        "zh": "GTC 2026 开幕特辑 · NVIDIA「创意操作系统」愿景 · AI 生成从工具变平台 · Meta Vibes 变身创意编辑器",
        "en": "GTC 2026 Special · NVIDIA's 'Creative OS' Vision · AI Generation Evolves from Tool to Platform · Meta Vibes Becomes Creative Editor"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计（晚间版）</h3><ul><li><strong>NVIDIA GTC 2026 今日开幕：「Creative OS」专场定义 AI 创意工作流的下一个范式</strong> — GTC 2026（3月16-19日，圣何塞）今天正式开幕。在众多 AI 议题中，「The Creative OS: AI Built With Human Imagination at the Center」专场格外值得关注。核心主张：AI 不应该取代创意人的想象力，而应该成为一个「创意操作系统」——可扩展、可控制、以人类想象力为中心。这与当前 AI 设计工具「全自动生成」的叙事形成鲜明对比。NVIDIA 的定位很清楚：它不做设计工具，但它要成为所有 AI 创意工具的底层引擎。<br><small>来源：<a href=\"https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-s81778/\">NVIDIA GTC Creative OS Session</a> | <a href=\"https://blogs.nvidia.com/blog/gtc-2026-news/\">NVIDIA Blog</a></small></li><li><strong>Meta Vibes 从 AI 视频信息流进化为完整创意编辑环境</strong> — Forbes 报道，Meta 正在将其 Vibes 功能从简单的 AI 视频 feed 升级为一个基于 Web 的创意工作室。用户可以创建项目、生成图片和视频、在时间线上组装素材——工具形态类似传统影视后期的节点系统。这意味着 Meta 不只想让用户「消费」AI 内容，还想让他们「生产」AI 内容。结合即将发布的 Mango（图像/视频生成模型），Meta 正在构建一个从生成到编辑的完整创意链路。<br><small>来源：<a href=\"https://www.forbes.com/sites/charliefink/2026/03/12/ami-world-model-startup-raises-1-billion-500-million-robotics-raise-youtube-crowned/\">Forbes</a></small></li><li><strong>GTC 2026 Media & Entertainment 专场：生成式 AI 正在改变所有类型的媒体创作</strong> — GTC 的 Media & Entertainment 赛道涵盖了从影视 VFX 到游戏引擎到实时渲染的全链路 AI 应用。关键信号：AI 不再只是「生成一张图」，而是嵌入到整个创意生产流水线中——从概念设计到资产生成到后期合成。这与今天早上我们讨论的 Prompt-to-UI 工具链形成平行结构：设计领域的 AI 化和影视/游戏领域的 AI 化正在同步发生，共享同一个底层逻辑——人类定义意图，AI 执行生成。<br><small>来源：<a href=\"https://www.nvidia.com/gtc/session-catalog/?industries=Media%20%26%20Entertainment\">GTC Media & Entertainment Sessions</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>从「AI 工具」到「AI 操作系统」</strong>：NVIDIA 的 Creative OS 概念暗示创意工作流的未来不是单点工具，而是一个统一的 AI 平台</li><li><strong>Meta 的创意野心浮出水面</strong>：Vibes 编辑器 + Mango 生成模型 = 消费级 AI 创意平台</li><li><strong>GTC 2026 是创意 AI 的风向标</strong>：硬件（Vera Rubin）+ 软件（Creative OS）+ 模型（Mango）三层叠加</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>GTC 2026 今天开幕，但对设计师来说，最值得关注的不是 Jensen 的主题演讲，而是一个叫「Creative OS」的专场——它可能预示了创意工作流的下一个范式转移。</strong></p><p>让我把今天的信息串起来。早上我们聊了 Prompt-to-UI 三国杀（Figma Make vs Motiff vs Google Stitch），核心结论是「约束生成」比「自由生成」更有价值。现在 NVIDIA 在 GTC 上提出了一个更宏大的框架：AI 应该成为一个「创意操作系统」——不是取代设计师的想象力，而是让想象力可以被「编程」和「执行」。这不是一个新想法，但由 NVIDIA 来说，分量不同。因为 NVIDIA 控制着几乎所有 AI 创意工具的底层算力。当它定义「Creative OS」的愿景时，它实际上在告诉整个创意软件行业：你们的工具应该长成什么样。</p><p>再看 Meta 的动作。Vibes 正在从一个 AI 视频消费功能进化为一个创意编辑环境——时间线、项目管理、多媒体合成。这不是社交媒体功能的迭代，这是 Meta 在悄悄构建一个消费级 Adobe。配合即将发布的 Mango（图像/视频生成模型），Meta 有可能在 2026 年下半年推出一个从「想法→生成→编辑→发布」的完整创意链路，而且完全内嵌在 Instagram/Facebook 生态中。对专业设计师来说这可能不痛不痒，但对千万级的「创意消费者」来说——那些用 Canva 做海报、用 CapCut 剪视频的人——Meta 的工具可能更有吸引力，因为它不需要你离开社交平台。</p><p>把这些信号合在一起看，2026 年的创意 AI 正在分成三个层次：<strong>底层是 NVIDIA 的 Creative OS（算力 + 基础设施），中间层是 Figma/Adobe 等专业工具（约束生成 + 精确控制），顶层是 Meta/抖音等平台（消费级生成 + 社交分发）。</strong>这三层的玩家、用户和价值主张完全不同，但它们共享一个趋势：AI 创意工作流正在从「点状工具」进化为「完整平台」。</p><p>对设计师意味着什么？<strong>你的竞争对手不再只是其他设计师，还包括拿着 Meta Vibes 的普通用户。</strong>当 AI 把创意生产的门槛降到接近零时，设计师的价值必须建立在 AI 做不好的事情上：品牌策略、用户洞察、复杂系统的设计决策。这不是危言耸听——今天 GTC 上 NVIDIA 明确说了，AI 的角色是「执行人类想象力」。问题是：当执行成本趋近于零，谁的想象力更值钱？答案很残酷：是那些有深度专业知识和独特视角的人，不是那些只会操作工具的人。GTC 2026 不只是一个技术会议，它是创意行业权力重组的信号弹。</p></div>",
        "en": "<h3>📌 AI × Design (Evening)</h3><ul><li><strong>NVIDIA GTC 2026 Opens: 'Creative OS' Session Defines Next Paradigm for AI Creative Workflows</strong> — The 'AI Built With Human Imagination at the Center' session argues AI should be a creative operating system — scalable, controllable, human-centered. NVIDIA positions itself as the engine under every AI creative tool.<br><small>Source: <a href=\"https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-s81778/\">NVIDIA GTC</a></small></li><li><strong>Meta Vibes Evolves from AI Video Feed to Full Creative Editing Environment</strong> — Forbes reports Meta is upgrading Vibes into a web-based creative studio with project creation, image/video generation, and timeline-based editing. Combined with the upcoming Mango model, Meta is building a complete create-to-publish pipeline.<br><small>Source: <a href=\"https://www.forbes.com/sites/charliefink/2026/03/12/ami-world-model-startup-raises-1-billion-500-million-robotics-raise-youtube-crowned/\">Forbes</a></small></li><li><strong>GTC Media & Entertainment Track: Generative AI Transforming All Media Creation</strong> — Sessions cover the full pipeline from concept design to asset generation to post-production compositing. AI is embedding into entire creative production chains, not just single outputs.<br><small>Source: <a href=\"https://www.nvidia.com/gtc/session-catalog/?industries=Media%20%26%20Entertainment\">GTC M&E Sessions</a></small></li></ul><h3>🔄 Trends</h3><ul><li>From 'AI tools' to 'AI operating systems': NVIDIA's Creative OS concept signals unified creative platforms</li><li>Meta's creative ambitions surface: Vibes editor + Mango model = consumer AI creative platform</li><li>GTC 2026 as creative AI weathervane: hardware (Vera Rubin) + software (Creative OS) + models (Mango)</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>GTC 2026 opens today, and the most important signal for designers isn't Jensen's keynote — it's a session called 'Creative OS' that may preview the next paradigm shift in creative workflows.</strong></p><p>This morning we discussed the Prompt-to-UI battle (Figma Make vs Motiff vs Google Stitch). Now NVIDIA frames a grander vision: AI as a 'creative operating system' — not replacing imagination but making it programmable and executable. Meta is quietly building a consumer-grade Adobe: Vibes evolving into a timeline-based creative editor, paired with Mango for generation. The 2026 creative AI stack is forming three layers: NVIDIA's Creative OS (compute + infrastructure), Figma/Adobe (professional constrained generation), and Meta/TikTok (consumer generation + social distribution). <strong>For designers: your competition now includes anyone with Meta Vibes. When AI execution cost approaches zero, value concentrates in deep expertise and unique perspective — not tool proficiency. GTC 2026 isn't just a tech conference; it's a signal flare for creative industry power restructuring.</strong></p></div>"
    },
    "cover": design_cover,
    "sources": design_sources,
}

tech_issue = {
    "date": "2026-03-16",
    "section": "tech",
    "title": {
        "zh": "LeCun 离开 Meta 创办 AMI Labs · 10 亿美元种子轮豪赌「世界模型」 · Meta 反击：Mango + Avocado 双模型 · GTC 2026 开幕",
        "en": "LeCun Leaves Meta for AMI Labs · $1B Seed Round Bets on 'World Models' · Meta Strikes Back: Mango + Avocado Dual Models · GTC 2026 Opens"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技（晚间版）</h3><ul><li><strong>Yann LeCun 离开 Meta，创办 AMI Labs，种子轮融资 10.3 亿美元，估值 35 亿</strong> — AI 图灵奖得主 Yann LeCun 在离开 Meta 首席 AI 科学家职位一个月后，创办了 Advanced Machine Intelligence Labs（AMI）。公司方向：构建「世界模型」——能理解和推理物理世界的 AI 系统，而非仅仅预测文本。LeCun 长期批评 LLM 路线的局限性，认为纯语言模型永远无法实现真正的智能。AMI 的 10.3 亿美元种子轮来自美国、欧洲和亚洲投资者，目前仅有十几名员工。总部巴黎，纽约、蒙特利尔和新加坡设有办公室。「世界模型」将成为下一个热词——但 LeCun 认为 AMI 做的是真正不同的事。<br><small>来源：<a href=\"https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/\">TechCrunch</a> | <a href=\"https://www.nytimes.com/2026/03/10/technology/ami-labs-yann-lecun-funding.html\">纽约时报</a> | <a href=\"https://www.hpcwire.com/aiwire/2026/03/11/yann-lecuns-ami-secures-1b-seed-to-develop-ai-world-models/\">HPCwire</a></small></li><li><strong>Meta 反击：Mango（图像/视频生成）和 Avocado（下一代语言模型）双线作战</strong> — 在 LeCun 离开后，Meta 没有停下脚步。代号 Mango 的图像/视频生成模型直接对标 OpenAI Sora，代号 Avocado 的下一代文本模型旨在超越现有 Llama 系列。两个模型均由 Meta Superintelligence Labs 开发（由 Alexandr Wang 领导），计划 2026 上半年发布。Meta 投入 140 亿美元的 AI 基建正在转化为产品：从开源大模型到闭源商业模型，Meta 的策略正在发生微妙转变。<br><small>来源：<a href=\"https://mlq.ai/news/meta-readies-nextgeneration-mango-and-avocado-ai-models-for-2026-launch/\">MLQ</a> | <a href=\"https://www.storyboard18.com/digital/meta-plans-mango-and-avocado-ai-models-for-2026-launch-86286.htm\">Storyboard18</a></small></li><li><strong>NVIDIA GTC 2026 今日开幕：Jensen Huang 主题演讲，Agentic AI、Physical AI、AI for Science 成核心议题</strong> — GTC 2026（3月16-19日，圣何塞）今天正式开幕。核心议题包括 Agentic AI（自主 AI 代理）、Enterprise AI Factory、Physical AI、AI for Science 和 Scaling AI Inference。结合上周确认的 Vera Rubin 量产消息，NVIDIA 正在展示一个完整叙事：硬件（Rubin）+ 平台（CUDA-X）+ 应用（Agentic AI）三位一体。GTC 还首次推出开发者日和黑客松，信号明确——NVIDIA 要从「卖 GPU」转变为「拥有 AI 开发者生态」。<br><small>来源：<a href=\"https://www.nvidia.com/gtc/\">NVIDIA GTC 2026</a> | <a href=\"https://blogs.nvidia.com/blog/gtc-2026-news/\">NVIDIA Blog</a></small></li><li><strong>Kersai 2026 三月 AI 突破汇总：GPT-5.4 超越人类表现，DeepSeek V4 开源万亿参数</strong> — Kersai 的月度汇总指出，2026 年上半年可能出现首个「AGI 临近」的可信声明——不是真正的 AGI，但模型已能在多个专业领域执行专家级任务。GPT-5.4 在真实桌面任务基准上首次超越人类表现。DeepSeek V4：万亿参数、百万 token 上下文窗口、原生多模态（文本/代码/视觉/音频）、开源权重。模型发布速度本身正在成为一个危机——分析师已经跟不上了。<br><small>来源：<a href=\"http://kersai.com/ai-breakthroughs-in-2026-march-update/\">Kersai</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>LLM vs 世界模型：AI 路线之争白热化</strong>：LeCun 用 10 亿美元赌「语言模型是死胡同」</li><li><strong>Meta 的双线策略</strong>：一边开源（Llama），一边闭源（Mango/Avocado），两条腿走路</li><li><strong>GTC 2026 = AI 产业的 CES</strong>：从硬件到软件到应用，NVIDIA 正在定义整个 AI 技术栈</li><li><strong>模型发布速度危机</strong>：GPT-5.4、DeepSeek V4、Gemini 3.1 Pro……行业分析师已经跟不上了</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Yann LeCun 离开 Meta 创办 AMI Labs，拿到 10.3 亿美元种子轮——这不只是一个融资新闻，这是 AI 行业第一次出现真正意义上的「路线分裂」。</strong></p><p>让我解释为什么这件事比表面看起来重要得多。过去三年，AI 行业有一个几乎没有被挑战的共识：规模化语言模型（LLM）是通往 AGI 的主要路径。GPT-4、Claude、Gemini、Llama——所有头部实验室都在同一条赛道上跑。LeCun 是少数公开质疑这条路径的顶级研究者之一，但他在 Meta 内部的异议更多停留在学术讨论层面。现在他用脚投票了。10.3 亿美元、35 亿估值、十几个员工——这是一个赌注：「世界模型」（能理解物理世界因果关系的 AI）比「更大的语言模型」更接近真正的智能。</p><p>Meta 的反应也很耐人寻味。LeCun 走后不久，Meta 就加速了 Mango 和 Avocado 的开发——前者是图像/视频生成模型（对标 Sora），后者是下一代语言模型（超越 Llama）。注意这里的微妙转变：Meta 一直以开源著称（Llama 系列），但 Mango 和 Avocado 至今没有确认是否开源。Meta Superintelligence Labs 由 Alexandr Wang 领导，这个名字意味着 Meta 的 AI 目标已经不再是「最好的开源模型」，而是「超级智能」。当你的目标是 superintelligence 时，完全开源的策略就变得可疑了。</p><p>现在把 GTC 2026 放进来看。NVIDIA 今天开幕的 GTC 议程暴露了一个关键信号：<strong>Agentic AI（自主 AI 代理）是第一优先级。</strong>不是更大的模型，不是更好的基准测试分数，而是「AI 能自主执行复杂任务」。这与 LeCun 的「世界模型」方向有共鸣——要让 AI 真正自主行动，它需要理解物理世界的因果关系，而不只是预测下一个 token。NVIDIA 的 Physical AI 赛道也在说同一件事。</p><p>再加上 Kersai 的汇总：GPT-5.4 在真实桌面任务上超越人类、DeepSeek V4 开源万亿参数、模型发布速度本身成为危机。<strong>2026 年 3 月的 AI 行业正在同时经历两件矛盾的事：LLM 达到了前所未有的能力高峰（GPT-5.4 超人类表现），同时最有影响力的 AI 研究者之一正在公开宣告 LLM 路线的局限性。</strong></p><p><strong>我的判断：这不是非此即彼的选择。</strong>LLM 的能力天花板还没有被真正看到——GPT-5.4 的超人类表现证明 scaling 仍然有效。但 LeCun 的世界模型方向解决的是一个 LLM 确实做不好的问题：物理推理和因果理解。最终的赢家可能是两种方法的融合——用 LLM 处理语言和推理，用世界模型处理物理理解和规划。但在那一天到来之前，AMI Labs 的 10 亿美元赌注正在逼迫整个行业重新审视「更大的 LLM = 更强的 AI」这个假设。这是健康的。当所有人都在同一条赛道上冲刺时，最有价值的事情就是有人敢跑另一条。</p></div>",
        "en": "<h3>📌 AI × Tech (Evening)</h3><ul><li><strong>Yann LeCun Leaves Meta, Founds AMI Labs with $1.03B Seed at $3.5B Valuation</strong> — The Turing Award winner bets on 'world models' — AI that understands physical world causality rather than just predicting text. HQ in Paris, offices in NYC, Montreal, Singapore. Only ~12 employees.<br><small>Source: <a href=\"https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/\">TechCrunch</a> | <a href=\"https://www.nytimes.com/2026/03/10/technology/ami-labs-yann-lecun-funding.html\">NYT</a></small></li><li><strong>Meta Strikes Back: Mango (Image/Video) + Avocado (Next-Gen LLM)</strong> — Post-LeCun, Meta accelerates two new models under Superintelligence Labs. Mango targets OpenAI Sora; Avocado aims to surpass Llama. $14B AI infrastructure investment converting to products. Open-source status unclear.<br><small>Source: <a href=\"https://mlq.ai/news/meta-readies-nextgeneration-mango-and-avocado-ai-models-for-2026-launch/\">MLQ</a></small></li><li><strong>NVIDIA GTC 2026 Opens: Agentic AI, Physical AI, AI for Science as Core Themes</strong> — GTC 2026 (Mar 16-19, San Jose) launches with developer days and hackathons. NVIDIA's narrative: hardware (Vera Rubin) + platform (CUDA-X) + applications (Agentic AI).<br><small>Source: <a href=\"https://www.nvidia.com/gtc/\">NVIDIA GTC</a></small></li><li><strong>March 2026 AI Breakthroughs: GPT-5.4 Surpasses Human Performance, DeepSeek V4 Open-Sources Trillion Parameters</strong> — First credible claims of AGI-adjacent performance expected H1 2026. Model release velocity itself becoming a crisis.<br><small>Source: <a href=\"http://kersai.com/ai-breakthroughs-in-2026-march-update/\">Kersai</a></small></li></ul><h3>🔄 Trends</h3><ul><li>LLM vs World Models: first major route split in AI research, backed by $1B+</li><li>Meta's dual strategy: open-source (Llama) + closed-source (Mango/Avocado)</li><li>GTC 2026 = AI industry's CES: NVIDIA defining the full AI stack</li><li>Model release velocity crisis: analysts can't keep up</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>LeCun's departure from Meta to found AMI Labs isn't just a funding story — it's the first genuine 'route split' in AI's march toward intelligence.</strong></p><p>For three years, the industry consensus has been: scale LLMs = path to AGI. LeCun just bet $1.03B that this is wrong — or at least incomplete. World models that understand physical causality vs. language models that predict tokens. Meta's response is telling: accelerating Mango and Avocado under 'Superintelligence Labs' with unclear open-source commitment. The open-source champion may be pivoting. NVIDIA's GTC opens with Agentic AI as priority #1 — autonomous agents need world understanding, not just text prediction, aligning with LeCun's thesis. Meanwhile, GPT-5.4 surpasses human performance on real-world tasks, proving LLM scaling still works. <strong>The paradox of March 2026: LLMs hit unprecedented capability peaks while the most influential AI researcher publicly declares their limitations. My bet: the winner is convergence — LLMs for language/reasoning, world models for physical understanding. But AMI's $1B forces the industry to question 'bigger LLM = better AI.' That questioning is the most valuable thing happening in AI right now.</strong></p></div>"
    },
    "cover": tech_cover,
    "sources": tech_sources,
}

# Load existing issues and prepend new ones
with open('issues.json', 'r', encoding='utf-8') as f:
    issues = json.load(f)

issues = [design_issue, tech_issue] + issues

with open('issues.json', 'w', encoding='utf-8') as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"Done! Total issues: {len(issues)}")
