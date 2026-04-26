# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            body = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', body, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', body, re.I)
        return m.group(1) if m else ""
    except:
        return ""

# Today's issues
design_sources = [
    {
        "title": {"zh": "2026 创意转折：AI 如何重新定义品牌视觉", "en": "The 2026 Creative Pivot: How AI Is Redefining Brand Visuals"},
        "url": "https://thesiliconreview.com/2026/04/the-2026-creative-pivot-ai-redefining-brand-visuals",
    },
    {
        "title": {"zh": "AI 设计平台如何改变 2026 年的创意工作", "en": "How AI Design Platforms Are Changing Creative Work in 2026"},
        "url": "https://www.techguide.com.au/news/computers-news/how-ai-design-platforms-are-changing-creative-work-in-2026/",
    },
    {
        "title": {"zh": "DREAM MACHINE：2026 年 4 月创意 AI 新闻与洞察", "en": "DREAM MACHINE: Creative AI News & Insight — April 2026"},
        "url": "https://www.linkedin.com/pulse/dream-machine-creative-ai-news-insight-april-2026-issue-woodbridge-5vjuc",
    },
]

tech_sources = [
    {
        "title": {"zh": "2026 年 4 月 AI 突破：模型、融资与行业变局", "en": "AI in April 2026: Biggest Breakthroughs, Models & Industry Shifts"},
        "url": "https://kersai.com/ai-breakthroughs-april-2026-models-funding-shifts/",
    },
    {
        "title": {"zh": "Google Gemma 4：开源模型击败 20 倍体量的商业模型", "en": "Google Gemma 4: Free Open-Source AI That Beats Models 20x Its Size"},
        "url": "https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/",
    },
    {
        "title": {"zh": "Agentic AI 革命：2026 年 4 月重塑科技的 7 大突破", "en": "The Agentic AI Revolution: 7 Breakthroughs Reshaping Tech in April 2026"},
        "url": "https://www.switas.com/articles/the-agentic-ai-revolution-7-breakthroughs-reshaping-tech-in-april-2026",
    },
]

# Fetch og:images
for src_list in [design_sources, tech_sources]:
    for s in src_list:
        img = get_og_image(s["url"])
        s["image"] = img
        print(f"  og:image for {s['url'][:60]}... → {'✓' if img else '✗'}")

design_cover = next((s["image"] for s in design_sources if s["image"]), "")
tech_cover = next((s["image"] for s in tech_sources if s["image"]), "")

