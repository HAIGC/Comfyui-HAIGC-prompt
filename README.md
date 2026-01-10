# ComfyUI HAIGC Prompt / HAIGC 提示词插件

**[English]**
A comprehensive ComfyUI custom node suite designed for professional AI art and video generation. It simplifies prompt engineering by providing structured categories, bilingual interfaces (Chinese UI / English Output), and specialized tools for cinematography and text management.

**[中文]**
一套专为专业 AI 绘画和视频生成设计的 ComfyUI 自定义节点套件。它通过结构化的分类、中英双语界面（中文界面/英文输出）以及专业的摄影运镜和文本管理工具，极大地简化了提示词工程。

---

## ✨ Features / 功能特性

### 1. HAIGC Prompt / HAIGC 提示词
**Node Name**: `HAIGC_PromptNode`
- **Description**: The core prompt builder.
- **Categories**: Quality, Style, Lighting, Atmosphere, Camera, Composition, Color.
- **描述**: 核心提示词构建器。
- **分类**: 画质、风格、光照、环境气氛、镜头、构图、色调。

### 2. Video Camera Prompt / 视频运镜提示词
**Node Name**: `HAIGC_VideoCameraNode`
- **Description**: Specialized for AI Video (Sora, Runway, Pika, Kling).
- **Features**: 
  - Zoom & Focus (Dolly Zoom/Vertigo, Rack Focus)
  - Movement (Pan, Tilt, Truck)
  - Tracking (FPV, Subject Tracking)
  - Time & Speed (Bullet Time, Timelapse)
- **描述**: 专为 AI 视频生成（Sora, Runway, Pika, 可灵）设计。
- **特性**: 
  - 变焦与焦点（希区柯克变焦、焦点转移）
  - 运镜方式（摇摄、平移）
  - 跟拍与互动（FPV、主体跟随）
  - 速度与时间（子弹时间、延时摄影）

### 3. Style Prompt / 提示词风格
**Node Name**: `HAIGC_StyleNode`
- **Description**: One-click style selector.
- **Styles**: Photography, 3D Render, Anime, Oil Painting, Sketch, Ink, etc.
- **描述**: 一键风格选择器。
- **风格**: 摄影、3D渲染、动漫、油画、素描、水墨等。

### 4. Camera Settings / 2511摄影
**Node Name**: `HAIGC_CameraNode`
- **Description**: Simulates professional camera gears.
- **Settings**: Camera Body, Lens Focal Length, Film Type, Filter Effects.
- **描述**: 模拟专业相机设备。
- **设置**: 相机机身、镜头焦段、胶片类型、滤镜效果。

### 5. Multi-Text Builder / 多文本连接
**Node Name**: `HAIGC_TextBuilderNode`
- **Description**: Advanced text concatenation tool.
- **Features**: 
  - 5 Toggleable Inputs: Each text input has a dedicated on/off switch.
  - Prefix & Suffix: Add wrapper text to results.
  - List Output: Generates a list of strings for batch processing.
- **描述**: 高级文本拼接工具。
- **特性**: 
  - 5路可开关输入：每个文本输入都有独立的开启/关闭开关。
  - 前缀与后缀：支持为结果添加前后缀。
  - 列表输出：生成字符串列表用于批量处理。

---

## 📦 Installation / 安装说明

1. **Goto ComfyUI custom_nodes directory / 进入 ComfyUI 自定义节点目录**:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. **Clone the repository / 克隆仓库**:
   ```bash
   git clone https://github.com/YourUsername/Comfyui-HAIGC-prompt.git
   ```

3. **Restart ComfyUI / 重启 ComfyUI**.

---

## 🛠️ Usage / 使用方法

- **Find Nodes**: Double-click on the canvas and search for "HAIGC" or the specific node names (e.g., "视频运镜").
- **查找节点**: 在画布上双击并搜索 "HAIGC" 或具体节点名称（如“视频运镜”）。
- **Connect**: Connect the output to `CLIP Text Encode` or any node accepting String/List inputs.
- **连接**: 将输出连接到 `CLIP Text Encode` 或任何接受字符串/列表输入的节点。

---

## 📞 Contact / 联系方式

- **WeChat / 微信号**: `HAIGC1994`
- **Author / 作者**: HAIGC
- **Feedback**: If you have any suggestions or questions, please feel free to contact via WeChat.
- **反馈**: 如果您有任何建议或问题，欢迎通过微信联系。

---

*Made with ❤️ by HAIGC*
