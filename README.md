# Llama-v2-Chat-App

This project leverages Llama v2 Chat models for a Chatbot Application

## Description

This project was inspired on: [The FASTEST way to build CHAT UI for LLAMA-v2](https://youtu.be/PE0DQlQItro?list=PL98nY_tJQXZlXLELjCMA8cciKLRE2eLME) by [Abhishek Thakur](https://gist.github.com/abhishekkrthakur)

This Chat Application include the following features:

- Llama.cpp.
- Memory.
- Inference API for Text Generation.

All in a containerized maner.

## Results

Chatbot:
![image](https://github.com/kevinknights29/Llama-v2-Chat-App/assets/74464814/65a006ce-3684-4c80-a0cd-83c22a71298c)

API:
![image](https://github.com/kevinknights29/Llama-v2-Chat-App/assets/74464814/79f45546-5b02-4db5-ad60-07cccd7496b2)

## Usage

### Build APP and API Images

```bash
docker compose build
```

### Get everything up and running

```bash
docker compose down && docker compose up -d
```

### Have fun

Visit: `http://localhost:7861/` to access the Gradio Chatbot UI.

To learn more about the inference API, please visit: `http://localhost:5001/swagger`

## Contributing

### Installing pre-commit

Pre-commit is already part of this project dependencies.
If you would like to installed it as standalone run:

```console
pip install pre-commit
```

To activate pre-commit run the following commands:

- Install Git hooks:

```console
pre-commit install
```

- Update current hooks:

```console
pre-commit autoupdate
```

To test your installation of pre-commit run:

```console
pre-commit run --all-files
```
