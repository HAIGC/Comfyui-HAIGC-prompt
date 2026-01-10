class HAIGC_CameraNode:
    # Define dictionaries mapping Chinese display names to English prompts
    shot_sizes_dict = {
        "特写": "close-up",
        "中景": "medium shot",
        "全景": "wide shot"
    }

    angles_dict = {
        "低角度": "low-angle shot",
        "平角度": "eye-level shot",
        "仰角": "elevated shot",
        "高角度": "high-angle shot"
    }

    viewpoints_dict = {
        "正视角": "front view",
        "右前四分之三视图": "front-right quarter view",
        "右侧视角": "right side view",
        "右后四分之三视图": "back-right quarter view",
        "后视角": "back view",
        "左后四分之三视图": "back-left quarter view",
        "左侧视角": "left side view",
        "左前四分之三视图": "front-left quarter view"
    }

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "景别": (list(s.shot_sizes_dict.keys()), {"default": "特写"}),
                "角度": (list(s.angles_dict.keys()), {"default": "低角度"}),
                "视角": (list(s.viewpoints_dict.keys()), {"default": "正视角"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_camera_prompt"
    CATEGORY = "HAIGC/Prompt"

    def generate_camera_prompt(self, 景别, 角度, 视角):
        # Helper to lookup English part
        def get_en(val, mapping):
            if val:
                return mapping.get(val, None)
            return None

        size_en = get_en(景别, self.shot_sizes_dict)
        angle_en = get_en(角度, self.angles_dict)
        view_en = get_en(视角, self.viewpoints_dict)

        # Logic to combine them: 
        # Order: Viewpoint + Angle + Shot Size
        
        parts = []
        if view_en:
            parts.append(view_en)
        if angle_en:
            parts.append(angle_en)
        if size_en:
            parts.append(size_en)
            
        result = " ".join(parts)
        return (result,)

# Node mappings
NODE_CLASS_MAPPINGS = {
    "HAIGC_CameraNode": HAIGC_CameraNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HAIGC_CameraNode": "2511镜头角度"
}
