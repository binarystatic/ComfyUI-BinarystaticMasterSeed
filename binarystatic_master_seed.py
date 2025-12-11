class BinarystaticMasterSeed:
    """
    A Master Seed node that outputs a static integer and a formatted filename string.
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
                    "max": 0xffffffffffffffff,
                    "step": 1,
                    "display": "number" 
                }),
                "filename_prefix": ("STRING", {
                    "default": "ComfyUI",
                    "multiline": False
                }),
            },
        }

    RETURN_TYPES = ("INT", "STRING",)
    RETURN_NAMES = ("seed_int", "filename_string",)
    FUNCTION = "do_work"
    CATEGORY = "Binarystatic"

    def do_work(self, seed, filename_prefix):
        # Concatenate prefix and seed with an underscore for clean filenames
        # Example Output: "MyProject_850815272867312"
        filename_string = f"{filename_prefix}_{seed}"
        
        return (seed, filename_string,)