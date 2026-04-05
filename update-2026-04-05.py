# -*- coding: utf-8 -*-
"""Rex Daily Digest - 2026-04-05"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        resp = urllib.request.urlopen(req, timeout=10)
        data = resp.read(100000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', data, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data, re.I)
        return html.unescape(m.group(1)) if m else ""
    except:
        return ""

# Fetch og:images
urls = {
    "figma_agents": "https://muz.li/blog/figma-just-opened-the-canvas-to-ai-agents-heres-what-it-means-for-designers/",
    "vibe_coding": "https://www.toools.design/blog-posts/vibe-coding-tools-for-designers",
    "figma_ai_medium": "https://medium.com/@Rythmuxdesigner/figma-ai-is-here-how-its-changing-ui-design-workflows-in-2026-9afb8085dfb3",
    "openai_shuffle": "https://techcrunch.com/2026/04/03/openai-executive-shuffle-new-roles-coo-brad-lightcap-fidji-simo-kate-rouch/",
    "deepseek_v4": "https://www.asiaone.com/digital/deepseeks-v4-model-will-run-huawei-chips-information-reports",
    "apple_google": "https://fortune.com/2026/01/13/apple-ai-deal-with-google-gemini-means-for-google-apple-openai/",
}

print("Fetching og:images...")
images = {}
for k, u in urls.items():
    img = get_og_image(u)
    images[k] = img
    print(f"  {k}: {img[:80] if img else '(none)'}")

design_issue = {
    "date": "2026-04-05",
    "section": "design",
    "title": {
        "zh": "Figma 向 AI Agent 开放画布：设计师的协作对象从人变成了 AI · Vibe Coding 工具 2026 年度盘点：设计师不再需要「交付设计稿」· AI 正在重写设计工作流的每一层",
        "en": "Figma Opens Its Canvas to AI Agents: Designers Now Collaborate with AI · 2026's Best Vibe Coding Tools for Designers · AI Is Rewriting Every Layer of the Design Workflow"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul><li><strong>Figma 向 AI Agent 全面开放画布——Agent 现在可以直接在 Figma 里创建、编辑组件和应用变量</strong> — Figma 宣布 AI Agent 现在可以通过其 MCP Server 和 "use_figma" 工具<strong>直接在 Figma 画布上操作</strong>——不只是读取文件，而是真正地创建组件、编辑设计、应用 Design System 变量。这意味着 Figma 正在从「设计师的画布」变成「设计师 + AI Agent 的共享工作空间」。Muzli 的分析指出：<strong>那些深入理解成熟 Design System 长什么样的设计师，将最有能力指挥 Agent 产出高质量设计。</strong>画布不再是「交付物」，而是一个「活的协作空间」——Agent 和设计师在里面一起工作。<br><small>来源：<a href="https://muz.li/blog/figma-just-opened-the-canvas-to-ai-agents-heres-what-it-means-for-designers/">Muzli Blog</a></small></li><li><strong>2026 年 Vibe Coding 工具年度盘点：设计师直接生产软件的 10 种方式</strong> — Toools.design 发布了 2026 年最佳 Vibe Coding 工具盘点。核心发现：<strong>设计师正在跳过「设计稿 → 开发还原」的传统流程</strong>，直接用 Lovable、Bolt、Cursor、Figma Make 等工具生产可运行的应用。关键趋势：Figma Make 支持在「视觉设计模式」和「代码生成模式」之间切换；Cursor 成为设计师从原型到生产代码的桥梁；Y Combinator 投资的平台用 AI Agent 逐步推理需求并系统构建，而不是单次 prompt 生成。<strong>Rork 是唯一直接生成 React Native 原生代码的工具，面向 iOS 和 Android。</strong><br><small>来源：<a href="https://www.toools.design/blog-posts/vibe-coding-tools-for-designers">Toools.design</a></small></li><li><strong>Figma AI 如何改变 2026 年的 UI 设计工作流</strong> — Medium 上的深度文章分析了 Figma AI 的 First Draft 功能如何学习你的 Design System、品牌规范甚至历史项目，生成不需要从零开始的布局起点。两个关键数据：<strong>Figma 1300 万月活用户中，三分之二不是设计师</strong>——这说明工具的使用者正在扩大；免费版每月仅 3 次 AI 生成（「几乎不可用」），付费版 $32/月/用户。Figma 正在变成一个<strong>非设计师也能「设计」的平台</strong>。<br><small>来源：<a href="https://medium.com/@Rythmuxdesigner/figma-ai-is-here-how-its-changing-ui-design-workflows-in-2026-9afb8085dfb3">Medium</a>、<a href="https://www.buildmvpfast.com/blog/ux-design-ai-tools-for-designers-2026">BuildMVPFast</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>画布 → 共享工作空间</strong>：Figma 从「设计师的工具」变成「人 + Agent 的协作平台」</li><li><strong>设计稿的消亡</strong>：Vibe Coding 让设计师直接产出可运行软件，跳过中间产物</li><li><strong>设计民主化加速</strong>：Figma 2/3 用户不是设计师——AI 让「人人都能设计」从口号变成现实</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Figma 向 AI Agent 开放画布这件事，表面上是一个技术更新——MCP Server、use_figma 工具、Agent 可以操作组件——但它的深层含义是：设计工具的「用户」定义正在根本性地改变。</strong></p><p>过去十年，设计工具的进化是围绕「人类设计师」展开的：更好的协作（Figma 的多人编辑）、更快的原型（Framer）、更丰富的组件（Design System）。但 Agent 进入画布后，Figma 的「用户」不再只是有眼睛和双手的人类——还包括通过 API 调用来创建和修改设计的 AI 程序。这是一个范式转移：<strong>设计工具从「为人类设计的界面」变成了「人类和 AI 共同操作的基础设施」。</strong></p><p>Muzli 的分析里有一句特别精准的话：「理解成熟 Design System 的设计师将最有能力指挥 Agent。」这就是我一直在说的——<strong>AI 时代设计师的核心技能不是画 UI，而是定义标准。</strong>你的 Design System 有多清晰、多完整、多一致，直接决定了 Agent 的输出质量。这和上期我们讨论的 Malewicz 观点形成了完美的延续：人类手动维护的 Design System 在消亡（太慢），但 Design System 作为「给 AI 的指令集」反而变得更重要了。</p><p>再看 Vibe Coding 工具的爆发。Toools.design 盘点的 10 个工具里，至少 6 个是在过去 12 个月内出现或大幅更新的。最有趣的不是单个工具，而是一条清晰的<strong>设计师「脱媒」路径</strong>：用 Lovable/Bolt 生成原型 → 导出到 Cursor 继续开发 → 直接部署。整个流程里，传统意义上的「前端开发」角色被完全绕过了。这对设计行业意味着什么？<strong>设计师正在分化为两类：一类是掌握 AI + 代码工具、能独立交付产品的「全栈设计师」；另一类是只会在 Figma 里画稿、等着被 Agent 取代的「像素工匠」。</strong></p><p>最让我警觉的数据是 Figma 的用户构成：1300 万月活中三分之二不是设计师。这不是「设计民主化」的胜利——这是<strong>设计专业壁垒崩塌</strong>的信号。当产品经理、工程师、甚至创始人都能用 Figma + AI 直接「设计」出足够好的界面时，专职 UI 设计师的议价能力会显著下降。但反过来看，那些能做到 AI 做不到的事情——用户研究洞察、信息架构设计、品牌叙事、情感化设计——的设计师，在一个人人都能画 UI 的世界里反而更稀缺。</p><p><strong>我的判断：Figma 开放 Agent 画布 + Vibe Coding 工具成熟 = 2026 下半年我们将看到第一批「零设计师」的成功产品——由创始人或 PM 用 AI 直接设计和构建。这会震动整个设计行业，但最终结果不是设计师消失，而是「设计师」的定义被重写。未来的设计师不是「会用 Figma 的人」，而是「懂得什么样的产品体验是好的、并能指挥 AI 实现它的人」。工具能力在贬值，判断力在升值。这是 AI 时代所有创意职业的共同命运。</strong></p></div>',
        "en": '<h3>📌 AI × Design</h3><ul><li><strong>Figma Opens Canvas to AI Agents—Agents Can Now Create, Edit Components and Apply Variables Directly</strong> — Figma announced AI agents can now operate directly on the canvas via MCP Server and "use_figma" tool—not just reading files but creating components, editing designs, and applying design system variables. <strong>Designers who deeply understand mature design systems will be best positioned to direct agent output.</strong> The canvas is no longer a deliverable but a live collaborative artifact.<br><small>Source: <a href="https://muz.li/blog/figma-just-opened-the-canvas-to-ai-agents-heres-what-it-means-for-designers/">Muzli Blog</a></small></li><li><strong>2026 Vibe Coding Tools Roundup: 10 Ways Designers Ship Software Directly</strong> — Toools.design published a comprehensive roundup. Key finding: designers are skipping the "mockup → developer handoff" flow entirely. Figma Make bridges visual design and code generation; Cursor bridges prototype to production; YC-backed platforms use AI agents for systematic requirements reasoning. <strong>Rork is the only tool generating native React Native code for iOS/Android.</strong><br><small>Source: <a href="https://www.toools.design/blog-posts/vibe-coding-tools-for-designers">Toools.design</a></small></li><li><strong>How Figma AI Is Changing UI Design Workflows in 2026</strong> — Figma AI\'s First Draft learns your design system, brand guidelines, and past projects to generate starter layouts. Key data: <strong>two-thirds of Figma\'s 13M MAU are non-designers</strong>—the tool\'s user base is expanding beyond design. Free tier: 3 AI generations/month ("borderline unusable"); paid: $32/month/user.<br><small>Source: <a href="https://medium.com/@Rythmuxdesigner/figma-ai-is-here-how-its-changing-ui-design-workflows-in-2026-9afb8085dfb3">Medium</a>, <a href="https://www.buildmvpfast.com/blog/ux-design-ai-tools-for-designers-2026">BuildMVPFast</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Canvas → Shared workspace: Figma transforms from "designer\'s tool" to "human + agent collaboration platform"</li><li>Death of the mockup: vibe coding lets designers ship running software, skipping intermediate artifacts</li><li>Design democratization accelerates: 2/3 of Figma users aren\'t designers—AI makes "everyone can design" real</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Figma opening its canvas to AI agents appears to be a technical update—MCP Server, use_figma tool, agents operating on components—but the deeper meaning is that the definition of "user" in design tools is fundamentally changing.</strong> For the past decade, design tools evolved around human designers: better collaboration, faster prototyping, richer components. With agents on the canvas, Figma\'s "user" now includes AI programs that create and modify designs via API. This is a paradigm shift: design tools transform from "interfaces designed for humans" to "infrastructure operated by both humans and AI." Muzli nailed it: "designers who understand mature design systems will best direct agents." The core skill isn\'t drawing UI—it\'s defining standards. Your design system\'s clarity directly determines agent output quality. This perfectly extends last issue\'s Malewicz discussion: manually maintained design systems are dying (too slow), but design systems as "instruction sets for AI" are more important than ever. The vibe coding explosion is equally telling—at least 6 of Toools.design\'s 10 tools appeared or majorly updated in the past 12 months. The clear "disintermediation" path: Lovable/Bolt for prototype → Cursor for development → direct deployment, completely bypassing traditional frontend development. <strong>My prediction: Figma\'s agent canvas + mature vibe coding = H2 2026 will see the first successful "zero-designer" products built entirely by founders/PMs with AI. This will shake the design industry, but the outcome won\'t be designers disappearing—it\'ll be "designer" being redefined. Future designers won\'t be "people who use Figma" but "people who know what good product experience looks like and can direct AI to build it." Tool proficiency is depreciating; judgment is appreciating. This is the shared fate of all creative professions in the AI era.</strong></p></div>'
    },
    "cover": images.get("figma_agents", ""),
    "sources": [
        {
            "title": {"zh": "Figma 向 AI Agent 开放画布", "en": "Figma Opens the Canvas to AI Agents"},
            "url": "https://muz.li/blog/figma-just-opened-the-canvas-to-ai-agents-heres-what-it-means-for-designers/",
            "image": images.get("figma_agents", "")
        },
        {
            "title": {"zh": "2026 年设计师最佳 Vibe Coding 工具", "en": "10 Best Vibe Coding Tools for Designers in 2026"},
            "url": "https://www.toools.design/blog-posts/vibe-coding-tools-for-designers",
            "image": images.get("vibe_coding", "")
        },
        {
            "title": {"zh": "Figma AI 如何改变 2026 年 UI 设计工作流", "en": "Figma AI Is Here: How It's Changing UI Design Workflows in 2026"},
            "url": "https://medium.com/@Rythmuxdesigner/figma-ai-is-here-how-its-changing-ui-design-workflows-in-2026-9afb8085dfb3",
            "image": images.get("figma_ai_medium", "")
        }
    ]
}

tech_issue = {
    "date": "2026-04-05",
    "section": "tech",
    "title": {
        "zh": "OpenAI IPO 前夜高管大洗牌：COO 转岗「特别项目」，CEO AGI 负责人因病休假 · DeepSeek V4 将运行在华为芯片上：中国 AI 生态加速「去美化」· Anthropic Claude Mythos 泄露事件持续发酵",
        "en": "OpenAI Executive Shuffle Before IPO: COO Moves to 'Special Projects', AGI CEO on Medical Leave · DeepSeek V4 to Run on Huawei Chips: China's AI Ecosystem Accelerates De-Americanization · Anthropic's Claude Mythos Leak Continues to Reverberate"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul><li><strong>OpenAI IPO 前夜大洗牌：COO Brad Lightcap 转岗「特别项目」，CMO 因癌症治疗离职，AGI 负责人 Fidji Simo 因神经免疫疾病休假</strong> — TechCrunch 和 Business Insider 报道，OpenAI 正经历新一轮高管震荡。长期担任 COO 的 Brad Lightcap 将转任「特别项目」，直接向 Sam Altman 汇报；CMO Kate Rouch 因癌症治疗离开公司；AGI 开发负责人 Fidji Simo 因神经免疫疾病休假数周，期间由联合创始人 Greg Brockman 接管产品线。<strong>这一切发生在 OpenAI 以 8520 亿美元估值完成 1220 亿美元融资、正在筹备 IPO 之际。</strong>对于一家即将上市的公司来说，三位 C-suite 高管同时变动绝非常态。<br><small>来源：<a href="https://techcrunch.com/2026/04/03/openai-executive-shuffle-new-roles-coo-brad-lightcap-fidji-simo-kate-rouch/">TechCrunch</a>、<a href="https://www.businessinsider.com/openai-executive-shake-up-coo-cmo-2026-4">Business Insider</a></small></li><li><strong>DeepSeek V4 将运行在华为芯片上：阿里、字节、腾讯已下单数十万片华为新芯片</strong> — 据 The Information 报道，DeepSeek 的下一代模型 V4 将运行在华为最新芯片上，而非 Nvidia GPU。更关键的是：<strong>阿里巴巴、字节跳动和腾讯已经为华为即将推出的芯片下了数十万片的批量订单。</strong>DeepSeek 过去几个月一直与华为和寒武纪科技合作，重写模型底层代码以适配国产芯片。DeepSeek 还在开发两个 V4 变体，分别针对不同能力优化，全部基于国产芯片。<strong>这标志着中国 AI 生态系统「去美化」进入了一个新阶段——不是被动应对制裁，而是主动构建替代方案。</strong><br><small>来源：<a href="https://www.asiaone.com/digital/deepseeks-v4-model-will-run-huawei-chips-information-reports">AsiaOne/Reuters</a></small></li><li><strong>Anthropic Claude Mythos 泄露事件持续发酵：「有史以来最强大的 AI 模型」意外曝光</strong> — Fortune 独家报道：Anthropic 将一份包含未发布模型信息的草稿博客文章存放在了<strong>未加密的公开数据湖中</strong>，被安全研究人员发现。泄露文件显示 Claude Mythos 被内部描述为「我们有史以来开发的最强大的 AI 模型」。Manifold Markets 上的预测市场显示，社区对 Mythos 是否会在 4 月 13 日前官方公布的概率仅为 17%，但对 7 月 1 日前发布的预期正在上升。<strong>这次泄露的尴尬之处在于：Anthropic 一直以「安全优先」自居，却连自家的敏感文件都没保护好。</strong><br><small>来源：<a href="https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/">Fortune</a>、<a href="https://www.techzine.eu/news/applications/140017/details-leak-on-anthropics-step-change-mythos-model/">Techzine</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>OpenAI 的组织风险</strong>：8520 亿美元估值 + 三位 C-suite 同时变动 = IPO 前的不确定性信号</li><li><strong>中国 AI 供应链自主化</strong>：DeepSeek V4 + 华为芯片 + BAT 批量采购 = 国产 AI 全栈正在成型</li><li><strong>AI 安全的讽刺</strong>：Anthropic 的安全叙事与数据泄露现实之间的落差</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>今天的三条科技新闻放在一起，讲的是同一个故事：AI 行业正在从「谁的模型最强」进入「谁的组织最稳、谁的生态最完整」的竞争阶段。</strong></p><p>先说 OpenAI。三位 C-suite 高管同时变动——COO 转岗、CMO 因病离职、AGI CEO 因病休假——对于任何公司都是大事，更不用说一家估值 8520 亿、正在筹备 IPO 的公司。当然，其中两位是健康原因，不能简单解读为「内部动荡」。但 Brad Lightcap 从 COO 转到「特别项目」就值得玩味了。在硅谷，「特别项目」通常是「体面离开」的前奏曲。Lightcap 是 OpenAI 最早期的员工之一，他的 COO 角色对公司运营至关重要。在 IPO 前把运营负责人挪走，要么说明 Altman 想换一种管理风格迎接上市后的公众公司治理，要么说明内部对运营方向有分歧。<strong>无论哪种解读，对投资者来说都不是好消息。</strong></p><p>DeepSeek V4 转向华为芯片是本周最重要的地缘科技新闻。过去两年，美国对华芯片禁令的逻辑是：掐住 Nvidia GPU 供应，就能限制中国的 AI 发展。DeepSeek V3 和 R1 已经证明这个逻辑有漏洞——它们用有限的 Nvidia 旧卡就训出了有竞争力的模型。现在 V4 直接跳到华为芯片，而且不是小规模实验——<strong>阿里、字节、腾讯的「数十万片」采购订单说明这是产业级别的转向。</strong>DeepSeek 和华为、寒武纪一起重写底层代码这件事更有意义：这不是简单的「换个 GPU」，而是在构建一整套从芯片到模型的中国 AI 技术栈。芯片禁令的长期效果可能不是阻止中国 AI 发展，而是加速了一个完全独立于美国供应链的 AI 生态的诞生。</p><p>Anthropic 的泄露事件则是一个绝妙的讽刺。这家公司的整个品牌叙事建立在「我们是最重视 AI 安全的公司」之上——Constitutional AI、安全培训、红队测试……然后他们把未发布模型的详细信息放在了<strong>未加密的公开数据湖</strong>里。这不是被黑客攻破，不是内部人员泄密——是最基本的安全卫生没做好。这让人不禁想问：<strong>如果 Anthropic 连自家最敏感的商业机密都保护不好，我们凭什么相信他们能确保 AI 安全？</strong>当然，信息安全和 AI 安全是两码事，但品牌叙事讲的就是「我们比别人更谨慎」——一个把草稿博客放在公开存储桶里的公司，很难让人买账。</p><p><strong>把这三条新闻和今天的设计新闻连起来看：OpenAI 的组织动荡、Anthropic 的安全尴尬、DeepSeek 的芯片独立——头部 AI 公司各有各的问题。但 AI 工具层面的渗透（Figma Agent、Vibe Coding）却在加速。这说明 AI 的真正影响力已经不完全取决于模型公司的内部状态了——工具生态已经形成了自己的动量。即使 OpenAI 明天 IPO 失败，设计师照样会用 Cursor 写代码、用 Figma Make 出原型。AI 已经从「大公司的实验室产品」变成了「嵌入每个人工作流的基础设施」。这才是 2026 年最重要的变化。</strong></p></div>',
        "en": '<h3>📌 AI × Tech</h3><ul><li><strong>OpenAI Executive Shuffle Before IPO: COO Brad Lightcap to "Special Projects," CMO Exits for Cancer Treatment, AGI CEO on Medical Leave</strong> — Per TechCrunch and Business Insider, OpenAI is experiencing another leadership shake-up. Long-serving COO Brad Lightcap moves to "special projects" reporting to Altman; CMO Kate Rouch exits for cancer treatment; AGI CEO Fidji Simo takes medical leave for a neuroimmune condition, with Greg Brockman covering. <strong>All happening as OpenAI prepares for IPO at $852B valuation after raising $122B.</strong> Three C-suite changes simultaneously is far from normal for a pre-IPO company.<br><small>Source: <a href="https://techcrunch.com/2026/04/03/openai-executive-shuffle-new-roles-coo-brad-lightcap-fidji-simo-kate-rouch/">TechCrunch</a>, <a href="https://www.businessinsider.com/openai-executive-shake-up-coo-cmo-2026-4">Business Insider</a></small></li><li><strong>DeepSeek V4 to Run on Huawei Chips: Alibaba, ByteDance, Tencent Order Hundreds of Thousands of Units</strong> — Per The Information/Reuters, DeepSeek\'s V4 will run on Huawei\'s latest chips, not Nvidia GPUs. Chinese tech giants have placed bulk orders for hundreds of thousands of Huawei\'s upcoming chips. DeepSeek has been rewriting model code with Huawei and Cambricon Technologies for months. <strong>Two additional V4 variants optimized for different capabilities, all on Chinese chips.</strong> This marks China\'s AI ecosystem actively building alternatives rather than passively coping with sanctions.<br><small>Source: <a href="https://www.asiaone.com/digital/deepseeks-v4-model-will-run-huawei-chips-information-reports">AsiaOne/Reuters</a></small></li><li><strong>Anthropic Claude Mythos Leak Continues: "Most Powerful AI Model Ever" Accidentally Exposed</strong> — Fortune exclusive: Anthropic stored draft blog post announcing Claude Mythos in an unsecured public data lake. The document describes Mythos as "by far the most powerful AI model we\'ve ever developed." Manifold Markets shows 17% probability of announcement before April 13, but rising expectations for pre-July release. <strong>The irony: Anthropic positions itself as "safety-first" but couldn\'t protect its own sensitive files.</strong><br><small>Source: <a href="https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/">Fortune</a>, <a href="https://www.techzine.eu/news/applications/140017/details-leak-on-anthropics-step-change-mythos-model/">Techzine</a></small></li></ul><h3>🔄 Trends</h3><ul><li>OpenAI organizational risk: $852B valuation + three C-suite changes = pre-IPO uncertainty signal</li><li>China AI supply chain independence: DeepSeek V4 + Huawei chips + BAT bulk orders = domestic full-stack AI taking shape</li><li>AI safety irony: gap between Anthropic\'s safety narrative and data leak reality</li></ul><div class="rex-take"><h3>🔍 Rex\'s Take</h3><p><strong>Today\'s three tech stories tell the same narrative: AI competition is shifting from "who has the strongest model" to "who has the most stable organization and complete ecosystem."</strong> OpenAI\'s triple C-suite shift—two health-related, one strategic—raises questions ahead of IPO. Lightcap\'s move to "special projects" is classic Silicon Valley code for a graceful exit. Whether Altman is reshaping management for public company governance or internal strategy disagreements exist, neither reading reassures investors. DeepSeek V4\'s pivot to Huawei chips is this week\'s most important geopolitical tech story. The US chip ban logic—cut Nvidia supply to limit Chinese AI—is being actively circumvented at industrial scale. BAT\'s "hundreds of thousands" chip orders prove this isn\'t an experiment; it\'s an ecosystem shift. DeepSeek rewriting code with Huawei and Cambricon is building a complete Chinese AI stack from chip to model. The long-term effect of chip bans may not be slowing Chinese AI but accelerating a fully independent AI ecosystem. Anthropic\'s leak is a perfect irony: a company whose entire brand is "we take AI safety most seriously" stored unreleased model details in an unsecured public data lake. Not hacked, not insider leaked—basic security hygiene failure. <strong>Connecting today\'s design and tech stories: despite organizational turbulence at model companies (OpenAI, Anthropic) and geopolitical fragmentation (DeepSeek), AI tool adoption (Figma agents, vibe coding) accelerates independently. The tool ecosystem has its own momentum. Even if OpenAI\'s IPO fails tomorrow, designers will still use Cursor and Figma Make. AI has transformed from "lab product of big companies" to "infrastructure embedded in everyone\'s workflow." That\'s 2026\'s most important change.</strong></p></div>'
    },
    "cover": images.get("openai_shuffle", ""),
    "sources": [
        {
            "title": {"zh": "OpenAI 高管大洗牌", "en": "OpenAI Executive Shuffle: COO Brad Lightcap to Lead 'Special Projects'"},
            "url": "https://techcrunch.com/2026/04/03/openai-executive-shuffle-new-roles-coo-brad-lightcap-fidji-simo-kate-rouch/",
            "image": images.get("openai_shuffle", "")
        },
        {
            "title": {"zh": "DeepSeek V4 将运行在华为芯片上", "en": "DeepSeek's V4 Model Will Run on Huawei Chips"},
            "url": "https://www.asiaone.com/digital/deepseeks-v4-model-will-run-huawei-chips-information-reports",
            "image": images.get("deepseek_v4", "")
        },
        {
            "title": {"zh": "Anthropic Claude Mythos 泄露事件", "en": "Anthropic's Claude Mythos Leak Reveals 'Step Change' Model"},
            "url": "https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/",
            "image": images.get("apple_google", "")
        }
    ]
}

# Load existing issues and prepend new ones
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Added 2 issues (design + tech) for 2026-04-05. Total issues: {len(issues)}")
