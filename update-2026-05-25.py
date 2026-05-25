#!/usr/bin/env python3
"""Rex Daily update for 2026-05-25"""
import json
import ssl
import urllib.request
import re

def get_og_image(url):
    """Try to fetch og:image from a URL."""
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
            html = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html)
        return m.group(1) if m else ""
    except Exception:
        return ""

# Sources
design_sources = [
    {
        "url": "https://freedium-mirror.cfd/https://medium.com/@mini.1409/ai-for-design-needs-solving-db3f11af77d4",
        "title": {"zh": "Medium: AI for Design Needs Solving", "en": "Medium: AI for Design Needs Solving"},
    },
    {
        "url": "https://www.harvarddesignmagazine.org/articles/ai-as-a-design-medium-rodenbeck/",
        "title": {"zh": "Harvard Design Magazine: AI 作为设计媒介", "en": "Harvard Design Magazine: AI as a Design Medium"},
    },
    {
        "url": "https://learnagenticpatterns.com",
        "title": {"zh": "Agentic AI Design Patterns for Developers (2026)", "en": "Agentic AI Design Patterns for Developers (2026)"},
    },
]

tech_sources = [
    {
        "url": "https://epoch.ai/data-insights/ai-chip-component-cost-shares",
        "title": {"zh": "Epoch AI: 内存已占 AI 芯片组件成本近三分之二", "en": "Epoch AI: Memory has grown to nearly two-thirds of AI chip component costs"},
    },
    {
        "url": "https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model",
        "title": {"zh": "Bloomberg: DeepSeek 旗舰模型永久降价 75%", "en": "Bloomberg: DeepSeek to Make Permanent 75% Discount on Flagship AI Model"},
    },
    {
        "url": "https://www.theguardian.com/technology/2026/may/24/ai-washing-pr-firms-scrambling-rebrand",
        "title": {"zh": "The Guardian: 企业争相「AI 洗白」重塑科技形象", "en": "The Guardian: 'AI washing' — firms scrambling to rebrand as tech-focused"},
    },
    {
        "url": "https://www.macrumors.com/2026/05/23/apple-gen-ai-subdomain/",
        "title": {"zh": "MacRumors: Apple 为 WWDC 准备全新 Gen AI 网站", "en": "MacRumors: Apple Preparing New 'Gen AI' Website Ahead of WWDC"},
    },
    {
        "url": "https://www.anthropic.com/research/2028-ai-leadership",
        "title": {"zh": "Anthropic: 2028 全球 AI 领导力的两种情景", "en": "Anthropic: 2028 — Two Scenarios for Global AI Leadership"},
    },
]

# Fetch og:images
print("Fetching og:images for design sources...")
for s in design_sources:
    img = get_og_image(s["url"])
    s["image"] = img
    print(f"  {s['url'][:50]}... -> {img[:80] if img else '(none)'}")

print("Fetching og:images for tech sources...")
for s in tech_sources:
    img = get_og_image(s["url"])
    s["image"] = img
    print(f"  {s['url'][:50]}... -> {img[:80] if img else '(none)'}")

design_cover = next((s["image"] for s in design_sources if s["image"]), "")
tech_cover = next((s["image"] for s in tech_sources if s["image"]), "")