design_issue = {
    "date": "2026-04-26",
    "section": "design",
    "title": {
        "zh": "AI 设计平台大洗牌：从「设计师加速器」到「一站式视觉工厂」，PromeAI 模式揭示创意工具的终局形态",
        "en": "AI Design Platform Shakeout: From 'Designer Accelerator' to 'One-Stop Visual Factory' — The PromeAI Model Reveals Creative Tools' Endgame"
    },
    "content": {
        "zh": """<h3>📌 AI × 设计</h3><ul><li><strong>AI 设计平台进入「全栈整合」时代，单功能工具加速淘汰</strong> — TechGuide 的深度评测指出，2026 年 AI 设计平台的竞争已经从「谁能生成更好的图」转向「谁能整合更完整的工作流」。<strong>PromeAI 被点名为品类方向的代表：将草图转渲染、图像编辑、视频生成、风格控制整合到单一 Web 应用中</strong>，而不是让设计师在五个订阅之间来回切换。评测提出 2026 年评估 AI 设计工具的四个关键维度：与实际产出目标的对齐度、编辑能力的深度（不只是生成）、透明的 credit 定价、以及数据安全与商用授权。这标志着「AI 生成」从炫技功能变成了基础设施层。<br><small>来源：<a href="https://www.techguide.com.au/news/computers-news/how-ai-design-platforms-are-changing-creative-work-in-2026/">TechGuide</a></small></li><li><strong>品牌视觉的「软件化」：3/4 营销团队使用 AI 生成视觉资产</strong> — The Silicon Review 报道了一个标志性数据：<strong>四分之三的营销人员现在使用 AI 工具生产视觉内容</strong>，速度已经成为营销团队的新黄金标准。文章指出视觉资产正在从「艺术品」变成「软件」——可以在一个周末内根据市场变化快速迭代整个品牌视觉。这对以手工精品路线为主的设计工作室构成直接威胁。<br><small>来源：<a href="https://thesiliconreview.com/2026/04/the-2026-creative-pivot-ai-redefining-brand-visuals">The Silicon Review</a></small></li><li><strong>创意 AI 渗透游戏与音乐：Roblox AI 助手获 Agentic 工具，Deezer 日拦截 7.5 万首纯 AI 生成歌曲</strong> — LinkedIn 的 DREAM MACHINE 月度创意 AI 汇总揭示了两个惊人信号。<strong>Roblox 的 AI 助手现在可以规划、构建和测试游戏</strong>，从辅助工具升级为 Agentic 开发者。同时，<strong>Deezer 每天识别近 7.5 万首纯 AI 生成的音乐上传，比 2025 年 1 月增长 650%</strong>。NVIDIA 发布 UniRelight 重打光工具，Blender Buddy 为 3D 工作者提供 AI 助手。创意 AI 正在从图像/文本领域溢出到游戏、音乐、3D 全线。<br><small>来源：<a href="https://www.linkedin.com/pulse/dream-machine-creative-ai-news-insight-april-2026-issue-woodbridge-5vjuc">DREAM MACHINE / LinkedIn</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「全栈设计平台」取代「单点工具」</strong>：PromeAI 模式——一个平台覆盖从草图到成片的全流程——正在成为标准</li><li><strong>视觉资产「软件化」</strong>：品牌视觉从一次性创作变成持续迭代的动态资产，设计周期从周缩短到天</li><li><strong>AI 生成内容洪流</strong>：Deezer 日拦截 7.5 万首 AI 歌曲、AI 视觉内容泛滥——质量控制和内容鉴别成为新的稀缺能力</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>PromeAI 模式揭示了一个很多设计师不愿面对的事实：AI 设计工具的终局不是「更好的画笔」，而是「视觉内容的工厂流水线」。</strong></p><p>先说 TechGuide 评测里最有价值的一句话：「评估 AI 设计工具时，要看编辑能力的深度，而不只是生成能力」。这句话暗含的意思是——<strong>纯生成已经不是竞争力了</strong>。2024 年，你能用 AI 生成一张好看的图就很牛。2026 年，生成是默认功能，就像 Word 里的拼写检查。真正的竞争在于：生成之后你能不能精准编辑？能不能保持风格一致？能不能从草图到渲染到视频一条线走完？PromeAI 把这些全塞进一个平台，本质上是在说：<strong>「设计」作为一个需要在多个专业工具之间切换的复杂流程，正在被压缩成一个「输入→输出」的管道</strong>。</p><p>The Silicon Review 的「3/4 营销人员使用 AI 生成视觉」这个数据更值得深思。<strong>当视觉资产变成软件——可快速迭代、可批量生产、可周末翻新——传统设计工作室的商业模式就遇到了结构性挑战</strong>。以前客户找设计工作室做品牌视觉，是因为这活儿需要专业技能和审美判断。现在 AI 把「专业技能」这一层抽掉了，剩下的只有「审美判断」。问题是：有多少客户愿意为纯粹的审美判断付高价？答案可能比设计师们期望的少得多。</p><p>但最让我警觉的是 Deezer 的数据：<strong>每天 7.5 万首纯 AI 生成歌曲，比去年增长 650%</strong>。这不是设计行业的新闻，但它是设计行业的预言。当 AI 生成的音乐多到平台必须专门做检测工具来拦截时，AI 生成的视觉设计离同样的命运有多远？想象一下 Dribbble 或 Behance 如果每天涌入 7.5 万份 AI 生成的作品集——<strong>创意平台的价值不再是「展示作品」而是「鉴别真假」</strong>。</p><p><strong>把这三条新闻连起来看，2026 年创意行业的图景很清晰：生成能力过剩（7.5 万首 AI 歌曲/天），平台在整合（PromeAI 全栈化），用户在迁移（3/4 营销人员已经在用 AI）。在这个环境里，设计师的价值重心正在从「产出」端向「判断」端位移。具体来说：不是你能用 PromeAI 生成多少个方案，而是你能从 100 个 AI 方案里挑出那个真正解决问题的——然后用你的编辑能力把它打磨到位。这是「策展型设计师」的时代，而不是「生产型设计师」的时代。昨天我们说「生成是廉价的，策展才有价值」；今天的数据证明，这个转变正在以超出预期的速度发生。</strong></p></div>""",
        "en": """<h3>📌 AI × Design</h3><ul><li><strong>AI Design Platforms Enter the 'Full-Stack Integration' Era</strong> — TechGuide's review notes 2026 competition has shifted from "who generates better images" to "who integrates more complete workflows." <strong>PromeAI is highlighted as the category direction: bundling sketch-to-render, image editing, video generation, and style control into a single web app</strong>. The review proposes four evaluation criteria: alignment with output goals, editing depth (not just generation), transparent pricing, and data security with commercial rights.<br><small>Source: <a href="https://www.techguide.com.au/news/computers-news/how-ai-design-platforms-are-changing-creative-work-in-2026/">TechGuide</a></small></li><li><strong>Brand Visuals Become 'Software': 3/4 of Marketers Use AI for Visual Assets</strong> — The Silicon Review reports <strong>three-quarters of marketers now use AI tools to produce visual content</strong>. Visual assets are shifting from "art" to "software"—brands can pivot their entire look in a weekend.<br><small>Source: <a href="https://thesiliconreview.com/2026/04/the-2026-creative-pivot-ai-redefining-brand-visuals">The Silicon Review</a></small></li><li><strong>Creative AI Floods Gaming & Music: Roblox AI Gets Agentic Tools, Deezer Intercepts 75K Pure-AI Songs Daily</strong> — DREAM MACHINE's monthly roundup reveals <strong>Roblox's AI assistant can now plan, build, and test games</strong>. Meanwhile, <strong>Deezer identifies nearly 75,000 fully AI-generated music uploads per day, up 650% from January 2025</strong>. NVIDIA released UniRelight, and Blender Buddy brings AI to 3D workflows.<br><small>Source: <a href="https://www.linkedin.com/pulse/dream-machine-creative-ai-news-insight-april-2026-issue-woodbridge-5vjuc">DREAM MACHINE / LinkedIn</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>"Full-stack design platforms" replace "point tools"</strong>: The PromeAI model—one platform covering sketch to final—is becoming standard</li><li><strong>Visual assets become "software"</strong>: Brand visuals shift from one-time creation to continuously iterated dynamic assets</li><li><strong>AI content flood</strong>: 75K AI songs/day on Deezer alone—quality control and content authentication become scarce capabilities</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>The PromeAI model reveals what many designers don't want to face: AI design tools' endgame isn't "a better brush" but "a visual content factory line."</strong></p><p>The most valuable line from TechGuide's review: "evaluate editing depth, not just generation capability." The implication: <strong>pure generation is no longer competitive</strong>. In 2024, generating a good image with AI was impressive. In 2026, generation is a default feature like spell-check. The real competition: can you precisely edit after generation? Maintain style consistency? Go from sketch to render to video in one pipeline?</p><p>The Silicon Review's "3/4 of marketers use AI visuals" deserves deeper thought. <strong>When visual assets become software—rapidly iterable, mass-producible, refreshable over a weekend—traditional design studios face structural business model challenges</strong>. AI removes the "professional skill" layer, leaving only "aesthetic judgment." How many clients will pay premium for pure aesthetic judgment? Probably fewer than designers hope.</p><p>Most alarming: Deezer's data—<strong>75,000 pure-AI songs daily, up 650% YoY</strong>. This isn't design news, but it's design prophecy. When AI music floods platforms enough to require detection tools, how far is AI-generated visual design from the same fate? <strong>Creative platforms' value shifts from "showcasing work" to "authenticating it."</strong></p><p><strong>Connecting all three: 2026's creative landscape is clear—generation capacity is surplus (75K AI songs/day), platforms are consolidating (PromeAI goes full-stack), users are migrating (3/4 marketers already using AI). Designers' value center is shifting from "output" to "judgment." Not how many concepts you can generate with PromeAI, but picking the one that actually solves the problem from 100 AI options—then polishing it with your editing skills. This is the age of the "curator-designer," not the "producer-designer." Yesterday we said "generation is cheap, curation is valuable"; today's data proves this shift is happening faster than expected.</strong></p></div>"""
    },
    "cover": design_cover,
    "sources": design_sources
}

