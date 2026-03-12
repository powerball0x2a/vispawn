"""
Vispawn - 智能可视化生成器
用 AI 把任何概念变成可交互的 3D 可视化
"""
from .core import TheoremAnalyzer, CodeGenerator, CodeEvaluator, VizGenPipeline
from .core import VisualizationPlan, EvaluationResult
from .llm import LLMClient
from .agent import VispawnAgent, process_visualization_request, get_agent
from .agent import AgentStatus, TaskStatus, Task, SubAgent
from . import templates

__version__ = "0.1.0"
__author__ = "Vispawn Team"
__license__ = "MIT"

__all__ = [
    "TheoremAnalyzer",
    "CodeGenerator",
    "CodeEvaluator",
    "VizGenPipeline",
    "VisualizationPlan",
    "EvaluationResult",
    "LLMClient",
    "templates",
    # Agent 系统
    "VispawnAgent",
    "process_visualization_request",
    "get_agent",
    "AgentStatus",
    "TaskStatus",
    "Task",
    "SubAgent",
]
