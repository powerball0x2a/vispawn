"""
核心逻辑 - 分析、生成、评估
"""
import asyncio
import json
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .llm import LLMClient


@dataclass
class VisualizationPlan:
    """可视化方案"""
    topic: str
    type: str
    description: str
    concept: str
    elements: List[str]
    steps: List[str]
    audience: str
    complexity: str
    colors: Dict[str, str]


@dataclass
class EvaluationResult:
    """评估结果"""
    dimension: str
    score: float
    feedback: str
    issues: List[str] = field(default_factory=list)


class TheoremAnalyzer:
    """定理分析器"""

    # 预设定理
    PRESETS = {
        "勾股定理": {
            "type": "geometric",
            "description": "直角三角形两直角边的平方和等于斜边的平方",
            "concept": "在直角三角形三边上构建正方形，用方块填充展示面积相等",
            "elements": ["直角三角形", "正方形", "面积方块"],
            "steps": ["展示直角三角形", "构建正方形", "填充方块", "验证面积相等"],
            "audience": "middle", "complexity": "simple",
            "colors": {"primary": "#4a90e2", "secondary": "#e94560", "accent": "#ffd700", "bg": "#f5f5f5"}
        },
        "四冲程发动机": {
            "type": "mechanical",
            "description": "内燃机通过进气、压缩、做功、排气四个冲程完成工作循环",
            "concept": "展示活塞、连杆、曲轴联动，配合气门开闭",
            "elements": ["活塞", "连杆", "曲轴", "气门", "火花塞"],
            "steps": ["进气冲程", "压缩冲程", "做功冲程", "排气冲程"],
            "audience": "high", "complexity": "medium",
            "colors": {"primary": "#4a90e2", "secondary": "#e94560", "accent": "#ffd700", "bg": "#1a1a2e"}
        },
        "圆的面积": {
            "type": "geometric",
            "description": "圆的面积等于π乘以半径的平方",
            "concept": "将圆分割成扇形并重组成长方形，展示公式推导",
            "elements": ["圆", "扇形", "长方形"],
            "steps": ["展示圆", "分割扇形", "重组成长方形", "推导公式"],
            "audience": "middle", "complexity": "simple",
            "colors": {"primary": "#4a90e2", "secondary": "#1abc9c", "accent": "#ffd700", "bg": "#f5f5f5"}
        },
        "牛顿第二定律": {
            "type": "physical",
            "description": "物体加速度与作用力成正比，与质量成反比",
            "concept": "展示不同质量物体在相同力作用下的加速度差异",
            "elements": ["物体", "力矢量", "加速度指示"],
            "steps": ["展示公式", "改变质量观察加速度", "改变力观察加速度", "总结关系"],
            "audience": "high", "complexity": "medium",
            "colors": {"primary": "#e94560", "secondary": "#00d9ff", "accent": "#ffd700", "bg": "#1a1a2e"}
        },
    }

    def __init__(self, llm: LLMClient):
        self.llm = llm

    async def analyze(self, theorem: str) -> VisualizationPlan:
        """分析定理/概念，返回可视化方案"""

        # 1. 预检查：判断是否可以可视化
        can_visualize, reason = await self._check_visualizability(theorem)
        if not can_visualize:
            # 返回一个特殊的"不可可视化"方案
            raise ValueError(f"无法可视化: {reason}")

        # 2. 检查预设
        for key, preset in self.PRESETS.items():
            if key in theorem or theorem in key:
                return VisualizationPlan(topic=theorem, **preset)

        # 3. AI 分析
        prompt = f"""分析"{theorem}"，判断是否适合生成3D可视化：

如果适合，返回JSON：
{{
  "type": "geometric/mechanical/physical/chemical/conceptual",
  "can_visualize": true,
  "description": "50字内解释",
  "concept": "可视化思路",
  "elements": ["元素1", "元素2"],
  "steps": ["步骤1", "步骤2"],
  "audience": "middle/high",
  "complexity": "simple/medium"
}}

如果不适合，返回：
{{
  "can_visualize": false,
  "reason": "不适合可视化的原因"
}}"""

        try:
            response = await self.llm.generate(prompt, temperature=0.4)
            data = json.loads(self._extract_json(response.content))

            # 检查是否可以可视化
            if not data.get("can_visualize", True):
                raise ValueError(f"AI判断无法可视化: {data.get('reason', '未知原因')}")

            return VisualizationPlan(
                topic=theorem,
                type=data.get("type", "geometric"),
                description=data.get("description", ""),
                concept=data.get("concept", ""),
                elements=data.get("elements", []),
                steps=data.get("steps", []),
                audience=data.get("audience", "middle"),
                complexity=data.get("complexity", "medium"),
                colors={"primary": "#4a90e2", "secondary": "#e94560", "accent": "#ffd700", "bg": "#1a1a2e"}
            )
        except ValueError:
            # 重新抛出可可视化错误
            raise
        except Exception as e:
            # 默认方案（质量可能不佳）
            return VisualizationPlan(
                topic=theorem, type="geometric", description=theorem,
                concept="3D可视化展示", elements=["主要对象"], steps=["展示", "演示"],
                audience="middle", complexity="medium",
                colors={"primary": "#4a90e2", "secondary": "#e94560", "accent": "#ffd700", "bg": "#1a1a2e"}
            )

    async def _check_visualizability(self, theorem: str) -> tuple:
        """
        预检查：判断输入是否可以被可视化

        Returns:
            (can_visualize: bool, reason: str)
        """
        # 1. 明显不可视化的输入
        non_visualizable_patterns = [
            r"^\d+$",  # 纯数字
            r"^[a-zA-Z]+$",  # 纯英文单词
            r"^[\W]+$",  # 纯符号
        ]
        import re
        for pattern in non_visualizable_patterns:
            if re.match(pattern, theorem.strip()):
                return False, "输入过于简单或抽象"

        # 2. 长度检查
        if len(theorem) < 2:
            return False, "输入长度不足"
        if len(theorem) > 50:
            return False, "输入长度过长，请简化"

        # 3. 调用 LLM 判断（轻量级）
        prompt = f"""判断以下概念是否可以用Three.js生成3D可视化动画：

"{theorem}"

只回答"可以"或"不可以"，如果不可以，用一句话说明原因。"""

        try:
            response = await self.llm.generate(prompt, temperature=0.1, max_tokens=50)
            content = response.content.lower().strip()

            if "不可以" in content or "不能" in content or "无法" in content:
                # 提取原因
                reason = content
                return False, reason
        except:
            pass  # 如果判断失败，默认可以尝试

        return True, ""

    def _extract_json(self, text: str) -> str:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        return match.group(0) if match else "{}"


