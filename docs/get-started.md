# 快速开始

本指南将帮助你快速上手 Vispawn。

## 环境要求

- Python 3.9+
- API 密钥 (OpenAI / Anthropic)

## 安装

```bash
# 克隆项目
git clone https://github.com/yourusername/vispawn.git
cd vispawn

# 创建虚拟环境 (推荐)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

## 配置

1. 复制环境变量模板：

```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，添加你的 API 密钥：

```env
# 方案 1: 使用 OpenAI 兼容 API (推荐 Kimi)
OPENAI_API_KEY=your-api-key
OPENAI_MODEL=kimi-k2.5
OPENAI_BASE_URL=https://api.moonshot.cn/v1

# 方案 2: 使用 Anthropic Claude
# ANTHROPIC_API_KEY=your-api-key
# ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

## 启动服务

```bash
python main.py
```

服务启动后：
- 🌐 Web 界面: http://localhost:8000
- 📚 API 文档: http://localhost:8000/docs

## 使用方法

### 通过 Web 界面

1. 打开浏览器访问 http://localhost:8000
2. 在输入框中输入原理名称（如"勾股定理"）
3. 点击生成按钮
4. 等待生成完成后预览效果

### 通过 API

```bash
# 生成可视化
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"theorem": "四冲程发动机"}'

# 查询结果
curl http://localhost:8000/result/{task_id}
```

## 故障排除

### API 密钥错误

确保 `.env` 文件中的 API 密钥正确，且有足够的额度。

### 生成失败

检查控制台输出的错误信息，常见问题：
- 网络连接问题
- API 响应超时
- 请求内容不符合要求

### 查看日志

```bash
# 详细日志模式
python -u main.py
```

## 下一步

- [API 参考](api-reference.md)
- [贡献指南](contributing.md)
- [模板制作](templates/how-to-create.md)
