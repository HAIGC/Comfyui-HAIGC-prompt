from .haigc_prompt_node import HAIGC_PromptNode
from .haigc_camera_node import HAIGC_CameraNode
from .haigc_style_node import HAIGC_StyleNode
from .haigc_video_camera_node import HAIGC_VideoCameraNode
from .haigc_text_builder_node import HAIGC_TextBuilderNode
from .haigc_switch_node import HAIGC_SwitchNode
from .haigc_image_queue_node import HAIGC_ImageQueueNode

NODE_CLASS_MAPPINGS = {
    "HAIGC_PromptNode": HAIGC_PromptNode,
    "HAIGC_CameraNode": HAIGC_CameraNode,
    "HAIGC_StyleNode": HAIGC_StyleNode,
    "HAIGC_VideoCameraNode": HAIGC_VideoCameraNode,
    "HAIGC_TextBuilderNode": HAIGC_TextBuilderNode,
    "HAIGC_SwitchNode": HAIGC_SwitchNode,
    "HAIGC_ImageQueueNode": HAIGC_ImageQueueNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HAIGC_PromptNode": "HAIGC 提示词",
    "HAIGC_CameraNode": "HAIGC 镜头",
    "HAIGC_StyleNode": "提示词风格",
    "HAIGC_VideoCameraNode": "视频运镜提示词",
    "HAIGC_TextBuilderNode": "HAIGC 多文本连接",
    "HAIGC_SwitchNode": "HAIGC 逻辑开关",
    "HAIGC_ImageQueueNode": "HAIGC 图像队列"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