class CodeGenerator:
    """代码生成器 - 使用多Agent评估和迭代优化生成代码"""

    def __init__(self, llm: LLMClient):
        self.llm = llm

    async def generate(self, plan: VisualizationPlan) -> str:
        """生成 Three.js 代码"""

        # 针对机械类可视化的特殊要求
        mechanical_requirements = ""
        if plan.type == "mechanical":
            mechanical_requirements = f"""
【机械结构准确性要求 - 必须严格遵守】
这是一个机械原理可视化，必须准确展示各部件的结构和运动关系：

1. 部件建模要求：
   - 活塞：圆柱体，真实比例（直径略小于气缸）
   - 连杆：长条形，连接活塞和曲轴
   - 曲轴：包含主轴颈、曲柄臂、连杆轴颈三部分
   - 气缸：半透明圆筒，约束活塞运动
   - 气门：进气门（绿色）、排气门（红色），能上下运动表示开闭
   - 火花塞：位于气缸顶部中央位置

2. 运动学要求（极其重要）：
   - 曲轴做旋转运动（0-360度）
   - 活塞只做上下直线运动，不能旋转
   - 连杆做平面运动，一端随活塞上下，一端随曲轴旋转
   - 活塞位置公式：y = 中心位置 + cos(角度) * 曲轴半径
   - 连杆角度应通过几何计算：atan2(曲轴x偏移, 活塞y - 曲轴y)

3. 四冲程时序（720度完成一个循环）：
   - 0-180度：进气冲程 - 进气门开，排气门关，活塞下行
   - 180-360度：压缩冲程 - 两气门都关，活塞上行
   - 360-540度：做功冲程 - 两气门都关，火花塞点火，活塞下行
   - 540-720度：排气冲程 - 排气门开，进气门关，活塞上行

4. 视觉效果：
   - 添加阴影效果增强立体感
   - 不同部件使用不同颜色区分
   - 添加冲程信息显示
"""

        prompt = f"""生成"{plan.topic}"的Three.js可视化代码。

方案：{plan.concept}
类型：{plan.type}
元素：{', '.join(plan.elements)}
步骤：{', '.join(plan.steps)}
受众：{plan.audience}

颜色：主色{plan.colors['primary']}，辅色{plan.colors['secondary']}，强调色{plan.colors['accent']}，背景{plan.colors['bg']}

{mechanical_requirements}

通用要求：
1. 完整HTML文件，使用Three.js CDN (r160)
2. 使用OrbitControls允许用户旋转视角
3. 动画使用requestAnimationFrame，播放/暂停可控
4. 中文标签和说明
5. 提供play/pause/reset按钮控制
6. 响应式设计，适应窗口大小
7. 视觉风格现代专业，有适当的灯光和阴影

输出完整可运行的HTML代码，确保代码能直接运行并正确展示原理。"""

        response = await self.llm.generate(prompt, temperature=0.3, max_tokens=4000)
        return self._extract_html(response.content)

    def _extract_html(self, text: str) -> str:
        """提取HTML"""
        if "```html" in text:
            start = text.find("```html") + 7
            end = text.find("```", start)
            return text[start:end].strip()
        if "```" in text:
            start = text.find("```") + 3
            end = text.find("```", start)
            return text[start:end].strip()
        return text.strip()


