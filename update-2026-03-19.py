# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=8)
        data = resp.read(50000).decode("utf-8", errors="ignore")
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', data)
        if not m:
            m = re.search(r'content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', data)
        return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images
urls = {
    "figma": "https://www.figma.com/resource-library/ai-design-tools/",
    "stitch": "https://almcorp.com/blog/google-stitch-complete-guide-ai-ui-design-tool-2026/",
    "toools": "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
    "cnbc_gtc": "https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html",
    "gpt54": "https://openai.com/index/introducing-gpt-5-4/",
    "ghacks": "https://www.ghacks.net/2026/03/06/openai-launches-gpt-5-4-with-ai-agents-that-can-use-computers/",
    "nemoclaw": "https://finance.yahoo.com/news/nvidia-launches-nemoclaw-platform-for-ai-agents-200851962.html",
}

print("Fetching og:images...")
images = {}
for k, u in urls.items():
    img = get_og_image(u)
    images[k] = img
    print(f"  {k}: {img[:80] if img else '(none)'}")

design_issue = {
    "date": "2026-03-19",
    "section": "design",
    "title": {
        "zh": "Prompt-to-UI 三国杀进入下半场 · Figma Make / Google Stitch / Motiff 全面对比 · AI 设计工具从「能用」到「能信赖」的关键一步",
        "en": "Prompt-to-UI Battle Enters Second Half · Figma Make vs Google Stitch vs Motiff · AI Design Tools Move from 'Usable' to 'Trustworthy'"
    },
    "content": {
        "zh": """<h3>📌 AI × 设计</h3><ul><li><strong>2026 年 AI UI 设计工具全景：Figma Make、Google Stitch、Motiff 三足鼎立</strong> — 多个权威评测（Figma 官方、Muzli、toools.design）在 2026 年 3 月密集发布 AI 设计工具年度盘点。核心格局已清晰：<strong>Figma Make</strong> 凭借原生生态和设计系统整合占据专业设计师首选地位（$16/用户/月，含 AI 额度）；<strong>Google Stitch</strong> 从 Galileo AI 演化而来，擅长从自然语言/截图直接生成完整 UI + 可用前端代码（React/HTML/CSS），定位更偏原型验证；<strong>Motiff</strong> 主打代码导出质量，生成的 React 代码可直接投入生产。三者的竞争焦点正从「能不能生成 UI」转向「生成的 UI 能不能直接用」。<br><small>来源：<a href="https://www.figma.com/resource-library/ai-design-tools/">Figma 官方 AI 工具指南</a> | <a href="https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026">toools.design 2026 AI 设计工具深度对比</a> | <a href="https://medium.muz.li/best-ai-design-tools-for-ui-ux-designers-in-2026-54ecd8d8dee2">Muzli 2026 AI 设计工具测评</a></small></li><li><strong>Google Stitch 四大更新：编辑、分享、多平台适配全面升级</strong> — Google Labs 本周为 Stitch 推送四项重要更新：改进的编辑能力、更好的分享协作、以及优化的跨平台（Mobile/Web/Tablet）生成质量。Stitch 正在从「实验性玩具」向「可用工具」快速演进。值得注意的是，Stitch 免费可用，这对 Figma Make 的付费模式构成潜在压力。<br><small>来源：<a href="https://www.instagram.com/reel/DVHobrUj6jI/">AI on Instagram: Google Stitch 四大更新</a> | <a href="https://almcorp.com/blog/google-stitch-complete-guide-ai-ui-design-tool-2026/">ALM Corp: Google Stitch 完全指南</a></small></li><li><strong>设计师的 AI 工作流正在定型：「40+ 工具测试后，这是我的真实工作流」</strong> — Muzli 的深度测评文章引发设计社区讨论。作者测试了 40+ AI 设计工具后得出结论：2026 年有效的 AI 设计工作流不是堆工具，而是围绕 Figma 生态建立「AI 设计系统」——用 Figma Make 生成初始 UI，用 UX Pilot 做用户研究和热力图预测，用 Khroma 探索配色方向。关键洞察：<strong>最好的 AI 设计工具不是生成能力最强的，而是与现有工作流集成最好的。</strong><br><small>来源：<a href="https://medium.muz.li/best-ai-design-tools-for-ui-ux-designers-in-2026-54ecd8d8dee2">Muzli: 我的 2026 AI 设计工作流</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>Prompt-to-UI 从「Demo 级」进入「生产级」</strong>：竞争焦点从生成质量转向代码可用性和设计系统兼容</li><li><strong>免费 vs 付费的拉锯战</strong>：Google Stitch 免费策略 vs Figma Make 生态绑定策略</li><li><strong>AI 设计工具的整合期开始</strong>：设计师不再追新工具，而是在构建稳定的 AI 工作流</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>三月的 AI 设计工具市场出现了一个有意思的拐点：设计师们不再兴奋地追逐每一个新工具，而是开始冷静地问「这东西能不能真正融入我的日常工作流？」</strong></p><p>这是成熟的信号。Muzli 那篇「测了 40+ 工具后的真实工作流」文章之所以引发共鸣，不是因为它推荐了什么神器，而是因为它说出了一个大家心知肚明但不愿承认的事实：<strong>绝大多数 AI 设计工具在 Demo 里惊艳，在真实项目里鸡肋。</strong>真正有用的工具屈指可数，而且它们的价值不在于「AI 有多强」，而在于「和 Figma 的集成有多深」。</p><p>这就引出了当前三足鼎立格局的核心矛盾。<strong>Figma Make 的优势不是 AI 技术本身——老实说它的生成质量未必是最好的——而是它就在你已经打开的 Figma 文件里。</strong>这种「零切换成本」的生态优势是 Google Stitch 和 Motiff 拿免费策略和更好的代码质量都难以撼动的。历史总是重复：最好的技术不一定赢，嵌入最深的技术赢。想想 Sketch 是怎么输给 Figma 的——不是功能不行，是协作体验差了一个维度。</p><p>但 Google Stitch 的免费策略值得警惕。Google 在 AI 设计工具上不需要赚钱——它需要的是用户在 Google 生态里生成更多内容、使用更多 Google Cloud 资源。当 Stitch 从「实验性玩具」进化为「可用工具」（本周的四项更新就是信号），它对 Figma 的威胁不是直接替代，而是<strong>从下游蚕食</strong>：如果快速原型阶段不需要 Figma 了，那 Figma 在工作流中的起始位置就被动摇了。</p><p>Motiff 的路线则代表了另一种可能：<strong>不争「设计生成」，争「设计到代码」。</strong>它的 React 代码导出质量被多个评测认可为最佳。在「设计师需要自己写代码吗？」这个问题变得越来越模糊的 2026 年，Motiff 赌的是设计和开发之间的 handoff 会被 AI 完全消除——到那时，能直接输出生产级代码的工具会胜出。</p><p>我的判断：<strong>2026 年下半年，Prompt-to-UI 赛道会经历一轮洗牌。</strong>那些只做「文字生成 UI 图片」的工具会迅速被淘汰，因为这个功能已经被 Figma Make 和 Stitch 平台化了。存活下来的要么像 Motiff 一样在代码质量上做到极致，要么像 UX Pilot 一样占据一个 Figma 做不好的垂直场景（比如 AI 驱动的用户研究）。<strong>工具的爆发期结束了，整合期开始了。</strong>对设计师来说，这反而是好消息——你终于不用每周学一个新工具了。</p></div>""",
        "en": """<h3>📌 AI × Design</h3><ul><li><strong>2026 AI UI Design Tool Landscape: Figma Make, Google Stitch, Motiff in Three-Way Competition</strong> — Multiple authoritative reviews published in March 2026 reveal a clear market structure: Figma Make dominates with native ecosystem integration ($16/user/month); Google Stitch (evolved from Galileo AI) excels at generating full UI + production code from natural language; Motiff leads in code export quality with production-ready React output. Competition shifts from "can it generate UI" to "can the generated UI be used directly."<br><small>Source: <a href="https://www.figma.com/resource-library/ai-design-tools/">Figma Official</a> | <a href="https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026">toools.design</a></small></li><li><strong>Google Stitch Gets Four Major Updates</strong> — Google Labs ships improved editing, sharing, and cross-platform generation. Stitch is rapidly evolving from experimental toy to usable tool — and it's free, putting pressure on Figma's paid model.<br><small>Source: <a href="https://almcorp.com/blog/google-stitch-complete-guide-ai-ui-design-tool-2026/">ALM Corp Guide</a></small></li><li><strong>Designers Are Settling on AI Workflows</strong> — After testing 40+ tools, the community consensus: the best AI design tool isn't the most powerful generator — it's the one that integrates best with existing workflows.<br><small>Source: <a href="https://medium.muz.li/best-ai-design-tools-for-ui-ux-designers-in-2026-54ecd8d8dee2">Muzli</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Prompt-to-UI moves from demo-grade to production-grade</li><li>Free (Stitch) vs ecosystem lock-in (Figma Make) tension</li><li>AI design tool consolidation begins — designers stop chasing new tools</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>March 2026 marks a turning point: designers have stopped chasing every new AI tool and started asking "does this actually fit my workflow?"</strong></p><p>Figma Make's advantage isn't AI quality — it's zero switching cost inside an already-open Figma file. Best tech doesn't always win; most embedded tech wins. Google Stitch's free strategy threatens from downstream: if prototyping doesn't need Figma, Figma's workflow starting position erodes. Motiff bets on the design-to-code handoff disappearing entirely. <strong>H2 2026 prediction: tools that only generate "UI pictures from text" will be eliminated — that feature is now platformized. Survivors will either nail code quality (Motiff) or own a vertical Figma can't do well (UX Pilot for AI-driven research). The explosion phase is over; consolidation begins.</strong></p></div>"""
    },
    "cover": images.get("figma", ""),
    "sources": [
        {
            "title": {"zh": "Figma 官方：2026 年 11 款最佳 AI 设计工具", "en": "Figma: 11 Best AI Design Tools for 2026"},
            "url": "https://www.figma.com/resource-library/ai-design-tools/",
            "image": images.get("figma", "")
        },
        {
            "title": {"zh": "toools.design: 2026 年 9 款最佳 AI UI/UX 工具深度对比", "en": "toools.design: 9 Best AI UI/UX Tools 2026 Deep Dive"},
            "url": "https://www.toools.design/blog-posts/best-ai-tools-ui-ux-designers-2026",
            "image": images.get("toools", "")
        },
        {
            "title": {"zh": "Muzli: 2026 年 UI/UX 设计师最佳 AI 设计工具", "en": "Muzli: Best AI Design Tools for UI/UX Designers 2026"},
            "url": "https://medium.muz.li/best-ai-design-tools-for-ui-ux-designers-in-2026-54ecd8d8dee2",
            "image": ""
        },
        {
            "title": {"zh": "ALM Corp: Google Stitch 完全指南 2026", "en": "ALM Corp: Google Stitch Complete Guide 2026"},
            "url": "https://almcorp.com/blog/google-stitch-complete-guide-ai-ui-design-tool-2026/",
            "image": images.get("stitch", "")
        }
    ]
}

