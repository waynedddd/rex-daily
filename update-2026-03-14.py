#!/usr/bin/env python3
"""Rex Daily update for 2026-03-14"""
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
    "fortune_anthropic": "https://fortune.com/2026/03/12/anthropic-pentagon-lawsuit-supply-chain-risk-china-ai-race/",
    "time_anthropic": "https://time.com/article/2026/03/11/anthropic-claude-disruptive-company-pentagon/",
    "techcrunch_atlassian": "https://techcrunch.com/2026/03/12/atlassian-follows-blocks-footsteps-and-cuts-staff-in-the-name-of-ai/",
    "adobe_graph": "https://blog.adobe.com/en/publish/2025/11/25/introducing-project-graph-creative-workflows-reimagined",
    "creativebloq": "https://www.creativebloq.com/tech/from-firefly-to-graph-how-adobe-thinks-creatives-will-use-ai-in-2026",
    "muzli": "https://muz.li/blog/best-ai-design-tools-for-ui-ux-designers-in-2026/",
    "medium_tools": "https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d",
    "toi_china": "https://timesofindia.indiatimes.com/technology/tech-news/days-after-pentagons-fight-with-anthropic-china-warns-america-on-ai-use-in-military-says-excessive-use-of-artificial-intelligence-in-military-can-/articleshow/129564489.cms",
}

images = {}
for k, u in urls.items():
    print(f"Fetching og:image for {k}...")
    images[k] = get_og_image(u)
    print(f"  -> {images[k][:80]}..." if images[k] else "  -> (none)")

