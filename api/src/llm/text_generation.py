from __future__ import annotations

from pathlib import Path

from llama_cpp import Llama
from src.utils import utils

LLM = None


def _find_model(model_dir=utils.config()["model"]["dir"], pattern="*.bin"):
    print({model_dir})
    model_path = Path(model_dir)
    print(str(model_path.glob(pattern)))

    # model_file_path = list(model_path.glob(pattern))[0]

    return str()


def _get_generation_params(params=utils.config()["model"]):
    generation_params = {
        "max_tokens": params["max_tokens"],
        "stop": params["stop"],
        "echo": params["echo"],
    }
    return generation_params


def _format_prompt(prompt):
    # remove trailing spaces
    prompt = prompt.strip()
    # remove trailing question mark
    prompt = prompt[:-1] if prompt[-1] == "?" else prompt
    return f"Q:{prompt}? A:"


def text_generation(prompt):
    LMM = None
    LLM = Llama(
        model_path="models/llama-2-7b.Q8_0.gguf",
        n_gqa=8,
        n_threads=2)
    print("LLLLLL" + LLM)

    if LLM is None:
        LLM = Llama(
        model_path="models/llama-2-7b.Q8_0.gguf",
        n_gqa=8,
        n_threads=2)

    return LLM(_format_prompt(prompt), **_get_generation_params())


def text_generation_stream(prompt):
    global LLM
    print("LLM")
    print(LLM)

    if LLM is None:
        LLM = Llama(
        model_path="models/llama-2-7b.Q8_0.gguf",
        n_gqa=8,
        n_threads=2)

    return LLM(_format_prompt(prompt), stream=True, **_get_generation_params())