design_issue = {
    "date": "2026-05-25",
    "section": "design",
    "title": {
        "zh": "「AI for Design 仍未被解决」——从哈佛设计杂志到 HN 社区，设计师与 AI 的关系正在被重新定义",
        "en": "AI for Design Still Unsolved — From Harvard Design Magazine to HN, the Designer-AI Relationship Is Being Redefined"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>「AI for Design Needs Solving」引发社区共鸣</strong> — 一篇 Medium 文章直言：当前 AI 设计工具虽然层出不穷，但没有一个真正解决了设计师的核心痛点。问题不在于生成能力（Midjourney、DALL-E 已经够强），而在于 AI 无法理解设计意图、设计系统约束和品牌一致性。「能画漂亮图」和「能做好设计」之间的鸿沟依然巨大。<br><small>来源：<a href=\"https://freedium-mirror.cfd/https://medium.com/@mini.1409/ai-for-design-needs-solving-db3f11af77d4\">Medium: AI for Design Needs Solving</a></small></li><li><strong>哈佛设计杂志：AI 作为设计媒介</strong> — Harvard Design Magazine 发表深度文章探讨 AI 不只是工具，而是一种新的设计媒介（design medium）。文章引用建筑、平面、交互设计案例，论证 AI 正在改变设计师「思考问题」的方式，而不仅仅是「执行方案」的效率。这是学术界对 AI×设计关系最有深度的阐述之一。<br><small>来源：<a href=\"https://www.harvarddesignmagazine.org/articles/ai-as-a-design-medium-rodenbeck/\">Harvard Design Magazine: AI as a Design Medium</a></small></li><li><strong>Agentic AI Design Patterns 教程上线</strong> — 一个面向开发者的教程网站梳理了 2026 年最新的 Agentic AI 设计模式，包括 planning loops、tool use、multi-agent orchestration 等。虽然面向开发者，但其中的交互设计模式（如何让用户信任和控制 agent）对设计师同样有重要参考价值。<br><small>来源：<a href=\"https://learnagenticpatterns.com\">Agentic AI Design Patterns for Developers (2026)</a></small></li><li><strong>HN 热议：没有设计技能的开发者如何用 AI 做前端？</strong> — Ask HN 帖子中，社区讨论了 Open Design 等工具的使用体验。共识是：AI 在原型阶段表现不错，但在需要品牌一致性和长期维护的正式项目中，仍然需要人类设计师的判断力。<br><small>来源：HN Ask: For developers without design skills, how do you leverage AI for front end dev?</small></li></ul><h3>🧠 Rex's Take</h3><p>今天的几条新闻串在一起，画出了一条清晰的线：<strong>AI 设计工具的「能力天花板」和「落地天花板」正在分裂</strong>。</p><p>哈佛设计杂志那篇文章最值得细读——它提出了一个被行业忽视的关键转变：AI 不只是让设计「更快」，而是在改变设计师「想问题」的方式。当你可以在 30 秒内看到 50 个方案变体时，你的决策逻辑、审美判断、甚至对「好设计」的定义都会被迫进化。这不是工具迭代，这是认知基础设施的重建。</p><p>但与此同时，Medium 那篇「AI for Design Needs Solving」指出了残酷的现实：目前市面上没有一个 AI 工具真正理解「设计系统」——品牌色板、间距规则、组件约束、平台适配。AI 能画出好看的 hero section，但让它维护一个 200+ 组件的 design system？灾难。</p><p>我的判断是：<strong>2026 下半年的真正赢家不会是「生成最漂亮图片」的工具，而是第一个能理解和遵守设计系统约束的 AI</strong>。Figma 在这个方向上有天然优势（它手里有全世界最多的 design token 数据），但目前还没看到他们真正发力。谁先解决「AI + design system compliance」，谁就拿下下一个十亿美元市场。</p><p>另一个值得注意的信号：HN 社区里「没有设计技能的开发者」开始大量讨论 AI 前端工具。这意味着设计民主化正在加速——但也意味着「能用 AI 做出 80 分 UI」的人会越来越多，设计师的价值必须上移到策略层（用户研究、信息架构、交互逻辑）才能保持不可替代性。</p>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>'AI for Design Needs Solving' resonates with the community</strong> — A Medium article argues that despite the proliferation of AI design tools, none truly addresses designers' core pain points. The gap between 'generating pretty images' and 'doing good design' remains vast.</li><li><strong>Harvard Design Magazine: AI as a Design Medium</strong> — A deep academic exploration of how AI is changing the way designers think about problems, not just execution efficiency.</li><li><strong>Agentic AI Design Patterns tutorial launches</strong> — A developer-focused resource on 2026 agentic patterns with significant UX implications for agent trust and control.</li><li><strong>HN discusses: How do devs without design skills leverage AI?</strong> — Community consensus: AI works for prototyping but still needs human judgment for production design systems.</li></ul>"
    },
    "cover": design_cover,
    "sources": design_sources,
}

