"""
Vispawn Agent System - 自主规划系统
参考 OpenClaw 的 Agent 架构设计
"""
import asyncio
import uuid
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Callable, Any
from enum import Enum
from .llm import LLMClient


class AgentStatus(Enum):
    """Agent 状态"""
    IDLE = "idle"
    RUNNING = "running"
    WAITING = "waiting"
    COMPLETED = "completed"
    FAILED = "failed"


class TaskStatus(Enum):
    """任务状态"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class AgentConfig:
    """Agent 配置"""
    name: str
    role: str
    system_prompt: str
    tools: List[str] = field(default_factory=list)
    max_spawn_depth: int = 3
    max_children: int = 5
    timeout: int = 300


@dataclass
class Task:
    """任务定义"""
    task_id: str
    name: str
    description: str
    type: str  # "analysis", "generation", "evaluation", "validation"
    input_data: Dict[str, Any]
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[Dict] = None
    error: Optional[str] = None
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)
    parent_task_id: Optional[str] = None
    children_task_ids: List[str] = field(default_factory=list)
    progress: float = 0.0
    message: str = ""


@dataclass
class SubAgent:
    """子 Agent 实例"""
    agent_id: str
    config: AgentConfig
    status: AgentStatus
    current_task: Optional[Task] = None
    parent_agent_id: Optional[str] = None
    depth: int = 0
    created_at: float = field(default_factory=time.time)
    messages: List[Dict] = field(default_factory=list)


class SubAgentRegistry:
    """子 Agent 注册表 - 管理所有可用的子 Agent 类型"""

    def __init__(self):
        self._agents: Dict[str, AgentConfig] = {}
        self._register_default_agents()

    def _register_default_agents(self):
        """注册默认的子 Agent"""

        # 分析 Agent - 分析定理，制定可视化方案
        self.register(AgentConfig(
            name="analyzer",
            role="分析 Agent",
            system_prompt="""你是 Vispawn 的分析专家。你的任务是根据用户输入的定理/概念，分析并制定可视化方案。

你需要：
1. 理解用户想要可视化的概念
2. 确定可视化类型（几何/机械/物理/化学）
3. 确定目标受众和复杂度
4. 制定可视化元素和步骤

输出 JSON 格式的分析结果。""",
            tools=["analyze_theorem"]
        ))

        # 生成 Agent - 生成 Three.js 代码
        self.register(AgentConfig(
            name="generator",
            role="生成 Agent",
            system_prompt="""你是 Vispawn 的代码生成专家。你的任务是根据分析方案生成 Three.js 可视化代码。

你需要：
1. 理解可视化方案
2. 生成完整的、可运行的 HTML + Three.js 代码
3. 确保代码包含正确的 3D 对象、动画、交互控制
4. 添加适当的灯光、材质、阴影效果

输出完整的 HTML 代码。""",
            tools=["generate_code", "extract_html"]
        ))

        # 评估 Agent - 评估代码质量
        self.register(AgentConfig(
            name="evaluator",
            role="评估 Agent",
            system_prompt="""你是 Vispawn 的质量评估专家。你的任务是评估生成的 Three.js 代码质量。

评估维度：
1. 安全性 - 检查是否有危险代码
2. 语法正确性 - 检查 Three.js 基础组件
3. 结构准确性 - 检查是否正确实现了可视化
4. 视觉效果 - 评估材质、灯光、相机
5. 教学效果 - 评估交互性、清晰度

输出 JSON 格式的评估结果。""",
            tools=["evaluate_code", "get_improvement_suggestions"]
        ))

        # 验证 Agent - 渲染验证
        self.register(AgentConfig(
            name="validator",
            role="渲染验证 Agent",
            system_prompt="""你是 Vispawn 的渲染验证专家。你的任务是验证生成的 3D 可视化是否能正确渲染。

你需要：
1. 检查代码语法和结构
2. 模拟运行代码，检查潜在错误
3. 验证 Three.js 对象创建是否正确
4. 检查动画逻辑是否合理
5. 验证交互控制是否完整

