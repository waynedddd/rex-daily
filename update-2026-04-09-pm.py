# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily update — 2026-04-09 evening edition"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            body = r.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', body, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', body, re.I)
        return m.group(1) if m else ""
    except Exception:
        return ""

# Sources
sources_design = [
    {
        "url": "https://creativepool.com/magazine/features/what-parts-of-the-creative-industry-will-be-fully-ai-by-the-end-of-2026.34151",
        "title_zh": "创意行业哪些领域将在 2026 年底被 AI 全面接管",
        "title_en": "What Parts of the Creative Industry Will Be Fully AI by End of 2026"
    },
    {
        "url": "https://medium.com/spring-2026-writing-for-interactive-media-icm506/ai-wont-kill-design-but-it-will-expose-bad-thinking-c019ddf3460a",
        "title_zh": "AI 不会杀死设计，但会暴露糟糕的思考",
        "title_en": "AI Won't Kill Design, But It Will Expose Bad Thinking"
    },
    {
        "url": "https://creativepool.com/magazine/features/10-ai-industry-trends-that-will-reshape-creativity-in-2026.34174",
        "title_zh": "2026 年重塑创意行业的 10 大 AI 趋势",
        "title_en": "10 AI Industry Trends That Will Reshape Creativity in 2026"
    }
]

sources_tech = [
    {
        "url": "https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/",
        "title_zh": "Anthropic 发布 Claude Mythos Preview：最强模型不公开卖，专攻网络安全",
        "title_en": "Anthropic Debuts Claude Mythos Preview for Cybersecurity Initiative"
    },
    {
        "url": "https://techcrunch.com/2026/04/07/i-cant-help-rooting-for-tiny-open-source-ai-model-maker-arcee/",
        "title_zh": "26 人团队 Arcee 发布 399B 开源推理模型 Trinity Large Thinking",
        "title_en": "Arcee Releases Trinity Large Thinking: 399B Open Source Reasoning Model"
    },
    {
        "url": "https://techcrunch.com/2026/04/07/uber-is-the-latest-to-be-won-over-by-amazons-ai-chips/",
        "title_zh": "Uber 采用 Amazon Trainium AI 芯片，自研芯片阵营持续扩大",
        "title_en": "Uber Adopts Amazon's Trainium AI Chips"
    },
    {
        "url": "https://techcrunch.com/2026/04/07/cisa-budget-cuts-700-million-cybersecurity-agency-trump/",
        "title_zh": "Trump 政府计划削减 CISA 网络安全预算 7 亿美元",
        "title_en": "Trump Administration Plans $700M CISA Budget Cut"
    }
]

print("Fetching og:images...")
for s in sources_design + sources_tech:
    s["image"] = get_og_image(s["url"])
    print(f"  {s['url'][:60]}... -> {'OK' if s['image'] else 'NONE'}")

