"""Download the optional Inside Airbnb Barcelona files that are not in this repository.

  data/2026-09-17/reviews.csv.gz   (148 MB) reviews with text
  data/2025-11-17/calendar.csv.gz  ( 16 MB) availability per listing and day (no prices)

The listings of both snapshots are already in ./data.
Usage: python download_data.py
Licence: CC BY 4.0, Inside Airbnb (https://insideairbnb.com/).
"""
import urllib.request
from pathlib import Path

BASE = "https://data.insideairbnb.com/spain/catalonia/barcelona/{date}/data/{name}"
OUT = Path(__file__).resolve().parent / "data"

FILES = [
    ("2026-09-17", "reviews.csv.gz"),
    ("2025-11-17", "calendar.csv.gz"),
]

for date, name in FILES:
    target = OUT / date / name
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        print("Already there:", target)
        continue
    url = BASE.format(date=date, name=name)
    print("Downloading", url)
    try:
        urllib.request.urlretrieve(url, target)
    except Exception as ex:  # noqa: BLE001
        print("  FAILED:", ex, "- the snapshot may have been archived; see https://insideairbnb.com/get-the-data/")
        continue
    print(f"  {target.stat().st_size / 1e6:.1f} MB")
