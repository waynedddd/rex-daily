#!/usr/bin/env python3
"""Rex Daily update 2026-05-18 evening"""
import json, os, sys
import urllib.request
import urllib.error
import ssl
import re
from html.parser import HTMLParser

ctx = ssl.create_default_context()
ctx.load_default_certs()

def get_og_image(url):
    """Fetch og:image from a URL."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            html = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
        return m.group(1) if m else ""
    except:
        return ""

ISSUES_PATH = os.path.join(os.path.dirname(__file__), "issues.json")

# Load existing
with open(ISSUES_PATH, "r") as f:
    issues = json.load(f)

# New issues for 2026-05-18 evening
# Design: Figma State of the Designer 2026 + AI design tools explosion
# Tech: Google I/O 2026 eve - Gemini 3.1 Flash Live, Android XR, Gemini Intelligence

sources_design = [
    {
        "url": "https://www.figma.com/blog/state-of-the-designer-2026/",
        "title": {
            "zh": "Figma: State of the Designer 2026——设计师正在拥抱「混乱的中间地带」",
            "en": "Figma: State of the Designer 2026 — Designers Are Leaning Into the Messy Middle"
        }
    },
    {
        "url": "https://www.figma.com/blog/why-demand-for-designers-is-on-the-rise/",
        "title": {
            "zh": "Figma: 为什么设计师需求正在上升",
            "en": "Figma: Why Demand for Designers Is on the Rise"
        }
    },
    {
        "url": "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
        "title": {
            "zh": "Toools.design: 2026 年 UI/UX 设计师的 9 大 AI 工具深度评测",
            "en": "Toools.design: 9 Best AI Tools for UI/UX Designers in 2026: Deep Dive"
        }
    },
    {
        "url": "https://designlab.com/blog/ai-in-ux-product-design-trends-2026",
        "title": {
            "zh": "Designlab: 2026 年 AI 在 UX 和产品设计中的现状",
            "en": "Designlab: The State of AI in UX & Product Design: 2026"
        }
    }
]

sources_tech = [
    {
        "url": "https://www.androidcentral.com/phones/live/google-i-o-2026-live-blog-android-17-android-xr-glasses-and-all-the-gemini-ai-news",
        "title": {
            "zh": "Android Central: Google I/O 2026 实况——Android 17、Android XR 眼镜及 Gemini AI 全部新闻",
            "en": "Android Central: Google I/O 2026 Live Blog: Android 17, Android XR Glasses, and All the Gemini AI News"
        }
    },
    {
        "url": "https://sea.mashable.com/tech/45872/what-to-expect-from-google-io-2026-gemini-news-android-xr-glasses",
        "title": {
            "zh": "Mashable: Google I/O 2026 期待什么——Gemini 新闻和 Android XR 眼镜",
            "en": "Mashable: What to Expect from Google I/O 2026: Gemini News, Android XR Glasses"
        }
    },
    {
        "url": "https://pub.towardsai.net/google-i-o-2026-everything-google-is-about-to-announce-on-may-19-df54edefe634",
        "title": {
            "zh": "Towards AI: Google I/O 2026——Google 即将在 5 月 19 日宣布的一切",
            "en": "Towards AI: Google I/O 2026 — Everything Google Is About to Announce on May 19"
        }
    },
    {
        "url": "https://tech.yahoo.com/ai/gemini/articles/google-o-kicks-off-next-120000851.html",
        "title": {
            "zh": "Yahoo Tech: Google I/O 下周开幕——我们预期的三大公告",
            "en": "Yahoo Tech: Google I/O Kicks Off Next Week: The 3 Biggest Announcements We Expect"
        }
    }
]

# Fetch og:images
for s in sources_design + sources_tech:
    img = get_og_image(s["url"])
    s["image"] = img
    print(f"  og:image for {s['url'][:50]}... -> {img[:80] if img else '(none)'}")

design_cover = sources_design[0].get("image", "") or "https://cdn.sanity.io/images/599r6htc/regionalized/state-of-designer-2026.png"
tech_cover = sources_tech[0].get("image", "") or "https://www.androidcentral.com/sites/default/files/google-io-2026.jpg"

design_issue = {
    "date": "2026-05-18",
    "section": "design",
    "title": {
        "zh": "Figma「设计师现状 2026」报告揭示反直觉真相：AI 不是在取代设计师，而是在制造更多设计需求——但你需要的技能变了",
        "en": "Figma's 'State of the Designer 2026' Reveals a Counterintuitive Truth: AI Isn't Replacing Designers — It's Creating More Design Demand. But the Skills You Need Have Changed."
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Figma「State of the Designer 2026」报告发布：91% 设计师认为 AI 帮助他们做更有影响力的工作，设计招聘需求反而在上升</strong> — Figma 最新年度报告调研了全球设计师群体，核心发现是：AI 工具不仅没有减少设计师的需求，反而在推动设计招聘的加速。报告指出「在人人都能用 AI prompt 出一个原型的时代，craft（手艺）才是区分产品的关键」。91% 的设计师表示明确的目标和期望帮助他们做出最好的工作。配套研究「Why Demand for Designers Is on the Rise」进一步证实 AI 正在驱动设计招聘的新动力。<br><small>来源：<a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a> / <a href=\"https://www.figma.com/blog/why-demand-for-designers-is-on-the-rise/\">Figma: Why Demand for Designers Is on the Rise</a></small></li><li><strong>2026 AI 设计工具爆发：Figma Make、Flowstep、Motiff、Banani、UX Pilot 形成「AI 原生设计工具」新梯队</strong> — Toools.design 的深度评测覆盖了 9 款 AI 设计工具，揭示 2026 年的 AI 设计工具不再是「AI + 设计」的简单叠加，而是从底层重新思考设计流程：Flowstep 可以从文本生成完整用户旅程并一键导出 Figma；Motiff 直接输出 production-ready React/HTML 代码；UX Pilot 从用户研究到原型一站式完成。Designlab 总结 2026 趋势为「AI-augmented workflows + data-driven decision making」——设计不再只是「画」，而是「决策」。<br><small>来源：<a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">Toools.design</a> / <a href=\"https://designlab.com/blog/ai-in-ux-product-design-trends-2026\">Designlab</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 创造设计需求，而非消灭</strong>：Figma 报告用数据证明设计师需求在上升</li><li><strong>Craft 价值回归</strong>：当 AI 降低了设计的门槛，精细手艺反而成为差异化因素</li><li><strong>AI 原生设计工具新梯队成型</strong>：从 prompt-to-UI 到 research-to-prototype 的全栈覆盖</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Figma 这份报告来得恰到好处——就在整个行业弥漫着「AI 要干掉设计师」焦虑的时候，用数据给出了一个更 nuanced 的答案：AI 确实在改变设计师的角色，但改变的方向不是「消失」，而是「分层」。</strong></p><p>先说关键数字。「设计招聘需求在上升」这个结论听起来反直觉，但逻辑很清晰：<strong>当 AI 让「制作设计」的成本趋近于零，「需要设计的东西」就会爆炸式增长。</strong>这是经济学里的「杰文斯悖论」（Jevons Paradox）在设计领域的完美体现——效率提升不会减少需求，而是释放被压抑的需求。以前一个创业团队可能只做一个 landing page，现在他们可以让 AI 帮忙做 10 个变体进行 A/B 测试。总量在增加，但每个「设计」的单价和所需技能在变化。</p><p>更值得关注的是报告里那句话：「在人人都能 prompt 出原型的时代，craft 是区分产品的关键。」这和我上期日报分析的「执行层被压缩，审美判断力在升值」完全一致。但 Figma 的数据给了一个更精确的定义——<strong>2026 年设计师的核心竞争力不是「会用工具」，而是「知道什么是好的」</strong>。当 AI 可以在 5 秒内生成 20 个 dashboard 布局时，能判断「哪个布局最好、为什么好、怎么改到更好」的人才是不可替代的。</p><p>再看工具层面的变化。Flowstep 的「⌘C/⌘V 到 Figma」、Motiff 的「直出 React 代码」、UX Pilot 的「研究到原型一条龙」——这三个工具代表了 AI 设计工具的三个进化方向：<strong>无缝集成现有工具链（Flowstep）、直接跳过设计交付到代码（Motiff）、上游吞噬研究阶段（UX Pilot）</strong>。注意它们的共同点：都在试图减少「中间步骤」。传统设计流程是「研究 → 线框图 → 高保真 → 交互动效 → 开发 Spec → 代码」，现在每个环节之间的「人工翻译」都在被 AI 吃掉。</p><p>把 Figma 报告和工具爆发放在一起看，一个清晰的图景是：<strong>2026 年的设计行业正在经历「中产阶级空心化」</strong>——顶部（设计战略、系统定义、审美判断）和底部（AI 工具操作、prompt 工程）都有强需求，但中间层（手动制作高保真稿、切图、交互细节实现）正在快速萎缩。Figma 说「需求在上升」没有说谎，但这个「需求」的构成已经和两年前完全不同了。如果你还在用 2024 年的技能树来规划 2026 年的职业路径，你感受到的不会是「需求上升」，而是「被甩在身后」。</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Figma 'State of the Designer 2026' Report: 91% of Designers Say AI Helps Them Do Higher-Impact Work; Design Hiring Is Actually Rising</strong> — Figma's latest annual report finds AI tools aren't reducing demand for designers — they're accelerating design hiring. The key insight: \"In an era where anyone can use AI to prompt their way to a prototype, craft is what sets products apart.\" 91% of designers say clear goals help them do their best work. A companion study confirms AI is driving renewed momentum in design hiring.<br><small>Source: <a href=\"https://www.figma.com/blog/state-of-the-designer-2026/\">Figma Blog</a> / <a href=\"https://www.figma.com/blog/why-demand-for-designers-is-on-the-rise/\">Figma: Why Demand for Designers Is on the Rise</a></small></li><li><strong>2026 AI Design Tool Explosion: Figma Make, Flowstep, Motiff, Banani, UX Pilot Form a New 'AI-Native Design Tool' Tier</strong> — Toools.design's deep dive covers 9 AI tools reshaping design workflows: Flowstep generates complete user journeys from text with one-click Figma export; Motiff outputs production-ready React/HTML code; UX Pilot handles research-to-prototype end-to-end. Designlab summarizes 2026 as \"AI-augmented workflows + data-driven decision making\" — design is no longer about drawing, but deciding.<br><small>Source: <a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">Toools.design</a> / <a href=\"https://designlab.com/blog/ai-in-ux-product-design-trends-2026\">Designlab</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI creates design demand, not destroys it</strong>: Figma's data proves designer demand is rising</li><li><strong>Craft value returns</strong>: When AI lowers the design floor, fine craft becomes the differentiator</li><li><strong>AI-native design tool tier emerges</strong>: From prompt-to-UI to research-to-prototype full coverage</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Figma's report arrives at exactly the right moment — amid peak \"AI will kill designers\" anxiety, it offers a more nuanced data-backed answer: AI is changing the designer's role, but the direction isn't \"disappearance\" — it's \"stratification.\"</strong></p><p>The \"design hiring is rising\" finding sounds counterintuitive but follows clear logic: <strong>when AI makes \"creating design\" near-zero cost, \"things that need design\" explode.</strong> This is Jevons Paradox in design — efficiency gains don't reduce demand, they unlock suppressed demand. A startup that once made one landing page now A/B tests 10 AI-generated variants. Total volume grows, but the price and skills per \"design\" change.</p><p>The report's key line — \"in an era where anyone can prompt a prototype, craft sets products apart\" — aligns perfectly with my previous analysis. <strong>2026's core designer competency isn't \"using tools\" but \"knowing what's good.\"</strong> When AI generates 20 dashboard layouts in 5 seconds, the irreplaceable person is whoever can judge which is best, why, and how to improve it.</p><p>The tool landscape tells the same story. Flowstep (seamless Figma integration), Motiff (skip design deliverables, go straight to code), UX Pilot (absorb research upstream) — all reducing \"intermediate translation steps.\" The traditional flow of \"research → wireframe → hi-fi → interaction → dev spec → code\" is having every human-translation step eaten by AI.</p><p><strong>2026 design is experiencing \"middle-class hollowing\"</strong> — strong demand at the top (strategy, system definition, aesthetic judgment) and bottom (AI tool operation, prompt engineering), but the middle (manual hi-fi mockups, pixel specs, interaction implementation) is rapidly shrinking. Figma's \"demand is rising\" isn't wrong, but the composition of that demand is completely different from two years ago.</p></div>"
    },
    "cover": design_cover,
    "sources": sources_design
}

tech_issue = {
    "date": "2026-05-18",
    "section": "tech",
    "title": {
        "zh": "Google I/O 2026 明日开幕前夜：Gemini 3.1 Flash Live 抢跑发布、Android XR 眼镜确认亮相、「Gemini Intelligence」将 Android 从操作系统变成智能体系统",
        "en": "Google I/O 2026 Eve: Gemini 3.1 Flash Live Drops Early, Android XR Glasses Confirmed, 'Gemini Intelligence' Transforms Android from OS to Agent System"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Gemini 3.1 Flash Live 抢先发布：语音优先 AI 模型，理解口语、极速响应，Google I/O 前夜放出</strong> — Android Central 实况报道确认，Google 在 I/O 正式开幕前就发布了 Gemini 3.1 Flash Live——一个语音优先的 AI 模型，专注于「倾听用户语音、理解其含义、提供更快的语音交互」。这是 Google 对 OpenAI Advanced Voice Mode 的直接回应，也暗示明天 keynote 的核心叙事将围绕「对话式 AI 作为默认交互范式」展开。<br><small>来源：<a href=\"https://www.androidcentral.com/phones/live/google-i-o-2026-live-blog-android-17-android-xr-glasses-and-all-the-gemini-ai-news\">Android Central</a></small></li><li><strong>Android XR 眼镜确认在 Google I/O 2026 亮相：Google 的「空间计算 + AI Agent」赌注</strong> — Mashable 和 Yahoo Tech 确认 Android XR 智能眼镜将是明天 I/O 的硬件重头戏。不同于 Meta Ray-Ban 的社交拍照定位，Google 的 Android XR 眼镜被定位为「Gemini Agent 的物理载体」——通过摄像头理解环境、通过语音交互执行任务。Towards AI 分析指出，10 AM PT 的主 keynote 将承载 AI 平台论述和 Gemini 模型更新，1:30 PM 的 Developer Keynote 则面向开发者生态。<br><small>来源：<a href=\"https://sea.mashable.com/tech/45872/what-to-expect-from-google-io-2026-gemini-news-android-xr-glasses\">Mashable</a> / <a href=\"https://pub.towardsai.net/google-i-o-2026-everything-google-is-about-to-announce-on-may-19-df54edefe634\">Towards AI</a></small></li><li><strong>「Gemini Intelligence」概念浮出水面：Android 不再只是操作系统，而是智能体系统</strong> — 多个预测文章（YouTube 分析、Yahoo Tech）指出 Google 将在 I/O 上正式宣布「Gemini Intelligence」——将 Gemini 从一个 app 变成 Android 的系统层能力。这意味着 Gemini 不再是一个你「打开使用」的聊天机器人，而是贯穿通知、日历、邮件、相机等所有系统功能的 AI 层。配合 Android 17 的发布，Google 试图将 Android 重新定义为「AI-first OS」。<br><small>来源：<a href=\"https://tech.yahoo.com/ai/gemini/articles/google-o-kicks-off-next-120000851.html\">Yahoo Tech</a> / <a href=\"https://www.youtube.com/watch?v=2XDe1Yk3P2M\">The AI Nexus</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>语音优先成为 AI 交互的新默认</strong>：Gemini Flash Live、OpenAI AVM、Claude Voice——三巨头同时押注语音</li><li><strong>AI 从 App 变成 OS 层</strong>：Gemini Intelligence = AI 不是功能，是系统本身</li><li><strong>XR 眼镜 = AI Agent 的物理入口</strong>：Google、Meta、Apple 三家都在做，但叙事各不相同</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Google I/O 前夜释放 Gemini 3.1 Flash Live 是一个精心计算的时间操作——在明天 keynote 千万人关注之前，先让开发者和媒体体验到「声音」。这不是泄漏，这是预热。Google 在告诉你：明天的主题不是模型参数，而是交互范式。</strong></p><p>把 Flash Live、Android XR 眼镜和 Gemini Intelligence 三件事放在一起看，Google 的 I/O 2026 战略极其清晰：<strong>他们在构建一个从硬件到系统到模型完全贯通的「AI 体验栈」</strong>。底层是 Gemini 模型家族（Flash/Pro/Ultra），中层是 Gemini Intelligence 系统层（嵌入 Android 17 的每一个触点），上层是 Android XR 眼镜（把 AI Agent 带到物理世界）。这和 Apple 的 Vision Pro + Apple Intelligence 策略形成了直接对标，但 Google 的优势在于 Android 的十亿级设备基数。</p><p>但我要指出一个 Google 的结构性风险：<strong>Gemini 模型本身的竞争力。</strong>上期日报我们提到 TechTimes 爆料新 Gemini「落后于 Mythos 和 GPT-5.5」。如果模型层不是最强的，那「AI-first OS」的故事就变成了「用一个二流模型驱动一流平台」。这不是不能成功——Android 当年也不是最好的 OS，但赢在了生态和覆盖量。问题是 AI 时代用户对「智能」的感知比对 OS 的感知更直接：如果 Gemini Intelligence 在日常使用中明显不如 iPhone 上的 Claude/ChatGPT，用户会用脚投票。</p><p>语音优先（Voice-first）这个趋势也值得单独说。Flash Live 瞄准的是「实时语音理解」——不是你说完一整句话等 2 秒得到回复，而是 AI 在你说话的过程中就在理解和准备回应。这是 Google 在延迟上的传统优势领域（搜索、自动补全都是延迟敏感产品）。如果他们能把语音交互做到「比打字快、比打开 App 快」，那 Gemini Intelligence 的 OS 层集成就有了杀手级用例：<strong>你不需要打开任何 App，只需要说话。</strong>这对 Android XR 眼镜来说更是刚需——你没法在眼镜上打字。</p><p>明天 10 AM PT（北京时间 5 月 20 日凌晨 1 点）的 keynote 将是 2026 年最重要的科技产品演讲之一。我会持续追踪。关键观察点：Gemini 新模型是否有 benchmark 突破？Android XR 是开发者预览还是消费者产品？Gemini Intelligence 的系统权限有多深？这三个问题的答案将决定 Google 在 AI 时代的位置。</p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Gemini 3.1 Flash Live Drops Early: Voice-First AI Model for Real-Time Speech Understanding</strong> — Android Central's live coverage confirms Google released Gemini 3.1 Flash Live ahead of I/O — a voice-first model focused on listening to speech, understanding it, and delivering faster voice responses. A direct answer to OpenAI's Advanced Voice Mode, signaling tomorrow's keynote narrative: conversational AI as the default interaction paradigm.<br><small>Source: <a href=\"https://www.androidcentral.com/phones/live/google-i-o-2026-live-blog-android-17-android-xr-glasses-and-all-the-gemini-ai-news\">Android Central</a></small></li><li><strong>Android XR Glasses Confirmed for Google I/O 2026: Google's 'Spatial Computing + AI Agent' Bet</strong> — Mashable and Yahoo Tech confirm Android XR smart glasses as tomorrow's hardware highlight. Unlike Meta Ray-Ban's social/photo positioning, Google's XR glasses are positioned as \"physical vessels for Gemini Agents\" — understanding environments via camera, executing tasks via voice.<br><small>Source: <a href=\"https://sea.mashable.com/tech/45872/what-to-expect-from-google-io-2026-gemini-news-android-xr-glasses\">Mashable</a> / <a href=\"https://pub.towardsai.net/google-i-o-2026-everything-google-is-about-to-announce-on-may-19-df54edefe634\">Towards AI</a></small></li><li><strong>'Gemini Intelligence' Emerges: Android Becomes an Agent System, Not Just an OS</strong> — Multiple sources indicate Google will announce Gemini Intelligence at I/O — transforming Gemini from an app to an Android system-layer capability. Gemini won't be a chatbot you open but an AI layer running through notifications, calendar, email, camera. Combined with Android 17, Google aims to redefine Android as an \"AI-first OS.\"<br><small>Source: <a href=\"https://tech.yahoo.com/ai/gemini/articles/google-o-kicks-off-next-120000851.html\">Yahoo Tech</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>Voice-first becomes the new AI default</strong>: Flash Live, OpenAI AVM, Claude Voice — all three bet on voice</li><li><strong>AI moves from App to OS layer</strong>: Gemini Intelligence = AI isn't a feature, it's the system itself</li><li><strong>XR glasses = physical entry point for AI Agents</strong>: Google, Meta, Apple all building, different narratives</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Releasing Gemini 3.1 Flash Live the night before I/O is a calculated timing move — let developers and media experience the \"voice\" before tomorrow's million-viewer keynote. This isn't a leak; it's a warm-up. Google is telling you: tomorrow's theme isn't model parameters, it's interaction paradigm.</strong></p><p>Flash Live + Android XR + Gemini Intelligence together reveal Google's I/O 2026 strategy clearly: <strong>they're building a fully integrated \"AI experience stack\" from hardware to system to model.</strong> Base layer: Gemini model family (Flash/Pro/Ultra). Middle: Gemini Intelligence system layer (embedded in every Android 17 touchpoint). Top: Android XR glasses (bringing AI Agents to the physical world). This directly mirrors Apple's Vision Pro + Apple Intelligence, but Google's advantage is Android's billion-device base.</p><p>The structural risk: <strong>Gemini's model competitiveness.</strong> If the model layer isn't frontier-class, \"AI-first OS\" becomes \"a second-tier model powering a first-tier platform.\" Not impossible to succeed — Android wasn't the best OS either but won on ecosystem. But in the AI era, users perceive \"intelligence\" more directly than they perceive OS quality: if Gemini Intelligence noticeably underperforms Claude/ChatGPT on iPhone, users will vote with their feet.</p><p>Voice-first deserves separate attention. Flash Live targets real-time speech understanding — AI understands while you're still speaking. This is Google's latency advantage territory (Search, autocomplete are all latency-sensitive). If they achieve \"faster than typing, faster than opening an app,\" Gemini Intelligence gets its killer use case: <strong>you don't open any app, you just speak.</strong> For XR glasses this is essential — you can't type on glasses.</p><p>Tomorrow 10 AM PT (1 AM Beijing time May 20) will be one of 2026's most important tech keynotes. Key questions: Does the new Gemini model have benchmark breakthroughs? Is Android XR developer preview or consumer product? How deep are Gemini Intelligence's system permissions? The answers determine Google's position in the AI era.</p></div>"
    },
    "cover": tech_cover,
    "sources": sources_tech
}

# Insert at front
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

# Write with python json.dump
with open(ISSUES_PATH, "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"✅ Written {len(issues)} issues to issues.json")
print(f"  Design cover: {design_cover}")
print(f"  Tech cover: {tech_cover}")
