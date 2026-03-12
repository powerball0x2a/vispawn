"""
Vispawn - API Server
支持传统模式和 Agent 自主规划模式
"""
import os
import uuid
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Dict, Optional

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from vispawn import VispawnPipeline, get_agent, process_visualization_request

# 全局状态
pipeline: Optional[VispawnPipeline] = None
tasks: Dict[str, dict] = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """生命周期"""
    global pipeline
    pipeline = VispawnPipeline()
    print("✅ Vispawn 服务已启动")
    yield
    print("👋 服务关闭")


app = FastAPI(
    title="Vispawn",
    description="输入定理名称，自动生成3D可视化",
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 数据模型
class GenerateRequest(BaseModel):
    theorem: str


class GenerateResponse(BaseModel):
    task_id: str
    status: str


# 后台生成任务
async def generate_task(task_id: str, theorem: str):
    """后台生成"""
    try:
        tasks[task_id]["status"] = "processing"
        tasks[task_id]["progress"] = 30

        result = await pipeline.generate(theorem)

        tasks[task_id].update({
            "status": "completed" if result["passed"] else "completed_with_issues",
            "progress": 100,
            "completed_at": datetime.utcnow().isoformat(),
            "theorem": theorem,
            "plan": result["plan"],
            "code": result["code"],
            "total_score": result["total_score"],
            "passed": result["passed"],
            "scores": result["scores"],
            "generation_log": result.get("generation_log", []),
            "iterations": result.get("iterations", 1),
        })
    except Exception as e:
        tasks[task_id].update({
            "status": "failed",
            "error": str(e),
        })


# API 路由
@app.get("/")
async def root():
    """健康检查"""
    return {"status": "running", "version": "2.0.0"}


@app.post("/generate", response_model=GenerateResponse)
async def create_generation(request: GenerateRequest, background_tasks: BackgroundTasks):
    """创建生成任务"""
    task_id = str(uuid.uuid4())

    tasks[task_id] = {
        "task_id": task_id,
        "status": "pending",
        "progress": 0,
        "theorem": request.theorem,
        "created_at": datetime.utcnow().isoformat(),
    }

    background_tasks.add_task(generate_task, task_id, request.theorem)

    return {"task_id": task_id, "status": "pending"}


@app.get("/result/{task_id}")
async def get_result(task_id: str):
    """获取结果"""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.get("/preview/{task_id}", response_class=HTMLResponse)
async def preview(task_id: str):
    """预览代码"""
    if task_id not in tasks or not tasks[task_id].get("code"):
        raise HTTPException(status_code=404, detail="Code not found")
    return HTMLResponse(content=tasks[task_id]["code"])


@app.get("/tasks")
async def list_tasks():
    """列出所有任务"""
    return [
        {"task_id": k, "status": v["status"], "theorem": v.get("theorem", "")}
        for k, v in tasks.items()
    ]


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    """删除任务"""
    if task_id in tasks:
        del tasks[task_id]
    return {"message": "deleted"}


@app.get("/app", response_class=HTMLResponse)
async def get_app():
    """前端页面"""
    import os
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>index.html not found</h1>", status_code=404)


# ============================================================
# Agent 自主规划模式 API
# ============================================================

@app.post("/agent/generate")
async def agent_generate(request: GenerateRequest):
    """
    Agent 自主规划模式 - 接收任务后自主创建 Agent 完成生成

    参考 OpenClaw 的自主规划机制：
    1. 主 Agent 接收任务
    2. 自主分析任务复杂度
    3. 分解为子任务（分析、生成、评估、验证）
    4. 调度子 Agent 并行/串行执行
    5. 整合结果并验证渲染效果
    """
    task_id = str(uuid.uuid4())

    # 使用 Agent 系统处理
    try:
        result = await process_visualization_request(request.theorem)

        return {
            "task_id": task_id,
            "status": "completed",
            "result": result
        }
    except Exception as e:
        return {
            "task_id": task_id,
            "status": "failed",
            "error": str(e)
        }


@app.get("/agent/status/{task_id}")
async def agent_status(task_id: str):
    """获取 Agent 任务状态"""
    # Agent 模式的任务存储在全局任务中
    if task_id in tasks:
        return tasks[task_id]
    return {"status": "not_found"}


@app.get("/agent/agents")
async def list_agents():
    """列出所有可用的子 Agent"""
    agent = get_agent()
    return {
        "available_agents": agent.registry.list_agents(),
        "running_agents": list(agent._running_agents.keys())
    }