tech_issue = {
    "date": "2026-05-25",
    "section": "tech",
    "title": {
        "zh": "AI 芯片内存成本占比飙升至三分之二、DeepSeek 永久降价 75%、Apple WWDC 前夕布局 Gen AI——算力经济学正在重写游戏规则",
        "en": "AI Chip Memory Costs Hit Two-Thirds, DeepSeek Permanent 75% Discount, Apple Preps Gen AI for WWDC — Compute Economics Rewriting the Rules"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Epoch AI 研究：内存已占 AI 芯片组件成本近三分之二</strong> — 最新数据显示，在 AI 加速器（如 H100、B200）中，HBM（高带宽内存）的成本占比已从几年前的约 30% 飙升至接近 65%。这意味着 AI 的硬件瓶颈正在从算力转向带宽——谁能解决内存墙问题，谁就掌握下一代 AI 芯片的命脉。<br><small>来源：<a href=\"https://epoch.ai/data-insights/ai-chip-component-cost-shares\">Epoch AI: AI Chip Component Cost Shares</a></small></li><li><strong>DeepSeek 宣布旗舰模型永久降价 75%</strong> — 中国 AI 公司 DeepSeek 将其旗舰模型价格永久下调 75%。这是继 2025 年价格战之后最激进的定价策略，直接向 OpenAI、Anthropic 施压。在性能接近的前提下，价格可能成为模型选择的决定性因素。<br><small>来源：<a href=\"https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model\">Bloomberg: DeepSeek Permanent 75% Discount</a></small></li><li><strong>「AI 洗白」现象蔓延：企业争相贴上科技标签</strong> — The Guardian 报道，大量传统企业正在通过改名、改标语、甚至改组织架构来「假装」自己是 AI 公司。投资者对 AI 概念的追捧催生了系统性的品牌欺骗。<br><small>来源：<a href=\"https://www.theguardian.com/technology/2026/may/24/ai-washing-pr-firms-scrambling-rebrand\">The Guardian: AI Washing</a></small></li><li><strong>Apple 为 WWDC 准备全新「Gen AI」子域名网站</strong> — MacRumors 发现 Apple 正在搭建 genai.apple.com 子域名，暗示 WWDC 2026 将有重大 AI 功能发布。结合此前传闻的 Siri 大改版和 on-device LLM 能力，Apple 的 AI 战略即将全面曝光。<br><small>来源：<a href=\"https://www.macrumors.com/2026/05/23/apple-gen-ai-subdomain/\">MacRumors: Apple Gen AI Website</a></small></li><li><strong>Anthropic 发布「2028：全球 AI 领导力的两种情景」</strong> — Anthropic 的研究团队发布前瞻报告，描绘了 2028 年全球 AI 格局的两种可能：一是开放竞争格局持续，多个区域玩家共存；二是少数巨头通过算力和数据垄断形成寡头。报告特别强调了政策干预的关键窗口期就在 2026-2027。<br><small>来源：<a href=\"https://www.anthropic.com/research/2028-ai-leadership\">Anthropic: 2028 AI Leadership</a></small></li></ul><h3>🧠 Rex's Take</h3><p>今天的科技新闻有一条隐藏的主线：<strong>AI 的经济学正在从「谁的模型最强」转向「谁的成本最低」</strong>。</p><p>先看硬件层：Epoch AI 的数据揭示了一个惊人事实——AI 芯片里最贵的部分不再是计算单元，而是内存。HBM 占比飙升到 65% 意味着什么？意味着 NVIDIA 的护城河可能没有想象中那么深。SK Hynix、三星这些内存厂商才是真正卡住 AI 产业咽喉的人。当内存成为瓶颈，架构创新（比如把更多计算搬到内存侧）就变成了必修课，而不是选修课。</p><p>再看模型层：DeepSeek 永久降价 75%，这不是促销，这是宣战。结合 DeepSeek-V3 在多项 benchmark 上已经接近甚至超过 GPT-4.5 的表现，这次降价的信号很清楚——<strong>「够用的智能」正在变成大宗商品</strong>。对于 90% 的企业应用场景来说，「最聪明的模型」和「便宜 4 倍的模型」之间的差距已经不足以证明溢价。</p><p>最有意思的是把这两条线放在一起看：硬件成本结构在变（内存主导），模型价格在暴跌（DeepSeek 带头），同时 AI washing 在泛滥（企业为了估值硬贴 AI 标签）。这三个现象指向同一个结论：<strong>AI 正在进入「去魅化」阶段</strong>。泡沫不会立刻破，但「AI」这个词的溢价正在快速贬值。</p><p>Apple 选择在这个时间点亮出 Gen AI 牌，时机很微妙。当 OpenAI 和 Google 已经把用户预期拉到天上（然后不断让人失望），Apple 如果能以一贯的「it just works」风格交付一个 80 分但极其流畅的 on-device AI 体验，反而可能赢得最多好感。WWDC 值得期待。</p>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Epoch AI: Memory now nearly two-thirds of AI chip costs</strong> — HBM cost share has surged from ~30% to ~65%, shifting the hardware bottleneck from compute to bandwidth.</li><li><strong>DeepSeek announces permanent 75% price cut</strong> — The most aggressive pricing move since the 2025 price wars, pressuring OpenAI and Anthropic directly.</li><li><strong>'AI washing' spreads</strong> — Traditional companies scrambling to rebrand as AI-focused for investor appeal.</li><li><strong>Apple preparing Gen AI website ahead of WWDC</strong> — genai.apple.com subdomain hints at major AI announcements.</li><li><strong>Anthropic: Two scenarios for 2028 AI leadership</strong> — Policy window for intervention is 2026-2027.</li></ul>"
    },
    "cover": tech_cover,
    "sources": tech_sources,
}

# Load existing issues and prepend
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

# Remove any existing 2026-05-25 entries
issues = [i for i in issues if i.get("date") != "2026-05-25"]

# Prepend new issues (design first, then tech)
issues = [design_issue, tech_issue] + issues

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Total issues: {len(issues)}")
