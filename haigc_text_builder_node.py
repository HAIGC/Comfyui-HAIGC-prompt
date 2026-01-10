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
                "list_input": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_list",)
    OUTPUT_IS_LIST = (True,)
    INPUT_IS_LIST = True
    FUNCTION = "process_text"
    CATEGORY = "HAIGC/Text"

    def process_text(self, switch_1, switch_2, switch_3, switch_4, switch_5, 前缀, 后缀, 忽略空行, text_1=None, text_2=None, text_3=None, text_4=None, text_5=None, list_input=None):
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

        # Extract settings (take first item if batched/listed)
        s_switch_1 = get_scalar(switch_1, True)
        s_switch_2 = get_scalar(switch_2, True)
        s_switch_3 = get_scalar(switch_3, True)
        s_switch_4 = get_scalar(switch_4, True)
        s_switch_5 = get_scalar(switch_5, True)
        
        s_prefix = get_scalar(前缀, "")
        s_suffix = get_scalar(后缀, "")
        s_ignore_empty = get_scalar(忽略空行, True)

        # Collect inputs
        final_list = []

        # 1. Handle chained list input (pass through as-is, no prefix/suffix applied here)
        # Assuming upstream list is already processed
        if list_input is not None:
            # list_input is a list of all inputs connected. 
            # If multiple inputs were connected to list_input (not possible for single port usually, unless batched)
            # In INPUT_IS_LIST=True, list_input is the list of values.
            final_list.extend(get_list(list_input))

        # 2. Process current node inputs
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
            
            # t_input is a list because INPUT_IS_LIST=True
            # It contains the values from the connected node.
            # If connected node outputs a list, t_input is that list (or flattened? ComfyUI passes the return value).
            # If connected node outputs a single string, t_input is [string].
            
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
        final_list.extend(processed_current_texts)
        
        return (final_list,)

# Node mappings
NODE_CLASS_MAPPINGS = {
    "HAIGC_TextBuilderNode": HAIGC_TextBuilderNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HAIGC_TextBuilderNode": "多文本连接"
}
