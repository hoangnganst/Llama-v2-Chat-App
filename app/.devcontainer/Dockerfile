FROM python:3.11.4-slim-bullseye

ENV LANG=C.UTF-8

# Set working directory
WORKDIR /opt/app

# Install packages
RUN apt update && \
    apt install -y --no-install-recommends \
    wget \
    git

# Copy files
COPY install_dependencies.sh .
COPY dev-requirements.txt .

# Install dependencies
RUN bash ./install_dependencies.sh ./dev-requirements.txt
