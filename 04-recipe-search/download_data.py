"""Download the recipe datasets from Kaggle into ./data.

Requirements:
  pip install kaggle
  Kaggle token: https://www.kaggle.com/settings -> "Create New Token" -> save kaggle.json in
  ~/.kaggle/kaggle.json (Windows: C:\\Users\\<you>\\.kaggle\\kaggle.json).
  For 'whats-cooking' you must accept the competition rules first, with the same account:
  https://www.kaggle.com/competitions/whats-cooking/rules
Usage:
  python download_data.py [output_folder]
"""
import sys
import zipfile
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent / "data")

api = KaggleApi()
api.authenticate()


def unzip_here(folder):
    for z in folder.glob("*.zip"):
        zipfile.ZipFile(z).extractall(folder)
        z.unlink()


# 1) What's Cooking (competition): train.json + test.json (unlabelled), ~15 MB
wc = OUT / "whats_cooking"
wc.mkdir(parents=True, exist_ok=True)
for f in ["train.json.zip", "test.json.zip"]:
    api.competition_download_file("whats-cooking", f, path=wc)
unzip_here(wc)

# 2) Food.com Recipes and User Interactions: RAW_recipes.csv, RAW_interactions.csv (~640 MB)
fc = OUT / "food_com"
fc.mkdir(parents=True, exist_ok=True)
for f in ["RAW_recipes.csv", "RAW_interactions.csv"]:
    api.dataset_download_file("shuyangli94/food-com-recipes-and-user-interactions", f, path=fc)
unzip_here(fc)

print("Done:")
for p in sorted(OUT.rglob("*")):
    if p.is_file():
        print(f"  {p.relative_to(OUT)}  {p.stat().st_size / 1e6:.1f} MB")
