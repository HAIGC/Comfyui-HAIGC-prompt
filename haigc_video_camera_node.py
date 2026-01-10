class HAIGC_VideoCameraNode:
    # 1. Zoom & Focus (变焦与焦点)
    zoom_focus_dict = {
        "无": "None",
        "慢速前推": "Slow zoom in",
        "慢速后拉": "Slow zoom out",
        "快速前推": "Fast zoom in",
        "快速后拉": "Fast zoom out",
        "平滑光学推进": "Smooth optical zoom in",
        "快速变焦": "Crash zoom",
        "瞬间变焦": "Snap zoom",
        "希区柯克变焦(眩晕)": "Dolly zoom, vertigo effect",
        "尺度连贯(主体不变)": "Dolly zoom, maintaining subject size",
        "极致微距变焦": "Extreme macro zoom",
        "穿梭宇宙般超级变焦": "Cosmic zoom, hyper-zoom",
        "焦点操控": "Focus control",
        "虚焦淡入": "Rack focus, blur to sharp",
        "焦点转移(前到后)": "Rack focus, foreground to background",
        "焦点转移(后到前)": "Rack focus, background to foreground",
        "浅景深": "Shallow depth of field",
        "深景深": "Deep focus",
        "移轴效果": "Tilt-shift effect"
    }

    # 2. Camera Movement (运镜方式)
    movement_dict = {
        "无": "None",
        "固定镜头": "Static camera",
        "三脚架上摇": "Tripod tilt up",
        "三脚架下摇": "Tripod tilt down",
        "左摇镜头": "Pan left",
        "右摇镜头": "Pan right",
        "甩镜头": "Whip pan",
        "滑轨左移": "Truck left, slider left",
        "滑轨右移": "Truck right, slider right",
        "升起拍摄": "Pedestal up, crane up",
        "降下拍摄": "Pedestal down, crane down",
        "摇臂上升揭示": "Jib up, high angle reveal",
        "摇臂下降落地": "Jib down, ground level landing",
        "环绕运镜(180度)": "180 degree orbit",
        "快速360度环绕": "Fast 360 degree orbit",
        "缓慢电影感弧线": "Slow cinematic arc",
        "手持纪实风格": "Handheld camera, documentary style",
        "摄像机抖动": "Camera shake",
        "第一人称步行": "POV walking shot",
        "第一人称奔跑": "POV running shot"
    }

    # 3. Tracking & Following (跟拍与互动)
    tracking_dict = {
        "无": "None",
        "主体跟拍": "Tracking shot, following subject",
        "后拉跟拍(引领)": "Backward tracking, leading shot",
        "前推跟拍(跟随)": "Forward tracking, following shot",
        "平行侧跟": "Side tracking, parallel tracking",
        "过肩镜头": "Over-the-shoulder shot",
        "遮蔽物揭示": "Reveal shot from behind obstacle",
        "穿越孔洞": "Fly through hole",
        "穿越光圈": "Fly through ring",
        "抛掷物视角": "Projectile view, thrown camera",
        "旋涡吸入": "Vortex shot",
        "滚筒旋转": "Barrel roll"
    }

    # 4. Drone & Aerial (航拍与无人机)
    drone_dict = {
        "无": "None",
        "无人机航拍": "Drone shot, aerial view",
        "BBC纪录片风格": "BBC documentary style drone shot",
        "无人机飞越": "Drone flyover",
        "史诗级大场景揭示": "Epic drone reveal, wide landscape",
        "影院级巨幕环绕": "Cinematic wide drone orbit, IMAX visual",
        "垂直俯拍(上帝视角)": "Top-down view, God's eye view, bird's eye view",
        "FPV极限俯冲": "FPV drone diving shot",
        "低空掠过": "Low altitude flyover",
        "贴地飞行": "Ground skimming shot",
        "极低角度跟拍": "Low angle tracking, ground level"
    }

    # 5. Angles & Lenses (角度与镜头)
    angle_lens_dict = {
        "无": "None",
        "鱼眼镜头": "Fisheye lens",
        "猫眼镜头": "Cat eye lens effect",
        "广角镜头": "Wide angle lens",
        "长焦镜头": "Telephoto lens",
        "低角度": "Low angle",
        "高角度": "High angle",
        "倾斜镜头(荷兰角)": "Dutch angle, tilted frame",
        "极低角度": "Extreme low angle",
        "极高角度": "Extreme high angle"
    }

    # 6. Speed & Time (速度与时间)
    speed_time_dict = {
        "无": "None",
        "正常速度": "Real time speed",
        "慢动作": "Slow motion",
        "超级慢动作": "Super slow motion",
        "快进": "Fast forward",
        "移动延时": "Hyperlapse",
        "超级延时": "Timelapse",
        "子弹时间": "Bullet time, frozen moment",
        "时间倒流": "Reverse motion"
    }

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "变焦与焦点": (list(s.zoom_focus_dict.keys()), {"default": "无"}),
                "运镜方式": (list(s.movement_dict.keys()), {"default": "无"}),
                "跟拍与互动": (list(s.tracking_dict.keys()), {"default": "无"}),
                "航拍与无人机": (list(s.drone_dict.keys()), {"default": "无"}),
                "角度与镜头": (list(s.angle_lens_dict.keys()), {"default": "无"}),
                "速度与时间": (list(s.speed_time_dict.keys()), {"default": "无"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_video_prompt"
    CATEGORY = "HAIGC/Prompt"

    def generate_video_prompt(self, 变焦与焦点, 运镜方式, 跟拍与互动, 航拍与无人机, 角度与镜头, 速度与时间):
        # Helper to lookup English part
        def get_en(val, mapping):
            if val and val != "无":
                return mapping.get(val, None)
            return None

        items = [
            (变焦与焦点, self.zoom_focus_dict),
            (运镜方式, self.movement_dict),
            (跟拍与互动, self.tracking_dict),
            (航拍与无人机, self.drone_dict),
            (角度与镜头, self.angle_lens_dict),
            (速度与时间, self.speed_time_dict)
        ]
        
        prompts = []
        for val, mapping in items:
            en_val = get_en(val, mapping)
            if en_val:
                prompts.append(en_val)
            
        result = ", ".join(prompts)
        return (result,)

# Node mappings
NODE_CLASS_MAPPINGS = {
    "HAIGC_VideoCameraNode": HAIGC_VideoCameraNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HAIGC_VideoCameraNode": "视频运镜提示词"
}
