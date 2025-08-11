# messages.py
from __future__ import annotations

import json
import os
import random
from pathlib import Path
from typing import Any, Dict, List

APP_DIR = Path(os.getenv("APPDATA")) / "WellChecker"
APP_DIR.mkdir(parents=True, exist_ok=True)

HISTORY_FILE = APP_DIR / "healing_history.json"
HISTORY_KEEP = 8  # 直近何件を重複回避対象にするか


# 条件別メッセージ（{name} は任意差し込み）
MESSAGES: Dict[str, List[Dict[str, Any]]] = {
    "◎": [
        {"id": "g1", "text": "今日も絶好調！{name}さん、のびのびいきましょう。"},
        {"id": "g2", "text": "良いスタートです。周りにも良い影響が伝わります。"},
        {"id": "g3", "text": "その調子！コツコツが最強です。"},
    ],
    "○": [
        {"id": "n1", "text": "いつも通りがいちばんの強み。安心して進めましょう。"},
        {"id": "n2", "text": "穏やかに、着実に。必要なときだけ力を入れましょう。"},
        {"id": "n3", "text": "{name}さんのペースでOK。"},
        {"id": "n4", "text": "今日は肩の力を抜いて、自然体でいきましょう。"},
        {"id": "n5", "text": "変わらない一日こそ、安定の証。"},
        {"id": "n6", "text": "焦らず、ゆっくりと。地道な一歩が大事です。"},
        {"id": "n7", "text": "小さなこともコツコツ積み上げていきましょう。"},
        {"id": "n8", "text": "その落ち着きが周りにも良い影響を与えています。"},
        {"id": "n9", "text": "気負わず、流れに身を任せて。"},
        {"id": "n10", "text": "今日は淡々と、自分のペースで。"},
        {"id": "n11", "text": "一歩ずつ、着実に。安定感があなたの強みです。"},
        {"id": "n12", "text": "今日も無理なく、自然体で。"},
        {"id": "n13", "text": "変わらない日常に、感謝の気持ちをひとつ。"},
        {"id": "n14", "text": "静かに淡々とこなす一日も悪くないですね。"},
        {"id": "n15", "text": "調子が安定しているときこそ、周囲に目を向けてみましょう。"},
        {"id": "n16", "text": "穏やかな気持ちでスタートできそうですね。"},
        {"id": "n17", "text": "無理せず、自然な笑顔で過ごせる一日になりますように。"},
        {"id": "n18", "text": "今日は空を見上げる時間も持ってみましょう。"},
        {"id": "n19", "text": "変わらぬ一日も、よく見ると新しい発見があります。"},
        {"id": "n20", "text": "一息つきながら、穏やかに進めましょう。"},
    ],
    "△": [
        {"id": "s1", "text": "無理は禁物、深呼吸してから始めましょう。"},
        {"id": "s2", "text": "必要なら早めに相談を。ひとりで背負わなくて大丈夫です。"},
        {"id": "s3", "text": "小さな一歩でOK。こまめに休憩を。"},
    ],
    "✕": [
        {"id": "b1", "text": "しっかり休むのも大事な選択です。今日は自分をいたわって。"},
        {"id": "b2", "text": "体調が最優先。周囲への共有は最小限で大丈夫。"},
        {"id": "b3", "text": "あせらず回復に集中しましょう。"},
    ],
}


def _load_history() -> list[str]:
    if HISTORY_FILE.exists():
        try:
            return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def _save_history(ids: list[str]) -> None:
    HISTORY_FILE.write_text(json.dumps(ids[-HISTORY_KEEP:], ensure_ascii=False), encoding="utf-8")


def pick_healing_message(condition: str, name: str | None = None) -> str:
    """
    条件(◎/○/△/✕)に対応するメッセージから、
    直近履歴(HISTORY_KEEP件)と重複しないものをランダムに1つ返す。
    {name} を含む文面には名前を差し込む。
    """
    name = name or ""
    pool = MESSAGES.get(condition, [])
    if not pool:
        return ""

    hist = _load_history()
    candidates = [m for m in pool if m["id"] not in hist] or pool
    msg = random.choice(candidates)
    _save_history(hist + [msg["id"]])

    text = msg["text"]
    if "{name}" in text:
        text = text.format(name=name)
    return text
