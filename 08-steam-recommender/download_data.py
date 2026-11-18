"""Download 'Game Recommendations on Steam' (Kaggle, CC0) into ./data/full.

The repository already includes a 4 M-row sample in ./data; you only need this script to
work with the full dataset (>2 GB uncompressed) or with users.csv.

Requirements:
  pip install kaggle
  Kaggle token: https://www.kaggle.com/settings -> "Create New Token" -> ~/.kaggle/kaggle.json
Usage:
  python download_data.py            # full dataset
  python download_data.py --small    # only games.csv, users.csv and games_metadata.json
"""
import sys
import zipfile
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi

DATASET = "antonkozyriev/game-recommendations-on-steam"
OUT = Path(__file__).resolve().parent / "data" / "full"
OUT.mkdir(parents=True, exist_ok=True)

api = KaggleApi()
api.authenticate()

if "--small" in sys.argv:
    for f in ["games.csv", "users.csv", "games_metadata.json"]:
        api.dataset_download_file(DATASET, f, path=OUT)
    for z in OUT.glob("*.zip"):
        zipfile.ZipFile(z).extractall(OUT)
        z.unlink()
else:
    api.dataset_download_files(DATASET, path=OUT, unzip=True)

for p in sorted(OUT.iterdir()):
    print(f"{p.name}: {p.stat().st_size / 1e6:.1f} MB")
