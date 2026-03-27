# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Update - 2026-03-27"""
import json, urllib.request, re, html

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

# Fetch og:images
urls = {
    "rgd": "https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
    "medium": "https://medium.com/@shrey_uiux/5-ai-design-tools-that-are-still-worth-using-after-the-hype-2026-2809b0ce002a",
    "figma_make": "https://www.figma.com/solutions/ai-design-generator/",
    "figma_tools": "https://www.figma.com/resource-library/ai-design-tools/",
    "toools": "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
    "meta_register": "https://www.theregister.com/2026/03/12/meta_custom_chips/",
    "meta_cnbc": "https://www.cnbc.com/2026/03/11/meta-ai-mtia-chip-data-center.html",
    "atlassian_guardian": "https://www.theguardian.com/technology/2026/mar/12/atlassian-layoffs-software-technology-ai-push-mike-cannon-brookes-asx",
    "atlassian_reuters": "https://www.reuters.com/technology/atlassian-lay-off-about-1600-people-pivot-ai-2026-03-11/",
    "atlassian_bi": "https://www.businessinsider.com/layoff-ai-strategy-atlassian-block-2026-3",
    "ai_tools_record": "https://www.caller.com/press-release/story/100307/ai-tool-launches-hit-record-pace-as-industry-moves-from-experimentation-to-infrastructure/",
    "almcorp": "https://almcorp.com/blog/how-to-use-ai-for-graphic-design/",
}

print("Fetching og:images...")
images = {}
for key, url in urls.items():
    img = get_og_image(url)
    images[key] = img
    print(f"  {key}: {img[:60] if img else '(none)'}")

# Load existing issues
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

