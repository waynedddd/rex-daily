# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Evening Update - March 12, 2026"""
import json
import urllib.request
import re
import ssl

def fetch_og_image(url, timeout=8):
    """Fetch og:image from a URL."""
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            html = resp.read(50000).decode("utf-8", errors="ignore")
            m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
            if not m:
                m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
            return m.group(1) if m else None
    except Exception as e:
        print(f"  og:image fetch failed for {url}: {e}")
        return None

# Define new evening entries
design_sources = [
    {"url": "https://www.buildingcreativemachines.com/p/ai-and-creativity-monthly-brief-march",
     "title_zh": "AI & Creativity Monthly Brief — March 2026",
     "title_en": "AI & Creativity Monthly Brief — March 2026"},
    {"url": "https://www.figma.com/resource-library/ai-product-design/",
     "title_zh": "5 Best AI Product Design Tools 2026 - Figma",
     "title_en": "5 Best AI Product Design Tools 2026 - Figma"},
    {"url": "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
     "title_zh": "9 Best AI Tools for UI/UX Designers 2026 - Toools.design",
     "title_en": "9 Best AI Tools for UI/UX Designers 2026 - Toools.design"},
    {"url": "https://www.youtube.com/watch?v=Y0n6F9VlLVc",
     "title_zh": "2026 AI Design Field Report - YouTube",
     "title_en": "The 2026 AI Design Field Report - YouTube"},
]

tech_sources = [
    {"url": "https://www.vox.com/podcasts/481567/ai-claude-chatgpt-iran-war-pentagon-autonomous-weapons",
     "title_zh": "美国可能如何在伊朗使用 AI - Vox",
     "title_en": "How the US might be using AI in Iran - Vox"},
    {"url": "https://nymag.com/intelligencer/article/military-ai-iran-openai-claude.html",
     "title_zh": "军方能阻止 AI 变成终结者吗？ - NY Mag",
     "title_en": "Can the Military Prevent AI From Going Full Terminator? - NY Mag"},
    {"url": "https://medium.com/@annie_7775/ai-updates-for-the-week-of-3-8-26-66e233f3a206",
     "title_zh": "AI 周报 3/8/26: Gemini 3.1 Flash-Lite、Claude Code 语音 - Medium",
     "title_en": "AI Updates for the Week of 3/8/26 - Medium"},
    {"url": "https://voxukraine.org/en/the-war-on-iran-and-the-war-on-anthropic",
     "title_zh": "伊朗战争与 Anthropic 之战 - VoxUkraine",
     "title_en": "The War on Iran and the War on Anthropic - VoxUkraine"},
]

print("Fetching og:images for design sources...")
for s in design_sources:
    s["image"] = fetch_og_image(s["url"])
    print(f"  {s['url']}: {s['image']}")

print("Fetching og:images for tech sources...")
for s in tech_sources:
    s["image"] = fetch_og_image(s["url"])
    print(f"  {s['url']}: {s['image']}")

design_cover = next((s["image"] for s in design_sources if s["image"]), None)
tech_cover = next((s["image"] for s in tech_sources if s["image"]), None)