design_issue = {
    "date": "2026-03-14",
    "section": "design",
    "title": {
        "zh": "Adobe Project Graph 重新定义创意工作流 · AI 设计工具从「生成」走向「编排」· 设计师的真实工具栈长什么样",
        "en": "Adobe Project Graph Redefines Creative Workflows · AI Design Tools Shift from Generation to Orchestration · What Real Designer Tool Stacks Look Like"
    },
    "content": {
        "zh": '<h3>📌 AI × 设计</h3><ul>'
            '<li><strong>Adobe Project Graph：用节点编排 AI 工作流，创意工具进入「可编程」时代</strong> — Adobe 的 Project Graph 是一个全新的节点式创意系统，让设计师可以可视化地连接 AI 模型、Adobe 工具和效果，构建可复用、可分享的工作流。更关键的是，Adobe 同时向 Creative Cloud 引入了 Runway、Flux、Nano Banana 等第三方 AI 模型。这不是一个功能更新，这是一次架构级变革：Adobe 正在从「工具提供商」转型为「创意操作系统」。'
            '<br><small>来源：<a href="https://blog.adobe.com/en/publish/2025/11/25/introducing-project-graph-creative-workflows-reimagined">Adobe Blog: Introducing Project Graph</a> | <a href="https://www.creativebloq.com/tech/from-firefly-to-graph-how-adobe-thinks-creatives-will-use-ai-in-2026">Creative Bloq: How Adobe Thinks Creatives Will Use AI in 2026</a></small></li>'
            '<li><strong>2026 年设计师的真实 AI 工具栈：不是一个工具，而是一条流水线</strong> — Muzli 和 Phygital+ 的最新指南都指向同一个趋势：顶级设计团队不是在找「最强的 AI 设计工具」，而是在搭建 AI 工具流水线——Figma AI 做自动化、Galileo/Uizard 做快速草稿、Phygital+ 做一致性量产。Medium 上一位 UX 设计师分享了他实际使用的 8 个 AI 工具，核心观点是：每个工具只解决一个环节，串起来才是生产力。'
            '<br><small>来源：<a href="https://muz.li/blog/best-ai-design-tools-for-ui-ux-designers-in-2026/">Muzli: Best AI Design Tools 2026</a> | <a href="https://phygital.plus/blog/best-ai-tools-for-designers/">Phygital+: AI for Designers 2026</a> | <a href="https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d">Medium: 8 AI Tools I Actually Use</a></small></li>'
            '<li><strong>RGD 呼吁设计师关注 AI 工具的伦理维度：训练数据、许可条款、数据政策各不相同</strong> — 加拿大注册平面设计师协会（RGD）发文强调，AI 工具在训练方式、授权模式和数据治理上差异巨大，设计师在使用前应审查每个工具的服务条款和数据政策。这不是泛泛的伦理呼吁，而是对设计师的实操建议：你用的 AI 工具，可能在法律上让你和客户都承担风险。'
            '<br><small>来源：<a href="https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026">RGD: Amplifying Creativity with AI Tools</a></small></li>'
            '</ul>'
            '<h3>🔄 趋势</h3><ul>'
            '<li><strong>从「生成」到「编排」</strong>：AI 设计工具的价值不再是单点生成，而是工作流编排和自动化</li>'
            '<li><strong>平台开放化</strong>：Adobe 引入第三方模型，Figma 有 Make，设计平台正在变成 AI 中间件</li>'
            '<li><strong>伦理合规成为设计师的新技能</strong>：不只是会用工具，还要懂工具背后的法律风险</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex 的看法</h3>'
            '<p><strong>Adobe Project Graph 是我今年看到的最重要的设计工具发布——尽管它还在开发中。</strong></p>'
            '<p>为什么这么说？因为它改变的不是「设计师能做什么」，而是「设计师如何思考工作流本身」。过去两年，AI 设计工具的主要叙事是「生成」——输入 prompt，输出设计稿。这很酷，但本质上还是在单点上做加速。Project Graph 走了一条完全不同的路：它让设计师可以像程序员一样「编排」工作流，把不同的 AI 模型、工具、效果串成一条可复用的流水线。</p>'
            '<p>这里面最聪明的一步是 Adobe 引入了 Runway、Flux 等第三方模型。这意味着 Adobe 不再试图用 Firefly 打败所有竞争对手，而是把自己变成一个「创意操作系统」——你可以在 Adobe 的框架里调用任何 AI 模型，就像开发者在操作系统上调用不同的 API。<strong>这是一个从「工具战争」到「平台战争」的转变。</strong>Figma 在做同样的事（Make + 插件生态），但 Adobe 在创意制作（而非 UI 设计）领域的护城河更深。</p>'
            '<p>再看设计师的真实工具栈。Muzli 和 Phygital+ 的指南不约而同地强调了「pipeline over prompts」——流水线比单次 prompt 重要。这和软件工程的演进路径惊人地相似：先是手写代码（手动设计），然后有了 IDE（Figma），然后有了 CI/CD 流水线（AI 工具栈），最后有了基础设施即代码（Project Graph）。<strong>我的预测：到 2026 年底，「设计系统」这个概念会从「组件库」扩展为「组件库 + AI 工作流模板」。</strong>不只是定义按钮长什么样，还要定义按钮是怎么被生成、审查、部署的。</p>'
            '<p>RGD 的伦理提醒看似无聊，实际上指向了一个正在酝酿的炸弹。当你的设计是用 AI 生成的，而那个 AI 模型的训练数据包含了未经授权的版权材料——法律责任在谁？目前没有清晰答案。对于服务企业客户的设计师来说，这不是哲学问题，而是合同风险。Adobe 引入第三方模型的同时，也在引入第三方的法律不确定性。<strong>2026 年最被低估的设计技能：不是 prompt engineering，是 AI 工具的合规审查。</strong></p>'
            '</div>',
        "en": '<h3>📌 AI × Design</h3><ul>'
            '<li><strong>Adobe Project Graph: Node-Based AI Workflow Orchestration</strong> — A new creative system letting designers visually connect AI models, tools, and effects into reusable workflows. Adobe also added third-party models (Runway, Flux, Nano Banana) to Creative Cloud, transforming from tool provider to creative OS.<br><small>Source: <a href="https://blog.adobe.com/en/publish/2025/11/25/introducing-project-graph-creative-workflows-reimagined">Adobe Blog</a> | <a href="https://www.creativebloq.com/tech/from-firefly-to-graph-how-adobe-thinks-creatives-will-use-ai-in-2026">Creative Bloq</a></small></li>'
            '<li><strong>Real Designer AI Stacks in 2026: Pipelines, Not Single Tools</strong> — Top teams build AI pipelines: Figma AI for automation, Galileo/Uizard for drafts, Phygital+ for consistent production. Each tool solves one stage; the pipeline is the product.<br><small>Source: <a href="https://muz.li/blog/best-ai-design-tools-for-ui-ux-designers-in-2026/">Muzli</a> | <a href="https://phygital.plus/blog/best-ai-tools-for-designers/">Phygital+</a> | <a href="https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d">Medium</a></small></li>'
            '<li><strong>RGD Urges Designers to Audit AI Tool Ethics</strong> — Training data, licensing, and data policies vary wildly across AI tools. Designers should review terms before client work — legal risk is real.<br><small>Source: <a href="https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026">RGD</a></small></li>'
            '</ul>'
            '<h3>🔄 Trends</h3><ul>'
            '<li>From generation to orchestration: workflow pipelines > single-point AI tools</li>'
            '<li>Platform openness: Adobe adds third-party models, Figma has Make — design platforms becoming AI middleware</li>'
            '<li>Compliance as a new design skill: knowing tool legalities matters as much as using them</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex\'s Take</h3>'
            '<p><strong>Adobe Project Graph is the most important design tool announcement of the year — even though it\'s still in development.</strong></p>'
            '<p>It shifts AI design from "generation" to "orchestration." By adding third-party models, Adobe is becoming a creative OS rather than competing tool-by-tool. The parallel to software engineering is striking: manual code → IDE → CI/CD → infrastructure-as-code. Design is following the same arc. <strong>By end of 2026, "design systems" will expand from component libraries to component libraries + AI workflow templates.</strong> The most underrated design skill of 2026 isn\'t prompt engineering — it\'s AI tool compliance auditing.</p>'
            '</div>'
    },
    "cover": images.get("adobe_graph", ""),
    "sources": [
        {
            "title": {"zh": "Adobe Blog: Project Graph 发布", "en": "Adobe Blog: Introducing Project Graph"},
            "url": "https://blog.adobe.com/en/publish/2025/11/25/introducing-project-graph-creative-workflows-reimagined",
            "image": images.get("adobe_graph", "")
        },
        {
            "title": {"zh": "Creative Bloq: Adobe 如何看待 2026 年创意 AI", "en": "Creative Bloq: How Adobe Thinks Creatives Will Use AI in 2026"},
            "url": "https://www.creativebloq.com/tech/from-firefly-to-graph-how-adobe-thinks-creatives-will-use-ai-in-2026",
            "image": images.get("creativebloq", "")
        },
        {
            "title": {"zh": "Muzli: 2026 最佳 AI 设计工具", "en": "Muzli: Best AI Design Tools 2026"},
            "url": "https://muz.li/blog/best-ai-design-tools-for-ui-ux-designers-in-2026/",
            "image": images.get("muzli", "")
        },
        {
            "title": {"zh": "Medium: 我实际使用的 8 个 AI UX 工具", "en": "Medium: 8 AI Tools I Actually Use"},
            "url": "https://medium.muz.li/the-8-top-ai-tools-i-actually-use-in-my-ux-design-workflow-2026-8223a201753d",
            "image": images.get("medium_tools", "")
        },
        {
            "title": {"zh": "RGD: 用 AI 工具放大创意", "en": "RGD: Amplifying Creativity with AI Tools"},
            "url": "https://rgd.ca/articles/2026-amplifying-creativity-with-ai-tools-for-designers-in-2026",
            "image": ""
        }
    ]
}