design_issue = {
    "date": "2026-03-27",
    "section": "design",
    "title": {
        "zh": "AI 设计工具进入「去炒作」时代：嵌入式工作流取代独立工具 · Figma Make 全面嵌入设计生态 · Agentic 设计工作流初现端倪",
        "en": "AI Design Tools Enter 'Post-Hype' Era: Embedded Workflows Replace Standalone Tools · Figma Make Embeds Across Design Ecosystem · Agentic Design Workflows Emerge"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul><li><strong>AI 设计工具的「去炒作期」：嵌入现有工作流才是正途</strong> — 加拿大注册平面设计师协会（RGD）发布深度文章指出，2026 年 AI 设计工具的核心趋势不再是「替代设计师」，而是「嵌入现有工作流」。Adobe Firefly 在早期探索阶段辅助测试表面纹理和视觉方向，Mixboard 则切入灵感拼贴环节。文章特别强调：设计师应审查每个工具的训练数据来源、数据政策和许可条款。与此同时，Medium 上的设计评论指出，经历炒作周期后，2026 年真正值得用的 AI 设计工具只有 5 个——大浪淘沙后，存活下来的是那些<strong>解决具体问题而非追逐「AI」标签的工具</strong>。<br><small>来源：<a href="https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026">RGD</a> | <a href="https://medium.com/@shrey_uiux/5-ai-design-tools-that-are-still-worth-using-after-the-hype-2026-2809b0ce002a">Medium</a></small></li><li><strong>Figma Make 原型可嵌入 Figma Design、FigJam 和 Slides</strong> — Figma 宣布 Figma Make 原型现在可以嵌入到 Figma Design、FigJam 和 Figma Slides 中，同时推出新的编辑工具。这意味着 AI 生成的原型不再是一个孤立的输出，而是可以直接嵌入设计系统的各个环节。Figma 还发布了「约束下的烹饪」框架，教设计师如何写出结构化的 AI 提示词——<strong>把 AI 从猜谜游戏变成可靠的设计伙伴</strong>。此外，Figma Make 现已对政府团队开放（Figma for Government），加速公共服务现代化。<br><small>来源：<a href="https://www.figma.com/solutions/ai-design-generator/">Figma Make</a> | <a href="https://www.figma.com/resource-library/ai-design-tools/">Figma AI Tools</a></small></li><li><strong>Agentic 设计工作流：从单步生成到多步自主执行</strong> — ALM Corp 的深度分析指出，2026 年最值得关注的设计 AI 趋势是「Agentic 设计工作流」——多个 AI 工具可以自主完成从研究综合、方向提案、布局变体生成到最优方案筛选的全流程，设计师只需在关键节点做判断。Toools.design 对 9 款主流 AI UI/UX 工具的对比评测显示，Figma Make（$16/用户/月）、Motiff（支持 React/HTML 代码导出）和 Visily（截图/草图转设计）是三个差异化最清晰的选择。<br><small>来源：<a href="https://almcorp.com/blog/how-to-use-ai-for-graphic-design/">ALM Corp</a> | <a href="https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026">Toools.design</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「嵌入式 AI」取代「独立 AI 工具」</strong>：2026 年的赢家不是做新工具的，而是把 AI 嵌入现有工作流的</li><li><strong>设计师的 AI 素养要求升级</strong>：不只是会用工具，还要理解训练数据、许可和伦理</li><li><strong>Agentic 工作流是下一个前沿</strong>：从「AI 做一步」到「AI 做整条链」的范式转移正在发生</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>AI 设计工具领域正在经历一个安静但意义深远的转折：炒作退潮后，真正的整合期到了。</strong></p><p>回看过去两年，AI 设计工具经历了典型的 Gartner 炒作周期：2024 年是「万物皆可 AI」的膨胀期，每周都有新工具宣称要「革命性改变设计」；2025 年是幻灭期，大量工具因为不解决真实问题而被抛弃；现在，2026 年 Q1，我们进入了「生产力高原」——存活下来的工具都有一个共同特征：<strong>它们不试图成为独立的「AI 设计平台」，而是嵌入到设计师已经在用的工具里。</strong></p><p>RGD 的文章说得很到位：Adobe Firefly 的价值不在于它本身有多强，而在于它就在 Photoshop 和 Illustrator 里。Figma Make 的突破也不是生成能力（Midjourney 生成质量更高），而是<strong>生成的结果可以直接嵌入 Figma Design、FigJam 和 Slides</strong>。这是「嵌入式 AI」vs「独立 AI」的终局——就像当年 Spell Check 从独立软件变成 Word 的内置功能一样，AI 设计能力正在成为设计工具的「默认层」而非「附加层」。</p><p>但最让我兴奋的是「Agentic 设计工作流」的萌芽。目前大多数 AI 设计工具还是「单步式」的——你给一个提示词，它返回一个结果。ALM Corp 描述的 Agentic 工作流完全不同：AI 先做用户研究综合，再提出设计方向，然后生成多个布局变体，最后自动评估并推荐最优方案。设计师的角色从「操作者」变成了「审判者」。<strong>这不是假设——它在 2026 年已经初步可行了。</strong>把 Perplexity（研究） + Figma Make（生成） + UX Pilot（评估）串起来，你就有了一条初级的 Agentic 设计链。</p><p>这对设计师意味着什么？Medium 那篇「炒作后还值得用的 5 个工具」给了一个清醒的框架：不要追工具，追问题。你的瓶颈在灵感探索？试 Mixboard。在布局效率？试 Figma Make。在用户验证？试 UX Pilot 的预测热图。<strong>2026 年对设计师的要求不再是「会不会用 AI」，而是「能不能把 3-4 个 AI 工具编排成一条高效的个人工作流」。</strong>这是一种新的元技能——你可以叫它「AI 编排力」。RGD 提醒的伦理和许可审查也很关键：当你的设计流水线有 4 个 AI 工具时，任何一个的训练数据问题都可能成为法律风险。这种「供应链思维」以前只属于工程团队，现在设计师也需要了。</p></div>',
        "en": '<h3>📌 AI × Design</h3><ul><li><strong>AI Design Tools Enter Post-Hype Phase: Embedded Workflows Win</strong> — Canada\'s RGD published analysis showing 2026\'s AI design trend is embedding into existing workflows, not replacing designers. Adobe Firefly assists during exploration; Mixboard enters the moodboarding phase. Designers urged to review training data sources and licensing. Medium critique: only 5 AI design tools survived the hype cycle — those solving real problems.<br><small>Source: <a href="https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026">RGD</a> | <a href="https://medium.com/@shrey_uiux/5-ai-design-tools-that-are-still-worth-using-after-the-hype-2026-2809b0ce002a">Medium</a></small></li><li><strong>Figma Make Prototypes Now Embeddable Across Figma Ecosystem</strong> — Figma Make prototypes can now be embedded in Figma Design, FigJam, and Slides. New editing tools and a structured prompting framework ("Cooking with Constraints") turn AI from guesswork into a reliable design partner. Now available for government teams.<br><small>Source: <a href="https://www.figma.com/solutions/ai-design-generator/">Figma Make</a></small></li><li><strong>Agentic Design Workflows: From Single-Step to Multi-Step Autonomous Execution</strong> — ALM Corp analysis highlights agentic design workflows as 2026\'s most significant trend — AI tools autonomously completing research synthesis, direction proposals, layout variations, and optimal solution selection. Toools.design benchmarks 9 AI UI/UX tools, with Figma Make, Motiff, and Visily as standout differentiators.<br><small>Source: <a href="https://almcorp.com/blog/how-to-use-ai-for-graphic-design/">ALM Corp</a> | <a href="https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026">Toools.design</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Embedded AI replaces standalone AI tools as the winning strategy</li><li>Designer AI literacy now requires understanding training data and licensing</li><li>Agentic workflows: the paradigm shift from single-step to full-chain AI</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>AI design tools are experiencing a quiet but profound inflection: the hype has receded, and the real integration era begins.</strong> The surviving tools share one trait — they don\'t try to be standalone "AI design platforms" but embed into tools designers already use. Adobe Firefly\'s value isn\'t its generation quality but its presence inside Photoshop. Figma Make\'s breakthrough isn\'t generation (Midjourney is better) but that outputs embed directly into Figma Design, FigJam, and Slides. This is the "embedded AI" endgame — like spell-check becoming a built-in feature rather than standalone software. The most exciting development: agentic design workflows where AI chains research → direction → layout → evaluation autonomously. This isn\'t hypothetical — chain Perplexity + Figma Make + UX Pilot and you have a basic agentic design pipeline today. <strong>The 2026 designer meta-skill isn\'t "using AI" — it\'s orchestrating 3-4 AI tools into an efficient personal workflow.</strong></p></div>'
    },
    "cover": images.get("figma_make") or images.get("toools") or "https://cdn.sanity.io/images/599r6htc/regionalized/3759579b2338ef96d586780800a7ed2ad6bbe28f-1440x720.png?w=1200&q=70&fit=max&auto=format",
    "sources": [
        {
            "title": {"zh": "RGD: 2026 年用 AI 工具放大设计师创造力", "en": "RGD: Amplifying Creativity with AI Tools for Designers in 2026"},
            "url": "https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
            "image": images.get("rgd", "")
        },
        {
            "title": {"zh": "Medium: 炒作之后，2026 年还值得用的 5 个 AI 设计工具", "en": "Medium: 5 AI Design Tools Still Worth Using After the Hype"},
            "url": "https://medium.com/@shrey_uiux/5-ai-design-tools-that-are-still-worth-using-after-the-hype-2026-2809b0ce002a",
            "image": images.get("medium", "")
        },
        {
            "title": {"zh": "Figma Make: 你的 AI 设计工具", "en": "Figma Make: Your AI Design Tool"},
            "url": "https://www.figma.com/solutions/ai-design-generator/",
            "image": images.get("figma_make", "")
        },
        {
            "title": {"zh": "ALM Corp: 2026 年如何用 AI 做平面设计", "en": "ALM Corp: How to Use AI for Graphic Design in 2026"},
            "url": "https://almcorp.com/blog/how-to-use-ai-for-graphic-design/",
            "image": images.get("almcorp", "")
        },
        {
            "title": {"zh": "Toools.design: 2026 年 9 款最佳 AI UI/UX 工具深度评测", "en": "Toools.design: 9 Best AI Tools for UI/UX Designers in 2026"},
            "url": "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
            "image": images.get("toools", "")
        }
    ]
}