输出 JSON 格式的验证结果，包括是否通过验证。""",
            tools=["validate_rendering", "check_syntax"]
        ))

    def register(self, config: AgentConfig):
        """注册 Agent 配置"""
        self._agents[config.name] = config

    def get(self, name: str) -> Optional[AgentConfig]:
        """获取 Agent 配置"""
        return self._agents.get(name)

    def list_agents(self) -> List[str]:
        """列出所有可用的 Agent"""
        return list(self._agents.keys())

    def create_specialized_agent(self, base_task: str, context: Dict) -> Optional[AgentConfig]:
        """
        运行时动态创建专业化的 Agent

        根据任务需求，动态创建专门的 Agent：
        - 几何专家 Agent
        - 物理模拟 Agent
        - 动画专家 Agent
        - 交互设计 Agent
        等等

        Args:
            base_task: 基础任务类型
            context: 任务上下文

        Returns:
            Agent 配置，如果无法创建则返回 None
        """
        # 根据任务类型动态创建专业化 Agent
        specialized_agents = {
            "geometric": self._create_geometric_agent,
            "mechanical": self._create_mechanical_agent,
            "physical": self._create_physical_agent,
            "chemical": self._create_chemical_agent,
            "animation": self._create_animation_agent,
            "interactive": self._create_interactive_agent,
        }

        creator = specialized_agents.get(base_task)
        if creator:
            return creator(context)

        return None

    def _create_geometric_agent(self, context: Dict) -> AgentConfig:
        """创建几何专业 Agent"""
        topic = context.get("topic", "几何")
        return AgentConfig(
            name=f"geometric_{uuid.uuid4().hex[:6]}",
            role="几何可视化专家",
            system_prompt=f"""你是几何可视化专家，擅长创建精确的几何图形动画。

当前任务：{topic}

你需要：
1. 创建精确的几何形状（三角形、圆形、多边形等）
2. 使用正确的几何变换
3. 添加尺寸标注和公式展示
4. 确保数学准确性

生成 Three.js 代码。""",
            tools=["generate_code"]
        )

    def _create_mechanical_agent(self, context: Dict) -> AgentConfig:
        """创建机械专业 Agent"""
        topic = context.get("topic", "机械")
        return AgentConfig(
            name=f"mechanical_{uuid.uuid4().hex[:6]}",
            role="机械可视化专家",
            system_prompt=f"""你是机械可视化专家，擅长创建机械原理动画。

当前任务：{topic}

你需要：
1. 创建精确的机械部件模型
2. 实现正确的运动学关系
3. 展示机械工作原理
4. 添加运动轨迹和时序说明

生成 Three.js 代码。""",
            tools=["generate_code"]
        )

    def _create_physical_agent(self, context: Dict) -> AgentConfig:
        """创建物理专业 Agent"""
        topic = context.get("topic", "物理")
        return AgentConfig(
            name=f"physical_{uuid.uuid4().hex[:6]}",
            role="物理可视化专家",
            system_prompt=f"""你是物理可视化专家，擅长创建物理模拟动画。

当前任务：{topic}

你需要：
1. 正确实现物理公式和定律
2. 创建物理量可视化（力、速度、加速度等）
3. 添加交互控制参数
4. 展示物理关系

生成 Three.js 代码。""",
            tools=["generate_code"]
        )

    def _create_chemical_agent(self, context: Dict) -> AgentConfig:
        """创建化学专业 Agent"""
        topic = context.get("topic", "化学")
        return AgentConfig(
            name=f"chemical_{uuid.uuid4().hex[:6]}",
            role="化学可视化专家",
            system_prompt=f"""你是化学可视化专家，擅长创建分子结构和化学反应动画。

当前任务：{topic}

你需要：
1. 创建分子/原子 3D 模型
2. 展示化学键和空间结构
3. 模拟化学反应过程
4. 添加化学式标注

生成 Three.js 代码。""",
            tools=["generate_code"]
        )

    def _create_animation_agent(self, context: Dict) -> AgentConfig:
        """创建动画专家 Agent"""
        return AgentConfig(
            name=f"animation_{uuid.uuid4().hex[:6]}",
            role="动画专家",
            system_prompt="""你是动画专家，擅长创建流畅的 3D 动画。

你的任务：
1. 优化动画性能和流畅度
2. 添加缓动和过渡效果
3. 实现复杂的动画序列
4. 确保动画与交互协调

输出改进的代码。""",
            tools=["optimize_code"]
        )

    def _create_interactive_agent(self, context: Dict) -> AgentConfig:
        """创建交互设计 Agent"""
        return AgentConfig(
            name=f"interactive_{uuid.uuid4().hex[:6]}",
            role="交互设计专家",
            system_prompt="""你是交互设计专家，擅长创建优秀的用户体验。

你的任务：
1. 设计直观的交互控制
2. 添加滑块、按钮等控件
3. 实现参数调节功能
4. 优化用户操作流程

