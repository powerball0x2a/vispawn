# Vispawn ⚡️

<div align="center">

[![PyPI Version](https://img.shields.io/pypi/v/vispawn?logo=pypi)](https://pypi.org/project/vispawn/)
[![Python Version](https://img.shields.io/python/py-version/vispawn?logo=python)](https://www.python.org)
[![Three.js](https://img.shields.io/badge/Three.js-r160-orange?logo=three.js)](https://threejs.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/powerball0x2a/vispawn?style=social)](https://github.com/powerball0x2a/vispawn/stargazers)

<br/>

> **AIでどんなコンセプトもインタラクティブな3D可視化に**
>
> つまらない静的チャートに別れを告げ、教学演示を生き生きとさせましょう ✨

[English](README.md) · [简体中文](README.zh-CN.md) · [繁体中文](README.zh-TW.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [クイックスタート](#-クイックスタート) · [API Docs](docs/api-reference.md) · [Contributing](docs/contributing.md)

</div>

---

## ⭐ なぜ Vispawn ？

| 従来の方法 | Vispawn |
|:------------|:--------|
| 何百行ものThree.jsコードを書く | 📝 只需一句话 |
| 数時間から数日間 | ⚡ 数秒で生成 |
| 3Dグラフィックの経験が必要 | 🎯 基礎知識不要 |
| 静的デモ | 🎮 インタラクティブ操作可能 |

**入力**：`"三角定理"` → **出力**：完全な3Dインタラクティブデモ

---

## ✨ 機能

<div align="center">

| 🤖 AI駆動 | 🔄 自主計画 | 🎯 多面評価 |
|:----------|:------------|:------------|
| 自然言語入力、Three.js 3Dコードを自動生成 | OpenClawのようなAgentシステム、任務を自主的に分解 | セキュリティ、構文、准确性、視覚効果、教育効果 |

| 📦 25+ テンプレート | ⚡ 並列実行 | 🌐 Webネイティブ |
|:----------------------|:------------|:---------------|
| 数学、物理、化学の主要概念をカバー | 依存関係をスマート分析、最大並列効率 | ピュアフロントエンド、プラグイン不要 |

</div>

---

## 🚀 クイックスタート

### インストール

```bash
# pip インストール（推奨）
pip install vispawn

# またはソースから
git clone https://github.com/powerball0x2a/vispawn.git
cd vispawn
pip install -e .
```

### APIキーの設定

```bash
# 環境変数ファイルを作成
cp .env.example .env

# .envを編集APIキーを追加
OPENAI_API_KEY=sk-xxxx    # OpenAI
# または
ANTHROPIC_API_KEY=sk-ant-xxxx  # Anthropic Claude
```

### サービスの起動

```bash
# サービス起動
vispawn

# または
python main.py
```

ブラウザで開く：**http://localhost:8000** 🎉

---

## 📖 使用例

### 方法1：Webインターフェース

http://localhost:8000/app を開き、入力：

```
四ストロークエンジン
```

システムは自動的に：
1. 🤖 任務の複雑度を分析
2. 📋 実行ステップを自主的に計画
3. ⚡ サブAgentをスマートにスケジューリング
4. ✅ 生成しレンダリングを検証

### 方法2：API

```bash
# Agentモード（推奨）- 自主計画
curl -X POST http://localhost:8000/agent/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "三角定理"}'
```

---

## 🏗️ アーキテクチャ

```
User Input: "三角定理"
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

## 📦 テンプレート (25+)

### 数学

| コンセプト | デモ |
|:--------|:-----|
| 🔺 三角定理 | a² + b² = c² 面積証明 |
| 📐 三角関数 | sin/cos グラフアニメーション |
| 📈 指数関数 | 指数関数的成長 |
| 📉 対数関数 | 対数曲線 |
| ⬜ 正多角形の面積 | 多角形面積公式 |
| 🔵 円錐の体積 | V = 1/3πr²h |
| ⚪ 球の体積 | V = 4/3πr³ |
| 🔺 相似三角形 | 相似条件 |
| 🎲 確率サイコロ | 確率実験 |
| 🔢 順列 | 順列の可視化 |

### 物理

| コンセプト | デモ |
|:--------|:-----|
| ⚙️ 4サイクルエンジン | 吸気→圧縮→燃焼→排気 |
| 💡 光の屈折 | スネルの法則デモ |
| 🧲 電磁誘導 | ファラデーの法則 |
| 🏃 自由落下 | 重力加速度 |
| 🌊 単振動 | ばね振動子 |
| 🌊 波の伝搬 | 縦波と横波 |
| 🔥 熱伝達 | 熱伝導 |
| 🌑 万有引力 | 惑星運動 |
| 💥 運動量保存 | 衝突実験 |

### 化学

| コンセプト | デモ |
|:--------|:-----|
| 💧 水分子 | H₂O 3Dモデル |
| ⚗️ 化学反応 | 反応タイプ |
| ⚛️ 原子構造 | 原子核と電子雲 |

---

## 🛠️ 技術スタック

| 分野 | 技術 |
|:-----|:-----|
| 🐍 **言語** | Python 3.9+ |
| 🌐 **フロントエンド** | HTML5 + Three.js r160 |
| ⚡ **バックエンド** | FastAPI + Uvicorn |
| 🤖 **AI** | OpenAI GPT / Anthropic Claude |

---

## 🤝 コントリビューション

コントリビューション大歓迎！[コントリビューションガイド](docs/contributing.md)をお読みください。

---

## 📄 ライセンス

MITライセンス - [LICENSE](LICENSE)をご覧ください。

---

## 🙏 謝辞

- [Three.js](https://threejs.org/) - 3Dレンダリングエンジン
- [FastAPI](https://fastapi.tiangolo.com/) - Webフレームワーク
- [OpenClaw](https://github.com/openclaw/openclaw) - マルチエージェントアーキテクチャのインスピレーション
- [pi-mono](https://github.com/badlogic/pi-mono) - エージェント実行フレームワーク
- [pi-agent-core](https://github.com/pietai/pi-agent-core) - エージェント実行フレームワーク

---

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=powerball0x2a/vispawn&type=Date)](https://star-history.com/#powerball0x2a/vispawn)

<div align="center">

**このプロジェクトが役に立ったら、⭐ Star해주세요！**

</div>
