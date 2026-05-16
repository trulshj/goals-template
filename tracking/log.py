import os
from datetime import datetime
from zoneinfo import ZoneInfo

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "log.md")
TZ = ZoneInfo("Europe/Oslo")


def write_entry(entry: str, prefix: str) -> None:
    """Write or update a log entry for today. Replaces any existing line starting with prefix in today's section."""
    date_str = datetime.now(TZ).strftime("%Y-%m-%d")

    with open(LOG_PATH, "r") as f:
        lines = f.readlines()

    header_idx = None
    entry_idx = None
    for i, line in enumerate(lines):
        if line.rstrip() == f"## {date_str}":
            header_idx = i
        elif header_idx is not None and line.startswith("## "):
            break
        elif header_idx is not None and line.startswith(prefix):
            entry_idx = i
            break

    if entry_idx is not None:
        lines[entry_idx] = entry + "\n"
    elif header_idx is not None:
        lines.insert(header_idx + 1, entry + "\n")
    else:
        sep_idx = next(i for i, l in enumerate(lines) if l.rstrip() == "---")
        for j, item in enumerate(["\n", f"## {date_str}\n", entry + "\n"]):
            lines.insert(sep_idx + 1 + j, item)

    with open(LOG_PATH, "w") as f:
        f.writelines(lines)