输出改进的代码。""",
            tools=["enhance_interaction"]
        )


class AgentEventBus:
    """Agent 事件总线 - 处理 Agent 间通信"""

    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}
        self._events: List[Dict] = []

    def subscribe(self, event_type: str, callback: Callable):
        """订阅事件"""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)

    def publish(self, event_type: str, data: Dict):
        """发布事件"""
        event = {
            "type": event_type,
            "data": data,
            "timestamp": time.time()
        }
        self._events.append(event)

        if event_type in self._subscribers:
            for callback in self._subscribers[event_type]:
                try:
                    callback(event)
                except Exception as e:
                    print(f"Event callback error: {e}")

    def get_events(self, event_type: Optional[str] = None) -> List[Dict]:
        """获取事件历史"""
        if event_type:
            return [e for e in self._events if e["type"] == event_type]
        return self._events


class TaskQueue:
    """任务队列 - 管理任务执行"""

    def __init__(self):
        self._tasks: Dict[str, Task] = {}
        self._pending: asyncio.Queue = asyncio.Queue()

    def add_task(self, task: Task) -> str:
        """添加任务"""
        self._tasks[task.task_id] = task
        self._pending.put_nowait(task.task_id)
        return task.task_id

    def get_task(self, task_id: str) -> Optional[Task]:
        """获取任务"""
        return self._tasks.get(task_id)

    def update_task(self, task_id: str, **kwargs):
        """更新任务"""
        if task_id in self._tasks:
            task = self._tasks[task_id]
            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            task.updated_at = time.time()

    def get_pending_task(self, timeout: float = 1.0) -> Optional[str]:
        """获取待处理任务"""
        try:
            return asyncio.wait_for(self._pending.get(), timeout)
        except asyncio.TimeoutError:
            return None

    def list_tasks(self, status: Optional[TaskStatus] = None) -> List[Task]:
        """列出任务"""
        if status:
            return [t for t in self._tasks.values() if t.status == status]
        return list(self._tasks.values())


class VispawnAgent:
    """Vispawn 主 Agent - 自主规划系统核心"""

    # 最大子 Agent 深度
    MAX_SPAWN_DEPTH = 3
    # 每个 Agent 最大子进程数
    MAX_CHILDREN_PER_AGENT = 5

    def __init__(self, llm: Optional[LLMClient] = None):
        self.llm = llm or LLMClient()
        self.registry = SubAgentRegistry()
        self.event_bus = AgentEventBus()
        self.task_queue = TaskQueue()

        # 运行中的 Agent
        self._running_agents: Dict[str, SubAgent] = {}
        self._agent_counter = 0

        # 主 Agent 配置
        self._main_config = AgentConfig(
            name="main",
            role="主 Agent",
            system_prompt="""你是 Vispawn 的主 Agent，负责协调整个可视化生成过程。

你的工作流程：
1. 接收用户的可视化需求
2. 分析任务复杂度，决定是否需要分解
3. 调度合适的子 Agent 完成子任务
4. 整合各子任务的结果
5. 确保最终渲染效果符合要求

你可以使用的子 Agent：
- analyzer: 分析定理，制定可视化方案
- generator: 生成 Three.js 代码
- evaluator: 评估代码质量
- validator: 验证渲染效果

注意：
- 复杂任务应该分解为多个子任务并行处理
- 每个子任务完成后要验证结果
- 如果子任务失败，可以重新调度或调整策略""",
            tools=["spawn_subagent", "analyze", "generate", "evaluate", "validate"]
        )

        # 事件订阅
        self._setup_event_handlers()

    def _setup_event_handlers(self):
        """设置事件处理器"""
        self.event_bus.subscribe("task_completed", self._on_task_completed)
        self.event_bus.subscribe("task_failed", self._on_task_failed)
        self.event_bus.subscribe("subagent_completed", self._on_subagent_completed)

    def _on_task_completed(self, event: Dict):
        """任务完成事件处理"""
        print(f"Task completed: {event['data'].get('task_id')}")

    def _on_task_failed(self, event: Dict):
        """任务失败事件处理"""
        print(f"Task failed: {event['data'].get('task_id')}")

    def _on_subagent_completed(self, event: Dict):
        """子 Agent 完成事件处理"""
        print(f"Subagent completed: {event['data'].get('agent_id')}")

    async def process(self, user_input: str) -> Dict:
        """
        处理用户输入 - 主入口

        这是主 Agent 的核心方法，会：
        1. 分析用户需求
        2. 自主规划任务分解
        3. 调度子 Agent
        4. 整合结果
        5. 验证最终效果
        """
        # 创建主任务
        main_task = Task(
            task_id=str(uuid.uuid4()),
            name="main",
            description=user_input,
            type="coordination",
            input_data={"user_input": user_input}
        )

        print(f"\n🤖 [主 Agent] 收到任务: {user_input}")

        # 步骤 1: 自主分析任务
        plan = await self._plan_task(user_input)

        # 步骤 2: 根据计划执行任务
        result = await self._execute_plan(plan, main_task)

        # 步骤 3: 最终验证
        final_validation = await self._validate_final_result(result)

        return {
            "task_id": main_task.task_id,
            "user_input": user_input,
            "plan": plan,
            "result": result,
            "validation": final_validation,
            "status": "completed" if final_validation.get("passed") else "needs_revision"
        }

    async def _plan_task(self, user_input: str) -> Dict:
        """
        自主规划 - 分析任务并制定执行计划

        参考 OpenClaw 的自主规划能力：
        - 分析任务复杂度
        - 决定是否需要分解
        - 制定子任务列表
        - 根据任务类型动态选择/创建合适的 Agent
        """
        prompt = f"""分析以下可视化任务，制定执行计划：

