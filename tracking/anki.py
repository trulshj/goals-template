#!/usr/bin/env python3
import sys
import requests
from datetime import datetime
from log import TZ, write_entry

ANKI_URL = "http://127.0.0.1:8765"


def anki(action, **params):
    payload = {"action": action, "version": 6}
    if params:
        payload["params"] = params
    try:
        resp = requests.post(ANKI_URL, json=payload, timeout=5)
        resp.raise_for_status()
    except requests.ConnectionError:
        sys.exit("Error: Could not connect to AnkiConnect. Is Anki running?")
    result = resp.json()
    if result.get("error"):
        sys.exit(f"AnkiConnect error: {result['error']}")
    return result["result"]


def get_reviews_today():
    return anki("getNumCardsReviewedToday")


def get_new_cards_today():
    now = datetime.now(TZ)
    start_of_day = datetime(now.year, now.month, now.day, tzinfo=TZ)
    start_ms = int(start_of_day.timestamp() * 1000)

    decks = anki("deckNames")
    seen = set()
    new_count = 0
    for deck in decks:
        for review in anki("cardReviews", deck=deck, startID=start_ms):
            key = (review[0], review[1])  # (reviewTime, cardId)
            if key not in seen:
                seen.add(key)
                if review[8] == 0:  # reviewType 0 = new/learning
                    new_count += 1
    return new_count


if __name__ == "__main__":
    reviews = get_reviews_today()
    new_cards = get_new_cards_today()
    entry = f"- [Personal / O3 / KR2] Anki: {reviews} reviews, {new_cards} new cards"
    write_entry(entry, "- [Personal / O3 / KR2] Anki:")
    date_str = datetime.now(TZ).strftime("%Y-%m-%d")
    print(f"Logged for {date_str}: {reviews} reviews, {new_cards} new cards.")
