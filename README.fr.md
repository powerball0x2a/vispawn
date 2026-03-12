# Vispawn ⚡️

<div align="center">

[![PyPI Version](https://img.shields.io/pypi/v/vispawn?logo=pypi)](https://pypi.org/project/vispawn/)
[![Python Version](https://img.shields.io/python/py-version/vispawn?logo=python)](https://www.python.org)
[![Three.js](https://img.shields.io/badge/Three.js-r160-orange?logo=three.js)](https://threejs.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/powerball0x2a/vispawn?style=social)](https://github.com/powerball0x2a/vispawn/stargazers)

<br/>

> **Transformez n'importe quel concept en visualisations 3D interactives avec l'IA**
>
> Dites adieu aux graphiques statiques ennuyeux et donnez vie à vos cours ✨

[English](README.md) · [简体中文](README.zh-CN.md) · [繁体中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Démarrage rapide](#-démarrage-rapide) · [API Docs](docs/api-reference.md) · [Contributing](docs/contributing.md)

</div>

---

## ⭐ Pourquoi Vispawn ?

| Traditionnel | Vispawn |
|:-------------|:--------|
| Écrire des centaines de lignes de code Three.js | 📝 Entrez simplement une phrase |
| Des heures voire des jours | ⚡ Généré en quelques secondes |
| Expérience en graphisme 3D requise | 🎯 Pas de connaissances préalables |
| Démonstrations statiques | 🎮 Interactif et contrôlable |

**Entrée**: `"Théorème de Pythagore"` → **Sortie**: Démonstration 3D interactive complète

---

## ✨ Fonctionnalités

<div align="center">

| 🤖 Alimenté par l'IA | 🔄 Planification autonome | 🎯 Évaluation multidimensionnelle |
|:---------------------|:--------------------------|:-----------------------------------|
| Entrée en langage naturel, génération automatique de code Three.js 3D | Système Agent style OpenClaw avec décomposition autonome des tâches | Vérifications de sécurité, syntaxe, précision, qualité visuelle, effets pédagogiques |

| 📦 25+ Modèles | ⚡ Exécution parallèle | 🌐 Natif Web |
|:----------------|:----------------------|:-------------|
| Couvre les concepts clés en mathématiques, physique, chimie | Analyse intelligente des dépendances, parallélisation maximale | Frontend pur, aucun plugin nécessaire |

</div>

---

## 🚀 Démarrage rapide

### Installation

```bash
# pip (recommandé)
pip install vispawn

# ou depuis les sources
git clone https://github.com/powerball0x2a/vispawn.git
cd vispawn
pip install -e .
```

### Configuration de la clé API

```bash
# Créer le fichier .env
cp .env.example .env

# Éditer .env, ajouter la clé API
OPENAI_API_KEY=sk-xxxx    # OpenAI
# ou
ANTHROPIC_API_KEY=sk-ant-xxxx  # Anthropic Claude
```

### Lancer le service

```bash
# Lancer le service
vispawn

# ou
python main.py
```

Ouvrir dans le navigateur: **http://localhost:8000** 🎉

---

## 📖 Exemples d'utilisation

### Option 1: Interface Web

Ouvrez http://localhost:8000/app, entrez:

```
Moteur quatre temps
```

Le système:
1. 🤖 Analyse la complexité de la tâche
2. 📋 Planifie les étapes d'exécution de manière autonome
3. ⚡ Planifie intelligemment les sous-agents
4. ✅ Génère et valide le rendu

### Option 2: API

```bash
# Mode Agent (recommandé) - planification autonome
curl -X POST http://localhost:8000/agent/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "Théorème de Pythagore"}'
```

---

## 🏗️ Architecture

```
User Input: "Théorème de Pythagore"
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

## 📦 Modèles (25+)

### Mathématiques

| Concept | Démo |
|:--------|:-----|
| 🔺 Théorème de Pythagore | Preuve par l'aire a² + b² = c² |
| 📐 Trigonométrie | Animation graphe sin/cos |
| 📈 Fonction exponentielle | Croissance exponentielle |
| 📉 Fonction logarithme | Courbe logarithmique |
| ⬜ Aire du polygone régulier | Formule de l'aire du polygone |
| 🔵 Volume du cône | V = 1/3πr²h |
| ⚪ Volume de la sphère | V = 4/3πr³ |
| 🔺 Triangles similaires | Critères de similarité |
| 🎲 Dés probabilistes | Expérience de probabilité |
| 🔢 Permutations | Visualisation des permutations |

### Physique

| Concept | Démo |
|:--------|:-----|
| ⚙️ Moteur 4 temps | Admission→Compression→Combustion→Échappement |
| 💡 Réfraction de la lumière | Démonstration loi de Snell |
| 🧲 Induction électromagnétique | Loi de Faraday |
| 🏃 Chute libre | Accélération gravitationnelle |
| 🌊 Mouvement harmonique simple | Oscillateur à ressort |
| 🌊 Propagation des ondes | Ondes longitudinales et transversales |
| 🔥 Transfert thermique | Conduction thermique |
| 🌑 Gravitation universelle | Mouvement planétaire |
| 💥 Conservation de l'impulsion | Expérience de collision |

### Chimie

| Concept | Démo |
|:--------|:-----|
| 💧 Molécule d'eau | Modèle 3D H₂O |
| ⚗️ Réactions chimiques | Types de réactions |
| ⚛️ Structure atomique | Noyau et nuage électronique |

---

## 🛠️ Stack technique

| Domaine | Technologie |
|:--------|:------------|
| 🐍 **Langage** | Python 3.9+ |
| 🌐 **Frontend** | HTML5 + Three.js r160 |
| ⚡ **Backend** | FastAPI + Uvicorn |
| 🤖 **IA** | OpenAI GPT / Anthropic Claude |

---

## 🤝 Contribution

Les contributions sont les bienvenues! Veuillez d'abord lire le [guide de contribution](docs/contributing.md).

---

## 📄 Licence

Licence MIT - Voir [LICENSE](LICENSE).

---

## 🙏 Remerciements

- [Three.js](https://threejs.org/) - Moteur de rendu 3D
- [FastAPI](https://fastapi.tiangolo.com/) - Framework Web
- [OpenClaw](https://github.com/openclaw/openclaw) - Inspiration pour l'architecture multi-agents
- [pi-mono](https://github.com/badlogic/pi-mono) - Framework d'exécution Agent
- [pi-agent-core](https://github.com/pietai/pi-agent-core) - Framework d'exécution Agent

---

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=powerball0x2a/vispawn&type=Date)](https://star-history.com/#powerball0x2a/vispawn)

<div align="center">

**Si ce projet vous a aidé, donnez ⭐ Star!**

</div>
