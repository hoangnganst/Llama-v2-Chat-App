FROM python:3.11.4-slim-bullseye

ENV LANG=C.UTF-8

# Set llama.cpp environment variables
ENV CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS"
ENV FORCE_CMAKE=1

# Set working directory
WORKDIR /opt/api

# Install packages
RUN apt update && \
    apt install -y --no-install-recommends \
    wget \
    build-essential \
    python3-launchpadlib \
    python3-dev \
    gcc

# Download models
RUN mkdir -p models && \
    cd models && \
    wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_0.bin

# Copy and install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy files
COPY . .

# Expose port
EXPOSE 5000

# Run API
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
