import configparser
import os
from pathlib import Path

# CONFIG_PATH = Path(os.getenv("APPDATA")) / "WellChecker" / "config.ini"
# CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

def get_config(config_path: Path) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    if config_path.exists():
        config.read(config_path, encoding='utf-8')
    return config


def load_config(config_path: Path) -> dict:
    config = configparser.ConfigParser()
    config.read(config_path, encoding="utf-8")
    result = {
        "employee_id": config.get("USER", "employee_id", fallback=""),
        "name": config.get("USER", "name", fallback=""),
        "manager_name": config.get("MANAGER", "name", fallback=""),
        "manager_email": config.get("MANAGER", "email", fallback=""),
        "max_days": config.getint("LOG", "max_days", fallback=90),
        "max_files": config.getint("LOG", "max_files", fallback=100),
    }
    return result

def save_config(config_path: Path, employee_id, name, manager_name, manager_email):
    config = configparser.ConfigParser()
    config["USER"] = {
        "employee_id": employee_id,
        "name": name
    }
    config["MANAGER"] = {
        "name": manager_name,
        "email": manager_email
    }
    config["LOG"] = {
        "max_days": "90",
        "max_files": "100"
    }
    with open(config_path, "w", encoding='utf-8') as configfile:
        config.write(configfile)

def config_exists(config_path: Path) -> bool:
    return config_path.exists()