@dataclass
class GenerationStep:
    """生成步骤记录"""
    step: str
    status: str  # "running", "completed", "failed"
    message: str
    timestamp: float
    details: Optional[Dict] = None


class CodeEvaluator:
    """代码评估器 - 多维度评估生成结果"""

    def __init__(self, llm: LLMClient):
        self.llm = llm

    async def evaluate(self, code: str, topic: str, plan: VisualizationPlan) -> List[EvaluationResult]:
        """评估代码质量 - 多维度评估"""

        results = []

        # 1. 安全检测 (本地)
        dangerous = ['eval(', 'Function(', 'document.write', 'parent.', 'top.', 'innerHTML']
        security_issues = [d for d in dangerous if d in code]
        results.append(EvaluationResult(
            dimension="security",
            score=max(0, 100 - len(security_issues) * 30),
            feedback="安全检测通过" if not security_issues else f"发现{len(security_issues)}个安全问题",
            issues=security_issues
        ))

        # 2. 语法检测 (本地)
        syntax_checks = [
            ("THREE.Scene" in code, "缺少Scene"),
            ("THREE.PerspectiveCamera" in code, "缺少Camera"),
            ("THREE.WebGLRenderer" in code, "缺少Renderer"),
            ("requestAnimationFrame" in code, "缺少动画循环"),
            ("<!DOCTYPE html>" in code, "不是完整HTML文件"),
            ("three@0.160" in code or "three.js" in code.lower(), "缺少Three.js引用"),
        ]
        syntax_issues = [msg for check, msg in syntax_checks if not check]
        results.append(EvaluationResult(
            dimension="syntax",
            score=max(0, 100 - len(syntax_issues) * 20),
            feedback="语法检测通过" if not syntax_issues else f"缺少: {', '.join(syntax_issues)}",
            issues=syntax_issues
        ))

        # 3. 结构准确性检测 (根据类型)
        accuracy_issues = []

        if plan.type == "mechanical":
            # 机械类：检查运动部件
            mechanical_checks = [
                ("position" in code or "rotation" in code, "缺少运动实现"),
                ("Math.sin" in code or "Math.cos" in code or "animate" in code, "缺少动画计算"),
                ("addEventListener" in code, "缺少交互控制"),
            ]
            accuracy_issues = [msg for check, msg in mechanical_checks if not check]

        elif plan.type == "geometric":
            # 几何类：检查图形元素
            geometric_checks = [
                ("Geometry" in code or "geometry" in code.lower(), "缺少几何体"),
                ("Mesh" in code, "缺少Mesh对象"),
                ("position" in code or "scale" in code, "缺少变换操作"),
                ("add(" in code, "缺少场景添加"),
            ]
            accuracy_issues = [msg for check, msg in geometric_checks if not check]

        elif plan.type == "physical":
            # 物理类：检查物理模拟
            physical_checks = [
                ("velocity" in code.lower() or "speed" in code.lower(), "缺少速度概念"),
                ("force" in code.lower() or "acceleration" in code.lower(), "缺少力/加速度"),
                ("animate" in code or "requestAnimationFrame" in code, "缺少动画循环"),
            ]
            accuracy_issues = [msg for check, msg in physical_checks if not check]

        # 通用准确性检查
        general_checks = [
            (plan.topic[:3] in code or plan.topic[-3:] in code or plan.concept[:3] in code,
             f"未体现主题'{plan.topic}'的关键内容"),
        ]
        accuracy_issues.extend([msg for check, msg in general_checks if not check])

        if accuracy_issues:
            results.append(EvaluationResult(
                dimension="accuracy",
                score=max(0, 100 - len(accuracy_issues) * 20),
                feedback=f"准确性问题: {', '.join(accuracy_issues[:3])}",
                issues=accuracy_issues
            ))

        # 4. AI 评估视觉效果
        visual_prompt = f"""评估以下Three.js代码的视觉效果(0-100)：

代码片段：
{code[:1500]}

主题：{topic}
类型：{plan.type}

从以下维度评估并返回JSON：
{{
  "score": 0-100,
  "feedback": "简要评价",
  "lighting": "灯光效果评价",
  "materials": "材质效果评价",
  "camera": "相机设置评价"
}}"""

        try:
            response = await self.llm.generate(visual_prompt, temperature=0.3, max_tokens=1000)
            data = json.loads(self._extract_json(response.content))
            results.append(EvaluationResult(
                dimension="visual",
                score=data.get("score", 70),
                feedback=data.get("feedback", "视觉评估完成"),
                issues=[]
            ))
        except Exception as e:
            results.append(EvaluationResult(
                dimension="visual",
                score=70,
                feedback=f"视觉评估失败: {str(e)}",
                issues=[]
            ))

        # 5. AI 评估教学效果
        edu_prompt = f"""评估"{topic}"可视化代码的教学效果(0-100)：

代码片段：
{code[:1500]}

目标受众：{plan.audience}
复杂度：{plan.complexity}

从以下维度评估并返回JSON：
{{
  "score": 0-100,
  "feedback": "教学效果评价",
  "clarity": "清晰度评价",
  "interactivity": "交互性评价",
  "concept_accuracy": "概念准确性评价"
}}"""

        try:
            response = await self.llm.generate(edu_prompt, temperature=0.3, max_tokens=1000)
            data = json.loads(self._extract_json(response.content))
            results.append(EvaluationResult(
                dimension="pedagogy",
                score=data.get("score", 70),
                feedback=data.get("feedback", "教学评估完成"),
                issues=[]
            ))
        except Exception as e:
            results.append(EvaluationResult(
                dimension="pedagogy",
                score=70,
                feedback=f"教学评估失败: {str(e)}",
                issues=[]
            ))

        return results

    def get_improvement_suggestions(self, results: List[EvaluationResult], plan: VisualizationPlan) -> str:
        """根据评估结果生成改进建议"""
        suggestions = []

        for result in results:
            if result.score < 80 and result.issues:
                if result.dimension == "syntax":
                    suggestions.append("确保代码包含完整的Three.js基础组件（Scene、Camera、Renderer）")
                elif result.dimension == "accuracy":
                    suggestions.append(f"改进机械结构准确性: {', '.join(result.issues)}")
                elif result.dimension == "security":
                    suggestions.append("移除不安全的代码模式")
                elif result.dimension == "visual":
                    suggestions.append("增强视觉效果：添加更好的灯光、材质和阴影")
                elif result.dimension == "pedagogy":
                    suggestions.append("改进教学效果：添加步骤说明和更好的交互控制")

        if plan.type == "mechanical":
            suggestions.append("确保活塞只做直线运动，曲轴只做旋转运动，运动关系符合物理约束")

        return "\n".join(suggestions) if suggestions else "代码质量良好，无需改进"

    def _extract_json(self, text: str) -> str:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        return match.group(0) if match else "{}"


