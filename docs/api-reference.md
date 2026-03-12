# API 参考

Vispawn 提供 RESTful API 接口。

## 基础信息

- 基础 URL: `http://localhost:8000`
- 数据格式: JSON

## 端点

### 1. 生成可视化

生成指定原理的 3D 可视化。

**端点**: `POST /generate`

**请求体**:

```json
{
  "theorem": "原理名称",
  "max_iterations": 3
}
```

**参数**:
- `theorem` (必填): 原理名称，如 "勾股定理"、"四冲程发动机"
- `max_iterations` (可选): 最大迭代次数，默认 3

**响应**:

```json
{
  "task_id": "abc123",
  "status": "pending"
}
```

### 2. 查询结果

查询可视化生成结果。

**端点**: `GET /result/{task_id}`

**路径参数**:
- `task_id`: 任务 ID

**响应**:

```json
{
  "task_id": "abc123",
  "status": "completed",
  "result": {
    "plan": {
      "topic": "勾股定理",
      "type": "geometric",
      "description": "直角三角形两直角边的平方和等于斜边的平方",
      "concept": "在直角三角形三边上构建正方形",
      "elements": ["直角三角形", "正方形", "面积方块"],
      "steps": ["展示直角三角形", "构建正方形", "填充方块", "验证面积相等"],
      "audience": "middle",
      "complexity": "simple"
    },
    "code": "<html>...</html>",
    "total_score": 85.5,
    "passed": true,
    "scores": {
      "security": {"score": 100, "feedback": "安全检测通过", "issues": []},
      "syntax": {"score": 90, "feedback": "语法检测通过", "issues": []},
      "accuracy": {"score": 85, "feedback": "准确性良好", "issues": []},
      "visual": {"score": 80, "feedback": "视觉效果良好", "issues": []},
      "pedagogy": {"score": 82, "feedback": "教学效果良好", "issues": []}
    },
    "iterations": 2
  }
}
```

### 3. 预览代码

在浏览器中预览生成的可视化。

**端点**: `GET /preview/{task_id}`

**路径参数**:
- `task_id`: 任务 ID

### 4. 列表模板

获取所有可用的预设模板。

**端点**: `GET /templates`

**响应**:

```json
{
  "templates": ["勾股定理", "四冲程发动机", "圆的面积", "牛顿第二定律"]
}
```

### 5. 健康检查

检查服务状态。

**端点**: `GET /health`

**响应**:

```json
{
  "status": "ok",
  "version": "0.1.0"
}
```

## 错误处理

错误响应格式：

```json
{
  "error": "错误信息",
  "detail": "详细说明"
}
```

常见错误码：

| 状态码 | 说明 |
|-------|------|
| 400 | 请求参数错误 |
| 404 | 任务不存在 |
| 500 | 服务端错误 |
| 503 | LLM API 不可用 |

## Python SDK 使用

```python
import asyncio
from vispawn import VispawnPipeline

async def main():
    pipeline = VispawnPipeline()
    result = await pipeline.generate("勾股定理")

    print(f"生成完成，得分: {result['total_score']}")
    print(result['code'])

asyncio.run(main())
```
