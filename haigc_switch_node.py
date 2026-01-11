
class HAIGC_SwitchNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "switch_value": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("boolean",)
    FUNCTION = "process_switch"
    CATEGORY = "HAIGC/Utils"

    def process_switch(self, switch_value):
        return (switch_value,)
