# Demo 录制指南

本文档指导如何录制 Vispawn 的演示视频。

## 录制工具推荐

### macOS
- **QuickTime Player** (自带)
- **CleanShot X** (更专业)

### Windows
- **OBS Studio** (免费开源)
- **Bandicam**

### 跨平台
- **Screen Studio** (https://screenstudio.com)
- **Loom** (在线)

## 录制要点

### 1. 提前准备

- [ ] 启动 Vispawn 服务：`python main.py`
- [ ] 打开浏览器到 http://localhost:8000
- [ ] 准备好要演示的原理名称

### 2. 录制内容建议

#### Demo 1: 四冲程发动机（机械类）

1. 输入"四冲程发动机"
2. 等待生成完成（展示加载状态）
3. 播放动画
4. 切换到代码视图
5. 暂停/播放演示交互

#### Demo 2: 勾股定理（几何类）

1. 输入"勾股定理"
2. 展示生成结果
3. 旋转视角
4. 展示控制按钮

#### Demo 3: AI 生成能力展示

1. 输入一个冷门原理（如"齿轮传动"）
2. 展示AI生成过程
3. 展示评估反馈

### 3. 录制设置

推荐设置：
- 分辨率: 1920x1080
- 帧率: 30fps
- 格式: MP4

### 4. 后期处理

- 裁剪多余部分
- 添加字幕（可选）
- 添加背景音乐（可选）
- 导出为 GIF（用于 README）

## 快速截图技巧

### macOS
```bash
# 截取全屏
Cmd + Shift + 3

# 截取选区
Cmd + Shift + 4

# 截取窗口
Cmd + Shift + 4 + 空格
```

### 推荐的截图区域

README 需要的截图：
- 800x450 像素
- 深色背景效果最好

## 已有 Demo

当前已有的示例：

| 示例 | 位置 |
|-----|------|
| 四冲程发动机 | `examples/engine/index.html` |
| 勾股定理 | `examples/pythagorean/index.html` |

## 视频发布平台

- YouTube
- B站
- 小红书

建议标题格式：
- "我用 AI 自动生成了一个 3D 发动机原理演示"
- "输入一个定理，自动生成可交互的 3D 可视化"
