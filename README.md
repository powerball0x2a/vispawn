# Vispawn ⚡️

<div align="center">

[![PyPI Version](https://img.shields.io/pypi/v/vispawn?logo=pypi)](https://pypi.org/project/vispawn/)
[![Python Version](https://img.shields.io/python/py-version/vispawn?logo=python)](https://www.python.org)
[![Three.js](https://img.shields.io/badge/Three.js-r160-orange?logo=three.js)](https://threejs.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/vispawn?style=social)](https://github.com/yourusername/vispawn/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/yourusername/vispawn?style=social)](https://github.com/yourusername/vispawn/network)
[![Last Commit](https://img.shields.io/github/last-commit/yourusername/vispawn)](https://github.com/yourusername/vispawn/commits)
[![Contributors](https://img.shields.io/github/contributors/yourusername/vispawn)](https://github.com/yourusername/vispawn/graphs/contributors)

<br/>

> **Turn any concept into interactive 3D visualizations with AI**
>
> Say goodbye to boring static charts, bring your teaching to life ✨

[English](README.md) · [快速开始](#-快速开始) · [API Docs](docs/api-reference.md) · [Contributing](docs/contributing.md)

</div>

---

## ⭐ Why Vispawn?

| Traditional | Vispawn |
|:------------|:--------|
| Write hundreds of lines of Three.js code | 📝 Just type a sentence |
| Hours or even days | ⚡ Seconds to generate |
| Requires 3D graphics experience | 🎯 Zero baseline needed |
| Static demos | 🎮 Interactive & controllable |

**Input**: `"Pythagorean theorem"` → **Output**: Complete 3D interactive demo

---

## ✨ Features

<div align="center">

| 🤖 AI-Powered | 🔄 Autonomous Planning | 🎯 Multi-Dimensional Evaluation |
|:--------------|:---------------------|:--------------------------------|
| Natural language input, auto-generates Three.js 3D code | OpenClaw-like Agent system with autonomous task decomposition | Security, syntax, accuracy, visual quality, pedagogy checks |

| 📦 25+ Templates | ⚡ Parallel Execution | 🌐 Web Native |
|:-----------------|:---------------------|:--------------|
| Math, Physics, Chemistry core concepts | Smart dependency analysis, maximized parallel efficiency | Pure frontend, no plugins needed |

</div>

---

## 🚀 Quick Start

### Installation

```bash
# pip install (recommended)
pip install vispawn

# or from source
git clone https://github.com/yourusername/vispawn.git
cd vispawn
pip install -e .
```

### Configure API Key

```bash
# Create env file
cp .env.example .env

# Edit .env, add at least one API key
OPENAI_API_KEY=sk-xxxx    # OpenAI
# or
ANTHROPIC_API_KEY=sk-ant-xxxx  # Anthropic Claude
```

### Run Service

```bash
# Start service
vispawn

# or
python main.py
```

Then open browser: **http://localhost:8000** 🎉

---

## 📖 Usage Examples

### Option 1: Web Interface

Open http://localhost:8000/app, enter:

```
Four-stroke engine
```

System will:
1. 🤖 Analyze task complexity
2. 📋 Auto-plan execution steps
3. ⚡ Smart schedule sub-agents
4. ✅ Generate and validate rendering

### Option 2: API

```bash
# Agent mode (recommended) - autonomous planning
curl -X POST http://localhost:8000/agent/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "Pythagorean theorem"}'

# Traditional mode
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "Pythagorean theorem"}'
```

```python
# Python SDK
from vispawn import process_visualization_request
import asyncio

async def main():
    result = await process_visualization_request("Pythagorean theorem")
    print(result["validation"]["recommendation"])

asyncio.run(main())
```

---

## 🏗️ Architecture

```
User Input: "Pythagorean theorem"
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│                     Main Agent                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Autonomous Planning Engine                         │    │
│  │  - Task complexity analysis                         │    │
│  │  - Smart parallel/serial decision                  │    │
│  │  - Sub-agent scheduling                            │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                    │
        ┌──────────┴──────────┐
        ▼                     ▼
   ┌─────────┐           ┌─────────┐
   │Analyze  │           │Generate │
   │analyzer │ ────────▶│generator│
   └─────────┘           └─────────┘
        │                     │
        └──────────┬──────────┘
                   ▼
            ┌─────────┐
            │Evaluate │
            │evaluator│
            └─────────┘
                   │
                   ▼
            ┌─────────┐
            │Validate │
            │validator│
            └─────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│                     Final Result                             │
│  - Three.js code                                          │
│  - Quality score                                          │
│  - Rendering validation                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 Templates (25+)

### Math

| Concept | Demo |
|:--------|:-----|
| 🔺 Pythagorean Theorem | a² + b² = c² area proof |
| 📐 Trigonometry | sin/cos graph animation |
| 📈 Exponential Function | Exponential growth |
| 📉 Logarithmic Function | Log curve |
| ⬜ Regular Polygon Area | Polygon area formula |
| 🔵 Cone Volume | V = 1/3πr²h |
| ⚪ Sphere Volume | V = 4/3πr³ |
| 🔺 Similar Triangles | Similarity criteria |
| 🎲 Probability Dice | Probability experiment |
| 🔢 Permutations | Permutations visualization |

### Physics

| Concept | Demo |
|:--------|:-----|
| ⚙️ Four-stroke Engine | Intake→Compression→Power→Exhaust |
| 💡 Light Refraction | Snell's law demo |
| 🧲 Electromagnetic Induction | Faraday's law |
| 🏃 Free Fall | Gravity acceleration |
| 🌊 Simple Harmonic Motion | Spring oscillator |
| 🌊 Wave Propagation | Longitudinal & transverse waves |
| 🔥 Heat Transfer | Heat conduction |
| 🌑 Universal Gravitation | Planetary motion |
| 💥 Momentum Conservation | Collision experiment |

### Chemistry

| Concept | Demo |
|:--------|:-----|
| 💧 Water Molecule | H₂O 3D model |
| ⚗️ Chemical Reactions | Reaction types |
| ⚛️ Atomic Structure | Nucleus & electron cloud |

---

## 🛠️ Tech Stack

<div align="center">

| Area | Technology |
|:-----|:-----------|
| 🐍 **Language** | Python 3.9+ |
| 🌐 **Frontend** | HTML5 + Three.js r160 |
| ⚡ **Backend** | FastAPI + Uvicorn |
| 🤖 **AI** | OpenAI GPT / Anthropic Claude |
| 📦 **Deploy** | Docker / Railway / Vercel |

</div>

---

## 🤝 Contributing

Contributions welcome! Please read [Contributing Guide](docs/contributing.md) first.

```bash
# Fork the project
# Create feature branch
git checkout -b feature/amazing-feature

# Develop and test
pip install -e ".[dev]"
pytest

# Submit PR
git commit -m "Add amazing feature"
git push origin feature/amazing-feature
```

### Contributors

[![Contributors](https://contrib.rocks/image?repo=yourusername/vispawn)](https://github.com/yourusername/vispawn/graphs/contributors)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- [Three.js](https://threejs.org/) - 3D rendering engine
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [OpenClaw](https://github.com/openclaw/openclaw) - Agent architecture inspiration (multi-agent system, autonomous planning, sub-agent spawning)
- [pi-mono](https://github.com/badlogic/pi-mono) - Agent execution framework

---

<div align="center">

**If this project helps you, please ⭐ Star!**

[![Star](https://img.shields.io/github/stars/yourusername/vispawn?style=social)](https://github.com/yourusername/vispawn/stargazers)

</div>
