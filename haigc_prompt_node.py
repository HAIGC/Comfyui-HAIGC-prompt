import random

class HAIGC_PromptNode:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        # Define prompt categories and options as dictionaries: { "Chinese Label": "English Prompt" }
        
        s.camera_dict = {
            "无": "None",
            "拉近": "Zoom In",
            "拉远": "Zoom Out",
            "左移": "Pan Left",
            "右移": "Pan Right",
            "上仰": "Tilt Up",
            "下俯": "Tilt Down",
            "跟随": "Tracking Shot",
            "推拉变焦": "Dolly Zoom",
            "鱼眼": "Fish Eye",
            "广角": "Wide Angle",
            "长焦": "Telephoto",
            "微距": "Macro",
            "无人机视角": "Drone View",
            "鸟瞰图": "Bird's Eye View",
            "仰视/虫视": "Worm's Eye View",
            "等轴测": "Isometric",
            "第一人称": "POV",
            "过肩镜头": "Over-the-Shoulder"
        }

        s.styles_dict = {
            "无": "None",
            "照片级真实": "Photorealistic",
            "超写实": "Hyperrealistic",
            "动漫": "Anime",
            "漫画": "Manga",
            "油画": "Oil Painting",
            "水彩": "Watercolor",
            "素描": "Sketch",
            "赛博朋克": "Cyberpunk",
            "蒸汽朋克": "Steampunk",
            "超现实主义": "Surrealism",
            "极简主义": "Minimalist",
            "哥特式": "Gothic",
            "波普艺术": "Pop Art",
            "浮世绘": "Ukiyo-e",
            "像素艺术": "Pixel Art",
            "3D渲染": "3D Render",
            "遮罩绘画": "Matte Painting",
            "概念艺术": "Concept Art",
            "印象派": "Impressionism",
            "新艺术运动": "Art Nouveau",
            "蒸汽波": "Vaporwave",
            "低多边形": "Low Poly"
        }

        s.font_designs_dict = {
            "无": "None",
            "粗体": "Bold",
            "斜体": "Italic",
            "衬线体": "Serif",
            "无衬线体": "Sans-Serif",
            "手写体": "Handwriting",
            "书法": "Calligraphy",
            "霓虹灯": "Neon Light",
            "涂鸦": "Graffiti",
            "3D字体": "3D Text",
            "金属质感": "Metallic",
            "木质": "Wooden",
            "石质": "Stone",
            "火焰": "Fire",
            "水流": "Water",
            "故障风": "Glitch",
            "花卉装饰": "Floral",
            "复古": "Retro",
            "未来感": "Futuristic"
        }

        s.dof_dict = {
            "无": "None",
            "浅景深/虚化背景": "Shallow Depth of Field",
            "深景深/全清晰": "Deep Focus",
            "散景": "Bokeh",
            "清晰对焦": "Sharp Focus",
            "柔焦": "Soft Focus",
            "运动模糊": "Motion Blur",
            "移轴": "Tilt-Shift",
            "大光圈": "F/1.8",
            "小光圈": "F/22"
        }

        s.lighting_dict = {
            "无": "None",
            "自然光": "Natural Light",
            "阳光": "Sunlight",
            "月光": "Moonlight",
            "摄影棚光": "Studio Light",
            "电影光": "Cinematic Light",
            "体积光/丁达尔效应": "Volumetric Light",
            "霓虹光": "Neon Light",
            "黄金时刻": "Golden Hour",
            "蓝调时刻": "Blue Hour",
            "轮廓光": "Rim Light",
            "逆光": "Backlight",
            "硬光": "Hard Light",
            "柔光": "Soft Light",
            "伦勃朗光": "Rembrandt Lighting",
            "生物发光": "Bioluminescence"
        }

        s.colors_dict = {
            "无": "None",
            "鲜艳": "Vibrant",
            "柔和/暗淡": "Muted",
            "粉彩": "Pastel",
            "单色": "Monochrome",
            "黑白": "Black and White",
            "复古褐": "Sepia",
            "高对比度": "High Contrast",
            "低对比度": "Low Contrast",
            "暖色调": "Warm Tones",
            "冷色调": "Cool Tones",
            "霓虹色": "Neon Colors",
            "迷幻色": "Psychedelic"
        }
        
        s.quality_dict = {
            "无": "None",
            "杰作": "Masterpiece",
            "最佳质量": "Best Quality",
            "高分辨率": "High Resolution",
            "4K分辨率": "4K",
            "8K分辨率": "8K",
            "高动态范围": "HDR",
            "细节丰富": "Detailed",
            "高度细节": "Highly Detailed"
        }

        return {
            "required": {
                "运镜": (list(s.camera_dict.keys()), {"default": "无"}),
                "风格": (list(s.styles_dict.keys()), {"default": "无"}),
                "字体设计": (list(s.font_designs_dict.keys()), {"default": "无"}),
                "景深": (list(s.dof_dict.keys()), {"default": "无"}),
                "光影": (list(s.lighting_dict.keys()), {"default": "无"}),
                "色调": (list(s.colors_dict.keys()), {"default": "无"}),
                "画质": (list(s.quality_dict.keys()), {"default": "无"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "HAIGC/Prompt"

    def generate_prompt(self, 运镜, 风格, 字体设计, 景深, 光影, 色调, 画质):
        # Access class dictionaries via INPUT_TYPES
        # Note: In ComfyUI, 'self' here is the instance, but INPUT_TYPES is a class method.
        # We can re-access the dictionaries by calling INPUT_TYPES again or defining them at class level.
        # To avoid re-definition, let's just define them at class level or access them cleanly.
        # Actually, it's cleaner to have them as class attributes.
        
        # Let's instantiate the class to access 's' from INPUT_TYPES is not right.
        # Let's just define them in the method or use a helper. 
        # Since I defined them inside INPUT_TYPES as 's.dict', they are attributes of the class 's' which is HAIGC_PromptNode.
        
        cls = HAIGC_PromptNode
        
        # Re-accessing maps (Since they were attached to 's' in INPUT_TYPES, let's check if they persist.
        # Usually 's' is the class itself. So yes.)
        
        prompts = []
        
        def get_english(value, mapping):
            if value and value != "无":
                return mapping.get(value, None)
            return None

        # We need to ensure the dicts are accessible. 
        # INPUT_TYPES is called by ComfyUI to get the structure. 
        # If we attached them to 's' (the class), they should be available.
        # However, to be safe and clean, let's move the dict definitions to the class body or a separate helper.
        # But wait, in the previous code I did `s.camera_movements = [...]`.
        # So `HAIGC_PromptNode.camera_movements` would exist.
        # Let's assume the same logic applies.
        
        # But wait, INPUT_TYPES is a method. If I define s.x inside it, it sets the attribute on the class.
        # So yes, HAIGC_PromptNode.camera_dict should exist after INPUT_TYPES is called.
        # BUT, relying on execution order is risky if ComfyUI caches things.
        # Better to define them at class level properly.
        
        pass 
        # I will rewrite the class to have dictionaries at class level.

# Refined implementation below:

class HAIGC_PromptNode:
    # Dictionaries defined at class level for easy access
    camera_dict = {
        "无": "None",
        "拉近": "Zoom In",
        "拉远": "Zoom Out",
        "左移": "Pan Left",
        "右移": "Pan Right",
        "上仰": "Tilt Up",
        "下俯": "Tilt Down",
        "跟随": "Tracking Shot",
        "推拉变焦": "Dolly Zoom",
        "鱼眼": "Fish Eye",
        "广角": "Wide Angle",
        "长焦": "Telephoto",
        "微距": "Macro",
        "无人机视角": "Drone View",
        "鸟瞰图": "Bird's Eye View",
        "仰视/虫视": "Worm's Eye View",
        "等轴测": "Isometric",
        "第一人称": "POV",
        "过肩镜头": "Over-the-Shoulder"
    }

    styles_dict = {
        "无": "None",
        "照片级真实": "Photorealistic",
        "超写实": "Hyperrealistic",
        "动漫": "Anime",
        "漫画": "Manga",
        "油画": "Oil Painting",
        "水彩": "Watercolor",
        "素描": "Sketch",
        "赛博朋克": "Cyberpunk",
        "蒸汽朋克": "Steampunk",
        "超现实主义": "Surrealism",
        "极简主义": "Minimalist",
        "哥特式": "Gothic",
        "波普艺术": "Pop Art",
        "浮世绘": "Ukiyo-e",
        "像素艺术": "Pixel Art",
        "3D渲染": "3D Render",
        "遮罩绘画": "Matte Painting",
        "概念艺术": "Concept Art",
        "印象派": "Impressionism",
        "新艺术运动": "Art Nouveau",
        "蒸汽波": "Vaporwave",
        "低多边形": "Low Poly"
    }

    font_designs_dict = {
        "无": "None",
        "粗体": "Bold",
        "斜体": "Italic",
        "衬线体": "Serif",
        "无衬线体": "Sans-Serif",
        "手写体": "Handwriting",
        "书法": "Calligraphy",
        "霓虹灯": "Neon Light",
        "涂鸦": "Graffiti",
        "3D字体": "3D Text",
        "金属质感": "Metallic",
        "木质": "Wooden",
        "石质": "Stone",
        "火焰": "Fire",
        "水流": "Water",
        "故障风": "Glitch",
        "花卉装饰": "Floral",
        "复古": "Retro",
        "未来感": "Futuristic"
    }

    dof_dict = {
        "无": "None",
        "浅景深/虚化背景": "Shallow Depth of Field",
        "深景深/全清晰": "Deep Focus",
        "散景": "Bokeh",
        "清晰对焦": "Sharp Focus",
        "柔焦": "Soft Focus",
        "运动模糊": "Motion Blur",
        "移轴": "Tilt-Shift",
        "大光圈": "F/1.8",
        "小光圈": "F/22"
    }

    lighting_dict = {
        "无": "None",
        "自然光": "Natural Light",
        "阳光": "Sunlight",
        "月光": "Moonlight",
        "摄影棚光": "Studio Light",
        "电影光": "Cinematic Light",
        "体积光/丁达尔效应": "Volumetric Light",
        "霓虹光": "Neon Light",
        "黄金时刻": "Golden Hour",
        "蓝调时刻": "Blue Hour",
        "轮廓光": "Rim Light",
        "逆光": "Backlight",
        "硬光": "Hard Light",
        "柔光": "Soft Light",
        "伦勃朗光": "Rembrandt Lighting",
        "生物发光": "Bioluminescence"
    }

    colors_dict = {
        "无": "None",
        "鲜艳": "Vibrant",
        "柔和/暗淡": "Muted",
        "粉彩": "Pastel",
        "单色": "Monochrome",
        "黑白": "Black and White",
        "复古褐": "Sepia",
        "高对比度": "High Contrast",
        "低对比度": "Low Contrast",
        "暖色调": "Warm Tones",
        "冷色调": "Cool Tones",
        "霓虹色": "Neon Colors",
        "迷幻色": "Psychedelic"
    }
    
    quality_dict = {
        "无": "None",
        "杰作": "Masterpiece",
        "最佳质量": "Best Quality",
        "高分辨率": "High Resolution",
        "4K分辨率": "4K",
        "8K分辨率": "8K",
        "高动态范围": "HDR",
        "细节丰富": "Detailed",
        "高度细节": "Highly Detailed"
    }

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "运镜": (list(s.camera_dict.keys()), {"default": "无"}),
                "风格": (list(s.styles_dict.keys()), {"default": "无"}),
                "字体设计": (list(s.font_designs_dict.keys()), {"default": "无"}),
                "景深": (list(s.dof_dict.keys()), {"default": "无"}),
                "光影": (list(s.lighting_dict.keys()), {"default": "无"}),
                "色调": (list(s.colors_dict.keys()), {"default": "无"}),
                "画质": (list(s.quality_dict.keys()), {"default": "无"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "HAIGC/Prompt"

    def generate_prompt(self, 运镜, 风格, 字体设计, 景深, 光影, 色调, 画质):
        prompts = []
        
        # Helper to get English value
        def get_en(val, mapping):
            if val and val != "无":
                return mapping.get(val, None)
            return None

        items = [
            (运镜, self.camera_dict),
            (风格, self.styles_dict),
            (字体设计, self.font_designs_dict),
            (景深, self.dof_dict),
            (光影, self.lighting_dict),
            (色调, self.colors_dict),
            (画质, self.quality_dict)
        ]
        
        for val, mapping in items:
            en_val = get_en(val, mapping)
            if en_val and en_val != "None":
                prompts.append(en_val)
        
        result = ", ".join(prompts)
        return (result,)

# Node mappings
NODE_CLASS_MAPPINGS = {
    "HAIGC_PromptNode": HAIGC_PromptNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HAIGC_PromptNode": "HAIGC 提示词"
}
