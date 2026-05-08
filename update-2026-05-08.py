# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily update for 2026-05-08"""
import json
import urllib.request
import re
from html.parser import HTMLParser

def get_og_image(url):
    """Fetch og:image from a URL."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read(50000).decode('utf-8', errors='ignore')
            match = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html)
            if not match:
                match = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html)
            return match.group(1) if match else ""
    except:
        return ""

# Fetch og:images for sources
design_sources = [
    ("https://www.guideflow.com/blog/ai-design-tools", "2026 年 15 款最佳 AI 设计工具深度对比：免费与付费方案全解析", "15 Best AI Design Tools in 2026: Free & Paid Options Compared"),
    ("https://medium.com/@DilSalaKamina/i-tested-50-ai-design-tools-so-you-dont-have-to-the-10-every-product-designer-actually-needs-in-5bce66cdb74a", "我测试了 50+ AI 设计工具：2026 年产品设计师真正需要的 10 款", "I Tested 50+ AI Design Tools: The 10 Every Product Designer Actually Needs in 2026"),
    ("https://www.figma.com/resource-library/ai-product-design/", "Figma 官方推荐：2026 年 5 款最佳 AI 产品设计工具", "5 Best AI Product Design Tools for 2026 by Figma"),
]

tech_sources = [
    ("https://www.latimes.com/business/story/2026-05-06/nvidia-faces-its-biggest-threat-yet-as-tech-giants-build-their-own-ai-chips", "Nvidia 面临最大威胁：科技巨头集体自研 AI 芯片", "Nvidia Faces Its Biggest Threat Yet as Tech Giants Build Their Own AI Chips"),
    ("https://www.latimes.com/business/story/2026-05-06/u-s-china-ai-gap-has-closed-and-silicon-valley-is-starting-to-notice", "中美 AI 差距已经消失——硅谷开始感受到了", "The U.S.-China AI Gap Has Closed — and Silicon Valley Is Starting to Notice"),
    ("https://aicentral.substack.com/p/the-ai-landscape-may-2026", "2026 年 5 月 AI 全景：GPT-5.5-Cyber、DeepSeek V4、Mythos 余波", "The AI Landscape: May 2026 — GPT-5.5-Cyber, DeepSeek V4, Mythos Aftermath"),
]

print("Fetching og:images...")
design_images = []
for url, _, _ in design_sources:
    img = get_og_image(url)
    design_images.append(img)
    print(f"  {url[:50]}... -> {img[:60] if img else '(none)'}")

tech_images = []
for url, _, _ in tech_sources:
    img = get_og_image(url)
    tech_images.append(img)
    print(f"  {url[:50]}... -> {img[:60] if img else '(none)'}")

design_cover = next((img for img in design_images if img), "")
tech_cover = next((img for img in tech_images if img), "")

# Build issues
design_issue = {
    "date": "2026-05-08",
    "section": "design",
    "title": {
        "zh": "AI 设计工具突破 50 款：当所有人都能「一句话出图」，设计师的护城河到底在哪？——从工具测评潮看 2026 设计行业的真正分水岭",
        "en": "50+ AI Design Tools and Counting: When Everyone Can 'Prompt-to-UI,' Where's the Designer's Moat? — What the 2026 Tool Review Wave Reveals About Design's Real Inflection Point"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Guideflow 发布 2026 年 15 款 AI 设计工具全面对比：免费工具已「够用」，付费工具需要讲新故事</strong> — Guideflow 的深度测评覆盖了从 Microsoft Designer（免费，DALL-E 驱动）到 Figma Make（$16/月）再到 Galileo AI 的全部主流选手。核心发现：<strong>免费工具（Microsoft Designer、Google Stitch）的质量已经达到「对非设计师够用」的水平</strong>，这意味着付费工具必须在工作流集成和代码导出上找到差异化。Canva Magic Design 被评为「对非设计师最友好的 AI 设计生成器」，拥有 25 万+模板。<br><small>来源：<a href=\"https://www.guideflow.com/blog/ai-design-tools\">Guideflow</a></small></li><li><strong>产品设计师实测 50+ AI 工具后的结论：真正有用的只有 10 款</strong> — Medium 上一篇引发设计师共鸣的长文：作者用 15 个月时间测试了 50 多款 AI 设计工具，从利益相关者会议到最终交付全链路。结论是大部分 AI 设计工具「来自没用过 Figma 的营销人员」，真正有价值的工具按设计流程阶段组织：Relume（站点地图+线框）、UX Pilot（研究到原型）、Figma Make（生成 UI）。<strong>「工具太多」本身已经成为设计师的新问题。</strong><br><small>来源：<a href=\"https://medium.com/@DilSalaKamina/i-tested-50-ai-design-tools-so-you-dont-have-to-the-10-every-product-designer-actually-needs-in-5bce66cdb74a\">Medium</a></small></li><li><strong>Figma 官方发布 AI 产品设计工具指南：强调「连接性工作流」而非单点生成</strong> — Figma 资源库更新了 2026 年 AI 产品设计工具指南，将自家定位为「AI-connected workflow 的最通用解决方案」。核心信息：text-to-design 只是起点，真正的价值在于从 AI 线框到可工作原型的完整连接。Figma 明确把竞争焦点从「生成能力」转向「生态系统整合」。<br><small>来源：<a href=\"https://www.figma.com/resource-library/ai-product-design/\">Figma</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「工具过剩」成为新问题</strong>：50+ AI 设计工具同时存在，设计师的时间成本从「画图」转移到「选工具」——讽刺的是，这正是 AI 本该解决的问题</li><li><strong>免费工具质量逼近付费</strong>：Microsoft Designer + Google Stitch 的免费组合已经能覆盖 80% 的日常设计需求，付费工具的定价权正在被侵蚀</li><li><strong>Figma 的防守姿态</strong>：从「我们是设计工具」到「我们是 AI 设计的操作系统」——Figma 在用生态锁定对抗单点工具的冲击</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>当一个产品设计师需要花 15 个月测试 50+ 工具才能告诉你「真正有用的只有 10 款」时，这个市场出了什么问题？</strong></p><p>答案很简单：<strong>AI 设计工具的供给侧已经完全失控了</strong>。2024 年的问题是「能不能用 AI 做设计」，2025 年的问题是「哪个 AI 设计工具最好」，2026 年的问题变成了「如何在 50 款看起来差不多的 AI 工具中活下来」。这不是用户的问题，这是行业的结构性泡沫。</p><p>让我来说一个反直觉的观点：<strong>AI 设计工具的泛滥，正在让「不用 AI」变成一种差异化策略</strong>。当每个初创公司都能用 Figma Make 或 Google Stitch 在 10 分钟内生成一个「看起来还行」的 UI 时，市场上充斥着大量「80 分设计」。这些设计不难看，但也没有灵魂——它们遵循所有最佳实践、用了正确的间距和配色、但无法让任何人停下来多看一眼。<strong>在一个 AI 能生产无限 80 分设计的世界里，「95 分设计」的溢价不是在降低——它在飙升。</strong></p><p>Guideflow 的测评里有一个数据值得注意：Microsoft Designer 完全免费、用 DALL-E 驱动。Google Stitch 也免费。当行业标杆级的大公司把 AI 设计工具作为免费功能捆绑时，那些独立的 AI 设计 SaaS 的商业模式就面临根本性质疑。<strong>你怎么和「免费」竞争？</strong>答案只有两个：要么你做的事情 Microsoft/Google 永远不会做（比如 UX Pilot 的研究到原型链路），要么你嵌入一个他们无法复制的生态（比如 Figma 的插件体系）。</p><p>那篇 Medium 文章的作者说「大部分 AI 设计工具来自没用过 Figma 的营销人员」——这话刻薄但精准。<strong>设计工具行业正在经历和 2023 年「AI wrapper」一样的清洗</strong>：一大批产品本质上只是在调用同一个基础模型的 API、套了一个略有不同的 UI、然后收 $15/月。用户最终会发现这些工具之间没有本质区别，然后回到 Figma 这样的平台级产品里——因为 Figma 的价值不在于某一个 AI 功能，而在于整个团队的工作流已经建立在它之上。</p><p><strong>我的预测：到 2026 年底，今天还活着的 50+ AI 设计工具中，至少一半会关停或被收购。存活的逻辑很清楚：要么你是平台（Figma、Canva），要么你解决了一个平台不愿做的垂直问题（UX 研究、设计系统自动化），要么你是免费的钩子（Microsoft、Google）。其他一切——那些「又一个 prompt-to-UI」的产品——都是在倒计时。设计师们，省点时间吧，不需要测 50 款工具。</strong></p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Guideflow Publishes Comprehensive 2026 AI Design Tool Comparison: Free Tools Are Now 'Good Enough'</strong> — Guideflow's deep review covers all major players from Microsoft Designer (free, DALL-E powered) to Figma Make ($16/mo) to Galileo AI. Key finding: <strong>free tools (Microsoft Designer, Google Stitch) have reached 'good enough for non-designers' quality</strong>, forcing paid tools to differentiate on workflow integration and code export. Canva Magic Design rated most accessible with 250K+ templates.<br><small>Source: <a href=\"https://www.guideflow.com/blog/ai-design-tools\">Guideflow</a></small></li><li><strong>Product Designer Tests 50+ AI Tools, Concludes Only 10 Are Actually Useful</strong> — A viral Medium post: the author spent 15 months testing 50+ AI design tools across the full design pipeline. Conclusion: most tools are built by 'marketers who haven't used Figma.' Truly valuable tools organized by workflow stage: Relume (sitemap+wireframe), UX Pilot (research-to-prototype), Figma Make (UI generation). <strong>'Too many tools' has become designers' new problem.</strong><br><small>Source: <a href=\"https://medium.com/@DilSalaKamina/i-tested-50-ai-design-tools-so-you-dont-have-to-the-10-every-product-designer-actually-needs-in-5bce66cdb74a\">Medium</a></small></li><li><strong>Figma Publishes Official AI Product Design Guide: Emphasizes 'Connected Workflows' Over Point Solutions</strong> — Figma's resource library updated its 2026 AI product design guide, positioning itself as 'the most versatile solution for AI-connected workflows.' Core message: text-to-design is just the starting point; real value lies in connecting AI wireframes to working prototypes.<br><small>Source: <a href=\"https://www.figma.com/resource-library/ai-product-design/\">Figma</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>'Tool Overload' Is the New Problem</strong>: 50+ AI design tools competing simultaneously — designers now spend more time choosing tools than using them</li><li><strong>Free Tools Approaching Paid Quality</strong>: Microsoft Designer + Google Stitch's free combo covers 80% of daily design needs, eroding paid tools' pricing power</li><li><strong>Figma's Defensive Posture</strong>: From 'we're a design tool' to 'we're the OS for AI design' — using ecosystem lock-in against point solutions</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>When a product designer needs 15 months testing 50+ tools to conclude 'only 10 are useful,' something is fundamentally broken in this market.</strong></p><p>The answer is simple: <strong>the supply side of AI design tools has completely lost control.</strong> 2024's question was 'can AI do design?' 2025's was 'which AI design tool is best?' 2026's has become 'how do you survive among 50 nearly identical AI tools?' This isn't a user problem — it's a structural bubble.</p><p>Here's a counterintuitive take: <strong>the flood of AI design tools is making 'not using AI' a differentiation strategy.</strong> When every startup can generate a 'decent-looking' UI with Figma Make or Google Stitch in 10 minutes, the market floods with '80-point designs.' These designs aren't ugly, but they're soulless — following all best practices with correct spacing and colors, yet unable to make anyone pause. <strong>In a world where AI produces infinite 80-point designs, the premium for '95-point design' isn't decreasing — it's skyrocketing.</strong></p><p>A key data point from Guideflow: Microsoft Designer is completely free with DALL-E. Google Stitch is free. When industry giants bundle AI design as a free feature, the business model of standalone AI design SaaS faces existential questions. <strong>How do you compete with 'free'?</strong> Only two answers: either you do something Microsoft/Google never will (like UX Pilot's research-to-prototype pipeline), or you embed in an ecosystem they can't replicate (like Figma's plugin architecture).</p><p><strong>Prediction: by end of 2026, at least half of today's 50+ AI design tools will shut down or get acqui-hired. Survival logic is clear: either you're a platform (Figma, Canva), solve a vertical problem platforms won't (UX research, design system automation), or you're a free hook (Microsoft, Google). Everything else — the 'yet another prompt-to-UI' products — are on a countdown timer.</strong></p></div>"
    },
    "cover": design_cover,
    "sources": []
}

for i, (url, zh, en) in enumerate(design_sources):
    design_issue["sources"].append({
        "url": url,
        "title": {"zh": zh, "en": en},
        "image": design_images[i]
    })

tech_issue = {
    "date": "2026-05-08",
    "section": "tech",
    "title": {
        "zh": "Nvidia 的「英特尔时刻」来了？科技巨头集体自研 AI 芯片 + 中美 AI 差距消失 + GPT-5.5-Cyber 限制发布——三条新闻拼出 AI 算力格局的剧变",
        "en": "Nvidia's 'Intel Moment' Arrives? Tech Giants Building Own AI Chips + US-China AI Gap Closes + GPT-5.5-Cyber Restricted Release — Three Stories Reveal AI Compute's Tectonic Shift"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Nvidia 面临史上最大威胁：Google、Amazon、Meta、Microsoft 集体自研 AI 芯片，投资者大规模抛售 Nvidia 股票</strong> — LA Times 报道（5月6日），本季财报虽然对 AI 利好频传，但投资者不再追捧 Nvidia，反而在大规模卖出。原因：Google TPU 持续迭代、Amazon Trainium、Meta MTIA（每 6 个月更新一代）、Microsoft 自研芯片全面发力。<strong>当你最大的客户都在做你的替代品时，「护城河」这个词需要重新定义。</strong><br><small>来源：<a href=\"https://www.latimes.com/business/story/2026-05-06/nvidia-faces-its-biggest-threat-yet-as-tech-giants-build-their-own-ai-chips\">LA Times</a> / <a href=\"https://finance.yahoo.com/news/nvidia-stock-faces-threat-google-123241502.html\">Yahoo Finance</a></small></li><li><strong>LA Times：中美 AI 差距已经消失，硅谷开始紧张</strong> — DeepSeek 震动全球一年多后，中国已经成为 AI 工具大规模落地的试验场。DeepSeek V4 在华为 Ascend 950 和寒武纪芯片上完成训练（4月24日发布），开源 V4-Pro 和 V4-Flash。<strong>芯片禁令没有阻止中国 AI 进步，反而催生了替代芯片生态。</strong>硅谷首次感到「落后焦虑」不是在模型层面，而是在应用落地速度上。<br><small>来源：<a href=\"https://www.latimes.com/business/story/2026-05-06/u-s-china-ai-gap-has-closed-and-silicon-valley-is-starting-to-notice\">LA Times</a></small></li><li><strong>OpenAI 发布 GPT-5.5-Cyber 但仅限「可信赖网络防御者」使用，英国 AI 安全研究所称其为「测试过最强网络安全模型」</strong> — GPT-5.5-Cyber 完成了英国 AISI 多步攻击模拟的端到端执行（仅第二个做到的系统）。讽刺的是，Altman 4月21日刚批评 Anthropic 的 Mythos 限制发布是「恐惧营销」，10 天后 OpenAI 对自己的模型采取了完全相同的策略。美国政府正在起草法律，确保类似 Mythos 和 GPT-5.5-Cyber 级别的模型不能自由发布。<br><small>来源：<a href=\"https://aicentral.substack.com/p/the-ai-landscape-may-2026\">AI Central</a> / <a href=\"https://timesofindia.indiatimes.com/technology/tech-news/us-government-planning-law-so-google-openai-and-no-other-company-can-freely-release-an-ai-model-like-anthropics-mythos-that-scared-many/articleshow/130819415.cms\">Times of India</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 算力垂直整合加速</strong>：从「买 Nvidia GPU」到「自己造芯片」——科技巨头正在复制 Apple Silicon 的路径</li><li><strong>芯片禁令的反噬效应</strong>：中国被迫用华为 Ascend 替代 Nvidia → DeepSeek V4 证明可行 → 整个替代芯片生态加速成熟</li><li><strong>「太危险不发布」成为行业标准</strong>：Anthropic Mythos → OpenAI GPT-5.5-Cyber → 美国政府立法 → AI 安全从自律走向强制监管</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天这三条新闻指向同一个结论：2026 年 AI 行业的权力结构正在经历根本性重组，而 Nvidia 可能是第一个「大到不能赢」的受害者。</strong></p><p>先说 Nvidia 的困境。投资者在 AI 利好频传时抛售 Nvidia 股票——这不是恐慌，这是预见。<strong>当 Google、Amazon、Meta、Microsoft 同时开发自研 AI 芯片时，Nvidia 面临的不是「竞争」，而是「客户叛逃」。</strong>这和 Intel 曾经面临的困境惊人相似：你的核心客户（PC 制造商）开始自己做芯片（Apple Silicon）。区别在于，Intel 花了 10 年才感受到冲击，Nvidia 可能只有 2-3 年。Meta 的 MTIA 每 6 个月迭代一次——这不是在做实验，这是在战略执行。Google TPU 已经能训练 DeepSeek 等级的模型。<strong>Nvidia 的「护城河」从来不是技术本身——是生态和 CUDA 锁定。但当你的四个最大客户都有足够的工程资源绕过这个锁定时，生态优势的保质期比你想象的短得多。</strong></p><p>中美 AI 差距消失这条新闻和 Nvidia 的故事本质上是同一个叙事的两面。<strong>美国的芯片禁令不仅没有阻止中国 AI 发展，反而催生了一个完整的替代计算生态。</strong>DeepSeek V4 在华为 Ascend 950 和寒武纪芯片上完成训练——一年前这被认为不可能。华为在 V4 发布当天公开确认了 Ascend 950 集群的支持，这不是低调验证，这是「战略宣言」。更重要的是，LA Times 指出中国的优势不在模型能力（差距确实在缩小），而在<strong>应用落地速度</strong>——当一个 14 亿人的市场把 AI 当水电煤来用时，它产生的应用创新和数据飞轮是硅谷在一个 3.3 亿人的市场里无法复制的。</p><p>GPT-5.5-Cyber 的故事是今天最具黑色幽默感的一条。<strong>Sam Altman 4月21日公开嘲讽 Anthropic 的 Mythos 限制发布是「恐惧营销」，说这种做法是「把 AI 控制在少数人手里」。10 天后，OpenAI 对 GPT-5.5-Cyber 采取了完全相同的策略——仅向「可信赖网络防御者」开放。</strong>这不是虚伪（好吧，也许有一点），这是模型能力增长速度超出了所有人——包括制造者——的预期。当英国 AISI 说 GPT-5.5-Cyber 是它测试过的最强网络攻击系统、且能完成端到端多步攻击模拟时，你就理解为什么限制发布不再是「可选项」而是「必须」。美国政府正在起草相关法律——AI 监管从「要不要管」正式进入「怎么管」阶段。</p><p><strong>把这三条新闻放在一起，我看到的 pattern 是：AI 行业正在从「增长期」进入「重组期」。Nvidia 的垄断地位开始松动，中国的替代路径被证明可行，最强模型开始被限制发布。这意味着 2026 下半年的赢家不再是「做最强模型的人」或「卖最多 GPU 的人」，而是能最快把 AI 能力转化为用户价值的人。算力民主化（自研芯片）+ 模型民主化（开源 DeepSeek V4）+ 应用爆发（中国市场）= AI 行业的价值锚点正在从「上游」向「下游」迁移。对设计师来说，这是个好消息：当 AI 能力不再稀缺时，「如何用 AI」比「有没有 AI」重要一万倍。</strong></p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Nvidia Faces Biggest Threat Ever: Google, Amazon, Meta, Microsoft All Building Custom AI Chips; Investors Dumping Nvidia Stock</strong> — LA Times reports (May 6) that despite strong AI earnings season, investors are selling Nvidia en masse. Reason: Google TPU iterations, Amazon Trainium, Meta MTIA (updating every 6 months), Microsoft custom chips all accelerating. <strong>When your biggest customers are all building your replacement, 'moat' needs redefining.</strong><br><small>Source: <a href=\"https://www.latimes.com/business/story/2026-05-06/nvidia-faces-its-biggest-threat-yet-as-tech-giants-build-their-own-ai-chips\">LA Times</a> / <a href=\"https://finance.yahoo.com/news/nvidia-stock-faces-threat-google-123241502.html\">Yahoo Finance</a></small></li><li><strong>LA Times: The U.S.-China AI Gap Has Closed, Silicon Valley Is Getting Nervous</strong> — Over a year after DeepSeek's shock debut, China has become the testing ground for mass AI deployment. DeepSeek V4 trained on Huawei Ascend 950 and Cambricon chips (released April 24), open-sourcing V4-Pro and V4-Flash. <strong>Chip bans didn't stop Chinese AI — they spawned an alternative chip ecosystem.</strong><br><small>Source: <a href=\"https://www.latimes.com/business/story/2026-05-06/u-s-china-ai-gap-has-closed-and-silicon-valley-is-starting-to-notice\">LA Times</a></small></li><li><strong>OpenAI Releases GPT-5.5-Cyber But Only for 'Trusted Cyber Defenders'; UK AISI Calls It 'Strongest Cybersecurity Model Tested'</strong> — GPT-5.5-Cyber completed AISI's multi-step attack simulation end-to-end (only second system to do so). Irony: Altman mocked Anthropic's Mythos restrictions as 'fear-based marketing' on April 21; 10 days later OpenAI adopted the exact same approach. US government now drafting legislation to regulate releases of Mythos/GPT-5.5-Cyber-class models.<br><small>Source: <a href=\"https://aicentral.substack.com/p/the-ai-landscape-may-2026\">AI Central</a> / <a href=\"https://timesofindia.indiatimes.com/technology/tech-news/us-government-planning-law-so-google-openai-and-no-other-company-can-freely-release-an-ai-model-like-anthropics-mythos-that-scared-many/articleshow/130819415.cms\">Times of India</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>AI Compute Vertical Integration Accelerates</strong>: From 'buy Nvidia GPUs' to 'build your own chips' — tech giants replicating Apple Silicon's playbook</li><li><strong>Chip Ban Blowback</strong>: China forced to use Huawei Ascend → DeepSeek V4 proves viability → entire alternative chip ecosystem matures</li><li><strong>'Too Dangerous to Release' Becomes Industry Standard</strong>: Anthropic Mythos → OpenAI GPT-5.5-Cyber → US government legislation → AI safety shifts from self-regulation to mandatory oversight</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>These three stories point to one conclusion: AI's power structure is undergoing fundamental reorganization in 2026, and Nvidia may be the first victim of being 'too big to win.'</strong></p><p>Investors selling Nvidia during an AI bull market isn't panic — it's foresight. <strong>When Google, Amazon, Meta, and Microsoft simultaneously develop custom AI chips, Nvidia faces not 'competition' but 'customer defection.'</strong> This mirrors Intel's predicament: your core customers (PC makers) start building their own chips (Apple Silicon). The difference: Intel had 10 years to feel the impact; Nvidia may have 2-3. Meta's MTIA iterates every 6 months — that's not experimentation, that's strategic execution. <strong>Nvidia's moat was never the technology itself — it was ecosystem and CUDA lock-in. But when your four largest customers all have sufficient engineering resources to route around that lock-in, ecosystem advantage has a shorter shelf life than imagined.</strong></p><p>The US-China AI gap closing is the same narrative's flip side. <strong>US chip bans didn't halt Chinese AI — they spawned a complete alternative compute ecosystem.</strong> DeepSeek V4 training on Huawei Ascend 950 and Cambricon was considered impossible a year ago. Huawei publicly confirming cluster support on launch day wasn't quiet validation — it was a strategic declaration. More importantly, LA Times notes China's edge isn't model capability (gap is narrowing) but <strong>deployment velocity</strong> — when 1.4 billion people use AI like utilities, the application innovation and data flywheel can't be replicated in a 330-million market.</p><p>GPT-5.5-Cyber is today's darkest comedy. <strong>Altman publicly mocked Anthropic's Mythos restrictions as 'fear-based marketing' on April 21. Ten days later, OpenAI adopted the identical strategy.</strong> This isn't hypocrisy (well, maybe a little) — it's capability growth exceeding everyone's expectations, including the builders'. US government now drafting legislation — AI regulation officially enters 'how to regulate' phase.</p><p><strong>Pattern: AI is transitioning from 'growth phase' to 'reorganization phase.' Nvidia's monopoly loosening, China's alternative path proven viable, strongest models restricted. Winners in H2 2026 won't be 'who builds the strongest model' or 'who sells the most GPUs' — but who fastest converts AI capability into user value. Compute democratization + model democratization + application explosion = AI's value anchor migrating from upstream to downstream. For designers: when AI capability is no longer scarce, 'how you use AI' matters infinitely more than 'whether you have AI.'</strong></p></div>"
    },
    "cover": tech_cover,
    "sources": []
}

for i, (url, zh, en) in enumerate(tech_sources):
    tech_issue["sources"].append({
        "url": url,
        "title": {"zh": zh, "en": en},
        "image": tech_images[i]
    })

# Load existing issues and prepend
issues_path = "/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json"
with open(issues_path, 'r', encoding='utf-8') as f:
    issues = json.load(f)

issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open(issues_path, 'w', encoding='utf-8') as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Inserted 2 new issues (design + tech) for 2026-05-08. Total issues: {len(issues)}")
