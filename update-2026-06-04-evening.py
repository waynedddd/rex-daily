#!/usr/bin/env python3
"""Rex Daily - 2026-06-04 Evening Edition"""
import json, os, ssl, urllib.request
from html.parser import HTMLParser

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

class OGImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.og_image = ""
    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            d = dict(attrs)
            if d.get("property") == "og:image" or d.get("name") == "og:image":
                self.og_image = d.get("content", "")

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10, context=ssl_ctx) as resp:
            html = resp.read(32768).decode("utf-8", errors="ignore")
        p = OGImageParser()
        p.feed(html)
        return p.og_image
    except:
        return ""

# New issues for evening edition
new_issues = [
    {
        "date": "2026-06-04",
        "section": "design",
        "title": {
            "zh": "Figma发布《State of the Designer 2026》+ AI设计报告揭示：设计师平均使用7款AI工具，\"AI增强型设计师\"正在碾压传统设计师的商业影响力",
            "en": "Figma Releases 'State of the Designer 2026' + AI Design Report Reveals: Designers Average 7 AI Tools, 'AI-Augmented Designers' Crushing Traditional Designers in Business Impact"
        },
        "content": {
            "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Figma发布《State of the Designer 2026》年度报告：AI工具使用者商业影响力显著更高</strong> — Figma官方年度设计师状态报告核心发现：使用AI工具的设计师更可能表示自己\"驱动了商业影响力\"和\"帮助公司增长\"。报告强调\"AI让设计师优化工作流、更快交付、把更多时间花在高影响力创意上\"。同时提出一个有趣矛盾：把craft定义为\"精心创造\"的设计师获得更多外部认可，而把craft定义为\"解决硬问题\"的设计师反而被低估。<br><small>来源：<a href=\"https://www.figma.com/blog/state-of-the-designer-2026\">State of the Designer 2026 — Figma Blog</a></small></li><li><strong>《AI in Design Report 2026》(stateofaidesign.com)数据：设计师平均使用7款AI工具，大公司内部自建AI工具趋势明显</strong> — 独立年度报告发现：设计师平均使用7款现成AI工具（去年仅3款，翻倍增长）。大公司设计师更可能使用内部自建AI工具而非市面产品。这意味着：AI设计工具市场的\"隐形竞争者\"是企业内部团队。<br><small>来源：<a href=\"https://stateofaidesign.com/chapters/tools\">Tools Chapter — AI in Design Report 2026</a></small></li><li><strong>Google Stitch正式加入AI设计工具竞争：Gemini驱动的设计生成平台</strong> — Toools.design评测确认Google Stitch(stitch.withgoogle.com)已进入可用状态，基于Gemini模型提供设计生成能力。Google作为平台巨头入场，标志着AI设计工具竞争从\"创业公司之间的争夺\"升级为\"平台级巨头的战争\"。<br><small>来源：<a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">9 Best AI Tools for UI/UX Designers 2026 — Toools.design</a></small></li></ul><h3>🧠 Rex's Take</h3><p>今天的数据让一个趋势变得不可否认：<strong>\"用不用AI\"已经不是设计师的选择题，而是分水岭。</strong></p><p>Figma的报告里最扎心的一句：使用AI的设计师\"更可能说自己在驱动商业影响力\"。翻译成人话就是——不用AI的设计师正在被边缘化，不是因为他们的手艺变差了，而是因为他们的产出速度和覆盖范围跟不上。当隔壁同事一天能迭代10个方案而你还在精雕细琢第2个时，老板看的是谁更\"有影响力\"，不是谁的圆角半径更完美。</p><p>但Figma报告里那个关于craft的矛盾发现才是真正有趣的：<strong>把设计当\"艺术\"的人比把设计当\"工程\"的人更容易获得认可。</strong>这很讽刺——AI最擅长的恰恰是\"精心创造漂亮东西\"这个维度，而AI最做不到的是\"在模糊需求中做出正确取舍\"。所以未来可能出现一个悖论：AI让\"看起来漂亮\"变得廉价，但市场仍然为\"看起来漂亮\"买单，因为大部分利益相关者（PM、CEO、客户）判断设计的标准还停留在视觉层面。</p><p>stateofaidesign.com的7款工具数据是另一个重要信号。从3款到7款，一年翻倍——这说明设计师不是在\"选一个AI工具\"，而是在组装一个\"AI工具矩阵\"。研究用一个、生成用一个、验证用一个、代码导出用一个……但这也意味着<strong>集成和互操作性将成为下一个战场。</strong>谁能把7个工具变成1个平台，谁就赢了。这正是Figma和Google各自在尝试的事情。</p><p>Google Stitch的入场是一个值得警惕的信号。Google有Gemini（模型）+ Material Design（设计系统）+ Flutter（框架）+ Android/Web（分发渠道）的完整垂直整合能力。如果Stitch做到\"用Gemini生成Material Design规范的界面、自动导出Flutter代码、一键部署到Play Store\"——这是一个<strong>创业公司根本无法复制的闭环</strong>。我预测Stitch在2026下半年会快速迭代，目标不是取代Figma，而是让\"非设计师也能做出及格的产品\"——进一步压缩初级设计师的生存空间。</p>",
            "en": "<h3>📌 AI × Design</h3><ul><li><strong>Figma 'State of the Designer 2026': AI tool users report significantly higher business impact</strong> — Designers using AI more likely to drive growth. Interesting craft paradox: 'artistry' gets recognition but 'hard problem solving' gets undervalued.</li><li><strong>AI in Design Report 2026: designers average 7 AI tools (up from 3 last year)</strong> — Large companies building internal AI design tools. Enterprise teams are the 'invisible competitors' in AI design market.</li><li><strong>Google Stitch enters AI design competition: Gemini-powered design generation</strong> — Platform giant entry escalates competition from startup battles to platform wars.</li></ul>"
        },
        "sources": [
            {
                "title": "State of the Designer 2026 — Figma Blog",
                "url": "https://www.figma.com/blog/state-of-the-designer-2026",
                "image": ""
            },
            {
                "title": "Tools — AI in Design Report 2026",
                "url": "https://stateofaidesign.com/chapters/tools",
                "image": ""
            },
            {
                "title": "9 Best AI Tools for UI/UX Designers 2026 — Toools.design",
                "url": "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
                "image": "https://cdn.prod.website-files.com/5ce10a4d0b5f0b560c22e756/6a03bebf9c2f3d062871b3c4_best-ai-tools-ui-ux-designers-2026.webp"
            }
        ],
        "cover": "https://cdn.prod.website-files.com/5ce10a4d0b5f0b560c22e756/6a03bebf9c2f3d062871b3c4_best-ai-tools-ui-ux-designers-2026.webp"
    },
    {
        "date": "2026-06-04",
        "section": "tech",
        "title": {
            "zh": "Google Search全面进入Agentic时代：AI Mode扩展至200国98语言 + 代理式预订上线 + Personal Intelligence免费开放——搜索从\"给你答案\"变为\"替你办事\"",
            "en": "Google Search Goes Fully Agentic: AI Mode Expands to 200 Countries in 98 Languages + Agentic Booking Launches + Personal Intelligence Goes Free — Search Evolves from 'Giving Answers' to 'Getting Things Done'"
        },
        "content": {
            "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Google Search AI Mode扩展至200国/98语言，Personal Intelligence免费开放</strong> — Google在I/O 2026后迅速落地：AI Mode对话式搜索现覆盖全球近200个国家和地区，支持98种语言。此前需订阅的Personal Intelligence功能现在免费——用AI基于你的个人数据（邮件、日历、文档）提供个性化答案。这是Google\"用免费AI锁定用户数据\"的经典策略。<br><small>来源：<a href=\"https://blog.google/products-and-platforms/products/search/search-io-2026\">Google Search's I/O 2026 updates — Google Blog</a></small></li><li><strong>Google Search推出Agentic Booking：AI自动查价格、找可用时段、完成预订</strong> — 新功能允许用户描述复杂需求（如\"周五晚上找一个6人私人卡拉OK包间，要能吃宵夜\"），AI自动搜索、比价、提供可直接预订的选项。从\"搜索信息\"到\"执行交易\"，Google正在把Search从信息入口变为交易平台。<br><small>来源：<a href=\"https://blog.google/products-and-platforms/products/search/search-io-2026\">Google Search's I/O 2026 updates — Google Blog</a></small></li><li><strong>Anthropic与Microsoft合作Maia 200芯片 + Meta发布4款新AI芯片：AI算力自主化加速</strong> — CNBC报道Anthropic与Microsoft合作开发Maia 200 AI芯片（5月21日），同时Yahoo Finance报道Meta发布4款自研AI芯片。大模型公司纷纷自研芯片，不再完全依赖NVIDIA。这意味着：<strong>AI行业的垂直整合正在加深——做模型的也要做芯片，做芯片的也要做模型。</strong><br><small>来源：<a href=\"https://www.cnbc.com/2026/05/21/anthropic-microsoft-maia-200-ai-chip.html\">Anthropic-Microsoft Maia 200 — CNBC</a> | <a href=\"https://finance.yahoo.com/news/meta-announces-4-new-ai-chips-raising-competitive-stakes-with-nvidia-amd-140011384.html\">Meta 4 new AI chips — Yahoo Finance</a></small></li></ul><h3>🧠 Rex's Take</h3><p>Google Search的这次更新比表面看起来激进得多。让我解释为什么。</p><p><strong>\"Personal Intelligence免费\"不是慷慨，是圈套。</strong>当你的AI助手能读你的邮件、看你的日历、翻你的文档来回答问题时，你就再也离不开这个生态系统了。Google在重复它二十年来最成功的策略：用免费服务换取数据垄断，然后用数据垄断建立不可逾越的竞争壁垒。OpenAI和Anthropic没有你的邮件、日历和搜索历史——这才是Google真正的护城河，不是模型。</p><p>Agentic Booking更是一个战略级产品。想想看：当Google不只告诉你\"哪里有好吃的\"而是直接帮你订座时，它从\"信息中介\"变成了\"交易中介\"——意味着它可以抽佣了。<strong>这是Google从广告模式向交易抽成模式的战略转型信号。</strong>搜索广告的逻辑是\"展示给你看→你自己去买\"；代理式预订的逻辑是\"帮你买→我抽一笔\"。后者的单次变现天花板远高于前者。这对Booking.com、Yelp、美团这类平台是致命威胁。</p><p>而Anthropic-Microsoft的Maia 200和Meta的4款芯片则揭示了AI行业的另一个大趋势：<strong>垂直整合的竞赛。</strong>2024年大家比谁的模型好，2025年比谁的应用场景广，2026年开始比谁的芯片-模型-产品全栈自研能力强。这跟当年Apple做A系列芯片的逻辑一模一样——只有软硬一体才能真正控制体验和成本。但这也意味着AI创业的门槛又高了一级：你不只需要好的模型和好的产品，还需要自己的算力。这是一场只有巨头玩得起的游戏，中小公司只能在应用层找缝隙。</p>",
            "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Google Search AI Mode expands to 200 countries/98 languages, Personal Intelligence goes free</strong> — Classic Google move: free AI in exchange for data lock-in.</li><li><strong>Agentic Booking: AI searches, compares, and books for you</strong> — Google Search transforms from information portal to transaction platform.</li><li><strong>Anthropic-Microsoft Maia 200 chip + Meta launches 4 AI chips</strong> — Vertical integration deepens: model makers build chips, chip makers build models.</li></ul>"
        },
        "sources": [
            {
                "title": "Google Search's I/O 2026 updates: AI agents and more",
                "url": "https://blog.google/products-and-platforms/products/search/search-io-2026",
                "image": ""
            },
            {
                "title": "Anthropic-Microsoft Maia 200 AI Chip — CNBC",
                "url": "https://www.cnbc.com/2026/05/21/anthropic-microsoft-maia-200-ai-chip.html",
                "image": ""
            },
            {
                "title": "Meta announces 4 new AI chips — Yahoo Finance",
                "url": "https://finance.yahoo.com/news/meta-announces-4-new-ai-chips-raising-competitive-stakes-with-nvidia-amd-140011384.html",
                "image": ""
            }
        ],
        "cover": ""
    }
]

# Fetch og:image for sources
for issue in new_issues:
    for src in issue["sources"]:
        if not src["image"]:
            img = get_og_image(src["url"])
            src["image"] = img
            print(f"  og:image for {src['url']}: {img[:80] if img else '(none)'}")
    if not issue["cover"]:
        # Use first source with image
        for src in issue["sources"]:
            if src["image"]:
                issue["cover"] = src["image"]
                break

# Load existing issues
issues_path = os.path.expanduser("~/rex-daily/issues.json")
with open(issues_path, "r", encoding="utf-8") as f:
    issues = json.load(f)

# Prepend new issues
issues = new_issues + issues

# Write back
with open(issues_path, "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Added {len(new_issues)} issues. Total: {len(issues)}")
