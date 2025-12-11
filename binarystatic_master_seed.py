class BinarystaticMasterSeed:
    """
    A simple Master Seed node that outputs a static integer.
    Designed to serve as a single source of truth for seed values across a workflow.
    """
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("INT", {
                    "default": 0, 
                    "min": 0, 
                    "max": 0xffffffffffffffff, # Ensures 64-bit support
                    "step": 1,
                    "display": "number" 
                }),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed_int",)
    FUNCTION = "do_work"
    CATEGORY = "BinaryStatic"

    def do_work(self, seed):
        return (seed,)