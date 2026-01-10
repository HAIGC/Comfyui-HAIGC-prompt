class HAIGC_TextBuilderNode:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "switch_1": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
                "switch_2": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
                "switch_3": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
                "switch_4": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
                "switch_5": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
                "前缀": ("STRING", {"multiline": False, "default": ""}),
                "后缀": ("STRING", {"multiline": False, "default": ""}),
                "忽略空行": ("BOOLEAN", {"default": True}),
            },
            "optional": {
                "text_1": ("STRING", {"forceInput": True}),
                "text_2": ("STRING", {"forceInput": True}),
                "text_3": ("STRING", {"forceInput": True}),
                "text_4": ("STRING", {"forceInput": True}),
                "text_5": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_list",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "process_text"
    CATEGORY = "HAIGC/Text"

    def process_text(self, switch_1, switch_2, switch_3, switch_4, switch_5, 前缀, 后缀, 忽略空行, text_1=None, text_2=None, text_3=None, text_4=None, text_5=None):
        # Collect all inputs and their switches
        # switch_X is the boolean switch
        # text_X is the string content
        input_data = [
            (text_1, switch_1),
            (text_2, switch_2),
            (text_3, switch_3),
            (text_4, switch_4),
            (text_5, switch_5)
        ]
        
        # Filter logic
        valid_texts = []
        for t, enabled in input_data:
            if not enabled:
                continue
            if t is None:
                continue
            
            # Handle list input (if an input is already a list, we might want to flatten or extend? 
            # Or just treat it as a string? 
            # ComfyUI "STRING" input can sometimes be a list if connected to a list output.
            # Let's handle both single string and list of strings.)
            if isinstance(t, list):
                # If it's a list, we process each item
                for item in t:
                    if 忽略空行:
                        if item and str(item).strip():
                            valid_texts.append(str(item))
                    else:
                        valid_texts.append(str(item))
            else:
                # Single string
                t_str = str(t)
                if 忽略空行:
                    if t_str and t_str.strip():
                        valid_texts.append(t_str)
                else:
                    valid_texts.append(t_str)

        # Apply prefix/suffix to each item for the list output
        final_list = [f"{前缀}{t}{后缀}" for t in valid_texts]
        
        return (final_list,)

# Node mappings
NODE_CLASS_MAPPINGS = {
    "HAIGC_TextBuilderNode": HAIGC_TextBuilderNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HAIGC_TextBuilderNode": "多文本连接"
}
