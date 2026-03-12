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

[English](README.md) · [简体中文](README.zh-CN.md) · [繁体中文](README.zh-TW.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [クイックスタート](#-クイックスタート)

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

<div align="center">

**このプロジェクトが役に立ったら、⭐ Star해주세요！**

</div>
