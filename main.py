#!/usr/bin/env python3
"""
Vispawn 启动脚本
"""
import os
import sys

# 加载 .env
env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key, value)

# 检查 API 密钥
if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
    print("⚠️  警告: 未设置 API 密钥，将使用模拟模式")
    print(f"   如需真实 LLM 调用，请编辑 {env_path} 添加 API 密钥")
    print()

# 启动服务
import uvicorn

port = int(os.getenv("PORT", "8000"))

print(f"🚀 启动 Vispawn 服务...")
print(f"📖 文档: http://localhost:{port}/docs")
print(f"🎨 前端: http://localhost:{port}/app")
print()

uvicorn.run("api:app", host="0.0.0.0", port=port, reload=True)
