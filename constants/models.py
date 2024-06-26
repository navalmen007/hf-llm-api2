MODEL_MAP = {
    "mixtral-8x7b": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # [Recommended]
    "dolphin-mixtral-8x7b": "cognitivecomputations/dolphin-2.5-mixtral-8x7b",
    #"nous-mixtral-8x7b": "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
    "mistral-7b": "mistralai/Mistral-7B-Instruct-v0.2",
    "CodeQwen1.5": "Qwen/CodeQwen1.5-7B-Chat",
    "dolphin-mistral-7b": "MaziyarPanahi/dolphin-2.0-mistral-7b-Mistral-7B-Instruct-v0.1",
    "openchat-3.5": "openchat/openchat-3.5-0106",
    "gemma-7b": "google/gemma-7b-it",
    "default": "mistralai/Mixtral-8x7B-Instruct-v0.1",
}


STOP_SEQUENCES_MAP = {
    "mixtral-8x7b": "</s>",
    "dolphin-mixtral-8x7b": "<|im_end|>",
    #"nous-mixtral-8x7b": "<|im_end|>",
    "mistral-7b": "</s>",
    "CodeQwen1.5": "<|im_end|>", 
    "dolphin-mistral-7b": "</s>",
    "openchat-3.5": "<|end_of_turn|>",
    "gemma-7b": "<eos>",
}

TOKEN_LIMIT_MAP = {
    "mixtral-8x7b": 32768,
    "dolphin-mixtral-8x7b": 32768,
    #"nous-mixtral-8x7b": 32768,
    "mistral-7b": 32768,
    "CodeQwen1.5": 32768,
    "dolphin-mistral-7b": 32768,
    "openchat-3.5": 8192,
    "gemma-7b": 8192,
}

TOKEN_RESERVED = 20


AVAILABLE_MODELS = [
    "mixtral-8x7b",
    "dolphin-mixtral-8x7b",
    #"nous-mixtral-8x7b",
    "mistral-7b",
    "CodeQwen1.5",
    "dolphin-mistral-7b",
    "openchat-3.5",
    "gemma-7b",
]

# https://platform.openai.com/docs/api-reference/models/list
AVAILABLE_MODELS_DICTS = [
    {
        "id": "mixtral-8x7b",
        "description": "[mistralai/Mixtral-8x7B-Instruct-v0.1]: https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1",
        "object": "model",
        "created": 1700000000,
        "owned_by": "mistralai",
    },
    {
        "id": "dolphin-mixtral-8x7b",
        "description": "[cognitivecomputations/dolphin-2.5-mixtral-8x7b]: https://huggingface.co/cognitivecomputations/dolphin-2.5-mixtral-8x7b",
        "object": "model",
        "created": 1700000000,
        "owned_by": "cognitivecomputations",
    },
    #{
    #    "id": "nous-mixtral-8x7b",
    #    "description": "[NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO]: https://huggingface.co/NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
    #    "object": "model",
    #    "created": 1700000000,
    #    "owned_by": "NousResearch",
    #},
    {
        "id": "mistral-7b",
        "description": "[mistralai/Mistral-7B-Instruct-v0.2]: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2",
        "object": "model",
        "created": 1700000000,
        "owned_by": "mistralai",
    },
    {
        "id": "CodeQwen1.5",
        "description": "[Qwen/CodeQwen1.5-7B-Chat]: https://huggingface.co/Qwen/CodeQwen1.5-7B-Chat",
        "object": "model",
        "created": 1700000000,
        "owned_by": "mistralai",
    },
    {
        "id": "dolphin-mistral-7b",
        "description": "[MaziyarPanahi/dolphin-2.0-mistral-7b-Mistral-7B-Instruct-v0.1]: https://huggingface.co/MaziyarPanahi/dolphin-2.0-mistral-7b-Mistral-7B-Instruct-v0.1",
        "object": "model",
        "created": 1700000000,
        "owned_by": "mistralai",
    },
    {
        "id": "openchat-3.5",
        "description": "[openchat/openchat-3.5-0106]: https://huggingface.co/openchat/openchat-3.5-0106",
        "object": "model",
        "created": 1700000000,
        "owned_by": "openchat",
    },
    {
        "id": "gemma-7b",
        "description": "[google/gemma-7b-it]: https://huggingface.co/google/gemma-7b-it",
        "object": "model",
        "created": 1700000000,
        "owned_by": "Google",
    },
]
