# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Digest - 2026-03-16 Morning Update"""
import json
import urllib.request
import re
import html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=8)
        data = resp.read(50000).decode('utf-8', errors='ignore')
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', data, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data, re.I)
        return m.group(1) if m else ""
    except:
        return ""

# Sources
design_sources = [
    {
        "title": {"zh": "Figma Make: 从 Prompt 到代码的 AI 设计生成", "en": "Figma Make: Prompt-to-Code AI Design Generation"},
        "url": "https://www.figma.com/make/",
    },
    {
        "title": {"zh": "toools.design: 2026 最佳 AI UI/UX 工具深度评测", "en": "toools.design: 9 Best AI Tools for UI/UX Designers 2026"},
        "url": "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
    },
    {
        "title": {"zh": "Medium: 我在 UX 设计工作流中实际使用的 8 款 AI 工具", "en": "Medium: 8 Top AI Tools I Actually Use in My UX Design Workflow"},
        "url": "https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d",
    },
]

tech_sources = [
    {
        "title": {"zh": "Axios: Anthropic 起诉五角大楼「供应链风险」标签", "en": "Axios: Anthropic Sues Pentagon Over Supply Chain Risk Label"},
        "url": "https://www.axios.com/2026/03/09/anthropic-sues-pentagon-supply-chain-risk-label",
    },
    {
        "title": {"zh": "Fortune: Anthropic 诉五角大楼——结果可能重塑 AI 行业", "en": "Fortune: Anthropic vs Pentagon Could Reshape AI Industry"},
        "url": "https://fortune.com/2026/03/12/anthropic-pentagon-lawsuit-supply-chain-risk-china-ai-race/",
    },
    {
        "title": {"zh": "The Verge: NVIDIA Vera Rubin AI 平台在 CES 2026 发布", "en": "The Verge: NVIDIA Launches Vera Rubin at CES 2026"},
        "url": "https://www.theverge.com/tech/855412/nvidia-launches-vera-rubin-ai-computing-platform-at-ces-2026",
    },
    {
        "title": {"zh": "Yahoo Finance: Anthropic 的 2026 年——才三月就已经很疯狂", "en": "Yahoo Finance: Anthropic Is Having a Huge 2026"},
        "url": "https://finance.yahoo.com/news/anthropic-having-huge-2026-only-192121860.html",
    },
]

# Fetch og:images
print("Fetching og:images...")
for s in design_sources + tech_sources:
    img = get_og_image(s["url"])
    s["image"] = img
    print(f"  {s['url'][:60]}... -> {'found' if img else 'none'}")

design_cover = next((s["image"] for s in design_sources if s["image"]), "")
tech_cover = next((s["image"] for s in tech_sources if s["image"]), "")

