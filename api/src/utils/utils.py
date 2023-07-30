from __future__ import annotations

import os

import yaml
from yaml.loader import SafeLoader

# Directories
MODULE_FOLDER = os.path.dirname(os.path.abspath(__file__))
API_FOLDER = os.path.dirname(os.path.dirname(MODULE_FOLDER))

# Files
CONFIG_FILE = os.path.join(API_FOLDER, "config.yaml")

conf: dict = {}


def config() -> dict:
    """
    Loads the config.yaml file and returns a dict
    stored in config
    Returns:
        dict: configuration dictionary
    """

    global conf
    if not conf:
        with open(CONFIG_FILE, encoding="utf-8") as cfg:
            conf = yaml.load(cfg, Loader=SafeLoader)
    return conf
