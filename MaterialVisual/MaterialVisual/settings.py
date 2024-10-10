import os
from pathlib import Path
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from .static_settings import *


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
CONFIG_PATH = os.path.join(BASE_DIR, ".conf", "config.yaml")


def parse_config():
    with open(CONFIG_PATH, "r") as f:
        return load(f, Loader=Loader)


# parse the config.yaml
CONFIG = parse_config()
if CONFIG:
    for k, v in CONFIG.items():
        globals()[k] = v