design_entry = {
    "date": "2026-03-12",
    "section": "design",
    "title": {
        "zh": "生成式设计进入「流水线时代」· Figma 定义 AI 产品设计五步法 · 创意工具的竞争焦点从生成转向流程",
        "en": "Generative Design Enters the Pipeline Era · Figma Defines 5-Step AI Product Design · Creative Tool Competition Shifts from Generation to Process"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计（晚间更新）</h3><ul><li><strong>Building Creative Machines 发布 3 月 AI 创意月报：生成式设计正在变成「可管理的流水线」</strong> — 这份来自创意 AI 研究社区的月报指出一个关键转变：2026 年 3 月，生成式设计不再是「输入 prompt，看看能出什么」的随机过程，而是正在被组织成可测量、可迭代的工作流水线。竞争优势从「谁的 AI 生成更好」转向「谁的创意工具+流程更高效」——换句话说，instrumented loops（可观测的反馈循环）和质量控制机制成了新的护城河。<br><small>来源：<a href=\"https://www.buildingcreativemachines.com/p/ai-and-creativity-monthly-brief-march\">AI & Creativity Monthly Brief March 2026</a></small></li><li><strong>Figma 发布 AI 产品设计指南：5 款工具的「连接式工作流」</strong> — Figma 官方博客系统性地阐述了 AI 产品设计的最佳实践：不是选一个万能工具，而是用 5 款工具构建一个互相连接的 pipeline。Figma Design 负责核心 UI，Canva Magic Studio 处理品牌视觉，Adobe Firefly 做素材生成——关键词是「连接」和「编排」，而非单点工具的性能。<br><small>来源：<a href=\"https://www.figma.com/resource-library/ai-product-design/\">5 Best AI Product Design Tools 2026 - Figma</a></small></li><li><strong>Toools.design 横评更新：Stitch（Google）和 Flowstep 入场</strong> — Google Stitch 支持 prompt + 图像输入生成 UI，Flowstep 以「逐步引导」降低上手门槛。9 款工具的横评显示，免费层和代码导出已成标配，下一个差异化战场是<strong>品牌一致性保持</strong>——上传你的设计系统，AI 生成的结果与品牌语言一致。<br><small>来源：<a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">9 Best AI Tools for UI/UX Designers 2026</a></small></li><li><strong>YouTube 深度报告：顶级团队实际如何使用 AI 设计工具</strong> — 一个高热度视频揭示了理想与现实的差距：虽然 AI 工具的 demo 很炫，但真实团队中 AI 主要被用于三件事——初稿加速、变体批量生成、设计审查辅助。还没有团队敢让 AI 做最终决策。<br><small>来源：<a href=\"https://www.youtube.com/watch?v=Y0n6F9VlLVc\">The 2026 AI Design Field Report - YouTube</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>从「生成」到「流水线」</strong>：生成式设计的竞争焦点从产出质量转向流程效率</li><li><strong>品牌一致性成新战场</strong>：能保持设计系统一致性的 AI 工具将胜出</li><li><strong>AI 仍在「辅助」而非「决策」</strong>：实际使用中 AI 做初稿和变体，人类做判断</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天的设计新闻看似碎片化，但拼在一起，画出了一条清晰的演进线：AI 设计工具正在从「魔法时刻」走向「工业流水线」。</strong></p><p>Building Creative Machines 的月报用了一个精准的词：「managed pipeline」。两年前，AI 设计的叙事是「输入一句话，获得惊人的设计」。现在，真正在前线工作的团队发现，一次性生成的东西几乎不能直接用——你需要的是可重复、可测量、可迭代的生成流程。这正是 Figma 发布的那篇 5 工具指南的核心逻辑：不是一个工具搞定一切，而是 5 个工具各司其职，通过 API 和文件格式互相连接。</p><p>这个趋势与今天早间报道的「灵魂派 vs 系统派」分裂形成了有趣的张力。Moonchild 代表的「灵魂派」追求一次性的创意爆发，而 Figma 描述的流水线模式本质上是「系统派」的终极形态。我认为<strong>短期内两者会并存，但中长期看，流水线模式会赢。</strong>原因很简单：企业需要可预测性。一个设计团队不能每次都靠灵感 prompt 出好结果——他们需要的是 80% 的情况下 AI 能给出符合品牌规范的合格输出，然后设计师在剩下的 20% 上投入创意。</p><p>YouTube 那个 Field Report 的观察也印证了这一点：<strong>没有团队敢让 AI 做最终设计决策。</strong>AI 做的是初稿、变体、审查——全是流水线中间环节。设计师的角色不是被取代，而是从「执行者」变成了「质量总监 + 流水线架构师」。这跟软件工程领域从手写代码到 CI/CD pipeline 的演进如出一辙。</p><p>我的预测：2026 下半年，你会看到一个新品类出现——「AI 设计流水线编排工具」，类似于 Zapier 之于 SaaS 工具。谁能把 Moonchild 的创意生成、Figma 的精细编辑、Motiff 的代码导出、Attention Insight 的质量验证串成一键流水线，谁就是下一个独角兽。目前最接近的是 Figma 自己，但它的生态墙可能反而成为包袱。</p></div>",
        "en": "<h3>📌 AI × Design (Evening Update)</h3><ul><li><strong>Building Creative Machines March Brief: Generative Design Becomes a Managed Pipeline</strong> — The competitive edge shifts from \"whose AI generates better\" to \"whose creative tooling + process is more efficient.\" Instrumented loops and quality control are the new moats.<br><small>Source: <a href=\"https://www.buildingcreativemachines.com/p/ai-and-creativity-monthly-brief-march\">AI & Creativity Monthly Brief</a></small></li><li><strong>Figma Publishes AI Product Design Guide: 5-Tool Connected Workflow</strong> — Not one magic tool but five connected tools forming a pipeline. Figma Design for core UI, Canva for brand visuals, Adobe Firefly for asset generation.<br><small>Source: <a href=\"https://www.figma.com/resource-library/ai-product-design/\">Figma</a></small></li><li><strong>Toools.design Update: Google Stitch and Flowstep Enter the Arena</strong> — Brand consistency preservation emerges as the next differentiator — upload your design system, AI generates on-brand results.<br><small>Source: <a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">Toools.design</a></small></li><li><strong>YouTube Field Report: How Top Teams Actually Use AI Design Tools</strong> — AI used for drafts, variant generation, and review assistance. No team lets AI make final design decisions yet.<br><small>Source: <a href=\"https://www.youtube.com/watch?v=Y0n6F9VlLVc\">YouTube</a></small></li></ul><h3>🔄 Trends</h3><ul><li>From generation to pipeline: competition shifts to process efficiency</li><li>Brand consistency becomes the new battleground</li><li>AI still assists, doesn't decide: humans retain final judgment</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>AI design tools are graduating from \"magic moments\" to \"industrial pipelines.\"</strong> Building Creative Machines nails it: managed pipelines with instrumented loops are replacing one-shot prompt-to-design. Figma's 5-tool guide confirms it — orchestration beats individual tool power. This creates tension with morning's \"Soul vs System\" split: Moonchild's creative bursts vs Figma's systematic pipelines. My bet: pipelines win long-term because enterprises need predictability. The YouTube Field Report confirms it — no team lets AI make final calls. Designers become quality directors + pipeline architects. Prediction: H2 2026 will see a new category — \"AI design pipeline orchestrators\" — the Zapier of creative tools. Whoever chains Moonchild's generation + Figma's editing + Motiff's code export + Attention Insight's validation into one-click pipelines builds the next unicorn.</p></div>"
    },
    "cover": design_cover,
    "sources": [{"title": {"zh": s["title_zh"], "en": s["title_en"]}, "url": s["url"], "image": s["image"]} for s in design_sources]
}

