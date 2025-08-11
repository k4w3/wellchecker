import configparser
from pathlib import Path


def get_config(config_path: Path) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    if config_path.exists():
        config.read(config_path, encoding="utf-8")
    return config


def load_config(config_path: Path) -> dict:
    config = configparser.ConfigParser()
    config.read(config_path, encoding="utf-8")
    return {
        "employee_id": config.get("USER", "employee_id", fallback=""),
        "user_last_name": config.get("USER", "last_name", fallback=""),
        "user_first_name": config.get("USER", "first_name", fallback=""),
        "manager_last_name": config.get("MANAGER", "last_name", fallback=""),
        "manager_first_name": config.get("MANAGER", "first_name", fallback=""),
        "manager_email": config.get("MANAGER", "manager_email", fallback=""),
        "cc_email": config.get("MANAGER", "cc", fallback=""),
        "max_days": config.getint("LOG", "max_days", fallback=90),
        "max_files": config.getint("LOG", "max_files", fallback=100),
    }


def save_config(config_path: Path, employee_id, user_last_name, user_first_name, manager_last_name, manager_first_name, manager_email, cc_email=""):
    config = configparser.ConfigParser()
    config["USER"] = {
        "employee_id": employee_id,
        "last_name": user_last_name,
        "first_name": user_first_name,
    }
    config["MANAGER"] = {"last_name": manager_last_name, "first_name": manager_first_name, "manager_email": manager_email, "cc": cc_email}
    config["LOG"] = {"max_days": "90", "max_files": "100"}
    with open(config_path, "w", encoding="utf-8") as configfile:
        config.write(configfile)


def config_exists(config_path: Path) -> bool:
    return config_path.exists()