design_issue = {
    "date": "2026-03-16",
    "section": "design",
    "title": {
        "zh": "Prompt-to-UI 三国杀 · Figma Make vs Motiff vs Google Stitch · 设计师的新角色：提示词工程师？",
        "en": "Prompt-to-UI Three-Way Battle · Figma Make vs Motiff vs Google Stitch · Designers' New Role: Prompt Engineers?"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Figma Make 全面铺开：Prompt-to-Code 进入政府市场，设计系统可直接嵌入 AI 生成流程</strong> — Figma 持续扩展 Make 功能，现已支持将 Make 原型嵌入 Figma Design、FigJam 和 Slides，并正式进入 Figma for Government。关键能力：用户可以创建包含设计系统的 Make 模板，确保 AI 生成的每个输出都符合品牌规范。这意味着 AI 不再是「野生成」，而是在约束框架内生成——这是企业级采用的关键门槛。<br><small>来源：<a href=\"https://www.figma.com/make/\">Figma Make</a> | <a href=\"https://www.figma.com/solutions/ai-design-systems-generator/\">Figma AI Design Systems Generator</a></small></li><li><strong>Motiff AI 异军突起：Prompt 生成可编辑 UI + 生产级 React/HTML 代码导出</strong> — Motiff 正在成为 Figma Make 最有力的竞争者。核心差异化：不只生成视觉设计，还直接输出可用的 React 和 HTML 代码。$16/月起，100 积分/月的免费额度让独立设计师也能试用。toools.design 的深度评测指出，Motiff 在「设计-代码」桥接上比 Figma Make 更激进。<br><small>来源：<a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">toools.design 深度评测</a> | <a href=\"https://motiff.com/\">Motiff 官网</a></small></li><li><strong>Google Stitch 仍在实验阶段，但支持上传现有设计系统——AI 生成与品牌一致性的关键能力</strong> — Google 的 Stitch 是一款实验性 AI 设计工具，从文本提示或上传图片生成移动和 Web UI。其独特之处在于支持导入自定义设计系统，让 AI 生成的结果保持品牌一致性。尽管尚未正式商业化，但这种「约束生成」思路与 Figma Make 的方向不谋而合。<br><small>来源：<a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">toools.design</a></small></li><li><strong>一线设计师的现实反馈：AI 工具用于探索加速，最终打磨仍需手动判断</strong> — Medium 上一位 UX 设计师分享了他实际使用 8 款 AI 工具的工作流。核心结论：AI 擅长加速早期探索（低保真原型、色彩方案、视觉预测），但最终的精确度、一致性和设计意图仍依赖 Figma 手动操作。「未来不是找到一个完美的 AI 工具，而是学会组合使用。」<br><small>来源：<a href=\"https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d\">Medium: 8 Top AI Tools I Actually Use</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>Prompt-to-UI 进入三国杀阶段</strong>：Figma Make、Motiff、Google Stitch 各有定位，竞争格局初现</li><li><strong>「约束生成」成为企业采用关键</strong>：能导入设计系统并遵循品牌规范的 AI 工具才有企业市场</li><li><strong>设计-代码边界持续模糊</strong>：Motiff 直接出 React 代码，Figma 推 MCP 连接 AI 编码工具</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Prompt-to-UI 工具的战场终于从「谁能生成最好看的界面」进化到了一个真正重要的问题：谁能在约束条件下生成最可用的界面？</strong></p><p>让我把这三个工具摆在一起看。Figma Make 的策略很清晰：不追求最强的 AI 生成能力，而是把 AI 深度嵌入已有的设计生态。Make 原型可以嵌入 Figma Design、FigJam 和 Slides——这意味着 AI 生成不再是一个孤立的步骤，而是整个设计工作流的自然组成部分。更重要的是，Make 支持将设计系统直接嵌入模板，确保 AI 每次生成都在品牌约束框架内。这是典型的 Figma 打法：不一定最酷，但一定最实用、最容易被团队采纳。</p><p>Motiff 选择了一条更激进的路：直接输出生产级 React 和 HTML 代码。这不是小事。传统工作流里，设计师输出视觉稿，开发者「翻译」成代码，这个翻译过程是设计还原率最大的瓶颈。Motiff 试图彻底消灭这个环节。如果它的代码质量真的能达到生产可用级别（目前还需要更多验证），那它颠覆的不只是设计工具市场，而是整个设计-开发协作流程。$16/月的价格也很有攻击性——直接对标 Figma Pro。</p><p>Google Stitch 还在实验阶段，但它和 Figma Make 不约而同地支持了同一个关键能力：导入自定义设计系统。这说明行业已经形成共识——<strong>「野生成」（不带约束的 AI 生成）在消费级产品里很有趣，但在企业设计中毫无价值。</strong>没有哪个品牌总监会接受 AI 随机生成的配色和排版。约束生成才是真正的需求。</p><p>但最让我注意的是那位 Medium 设计师的分享。他用了 8 款 AI 工具，结论是什么？「最终打磨仍需手动判断。」这不是 AI 工具的失败，这是 AI 工具的正确定位。上周我们讨论了设计师从「创作者」到「策展人」的转变——今天的现实数据证实了这一点：AI 负责生成初稿和探索方向，人类负责判断、筛选和精修。问题是，当越来越多设计师跳过「精修」阶段直接交付 AI 产出时，平均设计质量会发生什么变化？</p><p><strong>我的预测：2026 年下半年，Prompt-to-UI 领域会出现一次洗牌。</strong>Figma Make 凭借生态锁定会是最安全的选择；Motiff 如果代码质量过关，有可能成为独立设计师和小团队的首选；Google Stitch 的命运取决于 Google 是否认真对待这个产品（考虑到 Google 砍产品的传统，这不是一个可以放心押注的赌局）。但真正值得关注的不是哪个工具赢，而是这些工具合在一起正在重新定义「设计师」这个职业的边界——当 Prompt 可以出设计，Motiff 可以出代码，设计师到底在做什么？答案是：做那些 AI 做不好的事——理解用户、定义问题、做出有品味的取舍。这是不可自动化的。至少目前是。</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Figma Make Goes Wide: Prompt-to-Code Enters Government, Design Systems Embeddable in AI Generation</strong> — Make prototypes can now embed in Figma Design, FigJam, and Slides. Figma for Government support means enterprise-grade constrained generation.<br><small>Source: <a href=\"https://www.figma.com/make/\">Figma Make</a></small></li><li><strong>Motiff AI Rises: Prompt-Generated Editable UI + Production-Ready React/HTML Export</strong> — Motiff differentiates by outputting usable React and HTML code directly. At $16/month, it's an aggressive Figma Pro competitor.<br><small>Source: <a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">toools.design Deep Dive</a></small></li><li><strong>Google Stitch: Experimental but Supports Custom Design System Import</strong> — Generates mobile/web UI from prompts while maintaining brand consistency through imported design systems.<br><small>Source: <a href=\"https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026\">toools.design</a></small></li><li><strong>Practitioner Reality Check: AI Accelerates Exploration, Final Polish Still Manual</strong> — A UX designer's 8-tool workflow confirms AI's sweet spot is early exploration, not final delivery.<br><small>Source: <a href=\"https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d\">Medium</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Prompt-to-UI enters three-way battle: Figma Make vs Motiff vs Google Stitch</li><li>Constrained generation (design system-aware) becomes the enterprise adoption gate</li><li>Design-code boundary continues blurring: Motiff outputs React, Figma pushes MCP</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>The prompt-to-UI battlefield has evolved from \"who generates the prettiest screens\" to the question that actually matters: who can generate the most usable output under constraints?</strong></p><p>Figma Make's play is ecosystem lock-in — embed AI generation into existing workflows with design system constraints. Motiff takes the aggressive route: production-ready React/HTML code output, potentially eliminating the design-to-dev handoff bottleneck entirely. Google Stitch and Figma Make independently converging on custom design system import proves the industry consensus: unconstrained AI generation is fun for consumers but worthless in enterprise design. The practitioner feedback is key: AI handles exploration, humans handle judgment and polish. <strong>My prediction: H2 2026 sees a shakeout. Figma Make wins on ecosystem, Motiff could capture indie designers if code quality holds, and Stitch's fate depends on Google's product commitment (not a safe bet). But the real story is these tools collectively redefining what \"designer\" means — when prompts generate designs and tools export code, designers must focus on what AI can't do: understanding users, defining problems, and making tasteful trade-offs.</strong></p></div>"
    },
    "cover": design_cover,
    "sources": design_sources,
}