tech_issue = {
    "date": "2026-04-26",
    "section": "tech",
    "title": {
        "zh": "模型大战白热化：Google Gemma 4 开源逆袭、Anthropic 估值 8000 亿、Microsoft 自研三款 MAI 模型宣告「去 OpenAI 化」",
        "en": "Model Wars Intensify: Google Gemma 4 Open-Source Upset, Anthropic at $800B Valuation, Microsoft's Three In-House MAI Models Signal 'De-OpenAI-ification'"
    },
    "content": {
        "zh": """<h3>📌 AI × 科技</h3><ul><li><strong>Google Gemma 4 开源发布：笔记本可运行的模型击败 20 倍体量商业模型</strong> — Google 于 4 月发布 Gemma 4，定位为「迄今最智能的开源模型」。<strong>Gemma 4 可以在笔记本电脑上本地运行，但在多项基准测试中击败了参数量 20 倍于它的商业模型</strong>。这对开源 AI 社区是重大利好，也直接挑战了 OpenAI 和 Anthropic 的付费模型壁垒。Gemma 4 的发布延续了 Google 「开源+云服务」双轨策略：免费模型吸引开发者，再通过 Google Cloud 和 AI Studio 商业化。<br><small>来源：<a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/">Google AI Blog</a>、<a href="https://kersai.com/google-gemma-4-free-open-source-ai-beats-models-20x-its-size-complete-guide-2026/">KersAI</a></small></li><li><strong>Anthropic 估值 8000 亿美元，Claude Mythos 被视为「突破性」模型</strong> — KersAI 综合报道指出，<strong>Anthropic 估值已达 $8000 亿，其最新模型 Claude Mythos 被业内视为「突破性」产品</strong>。同期，GPT-5.4 已发布数周，Gemini 3.1 也在迭代中。AI 模型竞赛进入「多极时代」：OpenAI、Anthropic、Google、xAI 四家同时在最前沿较量。值得注意的是，<strong>Yann LeCun 的 AMI Labs 获得 10.3 亿美元融资</strong>，押注「世界模型」路线，公开宣称现有 LLM 架构是错的——这是 AI 基础研究领域的一次重大赌注。<br><small>来源：<a href="https://kersai.com/ai-breakthroughs-april-2026-models-funding-shifts/">KersAI</a>、<a href="https://kersai.com/yann-lecun-ami-labs-world-models-llms-wrong-complete-guide-2026/">KersAI</a></small></li><li><strong>Microsoft 发布三款自研 MAI 模型，「去 OpenAI 化」信号明确</strong> — Microsoft 悄然发布了三款完全自研的 MAI 系列模型，覆盖转录、语音和图像领域。<strong>这是 Microsoft 首次在核心 AI 能力上绕过 OpenAI 独立交付产品</strong>，被解读为 Microsoft 降低对 OpenAI 依赖的战略信号。结合 Copilot Cowork（能自主完成工作的 AI 助手）的同期发布，Microsoft 正在构建一个「不需要 OpenAI 也能运转」的完整 AI 产品线。<br><small>来源：<a href="https://kersai.com/microsoft-mai-models-2026-transcribe-voice-image-openai-independence/">KersAI</a>、<a href="https://kersai.com/microsoft-copilot-cowork-complete-guide-2026/">KersAI</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>开源模型逼近商业模型</strong>：Gemma 4 证明小参数开源模型可以在实际任务中击败大参数闭源模型，AI 的「免费层」越来越强</li><li><strong>四极争霸</strong>：OpenAI (GPT-5.4) / Anthropic (Claude Mythos) / Google (Gemini 3.1 + Gemma 4) / xAI (Grok) 同时在最前沿</li><li><strong>大公司「去依赖化」</strong>：Microsoft 自研模型、Meta 发布 Muse Spark——大科技公司不再愿意把 AI 核心能力交给第三方</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>4 月的 AI 模型战场有一个被严重低估的故事：不是 GPT-5.4 vs Claude Mythos 的巅峰对决，而是 Google Gemma 4 这个「免费小个子」悄悄改写了游戏规则。</strong></p><p>Gemma 4 能在笔记本上运行，却在基准测试中击败 20 倍体量的模型。这意味着什么？<strong>意味着「AI 能力」正在从「付费服务」变成「免费基础设施」的速度，比任何人预期的都快</strong>。OpenAI 和 Anthropic 的商业模型还在收 $20-200/月的订阅费，Google 直接把一个够用的模型免费塞进你的笔记本。这不是慈善，这是 Google 的经典打法：用免费杀死竞争对手的收入来源，然后在生态层面（Cloud、广告、搜索）变现。Android 对 iOS 做过这件事，Chrome 对 IE 做过，现在 Gemma 对 GPT 也要这样做。</p><p>但更让我感兴趣的是 Microsoft 的「静悄悄的叛变」。<strong>当你最大的投资方和分发伙伴开始自研模型绕过你，这才是 OpenAI 应该真正担心的事——比 Altman 家门口的燃烧弹危险得多</strong>。Microsoft 投了 OpenAI 130 亿美元，现在它说：「谢谢你教会了我，但我现在自己能做了。」MAI 系列覆盖语音、转录、图像——这些都是 OpenAI 的核心商业领域。Copilot Cowork 更是直接和 ChatGPT Enterprise 抢企业客户。这不是「合作伙伴关系的正常演进」，这是一场有计划的「去 OpenAI 化」运动。</p><p>Yann LeCun 拿到 10.3 亿美元押注「世界模型」则是另一个维度的故事。<strong>当一位图灵奖得主公开说「现有 LLM 全错了」并且拿到 10 亿美元来证明这一点，你至少应该留出 10% 的认知空间给这个可能性</strong>。如果 LeCun 是对的，那么今天所有围绕 LLM 构建的工具——包括所有 AI 设计工具、所有 Copilot、所有 ChatGPT wrapper——都建立在一个即将过时的范式上。当然，「如果」是个很大的词，但 10.3 亿美元的赌注说明至少有一群非常聪明的人认真考虑了这个可能性。</p><p><strong>回到设计行业的视角：Gemma 4 的免费可用意味着 AI 设计工具的成本将继续下降——当底层模型免费时，工具层很难收高价。Microsoft 的自研模型意味着 AI 能力的分发将更加碎片化——设计师可能同时面对 Figma (OpenAI)、Adobe (自研)、Canva (多模型) 等完全不同的 AI 后端。而 LeCun 的世界模型赌注则提醒我们：今天我们用来做 AI 设计的技术基座，可能在 5 年内被完全替代。在这个快速变化的环境里，设计师最不应该做的就是把自己绑定到任何单一工具或平台上——保持灵活性，才是最好的生存策略。</strong></p></div>""",
        "en": """<h3>📌 AI × Tech</h3><ul><li><strong>Google Gemma 4 Open-Source Launch: Laptop-Runnable Model Beats Commercial Models 20x Its Size</strong> — Google released Gemma 4 in April, calling it "our most intelligent open model to date." <strong>Gemma 4 runs locally on laptops yet outperforms commercial models with 20x its parameters</strong>. This challenges OpenAI and Anthropic's paid model moats and extends Google's dual-track strategy: free models attract developers, monetized through Google Cloud and AI Studio.<br><small>Source: <a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/">Google AI Blog</a>, <a href="https://kersai.com/google-gemma-4-free-open-source-ai-beats-models-20x-its-size-complete-guide-2026/">KersAI</a></small></li><li><strong>Anthropic Valued at $800B; Claude Mythos Deemed 'Groundbreaking'</strong> — <strong>Anthropic's valuation has reached $800 billion, with Claude Mythos hailed as a breakthrough</strong>. GPT-5.4 has been live for weeks, Gemini 3.1 iterates. The model race enters a "multipolar era": OpenAI, Anthropic, Google, and xAI all competing at the frontier. Meanwhile, <strong>Yann LeCun's AMI Labs raised $1.03 billion</strong> betting on "world models," openly declaring current LLM architectures are wrong.<br><small>Source: <a href="https://kersai.com/ai-breakthroughs-april-2026-models-funding-shifts/">KersAI</a></small></li><li><strong>Microsoft Ships Three In-House MAI Models, Signaling 'De-OpenAI-ification'</strong> — Microsoft quietly released three fully in-house MAI models covering transcription, voice, and image. <strong>This is Microsoft's first time delivering core AI capabilities that bypass OpenAI entirely</strong>. Combined with Copilot Cowork's launch, Microsoft is building a complete AI product line that doesn't need OpenAI.<br><small>Source: <a href="https://kersai.com/microsoft-mai-models-2026-transcribe-voice-image-openai-independence/">KersAI</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>Open-source closes the gap</strong>: Gemma 4 proves small open models can beat large closed ones; AI's "free tier" grows stronger</li><li><strong>Quadripolar competition</strong>: OpenAI / Anthropic / Google / xAI all at the frontier simultaneously</li><li><strong>Big tech "de-dependencies"</strong>: Microsoft's in-house models, Meta's Muse Spark—tech giants won't outsource core AI anymore</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>April's most underrated AI story isn't GPT-5.4 vs Claude Mythos—it's Google Gemma 4, the "free little guy" quietly rewriting the rules.</strong></p><p>Gemma 4 runs on a laptop yet beats models 20x its size on benchmarks. <strong>This means "AI capability" is transitioning from "paid service" to "free infrastructure" faster than anyone expected</strong>. OpenAI and Anthropic charge $20-200/month; Google puts a capable model on your laptop for free. This is Google's classic playbook: kill competitors' revenue with free, then monetize at the ecosystem level. Android did it to iOS, Chrome to IE, now Gemma to GPT.</p><p>More fascinating: Microsoft's "quiet rebellion." <strong>When your biggest investor and distribution partner starts building models that bypass you—that's what OpenAI should truly fear, far more than firebombs</strong>. Microsoft invested $13B in OpenAI and now says: "Thanks for teaching me, but I can do this myself." MAI covers voice, transcription, image—OpenAI's core commercial areas.</p><p>LeCun's $1.03B "world models" bet adds another dimension. <strong>When a Turing Award winner publicly says "all current LLMs are wrong" and gets $1B to prove it, allocate at least 10% of your cognitive space to that possibility</strong>. If he's right, every tool built on LLMs—every AI design tool, every Copilot, every ChatGPT wrapper—sits on a soon-to-be-obsolete paradigm.</p><p><strong>For design: Gemma 4's free availability means AI design tool costs will keep falling. Microsoft's in-house models mean AI capability distribution fragments further. LeCun's bet reminds us today's AI design infrastructure may be fully replaced within 5 years. In this rapidly shifting landscape, designers' worst move is locking into any single tool or platform—flexibility is the best survival strategy.</strong></p></div>"""
    },
    "cover": tech_cover,
    "sources": tech_sources
}

# Read existing issues.json and prepend
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    existing = json.load(f)

# Insert new issues at front (design first, then tech)
existing.insert(0, tech_issue)
existing.insert(0, design_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(existing, f, ensure_ascii=False, indent=2)

print(f"\n✅ issues.json updated: {len(existing)} total issues (2 new for 2026-04-26)")
