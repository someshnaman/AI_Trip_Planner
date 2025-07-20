import yaml
import os
from pathlib import Path

# Always points to the folder containing the currently running script
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config", "config.yaml")  # ".." moves up to project root


def load_config(config_path: str = "config/config.yaml") -> dict:
    config_path = Path(config_path)
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        print(config)
        return config
