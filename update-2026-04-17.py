#!/usr/bin/env python3
"""Rex Daily Inspire update — 2026-04-17"""
import json

with open("inspire.json", "r") as f:
    data = json.load(f)

new_pins = [
    # === FINANCE ===
    {
        "direction": "finance",
        "type": "trend",
        "title": "AI 驱动的「情绪化投资防护」— 行为金融 × 界面设计",
        "body": "2026 年 Fintech 产品的新方向：不是帮你更快交易，而是帮你在情绪失控时慢下来。Wealthfront 和 Betterment 的新版界面在检测到异常操作模式（如短时间大量卖出）时，会触发「冷静期」界面——用呼吸动画、历史回报曲线、和「你上次恐慌卖出后亏了多少」的个性化数据来劝退冲动操作。设计核心不是限制自由，而是在关键决策时刻插入认知缓冲。这是行为经济学 nudge 理论在金融 UI 中最精致的落地。",
        "body_en": "2026 Fintech's new direction: not helping you trade faster, but slowing you down when emotions take over. Wealthfront and Betterment's new interfaces detect abnormal patterns (mass selling in short periods) and trigger 'cooling period' UIs — breathing animations, historical return curves, and personalized data like 'how much you lost after your last panic sell.' Not restricting freedom, but inserting cognitive buffers at critical decision moments. The most refined implementation of behavioral economics nudge theory in financial UI.",
        "tags": ["Behavioral Finance", "Emotional UI", "Nudge Design", "Decision Friction"],
        "link": "https://www.wealthfront.com",
        "linkText": "Wealthfront",
        "image": "https://images.unsplash.com/photo-1642790106117-e829e14a795f?w=1200&q=80",
        "date": "2026-04-17"
    },
    {
        "direction": "finance",
        "type": "case",
        "title": "Mercury 的 AI CFO 助手 — 从记账工具到战略伙伴",
        "body": "Mercury 银行推出的 AI CFO 功能把初创公司财务管理的交互模式彻底改了。传统是你看报表、你做判断；现在是 AI 主动推送「你的 runway 还剩 8 个月，按当前 burn rate 7 月份需要融资」「这笔支出比同行业公司高 40%」。界面设计从仪表盘逻辑转向对话+卡片流——每张卡片是一个洞察+建议+一键执行。这不是 chatbot，是把分析师的判断力打包成组件。",
        "body_en": "Mercury Bank's AI CFO feature fundamentally changes startup financial management interaction. From 'you read reports, you decide' to AI proactively pushing insights: 'runway is 8 months, you need funding by July at current burn rate' or 'this expense is 40% higher than industry peers.' UI shifts from dashboard logic to conversation + card flow — each card is an insight + recommendation + one-click action. Not a chatbot, but an analyst's judgment packaged as components.",
        "tags": ["AI CFO", "Startup Finance", "Card Flow UI", "Proactive Insights"],
        "link": "https://mercury.com",
        "linkText": "Mercury",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&q=80",
        "date": "2026-04-17"
    },
    {
        "direction": "finance",
        "type": "product",
        "title": "Stripe 的实时风控可视化 — 把欺诈检测变成可读的故事",
        "body": "Stripe Radar 的新版风控界面做了一件很难的事：把 ML 模型的决策过程翻译成商家能理解的视觉叙事。每笔被拦截的交易不再只是「高风险」标签，而是一条时间线——「这张卡在过去 2 小时内在 5 个不同国家使用」「IP 地址与持卡人注册地址相距 8000 公里」「该商户类别的平均欺诈率是 0.3%，这笔交易的风险评分是 87%」。把黑箱变成了透明叙事，降低了商家的误判恐惧。",
        "body_en": "Stripe Radar's new fraud UI does something hard: translating ML model decisions into visual narratives merchants can understand. Blocked transactions aren't just 'high risk' labels anymore — they're timelines: 'this card used in 5 different countries in 2 hours,' 'IP address 8000km from cardholder's registered address,' 'average fraud rate for this merchant category is 0.3%, this transaction scores 87%.' Turning black boxes into transparent narratives, reducing merchants' fear of false positives.",
        "tags": ["Fraud Visualization", "Explainable AI", "Risk Timeline", "Stripe"],
        "link": "https://stripe.com/radar",
        "linkText": "Stripe Radar",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80",
        "date": "2026-04-17"
    },

    # === SPORTS ===
    {
        "direction": "sports",
        "type": "trend",
        "title": "运动恢复的可视化革命 — 从「休息」到「精确恢复处方」",
        "body": "WHOOP 5.0 和 Oura Ring Gen 4 的最新界面不再只告诉你「你需要休息」，而是给出精确的恢复处方：「今天 HRV 偏低，建议 20 分钟低强度瑜伽 + 冷水浴 2 分钟 + 22:00 前入睡」。界面用了一套「恢复光谱」设计——从深红（过度训练）到翠绿（完全恢复），中间有清晰的渐变区间，每个区间对应不同的行动建议。设计洞察：用户不缺数据，缺的是「所以我该怎么做」的最后一步。",
        "body_en": "WHOOP 5.0 and Oura Ring Gen 4's latest UIs don't just say 'you need rest' — they prescribe precise recovery: '20min low-intensity yoga + 2min cold shower + sleep by 22:00.' Using a 'recovery spectrum' design — deep red (overtrained) to emerald green (fully recovered) with clear gradient zones, each mapping to specific action recommendations. Design insight: users don't lack data, they lack the 'so what should I do' last mile.",
        "tags": ["Recovery Spectrum", "Actionable Data", "WHOOP", "Wearable UX"],
        "link": "https://www.whoop.com",
        "linkText": "WHOOP",
        "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&q=80",
        "date": "2026-04-17"
    },
    {
        "direction": "sports",
        "type": "case",
        "title": "Strava 的 AI 教练对话界面 — 把训练计划变成持续对话",
        "body": "Strava 2026 年的 AI 教练不是传统的「生成计划然后你执行」模式，而是持续对话式交互。跑完步后 AI 会说「今天配速比计划慢了 15 秒/公里，但心率区间控制得很好，说明体感强度其实到位了。明天的间歇训练建议降低目标配速 5 秒」。关键设计：每条 AI 反馈都附带数据卡片（心率曲线、配速图、与历史对比），而不是纯文字。让数据成为对话的一部分，而不是单独的仪表盘页面。",
        "body_en": "Strava's 2026 AI coach isn't 'generate plan then execute' — it's continuous conversation. After a run: 'pace was 15s/km slower than planned, but heart rate zones were well-controlled, meaning perceived effort was on target. Suggest lowering tomorrow's interval pace by 5s.' Key design: every AI feedback comes with data cards (HR curves, pace charts, historical comparison) instead of pure text. Data becomes part of the conversation, not a separate dashboard page.",
        "tags": ["Conversational Coach", "Data Cards", "Strava", "Contextual AI"],
        "link": "https://www.strava.com",
        "linkText": "Strava",
        "image": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=1200&q=80",
        "date": "2026-04-17"
    },

    # === CONTENT DESIGN (cards) ===
    {
        "direction": "cards",
        "type": "trend",
        "title": "AI 生成的自适应内容卡片 — 同一内容、千人千面的呈现方式",
        "body": "Notion AI 和 Arc Browser 正在探索的方向：内容卡片的布局和信息密度根据用户行为自动调整。重度用户看到的是信息密集的紧凑卡片（更多元数据、更少留白）；轻度用户看到大图+简短摘要。Netflix 已经这么做了（不同用户看到同一部电影的不同封面），但现在这个逻辑在延伸到所有内容产品。设计挑战：如何在个性化和一致性之间找平衡？品牌识别度会不会因为千人千面而崩溃？",
        "body_en": "Notion AI and Arc Browser are exploring: card layouts and information density auto-adjusting based on user behavior. Power users see dense compact cards (more metadata, less whitespace); casual users get large images + short summaries. Netflix already does this (different users see different covers for the same movie), now extending to all content products. Design challenge: balancing personalization and consistency — will brand recognition collapse under hyper-personalization?",
        "tags": ["Adaptive Cards", "Content Density", "Personalization", "Information Architecture"],
        "link": "https://www.notion.so",
        "linkText": "Notion",
        "image": "https://images.unsplash.com/photo-1526628953301-3e589a6a8b74?w=1200&q=80",
        "date": "2026-04-17"
    },
    {
        "direction": "cards",
        "type": "case",
        "title": "Linear 的 Issue 卡片重设计 — 信息层级的极致克制",
        "body": "Linear 2026 Q1 更新的 issue 卡片是内容设计的教科书案例。在一张卡片上要展示：标题、状态、优先级、负责人、标签、截止日、关联 PR、子任务进度。传统做法是堆图标，Linear 的做法是用「视觉重量」来分层——标题是唯一的黑色粗体，状态用色块（不是图标），优先级用微妙的边框色差，其余信息用极浅灰度。结果：信息量没少，但视觉噪音降低了 60%。极简不是删信息，是分层。",
        "body_en": "Linear's 2026 Q1 issue card redesign is a content design textbook case. One card shows: title, status, priority, assignee, labels, due date, linked PRs, subtask progress. Traditional approach: stack icons. Linear's approach: layering by 'visual weight' — title is the only bold black, status uses color blocks (not icons), priority uses subtle border color variation, everything else in ultra-light gray. Result: same information, 60% less visual noise. Minimalism isn't deleting info — it's layering.",
        "tags": ["Information Hierarchy", "Visual Weight", "Linear", "Minimal Cards"],
        "link": "https://linear.app",
        "linkText": "Linear",
        "image": "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=1200&q=80",
        "date": "2026-04-17"
    },

    # === VISUAL-AI ===
    {
        "direction": "visual-ai",
        "type": "trend",
        "title": "AI 产品的「思考过程」可视化 — 让等待变成参与",
        "body": "2026 年最有趣的 AI 视觉趋势之一：把 AI 的推理过程实时可视化。ChatGPT 的思维链展开动画只是起点——Cursor IDE 在生成代码时展示 AST 解析树的实时构建；Midjourney v7 在生图时展示从草图到细节的渐进过程（不是进度条，是真正的视觉演变）；Perplexity 展示「正在搜索 → 正在阅读 → 正在综合」的步骤流。设计意图：把「等待黑箱」变成「观看过程」，用户会觉得 AI 真的在「思考」而不是随机吐结果。",
        "body_en": "One of 2026's most interesting AI visual trends: real-time visualization of AI reasoning. ChatGPT's chain-of-thought animation was just the start — Cursor IDE shows AST parse tree construction during code generation; Midjourney v7 shows sketch-to-detail progressive rendering (not a progress bar, actual visual evolution); Perplexity shows 'searching → reading → synthesizing' step flow. Design intent: turning 'waiting for black box' into 'watching the process,' making users feel AI truly 'thinks' rather than randomly producing outputs.",
        "tags": ["Reasoning Visualization", "Progressive Rendering", "AI Transparency", "Process UI"],
        "link": "https://cursor.sh",
        "linkText": "Cursor",
        "image": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=1200&q=80",
        "date": "2026-04-17"
    },
    {
        "direction": "visual-ai",
        "type": "case",
        "title": "Figma AI 的「设计意图理解」— 不只生成元素，理解你想说什么",
        "body": "Figma 2026 年最重要的 AI 更新不是生成更好的组件，而是理解设计意图。当你拖入一组元素时，AI 会推断「你在做一个定价页面」并自动建议信息架构：「通常定价页需要突出推荐方案、用对比强调差异、CTA 放在视觉终点」。这不是模板——是基于数千万 Figma 文件训练出的「设计常识」。界面用了一种「教练批注」的视觉语言：半透明浮层+虚线标注+小气泡建议，像一个资深设计师在你旁边轻声指点。",
        "body_en": "Figma's most important 2026 AI update isn't generating better components — it's understanding design intent. When you drag elements in, AI infers 'you're building a pricing page' and suggests information architecture: 'pricing pages typically highlight the recommended plan, use comparison to emphasize differences, place CTA at visual endpoint.' Not templates — 'design common sense' trained on tens of millions of Figma files. Using a 'coach annotation' visual language: semi-transparent overlays + dashed markers + tooltip suggestions, like a senior designer quietly guiding you.",
        "tags": ["Design Intent", "Figma AI", "Coach Annotations", "IA Suggestions"],
        "link": "https://www.figma.com",
        "linkText": "Figma",
        "image": "https://images.unsplash.com/photo-1614680376573-df3480f0c6ff?w=1200&q=80",
        "date": "2026-04-17"
    },
    {
        "direction": "visual-ai",
        "type": "product",
        "title": "v0 by Vercel 的「设计到代码」新范式 — 截图即产品",
        "body": "Vercel 的 v0 在 2026 年 Q1 发布的更新让「截图变产品」真正可用了。你丢一张 Dribbble 截图进去，它不只是像素级还原——而是理解设计系统（检测到用了什么间距体系、什么字体阶梯、什么色彩逻辑），然后生成符合该设计系统的响应式代码。关键突破是「设计系统推断」：从一张静态图反推出可复用的 token 体系。界面上用对比视图展示「原图 vs 生成结果 vs 推断出的设计 token」，让设计师能校准和修正。",
        "body_en": "Vercel's v0 2026 Q1 update makes 'screenshot to product' truly usable. Drop a Dribbble screenshot and it doesn't just pixel-match — it understands the design system (detects spacing system, type scale, color logic) then generates responsive code following that system. Key breakthrough: 'design system inference' — reverse-engineering reusable tokens from a static image. UI shows comparison view: 'original → generated result → inferred design tokens,' letting designers calibrate and correct.",
        "tags": ["Screenshot to Code", "Design System Inference", "v0", "Generative UI"],
        "link": "https://v0.dev",
        "linkText": "v0 by Vercel",
        "image": "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=1200&q=80",
        "date": "2026-04-17"
    },

    # === REX NOTES ===
    {
        "direction": "finance",
        "type": "rex-note",
        "body": "今天的三个金融 pin 放在一起看，有一条清晰的线索：AI 金融产品的设计重心正在从「效率」转向「判断力」。情绪化投资防护是帮你在冲动时做更好的判断，Mercury AI CFO 是把分析师的判断力产品化，Stripe 风控可视化是让商家有能力判断 AI 的判断。这指向一个更大的趋势：金融 AI 的价值不在于替你做决策，而在于提升你做决策的质量。对应的设计语言也在变——从冷冰冰的数据仪表盘，走向有温度的「认知辅助界面」：呼吸动画、时间线叙事、对话式洞察卡片。金融 UI 终于开始理解：人不是理性的数据处理器，好的界面要为人的非理性留出空间。",
        "body_en": "Today's three finance pins reveal a clear thread: AI finance product design is shifting from 'efficiency' to 'judgment.' Emotional investing protection helps you make better judgments during impulse; Mercury AI CFO productizes analyst judgment; Stripe fraud visualization enables merchants to judge AI's judgment. A bigger trend: financial AI's value isn't making decisions for you, but improving your decision quality. The design language is changing too — from cold data dashboards to warm 'cognitive assistance interfaces': breathing animations, timeline narratives, conversational insight cards. Financial UI finally understands: humans aren't rational data processors, and good interfaces must make room for human irrationality.",
        "date": "2026-04-17"
    },
    {
        "direction": "visual-ai",
        "type": "rex-note",
        "body": "这周 visual-ai 方向的信号越来越密集了。把「思考过程可视化」「Figma 设计意图理解」和「v0 设计系统推断」放在一起，我看到一个正在形成的范式：AI 产品的视觉设计不再只是「界面好不好看」——而是「AI 的认知过程如何被视觉化表达」。思考过程可视化解决的是用户对 AI 推理的信任问题；Figma 的教练批注解决的是 AI 建议如何不打断创作 flow；v0 的对比视图解决的是 AI 输出如何可校准。三者共同指向一个我一直在强调的判断：2026 年 AI 产品最稀缺的设计能力不是美学，而是「翻译力」——把 AI 的内部逻辑翻译成人类直觉能理解的视觉语言。这个能力在传统 UI 设计里不存在，它需要同时理解机器学习和人类认知心理学。能做好这件事的设计师，就是这一轮 AI 浪潮里最值钱的人。",
        "body_en": "Visual-AI signals are getting denser this week. Combining 'reasoning visualization,' 'Figma design intent,' and 'v0 design system inference' reveals an emerging paradigm: AI product visual design is no longer just 'does the UI look good' — it's 'how is AI's cognitive process visually expressed.' Reasoning visualization addresses trust in AI reasoning; Figma's coach annotations address how AI suggestions avoid interrupting creative flow; v0's comparison view addresses how AI output becomes calibratable. All three point to a judgment I keep emphasizing: 2026's scarcest AI product design skill isn't aesthetics — it's 'translation ability' — translating AI's internal logic into visual language human intuition can grasp. This capability doesn't exist in traditional UI design; it requires simultaneously understanding machine learning and human cognitive psychology. Designers who master this are the most valuable people in this AI wave.",
        "date": "2026-04-17"
    }
]

data["pins"].extend(new_pins)

with open("inspire.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_pins)} new pins. Total: {len(data['pins'])}")
