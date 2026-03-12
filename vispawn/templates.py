"""
预设模板 - Vispawn 内置的可视化方案
"""
from typing import Dict, List, Any

# 预设模板库
# 每个模板包含完整的可视化方案配置

TEMPLATES: Dict[str, Dict[str, Any]] = {
    "勾股定理": {
        "type": "geometric",
        "description": "直角三角形两直角边的平方和等于斜边的平方",
        "concept": "在直角三角形三边上构建正方形，用方块填充展示面积相等",
        "elements": ["直角三角形", "正方形", "面积方块"],
        "steps": ["展示直角三角形", "构建正方形", "填充方块", "验证面积相等"],
        "audience": "middle",
        "complexity": "simple",
        "colors": {
            "primary": "#4a90e2",
            "secondary": "#e94560",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["几何", "数学", "面积", "初中"]
    },

    "四冲程发动机": {
        "type": "mechanical",
        "description": "内燃机通过进气、压缩、做功、排气四个冲程完成工作循环",
        "concept": "展示活塞、连杆、曲轴联动，配合气门开闭",
        "elements": ["活塞", "连杆", "曲轴", "气门", "火花塞"],
        "steps": ["进气冲程", "压缩冲程", "做功冲程", "排气冲程"],
        "audience": "high",
        "complexity": "medium",
        "colors": {
            "primary": "#4a90e2",
            "secondary": "#e94560",
            "accent": "#ffd700",
            "bg": "#1a1a2e"
        },
        "tags": ["机械", "物理", "发动机", "高中"]
    },

    "圆的面积": {
        "type": "geometric",
        "description": "圆的面积等于π乘以半径的平方",
        "concept": "将圆分割成扇形并重组成长方形，展示公式推导",
        "elements": ["圆", "扇形", "长方形"],
        "steps": ["展示圆", "分割扇形", "重组成长方形", "推导公式"],
        "audience": "middle",
        "complexity": "simple",
        "colors": {
            "primary": "#4a90e2",
            "secondary": "#1abc9c",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["几何", "数学", "圆", "初中"]
    },

    "牛顿第二定律": {
        "type": "physical",
        "description": "物体加速度与作用力成正比，与质量成反比",
        "concept": "展示不同质量物体在相同力作用下的加速度差异",
        "elements": ["物体", "力矢量", "加速度指示"],
        "steps": ["展示公式", "改变质量观察加速度", "改变力观察加速度", "总结关系"],
        "audience": "high",
        "complexity": "medium",
        "colors": {
            "primary": "#e94560",
            "secondary": "#00d9ff",
            "accent": "#ffd700",
            "bg": "#1a1a2e"
        },
        "tags": ["物理", "力学", "牛顿", "高中"]
    },

    # ========== 数学类模板 ==========

    "三角函数sin/cos图像": {
        "type": "geometric",
        "description": "正弦和余弦函数在单位圆上的周期性变化图像",
        "concept": "在单位圆中展示角度变化，同步绘制sin/cos波形曲线",
        "elements": ["单位圆", "角度指针", "正弦线", "余弦线", "波形曲线"],
        "steps": ["展示单位圆", "旋转角度指针", "同步正弦余弦值", "绘制完整波形"],
        "audience": "high",
        "complexity": "medium",
        "colors": {
            "primary": "#4a90e2",
            "secondary": "#e94560",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["几何", "数学", "三角函数", "高中"]
    },

    "指数函数图像": {
        "type": "geometric",
        "description": "指数函数y=a^x的图像性质与变化规律",
        "concept": "动态展示不同底数a的指数函数图像，比较增长趋势",
        "elements": ["坐标系", "指数曲线", "底数控制", "动态点"],
        "steps": ["建立坐标系", "绘制y=2^x", "绘制y=e^x", "绘制y=0.5^x", "比较增长趋势"],
        "audience": "high",
        "complexity": "medium",
        "colors": {
            "primary": "#9b59b6",
            "secondary": "#1abc9c",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["数学", "函数", "指数", "高中"]
    },

    "对数函数图像": {
        "type": "geometric",
        "description": "对数函数y=log_a(x)与指数函数的反函数关系",
        "concept": "展示对数函数图像，与指数函数关于y=x对称",
        "elements": ["坐标系", "对数曲线", "指数曲线", "对称轴y=x"],
        "steps": ["绘制y=log_2(x)", "绘制y=ln(x)", "绘制y=x对称轴", "展示反函数关系"],
        "audience": "high",
        "complexity": "medium",
        "colors": {
            "primary": "#e67e22",
            "secondary": "#3498db",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["数学", "函数", "对数", "高中"]
    },

    "抛物线二次函数": {
        "type": "geometric",
        "description": "二次函数y=ax^2+bx+c的图像特征与性质",
        "concept": "动态展示抛物线的开口方向、顶点位置、对称轴",
        "elements": ["坐标系", "抛物线", "顶点", "对称轴", "参数控制"],
        "steps": ["展示标准抛物线", "改变a观察开口", "改变b观察平移", "改变c观察上下移动", "标注顶点与焦点"],
        "audience": "high",
        "complexity": "medium",
        "colors": {
            "primary": "#e74c3c",
            "secondary": "#3498db",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["数学", "函数", "二次函数", "初中", "高中"]
    },

    "正多边形面积": {
        "type": "geometric",
        "description": "正多边形面积公式的推导与计算",
        "concept": "将正多边形分割为等腰三角形，展示面积公式S=n·a²/(4·tan(π/n))",
        "elements": ["正多边形", "中心连线", "边心距", "分割三角形"],
        "steps": ["展示正多边形", "分割为三角形", "推导单个三角形面积", "推导总面积公式"],
        "audience": "high",
        "complexity": "medium",
        "colors": {
            "primary": "#1abc9c",
            "secondary": "#9b59b6",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["几何", "数学", "多边形", "高中"]
    },

    "圆锥体积公式": {
        "type": "geometric",
        "description": "圆锥体积等于同底等高圆柱体积的三分之一",
        "concept": "用倒水实验展示圆锥与圆柱的体积关系",
        "elements": ["圆锥", "圆柱", "液体", "底面", "高"],
        "steps": ["展示圆锥与圆柱", "将圆锥水倒入圆柱", "三次倒满验证关系", "推导公式V=1/3πr²h"],
        "audience": "middle",
        "complexity": "medium",
        "colors": {
            "primary": "#f39c12",
            "secondary": "#3498db",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["几何", "数学", "立体几何", "初中"]
    },

    "球体积公式": {
        "type": "geometric",
        "description": "球体积公式V=4/3πr³的推导过程",
        "concept": "使用祖暅原理，将球体与圆柱、圆锥对比展示体积关系",
        "elements": ["球体", "圆柱", "圆锥", "截面"],
        "steps": ["展示球体", "展示圆柱挖圆锥", "对比截面面积", "推导球体积公式"],
        "audience": "high",
        "complexity": "complex",
        "colors": {
            "primary": "#e94560",
            "secondary": "#4a90e2",
            "accent": "#ffd700",
            "bg": "#1a1a2e"
        },
        "tags": ["几何", "数学", "立体几何", "高中"]
    },

    "相似三角形": {
        "type": "geometric",
        "description": "相似三角形的对应边成比例，对应角相等",
        "concept": "展示两个相似三角形，边动画显示比例关系",
        "elements": ["三角形A", "三角形B", "对应边", "比例标注", "对应角"],
        "steps": ["展示第一个三角形", "等比放大得到第二个", "标注对应边", "验证比例相等", "标注对应角相等"],
        "audience": "middle",
        "complexity": "simple",
        "colors": {
            "primary": "#4a90e2",
            "secondary": "#27ae60",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["几何", "数学", "相似", "初中"]
    },

    "概率骰子实验": {
        "type": "geometric",
        "description": "用骰子展示古典概型的概率计算方法",
        "concept": "模拟多次掷骰子，统计各点数出现的频率趋向理论概率",
        "elements": ["骰子", "统计表格", "频率直方图", "理论概率线"],
        "steps": ["展示骰子", "动画掷骰子过程", "统计各点数频率", "绘制频率直方图", "趋向理论概率"],
        "audience": "middle",
        "complexity": "medium",
        "colors": {
            "primary": "#9b59b6",
            "secondary": "#e74c3c",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["数学", "概率", "统计", "初中"]
    },

    "排列组合": {
        "type": "geometric",
        "description": "排列A(n,m)与组合C(n,m)的概念与计算",
        "concept": "用具体例子展示排列与组合的区别与计算方法",
        "elements": ["元素集合", "排列树", "组合图", "公式展示"],
        "steps": ["展示元素集合", "展示排列选择过程", "展示组合分组方式", "对比公式差异"],
        "audience": "high",
        "complexity": "medium",
        "colors": {
            "primary": "#3498db",
            "secondary": "#e67e22",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["数学", "排列", "组合", "高中"]
    },

    # ========== 物理类模板 ==========

    "光的折射": {
        "type": "physical",
        "description": "光从一种介质进入另一种介质时传播方向发生改变",
        "concept": "展示光在不同介质界面的折射现象，验证折射定律",
        "elements": ["光源", "入射光", "折射光", "法线", "介质界面"],
        "steps": ["展示光源", "发射光线", "到达界面发生折射", "测量入射角与折射角", "验证斯涅尔定律"],
        "audience": "middle",
        "complexity": "medium",
        "colors": {
            "primary": "#f1c40f",
            "secondary": "#3498db",
            "accent": "#e74c3c",
            "bg": "#1a1a2e"
        },
        "tags": ["物理", "光学", "折射", "初中"]
    },

    "电磁感应": {
        "type": "physical",
        "description": "闭合电路的一部分导体在磁场中运动产生感应电流",
        "concept": "展示导体切割磁感线产生感应电流的实验现象",
        "elements": ["磁铁", "导体棒", "电流表", "磁场线", "电路"],
        "steps": ["展示磁场", "导体静止无电流", "导体运动产生电流", "改变运动方向", "改变磁场方向"],
        "audience": "high",
        "complexity": "complex",
        "colors": {
            "primary": "#e74c3c",
            "secondary": "#3498db",
            "accent": "#ffd700",
            "bg": "#1a1a2e"
        },
        "tags": ["物理", "电磁学", "感应", "高中"]
    },

    "自由落体": {
        "type": "physical",
        "description": "物体只在重力作用下从静止开始下落的运动",
        "concept": "展示不同物体同时落地，验证重力加速度相同",
        "elements": ["下落物体", "时间刻度", "速度矢量", "加速度指示"],
        "steps": ["释放物体", "显示下落过程", "显示时间与位移", "多物体对比", "推导公式"],
        "audience": "middle",
        "complexity": "simple",
        "colors": {
            "primary": "#e94560",
            "secondary": "#4a90e2",
            "accent": "#ffd700",
            "bg": "#1a1a2e"
        },
        "tags": ["物理", "力学", "运动学", "高中"]
    },

    "简谐振动": {
        "type": "physical",
        "description": "弹簧振子在理想条件下的周期性往复运动",
        "concept": "展示弹簧振子的位移、速度、加速度随时间变化规律",
        "elements": ["弹簧", "振子", "平衡位置", "位移箭头", "振动图像"],
        "steps": ["展示弹簧振子", "开始振动", "同步位移图像", "同步速度图像", "同步加速度图像"],
        "audience": "high",
        "complexity": "complex",
        "colors": {
            "primary": "#9b59b6",
            "secondary": "#1abc9c",
            "accent": "#ffd700",
            "bg": "#1a1a2e"
        },
        "tags": ["物理", "力学", "振动", "高中"]
    },

    "波动传播": {
        "type": "physical",
        "description": "机械波在介质中的传播过程与特点",
        "concept": "展示横波或纵波的传播，动画显示波形移动",
        "elements": ["波源", "传播介质点", "波形曲线", "波长标尺", "能量指示"],
        "steps": ["展示波源振动", "带动相邻介质点", "形成波形曲线", "波形向前传播", "标注波长与周期"],
        "audience": "high",
        "complexity": "complex",
        "colors": {
            "primary": "#3498db",
            "secondary": "#e74c3c",
            "accent": "#ffd700",
            "bg": "#1a1a2e"
        },
        "tags": ["物理", "波动", "机械波", "高中"]
    },

    "热传导": {
        "type": "physical",
        "description": "热量从高温物体向低温物体传递的过程",
        "concept": "展示金属棒的热传导，观测温度随位置和时间的变化",
        "elements": ["热源", "金属棒", "温度指示点", "热分子动画", "温度梯度颜色"],
        "steps": ["点燃热源", "热量从一端传入", "温度梯度形成", "热传导动画", "显示温度分布曲线"],
        "audience": "middle",
        "complexity": "medium",
        "colors": {
            "primary": "#e74c3c",
            "secondary": "#f39c12",
            "accent": "#3498db",
            "bg": "#1a1a2e"
        },
        "tags": ["物理", "热学", "传导", "初中"]
    },

    "万有引力": {
        "type": "physical",
        "description": "任意两个物体之间存在相互吸引的力",
        "concept": "展示行星围绕太阳的轨道运动，验证万有引力定律",
        "elements": ["太阳", "行星", "轨道", "引力矢量", "向心力指示"],
        "steps": ["展示太阳系", "行星公转轨道", "显示引力方向", "引力提供向心力", "推导万有引力公式"],
        "audience": "high",
        "complexity": "complex",
        "colors": {
            "primary": "#f1c40f",
            "secondary": "#e74c3c",
            "accent": "#3498db",
            "bg": "#1a1a2e"
        },
        "tags": ["物理", "力学", "万有引力", "高中"]
    },

    "动量守恒": {
        "type": "physical",
        "description": "系统不受外力时，总动量保持不变",
        "concept": "展示两个物体碰撞前后的动量变化，验证守恒定律",
        "elements": ["物体A", "物体B", "速度矢量", "动量柱状图", "碰撞动画"],
        "steps": ["展示两个物体", "碰撞前动量", "碰撞过程", "碰撞后动量", "验证守恒"],
        "audience": "high",
        "complexity": "medium",
        "colors": {
            "primary": "#4a90e2",
            "secondary": "#e94560",
            "accent": "#ffd700",
            "bg": "#1a1a2e"
        },
        "tags": ["物理", "力学", "动量", "高中"]
    },

    # ========== 化学类模板 ==========

    "水分子结构": {
        "type": "chemical",
        "description": "水分子H2O的极性分子结构与形成过程",
        "concept": "展示氢原子与氧原子的电子共用，形成极性分子",
        "elements": ["氧原子", "氢原子", "电子", "化学键", "极性指示"],
        "steps": ["展示氧原子", "展示氢原子", "电子转移与共用", "形成共价键", "标注分子极性"],
        "audience": "middle",
        "complexity": "simple",
        "colors": {
            "primary": "#3498db",
            "secondary": "#e74c3c",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["化学", "分子结构", "水", "初中"]
    },

    "化学反应类型": {
        "type": "chemical",
        "description": "化合、分解、置换、复分解四种基本反应类型",
        "concept": "用具体化学反应实例展示四种反应类型的特点",
        "elements": ["反应物", "生成物", "反应条件", "反应类型标签"],
        "steps": ["展示化合反应", "展示分解反应", "展示置换反应", "展示复分解反应", "总结规律"],
        "audience": "middle",
        "complexity": "medium",
        "colors": {
            "primary": "#9b59b6",
            "secondary": "#1abc9c",
            "accent": "#ffd700",
            "bg": "#f5f5f5"
        },
        "tags": ["化学", "反应", "类型", "初中"]
    },

    "原子结构": {
        "type": "chemical",
        "description": "原子由原子核和核外电子构成，核外电子分层排布",
        "concept": "展示原子的核式结构模型与电子排布规律",
        "elements": ["原子核", "质子", "中子", "电子", "电子层"],
        "steps": ["展示原子核", "展示核外电子", "电子分层排布", "展示离子形成", "展示同位素"],
        "audience": "middle",
        "complexity": "medium",
        "colors": {
            "primary": "#e94560",
            "secondary": "#4a90e2",
            "accent": "#ffd700",
            "bg": "#1a1a2e"
        },
        "tags": ["化学", "原子", "结构", "初中"]
    },
}


def get_template(name: str) -> Dict[str, Any]:
    """获取指定名称的模板"""
    return TEMPLATES.get(name, {})


def list_templates() -> List[str]:
    """列出所有可用模板"""
    return list(TEMPLATES.keys())


def search_templates(keyword: str) -> List[str]:
    """搜索模板（按名称或标签）"""
    results = []
    keyword_lower = keyword.lower()

    for name, template in TEMPLATES.items():
        # 匹配名称
        if keyword_lower in name.lower():
            results.append(name)
            continue

        # 匹配标签
        tags = template.get("tags", [])
        if any(keyword_lower in tag.lower() for tag in tags):
            results.append(name)

    return results


def add_template(name: str, template: Dict[str, Any]) -> None:
    """添加新模板"""
    TEMPLATES[name] = template


# 模板分类索引
CATEGORIES = {
    "几何": [
        "勾股定理",
        "圆的面积",
        "三角函数sin/cos图像",
        "指数函数图像",
        "对数函数图像",
        "抛物线二次函数",
        "正多边形面积",
        "圆锥体积公式",
        "球体积公式",
        "相似三角形",
    ],
    "数学": [
        "指数函数图像",
        "对数函数图像",
        "抛物线二次函数",
        "概率骰子实验",
        "排列组合",
    ],
    "机械": ["四冲程发动机"],
    "物理": [
        "牛顿第二定律",
        "四冲程发动机",
        "光的折射",
        "电磁感应",
        "自由落体",
        "简谐振动",
        "波动传播",
        "热传导",
        "万有引力",
        "动量守恒",
    ],
    "化学": [
        "水分子结构",
        "化学反应类型",
        "原子结构",
    ],
    "力学": [
        "牛顿第二定律",
        "自由落体",
        "万有引力",
        "动量守恒",
    ],
    "光学": ["光的折射"],
    "电磁学": ["电磁感应"],
    "热学": ["热传导"],
    "波动": ["简谐振动", "波动传播"],
}


def get_by_category(category: str) -> List[str]:
    """按分类获取模板"""
    return CATEGORIES.get(category, [])
