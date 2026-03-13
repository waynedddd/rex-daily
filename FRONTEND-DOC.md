# Rex Daily — 前端技术文档

便于复用和二次开发的完整前端架构参考。

---

## 技术栈

| 层面 | 选择 |
|------|------|
| 框架 | **纯 HTML + Vanilla JS**，零依赖，单文件 |
| 数据 | 本地 JSON（`issues.json` / `inspire.json`），通过 `fetch` 加载 |
| 字体 | Google Fonts: Space Grotesk + Space Mono + Noto Sans SC |
| 部署 | 静态文件，可直接放 GitHub Pages / Netlify / 任何 CDN |

---

## 页面结构

### 1. `index.html` — Daily Digest（卡片堆叠浏览器）

**设计概念**：3D 卡片堆叠（Deck of Cards），S 形蜿蜒排列，点击展开全文阅读。

#### 布局架构

```
┌─────────────────────────────────────┐
│ Topbar: Logo | [Section▾] [Inspire] [EN] │  ← fixed, blur backdrop
├─────────────────────────────────────┤
│                                     │
│         ┌──────────┐                │
│    ┌────┤ 当前卡片  ├────┐           │  ← 3D perspective deck
│    │    └──────────┘    │           │
│    └── 前后卡片 S 形排列 ──┘           │
│                                     │
├─────────────────────────────────────┤
│ Side Nav (right): ↑ dots ↓          │  ← fixed, 右侧导航
│ Swipe Hint (bottom center)          │  ← fixed, 底部提示
└─────────────────────────────────────┘

Overlay（全屏阅读）:
┌─────────────────────────────────────┐
│ [✕ 关闭]                            │  ← sticky top
│ [封面图]                             │
│ 日期 · 标签                          │
│ 标题                                 │
│ HTML 正文（新闻 + 趋势 + Rex's Take） │
│ ── Sources ──                       │
│ [来源卡片列表]                        │
└─────────────────────────────────────┘
```

#### 核心交互

| 交互方式 | 行为 |
|---------|------|
| **滑动** | 移动端垂直滑动，桌面端水平滑动切换卡片 |
| **鼠标移动** | 桌面端鼠标偏离中心 20% 自动切换 |
| **滚轮** | 带 400ms cooldown 的卡片切换 |
| **键盘** | ← → ↑ ↓ 切换，Enter 展开，Esc 关闭 |
| **点击卡片** | 展开 Overlay 全文阅读 |
| **右侧导航** | 上下按钮 + 圆点直接跳转 |

#### 卡片布局算法（S 形蜿蜒）

```javascript
// 核心参数
const step = Math.abs(offset);        // 距当前卡片的距离
const dir = offset > 0 ? -1 : 1;     // 方向

// S 曲线：正弦摆动 + 线性漂移
const xSwing = Math.sin(step * 0.5) * 140;  // S 形振荡
const xDrift = step * 30 * dir;              // 恒定漂移
const x = xSwing * dir + xDrift;
const y = step * 60 * dir;                   // 等距 Y 间隔
const rot = Math.cos(step * 0.5) * 6 * dir;  // 跟随曲线切线旋转

const scale = Math.max(0.8, 1 - step * 0.03);
const brightness = Math.max(0.3, 1 - step * 0.15);
```

#### 卡片颜色叠加（封面主色提取）

当前卡片的封面图被缩放到 8×8 canvas 取平均色，用作背景卡片的着色叠加层：

```javascript
// 提取主色
canvas.width = 8; canvas.height = 8;
ctx.drawImage(img, 0, 0, 8, 8);
// ... 计算 RGB 均值

// 应用到非当前卡片
colorOverlay.style.background = `rgb(${r*darken}, ${g*darken}, ${b*darken})`;
colorOverlay.style.opacity = '0.92';
```

#### 状态管理

```javascript
// 持久化到 localStorage
currentLang    // 'zh' | 'en'  → localStorage('rex-lang')
currentSection // 'all' | 'design' | 'tech' → localStorage('rex-section')

// 运行时
issuesData     // 原始 JSON 数组
filtered       // 过滤后的数组
currentIndex   // 当前卡片索引
```

#### 数据源格式（`issues.json`）

```json
[
  {
    "date": "2026-03-12",
    "section": "design",
    "title": { "zh": "...", "en": "..." },
    "content": { "zh": "<html>...", "en": "<html>..." },
    "cover": "https://...",
    "sources": [
      {
        "title": { "zh": "...", "en": "..." },
        "url": "https://...",
        "image": "https://... | null"
      }
    ]
  }
]
```

---

### 2. `inspire.html` — Inspiration Board（瀑布流看板）

**设计概念**：Pinterest/Moodboard 风格瀑布流，按方向（direction）分区，带 Modal 详情弹窗。

#### 布局架构

```
┌─────────────────────────────────────┐
│ Topbar: Logo | [Daily] [Direction▾] [EN] │
├─────────────────────────────────────┤
│ Section: AI × Finance (12 shots)    │
│ ┌─────┬─────┬─────┬─────┐          │
│ │ img │ img │ img │ img │          │  ← CSS columns 瀑布流
│ │     │     ├─────┤     │          │
│ ├─────┤     │ img │     │          │
│ │ img ├─────┤     ├─────┤          │
│ │     │ Rex │     │ img │          │  ← rex-note 文字卡片穿插
│ └─────┴─────┴─────┴─────┘          │
│ Section: Content Design...          │
└─────────────────────────────────────┘

Modal（点击图片弹出）:
┌─────────────────────────────────────┐
│                              [✕]    │
│ [大图]                               │
│ Direction · Type                    │
│ 标题                                 │
│ 描述文字                              │
│ [Tag] [Tag] [Tag]                   │
│ [Source →]                          │
│ 日期                                 │
└─────────────────────────────────────┘
```

