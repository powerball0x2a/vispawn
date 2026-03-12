# Vispawn 模板库

欢迎使用 Vispawn 模板库！这里收集了社区贡献的优质可视化模板，帮助你快速创建原理可视化内容。

## 什么是模板

模板是预定义的可视化方案，包含了原理展示所需的元素、步骤、配色等信息。使用模板可以：

- 快速生成高质量可视化
- 确保原理展示的准确性
- 获得一致的用户体验

## 模板列表

### 几何类 (Geometric)

| 模板名称 | 描述 | 复杂度 | 目标受众 |
|---------|------|--------|----------|
| [勾股定理](./how-to-create.md#示例创建勾股定理模板) | 直角三角形两直角边的平方和等于斜边的平方 | 简单 | 初中 |
| 圆的面积 | 圆的面积等于π乘以半径的平方 | 简单 | 初中 |

### 机械类 (Mechanical)

| 模板名称 | 描述 | 复杂度 | 目标受众 |
|---------|------|--------|----------|
| 四冲程发动机 | 内燃机通过进气、压缩、做功、排气四个冲程完成工作循环 | 中等 | 高中 |

### 物理类 (Physical)

| 模板名称 | 描述 | 复杂度 | 目标受众 |
|---------|------|--------|----------|
| 牛顿第二定律 | 物体加速度与作用力成正比，与质量成反比 | 中等 | 高中 |

## 如何使用模板

### 方式一：按名称使用

当你需要可视化某个原理时，如果该原理已有模板，系统会自动使用：

```python
from vispawn import TheoremAnalyzer, LLMClient

async def main():
    llm = LLMClient()
    analyzer = TheoremAnalyzer(llm)

    # 如果 "勾股定理" 已有模板，会自动使用
    result = await analyzer.analyze("勾股定理")
    print(result)
```

### 方式二：搜索模板

使用关键词搜索合适的模板：

```python
from vispawn.templates import search_templates

# 搜索包含 "几何" 标签的模板
results = search_templates("几何")
print(results)  # ['勾股定理', '圆的面积']
```

### 方式三：按分类浏览

按学科分类查看可用模板：

```python
from vispawn.templates import get_by_category

# 获取所有几何类模板
templates = get_by_category("几何")
print(templates)  # ['勾股定理', '圆的面积']
```

## 模板参数说明

每个模板包含以下关键信息：

| 参数 | 说明 |
|------|------|
| type | 模板类型：geometric（几何）、mechanical（机械）、physical（物理） |
| description | 原理的简短描述 |
| concept | 可视化思路，用一句话说明如何展示原理 |
| elements | 需要的 3D 元素列表 |
| steps | 演示步骤，按顺序展示原理的过程 |
| audience | 目标受众：middle（初中）、high（高中/大学） |
| complexity | 复杂度：simple（简单）、medium（中等）、complex（复杂） |
| colors | 配色方案：primary（主色）、secondary（辅色）、accent（强调色）、bg（背景） |
| tags | 搜索标签，用于找到相关模板 |

## 模板分类

### 按类型

- **几何类 (geometric)**：适合展示形状、面积、体积等几何概念
- **机械类 (mechanical)**：适合展示机械原理、运动过程
- **物理类 (physical)**：适合展示物理定律、现象

### 按难度

- **简单 (simple)**：3-4 个步骤，适合入门学习
- **中等 (medium)**：5-6 个步骤，包含一定交互
- **复杂 (complex)**：7+ 步骤，多元素联动

### 按学段

- **初中 (middle)**：适合初中生理解的基础原理
- **高中及以上 (high)**：需要较强学科知识的高级原理

## 贡献模板

欢迎社区成员贡献模板！请阅读 [贡献指南](../contributing.md) 了解如何贡献。

快速入门请查看 [模板创建指南](./how-to-create.md)。

## 更新日志

### 2024-01

- 初始模板库上线
- 包含 4 个预设模板：
  - 勾股定理（几何）
  - 圆的面积（几何）
  - 四冲程发动机（机械）
  - 牛顿第二定律（物理）

---

## 下一步

- [创建你的第一个模板](./how-to-create.md)
- [了解模板贡献流程](../contributing.md#模板贡献指南)
- [查看 API 参考](../api-reference.md)