class VizGenPipeline:
    """完整流程 - 支持多智能体评估和迭代优化"""

    def __init__(self):
        self.llm = LLMClient()
        self.analyzer = TheoremAnalyzer(self.llm)
        self.generator = CodeGenerator(self.llm)
        self.evaluator = CodeEvaluator(self.llm)
        self.generation_steps: List[GenerationStep] = []

    def _log_step(self, step: str, status: str, message: str, details: Optional[Dict] = None):
        """记录生成步骤"""
        import time
        self.generation_steps.append(GenerationStep(
            step=step,
            status=status,
            message=message,
            timestamp=time.time(),
            details=details
        ))
        print(f"[{status.upper()}] {step}: {message}")

    async def generate(self, theorem: str, max_iterations: int = 3) -> Dict:
        """生成可视化 - 带评估反馈的迭代优化"""

        self.generation_steps = []
        self._log_step("analysis", "running", f"开始分析定理: {theorem}")

        # 1. 分析
        plan = await self.analyzer.analyze(theorem)
        self._log_step("analysis", "completed", f"类型: {plan.type}, 复杂度: {plan.complexity}")

        # 2. 生成 + 评估迭代
        best_code = ""
        best_score = 0
        best_results = []
        iteration_history = []

        for i in range(max_iterations):
            self._log_step(f"iteration_{i+1}", "running", f"第 {i+1}/{max_iterations} 轮迭代")

            # 生成代码
            if i == 0 or not iteration_history[-1].get("improvement_prompt"):
                # 首次生成或无需改进
                code = await self.generator.generate(plan)
            else:
                # 基于改进建议重新生成
                improvement_prompt = iteration_history[-1]["improvement_prompt"]
                code = await self._regenerate_with_feedback(plan, improvement_prompt)

            # 评估
            results = await self.evaluator.evaluate(code, theorem, plan)

            # 计算总分
            total = sum(r.score for r in results) / len(results)
            has_issues = any(r.issues for r in results)

            iteration_data = {
                "iteration": i + 1,
                "score": total,
                "results": results,
                "has_issues": has_issues
            }

            self._log_step(
                f"iteration_{i+1}",
                "completed" if total >= 75 else "warning",
                f"得分: {total:.1f}, 问题数: {sum(len(r.issues) for r in results)}",
                {"scores": {r.dimension: r.score for r in results}}
            )

            if total > best_score:
                best_score = total
                best_code = code
                best_results = results
                self._log_step("best_update", "completed", f"更新最佳代码，新得分: {total:.1f}")

            # 如果质量够高，提前结束
            if total >= 80 and not has_issues:
                self._log_step("early_stop", "completed", f"代码质量达标 (>=80)，提前结束")
                break

            # 生成改进建议用于下一轮
            if i < max_iterations - 1:
                improvement = self.evaluator.get_improvement_suggestions(results, plan)
                iteration_data["improvement_prompt"] = improvement
                self._log_step("improvement", "info", f"改进建议: {improvement[:100]}...")

            iteration_history.append(iteration_data)

        # 最终评估
        passed = best_score >= 70
        self._log_step("final", "completed" if passed else "failed", f"最终得分: {best_score:.1f}")

        return {
            "plan": {
                "topic": plan.topic,
                "type": plan.type,
                "description": plan.description,
                "concept": plan.concept,
                "elements": plan.elements,
                "steps": plan.steps,
                "audience": plan.audience,
                "complexity": plan.complexity,
            },
            "code": best_code,
            "total_score": round(best_score, 1),
            "passed": passed,
            "scores": {r.dimension: {"score": r.score, "feedback": r.feedback, "issues": r.issues} for r in best_results},
            "generation_log": [
                {"step": s.step, "status": s.status, "message": s.message, "details": s.details}
                for s in self.generation_steps
            ],
            "iterations": len(iteration_history),
        }

    async def _regenerate_with_feedback(self, plan: VisualizationPlan, feedback: str) -> str:
        """基于反馈重新生成代码"""
        prompt = f"""重新生成"{plan.topic}"的Three.js可视化代码。

方案：{plan.concept}
类型：{plan.type}
元素：{', '.join(plan.elements)}
步骤：{', '.join(plan.steps)}

上一轮评估的改进建议：
{feedback}

请根据以上改进建议，生成更准确、更高质量的代码。

要求：
1. 完整HTML文件，使用Three.js CDN (r160)
2. 修复上一轮代码中的所有问题
3. 确保机械结构和运动关系准确
4. 提供完整的播放控制功能

输出完整可运行的HTML代码。"""

        response = await self.llm.generate(prompt, temperature=0.3, max_tokens=4000)
        return self.generator._extract_html(response.content)