tech_entry = {
    "date": "2026-03-12",
    "section": "tech",
    "title": {
        "zh": "AI 战争伦理深度调查：Claude 和 ChatGPT 是否正在帮美国打仗？· Gemini 3.1 Flash-Lite 发布 · Claude Code 获得语音模式",
        "en": "AI War Ethics Deep Dive: Are Claude and ChatGPT Helping the US Fight? · Gemini 3.1 Flash-Lite Launches · Claude Code Gets Voice Mode"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技（晚间更新）</h3><ul><li><strong>Vox 深度播客：Claude 和 ChatGPT 是否正在帮美国在伊朗打仗？</strong> — Vox 和 NY Magazine 分别发布重磅调查，揭示 AI 在军事冲突中的实际使用情况。关键发现：自主武器的支持者认为「机器犯错可能比人类少」，但现实中「什么算非法命令」在战场上远非黑白分明。Anthropic 要求「不用于大规模监控和自主武器」，五角大楼说「不会非法使用」——措辞看似接近，但语义鸿沟巨大。NY Mag 的分析指出：大多数人误以为「自主武器」意味着终结者式的机器人，但实际上可能是一架自主决定攻击目标的无人机。<br><small>来源：<a href=\"https://www.vox.com/podcasts/481567/ai-claude-chatgpt-iran-war-pentagon-autonomous-weapons\">How the US might be using AI in Iran - Vox</a> | <a href=\"https://nymag.com/intelligencer/article/military-ai-iran-openai-claude.html\">Can the Military Prevent AI From Going Full Terminator? - NY Mag</a></small></li><li><strong>VoxUkraine 分析：伊朗战争与 Anthropic 之战是同一场战争</strong> — 来自乌克兰视角的深度分析：五角大楼一边在伊朗推进 AI 军事应用（包括大规模监控和自主武器系统信号），一边惩罚反对这些应用的 Anthropic。这两条线不是巧合，而是同一个决策逻辑的两面——<strong>美国政府正在系统性地移除 AI 军事化的伦理护栏。</strong><br><small>来源：<a href=\"https://voxukraine.org/en/the-war-on-iran-and-the-war-on-anthropic\">The War on Iran and the War on Anthropic - VoxUkraine</a></small></li><li><strong>Google 发布 Gemini 3.1 Flash-Lite：超轻量高速推理模型</strong> — AI 周报确认 Google 本周发布 Gemini 3.1 Flash-Lite，主打极低延迟和极低成本，面向高吞吐量 API 调用场景。这是 Google 在「便宜够用」市场段的又一次精准打击，直接对标 GPT-4o-mini 和 Claude Haiku。<br><small>来源：<a href=\"https://medium.com/@annie_7775/ai-updates-for-the-week-of-3-8-26-66e233f3a206\">AI Updates for the Week of 3/8/26 - Medium</a></small></li><li><strong>Claude Code 推出语音模式：用说话写代码</strong> — Anthropic 为 Claude Code 新增语音交互能力，开发者可以通过语音描述需求、审查代码、给出反馈。这不是噱头——考虑到 Claude Code 已经登顶开发者工具榜（今早 Pragmatic Engineer 调研），语音模式让「边走路边写代码」成为可能。<br><small>来源：<a href=\"https://medium.com/@annie_7775/ai-updates-for-the-week-of-3-8-26-66e233f3a206\">AI Updates for the Week of 3/8/26 - Medium</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 军事化的伦理辩论白热化</strong>：从行业内部分歧升级为地缘政治议题</li><li><strong>轻量模型军备竞赛</strong>：Gemini Flash-Lite 加入 GPT-4o-mini、Claude Haiku 的低价高速赛道</li><li><strong>开发工具多模态化</strong>：Claude Code 语音模式预示编程交互范式转变</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天晚间的三条新闻串联起来，讲的是同一个故事：AI 正在从工具变成武器，而最有伦理意识的公司正在为此付出代价。</strong></p><p>Vox 的播客和 NY Magazine 的深度报道终于把一个行业心知肚明但没人愿意正面谈的问题搬上台面：AI 到底在不在帮美国打仗？答案几乎肯定是「是」，只是程度和方式我们无法完全确认。NY Mag 的采访揭示了一个细思极恐的细节：<strong>Anthropic 和五角大楼的分歧不在于「是否可以用 AI」，而在于「自主」这个词的定义。</strong>五角大楼说「不会非法使用」——但在战争中，什么算「非法」？一架无人机自主选择了一个「高价值目标」，这是自主武器还是辅助工具？语义模糊本身就是权力的操作空间。</p><p>VoxUkraine 的分析更加直白：伊朗的军事行动和 Anthropic 的遭遇是同一枚硬币的两面。政府需要 AI 军事化，所以它一边推进部署，一边打压反对者。这不是阴谋论——这是权力运作的标准模式。而 Google 在这场风暴中安静扩张国防合同的行为，与今早 Axios 报道的\"渔翁得利\"完全一致。</p><p>技术面上，Gemini 3.1 Flash-Lite 的发布和 Claude Code 语音模式形成了有趣的呼应。Google 在打价格战——Flash-Lite 不是要成为最聪明的模型，而是要成为最便宜的。在 API 调用成本成为企业 AI 部署最大变量的今天，这是聪明的策略。而 Claude Code 加语音，结合其开发者工具第一的位置，等于是在说：<strong>你连键盘都不需要了，走在路上就能指挥 AI 团队写代码。</strong>这与今早讨论的「人类架构师 + AI Agent 团队」范式完美契合——架构师需要的是表达意图的能力，而语音是最自然的意图表达方式。</p><p>最后一个观察：这周的新闻密度异常高。Gemini 3.1、Claude Code 语音、Codex Security、Qwen 3.5——四家同时放大招。9 月发布的 Claude Opus/Sonnet 4.6 还在消化中，新一轮军备竞赛就已经开始了。<strong>AI 行业的时间尺度正在压缩——两年前一个大模型更新能讨论一个月，现在一周内就被下一个淹没。</strong>对设计师和开发者来说，选择工具的能力比使用工具的能力更重要了。</p></div>",
        "en": "<h3>📌 AI × Tech (Evening Update)</h3><ul><li><strong>Vox Deep Dive: Are Claude and ChatGPT Helping the US Fight in Iran?</strong> — Vox and NY Magazine investigate AI's actual military use. Anthropic's \"no mass surveillance or autonomous weapons\" vs Pentagon's \"no unlawful use\" — the semantic gap is enormous. What counts as \"autonomous\" in a war zone?<br><small>Source: <a href=\"https://www.vox.com/podcasts/481567/ai-claude-chatgpt-iran-war-pentagon-autonomous-weapons\">Vox</a> | <a href=\"https://nymag.com/intelligencer/article/military-ai-iran-openai-claude.html\">NY Mag</a></small></li><li><strong>VoxUkraine: The War on Iran and the War on Anthropic Are the Same War</strong> — The US government is systematically removing ethical guardrails on AI militarization: deploying in Iran while punishing Anthropic for objecting.<br><small>Source: <a href=\"https://voxukraine.org/en/the-war-on-iran-and-the-war-on-anthropic\">VoxUkraine</a></small></li><li><strong>Google Releases Gemini 3.1 Flash-Lite</strong> — Ultra-low latency and cost for high-throughput API calls. Targeting the cheap-and-good-enough market against GPT-4o-mini and Claude Haiku.<br><small>Source: <a href=\"https://medium.com/@annie_7775/ai-updates-for-the-week-of-3-8-26-66e233f3a206\">Medium</a></small></li><li><strong>Claude Code Gets Voice Mode</strong> — Voice interaction for describing requirements, reviewing code, giving feedback. Combined with its #1 developer tool ranking, enables coding while walking.<br><small>Source: <a href=\"https://medium.com/@annie_7775/ai-updates-for-the-week-of-3-8-26-66e233f3a206\">Medium</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI militarization ethics debate goes mainstream</li><li>Lightweight model arms race: Flash-Lite joins the cheap-fast lane</li><li>Developer tools go multimodal: voice-driven coding arrives</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Three evening stories, one narrative: AI is becoming a weapon, and the most ethical company is paying the price.</strong> Vox and NY Mag finally put the question on the table: is AI fighting America's wars? Almost certainly yes. The semantic gap between Anthropic's \"no autonomous weapons\" and Pentagon's \"no unlawful use\" is where power operates — what's \"unlawful\" in a war zone? VoxUkraine connects the dots: Iran deployment + Anthropic punishment = systematic removal of ethical guardrails. Google quietly wins. On the tech side, Gemini Flash-Lite plays the price war (smartest cheap model wins enterprise volume), while Claude Code's voice mode + its #1 ranking = architects directing AI teams by voice while walking. The industry's time scale is compressing — two years ago a major model update dominated conversation for a month; now it's buried in a week. For designers and developers, choosing tools matters more than using them.</p></div>"
    },
    "cover": tech_cover,
    "sources": [{"title": {"zh": s["title_zh"], "en": s["title_en"]}, "url": s["url"], "image": s["image"]} for s in tech_sources]
}

# Load existing issues.json
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

# Prepend new entries
issues = [design_entry, tech_entry] + issues

# Write back
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\nDone! Total issues: {len(issues)}")
print(f"Design cover: {design_cover}")
print(f"Tech cover: {tech_cover}")
