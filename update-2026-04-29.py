#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rex Daily Digest - 2026-04-29"""
import json, os

ISSUES_PATH = os.path.join(os.path.dirname(__file__), "issues.json")

with open(ISSUES_PATH, "r", encoding="utf-8") as f:
    issues = json.load(f)

new_issues = [
    {
        "date": "2026-04-29",
        "section": "design",
        "title": {
            "zh": "Canva AI「巴勒斯坦→乌克兰」替换丑闻：当设计工具的偏见被写进像素，AI 辅助设计的信任危机正式到来",
            "en": "Canva AI 'Palestine-to-Ukraine' Swap Scandal: When Bias Gets Baked Into Pixels, the Trust Crisis for AI-Assisted Design Has Officially Arrived"
        },
        "content": {
            "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Canva AI 工具被曝自动将「Palestine」替换为「Ukraine」，引发全球争议</strong> — PetaPixel 和多家媒体报道，用户发现 Canva 的 AI 设计助手在处理含有「Palestine」文字的设计时，自动将其替换为「Ukraine」。<strong>Canva 已确认问题并修复，同时宣布对其 AI 系统进行全面审计</strong>。这不是简单的技术 bug——它暴露了 AI 设计工具在训练数据和内容过滤层面可能存在的系统性偏见。当一个被全球 2 亿用户使用的设计平台的 AI 功能开始「改写」用户意图时，设计工具的中立性问题被推到了聚光灯下。<br><small>来源：<a href=\"https://petapixel.com/2026/04/27/canvas-new-ai-powered-tool-caught-swapping-palestine-for-ukraine/\">PetaPixel</a></small></li><li><strong>Homestyler 在米兰 ADI 设计博物馆举办首届 AIDA 全球 AI 设计大奖</strong> — AI 室内设计平台 Homestyler 在米兰设计周期间举办了首届 AIDA（AI Design Awards）全球大奖。<strong>这是全球首个专门面向 AI 辅助设计作品的国际级奖项</strong>，标志着 AI 设计从「工具」层面正式进入「作品评价体系」——行业开始认真讨论「AI 辅助的设计作品是否值得被独立评审和表彰」这个问题。<br><small>来源：<a href=\"https://www.eqs-news.com/news/corporate/homestyler-hosts-aida-global-ai-design-awards-ceremony-at-milans-adi-design-museum/2325155\">EQS News</a></small></li><li><strong>EU 要求 Google 开放 Android AI 助手接口，第三方 AI 设计工具或将获得系统级权限</strong> — 欧盟委员会裁定 Google 必须让第三方 AI 服务获得与 Gemini 同等的 Android 系统级访问权限，包括热词唤醒、屏幕上下文读取和本地模型运行权限。<strong>这对 AI 设计工具意味着：未来 Canva、Adobe Express 等移动端设计应用的 AI 功能可以获得与 Google 自家产品同等的系统级集成能力</strong>。Google 称此举为「不必要的干预」，最终裁决将于 7 月 27 日前做出。<br><small>来源：<a href=\"https://arstechnica.com/ai/2026/04/europe-could-force-google-to-open-android-to-other-ai-assistants/\">Ars Technica</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 设计工具的「信任危机」</strong>：Canva 偏见事件将推动行业建立 AI 辅助设计的审计和透明度标准</li><li><strong>AI 设计进入「奖项时代」</strong>：AIDA 大奖标志着行业开始为 AI 辅助作品建立独立评价体系</li><li><strong>移动端 AI 设计工具的平权运动</strong>：EU 的裁决可能打破 Google 在移动端 AI 集成的垄断</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Canva 的「巴勒斯坦→乌克兰」替换丑闻，表面上看是一个技术故障，但它打开了一个 AI 设计工具行业一直在回避的潘多拉魔盒：谁来为 AI 的「设计决策」负责？</strong></p><p>让我们把这件事放在正确的框架里理解。Canva 不是一个边缘产品——它是全球超过 2 亿活跃用户的设计平台，也是过去两年 AI 功能最激进的设计工具之一（还记得上个月 Canva 刚发布了 agentic AI 助手吗？）。当这样一个平台的 AI 功能自动将一个国家的名字替换为另一个国家的名字，这已经不是「oops，训练数据有偏差」可以敷衍过去的了。<strong>这是一个根本性的产品伦理问题：AI 设计工具应该在多大程度上「理解」并「修改」用户的设计意图？</strong></p><p>把 Canva 事件和 AIDA 大奖放在一起看，一个有趣的张力浮现了。一边是 AI 设计作品正在获得行业正式认可（米兰设计周上的首届 AI 设计大奖），另一边是 AI 设计工具的底层系统被发现可能在悄悄篡改用户的创作意图。<strong>这两件事指向同一个问题：当 AI 越来越深入地嵌入设计流程时，我们需要一套全新的「AI 设计伦理框架」</strong>——不只是关于版权和归属，更是关于意图忠实度、偏见检测、和工具透明度。</p><p>再看 EU 对 Android AI 开放性的要求。这条新闻被大多数设计媒体忽视了，但它的长期影响可能比 Canva 丑闻大得多。<strong>目前在移动端，AI 设计工具（Canva、Adobe Express、甚至 Figma 移动版）的 AI 功能受限于操作系统层面的权限壁垒</strong>——Gemini 可以读取屏幕上下文、调用本地模型、唤醒系统级快捷方式，但第三方工具不行。EU 的裁决如果落地，意味着 Canva 的 AI 可以像 Gemini 一样在系统级别运行——在任何应用里直接调用设计功能，读取当前屏幕内容来做上下文感知的设计建议。这会让移动端 AI 设计体验产生质的飞跃。</p><p><strong>三条新闻连在一起，2026 年 AI 设计行业的核心矛盾清晰可见：能力在爆发（AIDA 大奖、系统级集成），但信任基础在动摇（Canva 偏见）。我的预测是：Canva 事件将成为 AI 设计工具行业的「剑桥分析时刻」——在此之后，每个 AI 设计平台都将被要求公开其内容过滤策略、偏见审计报告、和用户意图保护机制。这不是坏事——它会让这个行业更成熟。就像 GDPR 最终让隐私保护变成了产品竞争力，AI 设计伦理标准最终也会成为差异化优势。那些提前投资透明度和审计能力的工具（比如已经在做开源审计的 ComfyUI），将在信任经济中胜出。</strong></p></div>",
            "en": "<h3>📌 AI × Design</h3><ul><li><strong>Canva AI Tool Caught Automatically Swapping 'Palestine' for 'Ukraine'</strong> — PetaPixel and multiple outlets report users discovered Canva's AI design assistant automatically replaced 'Palestine' with 'Ukraine' in designs. <strong>Canva confirmed the issue, applied a fix, and announced a full AI system audit</strong>. This exposes potential systematic bias in AI design tools' training data and content filters. When a platform used by 200M+ users starts 'rewriting' user intent, the neutrality of design tools comes under the spotlight.<br><small>Source: <a href=\"https://petapixel.com/2026/04/27/canvas-new-ai-powered-tool-caught-swapping-palestine-for-ukraine/\">PetaPixel</a></small></li><li><strong>Homestyler Hosts First AIDA Global AI Design Awards at Milan's ADI Design Museum</strong> — AI interior design platform Homestyler held the first AIDA (AI Design Awards) during Milan Design Week. <strong>This is the world's first international award specifically for AI-assisted design work</strong>, marking AI design's entry into formal evaluation systems.<br><small>Source: <a href=\"https://www.eqs-news.com/news/corporate/homestyler-hosts-aida-global-ai-design-awards-ceremony-at-milans-adi-design-museum/2325155\">EQS News</a></small></li><li><strong>EU Orders Google to Open Android AI Assistant Access to Third Parties</strong> — The European Commission ruled Google must give third-party AI services the same system-level Android access as Gemini, including hot-word activation, screen context reading, and local model execution. <strong>For AI design tools: Canva, Adobe Express, and others could gain system-level integration on mobile equal to Google's own products</strong>. Final ruling due by July 27.<br><small>Source: <a href=\"https://arstechnica.com/ai/2026/04/europe-could-force-google-to-open-android-to-other-ai-assistants/\">Ars Technica</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Design Tools' 'Trust Crisis'</strong>: The Canva bias incident will push the industry toward audit and transparency standards</li><li><strong>AI Design Enters the 'Awards Era'</strong>: AIDA marks formal evaluation frameworks for AI-assisted work</li><li><strong>Mobile AI Design Tool Parity</strong>: EU ruling could break Google's monopoly on mobile AI integration</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Canva's 'Palestine-to-Ukraine' swap scandal opens a Pandora's box the AI design industry has been avoiding: who's responsible for AI's 'design decisions'?</strong></p><p>Canva isn't a fringe product—it's a 200M+ active user platform and one of the most aggressive AI adopters among design tools. When its AI automatically replaces one country's name with another, this goes beyond 'oops, training data bias.' <strong>This is a fundamental product ethics question: to what extent should AI design tools 'understand' and 'modify' user intent?</strong></p><p>Pair the Canva scandal with the AIDA awards and an interesting tension emerges. On one hand, AI design work is gaining formal recognition (first AI design awards at Milan Design Week). On the other, AI systems are caught covertly altering creative intent. <strong>Both point to the same need: a new 'AI design ethics framework'</strong>—not just about copyright, but about intent fidelity, bias detection, and tool transparency.</p><p>The EU's Android AI openness ruling got ignored by most design media, but its long-term impact may dwarf the Canva scandal. <strong>Currently on mobile, AI design tools face OS-level permission walls</strong>—Gemini gets screen context, local models, system shortcuts; third parties don't. If the EU ruling lands, Canva's AI could run at system level—invoking design functions from any app, reading screen content for context-aware suggestions.</p><p><strong>Connected: AI design's core contradiction in 2026 is clear—capabilities are exploding (AIDA, system-level integration) while trust foundations are cracking (Canva bias). My prediction: this becomes AI design's 'Cambridge Analytica moment.' Every AI design platform will be required to publish content filtering policies, bias audit reports, and intent protection mechanisms. This will mature the industry—just as GDPR turned privacy into competitive advantage, AI design ethics standards will become differentiation. Tools that invest early in transparency (like open-source ComfyUI) will win in the trust economy.</strong></p></div>"
        },
        "cover": "https://cdn.arstechnica.net/wp-content/uploads/2025/06/Android-IO-1152x648.jpg",
        "sources": [
            {
                "title": {
                    "zh": "Canva AI 工具被曝将「Palestine」自动替换为「Ukraine」",
                    "en": "Canva's New AI-Powered Tool Caught Swapping 'Palestine' for 'Ukraine'"
                },
                "url": "https://petapixel.com/2026/04/27/canvas-new-ai-powered-tool-caught-swapping-palestine-for-ukraine/",
                "image": ""
            },
            {
                "title": {
                    "zh": "Homestyler 在米兰 ADI 设计博物馆举办首届 AIDA 全球 AI 设计大奖",
                    "en": "Homestyler Hosts AIDA Global AI Design Awards at Milan's ADI Design Museum"
                },
                "url": "https://www.eqs-news.com/news/corporate/homestyler-hosts-aida-global-ai-design-awards-ceremony-at-milans-adi-design-museum/2325155",
                "image": ""
            },
            {
                "title": {
                    "zh": "EU 要求 Google 开放 Android 系统给第三方 AI 助手",
                    "en": "EU Tells Google to Open Up AI on Android"
                },
                "url": "https://arstechnica.com/ai/2026/04/europe-could-force-google-to-open-android-to-other-ai-assistants/",
                "image": "https://cdn.arstechnica.net/wp-content/uploads/2025/06/Android-IO-1152x648.jpg"
            }
        ]
    },
    {
        "date": "2026-04-29",
        "section": "tech",
        "title": {
            "zh": "AI 巨头「开放赛季」：Google 最高 400 亿美元押注 Anthropic、OpenAI 正式登陆 AWS、Musk-Altman 世纪审判开庭——竞争格局从「独家绑定」转向「多云博弈」",
            "en": "AI Giants' 'Open Season': Google Bets Up to $40B on Anthropic, OpenAI Officially Lands on AWS, Musk-Altman Trial Begins — Competition Shifts from 'Exclusive Lock-in' to 'Multi-Cloud Game Theory'"
        },
        "content": {
            "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Google 最高投资 400 亿美元于 Anthropic，AI 投资规模再创纪录</strong> — Bloomberg 报道，Google 将至少投资 100 亿美元于 Anthropic，如果后者达到特定业绩目标，总投资额可升至 400 亿美元。<strong>此次投资对 Anthropic 估值 3500 亿美元，与 Amazon 数天前 50 亿美元的初始投资估值一致</strong>。Anthropic 近期因 Claude Code 和 Claude Cowork 的爆发式增长面临严重的算力供给缺口，Google 和 Amazon 的投资本质上是「用芯片和算力换股权」。<br><small>来源：<a href=\"https://arstechnica.com/ai/2026/04/google-will-invest-as-much-as-40-billion-in-anthropic/\">Ars Technica</a></small></li><li><strong>OpenAI 正式登陆 Amazon AWS，Microsoft 独家时代终结</strong> — 在 Microsoft-OpenAI 修订协议生效后，Amazon CEO Andy Jassy 宣布 OpenAI 模型将在未来数周内通过 AWS Bedrock 直接提供服务。<strong>Microsoft 保留 OpenAI 模型的非独家授权至 2032 年，但收入分成将有上限且仅保证到 2030 年</strong>。OpenAI 首席营收官透露，此前 Microsoft 的独家条款「限制了我们在企业客户中的覆盖范围」，客户对在 AWS 上运行 OpenAI 模型的需求「坦率地说令人震惊」。<br><small>来源：<a href=\"https://arstechnica.com/ai/2026/04/no-longer-exclusive-microsoft-agrees-to-let-openai-see-other-cloud-providers/\">Ars Technica</a></small></li><li><strong>Musk vs Altman 世纪审判正式开庭，将决定 OpenAI 的未来</strong> — Elon Musk 起诉 OpenAI 和 Sam Altman 的审判在联邦法院开庭。<strong>审判核心问题：OpenAI 从非盈利转向营利实体是否违反了其创始承诺</strong>。这场审判的结果可能决定 OpenAI 能否完成其盈利化转型——如果 Musk 胜诉，OpenAI 的 500 亿 Amazon 交易、400 亿 SoftBank 融资等一系列商业安排都可能面临法律挑战。<br><small>来源：<a href=\"https://arstechnica.com/tech-policy/2026/04/musk-and-altman-face-off-in-trial-that-will-determine-openais-future/\">Ars Technica</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 投资进入「芯片换股权」模式</strong>：Google 400 亿、Amazon 50 亿投 Anthropic——科技巨头用算力基础设施换 AI 公司股权</li><li><strong>AI 模型分发「去独家化」</strong>：OpenAI 上 AWS、Anthropic 同时接受 Google 和 Amazon 投资——多云分发成为标配</li><li><strong>OpenAI 面临「内忧外患」</strong>：外有 Musk 审判威胁盈利化转型，内有 Microsoft 自研模型降低依赖</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天的三条新闻合在一起，画出了一张 2026 年 AI 行业最清晰的权力版图：「独家绑定」时代结束了，「多云博弈」时代开始了。而这对设计行业的影响比大多数人意识到的要深远得多。</strong></p><p>先说数字。Google 最高 400 亿美元投 Anthropic，加上 Amazon 的 50 亿，再加上上周 Microsoft-OpenAI 修订协议——这意味着什么？<strong>意味着 AI 模型公司和云平台之间的关系，正在从「婚姻」变成「约会」</strong>。Anthropic 同时接受 Google 和 Amazon 的钱。OpenAI 同时在 Azure 和 AWS 上卖服务。每个人都在和每个人约会，没有人承诺独家。这在商业上完全合理——对 Anthropic 来说，Google 给芯片、Amazon 也给芯片，为什么只要一家的？对 OpenAI 来说，企业客户在 AWS 上，为什么要把自己锁在 Azure 里？</p><p>但这种「去独家化」对终端用户——包括设计师——的影响是双刃剑。好的一面：<strong>你用的 AI 设计工具将获得更多模型选择</strong>。当 OpenAI 和 Anthropic 的模型都可以在多个云上运行时，Figma 不再被绑定到某一家模型提供商，它可以为不同功能选择最优模型。坏的一面：<strong>模型切换和兼容性问题将成为设计工具的新痛点</strong>。你在 Figma 里用 Claude 生成的组件，和用 GPT 生成的组件，可能有微妙的风格差异——这对追求品牌一致性的设计团队是个真问题。</p><p>Musk vs Altman 的审判则是悬在这一切之上的达摩克利斯之剑。<strong>如果 Musk 胜诉——哪怕是部分胜诉——OpenAI 的盈利化转型就会受阻</strong>。这会直接影响 OpenAI 向 AWS 扩张的计划、500 亿 Amazon 交易的执行、以及所有基于 OpenAI 模型的企业级 AI 产品的稳定性。对设计行业的翻译：如果你的工具链依赖 OpenAI 的模型，Musk 审判的结果就是你的供应链风险。这不是杞人忧天——这是正在进行的法律程序。</p><p><strong>把今天的新闻和昨天的连起来看，一个完整的叙事浮现了：Microsoft-OpenAI 结束独家（4/28），OpenAI 正式登陆 AWS（4/28-29），Google 400 亿押注 Anthropic（4/29），同时 Musk 审判启动（4/28）。这四件事在一周内发生不是巧合——它们是 AI 行业从「创业冲刺」阶段进入「地缘政治 + 法律博弈」阶段的标志性事件。对设计师来说，2026 年最重要的技能不再是「学会用哪个 AI 工具」，而是「理解 AI 工具背后的权力结构，并保持自己的灵活性」。今天你 all-in Figma + OpenAI，明天 Figma 可能切换到 Claude，后天 OpenAI 可能因为审判被迫重组。唯一不变的是你的设计判断力和对多工具的适应能力。</strong></p></div>",
            "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Google to Invest Up to $40 Billion in Anthropic, Setting New AI Investment Record</strong> — Bloomberg reports Google will invest at least $10B in Anthropic, potentially rising to $40B based on performance targets. <strong>The deal values Anthropic at $350B, matching Amazon's $5B investment days earlier</strong>. Both are essentially 'chips-for-equity' deals as Anthropic faces severe compute shortages from Claude Code and Claude Cowork's explosive growth.<br><small>Source: <a href=\"https://arstechnica.com/ai/2026/04/google-will-invest-as-much-as-40-billion-in-anthropic/\">Ars Technica</a></small></li><li><strong>OpenAI Officially Lands on Amazon AWS as Microsoft Exclusivity Ends</strong> — Following the amended Microsoft-OpenAI agreement, Amazon CEO Andy Jassy announced OpenAI models will be available on AWS Bedrock within weeks. <strong>Microsoft retains a non-exclusive license to OpenAI's IP through 2032, but revenue sharing is now capped and only guaranteed through 2030</strong>. OpenAI's CRO revealed demand for running OpenAI models on AWS has been 'frankly staggering.'<br><small>Source: <a href=\"https://arstechnica.com/ai/2026/04/no-longer-exclusive-microsoft-agrees-to-let-openai-see-other-cloud-providers/\">Ars Technica</a></small></li><li><strong>Musk vs Altman Trial Begins, Could Determine OpenAI's Future</strong> — The trial over whether OpenAI's shift from nonprofit to for-profit violated its founding commitments has officially begun. <strong>If Musk wins—even partially—OpenAI's $50B Amazon deal, $40B SoftBank raise, and broader commercialization could face legal challenges</strong>.<br><small>Source: <a href=\"https://arstechnica.com/tech-policy/2026/04/musk-and-altman-face-off-in-trial-that-will-determine-openais-future/\">Ars Technica</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Investment Enters 'Chips-for-Equity' Mode</strong>: Google $40B + Amazon $5B into Anthropic—tech giants trade compute infrastructure for AI company stakes</li><li><strong>AI Model Distribution 'De-Exclusivizes'</strong>: OpenAI on AWS, Anthropic taking both Google and Amazon money—multi-cloud becomes default</li><li><strong>OpenAI Faces 'Internal and External Threats'</strong>: Musk trial threatens commercialization; Microsoft builds in-house alternatives</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Today's three stories together draw the clearest power map of 2026 AI: the 'exclusive lock-in' era is over, the 'multi-cloud game theory' era has begun.</strong></p><p>The numbers: Google up to $40B into Anthropic, Amazon's $5B, plus last week's Microsoft-OpenAI amended deal. <strong>AI model companies and cloud platforms are shifting from 'marriage' to 'dating'</strong>. Anthropic takes money from both Google and Amazon. OpenAI sells on both Azure and AWS. Everyone dates everyone; nobody commits to exclusivity.</p><p>This 'de-exclusivization' is double-edged for end users including designers. Upside: <strong>AI design tools gain more model choices</strong>—Figma no longer locked to one provider, can pick the best model per feature. Downside: <strong>model switching and compatibility become new pain points</strong>. Components generated with Claude vs GPT may have subtle style differences—a real problem for brand consistency.</p><p>The Musk-Altman trial is the Sword of Damocles over everything. <strong>If Musk wins even partially, OpenAI's commercialization stalls</strong>—impacting AWS expansion, the $50B Amazon deal, and every enterprise AI product built on OpenAI models. Translation for design: if your toolchain depends on OpenAI, this trial is your supply chain risk.</p><p><strong>Connecting today with yesterday: Microsoft-OpenAI end exclusivity (4/28), OpenAI lands on AWS (4/28-29), Google bets $40B on Anthropic (4/29), Musk trial launches (4/28). Four events in one week isn't coincidence—it marks AI's transition from 'startup sprint' to 'geopolitical + legal game theory.' For designers in 2026, the most important skill isn't 'which AI tool to learn' but 'understanding power structures behind AI tools and maintaining flexibility.' Today you're all-in on Figma + OpenAI; tomorrow Figma might switch to Claude; next week OpenAI might restructure from trial fallout. The only constant is your design judgment and multi-tool adaptability.</strong></p></div>"
        },
        "cover": "https://cdn.arstechnica.net/wp-content/uploads/2026/04/TPU-8i-rack-2560x1440.jpg",
        "sources": [
            {
                "title": {
                    "zh": "Google 最高投资 400 亿美元于 Anthropic",
                    "en": "Google Will Invest as Much as $40 Billion in Anthropic"
                },
                "url": "https://arstechnica.com/ai/2026/04/google-will-invest-as-much-as-40-billion-in-anthropic/",
                "image": "https://cdn.arstechnica.net/wp-content/uploads/2026/04/TPU-8i-rack-2560x1440.jpg"
            },
            {
                "title": {
                    "zh": "OpenAI 正式登陆 AWS，Microsoft 独家时代终结",
                    "en": "No Longer Exclusive: Microsoft Agrees to Let OpenAI See Other Cloud Providers"
                },
                "url": "https://arstechnica.com/ai/2026/04/no-longer-exclusive-microsoft-agrees-to-let-openai-see-other-cloud-providers/",
                "image": "https://cdn.arstechnica.net/wp-content/uploads/2024/12/GettyImages-2153474326-1024x648.jpg"
            },
            {
                "title": {
                    "zh": "Musk 与 Altman 世纪审判开庭，将决定 OpenAI 的未来",
                    "en": "Musk and Altman Face Off in Trial That Will Determine OpenAI's Future"
                },
                "url": "https://arstechnica.com/tech-policy/2026/04/musk-and-altman-face-off-in-trial-that-will-determine-openais-future/",
                "image": "https://cdn.arstechnica.net/wp-content/uploads/2026/04/elon-and-sam-are-bffs-1152x648.jpg"
            }
        ]
    }
]

issues = new_issues + issues

with open(ISSUES_PATH, "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"Done. Total issues: {len(issues)}")