design_issue = {
    "date": "2026-04-09",
    "section": "design",
    "title": {
        "zh": "创意行业 AI 替代路线图：库存摄影和广告文案已沦陷 · 设计不会被 AI 杀死，但糟糕的思考会 · 2026 年重塑创意行业的 10 大趋势",
        "en": "Creative Industry AI Replacement Roadmap: Stock Photography & Copywriting Fall First · AI Won't Kill Design But Exposes Bad Thinking · 10 Trends Reshaping Creativity in 2026"
    },
    "content": {
        "zh": """<h3>📌 AI × 设计</h3><ul><li><strong>Creativepool 深度报道：创意行业哪些领域将在 2026 年底被 AI 全面接管？</strong> — Creativepool 采访了多位行业领袖，绘制了一张 AI 替代路线图。<strong>已基本沦陷的领域：库存摄影（AI 图库已占新上传量的 40%+）、基础广告文案（程序化广告几乎全自动）、简单的品牌变体生成。</strong>正在被渗透的领域：UI/UX 原型、动效设计、市场调研报告。Huge CTO Marc Maleh 给出了最关键的洞察：<strong>AI 不是在「替代」创意人，而是在创造一个新角色——「Collaborative Human-AI Creative」</strong>。AI 现在不只是「建议」变体，它直接「部署」——动态个性化页面、自动化广告变体、实时预算调整——人类从「执行角色」转为「监督角色」。这和昨天 Figma Agent 画布能力的新闻完全呼应。<br><small>来源：<a href="https://creativepool.com/magazine/features/what-parts-of-the-creative-industry-will-be-fully-ai-by-the-end-of-2026.34151">Creativepool</a></small></li><li><strong>Medium 热文：AI 不会杀死设计，但它会暴露糟糕的思考</strong> — 这篇来自 ICM506 交互媒体写作课程的文章提出了一个犀利的观点：<strong>生成式 AI 可以自动化创意领域约 26% 的任务——但被自动化的恰恰是那些不需要真正思考的任务。</strong>真正的设计是定义问题、理解人的需求、做出有意义的权衡——这些 AI 做不了。作者认为 AI 的真正威胁不是替代好设计师，而是<strong>让坏设计师无处藏身</strong>——当 AI 能秒出 80 分的方案时，「能做出 80 分方案」就不再是一项有价值的技能。只有能做出 95 分方案的设计师才有存在的意义。<br><small>来源：<a href="https://medium.com/spring-2026-writing-for-interactive-media-icm506/ai-wont-kill-design-but-it-will-expose-bad-thinking-c019ddf3460a">Medium</a></small></li><li><strong>Creativepool：2026 年重塑创意行业的 10 大 AI 趋势</strong> — 这篇趋势总结中最值得关注的是「AI 叙事编织者」的概念。资深创意人 Ammar 指出：AI 正在成为一种<strong>「比大多数人都能更清晰地表达人类愿景」的工具</strong>。设计师的时间分配在发生根本性变化——更少花在手工制作上，更多花在<strong>编排设计的「故事」</strong>上。新角色正在涌现：AI 伦理学家、AI 工作流设计师、人机协作团队经理。中层常规工作将收缩，但新的角色空间也在打开。<br><small>来源：<a href="https://creativepool.com/magazine/features/10-ai-industry-trends-that-will-reshape-creativity-in-2026.34174">Creativepool</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 替代路线清晰化</strong>：库存摄影、基础文案、品牌变体——执行层已被压缩；但洞察力和审美判断力在升值</li><li><strong>「80 分陷阱」</strong>：AI 能秒出 80 分方案→只会做 80 分方案的设计师贬值→只有 95 分以上才有稀缺性</li><li><strong>设计师从 Maker 变 Orchestrator</strong>：不是推像素，而是编排叙事、定义约束、审核输出</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>今天这三篇文章合在一起，画出了 2026 年创意行业的一张残酷但清晰的地图。我读完的感受是：如果你还在靠「手活」吃饭，现在是认真焦虑的时候了。</strong></p><p>先说替代路线图。Creativepool 的报道终于把模糊的「AI 会影响创意行业」变成了具体的坐标：<strong>库存摄影、基础广告文案、简单品牌变体——这三块已经基本沦陷。</strong>这不是预测，这是已经发生的事实。如果你的工作主要是「从图库选图、改几个字、换个配色出变体」——你的工作在 2026 年已经被 AI 做了。但 Marc Maleh 的「Collaborative Human-AI Creative」概念指向了一个更深层的变化：<strong>AI 不只是工具，它正在重组创意生产的分工结构。</strong>过去是「创意总监想方案→设计师执行」，现在变成「创意总监想方案→AI 执行→设计师审核调整」。中间那层「执行层」被 AI 吃掉了。</p><p>Medium 那篇「AI 暴露糟糕思考」的文章虽然来自学术写作课程，但观点极其犀利。<strong>26% 的创意任务可被自动化——这个数字看似不大，但它精确切中了「不需要真正思考的任务」。</strong>这就是我说的「80 分陷阱」：当 AI 能在 30 秒内生成一个 80 分的 UI 方案时，「花 3 天做出 80 分方案」这种工作方式就彻底失去了市场。这对设计教育的冲击尤其大——大量设计课程还在教「如何做出合格的方案」，而不是「如何在 AI 的 80 分基础上做出 95 分的方案」。教育和行业之间的落差正在急剧拉大。</p><p>Creativepool 的 10 大趋势中，「AI 叙事编织者」的概念让我想到一个类比：<strong>设计师正在经历摄影师在数码时代经历过的转型。</strong>数码相机让「拍出清晰照片」不再需要技巧，但「拍出有灵魂的照片」依然需要。AI 让「做出合格的设计」不再需要技巧，但「做出有洞察力的设计」依然需要。关键的区别是：<strong>这次转型的速度快了 10 倍。</strong>摄影行业用了 15 年完成数码转型，设计行业可能只有 2-3 年。</p><p><strong>我的预判：2026 年下半年，创意行业会出现「大分化」——擅长与 AI 协作的设计师收入上升（因为产出量暴增），纯执行型设计师面临严重的供过于求。具体来说，自由职业平台（Upwork、Fiverr）上的基础设计价格将进一步下跌 30-50%，因为一个擅长 AI 的设计师能干过去三个人的活。但高端设计咨询的价格反而会上升——因为「定义问题」和「做出判断」的能力越来越稀缺。设计公司的招聘标准也会变化：不再看「能做什么风格」，而是看「能不能把 AI 的输出编排成品牌故事」。</strong></p></div>""",
        "en": """<h3>📌 AI × Design</h3><ul><li><strong>Creativepool: What Parts of the Creative Industry Will Be Fully AI by End of 2026?</strong> — Industry leaders map the AI replacement roadmap. <strong>Already fallen: stock photography (AI images now 40%+ of new uploads), basic ad copy (programmatic ads nearly fully automated), simple brand variant generation.</strong> Being infiltrated: UI/UX prototyping, motion design, market research. Huge CTO Marc Maleh's key insight: <strong>AI creates a new role — the \"Collaborative Human-AI Creative\"</strong>. AI now doesn't just suggest variations, it deploys them — dynamic personalized pages, automated creative variants, real-time budget shifts — humans move from execution to oversight.<br><small>Source: <a href="https://creativepool.com/magazine/features/what-parts-of-the-creative-industry-will-be-fully-ai-by-the-end-of-2026.34151">Creativepool</a></small></li><li><strong>AI Won't Kill Design, But It Will Expose Bad Thinking</strong> — Generative AI can automate ~26% of creative tasks — <strong>precisely the tasks requiring no real thinking.</strong> Real design is defining problems, understanding human needs, making meaningful trade-offs. AI's real threat isn't replacing good designers — it's <strong>leaving bad designers nowhere to hide.</strong> When AI produces 80-point solutions instantly, only 95-point designers retain value.<br><small>Source: <a href="https://medium.com/spring-2026-writing-for-interactive-media-icm506/ai-wont-kill-design-but-it-will-expose-bad-thinking-c019ddf3460a">Medium</a></small></li><li><strong>10 AI Industry Trends Reshaping Creativity in 2026</strong> — Most notable: the \"AI Narrative Weaver\" concept. AI becomes <strong>a tool that articulates human vision \"more clearly than most of us can.\"</strong> Designers spend less time on manual crafting, more on orchestrating design's \"story.\" New roles emerging: AI ethicists, AI workflow designers, human-AI team managers.<br><small>Source: <a href="https://creativepool.com/magazine/features/10-ai-industry-trends-that-will-reshape-creativity-in-2026.34174">Creativepool</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI replacement roadmap crystallizes: stock photos, basic copy, brand variants compressed; insight and aesthetic judgment appreciate</li><li>The \"80-point trap\": AI instant 80-point solutions devalue 80-point designers; only 95+ retains scarcity</li><li>Designer: Maker → Orchestrator — not pushing pixels but orchestrating narrative</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>These three articles draw a cruel but clear map of the 2026 creative industry. If you're still making a living on \"craft skills\" alone, it's time for serious concern.</strong></p><p>The replacement roadmap finally makes concrete what was vague: <strong>stock photography, basic ad copy, simple brand variants — already fallen.</strong> Marc Maleh's \"Collaborative Human-AI Creative\" points deeper: AI is reorganizing creative production's division of labor, eating the execution layer between creative directors and final output.</p><p>The \"26% automatable\" figure precisely targets tasks requiring no real thinking — the \"80-point trap.\" This devastates design education still teaching \"how to produce competent work\" rather than \"how to push AI's 80 to 95.\"</p><p><strong>Prediction: H2 2026 brings the \"great divergence\" — AI-skilled designers earn more (output multiplied), pure executors face severe oversupply. Freelance platform base design prices drop 30-50%. But high-end design consulting prices rise — problem-definition and judgment become scarcer. Hiring shifts from \"what styles can you do\" to \"can you orchestrate AI output into brand narrative.\"</strong></p></div>"""
    },
    "cover": sources_design[0].get("image", ""),
    "sources": [
        {
            "title": {"zh": s["title_zh"], "en": s["title_en"]},
            "url": s["url"],
            "image": s.get("image", "")
        } for s in sources_design
    ]
}

