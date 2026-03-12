# Vispawn ⚡️

<div align="center">

[![PyPI Version](https://img.shields.io/pypi/v/vispawn?logo=pypi)](https://pypi.org/project/vispawn/)
[![Python Version](https://img.shields.io/python/py-version/vispawn?logo=python)](https://www.python.org)
[![Three.js](https://img.shields.io/badge/Three.js-r160-orange?logo=three.js)](https://threejs.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/vispawn?style=social)](https://github.com/yourusername/vispawn/stargazers)

<br/>

> **Превратите любую концепцию в интерактивную 3D-визуализацию с помощью ИИ**
>
> Попрощайтесь со скучными статическими диаграммами, вдохните жизнь в свои уроки ✨

[English](README.md) · [简体中文](README.zh-CN.md) · [繁体中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Быстрый старт](#-быстрый-старт)

</div>

---

## ⭐ Почему Vispawn?

| Традиционный подход | Vispawn |
|:--------------------|:--------|
| Написание сотен строк кода Three.js | 📝 Просто введите предложение |
| Часы или даже дни | ⚡ Генерация за секунды |
| Требуется опыт работы с 3D-графикой | 🎯 Не требуется |
| Статические демонстрации | 🎮 Интерактивное управление |

**Ввод**: `"Теорема Пифагора"` → **Вывод**: Полная 3D-интерактивная демонстрация

---

## ✨ Функции

<div align="center">

| 🤖 На базе ИИ | 🔄 Автономное планирование | 🎯 Многомерная оценка |
|:--------------|:----------------------------|:----------------------|
| Ввод на естественном языке, автоматическая генерация кода Three.js 3D | Система Agent, подобная OpenClaw, с автономным разложением задач | Проверка безопасности, синтаксиса, точности, визуального качества, педагогического эффекта |

| 📦 25+ шаблонов | ⚡ Параллельное выполнение | 🌐 Web-ориентированность |
|:-----------------|:---------------------------|:------------------------|
| Покрытие основных понятий математики, физики, химии | Умный анализ зависимостей, максимальная параллелизация | Чистый фронтенд, плагины не нужны |

</div>

---

## 🚀 Быстрый старт

### Установка

```bash
# pip (рекомендуется)
pip install vispawn

# или из исходников
git clone https://github.com/yourusername/vispawn.git
cd vispawn
pip install -e .
```

### Настройка API-ключа

```bash
# Создать файл .env
cp .env.example .env

# Отредактировать .env, добавить API-ключ
OPENAI_API_KEY=sk-xxxx    # OpenAI
# или
ANTHROPIC_API_KEY=sk-ant-xxxx  # Anthropic Claude
```

### Запуск сервиса

```bash
# Запуск
vispawn

# или
python main.py
```

Откройте в браузере: **http://localhost:8000** 🎉

---

## 📖 Примеры использования

### Способ 1: Web-интерфейс

Откройте http://localhost:8000/app, введите:

```
Четырёхтактный двигатель
```

Система автоматически:
1. 🤖 Анализирует сложность задачи
2. 📋 Автономно планирует шаги выполнения
3. ⚡ Умно планирует под-агентов
4. ✅ Генерирует и проверяет рендеринг

### Способ 2: API

```bash
# Режим Agent (рекомендуется) - автономное планирование
curl -X POST http://localhost:8000/agent/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "Теорема Пифагора"}'
```

---

## 🛠️ Технологический стек

| Область | Технология |
|:---------|:-----------|
| 🐍 **Язык** | Python 3.9+ |
| 🌐 **Фронтенд** | HTML5 + Three.js r160 |
| ⚡ **Бэкенд** | FastAPI + Uvicorn |
| 🤖 **ИИ** | OpenAI GPT / Anthropic Claude |

---

## 🤝 Вклад в проект

Вклад приветствуется! Прочитайте [руководство по внесению вклада](docs/contributing.md).

---

## 📄 Лицензия

MIT License - см. [LICENSE](LICENSE).

---

## 🙏 Благодарности

- [Three.js](https://threejs.org/) - Движок 3D-рендеринга
- [FastAPI](https://fastapi.tiangolo.com/) - Веб-фреймворк
- [OpenClaw](https://github.com/openclaw/openclaw) - Вдохновение для архитектуры мультиагентов
- [pi-mono](https://github.com/badlogic/pi-mono) - Фреймворк выполнения агентов
- [pi-agent-core](https://github.com/pietai/pi-agent-core) - Фреймворк выполнения агентов

---

<div align="center">

**Если этот проект вам помог, поставьте ⭐ Star!**

</div>