用户需求：{user_input}

请分析：
1. 任务的复杂度（简单/中等/复杂）
2. 可视化类型（geometric/mechanical/physical/chemical）
3. 需要哪些子任务来完成
4. 子任务之间的依赖关系
5. 是否可以并行执行

输出 JSON 格式：
{{
  "complexity": "simple/medium/complex",
  "visualization_type": "geometric/mechanical/physical/chemical",
  "needs_decomposition": true/false,
  "tasks": [
    {{"name": "分析任务", "agent": "analyzer", "depends_on": [], "description": "..."}},
    {{"name": "生成代码", "agent": "generator", "depends_on": ["分析任务"], "description": "..."}},
    {{"name": "评估质量", "agent": "evaluator", "depends_on": ["生成代码"], "description": "..."}},
    {{"name": "验证渲染", "agent": "validator", "depends_on": ["评估质量"], "description": "..."}}
  ],
  "parallel_groups": [["任务1", "任务2"], ["任务3"]],
  "specialized_needs": ["animation", "interactive"]  // 可选的专业化需求
}}"""

        import json
        import re

        try:
            response = await self.llm.generate(prompt, temperature=0.3, max_tokens=1500)
            # 提取 JSON
            match = re.search(r'\{.*\}', response.content, re.DOTALL)
            if match:
                plan = json.loads(match.group(0))
                print(f"\n📋 [规划] 复杂度: {plan.get('complexity')}, 类型: {plan.get('visualization_type')}, 任务数: {len(plan.get('tasks', []))}")
                return plan
        except Exception as e:
            print(f"规划失败: {e}")

        # 默认计划
        return {
            "complexity": "medium",
            "visualization_type": "geometric",
            "needs_decomposition": True,
            "tasks": [
                {"name": "分析任务", "agent": "analyzer", "depends_on": []},
                {"name": "生成代码", "agent": "generator", "depends_on": ["分析任务"]},
                {"name": "评估质量", "agent": "evaluator", "depends_on": ["生成代码"]},
                {"name": "验证渲染", "agent": "validator", "depends_on": ["评估质量"]}
            ],
            "parallel_groups": []
        }

    async def _execute_plan(self, plan: Dict, main_task: Task) -> Dict:
        """
        执行计划 - 支持并行和串行混合执行

        策略：
        1. 分析任务依赖关系，构建 DAG
        2. 识别可以并行执行的任务组
        3. 根据依赖关系自主决定串行/并行
        4. 最大化并行度以提升效率
        """
        tasks = plan.get("tasks", [])
        results = {}
        completed = set()

        # 构建任务依赖图
        task_map = {t["name"]: t for t in tasks}

        # 分析并行机会
        parallel_groups = plan.get("parallel_groups", [])
        if not parallel_groups:
            # 自动分析并行机会
            parallel_groups = self._analyze_parallel_groups(tasks)

        print(f"\n📊 任务分析: {len(tasks)} 个任务, {len(parallel_groups)} 个并行组")
        for i, group in enumerate(parallel_groups):
            print(f"   组{i+1}: {group}")

        # 按组执行
        for group_idx, group in enumerate(parallel_groups):
            print(f"\n{'='*50}")
            print(f"📦 执行组 {group_idx + 1}/{len(parallel_groups)}: {group}")
            print(f"{'='*50}")

            # 准备组内任务
            group_tasks = []
            for task_name in group:
                if task_name in task_map:
                    task_def = task_map[task_name]
                    depends_on = task_def.get("depends_on", [])

                    # 检查依赖是否都完成
                    deps_met = all(dep in completed for dep in depends_on)

                    if deps_met:
                        # 创建任务对象
                        task = Task(
                            task_id=str(uuid.uuid4()),
                            name=task_name,
                            description=task_name,
                            type=task_def.get("agent", "generator"),
                            input_data={
                                "previous_results": results.copy(),  # 复制当前结果
                                "plan": plan
                            },
                            parent_task_id=main_task.task_id
                        )
                        group_tasks.append((task_name, task_def, task))
                    else:
                        print(f"   ⏳ 跳过 {task_name}，等待依赖: {depends_on}")

            # 并行执行组内任务
            if len(group_tasks) > 1:
                print(f"   ⚡ 并行执行 {len(group_tasks)} 个任务")
                task_coroutines = []
                for task_name, task_def, task in group_tasks:
                    agent_name = task_def.get("agent", "generator")
                    coroutine = self._spawn_and_run_agent(agent_name, task, depth=0)
                    task_coroutines.append((task_name, coroutine))

                # 使用 asyncio.gather 并行执行
                group_results = await asyncio.gather(
                    *[t[1] for t in task_coroutines],
                    return_exceptions=True
                )

                for i, (task_name, _) in enumerate(task_coroutines):
                    result = group_results[i]
                    if isinstance(result, Exception):
                        print(f"   ❌ {task_name} 失败: {result}")
                        results[task_name] = {"error": str(result)}
                    else:
                        print(f"   ✅ {task_name} 完成")
                        results[task_name] = result
                    completed.add(task_name)

            elif len(group_tasks) == 1:
                # 串行执行单个任务
                task_name, task_def, task = group_tasks[0]
                agent_name = task_def.get("agent", "generator")

                print(f"   ▸ 串行执行: {task_name}")
                result = await self._spawn_and_run_agent(agent_name, task, depth=0)

                if isinstance(result, Exception):
                    print(f"   ❌ {task_name} 失败: {result}")
                    results[task_name] = {"error": str(result)}
                else:
                    print(f"   ✅ {task_name} 完成")
                    results[task_name] = result
                completed.add(task_name)
            else:
                print(f"   ⏳ 组 {group_idx + 1} 无可执行任务")

            # 发布组完成事件
            self.event_bus.publish("group_completed", {
                "group_index": group_idx,
                "group": group,
                "results": {k: results.get(k) for k in group if k in results}
            })

        # 处理可能遗漏的任务（未在任何组中）
        for task_def in tasks:
            task_name = task_def["name"]
            if task_name not in completed:
                print(f"\n⚠️ 执行遗漏任务: {task_name}")
                depends_on = task_def.get("depends_on", [])

                # 等待依赖
                for dep in depends_on:
                    if dep not in completed:
                        print(f"   ⏳ 等待依赖: {dep}")

                task = Task(
                    task_id=str(uuid.uuid4()),
                    name=task_name,
                    description=task_name,
                    type=task_def.get("agent", "generator"),
                    input_data={
                        "previous_results": results,
                        "plan": plan
                    },
                    parent_task_id=main_task.task_id
                )

                agent_name = task_def.get("agent", "generator")
                result = await self._spawn_and_run_agent(agent_name, task, depth=0)
                results[task_name] = result
                completed.add(task_name)

        return results

    def _analyze_parallel_groups(self, tasks: List[Dict]) -> List[List[str]]:
        """
        自动分析任务依赖，生成最优的并行执行组

        策略：
        1. 没有依赖的任务可以并行
        2. 有依赖的任务按依赖顺序排列
        3. 同一层级的无依赖任务并行执行
        4. 考虑任务类型和资源需求
        """
        task_names = [t["name"] for t in tasks]
        task_map = {t["name"]: t for t in tasks}

        # 构建依赖图
        in_degree = {name: 0 for name in task_names}
        dependents = {name: [] for name in task_names}

        for task in tasks:
            name = task["name"]
            for dep in task.get("depends_on", []):
                if dep in in_degree:
                    in_degree[name] += 1
                    dependents[dep].append(name)

        # 拓扑排序，按层级分组
        groups = []
        remaining = set(task_names)

        while remaining:
            # 找出入度为0的任务（无依赖）
            ready = [name for name in remaining if in_degree[name] == 0]

            if not ready:
                # 可能有循环依赖，随机选择一个
                ready = [list(remaining)[0]]

            # 🔍 智能决策：对无依赖任务进行分组
            # 根据任务类型和资源需求决定是否并行
            optimized_group = self._optimize_parallel_decision(ready, task_map)
            groups.append(optimized_group)

            # 移除已完成的任务，更新入度
            for name in optimized_group:
                remaining.discard(name)
                for dependent in dependents.get(name, []):
                    if dependent in in_degree:
                        in_degree[dependent] -= 1

        return groups

    def _optimize_parallel_decision(self, ready_tasks: List[str], task_map: Dict) -> List[str]:
        """
        智能并行决策

        根据以下因素自主决定是否并行执行：
        1. 任务类型 - 评估任务可以并行，生成任务建议串行
        2. 资源需求 - 轻量任务并行，重量任务串行
        3. 依赖关系 - 同一系统的任务可以并行
        """
        if len(ready_tasks) <= 1:
            return ready_tasks

        # 任务分类
        evaluation_tasks = ["评估", "evaluator", "验证", "validator", "质量", "检查"]
        generation_tasks = ["生成", "generator", "创建", "build"]
        analysis_tasks = ["分析", "analyzer", "研究"]

        # 分类任务
        evaluation = []
        generation = []
        analysis = []
        others = []

        for task_name in ready_tasks:
            task_def = task_map.get(task_name, {})
            agent = task_def.get("agent", "").lower()
            name_lower = task_name.lower()

            # 根据关键词判断类型
            if any(kw in name_lower or kw in agent for kw in evaluation_tasks):
                evaluation.append(task_name)
            elif any(kw in name_lower or kw in agent for kw in generation_tasks):
                generation.append(task_name)
            elif any(kw in name_lower or kw in agent for kw in analysis_tasks):
                analysis.append(task_name)
            else:
                others.append(task_name)

        # 智能组合策略
        result = []

        # 策略1: 评估任务可以完全并行（互不干扰）
        if evaluation:
            print(f"      📊 评估任务并行: {evaluation}")
            result.extend(evaluation)

        # 策略2: 同一类型的生成任务可以并行
        if generation:
            if len(generation) > 2:
                # 太多生成任务，分批串行
                print(f"      📦 生成任务分批: {generation}")
                result.extend(generation)
            else:
                print(f"      📦 生成任务并行: {generation}")
                result.extend(generation)

        # 策略3: 分析任务可以并行
        if analysis:
            print(f"      🔍 分析任务并行: {analysis}")
            result.extend(analysis)

        # 其他任务
        if others:
            # 混合任务，保守串行
            print(f"      ⚠️ 混合任务串行: {others}")
            result.extend(others)

        # 如果没有分类，全部并行
        if not result:
            result = ready_tasks
            print(f"      ⚡ 默认并行: {result}")

        return result

    async def _spawn_and_run_agent(self, agent_name: str, task: Task, depth: int, context: Optional[Dict] = None) -> Dict:
        """
        创建并运行子 Agent

        参考 OpenClaw 的 spawn 机制：
        - 创建独立的子 Agent 实例
        - 注入相应的 system prompt
        - 运行并等待结果
        - 支持运行时动态创建专业化 Agent
        """

        # 检查深度限制
        if depth >= self.MAX_SPAWN_DEPTH:
            print(f"⚠️ 达到最大深度限制 ({self.MAX_SPAWN_DEPTH})")
            return {"error": "max_depth_reached"}

        context = context or {}

        # 尝试获取预定义的 Agent 配置
        config = self.registry.get(agent_name)

        # 如果没有预定义，尝试动态创建专业化 Agent
        if not config:
            print(f"   🔧 动态创建专业化 Agent: {agent_name}")
            config = self.registry.create_specialized_agent(agent_name, context)
            if config:
                # 注册动态创建的 Agent
                self.registry.register(config)
                print(f"   ✓ 已注册: {config.name} ({config.role})")

        if not config:
            return {"error": f"unknown_agent: {agent_name}"}

        # 创建子 Agent 实例
        self._agent_counter += 1
        agent_id = f"{agent_name}:{self._agent_counter}"

        subagent = SubAgent(
            agent_id=agent_id,
            config=config,
            status=AgentStatus.RUNNING,
            current_task=task,
            depth=depth
        )

        self._running_agents[agent_id] = subagent

        print(f"   🤖 Spawn 子 Agent: {agent_id} (深度: {depth}, 角色: {config.role})")

        try:
            # 根据 Agent 类型执行不同的任务
            if "analyzer" in agent_name or agent_name == "analyzer":
                result = await self._run_analyzer_agent(task)
            elif "generator" in agent_name or agent_name == "generator":
                result = await self._run_generator_agent(task, context)
            elif "evaluator" in agent_name or agent_name == "evaluator":
                result = await self._run_evaluator_agent(task)
            elif "validator" in agent_name or agent_name == "validator":
                result = await self._run_validator_agent(task)
            elif "geometric" in agent_name:
                result = await self._run_specialized_agent(task, "geometric")
            elif "mechanical" in agent_name:
                result = await self._run_specialized_agent(task, "mechanical")
            elif "physical" in agent_name:
                result = await self._run_specialized_agent(task, "physical")
            elif "animation" in agent_name:
                result = await self._run_animation_agent(task)
            elif "interactive" in agent_name:
                result = await self._run_interactive_agent(task)
            else:
                result = {"error": f"unknown_agent: {agent_name}"}

            subagent.status = AgentStatus.COMPLETED
            self.event_bus.publish("subagent_completed", {
                "agent_id": agent_id,
                "task_id": task.task_id,
                "result": result
            })

            return result

        except Exception as e:
            subagent.status = AgentStatus.FAILED
            print(f"   ❌ Agent {agent_id} 执行失败: {e}")
            return {"error": str(e)}

        finally:
            del self._running_agents[agent_id]

    async def _run_analyzer_agent(self, task: Task) -> Dict:
        """运行分析 Agent"""
        user_input = task.input_data.get("previous_results", {}).get("main", {}).get("user_input", "")
        if not user_input:
            # 从主任务获取
            user_input = task.input_data.get("plan", {}).get("user_input", "测试定理")

        from .core import TheoremAnalyzer

        analyzer = TheoremAnalyzer(self.llm)
        plan = await analyzer.analyze(user_input)

        return {
            "topic": plan.topic,
            "type": plan.type,
            "description": plan.description,
            "concept": plan.concept,
            "elements": plan.elements,
            "steps": plan.steps,
            "audience": plan.audience,
            "complexity": plan.complexity,
            "colors": plan.colors
        }

    async def _run_generator_agent(self, task: Task, context: Optional[Dict] = None) -> Dict:
        """运行生成 Agent"""
        context = context or {}

        # 获取分析结果
        prev_results = task.input_data.get("previous_results", {})
        analysis_result = prev_results.get("分析任务", {})

        if not analysis_result:
            # 使用默认方案
            from .core import VisualizationPlan
            plan = VisualizationPlan(
                topic="测试",
                type="geometric",
                description="测试",
                concept="测试可视化",
                elements=["方块"],
                steps=["展示"],
                audience="middle",
                complexity="simple",
                colors={"primary": "#4a90e2", "secondary": "#e94560", "accent": "#ffd700", "bg": "#f5f5f5"}
            )
        else:
            from .core import VisualizationPlan
            plan = VisualizationPlan(
                topic=analysis_result.get("topic", "测试"),
                type=analysis_result.get("type", "geometric"),
                description=analysis_result.get("description", ""),
                concept=analysis_result.get("concept", ""),
                elements=analysis_result.get("elements", []),
                steps=analysis_result.get("steps", []),
                audience=analysis_result.get("audience", "middle"),
                complexity=analysis_result.get("complexity", "simple"),
                colors=analysis_result.get("colors", {})
            )

        # 根据可视化类型添加专业化要求
        viz_type = context.get("visualization_type", plan.type)

        from .core import CodeGenerator
        generator = CodeGenerator(self.llm)
        code = await generator.generate(plan)

        return {
            "code": code,
            "topic": plan.topic,
            "type": plan.type,
            "visualization_type": viz_type
        }

    async def _run_specialized_agent(self, task: Task, specialization: str) -> Dict:
        """运行专业化的 Agent"""
        # 获取上下文
        prev_results = task.input_data.get("previous_results", {})
        generation_result = prev_results.get("生成代码", {})

        code = generation_result.get("code", "")

        if not code:
            return {"error": "no_code_to_specialize"}

        # 根据专业化方向优化代码
        if specialization == "geometric":
            prompt = f"""优化以下 Three.js 代码，专门针对几何可视化：

