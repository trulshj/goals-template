# goals-template

A personal OKR and goal-tracking workspace built around [Claude Code](https://claude.ai/code). See [CLAUDE.md](CLAUDE.md) for the full structure, file roles, and slash commands.

## Getting started

1. Clone this repo and open it in Claude Code
2. Edit `goals.md` with your own objectives and key results
3. Claude will read `CLAUDE.md` automatically and know how to help

## Automated tracking

Optional scripts in `tracking/` pull daily stats into `log.md` via cron. Add your own or adapt the existing ones.

| Script | Source |
|---|---|
| `tracking/wanikani.py` | WaniKani API — logs daily reviews, lessons, and current level |
| `tracking/anki.py` | AnkiConnect (local) — logs daily reviews and new cards; requires Anki to be open |

**Setup:**
```sh
pip install -r tracking/requirements.txt
cp tracking/.env.example tracking/.env
# add your WaniKani API key from wanikani.com/settings/personal-access-tokens
```

**Crontab (adjust paths to your setup):**
```
0 23 * * * /usr/bin/python3 /path/to/goals/tracking/wanikani.py
0 23 * * * /usr/bin/python3 /path/to/goals/tracking/anki.py
```

> **Note:** The KR references in the tracking scripts (e.g. `[Personal / O3 / KR1]`) are examples — update them to match your own goals structure.
