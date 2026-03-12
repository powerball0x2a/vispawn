# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **AI Agent System**: 自主规划 Agent 系统，参考 OpenClaw 架构
  - 子 Agent 机制：analyzer, generator, evaluator, validator
  - 动态创建专业化 Agent：geometric, mechanical, physical, animation, interactive
  - 并行/串行智能执行决策
  - 事件驱动架构
- **Agent API**: `/agent/generate` 端点支持自主规划模式

### Changed
- 扩展预设模板库从 4 个到 25+ 个
- 简化项目结构，移除实验性代码
- 优化代码生成质量评估体系

---

## [0.1.0] - 2024-03-12

### Added
- 初始版本发布
- 核心功能：
  - 自然语言输入 → Three.js 3D 可视化
  - 多维度质量评估（安全、语法、准确性、视觉、教学）
  - 迭代优化机制
  - 预设模板系统
- API 端点：
  - `/generate` - 生成可视化
  - `/result/{task_id}` - 查询结果
  - `/preview/{task_id}` - 预览代码
  - `/app` - Web 界面
- 预设模板：
  - 勾股定理
  - 四冲程发动机
  - 圆的面积
  - 牛顿第二定律

[Unreleased]: https://github.com/yourusername/vizgen/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/yourusername/vizgen/releases/tag/v0.1.0
