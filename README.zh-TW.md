# Vispawn ⚡️

<div align="center">

[![PyPI Version](https://img.shields.io/pypi/v/vispawn?logo=pypi)](https://pypi.org/project/vispawn/)
[![Python Version](https://img.shields.io/python/py-version/vispawn?logo=python)](https://www.python.org)
[![Three.js](https://img.shields.io/badge/Three.js-r160-orange?logo=three.js)](https://threejs.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/vispawn?style=social)](https://github.com/yourusername/vispawn/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/yourusername/vispawn?style=social)](https://github.com/yourusername/vispawn/network)

<br/>

> **用 AI 把任何概念變成可交互的 3D 可視化**
>
> 告別枯燥的靜態圖表，讓教學演示活起來 ✨

[English](README.md) · [简体中文](README.zh-CN.md) · [快速開始](#-快速開始) · [API 文檔](docs/api-reference.md) · [貢獻指南](docs/contributing.md)

</div>

---

## ⭐ 為什麼選擇 Vispawn？

| 傳統方式 | Vispawn |
|:---------|:-------|
| 手寫數百行 Three.js 代碼 | 📝 只需輸入一句話 |
| 幾小時甚至幾天 | ⚡ 幾秒鐘生成 |
| 需要 3D 圖形學經驗 | 🎯 零基礎也能用 |
| 靜態演示 | 🎮 互動式可操控 |

**輸入**：`"勾股定理"` → **輸出**：完整的 3D 互動式演示

---

## ✨ 核心特性

<div align="center">

| 🤖 AI 驅動 | 🔄 自主規劃 | 🎯 多維評估 |
|:-----------|:------------|:------------|
| 輸入自然語言，自動生成 Three.js 3D 代碼 | 類似 OpenClaw 的 Agent 系統，自主分解任務 | 安全檢測、語法檢查、準確性驗證、視覺效果、教學效果 |

| 📦 25+ 預設模板 | ⚡ 並行執行 | 🌐 Web 原生 |
|:----------------|:------------|:------------|
| 覆蓋數學、物理、化學核心原理 | 智能分析依賴關係，最大化並行效率 | 純前端展示，無需安裝插件 |

</div>

---

## 🚀 快速開始

### 安裝

```bash
# pip 安裝（推薦）
pip install vispawn

# 或從源碼安裝
git clone https://github.com/yourusername/vispawn.git
cd vispawn
pip install -e .
```

### 配置 API 密鑰

```bash
# 創建環境變量文件
cp .env.example .env

# 編輯 .env，添加至少一個 API 密鑰
OPENAI_API_KEY=sk-xxxx    # OpenAI
# 或
ANTHROPIC_API_KEY=sk-ant-xxxx  # Anthropic Claude
```

### 啟動服務

```bash
# 啟動服務
vispawn

# 或
python main.py
```

然後打開瀏覽器訪問：**http://localhost:8000** 🎉

---

## 📖 使用示例

### 方式一：Web 界面

打開 http://localhost:8000/app ，在輸入框中輸入：

```
四沖程發動機
```

系統會自動：
1. 🤖 分析任務複雜度
2. 📋 自主規劃執行步驟
3. ⚡ 智能調度子 Agent
4. ✅ 生成並驗證渲染效果

### 方式二：API 調用

```bash
# Agent 模式（推薦）- 自主規劃
curl -X POST http://localhost:8000/agent/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "勾股定理"}'

# 傳統模式
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "勾股定理"}'
```

```python
# Python SDK
from vispawn import process_visualization_request
import asyncio

async def main():
    result = await process_visualization_request("勾股定理")
    print(result["validation"]["recommendation"])

asyncio.run(main())
```

---

## 🏗️ 系統架構

```
用戶輸入: "勾股定理"
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│                     Main Agent                               │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  自主規劃引擎                                         │  │
│  │  - 任務複雜度分析                                    │  │
│  │  - 智能並行/串行決策                                │  │
│  │  - 子 Agent 調度                                       │  │
│  └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                    │
        ┌──────────┴──────────┐
        ▼                     ▼
   ┌─────────┐           ┌─────────┐
   │ 分析任務 │           │ 生成代碼 │
   │analyzer │ ────────▶│generator│
   └─────────┘           └─────────┘
        │                     │
        └──────────┬──────────┘
                   ▼
            ┌─────────┐
            │ 評估質量 │
            │evaluator│
            └─────────┘
                   │
                   ▼
            ┌─────────┐
            │驗證渲染 │
            │validator│
            └─────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│                     最終結果                                  │
│  - Three.js 代碼                                           │
│  - 質量評分                                                │
│  - 渲染驗證                                                │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 預設模板庫 (25+)

### 數學類

| 原理 | 演示 |
|:-----|:-----|
| 🔺 勾股定理 | a² + b² = c² 面積證明 |
| 📐 三角函數 | sin/cos 圖像動畫 |
| 📈 指數函數 | 指數增長可視化 |
| 📉 對數函數 | 對數曲線展示 |
| ⬜ 正多邊形面積 | 多邊形面積公式 |
| 🔵 圓錐體積 | V = 1/3πr²h |
| ⚪ 球體積 | V = 4/3πr³ |
| 🔺 相似三角形 | 相似判定條件 |
| 🎲 概率骰子 | 概率實驗模擬 |
| 🔢 排列組合 | 排列組合可視化 |

### 物理類

| 原理 | 演示 |
|:-----|:-----|
| ⚙️ 四沖程發動機 | 進氣→壓縮→做功→排氣 |
| 💡 光的折射 | 斯涅爾定律演示 |
| 🧲 電磁感應 | 法拉第電磁感應 |
| 🏃 自由落體 | 重力加速度演示 |
| 🌊 簡諧振動 | 彈簧振子運動 |
| 🌊 波動傳播 | 縱波與橫波 |
| 🔥 熱傳導 | 熱傳遞可視化 |
| 🌑 萬有引力 | 行星運動模擬 |
| 💥 動量守恆 | 碰撞實驗 |

### 化學類

| 原理 | 演示 |
|:-----|:-----|
| 💧 水分子結構 | H₂O 3D 模型 |
| ⚗️ 化學反應 | 反應類型演示 |
| ⚛️ 原子結構 | 原子核與電子雲 |

---

## 🛠️ 技術棧

<div align="center">

| 領域 | 技術 |
|:-----|:-----|
| 🐍 **語言** | Python 3.9+ |
| 🌐 **前端** | HTML5 + Three.js r160 |
| ⚡ **後端** | FastAPI + Uvicorn |
| 🤖 **AI** | OpenAI GPT / Anthropic Claude |
| 📦 **部署** | Docker / Railway / Vercel |

</div>

---

## 🤝 貢獻

歡迎貢獻代碼！請先閱讀 [貢獻指南](docs/contributing.md)。

```bash
# Fork 項目
# 創建特性分支
git checkout -b feature/amazing-feature

# 開發並測試
pip install -e ".[dev]"
pytest

# 提交 PR
git commit -m "Add amazing feature"
git push origin feature/amazing-feature
```

---

## 📄 許可證

MIT License - 查看 [LICENSE](LICENSE) 了解更多。

---

## 🙏 感謝

- [Three.js](https://threejs.org/) - 3D 渲染引擎
- [FastAPI](https://fastapi.tiangolo.com/) - Web 框架
- [OpenClaw](https://github.com/openclaw/openclaw) - 多智能體架構靈感（自主規劃、子 Agent 調度）
- [pi-mono](https://github.com/badlogic/pi-mono) - Agent 執行框架

---

<div align="center">

**如果這個項目對你有幫助，歡迎 ⭐ Star 支持！**

</div>
