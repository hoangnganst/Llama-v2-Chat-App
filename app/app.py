from __future__ import annotations

import os

import gradio as gr
import requests


TEXT_GENERATION_API = os.environ.get("TEXT_GENERATION_API")
METAPROMPT = (
    "<s>[INST] <<SYS>>"
    "You are a helpful bot. Answer the user's questions. Respect the user. "
    "Do not provide false information. If you do not know the answer, say I don't know."
    "<</SYS>>"
)


def _build_prompt(msg, hist):
    if len(hist) > 5:
        hist = hist[-5:]

    if len(hist) == 0:
        return METAPROMPT + f"{msg} [/INST]"

    prompt = METAPROMPT + f"{hist[0][0]} [/INST] {hist[0][1]} </s>"
    for usr_msg, model_msg in hist[1:]:
        prompt += f"<s>[INST] {usr_msg} [/INST] {model_msg} </s>"
    prompt += f"<s>[INST] {msg} [/INST]"
    return prompt


def _api_call(prompt):
    data = {
        "prompt": prompt,
    }
    response = requests.post(TEXT_GENERATION_API, json=data, stream=True, timeout=60)

    for line in response.iter_lines():
        if line:
            yield line.decode("utf-8")


def predict(msg, hist):
    prompt = _build_prompt(msg, hist)
    _api_call(prompt)


if __name__ == "__main__":
    gr.ChatInterface(predict, title="Chat with Llama-v2 7b").queue().launch(
        server_name="0.0.0.0",
        server_port=7860,
    )
