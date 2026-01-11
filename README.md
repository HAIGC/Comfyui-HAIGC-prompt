# ComfyUI HAIGC Prompt / HAIGC 提示词插件

<details>
<summary><strong>English</strong></summary>

## Overview

A ComfyUI custom node suite for prompt engineering and workflow batching. Most nodes use a Chinese UI while producing English prompt output where applicable.

## Nodes

### 1. HAIGC Prompt
**Node Name**: `HAIGC_PromptNode`
- Core prompt builder with structured categories (Quality / Style / Lighting / Atmosphere / Camera / Composition / Color).

### 2. Video Camera Prompt
**Node Name**: `HAIGC_VideoCameraNode`
- Cinematography / camera movement prompt selector for AI video generation.

### 3. Style Prompt
**Node Name**: `HAIGC_StyleNode`
- One-click style selector.

### 4. Camera Settings
**Node Name**: `HAIGC_CameraNode`
- Camera gear simulation prompts (body / focal length / film / filters).

### 5. Multi-Text Builder
**Node Name**: `HAIGC_TextBuilderNode`
- Builds a prompt list from multiple inputs and supports image-aligned expansion.
- Inputs:
  - `text_1 ~ text_5`: text inputs (ports), each controlled by `switch_1 ~ switch_5`
  - `list_input`: chain input for a text list (port)
  - `image_input`: image list input (port)
  - `main_switch`: master enable/disable for all text inputs
  - `前缀` / `后缀` / `忽略空行`
- Outputs:
  - `text_list`: list of prompts
  - `image_list`: list of images aligned to `text_list`
- Expansion rule (image-by-image):
  - For each image, all enabled prompts will run once, then move to the next image.
  - Example: 5 Images × 5 Prompts = 25 Executions.

### 6. Logic Switch
**Node Name**: `HAIGC_SwitchNode`
- A boolean relay node to control multiple nodes' master switches.

### 7. Image Queue
**Node Name**: `HAIGC_ImageQueueNode`
- Distributes up to 5 image inputs into dedicated outputs and an optional merged chain output.
- Inputs:
  - `image_1 ~ image_5`: 5 image slots
  - `image_chain`: optional upstream chain
  - `repeat_count`: repeats images inside each output list
  - `switch_chain`: enables/disables only the `image_chain` output
  - `switch_1 ~ switch_5`: only control whether each slot is merged into `image_chain` (does not affect `image_1 ~ image_5` outputs)
- Outputs:
  - `image_chain`: merged list output (controlled by switches)
  - `image_1 ~ image_5`: per-slot outputs (always output if input exists)

## Typical Workflows

### A) Single pipeline: 5 images × 5 prompts = 25 runs
1. Connect images to `HAIGC_ImageQueueNode` `image_1 ~ image_5` and set `repeat_count=1`.
2. Enable `switch_chain` and enable `switch_1 ~ switch_5` (so `image_chain` contains all 5 images).
3. Connect `image_chain` → `HAIGC_TextBuilderNode.image_input`.
4. Connect your 5 prompts to `text_1 ~ text_5`.
5. Downstream pairing:
   - `HAIGC_TextBuilderNode.image_list` → image input of your generation pipeline
   - `HAIGC_TextBuilderNode.text_list` → `CLIP Text Encode`

### B) 5 parallel pipelines: each pipeline processes one image
Connect `image_1` to pipeline #1, `image_2` to pipeline #2, ... This avoids list fan-out multiplication.

## Installation

1. Go to your ComfyUI custom nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repo:
   ```bash
   git clone https://github.com/YourUsername/Comfyui-HAIGC-prompt.git
   ```
3. Restart ComfyUI.

## Contact

- WeChat: `HAIGC1994`
- Author: HAIGC

</details>

一套用于提示词工程与工作流批量化的 ComfyUI 自定义节点套件。节点以中文界面为主，并在需要时输出英文提示词，方便直接用于主流模型与视频生成工具。

---

## 节点说明

### 1. HAIGC 提示词
**节点名称**: `HAIGC_PromptNode`
- 核心提示词构建器，按分类组织（画质 / 风格 / 光照 / 环境气氛 / 镜头 / 构图 / 色调）。

### 2. 视频运镜提示词
**节点名称**: `HAIGC_VideoCameraNode`
- AI 视频运镜/镜头语言提示词选择器。

### 3. 提示词风格
**节点名称**: `HAIGC_StyleNode`
- 一键风格选择器。

### 4. 摄影参数
**节点名称**: `HAIGC_CameraNode`
- 相机机身 / 镜头焦段 / 胶片 / 滤镜等摄影参数提示词。

### 5. 多文本连接
**节点名称**: `HAIGC_TextBuilderNode`
- 将多路文本拼接成提示词列表，并支持按图像展开执行。
- 输入端口：
  - `text_1 ~ text_5`：5路文本输入（端口），由 `switch_1 ~ switch_5` 控制是否启用
  - `list_input`：提示词列表串联输入（端口）
  - `image_input`：图像列表输入（端口）
  - `main_switch`：总开关（控制本节点 text_1~text_5 是否生效）
  - `前缀` / `后缀` / `忽略空行`
- 输出端口：
  - `text_list`：提示词列表
  - `image_list`：与 `text_list` 严格对齐的图像列表
- 图像展开规则（逐张执行）：
  - 先让第1张图按顺序运行全部提示词，再运行第2张图，直到所有图完成。
  - 示例：5张图 × 5组提示词 = 25次执行。

### 6. 逻辑开关
**节点名称**: `HAIGC_SwitchNode`
- 布尔值转接节点，用于一键控制多个节点的总开关。

### 7. 图像队列
**节点名称**: `HAIGC_ImageQueueNode`
- 5路图像分发 + 可选串联合并输出。
- 输入端口：
  - `image_1 ~ image_5`：5路图像输入
  - `image_chain`：上游串联输入（可选）
  - `repeat_count`：每个输出列表内部重复次数
  - `switch_chain`：仅控制 `image_chain` 输出是否输出
  - `switch_1 ~ switch_5`：仅控制该路是否合并进 `image_chain`（不影响 `image_1~image_5` 单路输出）
- 输出端口：
  - `image_chain`：合并后的图像列表输出
  - `image_1 ~ image_5`：每路单独输出（对应输入端口）

---

## 常用工作流

### A) 单通道跑满 25 次（5张图 × 5组提示词）
1. 将 5 张图分别连接到 `HAIGC 图像队列` 的 `image_1 ~ image_5`，并设置 `repeat_count=1`。
2. 打开 `switch_chain`，并打开 `switch_1 ~ switch_5`，让 `image_chain` 合并输出 5 张图。
3. `image_chain` → 连接到 `HAIGC 多文本连接.image_input`。
4. 将 5 组提示词连接到 `text_1 ~ text_5`。
5. 下游配对（关键）：
   - `HAIGC 多文本连接.image_list` → 连接到生成链路的图像输入
   - `HAIGC 多文本连接.text_list` → 连接到 `CLIP Text Encode`

### B) 五路并行（每路处理一张图）
将 `image_1` 接到第1条链路，`image_2` 接到第2条链路……避免把同一个列表输出分叉到多个节点造成倍增。

---

## 安装

1. 进入 ComfyUI 自定义节点目录：
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. 克隆仓库：
   ```bash
   git clone https://github.com/YourUsername/Comfyui-HAIGC-prompt.git
   ```
3. 重启 ComfyUI。

---

## 联系方式

- 微信号：`HAIGC1994`
- 作者：HAIGC