tech_issue = {
    "date": "2026-03-19",
    "section": "tech",
    "title": {
        "zh": "GTC 2026 重磅：Jensen 预告万亿美元 AI 硬件订单 · Groq 3 LPU 首秀 · NemoClaw AI Agent 平台发布 · GPT-5.4 开启「电脑操控」时代",
        "en": "GTC 2026 Bombshells: Jensen's $1T AI Hardware Forecast · Groq 3 LPU Debut · NemoClaw AI Agent Platform · GPT-5.4 Unlocks Computer Control"
    },
    "content": {
        "zh": """<h3>📌 AI × 科技</h3><ul><li><strong>NVIDIA GTC 2026 主题演讲：Jensen Huang 预告到 2027 年 AI 硬件订单将达万亿美元</strong> — Jensen 在周一的两小时主题演讲中投下重磅炸弹：Blackwell + Vera Rubin 的采购订单预计到 2027 年累计达 1 万亿美元。上月财报后 CFO Colette Kress 已暗示增长将超预期，GTC 上 Jensen 亲自确认了这个天文数字。Vera Rubin 将于今年晚些时候出货。更值得关注的是：Jensen 成功游说特朗普政府允许 H200 芯片出口中国，理由是「让中国依赖美国技术比逼它自主研发更好」——这是一个极具争议但可能改变地缘科技格局的决策。<br><small>来源：<a href="https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html">CNBC</a> | <a href="https://finance.yahoo.com/news/live/tech-stocks-today-nvidias-jensen-huang-kicks-off-gtc-event-with-1-trillion-forecast-144220827.html">Yahoo Finance</a></small></li><li><strong>NVIDIA Groq 3 LPU 首次亮相：收购 Groq 后的首款芯片产品</strong> — GTC 上发布的 Groq 3 Language Processing Unit 是 NVIDIA 去年 12 月以 200 亿美元收购 Groq 后的首款产品。Groq 3 + Groq LPX 机架将加入 Vera Rubin 平台，定位于 AI 推理加速。SRAM 密集型架构可对模型每一层的每个 token 进行加速。这意味着 NVIDIA 不再只做 GPU 训练——它正在全面布局推理市场，直接威胁到 AMD、Intel 以及 AWS Inferentia 等推理专用芯片的生存空间。<br><small>来源：<a href="https://www.tomshardware.com/pc-components/gpus/nvidia-groq-3-lpu-and-groq-lpx-racks-join-rubin-platform-at-gtc-sram-packed-accelerator-boosts-every-layer-of-the-ai-model-on-every-token">Tom's Hardware</a></small></li><li><strong>NVIDIA NemoClaw：面向 AI Agent 的全新开发平台</strong> — GTC 同时发布了 NemoClaw 平台，专为构建和部署 AI Agent 设计。结合 Jensen 在主题演讲中将 Agentic AI 列为第一优先级来看，NVIDIA 的战略很清晰：不只提供算力，还要拥有 AI Agent 的开发者生态。NemoClaw 的命名（Nemo + Claw = 模型框架 + 工具控制）暗示了 NVIDIA 对 Agent 架构的理解：Agent = 模型 + 工具使用能力。<br><small>来源：<a href="https://finance.yahoo.com/news/nvidia-launches-nemoclaw-platform-for-ai-agents-200851962.html">Yahoo Finance</a></small></li><li><strong>OpenAI GPT-5.4 发布：AI Agent 正式进入「电脑操控」时代</strong> — 3 月 6 日发布的 GPT-5.4 将推理、编码和 Agentic 能力统一到单一模型中。最大亮点：AI Agent 现在可以操控电脑完成任务——打开应用、操作电子表格、浏览网页、执行多步骤工作流。在 GDPval 基准测试（覆盖 44 个职业的知识工作评估）中，GPT-5.4 在 83% 的对比中匹配或超越行业专业人士（GPT-5.2 为 70.9%）。电子表格建模得分从 GPT-5.2 的 68.4% 跃升至 87.3%。OpenAI 称这是「最真实的模型」——幻觉率显著降低。新增 Tool Search API 让模型在面对大量工具时能高效选择。<br><small>来源：<a href="https://openai.com/index/introducing-gpt-5-4/">OpenAI 官方博客</a> | <a href="https://www.pcmag.com/news/gpt-54-is-here-new-model-prepares-for-autonomous-agents-shares-fewer-errors">PCMag</a> | <a href="https://www.ghacks.net/2026/03/06/openai-launches-gpt-5-4-with-ai-agents-that-can-use-computers/">gHacks</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>NVIDIA 从「GPU 供应商」变为「AI 全栈平台」</strong>：训练（GPU）+ 推理（Groq LPU）+ Agent 开发（NemoClaw）+ 芯片出口（H200 对华）</li><li><strong>AI Agent 的「电脑操控」能力正在从实验走向主流</strong>：GPT-5.4 + NemoClaw 双管齐下</li><li><strong>万亿美元的 AI 硬件市场</strong>：Jensen 的预测意味着 AI 基建投资仍在加速，没有放缓迹象</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>GTC 2026 第三天（3月19日），让我把这周最重要的两条线索串起来：NVIDIA 的全栈野心和 OpenAI 的 Agent 突破。它们正在合流，指向同一个方向——AI 从「对话工具」变成「工作执行者」。</strong></p><p>先说 Jensen 的万亿美元预言。到 2027 年 Blackwell + Vera Rubin 订单累计一万亿美元——这个数字让人本能地想质疑，但如果你看看背后的逻辑链，它可能是保守的。全球每一个大型企业都在建 AI 基础设施，每一个云厂商都在扩容，每一个国家都在搞「AI 主权」。当需求侧是「所有人」的时候，供给侧垄断者（NVIDIA 在高端 AI 芯片市场份额仍超 80%）的收入自然是天文数字。更有意思的是 H200 对华出口的决策——Jensen 说服了特朗普政府，理由很务实：与其让中国发展自己的芯片（DeepSeek 已经证明他们能用更少的算力做出接近顶级的模型），不如让他们依赖美国技术。这是「技术依赖」策略 vs「技术封锁」策略的路线之争，Jensen 选了前者。</p><p>再看 Groq 3 LPU。NVIDIA 花 200 亿买 Groq 不是为了好玩——它是在补推理市场的短板。训练市场 NVIDIA 已经垄断，但推理市场（模型部署后的实际运行）还是一个多方混战的局面：AWS Inferentia、Google TPU、AMD MI300X 都在争。Groq 的 SRAM 密集型架构专为推理优化，现在它成了 NVIDIA Rubin 平台的一部分。<strong>这意味着 NVIDIA 要同时垄断训练和推理两个市场。</strong>如果它成功了，AI 计算的每一个环节都将经过 NVIDIA 的芯片——这不是垄断，这是操作系统级别的控制。</p><p>现在把 GPT-5.4 放进来。OpenAI 这次最大的突破不是模型更聪明了（虽然确实更聪明），而是<strong>模型可以操控电脑了</strong>。打开应用、操作电子表格、浏览网页、执行多步骤工作流——GDPval 测试显示它在 44 个职业的知识工作中有 83% 匹配或超越人类专业人士。再加上 NVIDIA 同期发布的 NemoClaw Agent 平台，你看到的画面是：<strong>硬件层（Groq 3 加速推理）+ 平台层（NemoClaw 管理 Agent）+ 模型层（GPT-5.4 执行任务）三层叠加</strong>，构成了一个完整的「AI 自主工作」技术栈。</p><p>对普通人意味着什么？GPT-5.4 的电子表格建模得分从 68.4% 跳到 87.3%，这不是学术分数的变化——这意味着一个 AI Agent 做财务建模的准确率已经超过大多数初级分析师。<strong>当 AI 能操控电脑执行工作流时，被自动化的不是「对话」，而是「操作」——那些你每天花几个小时在电脑前点点点的重复性工作。</strong>2026 年下半年，我们大概率会看到第一波「AI Agent 替代初级白领岗位」的裁员新闻。不是因为 AI 比人聪明，而是因为它比人便宜、比人快、不会累、而且 NVIDIA 正在让运行它的成本持续下降。</p><p>GTC 2026 的真正信息不是万亿美元——而是 <strong>AI 正在从「你用的工具」变成「替你工作的员工」</strong>，而这个转变的基础设施，正在以万亿美元的速度被建设。</p></div>""",
        "en": """<h3>📌 AI × Tech</h3><ul><li><strong>NVIDIA GTC 2026: Jensen Huang Forecasts $1 Trillion in AI Hardware Orders Through 2027</strong> — During his two-hour keynote, Huang projected cumulative Blackwell + Vera Rubin purchase orders reaching $1T by 2027. Also successfully lobbied Trump administration to allow H200 chip exports to China.<br><small>Source: <a href="https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html">CNBC</a></small></li><li><strong>NVIDIA Groq 3 LPU Debuts: First Product from $20B Groq Acquisition</strong> — The SRAM-dense inference accelerator joins Vera Rubin platform, signaling NVIDIA's push to monopolize both training and inference markets.<br><small>Source: <a href="https://www.tomshardware.com/pc-components/gpus/nvidia-groq-3-lpu-and-groq-lpx-racks-join-rubin-platform-at-gtc-sram-packed-accelerator-boosts-every-layer-of-the-ai-model-on-every-token">Tom's Hardware</a></small></li><li><strong>NVIDIA NemoClaw: New Platform for Building AI Agents</strong> — Purpose-built for deploying autonomous AI agents, completing NVIDIA's full-stack vision: chips + platform + agent ecosystem.<br><small>Source: <a href="https://finance.yahoo.com/news/nvidia-launches-nemoclaw-platform-for-ai-agents-200851962.html">Yahoo Finance</a></small></li><li><strong>OpenAI GPT-5.4: AI Agents Can Now Control Computers</strong> — Unifies reasoning, coding, and agentic capabilities. Matches or exceeds professionals in 83% of knowledge work tasks (44 occupations). Spreadsheet modeling jumps from 68.4% to 87.3%. OpenAI's most factual model yet.<br><small>Source: <a href="https://openai.com/index/introducing-gpt-5-4/">OpenAI</a> | <a href="https://www.pcmag.com/news/gpt-54-is-here-new-model-prepares-for-autonomous-agents-shares-fewer-errors">PCMag</a></small></li></ul><h3>🔄 Trends</h3><ul><li>NVIDIA evolves from GPU vendor to full-stack AI platform: training + inference + agent dev + chip diplomacy</li><li>AI Agent "computer control" moves from experiment to mainstream</li><li>$1T AI hardware market signals no slowdown in infrastructure investment</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>GTC 2026's real message isn't the trillion dollars — it's that AI is transitioning from "a tool you use" to "an employee that works for you," and the infrastructure for this transition is being built at trillion-dollar scale.</strong></p><p>NVIDIA's Groq 3 acquisition completes a monopoly play across training AND inference. GPT-5.4's computer control + NemoClaw's agent platform = a complete "AI autonomous work" stack. When spreadsheet modeling accuracy jumps from 68.4% to 87.3%, that's not an academic benchmark — it means an AI agent now outperforms most junior analysts. <strong>H2 2026 prediction: we'll see the first wave of "AI Agent replaces junior white-collar roles" layoff news. Not because AI is smarter than humans, but because it's cheaper, faster, tireless — and NVIDIA is making it cheaper to run every quarter.</strong></p></div>"""
    },
    "cover": images.get("cnbc_gtc", "") or "https://image.cnbcfm.com/api/v1/image/108116029-1742248107CP_NVIDIA-GTC-2026_0112.jpg",
    "sources": [
        {
            "title": {"zh": "CNBC: NVIDIA GTC 2026 Jensen Huang 主题演讲", "en": "CNBC: NVIDIA GTC 2026 Jensen Huang Keynote"},
            "url": "https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html",
            "image": images.get("cnbc_gtc", "")
        },
        {
            "title": {"zh": "Tom's Hardware: NVIDIA Groq 3 LPU 加入 Rubin 平台", "en": "Tom's Hardware: NVIDIA Groq 3 LPU Joins Rubin Platform"},
            "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-groq-3-lpu-and-groq-lpx-racks-join-rubin-platform-at-gtc-sram-packed-accelerator-boosts-every-layer-of-the-ai-model-on-every-token",
            "image": ""
        },
        {
            "title": {"zh": "OpenAI 官方: 介绍 GPT-5.4", "en": "OpenAI: Introducing GPT-5.4"},
            "url": "https://openai.com/index/introducing-gpt-5-4/",
            "image": images.get("gpt54", "")
        },
        {
            "title": {"zh": "Yahoo Finance: NVIDIA 发布 NemoClaw AI Agent 平台", "en": "Yahoo Finance: NVIDIA Launches NemoClaw AI Agent Platform"},
            "url": "https://finance.yahoo.com/news/nvidia-launches-nemoclaw-platform-for-ai-agents-200851962.html",
            "image": images.get("nemoclaw", "")
        }
    ]
}

# Load existing issues and prepend
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

issues.insert(0, tech_issue)
issues.insert(0, design_issue)

with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Inserted 2 new issues (design + tech) for 2026-03-19. Total: {len(issues)} issues.")
