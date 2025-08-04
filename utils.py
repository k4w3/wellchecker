import datetime
import os
from pathlib import Path


def get_log_file():
    return Path(os.getenv("APPDATA")) / "WellChecker" / "last_run_datetime.txt"


def already_executed_recently(hours: int = 10) -> bool:
    """
    指定した時間以内にアプリが実行されているかを確認する。

    Args:
        hours (int): 最近実行済みとみなす時間（単位：時間）

    Returns:
        bool: 指定時間内に実行されていれば True、そうでなければ False
    """
    log_file = get_log_file()
    if log_file.exists():
        try:
            last_run_str = log_file.read_text(encoding="utf-8").strip()
            last_run_dt = datetime.datetime.strptime(last_run_str, "%Y-%m-%d %H:%M:%S")
            elapsed = datetime.datetime.now() - last_run_dt
            return elapsed.total_seconds() < hours * 3600
        except Exception:
            # 読み込みエラーや書式不正の場合は再実行を許可
            return False
    return False


def write_last_run_datetime():
    """
    現在の日時をログファイルに書き込む。
    """
    log_file = get_log_file()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_file.write_text(now_str, encoding="utf-8")
