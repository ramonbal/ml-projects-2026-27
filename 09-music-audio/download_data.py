"""Download the GTZAN audio (Kaggle mirror) into ./data/genres_original.

Only the WAV files are kept: the pre-computed feature CSVs and the spectrogram images of the
mirror are deleted, because this project works from the audio.

Requirements:
  pip install kaggle
  Kaggle token: https://www.kaggle.com/settings -> "Create New Token" -> ~/.kaggle/kaggle.json
Usage:
  python download_data.py [output_folder]
Note: jazz/jazz.00054.wav is corrupt in every known copy; skip it when loading.
"""
import shutil
import sys
import zipfile
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi

DATASET = "andradaolteanu/gtzan-dataset-music-genre-classification"
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent / "data")
OUT.mkdir(parents=True, exist_ok=True)

api = KaggleApi()
api.authenticate()
api.dataset_download_files(DATASET, path=OUT, unzip=False)  # ~1.2 GB zip

archive = next(OUT.glob("*.zip"))
with zipfile.ZipFile(archive) as z:
    wavs = [n for n in z.namelist() if "genres_original/" in n and n.endswith(".wav")]
    for name in wavs:
        rel = name[name.index("genres_original/"):]  # genres_original/<genre>/<file>.wav
        target = OUT / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        with z.open(name) as src, open(target, "wb") as dst:
            shutil.copyfileobj(src, dst)
archive.unlink()

genres = sorted(p.name for p in (OUT / "genres_original").iterdir() if p.is_dir())
print(f"{len(wavs)} clips in {OUT / 'genres_original'}: {', '.join(genres)}")