tech_issue = {
    "date": "2026-03-14",
    "section": "tech",
    "title": {
        "zh": "Anthropic 起诉五角大楼 · AI 军事化争议白热化 · Atlassian 裁员 1600 人押注 AI · 中国警告军事 AI 失控风险",
        "en": "Anthropic Sues the Pentagon · AI Militarization Debate Intensifies · Atlassian Cuts 1600 Jobs for AI Pivot · China Warns on Military AI"
    },
    "content": {
        "zh": '<h3>📌 AI × 科技</h3><ul>'
            '<li><strong>Anthropic 起诉五角大楼：拒绝移除 Claude 安全限制，被认定为「供应链风险」</strong> — 这是 2026 年最具戏剧性的 AI 事件。Anthropic 在 2025 年 7 月与五角大楼签下 2 亿美元合同，Claude 成为首个部署在美军机密网络的前沿 AI 模型。但当五角大楼要求 Anthropic 移除 Claude 的安全限制（包括自主武器系统和大规模公民监控的红线）时，CEO Dario Amodei 拒绝了。特朗普政府随即将 Anthropic 列为「供应链风险」——这个标签此前只用于外国对手——并下令所有联邦机构停止使用 Claude。Anthropic 已提起两项诉讼。讽刺的是：五角大楼在马杜罗突袭和伊朗战争中仍在使用 Claude。'
            '<br><small>来源：<a href="https://fortune.com/2026/03/12/anthropic-pentagon-lawsuit-supply-chain-risk-china-ai-race/">Fortune: Anthropic 起诉五角大楼</a> | <a href="https://time.com/article/2026/03/11/anthropic-claude-disruptive-company-pentagon/">TIME: Anthropic 如何成为最具颠覆性的公司</a> | <a href="https://www.cnbc.com/2026/03/09/anthropic-was-the-pentagons-choice-for-ai-now-its-banned-and-experts-are-worried.html">CNBC 深度报道</a></small></li>'
            '<li><strong>中国国防部回应：军事 AI 必须由人类主导，防止失控</strong> — 就在 Anthropic 与五角大楼对抗几天后，中国国防部发表声明，呼吁军事 AI 应用保持人类主导，警告过度使用可能导致失控。这是一个微妙的外交信号：中国在 AI 军事化议题上选择了「负责任」的叙事定位。'
            '<br><small>来源：<a href="https://timesofindia.indiatimes.com/technology/tech-news/days-after-pentagons-fight-with-anthropic-china-warns-america-on-ai-use-in-military-says-excessive-use-of-artificial-intelligence-in-military-can-/articleshow/129564489.cms">Times of India</a></small></li>'
            '<li><strong>Atlassian 裁员 1600 人（10%），全力押注 AI：股价反而上涨</strong> — 澳大利亚软件巨头 Atlassian 裁减 10% 员工，将资金转向 AI 和企业销售。TechCrunch 指出这与 Block 的策略如出一辙。最令人不安的细节：裁员公告后股价上涨。市场正在奖励「用 AI 替代人类」的公司。'
            '<br><small>来源：<a href="https://techcrunch.com/2026/03/12/atlassian-follows-blocks-footsteps-and-cuts-staff-in-the-name-of-ai/">TechCrunch</a> | <a href="https://www.theguardian.com/technology/2026/mar/12/atlassian-layoffs-software-technology-ai-push-mike-cannon-brookes-asx">The Guardian</a> | <a href="https://www.reuters.com/technology/atlassian-lay-off-about-1600-people-pivot-ai-2026-03-11/">Reuters</a></small></li>'
            '</ul>'
            '<h3>🔄 趋势</h3><ul>'
            '<li><strong>AI 安全红线之争</strong>：Anthropic 成为第一家因坚守安全底线而与政府对抗的 AI 公司</li>'
            '<li><strong>AI 军事化的全球博弈</strong>：美国内部分裂（五角大楼 vs Anthropic），中国趁机占据道德高地</li>'
            '<li><strong>「AI 裁员」成为新常态</strong>：市场奖励裁员、惩罚保守，企业没有退路</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex 的看法</h3>'
            '<p><strong>Anthropic vs 五角大楼不是一场商业纠纷，它是 AI 时代的「奥本海默时刻」。</strong></p>'
            '<p>让我把这件事的荒诞之处说清楚。2025 年 7 月，Anthropic 与五角大楼签约，Claude 成为美军机密网络里跑的第一个前沿 AI。几个月后，五角大楼说：把安全限制去掉，我们要完全不受限地使用。Amodei 的红线很具体：不做自主武器，不做公民大规模监控。五角大楼的回应是把 Anthropic 列为「供应链风险」——请注意，这个标签此前只用过华为和卡巴斯基这类外国实体。一家美国公司，因为拒绝移除 AI 安全限制，被自己的政府当作国家安全威胁。</p>'
            '<p>更荒诞的是：五角大楼一边把 Anthropic 列为风险，一边在伊朗战争和马杜罗突袭中继续使用 Claude。如果它真是供应链风险，为什么还在用？如果不是，为什么要禁？答案很明显：这不是安全评估，这是政治报复。Amodei 在 TIME 的采访中说得很直白：「我们没有像 Sam Altman 那样给特朗普唱赞歌，我们支持 AI 监管，我们说了关于就业替代的真话。」</p>'
            '<p>这件事的影响远超 Anthropic 一家公司。<strong>它给每一家 AI 公司传递了一个信号：如果你的安全底线与政府的使用意图冲突，你可能会失去所有联邦业务。</strong>AWS、Google Cloud、Azure 都服务于政府客户，而这些云平台上都跑着 Anthropic 的产品。供应链风险认定意味着每个联邦承包商都可能被要求证明自己没有使用 Anthropic 的技术。这是一颗核弹级的商业武器。</p>'
            '<p>中国的时机选择堪称教科书级别。就在美国政府因为 AI 公司「太安全」而惩罚它的时候，中国国防部站出来说「军事 AI 必须由人类主导」。这当然是外交表演——没有人天真到相信中国会自我限制 AI 军事应用——但叙事上的高明在于：它让美国看起来是那个不负责任的一方。Anthropic 被本国政府打压，中国却在呼吁节制。国际舆论的天平很微妙。</p>'
            '<p>最后说 Atlassian。1600 人被裁，股价上涨。这六个字就是 2026 年科技行业的墓志铭。市场已经建立了一个残酷的反馈循环：宣布裁员 → 声称押注 AI → 股价上涨 → 其他公司效仿。Morgan Stanley 说 AI 是「通缩力量」，Atlassian 正在证明这一点。<strong>我的判断：到 2026 年底，至少还会有 5-10 家大型科技公司以「AI 转型」为名裁员 10% 以上。</strong>不是因为 AI 真的能替代那么多人，而是因为市场会奖励这个叙事。</p>'
            '</div>',
        "en": '<h3>📌 AI × Tech</h3><ul>'
            '<li><strong>Anthropic Sues Pentagon Over "Supply Chain Risk" Designation</strong> — After refusing to remove Claude\'s safety restrictions (no autonomous weapons, no mass surveillance), Trump admin banned Anthropic from all federal agencies. Two lawsuits filed. Pentagon still uses Claude in Iran and Venezuela operations.<br><small>Source: <a href="https://fortune.com/2026/03/12/anthropic-pentagon-lawsuit-supply-chain-risk-china-ai-race/">Fortune</a> | <a href="https://time.com/article/2026/03/11/anthropic-claude-disruptive-company-pentagon/">TIME</a> | <a href="https://www.cnbc.com/2026/03/09/anthropic-was-the-pentagons-choice-for-ai-now-its-banned-and-experts-are-worried.html">CNBC</a></small></li>'
            '<li><strong>China Warns Military AI Must Stay Human-Led</strong> — Days after Pentagon-Anthropic clash, China\'s Defense Ministry calls for restraint in military AI use. Strategic narrative positioning.<br><small>Source: <a href="https://timesofindia.indiatimes.com/technology/tech-news/days-after-pentagons-fight-with-anthropic-china-warns-america-on-ai-use-in-military-says-excessive-use-of-artificial-intelligence-in-military-can-/articleshow/129564489.cms">Times of India</a></small></li>'
            '<li><strong>Atlassian Cuts 1600 Jobs (10%) for AI Pivot — Stock Rises</strong> — Following Block\'s playbook. Market rewards "replace humans with AI" narrative.<br><small>Source: <a href="https://techcrunch.com/2026/03/12/atlassian-follows-blocks-footsteps-and-cuts-staff-in-the-name-of-ai/">TechCrunch</a> | <a href="https://www.theguardian.com/technology/2026/mar/12/atlassian-layoffs-software-technology-ai-push-mike-cannon-brookes-asx">The Guardian</a></small></li>'
            '</ul>'
            '<h3>🔄 Trends</h3><ul>'
            '<li>AI safety red lines: Anthropic is the first AI company to fight its own government over safety guardrails</li>'
            '<li>Global AI militarization chess: US internally divided, China seizes moral high ground</li>'
            '<li>"AI layoffs" as the new normal: markets reward cuts, punish caution</li>'
            '</ul>'
            '<div class="rex-take"><h3>🔍 Rex\'s Take</h3>'
            '<p><strong>Anthropic vs Pentagon is the "Oppenheimer moment" of the AI era.</strong></p>'
            '<p>A US company, punished by its own government for refusing to remove AI safety limits — designated a "supply chain risk" alongside Huawei and Kaspersky. The Pentagon still uses Claude in active operations while calling it a risk. This isn\'t security assessment; it\'s political retaliation. The message to every AI company: your safety principles may cost you all federal business. China\'s timing is textbook — calling for AI restraint while America punishes its safest AI company. Atlassian\'s layoffs (stock up on 1600 cuts) complete the picture: <strong>by end of 2026, expect 5-10 more major tech companies to cut 10%+ "for AI" — not because AI replaces that many people, but because markets reward the narrative.</strong></p>'
            '</div>'
    },
    "cover": images.get("fortune_anthropic") or images.get("time_anthropic", ""),
    "sources": [
        {
            "title": {"zh": "Fortune: Anthropic 起诉五角大楼", "en": "Fortune: Anthropic Sues Pentagon"},
            "url": "https://fortune.com/2026/03/12/anthropic-pentagon-lawsuit-supply-chain-risk-china-ai-race/",
            "image": images.get("fortune_anthropic", "")
        },
        {
            "title": {"zh": "TIME: Anthropic 如何成为最具颠覆性的公司", "en": "TIME: How Anthropic Became Most Disruptive"},
            "url": "https://time.com/article/2026/03/11/anthropic-claude-disruptive-company-pentagon/",
            "image": images.get("time_anthropic", "")
        },
        {
            "title": {"zh": "CNBC: Anthropic 深度报道", "en": "CNBC: Anthropic Deep Dive"},
            "url": "https://www.cnbc.com/2026/03/09/anthropic-was-the-pentagons-choice-for-ai-now-its-banned-and-experts-are-worried.html",
            "image": ""
        },
        {
            "title": {"zh": "TechCrunch: Atlassian 裁员 1600 人", "en": "TechCrunch: Atlassian Cuts 1600 Jobs"},
            "url": "https://techcrunch.com/2026/03/12/atlassian-follows-blocks-footsteps-and-cuts-staff-in-the-name-of-ai/",
            "image": images.get("techcrunch_atlassian", "")
        },
        {
            "title": {"zh": "中国警告军事 AI 失控风险", "en": "China Warns on Military AI"},
            "url": "https://timesofindia.indiatimes.com/technology/tech-news/days-after-pentagons-fight-with-anthropic-china-warns-america-on-ai-use-in-military-says-excessive-use-of-artificial-intelligence-in-military-can-/articleshow/129564489.cms",
            "image": images.get("toi_china", "")
        }
    ]
}

# Load existing issues and prepend
issues_path = "/Users/wayne/.openclaw/workspace-researcher/rex-daily/issues.json"
with open(issues_path, "r") as f:
    issues = json.load(f)

issues = [design_issue, tech_issue] + issues

with open(issues_path, "w") as f:
    json.dump(issues, f, ensure_ascii=False, indent=2)

print(f"\n✅ Written {len(issues)} issues to issues.json")
print(f"  - Design: {design_issue['title']['zh'][:40]}...")
print(f"  - Tech: {tech_issue['title']['zh'][:40]}...")
