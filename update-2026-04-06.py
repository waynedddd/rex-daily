# -*- coding: utf-8 -*-
"""Rex Daily Digest - 2026-04-06"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        resp = urllib.request.urlopen(req, timeout=10)
        data = resp.read(100000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', data, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data, re.I)
        return html.unescape(m.group(1)) if m else ""
    except:
        return ""

# Fetch og:images
urls = {
    "nng": "https://www.nngroup.com/articles/ai-design-tools-update-2/",
    "figma_make": "https://www.figma.com/solutions/ai-design-generator/",
    "uxdi": "https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/",
    "ms_models": "https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/",
    "apple50": "https://www.techbrew.com/stories/2026/04/01/apple-turns-50-ai-strategy",
    "ms_venturebeat": "https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google",
}

print("Fetching og:images...")
images = {}
for k, u in urls.items():
    img = get_og_image(u)
    images[k] = img
    print(f"  {k}: {img[:80] if img else '(none)'}")

design_issue = {
    "date": "2026-04-06",
    "section": "design",
    "title": {
        "zh": "NN/g 最新报告：AI 设计工具「只是略微好了一点」——窄范围功能才是真正有用的 · Figma Make 全面开放：AI 原生设计工具进入主流 · 2026 年 AI UX 工具全景：9 大工具实测",
        "en": "NN/g Report: AI Design Tools Are 'Marginally Better' — Narrow-Scope Features Win · Figma Make Goes Mainstream · 2026 AI UX Tools Landscape: 9 Tools Tested"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul><li><strong>NN/g 最新报告：AI 设计工具「只是略微好了一点」——窄范围功能才是真正被设计师采用的</strong> — Nielsen Norman Group 发布了对 AI 设计工具的最新评估报告，标题直接就是「Marginally Better」。核心发现：<strong>设计师在日常工作中真正采用的 AI 功能，几乎都是「窄范围」的——专注于完成一个具体任务的工具</strong>，比如自动填充文案、生成配色方案、批量重命名图层。而那些号称能「一句话生成完整界面」的广范围 AI 工具？线框图和原型生成「仍需改进」。这是 NN/g 2024 年「AI 设计工具尚未准备好」报告的后续跟进，结论是：一年过去了，进步有限。<br><small>来源：<a href="https://www.nngroup.com/articles/ai-design-tools-update-2/">NN/g</a></small></li><li><strong>Figma Make 全面开放：AI 原生设计工具正式进入 Figma 主产品线</strong> — Figma 的 AI 设计生成器 Figma Make 现在可以在几分钟内创建完整的设计和视觉资产——从营销页面到产品仪表盘到移动端界面。Make 原型可以嵌入到 Figma Design、FigJam 和 Figma Slides 中。Figma 还发布了「约束烹饪」框架：<strong>结构化 prompt 可以把 AI 从「碰运气」变成「可靠的设计伙伴」</strong>。Figma Make 甚至已向 Figma for Government 开放，支持政府团队加速公共服务现代化。<br><small>来源：<a href="https://www.figma.com/solutions/ai-design-generator/">Figma</a></small></li><li><strong>UX Design Institute 实测 2026 年 9 大 AI UX 工具：Figma、ChatGPT、Miro、Dovetail 等</strong> — UX Design Institute 发布了 2026 年 AI UX 工具全景报告，覆盖 Figma、ChatGPT、Notion、Miro、Dovetail、Maze、Stark、Attention Insight 等 9 个工具。核心观点：<strong>AI 不会取代 UX 设计师，但会深刻改变工作流的每一环节。</strong>最有趣的趋势是 AI 在可访问性测试（Stark）和注意力预测（Attention Insight）这些「非创意」环节的渗透比创意生成环节更成功。华尔街也在押注 Figma 的 AI 未来。<br><small>来源：<a href="https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/">UX Design Institute</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>窄范围 > 广范围</strong>：NN/g 数据证实，设计师真正采用的 AI 是「做一件事做好」的工具，不是「万能生成器」</li><li><strong>Figma 的 AI 全家桶</strong>：Make + Design + FigJam + Slides = AI 贯穿设计全流程</li><li><strong>AI 在「非创意」环节更成功</strong>：可访问性、注意力预测、用户测试分析比「生成 UI」更实用</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>NN/g 的这份报告是我今年读到的最诚实的 AI 设计工具评估——没有之一。「Marginally Better」这个标题本身就是对整个行业炒作的一记耳光。</strong></p><p>让我把这和前几期的内容串起来。上期我们聊了 Figma 向 AI Agent 开放画布、Vibe Coding 工具爆发、设计民主化加速。那些是「供给侧」的故事——工具越来越多、越来越强。但 NN/g 的报告讲的是「需求侧」的真相：<strong>设计师在日常工作中真正用起来的 AI 功能，几乎都是最不性感的那些——自动填充、批量操作、文案生成。</strong>不是什么「一句话出界面」，不是什么「Agent 自动设计」。这个落差说明什么？说明 AI 设计工具的「Demo 效果」和「日常可用性」之间还有一条巨大的鸿沟。</p><p>NN/g 特别指出「窄范围功能最有用」，这和软件工程领域的经验完全一致。GitHub Copilot 最成功的不是「生成整个项目」，而是「自动补全当前行」。Cursor 最强的不是「一键出 app」，而是在具体上下文里精准完成代码片段。<strong>AI 在专注、有约束的任务上表现优异，在开放、模糊的创意任务上仍然拉胯。这不是暂时的技术限制——这是 AI 作为工具的本质特征。</strong></p><p>但这恰恰是好消息。为什么？因为这意味着<strong>设计师的判断力、品味和战略思维不会在短期内被替代。</strong>AI 能帮你快速填充 200 个占位符文案、生成 10 套配色方案、自动检测可访问性问题——这些「苦力活」被自动化了。但决定哪套配色方案最能传达品牌情感？这需要人类设计师。UX Design Institute 的报告印证了这一点：AI 在可访问性测试和注意力预测上比在 UI 生成上更成功，因为前者是有明确标准的分析任务，后者是需要审美判断的创意任务。</p><p>再看 Figma Make 的策略。Figma 没有把 Make 定位为「取代设计师的 AI」，而是「设计师的 AI 助手」——嵌入现有工作流、提供起点而非终点。「约束烹饪」框架更有意思：它本质上是在教设计师如何<strong>给 AI 设定正确的约束条件</strong>，而不是无脑丢一个 prompt 等结果。这呼应了上期的观点——<strong>未来设计师的核心技能是「定义标准」和「设定约束」</strong>，AI 在约束内执行。</p><p><strong>我的判断：NN/g 的「marginally better」不是坏消息，而是一个健康的现实校准。AI 设计工具的真正价值不在于取代设计师的创意判断，而在于消除工作流中的摩擦——那些重复、机械、有明确标准的任务。2026 年最成功的设计团队不是「用 AI 最多」的团队，而是「知道什么时候用 AI、什么时候不用」的团队。窄范围 AI 的胜利告诉我们：工具的价值在于做好一件事，不是承诺做好所有事。这个教训不仅适用于 AI 设计工具，也适用于整个 AI 产品设计领域。</strong></p></div>',
        "en": '<h3>📌 AI × Design</h3><ul><li><strong>NN/g Latest Report: AI Design Tools Are "Marginally Better" — Narrow-Scope Features Are What Designers Actually Adopt</strong> — Nielsen Norman Group published their latest assessment, titled plainly "Marginally Better." Core finding: <strong>AI features designers actually use daily are almost always "narrow-scoped" — tools focused on completing one specific task</strong>, like auto-filling copy, generating color palettes, or batch-renaming layers. Broad-scope "generate a full interface from a prompt" tools? Wireframe and prototype generation "still need work." This follows NN/g\'s 2024 "not ready for primetime" report, and the conclusion: a year later, progress is limited.<br><small>Source: <a href="https://www.nngroup.com/articles/ai-design-tools-update-2/">NN/g</a></small></li><li><strong>Figma Make Goes Mainstream: AI-Native Design Tool Fully Integrated Into Figma\'s Product Suite</strong> — Figma\'s AI design generator Figma Make now creates polished designs and visual assets in minutes — from marketing pages to product dashboards to mobile flows. Make prototypes can be embedded into Figma Design, FigJam, and Figma Slides. Figma also published a "Cooking with Constraints" framework: <strong>structured prompts turn AI from guesswork into a reliable design partner.</strong> Figma Make is now available in Figma for Government.<br><small>Source: <a href="https://www.figma.com/solutions/ai-design-generator/">Figma</a></small></li><li><strong>UX Design Institute Tests 9 AI UX Tools in 2026: Figma, ChatGPT, Miro, Dovetail & More</strong> — Comprehensive landscape report covering Figma, ChatGPT, Notion, Miro, Dovetail, Maze, Stark, and Attention Insight. Core thesis: <strong>AI won\'t replace UX designers but will reshape every stage of the workflow.</strong> Most interesting trend: AI penetrates "non-creative" tasks like accessibility testing (Stark) and attention prediction (Attention Insight) more successfully than creative generation.<br><small>Source: <a href="https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/">UX Design Institute</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Narrow > Broad: NN/g data confirms designers adopt AI that "does one thing well," not "universal generators"</li><li>Figma\'s AI suite: Make + Design + FigJam + Slides = AI across the full design workflow</li><li>AI succeeds more in "non-creative" tasks: accessibility, attention prediction, and user testing analysis outperform UI generation</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>NN/g\'s report is the most honest AI design tool assessment I\'ve read this year. "Marginally Better" as a title is a slap in the face to the entire industry\'s hype machine.</strong> Let me connect this to recent issues. Last time we covered Figma opening its canvas to AI agents, vibe coding tools exploding, and design democratization accelerating — all supply-side stories about tools getting more powerful. But NN/g tells the demand-side truth: <strong>the AI features designers actually use daily are the least sexy ones — auto-fill, batch operations, copy generation.</strong> Not "generate UI from a sentence." The gap between "demo effect" and "daily usability" remains enormous. NN/g\'s finding that narrow-scope features win mirrors software engineering: GitHub Copilot\'s killer feature isn\'t "generate entire projects" but "autocomplete the current line." Cursor\'s strength isn\'t "one-click apps" but precise code completion in context. <strong>AI excels at focused, constrained tasks and struggles with open, ambiguous creative tasks. This isn\'t a temporary limitation — it\'s a fundamental characteristic of AI as a tool.</strong> This is actually good news: it means designers\' judgment, taste, and strategic thinking won\'t be replaced soon. AI automates the grunt work while humans make the aesthetic and strategic decisions. <strong>My take: "marginally better" isn\'t bad news — it\'s a healthy reality calibration. The most successful design teams in 2026 won\'t be those using AI the most, but those who know when to use AI and when not to. Narrow-scope AI\'s victory teaches us: a tool\'s value is doing one thing well, not promising to do everything.</strong></p></div>'
    },
    "cover": images.get("nng", ""),
    "sources": [
        {
            "title": {"zh": "NN/g：AI 设计工具只是略微好了一点", "en": "AI Design Tools Are Marginally Better: Status Update"},
            "url": "https://www.nngroup.com/articles/ai-design-tools-update-2/",
            "image": images.get("nng", "")
        },
        {
            "title": {"zh": "Figma Make：AI 设计生成器", "en": "Figma Make: Your AI Design Tool"},
            "url": "https://www.figma.com/solutions/ai-design-generator/",
            "image": images.get("figma_make", "")
        },
        {
            "title": {"zh": "2026 年 9 大 AI UX 工具实测", "en": "The Top 9 AI Tools for UX Design in 2026"},
            "url": "https://www.uxdesigninstitute.com/blog/the-top-9-ai-tools-for-ux-2026/",
            "image": images.get("uxdi", "")
        }
    ]
}

tech_issue = {
    "date": "2026-04-06",
    "section": "tech",
    "title": {
        "zh": "微软发布三款自研 AI 基础模型，正面挑战 OpenAI 和 Google · Apple 50 周年：硬件帝国能否在 AI 时代续命？· AI 股票 2026 年大重置",
        "en": "Microsoft Launches 3 In-House AI Models, Directly Challenging OpenAI & Google · Apple at 50: Can a Hardware Empire Survive the AI Era? · AI Stocks Reset in 2026"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul><li><strong>微软发布三款完全自研的 AI 基础模型——语音转文字、语音生成、图像生成——直接与 OpenAI 竞争</strong> — 微软在 4 月 2 日一口气发布了三款完全自研的 AI 模型：MAI-Transcribe-1（语音转文字，号称超越 Whisper）、MAI-Voice-1（语音生成，$22/百万字符）、MAI-Image-2（图像生成，$5/百万 token）。这是微软 AI 部门（MAI）成立六个月来最重大的产品发布。<strong>关键信号：微软已经在 Copilot 语音模式和 Teams 会议转录中测试 MAI-Transcribe-1，准备替换第三方或旧内部模型。</strong>这意味着微软不再甘于只做 OpenAI 模型的分发渠道——它要在模型层直接竞争。定价策略也很激进，明显对标 OpenAI 和 Google。<br><small>来源：<a href="https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/">TechCrunch</a>、<a href="https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google">VentureBeat</a></small></li><li><strong>Apple 50 周年：硬件帝国在 AI 时代的「late mover」策略能否奏效？</strong> — Apple 于 4 月 1 日迎来 50 周年。在 AI 竞赛中，Apple 的策略截然不同：不建巨型云端模型，而是聚焦<strong>端侧 AI——利用自研芯片让小模型在 iPhone/Mac 上本地运行</strong>。一个有趣的矛盾：Apple 的 AI 产品远不如竞争对手突出，但<strong>过去一年 Apple 股价涨幅超过 Microsoft、Meta 和 Amazon</strong>。Siri 已向 Google Gemini 等第三方 AI 开放——这在几年前不可想象。Wozniak、前 CEO Sculley 和 Siri 联合创始人都暗示 Apple 可能在「play a longer game」。问题是：设备市场的统治地位是否允许 Apple 在 AI 竞赛中慢慢来？<br><small>来源：<a href="https://www.techbrew.com/stories/2026/04/01/apple-turns-50-ai-strategy">Tech Brew</a>、<a href="https://www.usatoday.com/story/money/2026/04/01/apple-turns-50-microsoft-google/89421094007/">USA Today</a></small></li><li><strong>AI 股票 2026 年大重置：Nvidia、Apple、Google、Microsoft 各自命运分化</strong> — MSN/市场分析报道，2026 年 AI 股票经历了显著重置。Nvidia 面临 GTC 大会和新财报的双重考验；Apple 在 AI 赛道上仍是一个谜；Microsoft 尽管推出自研模型但整体股价表现不佳；Google 在搜索 AI 化上持续投入。<strong>市场正在从「AI 概念炒作」转向「谁能把 AI 变成实际收入」的硬着陆阶段。</strong><br><small>来源：<a href="https://www.msn.com/en-us/news/technology/ai-stocks-reset-in-2026-what-s-next-for-apple-nvidia-google-and-microsoft/ar-AA1Wwhip">MSN</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>微软「去 OpenAI 化」加速</strong>：自研三款基础模型 + 激进定价 = 从分发渠道升级为模型开发者</li><li><strong>Apple 的反向策略</strong>：不追云端大模型，押注端侧 AI + 自研芯片 + 设备生态</li><li><strong>AI 投资进入「证明期」</strong>：市场不再买「AI 概念」，要看实际收入转化</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>微软发布自研模型这件事，放在一周前 OpenAI 高管大洗牌的背景下看，格外有意思。</strong></p><p>上期我们讨论了 OpenAI 三位 C-suite 同时变动的不寻常信号。现在微软的动作让画面更完整了：<strong>微软正在系统性地降低对 OpenAI 的依赖。</strong>MAI-Transcribe-1 直接对标 Whisper（OpenAI 的语音模型），而且已经在 Copilot 和 Teams 里内测替换。这不是「多元化布局」的委婉说法——这是「准备离婚时先转移资产」的策略。微软在 OpenAI 上投了 130 多亿美元，但现在它显然不想把自己的产品命运绑在一家高管频繁变动、估值泡沫化的公司上。</p><p>MAI 的三款模型选择了语音和图像这两个赛道，避开了最核心的文本 LLM 竞争（至少目前如此）。这是聪明的侧翼进攻：<strong>先在边缘模态建立能力，同时保留使用 OpenAI GPT 的选项做文本 LLM。</strong>但我赌 MAI 的文本模型已经在开发中——六个月内我们就会看到。</p><p>Apple 50 周年的故事则完全是另一个逻辑。所有人都在说 Apple 在 AI 赛道上「落后」，但 Apple 的股价涨幅超过了那些「领先」的公司。为什么？因为市场定价的不是「谁的 AI 最强」，而是「谁的商业护城河最深」。<strong>Apple 控制着全球最有价值的硬件生态——15 亿台活跃设备、App Store、自研芯片。</strong>只要 AI 功能需要通过手机触达用户，Apple 就永远有一张底牌。开放 Siri 给 Gemini 看起来是「认输」，但实际上是「让别人的 AI 在我的平台上跑」——平台税比模型利润可持续得多。</p><p>把今天的设计和科技新闻连起来看，有一个共同主题：<strong>「做得好」比「做得多」更重要。</strong>NN/g 说窄范围 AI 工具胜过广范围工具；Apple 说端侧小模型比云端大模型更适合自己；微软说与其全押一家，不如自建能力。市场正在从 AI 的「泡沫期」进入「分化期」——<strong>赢家不是技术最先进的，而是最清楚自己该做什么和不该做什么的。</strong></p><p><strong>我的预判：微软的自研模型路线会在 2026 下半年显著加速，年底前我们会看到 MAI 的文本模型。OpenAI 和微软的关系将从「战略合作伙伴」降格为「模型供应商之一」。而 Apple 的端侧 AI 策略将在 iOS 20（今年秋季）迎来关键验证——如果它能在不依赖云端的情况下提供足够好的 AI 体验，那「AI 竞赛」的定义本身就要被改写。不是谁的模型参数最大，而是谁的 AI 体验最无缝地融入用户生活。Apple 最擅长的，恰恰就是这件事。</strong></p></div>',
        "en": '<h3>📌 AI × Tech</h3><ul><li><strong>Microsoft Launches Three Fully In-House AI Foundation Models — Speech-to-Text, Voice Generation, Image Generation — Directly Competing with OpenAI</strong> — On April 2, Microsoft released three proprietary AI models: MAI-Transcribe-1 (speech-to-text, claiming to surpass Whisper), MAI-Voice-1 (voice generation, $22/million characters), and MAI-Image-2 (image generation, $5/million input tokens). This is the most significant release from Microsoft AI (MAI) since its formation six months ago. <strong>Key signal: Microsoft is already testing MAI-Transcribe-1 in Copilot Voice and Teams transcription, preparing to replace third-party models.</strong> Microsoft is no longer content being just a distribution channel for OpenAI — it\'s competing at the model layer. Aggressive pricing directly targets OpenAI and Google.<br><small>Source: <a href="https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/">TechCrunch</a>, <a href="https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google">VentureBeat</a></small></li><li><strong>Apple at 50: Can the "Late Mover" Strategy Work in the AI Era?</strong> — Apple celebrated its 50th anniversary on April 1. Its AI strategy differs radically: no giant cloud models, instead focusing on <strong>on-device AI powered by custom silicon</strong>. A fascinating paradox: Apple\'s AI offerings lag far behind competitors, yet <strong>Apple\'s stock has outperformed Microsoft, Meta, and Amazon over the past year.</strong> Siri now integrates third-party AI like Google Gemini — unthinkable years ago. Wozniak, former CEO Sculley, and Siri\'s co-founders suggest Apple may be "playing a longer game."<br><small>Source: <a href="https://www.techbrew.com/stories/2026/04/01/apple-turns-50-ai-strategy">Tech Brew</a>, <a href="https://www.usatoday.com/story/money/2026/04/01/apple-turns-50-microsoft-google/89421094007/">USA Today</a></small></li><li><strong>AI Stocks Reset in 2026: Nvidia, Apple, Google, Microsoft Diverge</strong> — Market analysis shows 2026 has brought a significant AI stock reset. Nvidia faces dual GTC and earnings tests; Apple remains an AI enigma; Microsoft underperforms despite new models; Google invests heavily in search AI. <strong>Markets are shifting from "AI hype" to "who can turn AI into actual revenue."</strong><br><small>Source: <a href="https://www.msn.com/en-us/news/technology/ai-stocks-reset-in-2026-what-s-next-for-apple-nvidia-google-and-microsoft/ar-AA1Wwhip">MSN</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Microsoft de-OpenAI-ification: three proprietary models + aggressive pricing = from distributor to model developer</li><li>Apple\'s contrarian strategy: on-device AI + custom silicon + device ecosystem over cloud-scale models</li><li>AI investment enters "prove it" phase: markets demand revenue conversion, not just AI narratives</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Microsoft\'s in-house model release, viewed against last week\'s OpenAI executive shuffle, paints a clear picture: Microsoft is systematically reducing its dependence on OpenAI.</strong> MAI-Transcribe-1 directly targets Whisper (OpenAI\'s speech model) and is already being tested as a replacement in Copilot and Teams. This isn\'t "diversification" — it\'s the "transfer assets before divorce" strategy. Microsoft invested $13B+ in OpenAI but clearly doesn\'t want its product destiny tied to a company with frequent leadership changes and bubble-level valuations. The three models strategically chose speech and image, avoiding direct text LLM competition (for now). Smart flanking: build capabilities in peripheral modalities while keeping OpenAI GPT for text. But I\'d bet MAI\'s text model is already in development — we\'ll see it within six months. Apple\'s story runs on entirely different logic. Everyone says Apple is "behind" in AI, yet its stock outperforms the "leaders." Why? Because markets price deepest moats, not strongest models. Apple controls 1.5 billion active devices, the App Store, and custom silicon. As long as AI needs phones to reach users, Apple holds a trump card. Opening Siri to Gemini looks like surrender but is actually "let others\' AI run on my platform" — platform tax is more sustainable than model margins. <strong>Today\'s common theme across design and tech: "doing the right things" beats "doing all things." NN/g says narrow AI tools beat broad ones; Apple says on-device beats cloud-scale; Microsoft says self-reliance beats single-vendor dependency. The AI market is entering differentiation phase — winners aren\'t the most advanced, but those who best know what to do and what not to do.</strong></p></div>'
    },
    "cover": images.get("ms_models", ""),
    "sources": [
        {
            "title": {"zh": "微软发布三款自研 AI 基础模型", "en": "Microsoft Takes on AI Rivals with Three New Foundational Models"},
            "url": "https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/",
            "image": images.get("ms_models", "")
        },
        {
            "title": {"zh": "Apple 50 周年：AI 战略何去何从", "en": "Apple at 50: AI Strategy Matters More Than Ever"},
            "url": "https://www.techbrew.com/stories/2026/04/01/apple-turns-50-ai-strategy",
            "image": images.get("apple50", "")
        },
        {
            "title": {"zh": "AI 股票 2026 年大重置", "en": "AI Stocks Reset in 2026"},
            "url": "https://www.msn.com/en-us/news/technology/ai-stocks-reset-in-2026-what-s-next-for-apple-nvidia-google-and-microsoft/ar-AA1Wwhip",
            "image": ""
        }
    ]
}

# Load existing issues and prepend new ones
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Added 2 issues (design + tech) for 2026-04-06. Total issues: {len(issues)}")
