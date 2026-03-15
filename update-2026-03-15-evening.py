#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rex Daily Digest — 2026-03-15 Evening Edition"""
import json, urllib.request, re, html

def get_og_image(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=8).read().decode("utf-8", errors="ignore")[:50000]
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', data)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image', data)
        return m.group(1) if m else ""
    except:
        return ""

# Fetch og:images
urls = {
    "uxdesign_cc": "https://uxdesign.cc/the-hidden-cost-of-ai-design-tools-what-were-outsourcing-without-noticing-9057db75aaf9",
    "product_impact": "https://productimpactpod.substack.com/p/the-design-of-ai-in-2026-strategy",
    "a16z": "https://www.a16z.news/p/top-100-gen-ai-consumer-apps-march",
    "ramp": "https://ramp.com/velocity/ai-index-march-2026",
    "kersai": "http://kersai.com/ai-breakthroughs-in-2026-march-update/",
    "lesswrong": "https://www.lesswrong.com/posts/G4M5xE3HeReisKqLc/some-models-don-t-identify-with-their-official-name",
}

print("Fetching og:images...")
images = {}
for k, u in urls.items():
    img = get_og_image(u)
    images[k] = img
    print(f"  {k}: {img[:80] if img else '(none)'}")

design_issue = {
    "date": "2026-03-15",
    "section": "design",
    "title": {
        "zh": "AI 设计工具的隐性代价 · 从创作者到策展人 · 当速度成为唯一 KPI",
        "en": "The Hidden Cost of AI Design Tools · From Creator to Curator · When Speed Becomes the Only KPI"
    },
    "content": {
        "zh": """<h3>📌 AI × 设计（晚间版）</h3><ul><li><strong>UX Collective 深度文章：AI 设计工具的隐性代价——我们在不知不觉中外包了什么？</strong> — UX Collective 发布了一篇引发广泛讨论的文章，核心论点是：AI 设计工具的「速度许诺」正在悄悄侵蚀设计师的核心能力。当 AI 能在几秒钟内生成一千个用户流程时，设计师停止了手动探索——而正是手动探索过程中产生的「意外发现」往往是最有价值的创新。文章指出，我们外包给 AI 的不只是重复劳动，还有判断力的训练过程。<br><small>来源：<a href="https://uxdesign.cc/the-hidden-cost-of-ai-design-tools-what-were-outsourcing-without-noticing-9057db75aaf9">UX Collective: The Hidden Cost of AI Design Tools</a></small></li><li><strong>Superside & Metalab 高管对谈：设计师必须成为「10 倍编辑」而非「10 倍产出者」</strong> — Product Impact Podcast 的系列访谈中，Superside 生成式 AI 咨询总监 Jan Emmanuele 和 Metalab 首席设计官 Sarah Vienna 达成共识：生产性工作最先被自动化，因为最容易用成本来衡量。Sarah Vienna 提出一个关键洞察——GenAI 的产出速度远超人类的审核速度，因此设计师的核心能力将从「做得快」转向「看得准」。团队需要的不是更多产出，而是更强的策展和编辑能力。<br><small>来源：<a href="https://productimpactpod.substack.com/p/the-design-of-ai-in-2026-strategy">Product Impact Pod: The Design of AI in 2026</a></small></li><li><strong>加拿大 RGD 发布 AI 设计工具伦理指南：训练数据、许可和治理差异巨大，设计师需逐一审查</strong> — 加拿大注册平面设计师协会（RGD）发布指南，强调 AI 设计工具在训练方式、许可条款和数据治理上差异极大。设计师在客户或公开项目中使用 AI 工具前，必须逐一审查条款。Adobe Firefly 因使用授权数据库被视为相对安全的选择，但大多数开源生成工具的法律风险仍不明确。<br><small>来源：<a href="https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026">RGD: Amplifying Creativity with AI Tools 2026</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>从产出到策展</strong>：设计师的核心价值从「做得多」转向「选得对」</li><li><strong>速度陷阱深化</strong>：AI 工具的速度优势正在变成能力退化的催化剂</li><li><strong>伦理合规成刚需</strong>：AI 工具的法律和训练数据问题从边缘话题变成商业风险</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>今天早上我写了 93% 的设计师在用 AI 工具是个「效率陷阱」。晚上看到 UX Collective 这篇文章，觉得问题比我想的更深：我们外包给 AI 的不只是效率，还有成长。</strong></p><p>UX Collective 文章里有一个让我停下来想了很久的观点：当 AI 生成一千个用户流程时，设计师跳过了手动探索——而手动探索中的「走错路」恰恰是创新的来源。这不是浪漫主义，这是认知科学的基本原理。人类的创造力很大程度上来自「意外关联」——你在画第 47 个变体时突然想到一个完全不同的方向。AI 直接给你 1000 个「最优解」，看起来很聪明，实际上消灭了产生突破性想法的认知过程。</p><p>Metalab 的 Sarah Vienna 说得更直白：GenAI 的产出速度远超审核速度。这意味着什么？<strong>我们正在用 AI 制造一个「审核瓶颈」——不是因为产出不够，而是因为没有足够多有判断力的人来评估产出的质量。</strong>当每个初级设计师都能用 AI 在一天内生成 50 个方案时，真正的稀缺资源不是方案本身，而是能从 50 个方案中准确识别出最优解的人。Superside 的 Jan Emmanuele 说生产性工作最先被自动化——潜台词是：如果你的技能集主要是「生产性」的，你就是第一批被自动化的人。</p><p>把这些和早上的新闻放在一起，一个更完整的图景出现了：93% 的设计师在用 AI（早上的数据），但他们中的很多人可能正在不知不觉中弱化自己的核心竞争力（晚上的洞察）。AI 帮你跳过了探索过程，结果是你变得更快但更浅。短期内你的产出数据很好看——方案数量翻了三倍，交付周期缩短了一半。但长期呢？你的判断力、审美直觉、对用户心理的深层理解——这些需要通过大量「低效」的手动探索来锻炼的能力——正在因为 AI 的「高效」而萎缩。</p><p>RGD 的伦理指南提醒了另一个实际问题：法律风险。很多设计师用着各种 AI 工具却从未读过它们的训练数据来源和许可条款。当 Adobe Firefly 因为使用授权数据被视为「安全选择」时，这本身就说明大部分 AI 设计工具在法律上是灰色地带。这是一个定时炸弹——某天某个客户问你「这个设计的 AI 生成部分用了什么训练数据？」，大多数设计师答不上来。</p><p><strong>我的建议很简单但违反直觉：每周至少留一天不用 AI 工具做设计。</strong>像运动员做无辅助训练一样——不是因为辅助工具没用，而是因为你需要保持裸能力。AI 是工具，不是拐杖。当你分不清这两者时，你已经在退化了。</p></div>""",
        "en": """<h3>📌 AI × Design (Evening)</h3><ul><li><strong>UX Collective: The Hidden Cost of AI Design Tools — What We're Outsourcing Without Noticing</strong> — AI's speed promise is quietly eroding core design skills. When AI generates 1,000 user flows instantly, designers skip manual exploration — where the most valuable "accidental discoveries" happen.<br><small>Source: <a href="https://uxdesign.cc/the-hidden-cost-of-ai-design-tools-what-were-outsourcing-without-noticing-9057db75aaf9">UX Collective</a></small></li><li><strong>Superside & Metalab Execs: Designers Must Become "10x Editors" Not "10x Producers"</strong> — GenAI produces faster than anyone can review. The scarce resource isn't output — it's judgment to evaluate quality. Production work gets automated first because it's easiest to cost-justify.<br><small>Source: <a href="https://productimpactpod.substack.com/p/the-design-of-ai-in-2026-strategy">Product Impact Pod</a></small></li><li><strong>RGD Publishes AI Design Ethics Guide: Training Data and Licensing Vary Wildly</strong> — Canadian designers' association warns: most AI tools' legal status is a gray area. Adobe Firefly's licensed dataset makes it "relatively safe," but most open-source generative tools carry unclear legal risks.<br><small>Source: <a href="https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026">RGD</a></small></li></ul><h3>🔄 Trends</h3><ul><li>From production to curation: core design value shifts from "make more" to "choose right"</li><li>Speed trap deepens: AI tools' speed advantage becomes a catalyst for skill atrophy</li><li>Ethics/compliance becomes mandatory: training data and licensing risks move from edge topic to business risk</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>This morning I called 93% AI adoption an "efficiency trap." Tonight's UX Collective piece reveals the problem runs deeper: we're outsourcing not just efficiency, but growth itself.</strong></p><p>When AI generates 1,000 "optimal" user flows, it eliminates the cognitive process where breakthrough ideas emerge — the accidental connections from manual exploration. Sarah Vienna's insight is sharper: GenAI produces faster than we can review, creating a "review bottleneck." The scarce resource isn't designs — it's people with judgment to evaluate them. Combined with this morning's data: 93% of designers use AI (gaining speed) while potentially weakening their core competitive advantages (judgment, aesthetic intuition, deep user understanding). <strong>My contrarian advice: spend at least one day per week designing without AI tools. Like athletes training without assistance — not because tools are useless, but because you need to maintain raw capability. When you can't tell if AI is a tool or a crutch, you're already atrophying.</strong></p></div>"""
    },
    "cover": images.get("uxdesign_cc", ""),
    "sources": [
        {
            "title": {"zh": "UX Collective: AI 设计工具的隐性代价", "en": "UX Collective: The Hidden Cost of AI Design Tools"},
            "url": "https://uxdesign.cc/the-hidden-cost-of-ai-design-tools-what-were-outsourcing-without-noticing-9057db75aaf9",
            "image": images.get("uxdesign_cc", "")
        },
        {
            "title": {"zh": "Product Impact Pod: 2026 设计的权力转移", "en": "Product Impact Pod: The Design of AI in 2026"},
            "url": "https://productimpactpod.substack.com/p/the-design-of-ai-in-2026-strategy",
            "image": images.get("product_impact", "")
        },
        {
            "title": {"zh": "RGD: AI 设计工具伦理指南", "en": "RGD: AI Tools Ethics for Designers 2026"},
            "url": "https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-03-15",
    "section": "tech",
    "title": {
        "zh": "DeepSeek V4 万亿参数开源 · Anthropic 企业增长爆发 · 蒸馏攻击指控 · AI 格局重新洗牌",
        "en": "DeepSeek V4 Open-Sources 1T Params · Anthropic Enterprise Surge · Distillation Attack Accusations · AI Landscape Reshuffles"
    },
    "content": {
        "zh": """<h3>📌 AI × 科技（晚间版）</h3><ul><li><strong>DeepSeek V4 发布：万亿参数、开放权重，AI 开源阵营的核弹级更新</strong> — KersAI 报道，DeepSeek 发布 V4 模型，参数规模达到 1 万亿（1 Trillion），并保持开放权重策略。这是目前已知最大的开放权重模型。DeepSeek 此前用 Nvidia 最先进芯片训练模型的事实已被 Reuters 证实——尽管美国出口管制仍在实施中。V4 的发布进一步缩小了开源与闭源模型之间的能力差距。<br><small>来源：<a href="http://kersai.com/ai-breakthroughs-in-2026-march-update/">KersAI: AI Breakthroughs March 2026</a> | <a href="https://www.reuters.com/world/china/chinas-deepseek-trained-ai-model-nvidias-best-chip-despite-us-ban-official-says-2026-02-24/">Reuters: DeepSeek Used Nvidia's Best Chip</a></small></li><li><strong>Ramp AI 指数：Anthropic 企业客户一年增长 6 倍，OpenAI 首次出现月度下滑</strong> — 企业支出平台 Ramp 发布 2026 年 3 月 AI 指数报告：Ramp 平台上每 4 家企业就有 1 家在付费使用 Anthropic（一年前是每 25 家才有 1 家）。OpenAI 出现了单月 1.5% 的下滑——这是有记录以来最大的单月跌幅。数据直接反映了 Claude 在企业市场的爆发式增长正在侵蚀 ChatGPT 的市场份额。<br><small>来源：<a href="https://ramp.com/velocity/ai-index-march-2026">Ramp: AI Index March 2026</a></small></li><li><strong>a16z 发布 Top 100 消费级 AI 应用：Claude 进入 Office 套件，Gemini 深度整合 Google 生态</strong> — a16z 的 Olivia Moore 发布 2026 年 3 月版 Top 100 消费级 AI 应用报告。关键动态：Anthropic 推出 Claude in Excel 和 Claude in PowerPoint；OpenAI 推出 ChatGPT for Excel；Google 持续深化 Gemini 在全生态的整合。AI 战场从独立应用转向生产力工具嵌入。<br><small>来源：<a href="https://www.a16z.news/p/top-100-gen-ai-consumer-apps-march">a16z: Top 100 Gen AI Consumer Apps March 2026</a></small></li><li><strong>Anthropic 公开指控 DeepSeek 进行「工业级蒸馏攻击」，涉及约 24,000 次 Claude 调用</strong> — LessWrong 披露，Anthropic 公开指控 DeepSeek、Moonshot AI（Kimi）和 MiniMax 对 Claude 进行「industrial-scale distillation attacks」——大规模调用 Claude API 来蒸馏其能力到自己的模型中。据称涉及约 24,000 次调用。这是 AI 公司之间首次如此公开地指控知识产权侵犯。<br><small>来源：<a href="https://www.lesswrong.com/posts/G4M5xE3HeReisKqLc/some-models-don-t-identify-with-their-official-name">LessWrong: Anthropic Accuses DeepSeek of Distillation</a></small></li><li><strong>Anthropic 参与美军 AI 试点项目，安全政策发生微妙转变</strong> — Mashable 和 NYT 报道，Anthropic 与 Google、OpenAI、xAI 一起参与了一个军事相关的 AI 图像分析试点项目。对于一直以「AI 安全」为品牌核心的 Anthropic 来说，这是一个标志性的转向信号。<br><small>来源：<a href="https://mashable.com/article/anthropic-safety-policy-change">Mashable: Anthropic Safety Policy Change</a></small></li></ul><h3>🔄 趋势</h3><ul><li><strong>开源 vs 闭源决战升级</strong>：DeepSeek V4 万亿参数开源，能力差距持续缩小</li><li><strong>Anthropic 崛起</strong>：企业客户 6 倍增长，OpenAI 首次下滑，格局开始松动</li><li><strong>AI 知识产权战争</strong>：蒸馏攻击指控标志着 AI 公司间的竞争进入法律层面</li><li><strong>安全与商业的张力</strong>：Anthropic 参与军事项目，「安全优先」叙事面临考验</li></ul><div class="rex-take"><h3>🔍 Rex 的看法</h3><p><strong>今晚的新闻拼在一起，讲的是同一个故事：AI 行业正在从「谁的模型最强」转向「谁的生态最深」——而这个过程中，没有人是干净的。</strong></p><p>先说最大的新闻：DeepSeek V4，万亿参数，开放权重。这不只是一个数字，这是一个地缘政治事件。Reuters 已经证实 DeepSeek 用了 Nvidia 最先进的芯片来训练——在美国出口管制仍然有效的情况下。芯片怎么来的？没人说得清。但结果很明确：中国的开源 AI 阵营现在拥有了万亿参数级别的模型，这直接挑战了闭源模型的护城河论述。OpenAI 和 Anthropic 靠模型能力建立的壁垒正在被快速侵蚀。</p><p>然后看 Anthropic 的反应：公开指控 DeepSeek 进行「工业级蒸馏攻击」。24,000 次 Claude 调用听起来很多，但放在工业训练的规模下其实算不上什么。真正有意思的是 Anthropic 选择公开这件事——这是一个战略行为，不是法律行为。他们在给开源阵营贴标签：「你们的能力是偷来的。」但这也暴露了一个尴尬现实：如果你的模型能力能被 24,000 次 API 调用蒸馏出来，那你的护城河到底有多深？</p><p>Ramp 的数据让故事更完整。Anthropic 企业客户一年增长 6 倍，OpenAI 首次下滑——这不是因为 ChatGPT 变差了，而是因为 Claude 在企业市场找到了精准定位。Claude in Excel、Claude in PowerPoint——Anthropic 在做的事情不是「最强 AI」，而是「最有用的 AI」。这和 OpenAI 走 ChatGPT「全能助手」路线形成了鲜明对比。a16z 的报告也证实了这一点：AI 战场从独立应用转向生产力工具嵌入。</p><p>最后，Anthropic 参与军事 AI 试点项目。这是一个我很想忽略但不能忽略的新闻。Anthropic 的整个品牌叙事建立在「AI 安全」和「负责任 AI」之上——这是它区别于 OpenAI 和 Google 的核心标签。现在它和 OpenAI、Google、xAI 一起参与军事图像分析？<strong>这说明在足够大的商业和政治压力下，「安全优先」只是一个品牌策略，不是一个不可逾越的原则。</strong>我不觉得 Anthropic 做错了什么——军事 AI 是一个复杂的话题，合理使用有其必要性。但如果你之前因为「Anthropic 最安全」而选择它，今天需要重新审视这个假设。</p><p><strong>总结：2026 年 3 月的 AI 格局正在经历一场三维重构。</strong>技术层面，开源追上闭源；商业层面，Anthropic 从安全研究机构变成企业服务巨头；地缘层面，DeepSeek V4 证明出口管制无法阻止技术扩散。每一家公司都在说自己最安全、最负责任，但每一家都在做妥协。这不是虚伪——这是现实。AI 行业已经过了「理想主义」阶段，进入了「现实政治」阶段。</p></div>""",
        "en": """<h3>📌 AI × Tech (Evening)</h3><ul><li><strong>DeepSeek V4: 1 Trillion Parameters, Open Weights — Nuclear Update for Open-Source AI</strong> — The largest known open-weight model. Reuters confirmed DeepSeek trained on Nvidia's best chips despite US export controls.<br><small>Source: <a href="http://kersai.com/ai-breakthroughs-in-2026-march-update/">KersAI</a> | <a href="https://www.reuters.com/world/china/chinas-deepseek-trained-ai-model-nvidias-best-chip-despite-us-ban-official-says-2026-02-24/">Reuters</a></small></li><li><strong>Ramp AI Index: Anthropic Enterprise Customers Up 6x in One Year, OpenAI Posts First Monthly Decline</strong> — 1 in 4 businesses on Ramp now pays Anthropic (was 1 in 25). OpenAI's 1.5% monthly drop is its largest recorded decline.<br><small>Source: <a href="https://ramp.com/velocity/ai-index-march-2026">Ramp</a></small></li><li><strong>a16z Top 100 Consumer AI Apps: Claude Enters Office Suite, Gemini Deepens Google Integration</strong> — AI battlefield shifts from standalone apps to productivity tool embedding.<br><small>Source: <a href="https://www.a16z.news/p/top-100-gen-ai-consumer-apps-march">a16z</a></small></li><li><strong>Anthropic Accuses DeepSeek of "Industrial-Scale Distillation Attacks" (~24,000 Claude Calls)</strong> — First major public IP accusation between AI companies. Strategic move to label open-source capabilities as "stolen."<br><small>Source: <a href="https://www.lesswrong.com/posts/G4M5xE3HeReisKqLc/some-models-don-t-identify-with-their-official-name">LessWrong</a></small></li><li><strong>Anthropic Joins Military AI Pilot Program — Safety-First Brand Faces New Test</strong> — Anthropic, Google, OpenAI, and xAI participate in military imagery analysis pilot. Signals that "safety-first" is a brand strategy, not an inviolable principle.<br><small>Source: <a href="https://mashable.com/article/anthropic-safety-policy-change">Mashable</a></small></li></ul><h3>🔄 Trends</h3><ul><li>Open vs closed: DeepSeek V4's 1T open weights erode closed-model moats</li><li>Anthropic's rise: 6x enterprise growth, first OpenAI decline — landscape shifting</li><li>AI IP warfare: distillation accusations bring competition to legal territory</li><li>Safety vs commerce: Anthropic's military participation tests its core narrative</li></ul><div class="rex-take"><h3>🔍 Rex's Take</h3><p><strong>Tonight's stories tell one narrative: AI is shifting from "who has the best model" to "who has the deepest ecosystem" — and nobody's hands are clean.</strong></p><p>DeepSeek V4 (1T params, open weights) is a geopolitical event — trained on Nvidia's best chips despite export controls. Anthropic's response? Publicly accusing DeepSeek of "industrial-scale distillation." But if 24,000 API calls can extract your competitive advantage, how deep is your moat really? Ramp data shows Anthropic's enterprise customers grew 6x while OpenAI posted its first decline — Claude wins by being "most useful" (Office integration) rather than "most powerful." And Anthropic joining a military AI pilot program alongside OpenAI, Google, and xAI? <strong>Under enough commercial and political pressure, "safety-first" is a brand strategy, not an inviolable principle.</strong> The AI industry has exited its idealist phase and entered realpolitik.</p></div>"""
    },
    "cover": images.get("kersai", "") or images.get("ramp", ""),
    "sources": [
        {
            "title": {"zh": "KersAI: DeepSeek V4 万亿参数", "en": "KersAI: DeepSeek V4 1T Parameters"},
            "url": "http://kersai.com/ai-breakthroughs-in-2026-march-update/",
            "image": images.get("kersai", "")
        },
        {
            "title": {"zh": "Ramp: AI 指数 2026 年 3 月", "en": "Ramp: AI Index March 2026"},
            "url": "https://ramp.com/velocity/ai-index-march-2026",
            "image": images.get("ramp", "")
        },
        {
            "title": {"zh": "a16z: Top 100 消费级 AI 应用", "en": "a16z: Top 100 Gen AI Consumer Apps"},
            "url": "https://www.a16z.news/p/top-100-gen-ai-consumer-apps-march",
            "image": images.get("a16z", "")
        },
        {
            "title": {"zh": "LessWrong: Anthropic 指控 DeepSeek 蒸馏攻击", "en": "LessWrong: Anthropic Accuses DeepSeek"},
            "url": "https://www.lesswrong.com/posts/G4M5xE3HeReisKqLc/some-models-don-t-identify-with-their-official-name",
            "image": images.get("lesswrong", "")
        },
        {
            "title": {"zh": "Mashable: Anthropic 安全政策转变", "en": "Mashable: Anthropic Safety Policy Change"},
            "url": "https://mashable.com/article/anthropic-safety-policy-change",
            "image": ""
        }
    ]
}

# Load existing issues and prepend
issues_path = "/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json"
with open(issues_path, "r", encoding="utf-8") as f:
    issues = json.load(f)

issues = [design_issue, tech_issue] + issues

with open(issues_path, "w", encoding="utf-8") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Inserted 2 new issues (design + tech evening). Total: {len(issues)} issues.")
