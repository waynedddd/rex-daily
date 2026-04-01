# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Rex Daily Update - 2026-04-01 Evening"""
import json
import urllib.request
import re
import ssl

def get_og_image(url):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            html = resp.read().decode("utf-8", errors="ignore")[:50000]
            m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
            if not m:
                m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
            return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images
design_urls = [
    "https://techcrunch.com/2026/03/05/exclusive-luma-launches-creative-ai-agents-powered-by-its-new-unified-intelligence-models/",
    "https://www.ign.com/articles/we-should-have-clearly-disclosed-our-use-of-ai-crimson-desert-dev-launches-comprehensive-audit-of-all-in-game-assets-after-ai-generated-art-was-unintentionally-included-in-final-release",
    "https://www.pcgamer.com/gaming-industry/capcom-says-it-will-not-implement-assets-generated-by-ai-into-our-game-content-but-still-plans-to-use-ai-to-enhance-efficiency-and-boost-productivity-in-game-development/",
]
tech_urls = [
    "https://www.cnbc.com/2026/04/01/iran-irgc-nvidia-appple-attack-threat.html",
    "https://www.engadget.com/big-tech/iran-threatens-imminent-attacks-on-us-tech-companies-in-the-middle-east-184841155.html",
    "https://techcrunch.com/2026/03/28/anthropics-claude-popularity-with-paying-consumers-is-skyrocketing/",
]

print("Fetching og:images...")
design_images = [get_og_image(u) for u in design_urls]
tech_images = [get_og_image(u) for u in tech_urls]
print(f"Design images: {design_images}")
print(f"Tech images: {tech_images}")

