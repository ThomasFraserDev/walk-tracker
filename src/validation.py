import re
from datetime import datetime

def validate_date(date_str: str) -> str | None:
    date_str = date_str.strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        return None
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return None

def parse_positive_int(value_str: str) -> int | None:
    try:
        v = int(value_str.strip())
        return v if v > 0 else None
    except ValueError:
        return None

def parse_positive_float(value_str: str) -> float | None:
    try:
        v = float(value_str.strip())
        return v if v > 0 else None
    except ValueError:
        return None

def validate_choice(value_str: str, choices: set[str]) -> str | None:
    val = value_str.strip().lower()
    return val if val in choices else None

def parse_yes_no(value_str: str) -> bool | None:
    val = value_str.strip().lower()
    if val in {"y", "yes"}:
        return True
    if val in {"n", "no"}:
        return False
    return None