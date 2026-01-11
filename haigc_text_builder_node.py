class HAIGC_TextBuilderNode:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "main_switch": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
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
                "image_input": ("IMAGE",),
                "list_input": ("STRING", {"forceInput": True}),
                "text_1": ("STRING", {"forceInput": True}),
                "text_2": ("STRING", {"forceInput": True}),
                "text_3": ("STRING", {"forceInput": True}),
                "text_4": ("STRING", {"forceInput": True}),
                "text_5": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING", "IMAGE")
    RETURN_NAMES = ("text_list", "image_list")
    OUTPUT_IS_LIST = (True, True)
    INPUT_IS_LIST = True
    FUNCTION = "process_text"
    CATEGORY = "HAIGC/Text"

    def process_text(self, main_switch, switch_1, switch_2, switch_3, switch_4, switch_5, 前缀, 后缀, 忽略空行, text_1=None, text_2=None, text_3=None, text_4=None, text_5=None, list_input=None, image_input=None):
        # Helper to extract value from list (since INPUT_IS_LIST=True wraps everything)
        def get_scalar(val, default=None):
            if val is None:
                return default
            if isinstance(val, list):
                return val[0] if len(val) > 0 else default
            return val

        # Helper to ensure we work with a list of strings
        def get_list(val):
            if val is None:
                return []
            if isinstance(val, list):
                return val
            return [str(val)]

        # Helper to normalize image input to list of tensors [1, H, W, C]
        def normalize_images(val):
            if val is None:
                return []
            
            normalized = []
            if isinstance(val, list):
                for item in val:
                    if item is None:
                        continue
                    if hasattr(item, "shape"):
                        if len(item.shape) == 4:
                            B, H, W, C = item.shape
                            for i in range(B):
                                normalized.append(item[i:i+1, ...])
                        elif len(item.shape) == 3:
                            normalized.append(item.unsqueeze(0))
            elif hasattr(val, "shape"):
                 if len(val.shape) == 4:
                    B, H, W, C = val.shape
                    for i in range(B):
                        normalized.append(val[i:i+1, ...])
                 elif len(val.shape) == 3:
                    normalized.append(val.unsqueeze(0))
            return normalized

        # Extract settings (take first item if batched/listed)
        s_main_switch = get_scalar(main_switch, True)
        s_switch_1 = get_scalar(switch_1, True)
        s_switch_2 = get_scalar(switch_2, True)
        s_switch_3 = get_scalar(switch_3, True)
        s_switch_4 = get_scalar(switch_4, True)
        s_switch_5 = get_scalar(switch_5, True)
        
        s_prefix = get_scalar(前缀, "")
        s_suffix = get_scalar(后缀, "")
        s_ignore_empty = get_scalar(忽略空行, True)
        
        # Normalize images
        images = normalize_images(image_input)
        if len(images) > 0:
            collapsed = []
            for img in images:
                if img is None:
                    continue
                if len(collapsed) == 0:
                    collapsed.append(img)
                    continue
                last = collapsed[-1]
                try:
                    if hasattr(img, "equal") and hasattr(last, "equal") and img.shape == last.shape and img.equal(last):
                        continue
                except Exception:
                    pass
                collapsed.append(img)
            images = collapsed
        num_images = len(images)

        # Collect text inputs
        text_items = []

        # 1. Handle chained list input (pass through as-is, no prefix/suffix applied here)
        if list_input is not None:
            text_items.extend(get_list(list_input))

        # 2. Process current node inputs (ONLY if main_switch is True)
        if s_main_switch:
            input_data = [
                (text_1, s_switch_1),
                (text_2, s_switch_2),
                (text_3, s_switch_3),
                (text_4, s_switch_4),
                (text_5, s_switch_5)
            ]
            
            current_node_texts = []
            for t_input, enabled in input_data:
                if not enabled:
                    continue
                if t_input is None:
                    continue
                
                items = get_list(t_input)
                for item in items:
                    item_str = str(item)
                    if s_ignore_empty:
                        if item_str and item_str.strip():
                            current_node_texts.append(item_str)
                    else:
                        current_node_texts.append(item_str)

            # 3. Apply prefix/suffix ONLY to the NEW items from THIS node
            processed_current_texts = [f"{s_prefix}{t}{s_suffix}" for t in current_node_texts]
            
            # Combine
            text_items.extend(processed_current_texts)
        
        # If no images, return text list as is (legacy behavior)
        if num_images == 0:
            return (text_items, [])

        final_text_list = []
        final_image_list = []

        if len(text_items) > 0:
            for img in images:
                for txt in text_items:
                    final_image_list.append(img)
                    final_text_list.append(txt)
        else:
            for img in images:
                final_image_list.append(img)
                final_text_list.append("")

        return (final_text_list, final_image_list)

# Node mappings
NODE_CLASS_MAPPINGS = {
    "HAIGC_TextBuilderNode": HAIGC_TextBuilderNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HAIGC_TextBuilderNode": "多文本连接"
}