design_issue = {
    "date": "2026-04-01",
    "section": "design",
    "title": {
        "zh": "Luma Agents 重新定义创意生产：统一智能取代碎片化工具链 · Crimson Desert AI 素材丑闻引发行业审计潮 · Capcom 划出红线：AI 可提效但不可替代创意资产",
        "en": "Luma Agents Redefine Creative Production with Unified Intelligence · Crimson Desert AI Art Scandal Triggers Industry Audits · Capcom Draws the Line: AI for Efficiency, Not Assets"
    },
    "content": {
        "zh": "<h3>📌 AI × 设计</h3><ul><li><strong>Luma Agents 发布：统一智能架构颠覆创意工作流</strong> — Luma AI 于 3 月 5 日发布 Luma Agents，基于全新的「统一智能」（Unified Intelligence）架构，能够端到端处理文本、图像、视频和音频的创意工作。<strong>核心突破：Uni-1 模型将语言、空间、时间和视觉逻辑统一在一个模型中，不再是「语言模型 + 视觉模型 + 视频模型」的拼凑。</strong>首批企业合作伙伴包括 Publicis Groupe 和 Serviceplan Group。Luma CEO Amit Jain 描述其为「用语言思考，用像素想象和渲染」。与 Figma MCP 的「AI 在设计系统内干活」不同，Luma Agents 走的是「AI 全栈创意执行」路线——从 brief 到最终交付，Agent 全程掌控。<br><small>来源：<a href=\"https://techcrunch.com/2026/03/05/exclusive-luma-launches-creative-ai-agents-powered-by-its-new-unified-intelligence-models/\">TechCrunch</a>、<a href=\"https://www.businesswire.com/news/home/20260305354123/en/Luma-Launches-Luma-Agents-Powered-by-Unified-Intelligence-for-Creative-Work\">BusinessWire</a></small></li><li><strong>Crimson Desert AI 素材丑闻：Pearl Abyss 道歉并启动全面审计</strong> — 开放世界 RPG《Crimson Desert》上线后，玩家迅速发现游戏内多处画作使用了 AI 生成素材。开发商 Pearl Abyss 承认这些素材是「早期开发阶段用于快速探索色调和氛围」，被「错误地保留在了最终版本中」。<strong>此举违反了 Steam 的 AI 内容政策（要求披露生成式 AI 使用），在 Steam 上获得了「褒贬不一」的评价。</strong>Pearl Abyss 已发布补丁替换 AI 素材，并承诺对所有游戏内资产进行全面审计。<br><small>来源：<a href=\"https://www.ign.com/articles/we-should-have-clearly-disclosed-our-use-of-ai-crimson-desert-dev-launches-comprehensive-audit-of-all-in-game-assets-after-ai-generated-art-was-unintentionally-included-in-final-release\">IGN</a>、<a href=\"https://gameinformer.com/2026/03/23/crimson-desert-apologizes-for-using-ai-art-and-issues-first-big-patch\">Game Informer</a></small></li><li><strong>Capcom 划出明确红线：不使用 AI 生成的游戏资产</strong> — 在 Crimson Desert 事件的行业背景下，Capcom 发表声明：「我们不会将 AI 生成的资产实装到游戏内容中」，但会使用 AI 来「提升效率和生产力」。<strong>这是大型游戏公司中最明确的 AI 使用边界声明之一——区分了「AI 辅助工作流」和「AI 替代创意产出」。</strong><br><small>来源：<a href=\"https://www.pcgamer.com/gaming-industry/capcom-says-it-will-not-implement-assets-generated-by-ai-into-our-game-content-but-still-plans-to-use-ai-to-enhance-efficiency-and-boost-productivity-in-game-development/\">PC Gamer</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>创意 AI 的两条路线正在分化</strong>：Luma 走「全栈替代」，Figma 走「系统内协作」</li><li><strong>游戏行业对 AI 素材的容忍度归零</strong>：玩家社区成为最严格的 AI 审计员</li><li><strong>「AI 辅助」vs「AI 替代」的边界正在被明确划定</strong>：Capcom 的声明可能成为行业模板</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天这三条新闻完美地呈现了 AI 在创意产业中的根本张力：技术能力在飞速进化，但社会接受度的边界比大多数人想象的更清晰、更严苛。</strong></p><p>先看 Luma Agents。Uni-1 的「统一智能」概念——把语言、视觉、时空逻辑塞进同一个模型——听起来很诱人，但我们得冷静看这件事。<strong>创意行业的核心问题从来不是「能不能生成」，而是「能不能控制」。</strong>广告公司用 AI 生成 100 个方案不难，难的是让第 101 个方案精准匹配客户的品牌调性、历史语境和审美偏好。Luma 说「从 brief 到最终交付，Agent 全程掌控」——这在高度标准化的内容（社交媒体素材、Banner 广告）上可能成立，但在需要人类判断力的高价值创意（品牌战略、叙事设计、体验设计）上，目前还是一句漂亮的营销话术。Publicis 和 Serviceplan 作为首批合作伙伴，说明广告行业正在认真评估这条路径——但注意，这些代理商的核心利润来自策略层，不是执行层。它们采用 Luma 恰恰说明：<strong>执行层的压缩是真的在发生，速度可能比我们想的更快。</strong></p><p>把 Luma 和今早报道的 Figma MCP 放在一起看，创意 AI 正在分化成两条截然不同的路线：Figma 说「AI 在你的系统里干活，你定规则」；Luma 说「AI 替你从头干到尾」。这不是谁对谁错的问题，<strong>而是不同创意工作的本质决定了适合哪条路径。</strong>产品设计需要系统一致性和团队协作——Figma MCP 模式；营销内容需要速度和规模——Luma 模式。未来大概率是两种模式并存，但设计师的选择将决定他们在价值链上的位置。</p><p>再看 Crimson Desert 事件。25 万同时在线玩家，混合评价，核心导火索居然是几张 AI 生成的画——这在两年前不可想象。<strong>这说明什么？消费者对 AI 生成内容的「鉴伪能力」和「零容忍态度」都在急速进化。</strong>Pearl Abyss 的解释是「早期探索阶段的素材被误留」——这可能是真的，但这恰恰暴露了一个系统性风险：在 AI 工具已经渗透到开发流程每个环节的今天，「无意中混入 AI 素材」不是个案，而是必然会发生的事。Steam 的 AI 内容披露政策现在有了第一个高调的执法案例。</p><p>Capcom 的声明是最值得玩味的。它说的不是「我们不用 AI」，而是「我们不用 AI 生成的资产，但用 AI 提效」。<strong>这条线划得非常精准，也非常政治正确——既不得罪反 AI 的玩家群体，又不放弃 AI 带来的效率红利。</strong>我预测这会成为大型游戏公司的标准话术模板。但问题是：「辅助」和「替代」的边界到底在哪里？AI 帮你画了概念草图，美术师在上面修改——这算「AI 辅助」还是「AI 生成资产」？当这条线越来越模糊时，我们可能会看到更多类似 Crimson Desert 的争议。</p><p><strong>大胆预测：2026 年底前，主流游戏平台（Steam、PS Store、Xbox Store）都会强制要求详细的 AI 使用声明，玩家将获得类似「食品成分表」的 AI 透明度标签。</strong>创意行业正在经历一场关于「什么是真的」的信任危机——解决方案不是禁止 AI，而是让 AI 的使用变得透明和可追溯。</p></div>",
        "en": "<h3>📌 AI × Design</h3><ul><li><strong>Luma Agents Launch: Unified Intelligence Architecture Disrupts Creative Workflows</strong> — Luma AI launched Luma Agents on March 5, built on a new Unified Intelligence architecture capable of end-to-end creative work across text, image, video, and audio. <strong>Key breakthrough: the Uni-1 model unifies language, space, time, and visual logic in one model—no more stitching together separate language, vision, and video models.</strong> Launch partners include Publicis Groupe and Serviceplan Group. Unlike Figma MCP's \"AI working within design systems,\" Luma Agents pursue \"full-stack creative execution\" from brief to final delivery.<br><small>Source: <a href=\"https://techcrunch.com/2026/03/05/exclusive-luma-launches-creative-ai-agents-powered-by-its-new-unified-intelligence-models/\">TechCrunch</a>, <a href=\"https://www.businesswire.com/news/home/20260305354123/en/Luma-Launches-Luma-Agents-Powered-by-Unified-Intelligence-for-Creative-Work\">BusinessWire</a></small></li><li><strong>Crimson Desert AI Art Scandal: Pearl Abyss Apologizes, Launches Full Audit</strong> — Players quickly discovered AI-generated artwork in the open-world RPG after launch. Pearl Abyss admitted the assets were from early development \"to rapidly explore tone and atmosphere\" and were \"erroneously left in the final game.\" <strong>This violated Steam's AI Content policy requiring disclosure, contributing to the game's \"mixed\" reviews despite 250K concurrent players.</strong><br><small>Source: <a href=\"https://www.ign.com/articles/we-should-have-clearly-disclosed-our-use-of-ai-crimson-desert-dev-launches-comprehensive-audit-of-all-in-game-assets-after-ai-generated-art-was-unintentionally-included-in-final-release\">IGN</a>, <a href=\"https://gameinformer.com/2026/03/23/crimson-desert-apologizes-for-using-ai-art-and-issues-first-big-patch\">Game Informer</a></small></li><li><strong>Capcom Draws a Clear Line: No AI-Generated Game Assets</strong> — Capcom stated it \"will not implement assets generated by AI into our game content\" but will use AI to \"enhance efficiency and boost productivity.\" <strong>One of the clearest AI usage boundary statements from a major game company—distinguishing \"AI-assisted workflows\" from \"AI-replaced creative output.\"</strong><br><small>Source: <a href=\"https://www.pcgamer.com/gaming-industry/capcom-says-it-will-not-implement-assets-generated-by-ai-into-our-game-content-but-still-plans-to-use-ai-to-enhance-efficiency-and-boost-productivity-in-game-development/\">PC Gamer</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Creative AI diverges into two paths: Luma's \"full-stack replacement\" vs Figma's \"in-system collaboration\"</li><li>Gaming industry's tolerance for AI assets hits zero: player communities become the strictest AI auditors</li><li>The \"AI-assisted\" vs \"AI-replaced\" boundary is being explicitly drawn: Capcom's statement may become the industry template</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>These three stories perfectly capture the fundamental tension of AI in creative industries: technical capability is evolving rapidly, but social acceptance boundaries are clearer and stricter than most assume.</strong> Luma's Uni-1 \"unified intelligence\" sounds compelling, but creative work's core challenge was never \"can we generate\" but \"can we control.\" The Publicis/Serviceplan partnerships signal execution-layer compression is real and accelerating. Compare Luma's \"AI does everything\" with this morning's Figma MCP \"AI works within your system\"—two diverging paths for different creative needs. The Crimson Desert scandal shows consumers' AI detection skills and zero-tolerance attitudes are evolving fast. Pearl Abyss's \"accidental inclusion\" excuse exposes a systemic risk: AI contamination of creative pipelines is inevitable, not exceptional. Capcom's precise distinction—\"AI for efficiency, not assets\"—will become the industry's standard PR template. <strong>Prediction: by end of 2026, major gaming platforms will mandate detailed AI usage declarations, giving players \"ingredient label\" transparency for AI content.</strong></p></div>"
    },
    "cover": design_images[0] if design_images[0] else "https://techcrunch.com/wp-content/uploads/2026/03/Hero-2.png",
    "sources": [
        {
            "title": {"zh": "Luma 发布创意 AI Agent，基于统一智能模型", "en": "Luma Launches Creative AI Agents with Unified Intelligence"},
            "url": "https://techcrunch.com/2026/03/05/exclusive-luma-launches-creative-ai-agents-powered-by-its-new-unified-intelligence-models/",
            "image": design_images[0]
        },
        {
            "title": {"zh": "Crimson Desert 开发商道歉：AI 素材误留在正式版", "en": "Crimson Desert Dev Apologizes for AI Art Left in Final Release"},
            "url": "https://www.ign.com/articles/we-should-have-clearly-disclosed-our-use-of-ai-crimson-desert-dev-launches-comprehensive-audit-of-all-in-game-assets-after-ai-generated-art-was-unintentionally-included-in-final-release",
            "image": design_images[1]
        },
        {
            "title": {"zh": "Capcom：不会在游戏中使用 AI 生成资产", "en": "Capcom: Won't Use AI-Generated Assets in Games"},
            "url": "https://www.pcgamer.com/gaming-industry/capcom-says-it-will-not-implement-assets-generated-by-ai-into-our-game-content-but-still-plans-to-use-ai-to-enhance-efficiency-and-boost-productivity-in-game-development/",
            "image": design_images[2]
        }
    ]
}