#### 瀑布流实现

纯 CSS `columns`，零 JS 布局计算：

```css
.moodboard {
  columns: 4;          /* 4 列 */
  column-gap: 6px;
}

.tile {
  break-inside: avoid; /* 防止跨列断裂 */
  margin-bottom: 6px;
}

/* 响应式 */
@media (max-width: 1100px) { .moodboard { columns: 3; } }
@media (max-width: 720px)  { .moodboard { columns: 2; column-gap: 4px; } }
```

#### Tile 类型

| 类型 | class | 特征 |
|------|-------|------|
| 图片 Pin | `.tile` | 图片 + hover 显示标题叠加层 |
| Rex Note | `.tile--rex` | 红色边框文字卡片，无图片 |

#### 方向过滤

下拉菜单按 direction 过滤，支持 "All Topics" 显示全部。每个方向有独立颜色标识。

#### 数据源格式（`inspire.json`）

```json
{
  "directions": [
    {
      "id": "finance",
      "name": "AI × 金融",
      "name_en": "AI × Finance",
      "color": "#c4a84e",
      "stats": [
        { "label": "market", "value": "$12.4B" }
      ]
    }
  ],
  "pins": [
    {
      "direction": "finance",
      "type": "case",
      "title": "...",
      "body": "中文描述",
      "body_en": "English description",
      "tags": ["Dashboard", "Dark UI"],
      "link": "https://...",
      "linkText": "Dribbble",
      "image": "https://...",
      "date": "2026-03-12"
    }
  ]
}
```

---

## 共享设计系统

### 配色

```css
--bg:           #0a0a0a          /* 主背景 */
--text:         #f5f0e8          /* 主文字（暖白） */
--text-muted:   rgba(255,255,255,0.5)
--border:       rgba(255,255,255,0.15)
--glass:        rgba(10,10,10,0.6) + backdrop-filter: blur(20px)

/* 板块颜色 */
.design:        bg rgba(196,168,78,0.3)  text #e8d48a   /* 金色 */
.tech:          bg rgba(74,138,158,0.3)   text #8ec8d8   /* 青色 */
.rex-take:      bg rgba(255,255,255,0.06) border rgba(255,255,255,0.1)
.rex-note:      bg rgba(227,51,51,0.08)   border rgba(227,51,51,0.15)
```

### 字体

```css
--font:      'Space Grotesk', 'Noto Sans SC', system-ui, sans-serif  /* 正文 */
--font-mono: 'Space Mono', monospace                                  /* 辅助信息 */
```

### 组件复用

**Topbar**（两个页面共用结构）：
- Logo 左，Controls 右
- pill 按钮：`.ctrl-btn`（圆角无底色）/ `.ctrl-btn.active`（有底色）
- 下拉菜单：`.nav-drop` → `.nav-drop-btn` + `.nav-drop-menu` → `.nav-drop-item`
- 毛玻璃背景：`rgba(10,10,10,0.6) + blur(20px)`

**语言切换**（两页共享 localStorage key `rex-lang`）：
- 中文时按钮显示 "EN"，英文时显示 "中"
- 调用 `getField(obj)` 或 `t(pin, field)` 按当前语言取值

**Overlay / Modal 动画**：
```css
/* 进入 */
opacity: 0 → 1
transform: translateY(60px) scale(0.92) → translateY(0) scale(1)
background: rgba(0,0,0,0) → rgba(0,0,0,0.9)
backdrop-filter: blur(0) → blur(20px)

/* 退出（增加 .closing class） */
反向播放，先加 .closing 再 setTimeout 移除
```

---

## 响应式断点

| 断点 | 行为变化 |
|------|---------|
| ≤ 1100px | Inspire 瀑布流 4 → 3 列 |
| ≤ 720px | Inspire 瀑布流 → 2 列 |
| ≤ 640px | Daily 卡片宽度适配、字号调整、滑动方向变为垂直、侧边导航缩小 |
| ≤ 380px | 超小屏进一步缩减 |

---

## 复用指南

### 最小可复用版本

只需 3 个文件即可运行：
1. `index.html`（Daily Digest）
2. `inspire.html`（Inspiration Board）
3. `issues.json` + `inspire.json`（数据）

### 替换数据

- 修改 `issues.json` 的内容即可更新 Daily Digest
- 修改 `inspire.json` 的 directions 和 pins 即可更新灵感板
- 所有图片通过 URL 引用，无需本地存储

### 扩展 section

在 `index.html` 的下拉菜单中增加选项，数据中增加对应 section 值即可：

```html
<button class="nav-drop-item" data-section="product" onclick="setSection('product')">Product</button>
```

### 扩展 direction

在 `inspire.json` 的 `directions` 数组中增加条目，pins 中使用对应 `direction` 值即可。

### 接入 Supabase（可选）

本地 JSON 可替换为 Supabase REST API：

```javascript
// 替换 fetch('issues.json') 为:
fetch('https://xxx.supabase.co/rest/v1/daily_briefs?order=date.desc', {
  headers: { 'apikey': 'xxx' }
})
```