tech_issue = {
    "date": "2026-03-27",
    "section": "tech",
    "title": {
        "zh": "Meta 发布 4 款自研 AI 芯片挑战 NVIDIA 霸权 · Atlassian 裁员 1600 人「AI 转型」引争议 · 全球 AI 工具突破 16000 款进入基础设施时代",
        "en": "Meta Unveils 4 Custom AI Chips Challenging NVIDIA · Atlassian Cuts 1,600 Jobs in Controversial 'AI Pivot' · Global AI Tools Surpass 16,000 Entering Infrastructure Era"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul><li><strong>Meta 发布 4 款自研 AI 芯片，每 6 个月迭代一次</strong> — Meta 公布了 MTIA 系列四款自研 AI 芯片（300、400、450、500），由台积电代工。MTIA 300 已部署用于训练小型排名和推荐模型，MTIA 400 优化推理任务（单机架 72 颗），450 和 500 预计 2027 年上线。Meta 工程副总裁 Yee Jiun Song 对 CNBC 表示，自研芯片让 Meta 在硅供应上拥有更多多样性，降低对单一供应商的价格依赖。The Register 报道称，MTIA 400 是 Meta 首款「原始性能与市场领先商用产品竞争力相当」的芯片，采用双计算芯粒架构。<strong>Meta 宣布将保持每 6 个月发布新芯片的节奏</strong>，这直接挑战了 NVIDIA 的迭代周期。Motley Fool 分析指出，随着 AI 从训练转向推理，NVIDIA 的护城河可能收窄——推理任务可以在多种芯片上运行，包括大客户自研的定制芯片。<br><small>来源：<a href="https://www.cnbc.com/2026/03/11/meta-ai-mtia-chip-data-center.html">CNBC</a> | <a href="https://www.theregister.com/2026/03/12/meta_custom_chips/">The Register</a> | <a href="https://www.fool.com/investing/2026/03/15/should-nvidia-be-worried-meta-platforms-ai-chips/">Motley Fool</a></small></li><li><strong>Atlassian 裁员 1600 人（10%），「AI 转型」叙事引发强烈争议</strong> — Atlassian CEO Mike Cannon-Brookes 宣布裁员 10%（约 1600 人），称这是向「AI 时代」转型的一部分。CTO Rajeev Rajan 同时下台，由被称为「下一代 AI 人才」的 Taroon Mandhana 和 Vikram Rao 接任。但 Business Insider 发文质疑：裁员公告越来越像 AI 策略发布会——Block 的 Jack Dorsey 裁员 40% 时同样用了「AI 重塑」的说法。Metaintro 的分析更为尖锐：Cannon-Brookes 几个月前还在表达不同立场，批评者认为裁员更多是投资者压力和成本削减驱动，而非真正的 AI 生产力提升。<strong>Professionals Australia 工会已要求紧急会议讨论 AI 技术引入与裁员的直接关联。</strong><br><small>来源：<a href="https://www.theguardian.com/technology/2026/mar/12/atlassian-layoffs-software-technology-ai-push-mike-cannon-brookes-asx">The Guardian</a> | <a href="https://www.reuters.com/technology/atlassian-lay-off-about-1600-people-pivot-ai-2026-03-11/">Reuters</a> | <a href="https://www.businessinsider.com/layoff-ai-strategy-atlassian-block-2026-3">Business Insider</a></small></li><li><strong>全球 AI 工具突破 16000 款，进入基础设施时代</strong> — EINPresswire 报道，全球 AI 工具已超过 16000 款（分析师估计含私有系统超 50000 款）。英国 AWS 数据显示每 60 秒就有一家新公司采用 AI。AI 正从「实验期」全面进入「基础设施期」——企业不再问「要不要用 AI」，而是「用哪些 AI、怎么编排」。<br><small>来源：<a href="https://www.caller.com/press-release/story/100307/ai-tool-launches-hit-record-pace-as-industry-moves-from-experimentation-to-infrastructure/">EINPresswire</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 芯片从「NVIDIA 独占」到「多元供应」</strong>：Meta 自研芯片 + 推理需求转移，NVIDIA 的垄断地位首次面临结构性挑战</li><li><strong>「AI 转型」成为裁员的万能叙事</strong>：从 Atlassian 到 Block，「AI」正在成为企业重组的公关话术</li><li><strong>AI 从实验到基础设施</strong>：16000+ 工具意味着「选择」和「编排」比「是否使用」更重要</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>这周的三条新闻看起来互不相关，但它们指向同一个主题：AI 正在从「附加项」变成「默认基础设施」，而这个过程比大多数人想象的更痛苦、更复杂。</strong></p><p>先说 Meta 的芯片。表面上看，这是又一家大厂做自研芯片的故事。但细看数字会发现不一样：Meta 宣布每 6 个月迭代一款新芯片，这比 NVIDIA 的 18-24 个月周期快 3-4 倍。MTIA 400 单机架 72 颗、双计算芯粒架构、「原始性能与商用领先产品竞争力相当」——这不是玩票，这是认真要在推理市场上抢地盘。为什么？因为 AI 正在从训练（training）密集转向推理（inference）密集。训练需要最顶级的 GPU，NVIDIA 的护城河很深；但推理可以在各种芯片上跑，包括定制的 ASIC。<strong>Meta 每天处理数十亿次推理请求（排名、推荐、内容生成），哪怕每次推理省 0.1 美分，年化节省都是数十亿美元。</strong>这就是为什么 Yee Jiun Song 说的「硅供应多样性」不是空话——它是 Meta 的成本生命线。</p><p>再看 Atlassian 的裁员，这件事比芯片竞争更值得设计师和产品经理关注。Business Insider 的标题一针见血：「裁员还是 AI 转型？现在已经分不清了。」Cannon-Brookes 几个月前还在强调 Atlassian 不会因 AI 裁员，现在裁 1600 人并换掉 CTO，接任者被定义为「下一代 AI 人才」。<strong>这不是个案——Block 裁 40%、WiseTech 裁员，都用了同样的「AI 重塑」叙事。</strong>我们正在见证一个新的企业话术范式：「AI 转型」已经成为裁员的万能合理化工具，就像 2008 年的「金融危机」和 2020 年的「疫情影响」一样。</p><p>但 Atlassian 的案例有一个更深层的信号。当一家以协作工具闻名的公司（Jira、Confluence、Trello）说「AI 改变了我们需要的技能组合」时，它其实在说：<strong>AI 正在重塑软件行业本身的劳动力结构。</strong>不是某些岗位被 AI 取代，而是整个组织的「技能密度」在重新配置。需要更多能训练和编排 AI 的人，更少做 AI 可以自动化的重复性工作的人。Professionals Australia 工会要求讨论「AI 引入与裁员的直接关联」，这在全球范围内可能是第一次有组织地挑战这个叙事——如果这成为判例，它将影响每一家用「AI 转型」裁员的公司。</p><p>把这些和昨天的新闻连起来：NVIDIA NemoClaw 做 Agent 基础设施、Gumloop 让非技术人员构建 Agent、Meta 自研芯片降低推理成本、全球 AI 工具突破 16000 款。<strong>2026 年 Q1 的元叙事已经非常清晰：AI 不再是「附加功能」或「实验项目」，它正在成为企业运营的默认基础设施——像电力和互联网一样不可见但无处不在。</strong>而这个转变的社会代价也在显现：Atlassian 的 1600 人只是开始。当 AI 基础设施足够成熟（16000+ 工具、定制芯片、无代码 Agent），「AI 改变了我们需要的技能组合」将成为未来 2 年企业重组的标准用语。<strong>我的建议：与其争论「AI 会不会取代你」，不如看看你的技能在 AI 基础设施化后还有多少不可替代性。</strong></p></div>',
        "en": '<h3>📌 AI × Tech</h3><ul><li><strong>Meta Unveils 4 Custom AI Chips, Promises New Chip Every 6 Months</strong> — Meta revealed MTIA series chips (300, 400, 450, 500), manufactured by TSMC. MTIA 300 deployed for training ranking/recommendation models; MTIA 400 (72 per rack) optimized for inference. VP Yee Jiun Song says custom chips provide silicon supply diversity. The Register reports MTIA 400 is Meta\'s first chip with "raw performance competitive with leading commercial products." Meta plans a new chip every 6 months — 3-4x faster than NVIDIA\'s cycle.<br><small>Source: <a href="https://www.cnbc.com/2026/03/11/meta-ai-mtia-chip-data-center.html">CNBC</a> | <a href="https://www.theregister.com/2026/03/12/meta_custom_chips/">The Register</a></small></li><li><strong>Atlassian Cuts 1,600 Jobs (10%) in Controversial "AI Pivot"</strong> — CEO Cannon-Brookes frames layoffs as AI-era restructuring; CTO replaced by "next-gen AI talent." Business Insider: "Layoffs or AI pivot? Hard to tell the difference now." Professionals Australia union demands urgent meeting on AI-layoff linkage. Critics note CEO\'s contradictory earlier statements.<br><small>Source: <a href="https://www.theguardian.com/technology/2026/mar/12/atlassian-layoffs-software-technology-ai-push-mike-cannon-brookes-asx">The Guardian</a> | <a href="https://www.reuters.com/technology/atlassian-lay-off-about-1600-people-pivot-ai-2026-03-11/">Reuters</a> | <a href="https://www.businessinsider.com/layoff-ai-strategy-atlassian-block-2026-3">Business Insider</a></small></li><li><strong>Global AI Tools Surpass 16,000, Entering Infrastructure Era</strong> — Industry trackers list 16,000+ AI products (estimated 50,000+ including private systems). In the UK, one new company adopts AI every 60 seconds. The shift from experimentation to infrastructure is complete.<br><small>Source: <a href="https://www.caller.com/press-release/story/100307/ai-tool-launches-hit-record-pace-as-industry-moves-from-experimentation-to-infrastructure/">EINPresswire</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI chips: from NVIDIA monopoly to multi-source supply (Meta\'s 6-month cycle)</li><li>"AI pivot" becoming the universal layoff narrative (Atlassian, Block, WiseTech)</li><li>AI moving from experiment to default infrastructure (16,000+ tools)</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Three seemingly unrelated stories point to one theme: AI is becoming default infrastructure, and the transition is more painful than expected.</strong> Meta\'s 6-month chip cycle (3-4x faster than NVIDIA\'s) targets inference — where billions of daily requests make even 0.1¢ savings worth billions annually. This is structural pressure on NVIDIA\'s moat. Atlassian\'s layoffs matter more than they seem: when a collaboration-tool company says "AI changed our skill mix," it signals the entire software industry\'s workforce is being reconfigured. Business Insider nailed it — "AI pivot" is becoming 2026\'s universal layoff justification, like "pandemic impact" was in 2020. The Australian union\'s challenge could set global precedent. Connecting everything: NemoClaw for agent infrastructure + Meta chips for cheap inference + 16,000 tools = AI becoming invisible default infrastructure like electricity. <strong>The social cost: Atlassian\'s 1,600 is just the beginning. In 2 years, "AI changed our skill mix" will be the standard corporate restructuring phrase.</strong></p></div>'
    },
    "cover": images.get("meta_cnbc") or images.get("meta_register") or "",
    "sources": [
        {
            "title": {"zh": "CNBC: Meta 发布自研 AI 芯片 MTIA", "en": "CNBC: Meta Reveals Custom AI Chips"},
            "url": "https://www.cnbc.com/2026/03/11/meta-ai-mtia-chip-data-center.html",
            "image": images.get("meta_cnbc", "")
        },
        {
            "title": {"zh": "The Register: Meta 自研芯片性能对标 NVIDIA", "en": "The Register: Meta Custom Chips Claim to Beat Nvidia"},
            "url": "https://www.theregister.com/2026/03/12/meta_custom_chips/",
            "image": images.get("meta_register", "")
        },
        {
            "title": {"zh": "The Guardian: Atlassian 裁员 1600 人推动 AI 转型", "en": "The Guardian: Atlassian Lays Off 1,600 for AI Push"},
            "url": "https://www.theguardian.com/technology/2026/mar/12/atlassian-layoffs-software-technology-ai-push-mike-cannon-brookes-asx",
            "image": images.get("atlassian_guardian", "")
        },
        {
            "title": {"zh": "Business Insider: 裁员还是 AI 转型？已经分不清了", "en": "Business Insider: Layoffs or AI Pivot? Hard to Tell"},
            "url": "https://www.businessinsider.com/layoff-ai-strategy-atlassian-block-2026-3",
            "image": images.get("atlassian_bi", "")
        },
        {
            "title": {"zh": "EINPresswire: AI 工具发布速度创纪录", "en": "EINPresswire: AI Tool Launches Hit Record Pace"},
            "url": "https://www.caller.com/press-release/story/100307/ai-tool-launches-hit-record-pace-as-industry-moves-from-experimentation-to-infrastructure/",
            "image": images.get("ai_tools_record", "")
        }
    ]
}

# Insert new issues at the beginning
issues.insert(0, design_issue)
issues.insert(1, tech_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("✅ issues.json updated with 2 new entries for 2026-03-27")
