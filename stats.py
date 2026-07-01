import json
import os

STATS_FILE = "stats.json"

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {
            "checks": 0,
            "alerts": 0,
            "products": 0
        }

    with open(STATS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_stats(stats):
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)

def increment_checks():
    stats = load_stats()
    stats["checks"] += 1
    save_stats(stats)

def increment_alerts():
    stats = load_stats()
    stats["alerts"] += 1
    save_stats(stats)
