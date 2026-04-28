# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily update for 2026-04-28"""
import json, urllib.request, urllib.error, re, os

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode("utf-8", errors="ignore")
            m = re.search(r'<meta[^>]*property="og:image"[^>]*content="([^"]+)"', html)
            return m.group(1) if m else ""
    except:
        return ""

issues_path = os.path.join(os.path.dirname(__file__), "issues.json")
with open(issues_path, "r") as f:
    issues = json.load(f)

# Design issue: ComfyUI $500M + GitHub Copilot usage-based billing
design_issue = {
    "date": "2026-04-28",
    "section": "design",
    "title": {
        "zh": "ComfyUI 估值 5 亿美元：创作者夺回 AI 生成控制权，「节点式工作流」正在重塑创意工具的权力结构",
        "en": "ComfyUI Hits $500M Valuation: Creators Reclaim Control Over AI Generation as Node-Based Workflows Reshape Creative Tool Power Dynamics"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul><li><strong>ComfyUI 完成 3000 万美元融资，估值达 5 亿美元</strong> — TechCrunch 报道，开源节点式 AI 生成工具 ComfyUI 刚刚完成新一轮融资。<strong>ComfyUI 让创作者通过可视化节点工作流精确控制 AI 图像、视频和音频生成的每个环节</strong>，而不是像 Midjourney 那样只写一句 prompt 然后「祈祷」。这标志着创意 AI 工具市场正在分化：一边是追求「零门槛」的消费级产品（Midjourney、DALL-E），另一边是追求「全控制」的专业级工具（ComfyUI、Stable Diffusion 生态）。5 亿美元的估值证明市场认可后者。<br><small>来源：<a href="https://techcrunch.com/2026/04/24/comfyui-hits-500m-valuation-as-creators-seek-more-control-over-ai-generated-media/">TechCrunch</a></small></li><li><strong>GitHub Copilot 转向按用量计费，AI 辅助工具告别「自助餐」时代</strong> — GitHub 宣布从 6 月 1 日起，Copilot 使用将消耗 AI Credits 而非固定月费。<strong>这是 AI 工具行业定价模式的一次范式转变</strong>：从「月费无限用」转向「用多少付多少」。对设计行业的启示很直接——当 Figma、Adobe 等工具的 AI 功能越来越重时，类似的按用量计费模式几乎必然会跟进。设计师的「AI 成本」将不再隐藏在订阅费里，而是与每一次生成、每一次迭代直接挂钩。<br><small>来源：<a href="https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/">GitHub Blog</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>创意 AI 的「控制权之争」</strong>：ComfyUI 的成功说明专业创作者不满足于黑箱式生成，他们要可编程、可调试、可复现的工作流</li><li><strong>AI 工具定价范式转移</strong>：从固定订阅到按用量计费，AI 功能的边际成本开始被显性化</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>ComfyUI 拿到 5 亿美元估值，这件事比表面看起来重要得多。它不只是「又一个 AI 工具融资」——它代表了创意工具市场的一次权力结构重组。</strong></p><p>过去两年，AI 生成工具的主流叙事是「降低门槛」：Midjourney 让不会画画的人能出图，DALL-E 让写句话就能「创作」。这个叙事服务的是消费者和营销人员，但它忽略了一个群体——<strong>真正靠视觉创作吃饭的专业人士</strong>。这些人不想要黑箱，他们想要手术刀。ComfyUI 的节点式工作流就是这把手术刀：你可以精确控制每一步——从噪声调度到 ControlNet 到 LoRA 混合，每个参数都可视、可调、可复现。这不是「更好的 Midjourney」，这是一种完全不同的范式。</p><p>把 ComfyUI 和 GitHub Copilot 的计费变革放在一起看，一个有趣的 pattern 浮现了：<strong>AI 工具正在从「一刀切的订阅」走向「按需付费 + 用户自主控制」的双重精细化</strong>。Copilot 说：你用多少 AI 算力，就付多少钱。ComfyUI 说：你想要多少控制，就给你多少控制。两者的共同点是<strong>把选择权还给用户</strong>。</p><p>这对设计行业意味着什么？我的预测是：<strong>2026 下半年，我们会看到 Figma 和 Adobe 跟进类似的按用量计费模式</strong>。目前 Figma 的 AI 功能（如 Make Designs）还包含在订阅里，但当 AI 推理成本成为产品成本的大头时，固定月费模式在数学上不可持续。GitHub 打了第一枪，Adobe 和 Figma 会跟——问题只是时间。</p><p>更深层的影响在于设计师的工作方式。<strong>当 AI 使用按次计费时，「随手试试看」的成本变得可见</strong>。这会倒逼设计师更有策略地使用 AI——不是每次灵感闪现都去跑一轮生成，而是先想清楚再让机器跑。讽刺的是，AI 工具的定价模式可能会让设计流程重新变得「深思熟虑」，而不是「AI 暴力试错」。ComfyUI 的节点式工作流天然适配这种模式——因为你在搭建节点图的过程中，其实就在做设计决策。</p><p><strong>最后一个观察：ComfyUI 是开源的。5 亿美元的估值给了一个开源项目，这本身就是一个信号——在 AI 创意工具领域，开源不是慈善，而是竞争策略。当你的工作流是开放的、可组合的、社区驱动的，你就获得了闭源工具永远无法复制的东西：一个不断贡献新节点、新工作流、新玩法的生态系统。这和 Gemma 4 用开源挑战 GPT 的逻辑如出一辙。2026 年的创意工具大战，开源正在赢。</strong></p></div>',
        "en": '<h3>📌 AI × Design</h3><ul><li><strong>ComfyUI Raises $30M at $500M Valuation</strong> — TechCrunch reports the open-source node-based AI generation tool just closed a new funding round. <strong>ComfyUI lets creators precisely control every step of AI image, video, and audio generation through visual node workflows</strong>, rather than writing a prompt and praying. This marks a clear fork in the creative AI market: consumer-grade "zero barrier" products (Midjourney, DALL-E) vs. professional-grade "full control" tools (ComfyUI, Stable Diffusion ecosystem). The $500M valuation validates the latter.<br><small>Source: <a href="https://techcrunch.com/2026/04/24/comfyui-hits-500m-valuation-as-creators-seek-more-control-over-ai-generated-media/">TechCrunch</a></small></li><li><strong>GitHub Copilot Moves to Usage-Based Billing, Ending the "All-You-Can-Eat" Era</strong> — Starting June 1, Copilot usage will consume AI Credits instead of flat monthly fees. <strong>This is a paradigm shift in AI tool pricing</strong>. The implication for design: when Figma and Adobe\'s AI features grow heavier, similar usage-based models will follow. Designers\' "AI costs" will be directly tied to each generation and iteration.<br><small>Source: <a href="https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/">GitHub Blog</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>The "Control War" in Creative AI</strong>: ComfyUI\'s success shows professional creators demand programmable, debuggable, reproducible workflows—not black boxes</li><li><strong>AI Tool Pricing Paradigm Shift</strong>: From flat subscriptions to usage-based billing; marginal costs of AI features are becoming explicit</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>ComfyUI\'s $500M valuation matters more than it appears. It represents a power structure realignment in the creative tools market.</strong></p><p>For two years, the mainstream AI generation narrative was "lower the barrier": Midjourney lets non-artists make images. That narrative serves consumers and marketers but ignores <strong>professional visual creators who want a scalpel, not a magic wand</strong>. ComfyUI\'s node-based workflows are that scalpel—precise control over every parameter, visible, adjustable, reproducible.</p><p>Pair ComfyUI with GitHub Copilot\'s billing shift, and a pattern emerges: <strong>AI tools are moving from "one-size-fits-all subscriptions" to "pay-per-use + user-controlled granularity"</strong>. Both return choice to users. My prediction: <strong>Figma and Adobe will follow with usage-based AI billing by late 2026</strong>. When AI inference costs dominate product costs, flat fees become mathematically unsustainable.</p><p>The deeper impact: when AI usage is metered per-call, "just try it" gains visible cost. This will push designers toward more deliberate AI use—think first, generate second. Ironically, AI pricing may make design processes more thoughtful, not less. ComfyUI\'s node workflows naturally fit this: building a node graph IS making design decisions.</p><p><strong>Final note: ComfyUI is open-source. A $500M valuation for an open-source project signals that in creative AI, openness isn\'t charity—it\'s competitive strategy. An open, composable, community-driven workflow ecosystem is something closed tools can never replicate. Same logic as Gemma 4 challenging GPT. In 2026\'s creative tools war, open source is winning.</strong></p></div>'
    },
    "cover": "https://techcrunch.com/wp-content/uploads/2026/04/ComfyUI-Co-founders-1.png?resize=1200,790",
    "sources": [
        {
            "title": {
                "zh": "ComfyUI 估值 5 亿美元，创作者寻求更多 AI 生成控制权",
                "en": "ComfyUI Hits $500M Valuation as Creators Seek More Control Over AI-Generated Media"
            },
            "url": "https://techcrunch.com/2026/04/24/comfyui-hits-500m-valuation-as-creators-seek-more-control-over-ai-generated-media/",
            "image": "https://techcrunch.com/wp-content/uploads/2026/04/ComfyUI-Co-founders-1.png?resize=1200,790"
        },
        {
            "title": {
                "zh": "GitHub Copilot 转向按用量计费",
                "en": "GitHub Copilot Is Moving to Usage-Based Billing"
            },
            "url": "https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/",
            "image": "https://github.blog/wp-content/uploads/2026/01/generic-invertocat-logo.png"
        }
    ]
}

