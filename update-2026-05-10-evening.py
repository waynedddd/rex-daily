#!/usr/bin/env python3
"""Rex Daily Digest - 2026-05-10 Evening Edition"""
import json, ssl, urllib.request, re, sys, os

ssl._create_default_https_context = ssl._create_unverified_context

def get_og_image(url):
    """Fetch og:image from a URL."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")[:50000]
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
        return m.group(1) if m else ""
    except Exception:
        return ""

# Define new issues
new_issues = [
    {
        "date": "2026-05-10",
        "section": "design",
        "title": {
            "zh": "Andy Budd 断言「设计师峰值已过」+ aivancity 发布 2026 生成式 AI 设计工具全景 + 超半数设计师担忧 AI 影响设计质量——当速度与品质的矛盾成为行业主旋律",
            "en": "Andy Budd Declares 'Peak Designer' Has Passed + aivancity Maps the 2026 Generative AI Design Landscape + Over Half of Designers Worry About AI's Impact on Quality — When Speed vs. Craft Becomes the Industry's Central Tension"
        },
        "content": {
            "zh": """<h3>📌 AI × 设计</h3><ul><li><strong>Andy Budd 发文：AI 不会「杀死设计」，但我们已经过了「设计师峰值」——未来 10 年设计师需求量将持续下降</strong> — 知名设计领袖 Andy Budd（Clearleft 创始人）在 3 月发布的长文持续引发行业讨论。他的核心观点：AI 不会在短期内消灭设计职业，但「peak designer」已经在几年前到来。未来 10 年，设计师总量会缩减，留下来的人需要从执行层转向策略层——<strong>从「pixel-pusher」变成「curator and strategist」</strong>。他特别强调：当 AI 让内容变得无限时，「品味、策展和手艺」才是真正的差异化因素。<br><small>来源：<a href="https://andybudd.com/archives/2026/03/how-ai-will-affect-the-design-industry">Andy Budd</a></small></li><li><strong>aivancity 发布 2026 年 UI/UX 生成式 AI 工具全景报告：界面设计 AI 已成创意 AI 最具战略价值的细分领域</strong> — 法国 AI 商学院 aivancity 的报告指出，AI 驱动的界面设计和用户体验已经成为创意 AI 中最具战略意义的细分市场。报告覆盖了从 Figma AI、UX Pilot 到 Galileo AI 的全链路工具，并指出一个关键趋势：<strong>prompt engineering 正在从开发者技能变成设计师核心技能</strong>。「弱 prompt：'设计一个 dashboard'。强 prompt：'设计一个面向可再生能源初创企业的暗色模式 dashboard，聚焦实时数据可视化'」——prompt 质量直接决定 AI 输出质量。<br><small>来源：<a href="https://aivancity.ai/en/blog/ui-ux-notre-selection-des-meilleurs-outils-ia-generatives-de-2026/">aivancity</a></small></li><li><strong>Designlab 调研：超过半数设计师担忧 AI 对设计质量的负面影响——速度 vs 品质的矛盾浮出水面</strong> — Designlab 2026 年度调研揭示了一个被 AI 乐观叙事掩盖的事实：虽然 AI 采用在加速，但<strong>超过 50% 的受访设计师表示担忧 AI 对设计质量的影响</strong>。这与 Figma 报告中「91% 说 AI 提升了质量」的数据形成了微妙的对比。差异可能在于：Figma 调研的是已经深度使用 AI 的设计师，而 Designlab 覆盖了更广泛的群体——包括那些看到 AI 生成的千篇一律界面后心生警惕的人。<br><small>来源：<a href="https://designlab.com/blog/ai-in-ux-product-design-trends-2026">Designlab</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>「Peak Designer」论成为行业共识的雏形</strong>：从 Andy Budd 到 NoGood，越来越多的声音认为设计师总量将缩减，但单个设计师的战略价值在上升</li><li><strong>Prompt Engineering 成为设计师新核心技能</strong>：AI 工具的输出质量取决于 prompt 质量——「会问问题」比「会画界面」更重要</li><li><strong>「速度 vs 品质」成为 2026 设计行业核心矛盾</strong>：AI 带来了前所未有的速度，但超半数设计师担忧这种速度正在牺牲品质</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Andy Budd 说「peak designer」已经过了，Designlab 说超半数设计师担忧质量下降，aivancity 说 prompt engineering 是新核心技能。把这三条信息放在一起，你会看到一幅清晰但不太舒服的画面：设计行业正在经历一场「中间层塌陷」。</strong></p><p>什么是中间层？就是那些「技术够用但不出众、有经验但没有独特视角」的设计师。在 AI 之前，这个群体是行业的中坚力量——他们按时交付、质量稳定、是团队里的可靠螺丝钉。但 AI 正在从两个方向挤压他们：<strong>从下方，AI 工具让初级设计师甚至非设计师能快速产出「80 分」的设计；从上方，顶尖设计师用 AI 放大了自己的产出能力，一个人能干三个人的活。</strong>中间层的生存空间在急剧缩小。</p><p>Designlab 的数据尤其值得关注：超过 50% 的设计师担忧 AI 对设计质量的影响。这和 Figma 的「91% 说 AI 提升了质量」并不矛盾——它们描述的是同一枚硬币的两面。<strong>对于那些有清晰设计判断力的设计师来说，AI 确实提升了质量，因为它加速了执行，让他们有更多时间思考。但对于那些依赖「做的过程」来找到设计方向的设计师来说，AI 生成的速度反而剥夺了他们的思考空间。</strong>你见过那种情况吧？一个设计师用 AI 在 10 分钟内生成了 20 个方案，然后花了两个小时在 20 个差不多的方案里纠结——这不是效率提升，这是决策瘫痪。</p><p>aivancity 关于 prompt engineering 的观点指向了一个更深层的变化：<strong>设计师的核心能力正在从「手艺」转向「表达」</strong>。一个好的 prompt 需要你清楚地知道自己要什么——目标用户是谁、使用场景是什么、视觉调性应该怎样、关键交互逻辑是什么。这些本质上是设计思维的能力，但它们曾经被隐藏在「画图」的过程中——你在 Figma 里推像素的时候其实在思考这些问题。现在 AI 要求你在动手之前就把这些想清楚并表达出来。<strong>这对「边做边想」型设计师是巨大的挑战，但对「先想后做」型设计师是巨大的机遇。</strong></p><p><strong>我的预测：2026 年底之前，我们会看到设计行业出现明确的分层——顶部是「设计策略师」（定义方向、用 AI 验证、用手艺做差异化），底部是「AI 设计操作员」（用 AI 工具批量产出标准化设计），中间是越来越薄的「传统设计师」层。Andy Budd 是对的：peak designer 确实已经过了。但 peak design value 可能才刚刚开始——当人人都能做出「还行」的设计时，「真正好」的设计的溢价会指数级上升。就像 Instagram 让人人都能拍照，但顶级摄影师的价格反而涨了。</strong></p></div>""",
            "en": """<h3>📌 AI × Design</h3><ul><li><strong>Andy Budd: AI Won't Kill Design, But We've Already Passed 'Peak Designer' — Designer Demand Will Decline Over the Next Decade</strong> — Renowned design leader Andy Budd (Clearleft founder) argues that while AI won't eliminate design as a profession, 'peak designer' arrived years ago. Future designers must shift from execution to strategy — <strong>from pixel-pushers to curators and strategists</strong>. When AI makes content infinite, 'taste, curation, and craft become the real differentiators.'<br><small>Source: <a href="https://andybudd.com/archives/2026/03/how-ai-will-affect-the-design-industry">Andy Budd</a></small></li><li><strong>aivancity Publishes 2026 Generative AI Design Tools Landscape: UI/UX AI Is the Most Strategic Creative AI Segment</strong> — French AI business school aivancity's report identifies AI-powered interface design as the most strategic segment of creative AI. Key finding: <strong>prompt engineering is transitioning from a developer skill to a core design skill</strong>. Prompt quality directly determines AI output quality.<br><small>Source: <a href="https://aivancity.ai/en/blog/ui-ux-notre-selection-des-meilleurs-outils-ia-generatives-de-2026/">aivancity</a></small></li><li><strong>Designlab Survey: Over Half of Designers Worry About AI's Negative Impact on Design Quality</strong> — While AI adoption accelerates, <strong>over 50% of surveyed designers express concern about AI's impact on design quality</strong>. This contrasts subtly with Figma's '91% say AI improves quality' — the difference likely reflects that Figma surveyed deep AI adopters, while Designlab captured a broader group including those alarmed by cookie-cutter AI-generated interfaces.<br><small>Source: <a href="https://designlab.com/blog/ai-in-ux-product-design-trends-2026">Designlab</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>'Peak Designer' Thesis Gaining Traction</strong>: From Andy Budd to NoGood, growing consensus that designer volume will shrink while individual strategic value rises</li><li><strong>Prompt Engineering as Core Design Skill</strong>: AI output quality depends on prompt quality — 'knowing what to ask' matters more than 'knowing how to draw'</li><li><strong>Speed vs. Craft: 2026's Central Design Tension</strong>: AI delivers unprecedented speed, but over half of designers worry it's sacrificing quality</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>Andy Budd says peak designer has passed. Designlab says over half worry about quality decline. aivancity says prompt engineering is the new core skill. Together, they paint a clear but uncomfortable picture: design is experiencing a 'middle-layer collapse.'</strong></p><p>The middle layer: designers who are 'competent but not exceptional, experienced but without a unique perspective.' Pre-AI, they were the industry backbone — reliable, consistent, on-time. But AI squeezes them from both directions: <strong>from below, AI tools let juniors and non-designers produce '80-point' designs quickly; from above, top designers use AI to multiply their output, one person doing three people's work.</strong></p><p>Designlab's data deserves attention: over 50% worry about quality impact. This doesn't contradict Figma's '91% say quality improved' — they describe two sides of the same coin. <strong>For designers with clear judgment, AI genuinely improves quality by accelerating execution and freeing time for thinking. But for those who find design direction through the making process, AI's generation speed actually strips away their thinking space.</strong> You've seen it: a designer generates 20 options in 10 minutes, then spends two hours paralyzed choosing between 20 similar variants. That's not efficiency — it's decision paralysis.</p><p><strong>My prediction: by late 2026, design will show clear stratification — 'design strategists' at the top (defining direction, validating with AI, differentiating through craft), 'AI design operators' at the bottom (batch-producing standardized designs with AI tools), and an increasingly thin 'traditional designer' layer in between. Andy Budd is right: peak designer has passed. But peak design value may just be beginning — when everyone can produce 'decent' design, the premium for 'truly great' design grows exponentially. Like Instagram made everyone a photographer, but top photographers' rates went up.</strong></p></div>"""
        },
        "cover": "",
        "sources": [
            {
                "url": "https://andybudd.com/archives/2026/03/how-ai-will-affect-the-design-industry",
                "title": {
                    "zh": "Andy Budd：AI 将如何影响设计行业",
                    "en": "Andy Budd: How AI Will Affect the Design Industry"
                },
                "image": ""
            },
            {
                "url": "https://aivancity.ai/en/blog/ui-ux-notre-selection-des-meilleurs-outils-ia-generatives-de-2026/",
                "title": {
                    "zh": "aivancity：2026 年最佳 UI/UX 生成式 AI 工具精选",
                    "en": "aivancity: Our Selection of the Best Generative AI Tools for UI/UX in 2026"
                },
                "image": ""
            },
            {
                "url": "https://designlab.com/blog/ai-in-ux-product-design-trends-2026",
                "title": {
                    "zh": "Designlab：2026 年 UX 与产品设计中的 AI 现状",
                    "en": "Designlab: The State of AI in UX & Product Design 2026"
                },
                "image": ""
            }
        ]
    },
    {
        "date": "2026-05-10",
        "section": "tech",
        "title": {
            "zh": "Anthropic 单季增长 80 倍后向 Musk「低头」租 GPU + Semafor 宣称「token 正在接管经济」+ AI 泡沫论遭遇最强反驳——当昨天的对手变成今天的房东，AI 算力争夺战进入新阶段",
            "en": "Anthropic's 80x Quarterly Growth Forces It to Rent GPUs from Musk + Semafor Declares 'Tokens Are Taking Over the Economy' + The AI Bubble Thesis Faces Its Strongest Rebuttal — When Yesterday's Enemy Becomes Today's Landlord, the AI Compute War Enters a New Phase"
        },
        "content": {
            "zh": """<h3>📌 AI × 科技</h3><ul><li><strong>Anthropic 单季度营收增长 80 倍，不得不向 Elon Musk 的 SpaceX 租用 22 万块 GPU——「叫过你 evil 的人现在付你房租」</strong> — Fortune 报道（5月8日），Anthropic 的营收经历了史无前例的 80 倍季度增长，导致算力严重不足。讽刺的是，三个月前 Musk 还公开称 Anthropic 为「evil」，现在 Anthropic 却不得不向 SpaceX 的 Colossus 数据中心（22 万块 NVIDIA GPU、300MW 算力）签下租约。Forbes 分析指出，这笔交易的本质是：<strong>双方都急需对方拥有的东西——Anthropic 需要算力，SpaceX 的 Grok 没有填满 Colossus 的产能</strong>。分析师估计这笔交易每年可为 SpaceX 带来 30-40 亿美元收入。<br><small>来源：<a href="https://fortune.com/2026/05/08/anthropic-80fold-growth-quarter-renting-elon-musk-data-center/">Fortune</a> / <a href="https://www.forbes.com/sites/jonmarkman/2026/05/06/anthropic-just-signed-a-compute-deal-with-elon-musks-spacex/">Forbes</a></small></li><li><strong>Semafor 深度分析：Anthropic-SpaceX 交易标志着「token 正在接管经济」——算力正在成为新时代的石油</strong> — Semafor 科技编辑 Reed Albergotti（5月8日）认为，这笔交易的意义远超双方利益交换。它揭示了一个结构性变化：<strong>AI 推理产生的 token 正在成为一种新的经济基础单位</strong>。就像石油驱动了 20 世纪的工业经济，token（以及产生 token 所需的算力）正在成为 21 世纪数字经济的驱动力。当一家 AI 公司愿意向自己的公开敌人低头只为获得更多 GPU，你就知道算力匮乏已经到了什么程度。<br><small>来源：<a href="https://www.semafor.com/article/05/08/2026/anthropic-spacex-compute-deal-shows-how-tokens-are-taking-over-the-economy">Semafor</a></small></li><li><strong>The Atlantic：也许 AI 根本不是泡沫——Anthropic 的增长数据让「AI 泡沫论」遭遇最强反驳</strong> — The Atlantic（5月刊）发表长文，以 Anthropic 的爆炸式增长为切入点重新审视 AI 泡沫论。文章指出：<strong>软件开发者正在大规模采用 AI 工具并报告天文数字的生产力提升，关于「美国建了太多数据中心」的担忧在需求面前显得苍白。</strong>与 2000 年互联网泡沫不同，今天的 AI 公司有真实且快速增长的营收支撑。但文章也警告：营收增长不等于盈利——Anthropic 的 GPU 租赁成本可能会吞噬大部分利润。<br><small>来源：<a href="https://www.theatlantic.com/economy/2026/05/ai-bubble-revenue-anthropic/687022/">The Atlantic</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>算力成为 AI 时代的「石油」</strong>：Anthropic 向竞争对手租 GPU 的事实证明算力匮乏比商业竞争更紧迫</li><li><strong>「Token 经济」正在成形</strong>：AI 推理产生的 token 正在成为新的经济基础单位，算力基础设施是新时代的炼油厂</li><li><strong>AI 泡沫论退潮</strong>：当一家公司单季增长 80 倍时，「泡沫」的叙事需要更有力的证据</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>Elon Musk 三个月前叫 Anthropic「evil」，现在每年从它手里收 30-40 亿美元房租。如果你想要一张图来理解 2026 年 AI 行业的真实状态，这就是那张图：意识形态让位于算力经济学。</strong></p><p>让我拆解一下为什么这笔交易是今年最重要的 AI 行业事件之一。Anthropic 单季增长 80 倍——不是用户增长，是<strong>营收增长</strong>。这个数字意味着什么？意味着 Claude 不再只是开发者的玩具，它正在被企业级客户大规模采购。但增长越快，算力缺口越大。Anthropic 面临的困境是：<strong>客户来得太快，GPU 不够用。</strong>这就是为什么它愿意向 Musk 低头——不是因为矛盾化解了，而是因为物理定律比面子重要。Colossus 有 22 万块 GPU 和 300MW 的电力，而 Grok 没有用满。这是一笔纯粹的经济理性交易：闲置的算力和饥渴的需求之间的套利。</p><p>Semafor 关于「token 接管经济」的分析值得认真对待。想想看：<strong>每一次你和 ChatGPT 对话、每一次 Claude 帮你写代码、每一次 Gemini 分析一张图片，背后都在消耗算力产生 token。当这些交互从「偶尔使用」变成「每天每小时都在用」时，token 的总消耗量会以指数级增长。</strong>谁控制了产生 token 的算力，谁就控制了这个新经济的基础设施。这就是为什么 NVIDIA 市值能撑在 3 万亿以上，为什么 Microsoft、Google、Amazon 在疯狂建数据中心，为什么 Musk 即使嘴上骂 Anthropic 也愿意做生意。<strong>算力就是新石油，GPU 集群就是新炼油厂，token 就是新汽油。</strong></p><p>The Atlantic 关于「AI 不是泡沫」的文章提出了一个关键区分：<strong>2000 年的互联网公司有用户但没有营收，2026 年的 AI 公司有真实且爆炸式增长的营收。</strong>但文章也指出了一个被忽视的风险：营收增长不等于盈利。Anthropic 增长 80 倍的同时，它的 GPU 租赁成本也在暴涨——向 SpaceX 租 22 万块 GPU 一年可能要花 30-40 亿美元。如果 Anthropic 的毛利率被算力成本吃掉，那它本质上是在用投资人的钱补贴企业客户使用 AI。这和 Uber 早期用补贴买增长的模式惊人地相似。</p><p><strong>把今天的 design 板块和 tech 板块联系起来看，你会发现一个有趣的对称性：设计行业在经历「中间层塌陷」（普通设计师被挤压），AI 行业在经历「中间层膨胀」（算力需求的中间环节——GPU、数据中心、电力——在疯狂扩张）。设计师的困境是「我的技能还值钱吗」，AI 公司的困境是「我能租到足够的 GPU 吗」。两个问题看似无关，但根源相同：AI 正在重新分配整个技术-创意产业链上的价值。在这条链上，越靠近「不可替代的稀缺资源」（无论是人类的审美判断力还是物理的算力），你的价值越高。中间的一切都在被压缩。</strong></p></div>""",
            "en": """<h3>📌 AI × Tech</h3><ul><li><strong>Anthropic's Revenue Grew 80x in One Quarter, Forcing It to Rent 220,000 GPUs from Elon Musk's SpaceX — 'The Man Who Called You Evil Now Pays Your Rent'</strong> — Fortune reports (May 8) that Anthropic's unprecedented 80x quarterly revenue growth created a severe compute deficit. Ironically, three months after Musk publicly called Anthropic 'evil,' the company signed a lease for SpaceX's Colossus data center (220,000 NVIDIA GPUs, 300MW). <strong>Both sides desperately needed what the other had — Anthropic needed compute, SpaceX's Grok hadn't filled Colossus.</strong> Analysts estimate the deal could bring SpaceX $3-4 billion annually.<br><small>Source: <a href="https://fortune.com/2026/05/08/anthropic-80fold-growth-quarter-renting-elon-musk-data-center/">Fortune</a> / <a href="https://www.forbes.com/sites/jonmarkman/2026/05/06/anthropic-just-signed-a-compute-deal-with-elon-musks-spacex/">Forbes</a></small></li><li><strong>Semafor Analysis: Anthropic-SpaceX Deal Shows 'Tokens Are Taking Over the Economy' — Compute Is the New Oil</strong> — Semafor tech editor Reed Albergotti (May 8) argues the deal's significance transcends the parties involved: <strong>AI inference tokens are becoming a new fundamental economic unit</strong>. Like oil powered 20th-century industrial economies, tokens (and the compute to produce them) are powering the 21st-century digital economy.<br><small>Source: <a href="https://www.semafor.com/article/05/08/2026/anthropic-spacex-compute-deal-shows-how-tokens-are-taking-over-the-economy">Semafor</a></small></li><li><strong>The Atlantic: Maybe AI Isn't a Bubble After All — Anthropic's Growth Data Delivers the Strongest Rebuttal to the AI Bubble Thesis</strong> — The Atlantic (May) examines how Anthropic's explosive growth challenges the bubble narrative. <strong>Software developers are adopting AI tools en masse with astronomical productivity gains; concerns about over-building data centers look pale against actual demand.</strong> But the article warns: revenue growth ≠ profitability — GPU rental costs may consume most profits.<br><small>Source: <a href="https://www.theatlantic.com/economy/2026/05/ai-bubble-revenue-anthropic/687022/">The Atlantic</a></small></li></ul><h3>🔄 Trends</h3><ul><li><strong>Compute as AI's 'Oil'</strong>: Anthropic renting GPUs from a competitor proves compute scarcity is more pressing than commercial rivalry</li><li><strong>'Token Economy' Taking Shape</strong>: AI inference tokens are becoming a new economic fundamental; compute infrastructure is the new refinery</li><li><strong>AI Bubble Thesis Retreating</strong>: When a company grows 80x in one quarter, the 'bubble' narrative needs stronger evidence</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>Elon Musk called Anthropic 'evil' three months ago. Now he collects $3-4 billion a year in rent from them. If you want one image to understand AI in 2026, this is it: ideology yields to compute economics.</strong></p><p>Anthropic's 80x quarterly growth isn't user growth — it's <strong>revenue growth</strong>. Claude is being purchased at enterprise scale. But faster growth means a bigger compute gap. Anthropic's dilemma: <strong>customers arriving too fast, GPUs not enough.</strong> That's why it swallowed its pride — physics matters more than face. Colossus has 220,000 GPUs and 300MW sitting underutilized because Grok couldn't fill it. Pure economic arbitrage between idle capacity and hungry demand.</p><p>Semafor's 'tokens taking over the economy' analysis deserves serious attention. <strong>Every ChatGPT conversation, every Claude coding session, every Gemini image analysis consumes compute to produce tokens. When these interactions shift from occasional to hourly, total token consumption grows exponentially.</strong> Whoever controls the compute that produces tokens controls this new economy's infrastructure. That's why NVIDIA stays above $3 trillion, why Microsoft/Google/Amazon are building data centers frantically, and why Musk does business with companies he publicly insults. <strong>Compute is the new oil, GPU clusters are the new refineries, tokens are the new gasoline.</strong></p><p><strong>Connecting today's design and tech sections reveals an interesting symmetry: the design industry is experiencing 'middle-layer collapse' (average designers squeezed out), while the AI industry is experiencing 'middle-layer expansion' (compute infrastructure — GPUs, data centers, power — expanding frantically). Designers ask 'are my skills still valuable?' AI companies ask 'can I rent enough GPUs?' Different questions, same root cause: AI is redistributing value across the entire tech-creative supply chain. The closer you are to irreplaceable scarce resources — whether human aesthetic judgment or physical compute — the higher your value. Everything in between is being compressed.</strong></p></div>"""
        },
        "cover": "",
        "sources": [
            {
                "url": "https://fortune.com/2026/05/08/anthropic-80fold-growth-quarter-renting-elon-musk-data-center/",
                "title": {
                    "zh": "Anthropic 单季增长 80 倍，现在要租 Elon Musk 的数据中心",
                    "en": "Anthropic Grew 80-Fold in a Single Quarter. Now It's Renting Elon Musk's Data Center"
                },
                "image": ""
            },
            {
                "url": "https://www.forbes.com/sites/jonmarkman/2026/05/06/anthropic-just-signed-a-compute-deal-with-elon-musks-spacex/",
                "title": {
                    "zh": "Anthropic 与 Elon Musk 的 SpaceX 签署算力租赁协议",
                    "en": "Anthropic Just Signed a Compute Deal with Elon Musk's SpaceX"
                },
                "image": ""
            },
            {
                "url": "https://www.semafor.com/article/05/08/2026/anthropic-spacex-compute-deal-shows-how-tokens-are-taking-over-the-economy",
                "title": {
                    "zh": "Semafor：Anthropic-SpaceX 算力交易揭示 token 正在接管经济",
                    "en": "Semafor: Anthropic-SpaceX Compute Deal Shows How Tokens Are Taking Over the Economy"
                },
                "image": ""
            },
            {
                "url": "https://www.theatlantic.com/economy/2026/05/ai-bubble-revenue-anthropic/687022/",
                "title": {
                    "zh": "The Atlantic：也许 AI 根本不是泡沫",
                    "en": "The Atlantic: Maybe AI Isn't a Bubble After All"
                },
                "image": ""
            }
        ]
    }
]

# Fetch og:image for all sources and covers
for issue in new_issues:
    for src in issue["sources"]:
        if not src["image"]:
            img = get_og_image(src["url"])
            src["image"] = img
            print(f"  og:image for {src['url']}: {img[:80] if img else '(none)'}")
    if not issue["cover"] and issue["sources"]:
        # Use first source's image as cover
        for src in issue["sources"]:
            if src["image"] and src["image"].startswith("http"):
                issue["cover"] = src["image"]
                break

# Load existing issues
issues_path = os.path.join(os.path.dirname(__file__), "issues.json")
with open(issues_path, "r", encoding="utf-8") as f:
    existing = json.load(f)

# Prepend new issues
updated = new_issues + existing

# Write back
with open(issues_path, "w", encoding="utf-8") as f:
    json.dump(updated, f, ensure_ascii=False, indent=2)

print(f"\nDone! Added {len(new_issues)} issues. Total: {len(updated)}")
