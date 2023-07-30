FROM python:3.11.4-slim-bullseye

ENV LANG=C.UTF-8

# Set working directory
WORKDIR /opt/app

# Install packages
RUN apt update && \
    apt install -y --no-install-recommends \
    build-essential \
    python3-launchpadlib \
    python3-dev \
    gcc

# Copy and install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy files
COPY . .

# Expose port
EXPOSE 7860

# Run APP
ENTRYPOINT python3 app.py
