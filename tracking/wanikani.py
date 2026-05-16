#!/usr/bin/env python3
import os
import sys
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
from log import TZ, write_entry

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

API_BASE = "https://api.wanikani.com/v2"


def headers():
    key = os.environ.get("WANIKANI_API_KEY")
    if not key:
        sys.exit("Error: WANIKANI_API_KEY environment variable not set.")
    return {"Authorization": f"Bearer {key}", "Wanikani-Revision": "20170710"}


def today_utc_iso():
    now = datetime.now(TZ)
    start = datetime(now.year, now.month, now.day, tzinfo=TZ)
    return start.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch_all(endpoint, params=None):
    items = []
    url = f"{API_BASE}/{endpoint}"
    while url:
        resp = requests.get(url, headers=headers(), params=params)
        resp.raise_for_status()
        body = resp.json()
        items.extend(body.get("data", []))
        url = body.get("pages", {}).get("next_url")
        params = None
    return items


def get_level():
    resp = requests.get(f"{API_BASE}/user", headers=headers())
    resp.raise_for_status()
    return resp.json()["data"]["level"]


def get_reviews_today():
    cutoff = today_utc_iso()
    stats = fetch_all("review_statistics", {"updated_after": cutoff})
    return len(stats)


def get_lessons_today():
    today_start = today_utc_iso()
    assignments = fetch_all("assignments", {"updated_after": today_start, "started": "true"})
    return sum(
        1 for a in assignments
        if a.get("data", {}).get("started_at", "") >= today_start
    )


if __name__ == "__main__":
    level = get_level()
    reviews = get_reviews_today()
    lessons = get_lessons_today()
    entry = f"- [Personal / O3 / KR1] WaniKani: {reviews} reviews, {lessons} lessons — level {level}"
    write_entry(entry, "- [Personal / O3 / KR1] WaniKani:")
    date_str = datetime.now(TZ).strftime("%Y-%m-%d")
    print(f"Logged for {date_str}: level {level}, {reviews} reviews, {lessons} lessons.")
