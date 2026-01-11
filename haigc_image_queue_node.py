import torch

class HAIGC_ImageQueueNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "repeat_count": ("INT", {"default": 1, "min": 1, "max": 100, "step": 1, "label": "每张图重复次数"}),
                "switch_chain": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
                "switch_1": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
                "switch_2": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
                "switch_3": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
                "switch_4": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
                "switch_5": ("BOOLEAN", {"default": True, "label_on": "开启", "label_off": "关闭"}),
            },
            "optional": {
                "image_chain": ("IMAGE",),
                "image_1": ("IMAGE",),
                "image_2": ("IMAGE",),
                "image_3": ("IMAGE",),
                "image_4": ("IMAGE",),
                "image_5": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE", "IMAGE", "IMAGE", "IMAGE", "IMAGE", "IMAGE")
    RETURN_NAMES = ("image_chain", "image_1", "image_2", "image_3", "image_4", "image_5")
    OUTPUT_IS_LIST = (True, True, True, True, True, True)
    INPUT_IS_LIST = True
    FUNCTION = "process_images"
    CATEGORY = "HAIGC/Image"

    def process_images(self, repeat_count, switch_chain, switch_1, switch_2, switch_3, switch_4, switch_5, image_chain=None, image_1=None, image_2=None, image_3=None, image_4=None, image_5=None):
        # Helper to extract scalar value from list input
        def get_scalar(val, default=1):
            if val is None:
                return default
            if isinstance(val, list):
                return val[0] if len(val) > 0 else default
            return val

        def get_bool(val, default=True):
            v = get_scalar(val, default)
            return bool(v)

        def iter_items(val):
            if val is None:
                return
            if isinstance(val, (list, tuple)):
                for x in val:
                    yield from iter_items(x)
            else:
                yield val

        # Helper to ensure we get a list of tensors [1, H, W, C]
        def normalize_input(val):
            if val is None:
                return []
            
            normalized = []
            for item in iter_items(val):
                if item is None:
                    continue
                
                if not hasattr(item, "shape"):
                    continue

                if len(item.shape) == 4:
                    B, H, W, C = item.shape
                    # Split batch into individual frames for "queue" execution
                    for i in range(B):
                        normalized.append(item[i:i+1, ...])
                elif len(item.shape) == 3:
                     # [H, W, C] -> [1, H, W, C]
                     normalized.append(item.unsqueeze(0))

            return normalized

        s_repeat = int(get_scalar(repeat_count, 1))
        s_switch_chain = get_bool(switch_chain, True)
        s_switch_1 = get_bool(switch_1, True)
        s_switch_2 = get_bool(switch_2, True)
        s_switch_3 = get_bool(switch_3, True)
        s_switch_4 = get_bool(switch_4, True)
        s_switch_5 = get_bool(switch_5, True)

        chain_images = normalize_input(image_chain)

        def select_slot(val, fallback_index):
            items = normalize_input(val)
            if len(items) > 0:
                return items
            if fallback_index < len(chain_images):
                return [chain_images[fallback_index]]
            return []

        def apply_repeat(images):
            if images is None or len(images) == 0:
                return []
            out = []
            for img in images:
                out.extend([img] * s_repeat)
            return out

        out_1 = apply_repeat(select_slot(image_1, 0))
        out_2 = apply_repeat(select_slot(image_2, 1))
        out_3 = apply_repeat(select_slot(image_3, 2))
        out_4 = apply_repeat(select_slot(image_4, 3))
        out_5 = apply_repeat(select_slot(image_5, 4))

        out_chain = []
        if s_switch_chain:
            out_chain.extend(apply_repeat(chain_images))
            if s_switch_1:
                out_chain.extend(out_1)
            if s_switch_2:
                out_chain.extend(out_2)
            if s_switch_3:
                out_chain.extend(out_3)
            if s_switch_4:
                out_chain.extend(out_4)
            if s_switch_5:
                out_chain.extend(out_5)

        return (out_chain, out_1, out_2, out_3, out_4, out_5)
