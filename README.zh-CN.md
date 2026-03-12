# Vispawn ⚡️

<div align="center">

[![PyPI Version](https://img.shields.io/pypi/v/vispawn?logo=pypi)](https://pypi.org/project/vispawn/)
[![Python Version](https://img.shields.io/python/py-version/vispawn?logo=python)](https://www.python.org)
[![Three.js](https://img.shields.io/badge/Three.js-r160-orange?logo=three.js)](https://threejs.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/vispawn?style=social)](https://github.com/yourusername/vispawn/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/yourusername/vispawn?style=social)](https://github.com/yourusername/vispawn/network)

<br/>

> **用 AI 把任何概念变成可交互的 3D 可视化**
>
> 告别枯燥的静态图表，让教学演示活起来 ✨

[English](README.md) · [简体中文](README.zh-CN.md) · [繁体中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [快速开始](#-快速开始) · [API 文档](docs/api-reference.md) · [贡献指南](docs/contributing.md)

</div>

---

## ⭐ 为什么选择 Vispawn？

| 传统方式 | Vispawn |
|:---------|:-------|
| 手写数百行 Three.js 代码 | 📝 只需输入一句话 |
| 几小时甚至几天 | ⚡ 几秒钟生成 |
| 需要 3D 图形学经验 | 🎯 零基础也能用 |
| 静态演示 | 🎮 交互式可操控 |

**输入**：`"勾股定理"` → **输出**：完整的 3D 交互式演示

---

## ✨ 核心特性

<div align="center">

| 🤖 AI 驱动 | 🔄 自主规划 | 🎯 多维评估 |
|:-----------|:------------|:------------|
| 输入自然语言，自动生成 Three.js 3D 代码 | 类似 OpenClaw 的 Agent 系统，自主分解任务 | 安全检测、语法检查、准确性验证、视觉效果，教学效果 |

| 📦 25+ 预设模板 | ⚡ 并行执行 | 🌐 Web 原生 |
|:----------------|:------------|:------------|
| 覆盖数学、物理、化学核心原理 | 智能分析依赖关系，最大化并行效率 | 纯前端展示，无需安装插件 |

</div>

---

## 🚀 快速开始

### 安装

```bash
# pip 安装（推荐）
pip install vispawn

# 或从源码安装
git clone https://github.com/yourusername/vispawn.git
cd vispawn
pip install -e .
```

### 配置 API 密钥

```bash
# 创建环境变量文件
cp .env.example .env

# 编辑 .env，添加至少一个 API 密钥
OPENAI_API_KEY=sk-xxxx    # OpenAI
# 或
ANTHROPIC_API_KEY=sk-ant-xxxx  # Anthropic Claude
```

### 启动服务

```bash
# 启动服务
vispawn

# 或
python main.py
```

然后打开浏览器访问：**http://localhost:8000** 🎉

---

## 📖 使用示例

### 方式一：Web 界面

打开 http://localhost:8000/app ，在输入框中输入：

```
四冲程发动机
```

系统会自动：
1. 🤖 分析任务复杂度
2. 📋 自主规划执行步骤
3. ⚡ 智能调度子 Agent
4. ✅ 生成并验证渲染效果

### 方式二：API 调用

```bash
# Agent 模式（推荐）- 自主规划
curl -X POST http://localhost:8000/agent/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "勾股定理"}'

# 传统模式
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

## 🏗️ 系统架构

```
用户输入: "勾股定理"
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│                     Main Agent                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  自主规划引擎                                       │    │
│  │  - 任务复杂度分析                                  │    │
│  │  - 智能并行/串行决策                               │    │
│  │  - 子 Agent 调度                                    │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                    │
        ┌──────────┴──────────┐
        ▼                     ▼
   ┌─────────┐           ┌─────────┐
   │ 分析任务 │           │ 生成代码 │
   │analyzer │ ────────▶│generator│
   └─────────┘           └─────────┘
        │                     │
        └──────────┬──────────┘
                   ▼
            ┌─────────┐
            │ 评估质量 │
            │evaluator│
            └─────────┘
                   │
                   ▼
            ┌─────────┐
            │验证渲染 │
            │validator│
            └─────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│                     最终结果                                 │
│  - Three.js 代码                                         │
│  - 质量评分                                              │
│  - 渲染验证                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 预设模板库 (25+)

### 数学类

| 原理 | 演示 |
|:-----|:-----|
| 🔺 勾股定理 | a² + b² = c² 面积证明 |
| 📐 三角函数 | sin/cos 图像动画 |
| 📈 指数函数 | 指数增长可视化 |
| 📉 对数函数 | 对数曲线展示 |
| ⬜ 正多边形面积 | 多边形面积公式 |
| 🔵 圆锥体积 | V = 1/3πr²h |
| ⚪ 球体积 | V = 4/3πr³ |
| 🔺 相似三角形 | 相似判定条件 |
| 🎲 概率骰子 | 概率实验模拟 |
| 🔢 排列组合 | 排列组合可视化 |

### 物理类

| 原理 | 演示 |
|:-----|:-----|
| ⚙️ 四冲程发动机 | 进气→压缩→做功→排气 |
| 💡 光的折射 | 斯涅尔定律演示 |
| 🧲 电磁感应 | 法拉第电磁感应 |
| 🏃 自由落体 | 重力加速度演示 |
| 🌊 简谐振动 | 弹簧振子运动 |
| 🌊 波动传播 | 纵波与横波 |
| 🔥 热传导 | 热传递可视化 |
| 🌑 万有引力 | 行星运动模拟 |
| 💥 动量守恒 | 碰撞实验 |

### 化学类

| 原理 | 演示 |
|:-----|:-----|
| 💧 水分子结构 | H₂O 3D 模型 |
| ⚗️ 化学反应 | 反应类型演示 |
| ⚛️ 原子结构 | 原子核与电子云 |

---

## 🛠️ 技术栈

<div align="center">

| 领域 | 技术 |
|:-----|:-----|
| 🐍 **语言** | Python 3.9+ |
| 🌐 **前端** | HTML5 + Three.js r160 |
| ⚡ **后端** | FastAPI + Uvicorn |
| 🤖 **AI** | OpenAI GPT / Anthropic Claude |
| 📦 **部署** | Docker / Railway / Vercel |

</div>

---

## 🤝 贡献

欢迎贡献代码！请先阅读 [贡献指南](docs/contributing.md)。

```bash
# Fork 项目
# 创建特性分支
git checkout -b feature/amazing-feature

# 开发并测试
pip install -e ".[dev]"
pytest

# 提交 PR
git commit -m "Add amazing feature"
git push origin feature/amazing-feature
```

### 贡献者

[![Contributors](https://contrib.rocks/image?repo=yourusername/vispawn)](https://github.com/yourusername/vispawn/graphs/contributors)

---

## 📄 许可证

MIT License - 查看 [LICENSE](LICENSE) 了解更多。

---

## 🙏 感谢

- [Three.js](https://threejs.org/) - 3D 渲染引擎
- [FastAPI](https://fastapi.tiangolo.com/) - Web 框架
- [OpenClaw](https://github.com/openclaw/openclaw) - 多智能体架构灵感（自主规划、子 Agent 调度）
- [pi-mono](https://github.com/badlogic/pi-mono) - Agent 执行框架

---

<div align="center">

**如果这个项目对你有帮助，欢迎 ⭐ Star 支持！**

[![Star](https://img.shields.io/github/stars/yourusername/vispawn?style=social)](https://github.com/yourusername/vispawn/stargazers)

</div>
