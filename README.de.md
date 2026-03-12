# Vispawn ⚡️

<div align="center">

[![PyPI Version](https://img.shields.io/pypi/v/vispawn?logo=pypi)](https://pypi.org/project/vispawn/)
[![Python Version](https://img.shields.io/python/py-version/vispawn?logo=python)](https://www.python.org)
[![Three.js](https://img.shields.io/badge/Three.js-r160-orange?logo=three.js)](https://threejs.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/powerball0x2a/vispawn?style=social)](https://github.com/powerball0x2a/vispawn/stargazers)

<br/>

> **Verwandeln Sie jedes Konzept mit KI in interaktive 3D-Visualisierungen**
>
> Verabschieden Sie sich von langweiligen statischen Diagrammen und erwecken Sie Ihren Unterricht zum Leben ✨

[English](README.md) · [简体中文](README.zh-CN.md) · [繁体中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Français](README.fr.md) · [Schnellstart](#-schnellstart) · [API Docs](docs/api-reference.md) · [Contributing](docs/contributing.md)

</div>

---

## ⭐ Warum Vispawn?

| Traditionell | Vispawn |
|:-------------|:---------|
| Hunderte Zeilen Three.js-Code schreiben | 📝 Nur einen Satz eingeben |
| Stunden oder sogar Tage | ⚡ In Sekunden generiert |
| 3D-Grafik-Erfahrung erforderlich | 🎯 Kein Vorwissen nötig |
| Statische Demos | 🎮 Interaktiv steuerbar |

**Eingabe**: `"Satz des Pythagoras"` → **Ausgabe**: Vollständige 3D-interaktive Demo

---

## ✨ Funktionen

<div align="center">

| 🤖 KI-gesteuert | 🔄 Autonome Planung | 🎯 Mehrdimensionale Bewertung |
|:----------------|:--------------------|:------------------------------|
| Natürliche Spracheingabe, automatische Three.js 3D-Code-Generierung | OpenClaw-ähnliches Agent-System mit autonomer Aufgabenverteilung | Sicherheits-, Syntax-, Genauigkeits-, visuelle Qualitäts- und Pädagogikprüfungen |

| 📦 25+ Vorlagen | ⚡ Parallele Ausführung | 🌐 Web-nativ |
|:----------------|:------------------------|:-------------|
| Deckt Kernkonzepte aus Mathematik, Physik und Chemie ab | Intelligente Abhängigkeitsanalyse, maximale Parallelisierung | Reines Frontend, keine Plugins nötig |

</div>

---

## 🚀 Schnellstart

### Installation

```bash
# pip (empfohlen)
pip install vispawn

# oder aus den Quellen
git clone https://github.com/powerball0x2a/vispawn.git
cd vispawn
pip install -e .
```

### API-Schlüssel konfigurieren

```bash
# .env-Datei erstellen
cp .env.example .env

# .env bearbeiten, API-Schlüssel hinzufügen
OPENAI_API_KEY=sk-xxxx    # OpenAI
# oder
ANTHROPIC_API_KEY=sk-ant-xxxx  # Anthropic Claude
```

### Service starten

```bash
# Service starten
vispawn

# oder
python main.py
```

Im Browser öffnen: **http://localhost:8000** 🎉

---

## 📖 Verwendungsbeispiele

### Option 1: Web-Interface

Öffnen Sie http://localhost:8000/app, eingeben:

```
Viertaktmotor
```

Das System:
1. 🤖 Analysiert die Aufgabenkomplexität
2. 📋 Plant die Ausführungsschritte autonom
3. ⚡ Plant Sub-Agents intelligent
4. ✅ Generiert und validiert das Rendering

### Option 2: API

```bash
# Agent-Modus (empfohlen) - autonome Planung
curl -X POST http://localhost:8000/agent/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "Satz des Pythagoras"}'
```

---

## 🏗️ Architektur

```
User Input: "Satz des Pythagoras"
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
│  - Three.js code                                           │
│  - Quality score                                           │
│  - Rendering validation                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 Vorlagen (25+)

### Mathematik

| Konzept | Demo |
|:--------|:-----|
| 🔺 Satz des Pythagoras | a² + b² = c² Flächenbeweis |
| 📐 Trigonometrie | Sinus/Kosinus Graph-Animation |
| 📈 Exponentialfunktion | Exponentielles Wachstum |
| 📉 Logarithmusfunktion | Log-Kurve |
| ⬜ Regelmäßiges Polygon | Polygon-Flächenformel |
| 🔵 Kegelvolumen | V = 1/3πr²h |
| ⚪ Kugelvolumen | V = 4/3πr³ |
| 🔺 Ähnliche Dreiecke | Ähnlichkeitskriterien |
| 🎲 Wahrscheinlichkeitswürfel | Wahrscheinlichkeitsexperiment |
| 🔢 Permutationen | Permutationsvisualisierung |

### Physik

| Konzept | Demo |
|:--------|:-----|
| ⚙️ Viertaktmotor | Ansaugen→Verdichtung→Arbeit→Ausstoß |
| 💡 Lichtbrechung | Snelliussches Gesetz Demo |
| 🧲 Elektromagnetische Induktion | Faradaysches Gesetz |
| 🏃 Freier Fall | Beschleunigung durch Schwerkraft |
| 🌊 Harmonische Schwingung | Federoszillator |
| 🌊 Wellenausbreitung | Longitudinal- & Transversalwellen |
| 🔥 Wärmeübertragung | Wärmeleitung |
| 🌑 Gravitation | Planetenbewegung |
| 💥 Impulserhaltung | Stoßexperiment |

### Chemie

| Konzept | Demo |
|:--------|:-----|
| 💧 Wassermolekül | H₂O 3D-Modell |
| ⚗️ Chemische Reaktionen | Reaktionstypen |
| ⚛️ Atomstruktur | Kern & Elektronenhülle |

---

## 🛠️ Tech-Stack

| Bereich | Technologie |
|:---------|:------------|
| 🐍 **Sprache** | Python 3.9+ |
| 🌐 **Frontend** | HTML5 + Three.js r160 |
| ⚡ **Backend** | FastAPI + Uvicorn |
| 🤖 **KI** | OpenAI GPT / Anthropic Claude |

---

## 🤝 Beitragen

Beiträge willkommen! Bitte lesen Sie zuerst den [Beitragsleitfaden](docs/contributing.md).

---

## 📄 Lizenz

MIT-Lizenz - Siehe [LICENSE](LICENSE).

---

## 🙏 Danksagung

- [Three.js](https://threejs.org/) - 3D-Rendering-Engine
- [FastAPI](https://fastapi.tiangolo.com/) - Web-Framework
- [OpenClaw](https://github.com/openclaw/openclaw) - Inspiration für die Multi-Agent-Architektur
- [pi-mono](https://github.com/badlogic/pi-mono) - Agent-Ausführungsframework
- [pi-agent-core](https://github.com/pietai/pi-agent-core) - Agent-Ausführungsframework

---

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=powerball0x2a/vispawn&type=Date)](https://star-history.com/#powerball0x2a/vispawn)

<div align="center">

**Wenn dieses Projekt Ihnen geholfen hat, geben Sie ⭐ Star!**

</div>