# Tech issue: Microsoft-OpenAI restructure, China blocks Meta-Manus, David Silver $1.1B
tech_issue = {
    "date": "2026-04-28",
    "section": "tech",
    "title": {
        "zh": "AI 权力版图重划：Microsoft-OpenAI 结束独家协议、中国否决 Meta 收购 Manus、DeepMind 元老 David Silver 融 11 亿美元押注无数据学习",
        "en": "AI Power Map Redrawn: Microsoft-OpenAI End Exclusive Deal, China Blocks Meta's Manus Acquisition, DeepMind Veteran David Silver Raises $1.1B for Data-Free Learning"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul><li><strong>Microsoft 和 OpenAI 终结独家及收入分成协议</strong> — Bloomberg 独家报道，<strong>Microsoft 将不再与 OpenAI 进行收入分成，同时允许 OpenAI 在 Amazon AWS 上销售产品</strong>，结束了双方的排他性关系。作为交换，Microsoft 获得了更多现金补偿。这意味着 OpenAI 的 500 亿美元 Amazon 交易不再面临法律风险。结合上周 Microsoft 自研 MAI 模型的消息，Microsoft-OpenAI 这对「AI 婚姻」正在从「蜜月期」进入「AA 制」。<br><small>来源：<a href="https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai">Bloomberg</a>、<a href="https://techcrunch.com/2026/04/27/openai-ends-microsoft-legal-peril-over-its-50b-amazon-deal/">TechCrunch</a></small></li><li><strong>中国否决 Meta 20 亿美元收购 AI 创业公司 Manus</strong> — 中国国家发改委正式叫停 Meta 收购新加坡 AI 创业公司 Manus（有中国背景）的交易。<strong>这是 AI 领域地缘政治博弈的一个标志性事件</strong>：即使公司注册在新加坡，只要核心团队或技术有中国关联，收购就可能被北京叫停。Meta 在全球 AI 并购中再次碰壁——之前的 Thinking Machines 交易也因类似原因受阻。<br><small>来源：<a href="https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html">CNBC</a>、<a href="https://techcrunch.com/2026/04/27/china-vetoes-metas-2b-manus-deal-after-months-long-probe/">TechCrunch</a></small></li><li><strong>DeepMind 元老 David Silver 创立 Ineffable Intelligence，融资 11 亿美元</strong> — AlphaGo 背后的关键人物 David Silver 仅数月前从 DeepMind 离职创办的 Ineffable Intelligence，<strong>以 51 亿美元估值完成 11 亿美元融资</strong>。公司目标是构建「无需人类数据就能学习」的 AI——延续 AlphaZero 的自我博弈路线。结合上周报道的 Yann LeCun 的 AMI Labs 获 10.3 亿美元融资，<strong>两笔合计超过 21 亿美元的巨额融资押注在「超越 LLM」的路线上</strong>。<br><small>来源：<a href="https://techcrunch.com/2026/04/27/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/">TechCrunch</a></small></li><li><strong>Anthropic 创建 Agent 对 Agent 交易市场实验</strong> — Anthropic 公布了一个实验项目：<strong>一个 AI Agent 同时扮演买家和卖家、用真钱进行真交易的分类市场</strong>。这不再是「AI 聊天机器人」的范畴，而是 AI 经济体的雏形——Agent 自主谈判、定价、成交。这可能是 2026 年最被低估的 AI 进展之一。<br><small>来源：<a href="https://techcrunch.com/2026/04/25/anthropic-created-a-test-marketplace-for-agent-on-agent-commerce/">TechCrunch</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 巨头「解绑」</strong>：Microsoft-OpenAI 结束独家，OpenAI 上 AWS，双方进入更独立的关系</li><li><strong>AI 收购遭遇地缘政治壁垒</strong>：Meta-Manus 被否凸显中美 AI 脱钩正在从芯片层延伸到创业公司层</li><li><strong>「后 LLM」路线获天量资金</strong>：Silver 11 亿 + LeCun 10.3 亿 = 21.3 亿美元押注自我学习和世界模型</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>今天的新闻表面上是四个独立故事，但它们共同描绘了一幅 2026 年 AI 行业权力结构正在被彻底重划的图景。</strong></p><p>先说 Microsoft-OpenAI「分手不离婚」。Bloomberg 这条新闻的信息量远超标题。<strong>收入分成终结 + 允许 OpenAI 上 AWS = Microsoft 承认了一个事实：锁定 OpenAI 的成本太高，不如放开换现金</strong>。上周我们聊过 Microsoft 自研三款 MAI 模型的「去 OpenAI 化」信号，现在看来这不是信号——这是已经执行到位的战略。Microsoft 的算盘很清楚：OpenAI 你去 AWS 卖吧，我用你的模型也用自己的，咱俩都别绑死。OpenAI 赢了自由度（500 亿 Amazon 交易落地），Microsoft 赢了灵活性（不再需要为 OpenAI 的每一步买单）。但最大的赢家可能是 AWS——突然间，全球最强的 AI 模型之一可以在它的平台上原生运行了。</p><p>再看中国否决 Meta 收购 Manus。<strong>这件事的意义远超 20 亿美元的交易本身</strong>。Manus 注册在新加坡，但核心团队有中国背景。中国发改委的逻辑是：不管你公司注册在哪，只要人和技术跟中国有关，就归我管。这等于在 AI 创业领域画了一条新红线——对所有有中国联合创始人或核心工程师的海外 AI 公司来说，被美国大科技公司收购这条退出路径可能已经关上了。这会怎样影响全球 AI 创业生态？我的猜测是：<strong>更多 AI 创业公司会在成立之初就做「干净切割」——要么完全中国，要么完全去中国化</strong>。中间地带正在消失。</p><p>David Silver 的 Ineffable Intelligence 和上周的 AMI Labs（LeCun）放在一起看最有意思。<strong>两位 AI 领域的教父级人物，合计拿到 21.3 亿美元，都在做同一件事：证明当前的 LLM 范式不是终点</strong>。Silver 走 AlphaZero 路线——让 AI 在没有人类数据的情况下通过自我博弈学习；LeCun 走世界模型路线——让 AI 像人类一样通过观察物理世界来建模。两条路线都指向同一个方向：<strong>摆脱对海量人类数据的依赖</strong>。如果他们中任何一个成功了，今天围绕「谁有更多训练数据」展开的竞争将变得毫无意义。</p><p><strong>最后说 Anthropic 的 Agent 交易市场。这个实验看似是个技术 demo，但它暗示的未来非常激进：当 AI Agent 可以自主谈判和交易时，「AI 经济体」就不再是科幻概念了。把今天的四条新闻连起来看：AI 巨头在「解绑」（Microsoft-OpenAI），国家在「画界」（China-Meta），基础范式在「迁移」（Silver-LeCun），而 AI 本身在「长出经济行为」（Anthropic marketplace）。2026 年不是 AI 的「发展年」——它是 AI 行业从「技术竞赛」转向「权力重组」的转折点。对设计行业的人来说，最实际的影响是：AI 工具的底层供应商关系正在变得极其复杂和不稳定。你用的 Figma AI 功能可能今天跑在 OpenAI 上，明天跑在 AWS 上，后天换成 Google。在这个动荡中，唯一稳定的投资是你自己的审美判断力和设计方法论——这些不会因为底层模型换了供应商而贬值。</strong></p></div>',
        "en": '<h3>📌 AI × Tech</h3><ul><li><strong>Microsoft and OpenAI End Exclusive and Revenue-Sharing Deal</strong> — Bloomberg reports <strong>Microsoft will stop sharing revenue with OpenAI and allow it to sell products on AWS</strong>, ending their exclusive relationship. In exchange, Microsoft gets more cash. This clears legal risk for OpenAI\'s $50B Amazon deal. Combined with Microsoft\'s in-house MAI models, the "AI marriage" is moving from honeymoon to separate checks.<br><small>Source: <a href="https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai">Bloomberg</a>, <a href="https://techcrunch.com/2026/04/27/openai-ends-microsoft-legal-peril-over-its-50b-amazon-deal/">TechCrunch</a></small></li><li><strong>China Blocks Meta\'s $2B Acquisition of AI Startup Manus</strong> — China\'s NDRC formally prohibited Meta\'s acquisition of Singapore-based AI startup Manus, which has Chinese roots. <strong>A landmark geopolitical event in AI</strong>: even Singapore-registered companies face Beijing\'s veto if core teams have Chinese ties.<br><small>Source: <a href="https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html">CNBC</a>, <a href="https://techcrunch.com/2026/04/27/china-vetoes-metas-2b-manus-deal-after-months-long-probe/">TechCrunch</a></small></li><li><strong>DeepMind Veteran David Silver Raises $1.1B for Ineffable Intelligence</strong> — The key mind behind AlphaGo left DeepMind months ago to found Ineffable Intelligence, now <strong>valued at $5.1B after an $1.1B raise</strong>. Goal: build AI that learns without human data. Combined with LeCun\'s AMI Labs ($1.03B), <strong>over $2.1B is now betting on "beyond LLM" paradigms</strong>.<br><small>Source: <a href="https://techcrunch.com/2026/04/27/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/">TechCrunch</a></small></li><li><strong>Anthropic Creates Agent-on-Agent Commerce Marketplace</strong> — Anthropic built <strong>a classified marketplace where AI agents represent both buyers and sellers, striking real deals for real money</strong>. This isn\'t chatbot territory—it\'s the embryo of an AI economy.<br><small>Source: <a href="https://techcrunch.com/2026/04/25/anthropic-created-a-test-marketplace-for-agent-on-agent-commerce/">TechCrunch</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Giants "Unbundling"</strong>: Microsoft-OpenAI end exclusivity; OpenAI goes multi-cloud</li><li><strong>AI M&A Hits Geopolitical Walls</strong>: Meta-Manus block shows US-China AI decoupling extending from chips to startups</li><li><strong>"Post-LLM" Routes Get Massive Funding</strong>: Silver $1.1B + LeCun $1.03B = $2.13B betting on self-learning and world models</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Four seemingly separate stories today collectively paint a picture of AI\'s power structure being completely redrawn in 2026.</strong></p><p>The Microsoft-OpenAI "separation without divorce" carries more information than the headline suggests. <strong>End revenue sharing + allow OpenAI on AWS = Microsoft admits locking in OpenAI costs too much</strong>. Last week\'s MAI models weren\'t a signal—they were an executed strategy. Microsoft\'s calculus: let OpenAI sell on AWS, use their models AND in-house ones, nobody\'s locked in. OpenAI wins freedom ($50B Amazon deal clears), Microsoft wins flexibility. But AWS might be the biggest winner—suddenly one of the world\'s strongest AI models runs natively on their platform.</p><p>China blocking Meta\'s Manus acquisition matters beyond $2B. <strong>Manus is Singapore-registered but has Chinese-origin teams. Beijing\'s message: regardless of incorporation, Chinese-connected talent and tech falls under our jurisdiction.</strong> This effectively closes the "get acquired by Big Tech" exit path for overseas AI companies with Chinese co-founders. My prediction: <strong>more AI startups will make "clean breaks" at founding—fully Chinese or fully de-Sinicized</strong>. The middle ground is disappearing.</p><p>Silver\'s Ineffable Intelligence paired with LeCun\'s AMI Labs is fascinating. <strong>Two godfather-level AI figures, $2.13B combined, both trying to prove the current LLM paradigm isn\'t the endpoint</strong>. Silver takes the AlphaZero route (self-play without human data); LeCun takes world models (learning by observing physics). Both point the same direction: <strong>breaking free from massive human data dependency</strong>.</p><p><strong>Anthropic\'s agent marketplace seems like a tech demo but implies a radical future. Connect today\'s four stories: giants are unbundling (Microsoft-OpenAI), nations are drawing lines (China-Meta), foundational paradigms are shifting (Silver-LeCun), and AI itself is developing economic behavior (Anthropic marketplace). 2026 isn\'t AI\'s "growth year"—it\'s the inflection from "tech race" to "power restructuring." For designers: AI tool supply chains are becoming extremely complex and unstable. Your Figma AI might run on OpenAI today, AWS tomorrow, Google next week. The only stable investment is your own aesthetic judgment and design methodology—those don\'t depreciate when the underlying model changes vendors.</strong></p></div>'
    },
    "cover": "",
    "sources": [
        {
            "title": {
                "zh": "Microsoft 和 OpenAI 终结独家与收入分成协议",
                "en": "Microsoft and OpenAI End Their Exclusive and Revenue-Sharing Deal"
            },
            "url": "https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai",
            "image": ""
        },
        {
            "title": {
                "zh": "中国否决 Meta 20 亿美元收购 AI 创业公司 Manus",
                "en": "China Blocks Meta's $2B Manus Deal After Months-Long Probe"
            },
            "url": "https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html",
            "image": ""
        },
        {
            "title": {
                "zh": "DeepMind 的 David Silver 融资 11 亿美元，构建无需人类数据的 AI",
                "en": "DeepMind's David Silver Raised $1.1B to Build AI That Learns Without Human Data"
            },
            "url": "https://techcrunch.com/2026/04/27/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/",
            "image": ""
        },
        {
            "title": {
                "zh": "Anthropic 创建 Agent 对 Agent 交易市场",
                "en": "Anthropic Created a Test Marketplace for Agent-on-Agent Commerce"
            },
            "url": "https://techcrunch.com/2026/04/25/anthropic-created-a-test-marketplace-for-agent-on-agent-commerce/",
            "image": ""
        }
    ]
}

# Fetch og:images for tech sources
og_urls = {
    "https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai": None,
    "https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html": None,
    "https://techcrunch.com/2026/04/27/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/": None,
    "https://techcrunch.com/2026/04/25/anthropic-created-a-test-marketplace-for-agent-on-agent-commerce/": None,
}

for url in og_urls:
    img = get_og_image(url)
    og_urls[url] = img
    print(f"OG: {url} -> {img[:80] if img else 'NONE'}")

# Apply images to tech sources
for src in tech_issue["sources"]:
    img = og_urls.get(src["url"], "")
    if img:
        src["image"] = img

# Set cover from first source with image
for src in tech_issue["sources"]:
    if src.get("image"):
        tech_issue["cover"] = src["image"]
        break

# Insert new issues at front
issues = [design_issue, tech_issue] + issues

with open(issues_path, "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"Done. Total issues: {len(issues)}")
