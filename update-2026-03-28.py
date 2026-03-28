# -*- coding: utf-8 -*-
"""Rex Daily Update - 2026-03-28"""
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
    "sciencedaily": "https://www.sciencedaily.com/releases/2026/03/260315004355.htm",
    "iphoneincanada": "https://www.iphoneincanada.ca/2026/03/26/apple-plans-to-open-siri-to-rival-ai-assistants-in-ios-27-overhaul/",
    "reuters_apple": "https://www.reuters.com/business/apple-plans-open-siri-rival-ai-services-bloomberg-news-reports-2026-03-26/",
    "anthropic_81k": "https://www.anthropic.com/features/81k-interviews",
    "anthropic_inst": "https://www.anthropic.com/news/the-anthropic-institute",
    "reflection_ai": "https://www.ainvest.com/news/reflection-ai-faces-critical-march-2026-test-20-billion-valuation-hinges-public-model-release-2603/",
    "reuters_arm": "https://www.reuters.com/business/media-telecom/arm-unveils-new-ai-chip-expects-it-add-billions-annual-revenue-2026-03-24/",
    "dcthemedian": "https://dcthemedian.substack.com/p/what-81000-people-want-from-ai",
    "design_weekly": "https://markets.financialcontent.com/wral/article/abnewswire-2026-3-11-ai-tools-for-designers-and-creative-professionals-design-tools-weekly-launches-new-initiative-to-streamline-fashion-ideation",
    "stitch_vibe": "https://stitch.withgoogle.com/",
    "zignuts": "https://www.zignuts.com/blog/best-ai-tools-for-ux-ui-designers",
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
        "zh": "AI 创造力超越普通人类但顶尖创意者仍不可替代 · Google Stitch 进化为「Vibe Design」画布 · Anthropic 8.1 万人调研揭示用户对 AI 的真实期待与焦虑",
        "en": "AI Creativity Surpasses Average Humans But Top Creatives Remain Irreplaceable · Google Stitch Evolves into 'Vibe Design' Canvas · Anthropic 81K Study Reveals Real AI Hopes and Fears"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul><li><strong>里程碑研究：AI 创造力超越普通人，但最有创造力的人类仍遥遥领先</strong> — ScienceDaily 报道了一项涉及超过 10 万人的大规模研究：当前最先进的生成式 AI 在标准化创造力测试中已经可以击败「普通」人类。但关键的但是来了——<strong>最具创造力的前 10% 人类，尤其在诗歌和叙事等富有层次的创意工作中，仍然远超 AI。</strong>这项研究为「AI 取代创意工作者」的恐慌提供了一个更精确的框架：AI 正在压缩创意工作的「中间层」——那些可以被标准化测试衡量的创意能力——但真正的创意天赋，那种结合了独特经验、文化洞察和审美直觉的能力，仍然是人类独有的。<br><small>来源：<a href="https://www.sciencedaily.com/releases/2026/03/260315004355.htm">ScienceDaily</a> | <a href="https://stephenslighthouse.com/2026/03/15/researchers-tested-ai-against-100000-humans-on-creativity/">Stephen\'s Lighthouse</a></small></li><li><strong>Google Stitch 进化为「Vibe Design」工具：AI 原生设计画布</strong> — DataCamp 的深度分析指出，Google Labs 已将 Stitch 升级为 AI 原生设计画布，可以从自然语言提示直接生成高保真 UI 界面。这被称为「Vibe Design」——类似于「Vibe Coding」的概念延伸。设计师用自然语言描述想要的界面，Stitch 直接生成可编辑的高保真设计，跳过传统的线框-视觉-原型流程。这是对昨天报道的「全栈化 AI 设计工具」趋势的进一步验证：<strong>设计的起点正在从空白画布变成自然语言。</strong><br><small>来源：<a href="https://dcthemedian.substack.com/p/what-81000-people-want-from-ai">DataCamp Median</a> | <a href="https://stitch.withgoogle.com/">Google Stitch</a></small></li><li><strong>Anthropic 发布史上最大 AI 用户研究：8.1 万人的声音</strong> — Anthropic 发布了有史以来最大规模的 AI 定性研究，采访了来自 159 个国家、70 种语言的 81,000 名 Claude 用户。关键数据：<strong>33% 的用户将 AI 视为学习工具</strong>（最大的正面认知），而 <strong>17% 担心 AI 导致认知退化</strong>。16% 重视 AI 的情感支持功能，12% 担心对其产生依赖。这些数据对设计师至关重要——它揭示了用户对 AI 产品的核心情感矛盾：<strong>「依赖」与「增强」之间的张力</strong>。任何设计 AI 功能的产品团队都需要认真对待这个双刃剑。<br><small>来源：<a href="https://www.anthropic.com/features/81k-interviews">Anthropic</a> | <a href="https://dcthemedian.substack.com/p/what-81000-people-want-from-ai">DataCamp Median</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 创造力的「中间压缩效应」</strong>：AI 正在消灭「平庸的创意」，但放大了「卓越创意」的稀缺性和价值</li><li><strong>「Vibe Design」= 设计的下一个范式</strong>：从像素操作到自然语言描述，设计的入口正在被彻底重写</li><li><strong>AI 用户心理的双刃剑</strong>：人们同时渴望 AI 增强和恐惧 AI 依赖——这是所有 AI 产品设计的核心矛盾</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>这三条新闻拼在一起，勾勒出了 2026 年创意行业最重要的一张图：AI 正在重新定义「创造力」的价值分布曲线。</strong></p><p>先从那个 10 万人创造力研究说起。表面上看，「AI 击败普通人类创造力」是一个恐怖的标题。但细读数据会发现一个更有趣也更重要的结论：<strong>AI 创造力的分布是扁平的——它可以稳定输出 70 分的创意，但几乎无法突破 90 分。</strong>而人类创造力的分布是长尾的——大多数人在 50-70 分区间，但顶尖的 10% 可以飙到 95+。这意味着什么？AI 正在消灭「平庸创意」的市场价值。如果一个设计师只能产出「还行」的方案，AI 用 5 秒就能给你 50 个「还行」的变体。但如果你能产出「惊艳」的方案——那种让人看了会说「这怎么想到的」的作品——你的价值反而在上升，因为 AI 让「还行」变得免费了，「惊艳」的相对稀缺性更高了。</p><p>这直接连接到 Google Stitch 的「Vibe Design」进化。当设计的起点从空白画布变成自然语言提示时，<strong>设计师的核心竞争力从「执行能力」（能不能画出来）转移到「判断能力」（知不知道该画什么）</strong>。Stitch 可以从一句话生成高保真 UI，但那句话怎么写、生成的结果好不好、用户会不会买单——这些判断需要的不是 Figma 技能，而是对用户、业务和审美的深度理解。「Vibe Design」降低了设计的门槛，但提高了设计判断力的天花板。这和创造力研究的结论完美吻合：工具越强，使用者的品味越重要。</p><p>Anthropic 的 8.1 万人研究则从用户心理层面补完了这张图。33% 视 AI 为学习工具 vs 17% 担心认知退化——这不是矛盾的，这是同一群人在不同时刻的两面。人们知道 AI 让他们更高效，但同时担心自己正在失去某些能力。这对设计 AI 产品的人来说是一个关键洞察：<strong>最好的 AI 产品不是替代用户的判断力，而是在增强能力的同时让用户感觉自己在「学习」和「成长」，而不是在「外包」和「退化」。</strong>Figma Make 的「Cooking with Constraints」框架就是一个好例子——它不是直接给你设计，而是教你如何写出好的提示词，这让用户觉得自己在「掌握」AI 而不是被 AI 取代。</p><p>把三条新闻连起来看，2026 年创意行业的新格局已经清晰：<strong>AI 正在执行「创意民主化」的同时制造「创意精英化」。</strong>每个人都能用 Stitch 生成 UI、用 AI 写文案、用 Midjourney 做视觉——这是民主化。但真正能从这些工具中榨出卓越成果的人，需要更高的判断力、更深的用户洞察、更独特的审美视角——这是精英化。中间地带正在消失。对设计师来说，2026 年的生存策略不是学更多工具（AI 工具学习成本已经趋近于零），而是<strong>投资在那些 AI 无法生成的东西上：独特的视角、深度的用户共情、跨领域的知识连接。</strong>这些正是那 10% 人类创意者胜过 AI 的原因。</p></div>',
        "en": '<h3>📌 AI × Design</h3><ul><li><strong>Landmark Study: AI Creativity Surpasses Average Humans, But Top 10% Still Far Ahead</strong> — A massive 100,000+ person study finds generative AI beats average humans on standardized creativity tests. But the top 10% of creative humans — especially in poetry and storytelling — still leave AI far behind. The implication: AI is compressing the "middle tier" of creative work while making truly exceptional creativity more scarce and valuable.<br><small>Source: <a href="https://www.sciencedaily.com/releases/2026/03/260315004355.htm">ScienceDaily</a> | <a href="https://stephenslighthouse.com/2026/03/15/researchers-tested-ai-against-100000-humans-on-creativity/">Stephen\'s Lighthouse</a></small></li><li><strong>Google Stitch Evolves into "Vibe Design" Canvas</strong> — Google Labs upgraded Stitch into an AI-native design canvas generating high-fidelity UI from natural language prompts. This "Vibe Design" concept — analogous to "Vibe Coding" — means the starting point of design is shifting from blank canvas to natural language. Further validation of the full-stack AI design trend.<br><small>Source: <a href="https://dcthemedian.substack.com/p/what-81000-people-want-from-ai">DataCamp Median</a> | <a href="https://stitch.withgoogle.com/">Google Stitch</a></small></li><li><strong>Anthropic Publishes Largest AI User Study: 81,000 Voices</strong> — Anthropic interviewed 81,000 Claude users across 159 countries in 70 languages. Key findings: 33% view AI as a learning tool, 17% worry about cognitive atrophy, 16% value emotional support, 12% fear dependence. The core tension for AI product design: the pull between "augmentation" and "dependency."<br><small>Source: <a href="https://www.anthropic.com/features/81k-interviews">Anthropic</a> | <a href="https://dcthemedian.substack.com/p/what-81000-people-want-from-ai">DataCamp Median</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI creativity\'s "middle compression" effect: eliminating mediocre creativity while amplifying the scarcity of exceptional talent</li><li>"Vibe Design" = design\'s next paradigm shift from pixel manipulation to natural language</li><li>The augmentation-dependency paradox: the core UX challenge for all AI products</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>These three stories together map 2026\'s most important shift in creative industries: AI is redistributing the value curve of creativity.</strong> The 100K-person study reveals AI creativity is flat — stable 70/100 output, rarely breaking 90. Human creativity is long-tail: most at 50-70, but top 10% hits 95+. AI is making "good enough" creativity free while making "exceptional" creativity more scarce and valuable. Google Stitch\'s "Vibe Design" evolution confirms the shift: when design starts from natural language, the competitive advantage moves from execution ("can you build it?") to judgment ("do you know what to build?"). Anthropic\'s 81K study adds the psychological layer: 33% see AI as learning tool vs 17% fearing cognitive atrophy — the same users, different moments. The best AI products make users feel they\'re mastering AI, not being replaced by it. Figma\'s "Cooking with Constraints" framework gets this right. <strong>2026\'s creative paradox: AI democratizes creative output while creating creative elitism. The middle tier vanishes. Invest in what AI can\'t generate: unique perspective, deep user empathy, cross-domain insight.</strong></p></div>'
    },
    "cover": images.get("sciencedaily") or images.get("anthropic_81k") or "https://www.sciencedaily.com/images/1920/lightbulb-creativity-explosion.webp",
    "sources": [
        {
            "title": {"zh": "ScienceDaily: AI 可以让人类更有创造力", "en": "ScienceDaily: Scientists Discover AI Can Make Humans More Creative"},
            "url": "https://www.sciencedaily.com/releases/2026/03/260315004355.htm",
            "image": images.get("sciencedaily", "")
        },
        {
            "title": {"zh": "Anthropic: 8.1 万人想从 AI 中得到什么", "en": "Anthropic: What 81,000 People Want From AI"},
            "url": "https://www.anthropic.com/features/81k-interviews",
            "image": images.get("anthropic_81k", "")
        },
        {
            "title": {"zh": "DataCamp Median: AI 创造力、Stitch 与 Anthropic 调研深度分析", "en": "DataCamp Median: AI Creativity, Stitch & Anthropic Study Analysis"},
            "url": "https://dcthemedian.substack.com/p/what-81000-people-want-from-ai",
            "image": images.get("dcthemedian", "")
        },
        {
            "title": {"zh": "Google Stitch: AI 原生设计画布", "en": "Google Stitch: AI-Native Design Canvas"},
            "url": "https://stitch.withgoogle.com/",
            "image": images.get("stitch_vibe", "")
        }
    ]
}