tech_issue = {
    "date": "2026-03-16",
    "section": "tech",
    "title": {
        "zh": "Anthropic 诉五角大楼 · AI 安全 vs 国家权力的宪法对决 · NVIDIA Vera Rubin 量产 · 训练成本降 90%",
        "en": "Anthropic Sues Pentagon · AI Safety vs State Power Constitutional Showdown · NVIDIA Vera Rubin in Production · 90% Training Cost Cut"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>Anthropic 正式起诉五角大楼：「供应链风险」标签违宪，要求撤销并禁止执行</strong> — Anthropic 在旧金山联邦法院对国防部提起诉讼，指控五角大楼将其列为「供应链风险」的行为「史无前例且违法」。起因：五角大楼要求 Anthropic 取消 Claude 的使用限制（禁止用于大规模监控和自主武器），Anthropic 拒绝后，特朗普政府下令所有联邦机构停止使用 Anthropic 产品。Anthropic 主张这违反了第一修正案——政府可以选择不合作，但不能因为企业的「受保护言论」而将其污名化为安全风险。<br><small>来源：<a href=\"https://www.axios.com/2026/03/09/anthropic-sues-pentagon-supply-chain-risk-label\">Axios</a> | <a href=\"https://techcrunch.com/2026/03/09/anthropic-sues-defense-department-over-supply-chain-risk-designation/\">TechCrunch</a> | <a href=\"https://www.cnn.com/2026/03/09/tech/anthropic-sues-pentagon\">CNN</a></small></li><li><strong>Fortune 深度分析：这场诉讼可能重塑整个 AI 行业——2 亿美元合同只是开始</strong> — Fortune 报道，「供应链风险」标签的影响远超五角大楼合同本身。所有与联邦政府做生意的企业都可能需要证明「零 Anthropic 暴露」——包括 AWS、Google Cloud、Azure 等 Anthropic 的核心分发渠道。这是一个连锁反应：如果标签不撤销，Anthropic 的整个企业商业化路径可能被切断。<br><small>来源：<a href=\"https://fortune.com/2026/03/12/anthropic-pentagon-lawsuit-supply-chain-risk-china-ai-race/\">Fortune</a></small></li><li><strong>NVIDIA Vera Rubin 进入「全面量产」：训练成本降 90%，推理 token 成本降 10 倍</strong> — Jensen Huang 确认 Vera Rubin 芯片已进入全面量产，预计 2026 下半年交付。关键指标：AI 训练所需 GPU 数量减少 75%（MoE 模型），推理 token 成本降低 10 倍。Rubin 不只是一块 GPU，而是一个「机架级超级计算机」——包含 Rubin GPU、Vera CPU 和 NVLink 6（260TB/s 数据传输速度）。分析师预计 Rubin + Blackwell 平台 2026 年合计营收可达约 5000 亿美元。<br><small>来源：<a href=\"https://www.theverge.com/tech/855412/nvidia-launches-vera-rubin-ai-computing-platform-at-ces-2026\">The Verge</a> | <a href=\"https://www.techrepublic.com/article/news-nvidia-introduces-vera-rubin-ces-2026/\">TechRepublic</a></small></li><li><strong>Yahoo Finance: Anthropic 的 2026 年「才三月就已经很疯狂」——安全工具正在颠覆企业软件</strong> — Yahoo Finance 的专题报道指出，Anthropic 开发的安全工具现在正在「颠覆企业软件，重塑工程师的工作方式」，同时将自己推向了「与五角大楼全面对峙」的中心。一个公司同时在商业上爆发增长和在政治上面临生存威胁——这种双重态势在科技史上相当罕见。<br><small>来源：<a href=\"https://finance.yahoo.com/news/anthropic-having-huge-2026-only-192121860.html\">Yahoo Finance</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 安全 vs 国家权力：宪法级对决</strong>：Anthropic 的诉讼可能成为 AI 行业的「里程碑判例」</li><li><strong>供应链武器化</strong>：政府用「供应链风险」标签作为商业制裁工具，影响整个 AI 生态</li><li><strong>算力成本断崖式下降</strong>：Vera Rubin 让万亿参数模型训练从「只有巨头能玩」变为「中等规模公司也能负担」</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>Anthropic 诉五角大楼，表面上是一场合同纠纷，实质上是 AI 时代第一场关于「谁有权定义 AI 使用边界」的宪法级对决。这比任何新模型发布都重要。</strong></p><p>让我拆解这件事的深层逻辑。Anthropic 2025 年 7 月签了 2 亿美元的五角大楼合同，合同里包含两条红线：Claude 不能用于大规模监控美国公民，不能用于自主武器。这不是什么激进立场——这是 Anthropic 品牌叙事的基石。然后五角大楼说：「把限制去掉，否则失去一切。」Anthropic 拒绝了。然后特朗普政府直接给 Anthropic 贴了「供应链风险」标签。</p><p>这个标签的杀伤力远超 2 亿美元合同本身。Fortune 的分析说得很清楚：所有联邦承包商可能都需要证明自己的系统中没有 Anthropic 产品。AWS、Google Cloud、Azure 都是联邦供应商，同时也是 Anthropic 的主要分发渠道。这是一个「连坐」逻辑——打击一家公司，但实际上威胁整个云计算生态。如果标签不撤销，Anthropic 可能在企业市场遭遇毁灭性打击，恰恰在它商业势头最猛的时候（上周 Ramp 数据：企业客户 6 倍增长）。</p><p>Anthropic 的法律论点很有意思：政府可以选择不购买 Claude，但不能用「供应链风险」标签来惩罚 Anthropic 坚持使用限制的立场——这属于受保护的商业言论。如果法院支持这个论点，它将为 AI 公司设定使用限制的权利提供宪法保护。如果法院不支持……那每家 AI 公司都必须重新评估自己是否愿意对政府客户设定任何条件。</p><p>现在把 NVIDIA Vera Rubin 的消息放进来看。训练成本降 90%，MoE 模型所需 GPU 减少 75%——这意味着什么？<strong>如果 Anthropic 因为五角大楼标签而在美国市场受阻，那些获得 Vera Rubin 芯片的国际和中国竞争对手（比如上周的 DeepSeek V4）将以更低成本训练出更强的模型。</strong>美国政府试图用「供应链风险」来控制 AI 公司的安全政策，但同时 NVIDIA 的新硬件正在让全球范围内的 AI 训练成本暴跌——这两个趋势合在一起的效果是：美国 AI 安全领军者被自己的政府削弱，而全球竞争对手的训练成本在急剧下降。</p><p><strong>这是 2026 年 AI 行业最讽刺的画面：一个政府一边声称要赢得 AI 竞赛，一边在惩罚自己最注重安全的 AI 公司。</strong>Anthropic 的诉讼结果不管怎样，都将是 AI 行业的分水岭。如果 Anthropic 赢了，AI 公司获得了对政府说「不」的法律武器；如果 Anthropic 输了，「AI 安全」作为商业策略将死于政治压力。无论哪种结果，这都比任何基准测试上的百分点更深远地影响 AI 的未来。</p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Anthropic Sues Pentagon: \"Supply Chain Risk\" Label Called Unconstitutional</strong> — Anthropic filed suit after refusing to remove Claude's restrictions on mass surveillance and autonomous weapons. Trump administration ordered all federal agencies to stop using Anthropic. The company argues this violates First Amendment protections.<br><small>Source: <a href=\"https://www.axios.com/2026/03/09/anthropic-sues-pentagon-supply-chain-risk-label\">Axios</a> | <a href=\"https://techcrunch.com/2026/03/09/anthropic-sues-defense-department-over-supply-chain-risk-designation/\">TechCrunch</a> | <a href=\"https://www.cnn.com/2026/03/09/tech/anthropic-sues-pentagon\">CNN</a></small></li><li><strong>Fortune Analysis: This Lawsuit Could Reshape the Entire AI Industry</strong> — The \"supply chain risk\" label threatens Anthropic's cloud distribution channels (AWS, Google Cloud, Azure) — all federal contractors may need to certify zero Anthropic exposure.<br><small>Source: <a href=\"https://fortune.com/2026/03/12/anthropic-pentagon-lawsuit-supply-chain-risk-china-ai-race/\">Fortune</a></small></li><li><strong>NVIDIA Vera Rubin in \"Full Production\": 90% Training Cost Reduction, 10x Cheaper Inference</strong> — Jensen Huang confirms mass production. 75% fewer GPUs needed for MoE model training. Analysts forecast ~$500B combined Rubin+Blackwell revenue in 2026.<br><small>Source: <a href=\"https://www.theverge.com/tech/855412/nvidia-launches-vera-rubin-ai-computing-platform-at-ces-2026\">The Verge</a> | <a href=\"https://www.techrepublic.com/article/news-nvidia-introduces-vera-rubin-ces-2026/\">TechRepublic</a></small></li><li><strong>Yahoo Finance: Anthropic's Wild 2026 — Safety Tools Disrupting Enterprise Software While Facing Pentagon Standoff</strong> — A company simultaneously experiencing explosive growth and existential political threat — rare in tech history.<br><small>Source: <a href=\"https://finance.yahoo.com/news/anthropic-having-huge-2026-only-192121860.html\">Yahoo Finance</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI Safety vs State Power: constitutional-level showdown with industry-wide implications</li><li>Supply chain weaponization: government uses risk labels as commercial sanctions</li><li>Training cost cliff: Vera Rubin makes trillion-param models accessible to mid-size orgs</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>Anthropic vs Pentagon is not a contract dispute — it's the first constitutional battle over who gets to define AI usage boundaries. This matters more than any model release.</strong></p><p>The kill chain: Pentagon demands unrestricted Claude access → Anthropic refuses (no mass surveillance, no autonomous weapons) → Trump designates Anthropic a \"supply chain risk\" → all federal agencies cut ties → cloud providers (AWS, Google Cloud, Azure) face pressure to certify zero Anthropic exposure. This \"guilt by association\" logic threatens Anthropic's entire enterprise distribution at its moment of peak commercial momentum (6x enterprise growth per Ramp data last week). Now layer in NVIDIA Vera Rubin: 90% training cost reduction means global competitors (DeepSeek V4 etc.) can train stronger models cheaper — while the US government weakens its own safety-conscious AI leader. <strong>The 2026 irony: a government claiming to lead the AI race is punishing its most safety-focused AI company. Whether Anthropic wins or loses, this is a watershed. Win = AI companies gain legal weapons to say \"no\" to governments. Lose = \"AI safety\" as a business strategy dies under political pressure. Either outcome reshapes AI's future more than any benchmark improvement ever could.</strong></p></div>"
    },
    "cover": tech_cover,
    "sources": tech_sources,
}

# Load existing issues and prepend new ones
with open('issues.json', 'r', encoding='utf-8') as f:
    issues = json.load(f)

issues = [design_issue, tech_issue] + issues

with open('issues.json', 'w', encoding='utf-8') as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"Done! Total issues: {len(issues)}")