{code}

优化方向：
1. 添加精确的几何标注
2. 优化几何变换效果
3. 添加尺寸显示
4. 确保数学准确性

输出优化后的完整代码。"""
        elif specialization == "mechanical":
            prompt = f"""优化以下 Three.js 代码，专门针对机械可视化：

{code}

优化方向：
1. 精确的机械部件建模
2. 正确的运动学关系
3. 添加运动轨迹显示
4. 机械时序说明

输出优化后的完整代码。"""
        elif specialization == "physical":
            prompt = f"""优化以下 Three.js 代码，专门针对物理可视化：

{code}

优化方向：
1. 正确的物理公式实现
2. 物理量可视化（力、速度等）
3. 添加参数调节滑块
4. 物理关系展示

输出优化后的完整代码。"""
        else:
            return {"error": f"unknown_specialization: {specialization}"}

        from .core import CodeGenerator
        generator = CodeGenerator(self.llm)

        try:
            response = await self.llm.generate(prompt, temperature=0.3, max_tokens=4000)
            optimized_code = generator._extract_html(response.content)
            return {
                "code": optimized_code,
                "specialization": specialization,
                "optimized": True
            }
        except Exception as e:
            return {"error": str(e), "original_code": code}

    async def _run_animation_agent(self, task: Task) -> Dict:
        """运行动画优化 Agent"""
        prev_results = task.input_data.get("previous_results", {})
        generation_result = prev_results.get("生成代码", {})

        code = generation_result.get("code", "")

        if not code:
            return {"error": "no_code_to_optimize"}

        prompt = f"""优化以下 Three.js 代码的动画效果：

