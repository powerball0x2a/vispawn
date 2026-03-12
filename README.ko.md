# Vispawn ⚡️

<div align="center">

[![PyPI Version](https://img.shields.io/pypi/v/vispawn?logo=pypi)](https://pypi.org/project/vispawn/)
[![Python Version](https://img.shields.io/python/py-version/vispawn?logo=python)](https://www.python.org)
[![Three.js](https://img.shields.io/badge/Three.js-r160-orange?logo=three.js)](https://threejs.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/powerball0x2a/vispawn?style=social)](https://github.com/powerball0x2a/vispawn/stargazers)

<br/>

> **AI로 모든 개념을 대화형 3D 시각화로 변환**
>
> 지루한 정적 차트에 작별하고 교육演示을 살아나게 하세요 ✨

[English](README.md) · [简体中文](README.zh-CN.md) · [繁体中文](README.zh-TW.md) · [日本語](README.ja.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [빠른 시작](#-빠른-시작)

</div>

---

## ⭐ 왜 Vispawn인가?

| 전통 방식 | Vispawn |
|:----------|:---------|
| 수백 줄의 Three.js 코드 작성 | 📝 한 문장만 입력 |
| 몇 시간에서 몇 일 | ⚡ 몇 초 만에 생성 |
| 3D 그래픽 경험 필요 | 🎯 기초 지식 불필요 |
| 정적 데모 | 🎮 대화형 조작 가능 |

**입력**: `"피타고라스 정리"` → **출력**: 완전한 3D 대화형 데모

---

## ✨ 기능

<div align="center">

| 🤖 AI 구동 | 🔄 자율 계획 | 🎯 다차원 평가 |
|:------------|:-------------|:---------------|
| 자연어 입력, Three.js 3D 코드 자동 생성 | OpenClaw 같은 Agent 시스템으로 작업 자율 분해 | 보안, 구문, 정확성, 시각 효과, 교육 효과 검사 |

| 📦 25+ 템플릿 | ⚡ 병렬 실행 | 🌐 Web 네이티브 |
|:--------------|:-------------|:----------------|
| 수학, 물리, 화학 핵심 개념 지원 | 종속성 스마트 분석, 최대 병렬 효율 | 플러그인 불필요 |

</div>

---

## 🚀 빠른 시작

### 설치

```bash
# pip 설치 (권장)
pip install vispawn

# 또는 소스에서
git clone https://github.com/powerball0x2a/vispawn.git
cd vispawn
pip install -e .
```

### API 키 설정

```bash
# 환경 변수 파일 생성
cp .env.example .env

# .env 편집, API 키 추가
OPENAI_API_KEY=sk-xxxx    # OpenAI
# 또는
ANTHROPIC_API_KEY=sk-ant-xxxx  # Anthropic Claude
```

### 서비스 시작

```bash
# 서비스 시작
vispawn

# 또는
python main.py
```

브라우저 열기: **http://localhost:8000** 🎉

---

## 📖 사용 예

### 방법1: Web 인터페이스

http://localhost:8000/app 를 열고 입력:

```
4행정 엔진
```

시스템이 자동으로:
1. 🤖 작업 복잡도 분석
2. 📋 실행 단계 자율 계획
3. ⚡ 하위 Agent 스마트 스케줄링
4. ✅ 생성 및 렌더링 검증

### 방법2: API

```bash
# Agent 모드 (권장) - 자율 계획
curl -X POST http://localhost:8000/agent/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "피타고라스 정리"}'
```

---

## 🛠️ 기술 스택

| 분야 | 기술 |
|:-----|:-----|
| 🐍 **언어** | Python 3.9+ |
| 🌐 **프론트엔드** | HTML5 + Three.js r160 |
| ⚡ **백엔드** | FastAPI + Uvicorn |
| 🤖 **AI** | OpenAI GPT / Anthropic Claude |

---

## 🤝 기여

기여 환영! [기여 가이드](docs/contributing.md)를 읽어주세요.

---

## 📄 라이선스

MIT 라이선스 - [LICENSE](LICENSE)를 참조하세요.

---

## 🙏 감사

- [Three.js](https://threejs.org/) - 3D 렌더링 엔진
- [FastAPI](https://fastapi.tiangolo.com/) - 웹 프레임워크
- [OpenClaw](https://github.com/openclaw/openclaw) - 멀티 에이전트 아키텍처 영감
- [pi-mono](https://github.com/badlogic/pi-mono) - 에이전트 실행 프레임워크
- [pi-agent-core](https://github.com/pietai/pi-agent-core) - 에이전트 실행 프레임워크

---

<div align="center">

**이 프로젝트가 도움이 되셨다면 ⭐ Star 해주세요!**

</div>
