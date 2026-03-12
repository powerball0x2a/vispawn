"""
简化的 LLM 客户端 - 支持真实 API 和模拟模式
"""
import json
import os
from dataclasses import dataclass
from typing import Optional

import httpx

# 自动加载 .env 文件
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


@dataclass
class LLMResponse:
    content: str
    model: str


class LLMClient:
    """统一的 LLM 客户端"""

    def __init__(self):
        self.provider = None
        self.api_key = None
        self.model = None
        self.base_url = None
        self.mock_mode = False

        # 检查是否有 API 密钥
        if os.getenv("OPENAI_API_KEY"):
            self.provider = "openai"
            self.api_key = os.getenv("OPENAI_API_KEY")
            self.model = os.getenv("OPENAI_MODEL", "gpt-4o")
            self.base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        elif os.getenv("ANTHROPIC_API_KEY"):
            self.provider = "anthropic"
            self.api_key = os.getenv("ANTHROPIC_API_KEY")
            self.model = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")
        else:
            # 模拟模式 - 用于测试
            self.mock_mode = True
            self.model = "mock"
            print("⚠️  未配置 API 密钥，使用模拟模式")

    async def generate(self, prompt: str, temperature: float = 0.5, max_tokens: int = 4000) -> LLMResponse:
        """生成文本"""
        if self.mock_mode:
            return self._mock_generate(prompt)

        if self.provider == "openai":
            return await self._call_openai(prompt, temperature, max_tokens)
        else:
            return await self._call_anthropic(prompt, temperature, max_tokens)

    def _mock_generate(self, prompt: str) -> LLMResponse:
        """模拟生成 - 用于测试"""
        # 根据 prompt 内容返回模拟响应
        if "分析" in prompt and "定理" in prompt:
            # 分析定理 - 返回 JSON
            return LLMResponse(
                content='''{
  "type": "geometric",
  "description": "这是一个几何定理的可视化展示",
  "concept": "使用3D图形展示定理的几何关系",
  "elements": ["三角形", "正方形", "圆形"],
  "steps": ["展示初始图形", "演示变换过程", "得出结论"],
  "audience": "middle",
  "complexity": "medium"
}''',
                model="mock"
            )
        elif "视觉效果" in prompt:
            return LLMResponse(
                content='{"score": 85, "feedback": "视觉效果良好"}',
                model="mock"
            )
        elif "教学效果" in prompt:
            return LLMResponse(
                content='{"score": 80, "feedback": "教学效果良好"}',
                model="mock"
            )
        else:
            # 返回一个简单的 Three.js 示例
            return LLMResponse(
                content='''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Three.js Visualization</title>
    <style>body { margin: 0; overflow: hidden; }</style>
</head>
<body>
    <script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
    <script>
        // Scene setup
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x1a1a2e);

        const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
        camera.position.set(0, 0, 5);

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Lighting
        const light = new THREE.DirectionalLight(0xffffff, 0.8);
        light.position.set(5, 10, 7);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0xffffff, 0.4));

        // Objects
        const geometry = new THREE.BoxGeometry(1, 1, 1);
        const material = new THREE.MeshPhongMaterial({ color: 0x4a90e2 });
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        // Animation
        function animate() {
            requestAnimationFrame(animate);
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;
            renderer.render(scene, camera);
        }
        animate();

        // Resize handler
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth/window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    </script>
</body>
</html>''',
                model="mock"
            )

    async def _call_openai(self, prompt: str, temperature: float, max_tokens: int) -> LLMResponse:
        """调用 OpenAI API"""
        # kimi-k2.5 模型只支持 temperature=1
        if "kimi" in self.model.lower():
            temperature = 1.0

        # kimi-k2.5 需要更长的超时
        timeout = 300.0 if "kimi" in self.model.lower() else 120.0

        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                }
            )
            response.raise_for_status()
            data = response.json()
            message = data["choices"][0]["message"]
            # Kimi 推理模型可能将内容放在 reasoning_content 中
            content = message.get("content") or message.get("reasoning_content", "")
            return LLMResponse(
                content=content,
                model=self.model
            )

    async def _call_anthropic(self, prompt: str, temperature: float, max_tokens: int) -> LLMResponse:
        """调用 Anthropic API"""
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": self.api_key,
                    "anthropic-version": "2023-06-01",
                },
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                }
            )
            response.raise_for_status()
            data = response.json()
            content = "".join(block["text"] for block in data["content"] if block["type"] == "text")
            return LLMResponse(content=content, model=self.model)