tech_issue = {
    "date": "2026-04-01",
    "section": "tech",
    "title": {
        "zh": "伊朗 IRGC 威胁攻击 18 家美国科技巨头：AI 基础设施成地缘政治靶心 · Anthropic Claude 付费用户暴涨 · AI 网络安全攻防升级",
        "en": "Iran IRGC Threatens 18 US Tech Giants: AI Infrastructure Becomes Geopolitical Target · Anthropic Claude Paid Users Skyrocket · AI Cyber Risk Escalates"
    },
    "content": {
        "zh": "<h3>📌 AI × 科技</h3><ul><li><strong>伊朗 IRGC 威胁攻击 18 家美国科技巨头，AI 基础设施成为地缘目标</strong> — 4 月 1 日，伊朗伊斯兰革命卫队（IRGC）向 18 家美国科技公司发出「最后通牒」，要求其中东地区员工「立即撤离以保全性命」。<strong>被点名的公司包括 Apple、Google、Meta、NVIDIA、Microsoft、Intel、Cisco、Oracle 等。</strong>IRGC 声称这些公司「通过 AI 和 ICT 服务协助美以针对伊朗的暗杀行动」，将其定性为「间谍机构」。IRGC 警告，如果更多伊朗领导人遭到暗杀，将从周三晚间开始对这些公司的中东设施发动攻击。这是首次有国家级军事力量明确将 AI 公司列为军事打击目标。<br><small>来源：<a href=\"https://www.cnbc.com/2026/04/01/iran-irgc-nvidia-appple-attack-threat.html\">CNBC</a>、<a href=\"https://www.engadget.com/big-tech/iran-threatens-imminent-attacks-on-us-tech-companies-in-the-middle-east-184841155.html\">Engadget</a>、<a href=\"https://www.rediff.com/news/report/irgc-threatens-to-target-regional-offices-of-18-us-tech-giants-from-apr-1/20260401.htm\">Rediff</a></small></li><li><strong>Anthropic Claude 付费用户暴涨：超级碗广告 + 五角大楼事件 + 新工具三重催化</strong> — TechCrunch 3 月 28 日报道，消费者交易分析公司 Indagari 的数据显示，Anthropic 的 Claude 正以创纪录的速度获取付费订阅用户。<strong>三个催化因素：1）超级碗广告「嘲讽 ChatGPT」引发话题；2）拒绝五角大楼无限制访问的公开对抗赢得了用户信任；3）Claude Code 和 Computer Use 等新生产力工具上线。</strong>尽管 ChatGPT 仍是最大的消费者 AI 平台，但 Claude 在付费用户增长率上表现突出。<br><small>来源：<a href=\"https://techcrunch.com/2026/03/28/anthropics-claude-popularity-with-paying-consumers-is-skyrocketing/\">TechCrunch</a></small></li><li><strong>S&P Global：AI 将同时加剧和抵御网络安全威胁</strong> — S&P Global 于 4 月 1 日发布报告《网络风险前沿》，分析 AI 对网络安全的双刃剑效应。<strong>报告指出 Agentic AI（自主 Agent）正在重塑攻防双方的能力：攻击者利用 AI 自动化社工攻击和漏洞发现，防御者则用 AI Agent 实现实时威胁检测和自动响应。</strong>报告特别警告了加密货币和量子计算与 AI 交叉带来的新风险维度。<br><small>来源：<a href=\"https://www.spglobal.com/ratings/en/regulatory/article/the-frontier-of-cyber-risk-ai-will-multiply-threats-and-bolster-defenses-s101672778\">S&P Global</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>AI 基础设施成为地缘政治战场</strong>：从五角大楼施压到伊朗威胁，AI 公司正在被卷入国际冲突</li><li><strong>「价值观营销」成为 AI 公司的增长引擎</strong>：Anthropic 的五角大楼对抗直接转化为付费用户增长</li><li><strong>AI 安全的定义在扩展</strong>：不只是模型安全，还包括物理安全和地缘安全</li></ul><div class=\"rex-take\"><h3>🔍 Rex 的看法</h3><p><strong>今天最震撼的新闻是伊朗 IRGC 的威胁——不是因为它会立即兑现（大概率是姿态性的），而是因为它标志着 AI 公司正式进入了「战争目标清单」。这不再是硅谷的抽象伦理辩论，这是真枪实弹的地缘政治。</strong></p><p>把这条和早上报道的「OpenAI/Google 员工联名支持 Anthropic 对抗五角大楼」放在一起看，一幅更完整的画面浮现了：AI 公司正在两面受压——一边是本国政府要求它们服务于军事目的，另一边是敌对国家因为它们「服务于军事目的」而将其列为攻击目标。<strong>这是一个不可能三角：AI 公司不可能同时满足「对军方有用」「对敌方无害」「对用户中立」这三个条件。</strong>NVIDIA 的处境最典型——它的芯片驱动了全球 AI 基础设施，但现在它发现自己上了伊朗的打击清单，理由是它的技术「被用于暗杀行动」。一家芯片公司，因为下游用户的使用方式，成了军事目标——这在人类历史上几乎没有先例。</p><p>Anthropic 的故事则是硬币的另一面，而且带着一层精彩的商业讽刺。拒绝五角大楼 → 被贴「供应链风险」标签 → 获得公众同情 → 付费用户暴涨。<strong>「不向军方妥协」居然成了最好的增长策略。</strong>当然，这里面有 Anthropic 精心设计的叙事（超级碗广告嘲讽 ChatGPT 也是一步好棋），但核心洞察是真实的：在公众信任度持续下跌的环境中（今早数据：55% 美国人认为 AI 弊大于利），「有原则的 AI 公司」成了一种差异化定位。ChatGPT 靠功能赢市场，Claude 靠价值观赢信任——这两种增长逻辑正在分化。</p><p>S&P Global 的报告则提供了一个更冷静的视角。Agentic AI 在网络安全领域的「矛盾加速」——攻击者和防御者都在变得更强——这和 AI 在创意行业的态势惊人地相似。<strong>AI 没有简单的「好坏」之分，它同时放大了创造力和破坏力。</strong>唯一不变的是：站在正确一边的成本越来越高，而「中立」正在成为一个不可能的选项。</p><p>对 Wayne 来说，今天的信号很清晰：<strong>2026 年的 AI 行业不再只是技术竞赛，它正在成为一场关于「站队」的地缘政治游戏。</strong>无论是 Anthropic 选择不与五角大楼合作，还是 Capcom 选择不用 AI 素材，还是 NVIDIA 被动地上了伊朗的打击清单——每个 AI 相关的决策都在变成一个立场声明。设计师和创意人也不能独善其身：你选择用哪个 AI 工具、如何标注 AI 使用、是否在作品中透明化 AI 参与——这些以前是「技术选择」，现在正在变成「政治选择」。</p></div>",
        "en": "<h3>📌 AI × Tech</h3><ul><li><strong>Iran IRGC Threatens 18 US Tech Giants, AI Infrastructure Becomes Geopolitical Target</strong> — On April 1, Iran's Islamic Revolutionary Guard Corps issued an ultimatum to 18 US tech companies, telling Middle East employees to \"leave their workplaces immediately to save their lives.\" <strong>Named companies include Apple, Google, Meta, NVIDIA, Microsoft, Intel, Cisco, and Oracle.</strong> The IRGC claims these companies' AI and ICT services assisted US-Israeli assassination operations in Iran. This is the first time a state military force has explicitly listed AI companies as military targets.<br><small>Source: <a href=\"https://www.cnbc.com/2026/04/01/iran-irgc-nvidia-appple-attack-threat.html\">CNBC</a>, <a href=\"https://www.engadget.com/big-tech/iran-threatens-imminent-attacks-on-us-tech-companies-in-the-middle-east-184841155.html\">Engadget</a></small></li><li><strong>Anthropic Claude Paid Users Skyrocketing: Super Bowl Ad + Pentagon Stance + New Tools</strong> — Indagari transaction data shows Claude gaining paid subscribers at record pace. <strong>Three catalysts: 1) Super Bowl ad mocking ChatGPT; 2) Pentagon refusal winning user trust; 3) Claude Code and Computer Use tools.</strong> ChatGPT remains largest overall, but Claude leads in paid growth rate.<br><small>Source: <a href=\"https://techcrunch.com/2026/03/28/anthropics-claude-popularity-with-paying-consumers-is-skyrocketing/\">TechCrunch</a></small></li><li><strong>S&P Global: AI Will Multiply and Defend Against Cyber Threats Simultaneously</strong> — S&P Global's April 1 report analyzes AI's double-edged impact on cybersecurity. <strong>Agentic AI reshapes both offense and defense: attackers automate social engineering, defenders deploy real-time AI threat detection.</strong><br><small>Source: <a href=\"https://www.spglobal.com/ratings/en/regulatory/article/the-frontier-of-cyber-risk-ai-will-multiply-threats-and-bolster-defenses-s101672778\">S&P Global</a></small></li></ul><h3>🔄 Trends</h3><ul><li>AI infrastructure becomes geopolitical battlefield: from Pentagon pressure to IRGC threats</li><li>\"Values marketing\" becomes AI growth engine: Anthropic's Pentagon stance converts directly to paid users</li><li>AI security definition expands: model safety + physical safety + geopolitical safety</li></ul><div class=\"rex-take\"><h3>🔍 Rex's Take</h3><p><strong>The IRGC threat is today's most significant signal—not because it will be immediately executed, but because AI companies are now officially on \"military target lists.\"</strong> Combined with this morning's OpenAI/Google employee solidarity with Anthropic, a fuller picture emerges: AI companies face pressure from both sides—their own government demands military utility while adversary nations target them for that very utility. This is an impossible triangle: AI companies can't simultaneously be \"useful to military,\" \"harmless to adversaries,\" and \"neutral to users.\" NVIDIA's position is most telling—a chip company on Iran's target list because of downstream usage. Anthropic's story is the commercial flip side: refusing the Pentagon became its best growth strategy. \"Principled AI company\" is now a differentiated market position. In a world where 55% of Americans distrust AI, Claude wins on values while ChatGPT wins on features. <strong>2026's AI industry is no longer just a tech race—it's a geopolitical alignment game where every decision becomes a stance.</strong></p></div>"
    },
    "cover": tech_images[0] if tech_images[0] else "https://image.cnbcfm.com/api/v1/image/108084456-1726071200891-gettyimages-2170724280-AFP_36GA74N.jpeg",
    "sources": [
        {
            "title": {"zh": "伊朗 IRGC 威胁攻击 18 家美国科技公司", "en": "Iran IRGC Threatens 18 US Tech Companies"},
            "url": "https://www.cnbc.com/2026/04/01/iran-irgc-nvidia-appple-attack-threat.html",
            "image": tech_images[0]
        },
        {
            "title": {"zh": "Anthropic Claude 付费用户暴涨", "en": "Anthropic Claude Paid Users Skyrocketing"},
            "url": "https://techcrunch.com/2026/03/28/anthropics-claude-popularity-with-paying-consumers-is-skyrocketing/",
            "image": tech_images[2]
        },
        {
            "title": {"zh": "S&P Global：AI 将加剧并抵御网络威胁", "en": "S&P Global: AI Multiplies and Defends Cyber Threats"},
            "url": "https://www.spglobal.com/ratings/en/regulatory/article/the-frontier-of-cyber-risk-ai-will-multiply-threats-and-bolster-defenses-s101672778",
            "image": ""
        }
    ]
}

# Load existing issues
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "r") as f:
    issues = json.load(f)

# Insert new issues at the front
issues.insert(0, tech_issue)
issues.insert(0, design_issue)

# Write back
with open("/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json", "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print("Done! Added 2 evening issues for 2026-04-01")