tech_issue = {
    "date": "2026-04-09",
    "section": "tech",
    "title": {
        "zh": "Anthropic 不卖最强模型 Mythos，转做网络安全联盟 · 26 人小队 Arcee 发布 399B 开源推理模型叫板中国 · Uber 投奔 Amazon 自研芯片，开源模型井喷",
        "en": "Anthropic Won't Sell Mythos — Deploys It for Cybersecurity Instead · 26-Person Arcee Ships 399B Open Source Reasoning Model · Uber Joins Amazon Chip Camp as Open Source Models Explode"
    },
    "content": {
        "zh": """<h3>📌 AI × 科技</h3><ul><li><strong>Anthropic 发布 Claude Mythos Preview：最强模型不公开卖，专供 40+ 科技公司做网络安全</strong> — Anthropic 本周做了一件出乎意料的事：<strong>它最强大的新模型 Claude Mythos Preview 不对外销售，而是提供给包括 Apple、Amazon、Microsoft 在内的 40 多家科技公司，专门用于发现和修补关键软件的安全漏洞。</strong>NYT 报道称，这是 Anthropic 在被五角大楼列为「供应链风险」（后被联邦法官叫停）之后的战略转向——通过「安全优先」的形象重建信任。与此同时，CISA（美国网络安全与基础设施安全局）正面临 Trump 政府 7 亿美元的预算削减。<strong>一边是政府在削弱网络安全机构，一边是 AI 公司在填补真空——这个对比耐人寻味。</strong><br><small>来源：<a href="https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/">TechCrunch</a>、<a href="https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html">NYT</a></small></li><li><strong>26 人团队 Arcee 发布 399B 开源推理模型 Trinity Large Thinking：Western 开源的反击</strong> — Arcee，一家只有 26 人、融资仅 2000 万美元的 SF 初创公司，发布了 <strong>Trinity Large Thinking——一个 399B 参数的 MoE 推理模型，每个 token 仅激活 13B 参数，Apache 2.0 开源</strong>。CEO Mark McQuade 对 TechCrunch 的表态很直白：要给西方公司一个「没有理由使用中国模型」的选择。这个模型基于 256 个专家、每次激活 4 个的稀疏 MoE 架构，在推理能力上号称是「非中国公司发布的最强开源模型」。同一周，Google 发布了 Gemma 4（Apache 2.0），智谱发布了 GLM-5.1（MIT 许可），阿里发布了 Qwen 3.6-Plus。<strong>开源模型正在经历寒武纪大爆发。</strong><br><small>来源：<a href="https://techcrunch.com/2026/04/07/i-cant-help-rooting-for-tiny-open-source-ai-model-maker-arcee/">TechCrunch</a>、<a href="https://datanorth.ai/news/arcee-ai-releases-trinity-large-thinking-open-source">DataNorth</a></small></li><li><strong>Uber 采用 Amazon Trainium AI 芯片：自研芯片阵营持续壮大</strong> — Uber 成为最新一家采用 Amazon 自研 AI 芯片 Trainium 的科技巨头。此前 Anthropic、OpenAI 甚至 Apple 都已采用。<strong>Amazon 的自研芯片战略正在从「内部优化」转变为「行业标准」——这对 Nvidia 的垄断地位构成了实质性挑战。</strong>TechCrunch 此前独家探访了 Amazon 的 Trainium 实验室，透露芯片设计团队正在研发第三代产品。<br><small>来源：<a href="https://techcrunch.com/2026/04/07/uber-is-the-latest-to-be-won-over-by-amazons-ai-chips/">TechCrunch</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 公司开始定义「安全基础设施」</strong>：Anthropic 不卖最强模型而用它做安全——AI 公司正在填补政府退出的领域</li><li><strong>开源模型寒武纪爆发</strong>：Arcee Trinity、Gemma 4、GLM-5.1、Qwen 3.6-Plus——一周内四大开源模型发布</li><li><strong>AI 算力格局重塑</strong>：Amazon Trainium 阵营扩大，Nvidia 垄断松动</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>本周科技新闻最重要的信号不在任何单条新闻里，而在它们的交叉点上。让我把这几条线索串起来。</strong></p><p>Anthropic 不卖 Mythos 这件事，表面上是「负责任的 AI」叙事，但背后的博弈更复杂。回想一下时间线：<strong>2 月被五角大楼列为「供应链风险」→ 3 月联邦法官叫停该决定 → 4 月推出 Mythos 做安全联盟</strong>。这不是巧合，这是精心设计的信任修复策略。Anthropic 在说：「我最强的模型不拿来赚钱，而是用来保护你的基础设施。」但这也意味着 <strong>Anthropic 正在创造一种新的商业模式——通过「安全服务」而非「API 销售」来变现最强模型。</strong>如果 Mythos 真的在 40 家公司的代码库中发现了大量漏洞，它将拥有一种前所未有的影响力——不是市场占有率，而是「安全债务话语权」。</p><p>把 Mythos 和 CISA 预算削减 7 亿美元放在一起看，画面就更有意思了。<strong>政府在退出网络安全投入，AI 公司在进入。</strong>这不是好事也不是坏事——但它意味着一个根本性的权力转移：网络安全的基础设施正在从公共部门向私营部门迁移。Anthropic 今天是「安全联盟」，明天可能是「安全标准制定者」。当一个 AI 公司比政府更了解关键软件的漏洞时，谁的话语权更大？</p><p>再看开源模型这边。Arcee 的 Trinity 模型让我兴奋的不是参数量，而是<strong>经济学：26 个人、2000 万美元、399B 参数、Apache 2.0</strong>。和一年前相比，训练前沿模型的门槛已经下降了一个数量级。加上同一周的 Gemma 4、GLM-5.1、Qwen 3.6-Plus——<strong>开源阵营在一周内发布了四个前沿模型。</strong>这对闭源模型的定价权构成了严重威胁。当免费的开源模型在多数任务上能达到闭源模型 90% 的性能时，企业为什么要付 API 费用？Arcee CEO 的「给西方公司不用中国模型的理由」也暗示了另一个维度：<strong>开源模型正在成为地缘政治工具</strong>——不只是技术选择，还是「站队」选择。</p><p><strong>我的预判：Anthropic 的「安全优先」策略将在 Q2 内引发 OpenAI 和 Google 的跟进——预计两家都会推出类似的安全联盟计划。开源模型方面，2026 Q3 之前至少还会出现 2-3 个 Arcee 级别的初创公司，用极低成本训练出前沿模型——这将迫使 OpenAI 和 Anthropic 重新定价。Amazon Trainium 的扩张将在下半年加速，预计年底前会有 10+ 家主要科技公司采用——Nvidia 股价可能因此面临 15-20% 的估值调整压力。最大胆的预测：到 2026 年底，「用哪个开源模型」将像「用哪个 Linux 发行版」一样，成为技术团队的身份标识。</strong></p></div>""",
        "en": """<h3>📌 AI × Tech</h3><ul><li><strong>Anthropic Launches Claude Mythos Preview: Most Powerful Model Not for Sale — Dedicated to Cybersecurity</strong> — Anthropic's most powerful model, Claude Mythos Preview, <strong>won't be sold publicly. Instead, it's provided to 40+ tech companies including Apple, Amazon, and Microsoft for finding and patching critical security vulnerabilities.</strong> This follows Anthropic being designated a Pentagon \"supply chain risk\" (later blocked by a federal judge). Meanwhile, CISA faces a $700M budget cut from the Trump administration. <strong>The government retreats from cybersecurity as AI companies fill the vacuum — a telling contrast.</strong><br><small>Source: <a href="https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/">TechCrunch</a>, <a href="https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html">NYT</a></small></li><li><strong>26-Person Arcee Ships 399B Open Source Reasoning Model Trinity Large Thinking</strong> — On a $20M budget, Arcee released <strong>Trinity Large Thinking — a 399B-parameter MoE reasoning model with 13B active parameters per token, Apache 2.0 licensed.</strong> CEO aims to give Western companies \"no reason to use Chinese models.\" Same week: Google's Gemma 4, Zhipu's GLM-5.1, Alibaba's Qwen 3.6-Plus. <strong>Open source models are experiencing a Cambrian explosion.</strong><br><small>Source: <a href="https://techcrunch.com/2026/04/07/i-cant-help-rooting-for-tiny-open-source-ai-model-maker-arcee/">TechCrunch</a>, <a href="https://datanorth.ai/news/arcee-ai-releases-trinity-large-thinking-open-source">DataNorth</a></small></li><li><strong>Uber Adopts Amazon Trainium AI Chips: Custom Silicon Camp Grows</strong> — Uber joins Anthropic, OpenAI, and Apple in adopting Amazon's Trainium chips. <strong>Amazon's custom chip strategy shifts from \"internal optimization\" to \"industry standard\" — posing real challenge to Nvidia's monopoly.</strong><br><small>Source: <a href="https://techcrunch.com/2026/04/07/uber-is-the-latest-to-be-won-over-by-amazons-ai-chips/">TechCrunch</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI companies defining \"security infrastructure\": Anthropic fills the gap government vacates</li><li>Open source Cambrian explosion: four frontier models in one week</li><li>Compute landscape reshaping: Amazon Trainium camp expands, Nvidia monopoly loosens</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>The most important signal isn't in any single story but at their intersection.</strong></p><p>Anthropic not selling Mythos is a trust-repair strategy after the Pentagon designation. But it also creates <strong>a new business model — monetizing the strongest model through \"security services\" rather than API sales.</strong> If Mythos finds critical vulnerabilities across 40 companies' codebases, Anthropic gains unprecedented influence — not market share, but \"security debt discourse power.\"</p><p>Combined with CISA's $700M budget cut: <strong>government exits cybersecurity, AI companies enter.</strong> A fundamental power transfer from public to private sector in security infrastructure.</p><p>Arcee's economics thrill me most: <strong>26 people, $20M, 399B parameters, Apache 2.0.</strong> Training costs dropped an order of magnitude. Four frontier open source models in one week threatens closed models' pricing power. \"Give Western companies no reason to use Chinese models\" adds a geopolitical dimension — <strong>open source models become alignment tools.</strong></p><p><strong>Predictions: OpenAI and Google will launch similar security alliances by Q2. 2-3 more Arcee-class startups will emerge by Q3. Amazon Trainium adoption reaches 10+ major companies by year-end, pressuring Nvidia valuation 15-20%. Boldest: by end of 2026, \"which open source model\" becomes a team identity marker like Linux distros.</strong></p></div>"""
    },
    "cover": sources_tech[0].get("image", ""),
    "sources": [
        {
            "title": {"zh": s["title_zh"], "en": s["title_en"]},
            "url": s["url"],
            "image": s.get("image", "")
        } for s in sources_tech
    ]
}

# Read existing, prepend, write
with open("issues.json", "r") as f:
    issues = json.load(f)

# Insert at front (design first, then tech, so tech ends up at index 0)
issues.insert(0, design_issue)
issues.insert(0, tech_issue)

with open("issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\nDone! {len(issues)} total issues. New issues prepended.")