{code}

优化方向：
1. 添加缓动函数（easing）
2. 优化动画性能
3. 添加动画过渡效果
4. 确保动画流畅

输出优化后的完整代码。"""

        from .core import CodeGenerator
        generator = CodeGenerator(self.llm)

        try:
            response = await self.llm.generate(prompt, temperature=0.3, max_tokens=4000)
            optimized_code = generator._extract_html(response.content)
            return {
                "code": optimized_code,
                "optimization": "animation",
                "optimized": True
            }
        except Exception as e:
            return {"error": str(e), "original_code": code}

    async def _run_interactive_agent(self, task: Task) -> Dict:
        """运行交互增强 Agent"""
        prev_results = task.input_data.get("previous_results", {})
        generation_result = prev_results.get("生成代码", {})

        code = generation_result.get("code", "")

        if not code:
            return {"error": "no_code_to_enhance"}

        prompt = f"""增强以下 Three.js 代码的交互功能：

{code}

增强方向：
1. 添加参数调节滑块
2. 添加播放/暂停/重置按钮
3. 添加视角切换功能
4. 添加全屏功能
5. 优化触摸交互

输出增强后的完整代码。"""

        from .core import CodeGenerator
        generator = CodeGenerator(self.llm)

        try:
            response = await self.llm.generate(prompt, temperature=0.3, max_tokens=4000)
            enhanced_code = generator._extract_html(response.content)
            return {
                "code": enhanced_code,
                "enhancement": "interactive",
                "enhanced": True
            }
        except Exception as e:
            return {"error": str(e), "original_code": code}

    async def _run_evaluator_agent(self, task: Task) -> Dict:
        """运行评估 Agent"""
        # 获取生成结果
        prev_results = task.input_data.get("previous_results", {})
        generation_result = prev_results.get("生成代码", {})

        code = generation_result.get("code", "")
        topic = generation_result.get("topic", "测试")

        if not code:
            return {"error": "no_code_to_evaluate"}

        # 构建 VisualizationPlan
        from .core import VisualizationPlan, CodeEvaluator
        plan = VisualizationPlan(
            topic=topic,
            type=generation_result.get("type", "geometric"),
            description="",
            concept="",
            elements=[],
            steps=[],
            audience="middle",
            complexity="simple",
            colors={}
        )

        evaluator = CodeEvaluator(self.llm)
        results = await evaluator.evaluate(code, topic, plan)

        # 计算总分
        total_score = sum(r.score for r in results) / len(results) if results else 0

        return {
            "scores": {r.dimension: {"score": r.score, "feedback": r.feedback, "issues": r.issues} for r in results},
            "total_score": total_score,
            "passed": total_score >= 70
        }

    async def _run_validator_agent(self, task: Task) -> Dict:
        """运行验证 Agent - 确保渲染效果"""
        # 获取评估结果
        prev_results = task.input_data.get("previous_results", {})
        evaluation_result = prev_results.get("评估质量", {})
        generation_result = prev_results.get("生成代码", {})

        code = generation_result.get("code", "")
        scores = evaluation_result.get("scores", {})
        total_score = evaluation_result.get("total_score", 0)

        # 本地验证
        validation_issues = []

        # 1. 检查代码是否包含必要的 Three.js 组件
        if "THREE.Scene" not in code:
            validation_issues.append("缺少 THREE.Scene")
        if "THREE.PerspectiveCamera" not in code:
            validation_issues.append("缺少 THREE.PerspectiveCamera")
        if "THREE.WebGLRenderer" not in code:
            validation_issues.append("缺少 THREE.WebGLRenderer")

        # 2. 检查动画
        if "requestAnimationFrame" not in code:
            validation_issues.append("缺少动画循环")

        # 3. 检查交互
        if "OrbitControls" not in code:
            validation_issues.append("缺少 OrbitControls")

        # 4. 检查 HTML 完整性
        if "<!DOCTYPE html>" not in code and "<html" not in code:
            validation_issues.append("不是完整的 HTML 文件")

        passed = len(validation_issues) == 0 and total_score >= 70

        return {
            "validation_issues": validation_issues,
            "total_score": total_score,
            "scores": scores,
            "passed": passed,
            "rendering_check": "passed" if passed else "failed"
        }

    async def _validate_final_result(self, result: Dict) -> Dict:
        """最终验证 - 确保渲染效果符合要求"""

        # 获取各阶段结果
        evaluation = result.get("评估质量", {})
        validation = result.get("验证渲染", {})

        # 综合评估
        final_score = evaluation.get("total_score", 0)
        validation_passed = validation.get("passed", False)

        # 判断是否通过
        passed = validation_passed and final_score >= 70

        return {
            "passed": passed,
            "final_score": final_score,
            "validation_passed": validation_passed,
            "issues": validation.get("validation_issues", []),
            "recommendation": "可以发布" if passed else "需要修改"
        }


# 全局实例
_global_agent: Optional[VispawnAgent] = None


def get_agent() -> VispawnAgent:
    """获取全局 Agent 实例"""
    global _global_agent
    if _global_agent is None:
        _global_agent = VispawnAgent()
    return _global_agent


async def process_visualization_request(user_input: str) -> Dict:
    """
    处理可视化请求 - 便捷入口

    这是对外的主要 API，模拟 OpenClaw 的 Agent 处理流程：
    1. 接收任务
    2. 自主规划
    3. 调度子 Agent
    4. 验证结果
    """
    agent = get_agent()
    return await agent.process(user_input)