tech_issue = {
    "date": "2026-03-28",
    "section": "tech",
    "title": {
        "zh": "Apple 计划在 iOS 27 中向竞争对手 AI 开放 Siri · Anthropic 成立研究院并引发 OpenAI「红色警报」 · ARM 发布新 AI 芯片预期年增数十亿美元收入 · Reflection AI $200 亿估值面临交付大考",
        "en": "Apple Plans to Open Siri to Rival AI in iOS 27 · Anthropic Institute Launch Triggers OpenAI 'Code Red' · ARM Unveils AI Chip Expecting Billions in Revenue · Reflection AI $20B Valuation Faces Delivery Test"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul><li><strong>Apple 将在 iOS 27 中向竞争对手 AI 开放 Siri</strong> — Bloomberg 的 Mark Gurman 报道，Apple 计划在 iOS 27 中让 Siri 成为一个 AI 枢纽：用户可以通过「Extensions」设置选择 Google Gemini、Anthropic Claude 等第三方 AI 助手来驱动 Siri，而不再局限于 OpenAI 的 ChatGPT。到时 Google 的 Gemini 将成为 AI Siri 的核心引擎之一。<strong>这是 Apple AI 战略的根本性转向——从「自研」到「平台化」，承认自己在 AI 模型层没有优势，转而用硬件+生态的护城河做 AI 分发平台。</strong>Apple 预计 2026 年仅从 AI 应用分发中就能获得超过 10 亿美元收入。<br><small>来源：<a href="https://www.reuters.com/business/apple-plans-open-siri-rival-ai-services-bloomberg-news-reports-2026-03-26/">Reuters</a> | <a href="https://www.iphoneincanada.ca/2026/03/26/apple-plans-to-open-siri-to-rival-ai-assistants-in-ios-27-overhaul/">iPhone in Canada</a> | <a href="https://www.bloomberg.com/news/articles/2026-03-26/apple-plans-to-open-up-siri-to-rival-ai-assistants-beyond-chatgpt-in-ios-27">Bloomberg</a></small></li><li><strong>Anthropic 成立研究院，OpenAI 内部拉响「红色警报」</strong> — Anthropic 本周发布了两个重磅动作：一是由联合创始人 Jack Clark 领导成立 Anthropic Institute（研究院），聚合机器学习工程师、经济学家和社会科学家，研究 AI 对就业、安全和社会的影响；二是发布了史上最大规模 AI 用户定性研究（81,000 人，159 国，70 种语言）。与此同时，WSJ 报道 OpenAI 内部负责应用的 Fidji Simo 将 Anthropic 的企业级优势称为「code red（红色警报）」，要求团队不要被「side quests（支线任务）」分心。两周后，OpenAI 宣布其非营利部门将投入 <strong>10 亿美元用于 AI 安全和社会风险研究</strong>——直接回应 Anthropic 的安全叙事。<br><small>来源：<a href="https://www.anthropic.com/news/the-anthropic-institute">Anthropic Institute</a> | <a href="https://www.anthropic.com/features/81k-interviews">Anthropic 81K Study</a> | <a href="https://dcthemedian.substack.com/p/what-81000-people-want-from-ai">DataCamp Median</a></small></li><li><strong>ARM 发布新 AI 芯片，预计增加数十亿年收入</strong> — ARM 在 3 月 24 日发布了新一代 AI 芯片架构，预计将为公司增加数十亿美元的年收入。这与 Meta 自研 MTIA 芯片、NVIDIA 的 Vera Rubin 平台形成三足鼎立：ARM 做架构授权、Meta 做自研 ASIC、NVIDIA 做 GPU 生态。<strong>AI 芯片市场正在从「NVIDIA 独占」快速走向「多层竞争」——架构层（ARM）、通用 GPU 层（NVIDIA）、定制 ASIC 层（Meta/Google/Amazon）三线并行。</strong><br><small>来源：<a href="https://www.reuters.com/business/media-telecom/arm-unveils-new-ai-chip-expects-it-add-billions-annual-revenue-2026-03-24/">Reuters</a></small></li><li><strong>Reflection AI $200 亿估值面临交付大考</strong> — NVIDIA 支持的 Reflection AI 正在寻求 $250 亿估值融资，但其核心的开源前沿模型至今未公开发布。AInvest 的分析指出，该公司 2025 年 10 月以 $80 亿估值融资 $20 亿，承诺发布可与闭源实验室竞争的开放权重模型。然而截至 2026 年 3 月，模型仍未发布。<strong>这可能是 AI 行业「估值泡沫」的一个标志性案例——融资速度远超交付速度。</strong><br><small>来源：<a href="https://www.ainvest.com/news/reflection-ai-faces-critical-march-2026-test-20-billion-valuation-hinges-public-model-release-2603/">AInvest</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>Apple 从「AI 自研」转向「AI 分发平台」</strong>：承认模型层劣势，用 10 亿+设备的分发能力做 AI 枢纽</li><li><strong>Anthropic vs OpenAI 进入「全面竞争」</strong>：从模型到研究院到安全叙事，两家公司的竞争维度全面扩展</li><li><strong>AI 芯片三层竞争格局成型</strong>：ARM（架构） + NVIDIA（GPU） + 自研 ASIC（Meta/Google）</li><li><strong>AI 估值泡沫信号</strong>：Reflection AI 的 $200 亿估值 vs 零公开模型，融资 ≠ 交付</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Apple 开放 Siri 给竞争对手 AI 这件事，表面上是一个产品更新，实质上是 AI 产业权力结构的一次重大重组。</strong></p><p>先理清 Apple 的逻辑。过去 18 个月，Apple Intelligence 的表现让整个行业失望——Siri 与 ChatGPT 的整合体验平庸，自研模型在能力上远落后于 GPT-5.4 和 Claude。Apple 做了一个罕见的战略认怂：<strong>承认自己在 AI 模型层没有优势，转而利用 10 亿+设备的硬件触达做 AI 分发平台。</strong>这和 App Store 的逻辑完全一致——Apple 不需要做最好的 App，它只需要拥有最好的 App 分发渠道。iOS 27 中 Siri 变成「AI 枢纽」后，Google、Anthropic、OpenAI 都成了 Apple 生态的供应商，Apple 坐收平台税。预计 2026 年仅 AI 分发收入就超过 10 亿美元——这是不写一行模型代码就能赚到的钱。</p><p>但这件事还有更深的含义。当用户可以在 Siri 中自由切换 AI 助手时，AI 模型之间的竞争将变得前所未有地直接和残酷。<strong>想象一下：你在 iPhone 上问一个问题，Siri 先用 Claude 回答，你不满意，切换到 Gemini——这种「一键比较」的体验会极大加速 AI 模型的同质化竞争。</strong>对 OpenAI 来说，失去 Siri 的独占地位意味着失去 iPhone 用户的默认入口——这才是 Fidji Simo 拉响「code red」的真正原因。</p><p>说到 OpenAI 的焦虑。Anthropic 本周的组合拳——研究院 + 81K 用户研究——打得非常精准。Jack Clark 领导的 Anthropic Institute 不只是一个研究机构，它是一个「安全叙事的制度化」：通过聚合经济学家和社会科学家，Anthropic 把「负责任的 AI」从 PR 话术变成了组织架构。OpenAI 两周后宣布 10 亿美元安全研究投入，看似大手笔，但节奏上已经是在追赶。<strong>AI 行业的竞争正在从「谁的模型更强」扩展到「谁的安全故事更可信」——这对企业客户的选择影响巨大。</strong></p><p>ARM 的新芯片和 Reflection AI 的估值故事则揭示了 AI 基础设施层的两个平行现实。ARM 那边是实打实的——新架构、可量化的收入预期、与整个移动+边缘计算生态的协同。这进一步印证了昨天讨论的 AI 芯片多层竞争格局：ARM 做架构授权（低风险高利润），NVIDIA 做通用 GPU（高性能高溢价），Meta/Google 做定制 ASIC（内部优化降成本）。三者不是替代关系，而是在 AI 计算的不同层面各取所需。</p><p>Reflection AI 那边则是另一个故事。$80 亿 → $200 亿 → 追求 $250 亿估值，但核心承诺——开源前沿模型——至今没兑现。这让我想起 2021 年加密货币的「白皮书融资」时代：估值基于愿景而非交付。<strong>Reflection AI 可能最终交付一个优秀的模型，但如果它在 2026 年上半年仍然无法发布，它将成为 AI 行业「估值泡沫」的标志性案例。</strong>NVIDIA 的背书不是质量保证——它只是说明 NVIDIA 在对冲自己的生态风险。投资者应该问一个简单的问题：如果你的公司估值 $200 亿，你的产品在哪里？</p></div>',
        "en": '<h3>📌 AI × Tech</h3><ul><li><strong>Apple to Open Siri to Rival AI Assistants in iOS 27</strong> — Bloomberg\'s Mark Gurman reports Apple plans to turn Siri into an AI hub in iOS 27, letting users choose Google Gemini, Anthropic Claude, and other AI assistants via Extensions settings. A fundamental strategic pivot: Apple admits model-layer weakness, leverages 1B+ device distribution as an AI platform. Expected $1B+ in AI distribution revenue in 2026.<br><small>Source: <a href="https://www.reuters.com/business/apple-plans-open-siri-rival-ai-services-bloomberg-news-reports-2026-03-26/">Reuters</a> | <a href="https://www.iphoneincanada.ca/2026/03/26/apple-plans-to-open-siri-to-rival-ai-assistants-in-ios-27-overhaul/">iPhone in Canada</a> | <a href="https://www.bloomberg.com/news/articles/2026-03-26/apple-plans-to-open-up-siri-to-rival-ai-assistants-beyond-chatgpt-in-ios-27">Bloomberg</a></small></li><li><strong>Anthropic Launches Institute, Triggers OpenAI "Code Red"</strong> — Anthropic launched the Anthropic Institute led by co-founder Jack Clark (ML engineers + economists + social scientists studying AI impact) and published the largest qualitative AI study (81K users, 159 countries, 70 languages). WSJ reports OpenAI\'s Fidji Simo called Anthropic\'s enterprise lead a "code red." OpenAI responded with $1B nonprofit safety research commitment.<br><small>Source: <a href="https://www.anthropic.com/news/the-anthropic-institute">Anthropic</a> | <a href="https://dcthemedian.substack.com/p/what-81000-people-want-from-ai">DataCamp Median</a></small></li><li><strong>ARM Unveils New AI Chip, Expects Billions in Annual Revenue</strong> — ARM\'s new AI chip architecture forms a three-layer competition: ARM (architecture licensing), NVIDIA (GPU ecosystem), custom ASICs (Meta/Google/Amazon). The AI chip market is rapidly moving from NVIDIA monopoly to multi-layer competition.<br><small>Source: <a href="https://www.reuters.com/business/media-telecom/arm-unveils-new-ai-chip-expects-it-add-billions-annual-revenue-2026-03-24/">Reuters</a></small></li><li><strong>Reflection AI $20B Valuation Faces Delivery Test</strong> — NVIDIA-backed Reflection AI seeks $25B valuation but its core open-weight frontier model remains unreleased since $2B raise at $8B in October 2025. A potential landmark case of AI valuation bubble — fundraising velocity far exceeding delivery.<br><small>Source: <a href="https://www.ainvest.com/news/reflection-ai-faces-critical-march-2026-test-20-billion-valuation-hinges-public-model-release-2603/">AInvest</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Apple pivots from AI self-reliance to AI distribution platform (App Store model for AI)</li><li>Anthropic vs OpenAI enters full-spectrum competition: models, research institutes, safety narratives</li><li>AI chip three-layer competition: ARM (architecture) + NVIDIA (GPU) + custom ASIC (Meta/Google)</li><li>AI valuation bubble signal: Reflection AI\'s $20B valuation vs zero public models</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Apple opening Siri to rival AI services looks like a product update but is actually a major restructuring of AI industry power.</strong> Apple\'s logic mirrors the App Store: you don\'t need the best AI, you need the best AI distribution channel. iOS 27 turns Siri into an AI hub where Google, Anthropic, and OpenAI become suppliers paying platform tax. The deeper implication: when users can one-click compare AI assistants through Siri, model competition becomes brutally direct — this is why OpenAI\'s Fidji Simo declared "code red." Anthropic\'s combo punch (Institute + 81K study) institutionalizes the safety narrative, forcing OpenAI to chase with $1B in safety research. Competition is expanding from "whose model is stronger" to "whose safety story is more credible." ARM\'s chip and Reflection AI\'s valuation reveal parallel realities in AI infrastructure: ARM delivers real architecture with quantifiable revenue; Reflection AI pursues $25B valuation with zero shipped models. <strong>If Reflection can\'t release by mid-2026, it becomes the poster child for AI\'s valuation bubble.</strong></p></div>'
    },
    "cover": images.get("reuters_apple") or images.get("iphoneincanada") or "",
    "sources": [
        {
            "title": {"zh": "Reuters: Apple 计划向竞争对手 AI 开放 Siri", "en": "Reuters: Apple Plans to Open Siri to Rival AI Services"},
            "url": "https://www.reuters.com/business/apple-plans-open-siri-rival-ai-services-bloomberg-news-reports-2026-03-26/",
            "image": images.get("reuters_apple", "")
        },
        {
            "title": {"zh": "Bloomberg: Apple iOS 27 将开放 Siri 给第三方 AI", "en": "Bloomberg: Apple Plans to Open Siri to Rival AI Assistants in iOS 27"},
            "url": "https://www.bloomberg.com/news/articles/2026-03-26/apple-plans-to-open-up-siri-to-rival-ai-assistants-beyond-chatgpt-in-ios-27",
            "image": ""
        },
        {
            "title": {"zh": "Anthropic Institute: AI 对社会影响的研究机构", "en": "Anthropic Institute: Research on AI's Social Impact"},
            "url": "https://www.anthropic.com/news/the-anthropic-institute",
            "image": images.get("anthropic_inst", "")
        },
        {
            "title": {"zh": "Reuters: ARM 发布新 AI 芯片", "en": "Reuters: ARM Unveils New AI Chip"},
            "url": "https://www.reuters.com/business/media-telecom/arm-unveils-new-ai-chip-expects-it-add-billions-annual-revenue-2026-03-24/",
            "image": images.get("reuters_arm", "")
        },
        {
            "title": {"zh": "AInvest: Reflection AI $200 亿估值面临交付考验", "en": "AInvest: Reflection AI $20B Valuation Faces Delivery Test"},
            "url": "https://www.ainvest.com/news/reflection-ai-faces-critical-march-2026-test-20-billion-valuation-hinges-public-model-release-2603/",
            "image": images.get("reflection_ai", "")
        }
    ]
}

issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("Done! Added 2 issues for 2026-03-28.")
