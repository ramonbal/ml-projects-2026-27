"""Optional out-of-distribution test: FMA-small clips of the genres Hip-Hop, Pop and Rock.

Downloads the FMA metadata (~342 MB) and the FMA-small audio (~7.2 GB, 8,000 MP3 clips of
30 s), and keeps only the clips of the three genres shared with GTZAN (hiphop, pop, rock;
1,000 per genre). The big archive goes to a temporary folder that is deleted at the end.

Requirements: pip install pandas
Usage:        python download_fma_subset.py [output_folder] [temp_folder]
              (defaults: ./data/fma_subset and the system temp folder; better outside OneDrive)
Source:       https://github.com/mdeff/fma - Defferrard et al., "FMA: A Dataset for Music
              Analysis", ISMIR 2017. Audio under each artist's Creative Commons licence
              (see the 'license' column of the output CSV).
"""
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

BASE = "https://os.unil.cloud.switch.ch/fma/"
GENRES = {"Hip-Hop": "hiphop", "Pop": "pop", "Rock": "rock"}  # FMA name -> GTZAN name

out = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent / "data" / "fma_subset")
tmp = Path(sys.argv[2] if len(sys.argv) > 2 else tempfile.mkdtemp(prefix="fma_"))
out.mkdir(parents=True, exist_ok=True)
tmp.mkdir(parents=True, exist_ok=True)


def fetch(name):
    dest = tmp / name
    if not dest.exists():
        print("Downloading", BASE + name)
        urllib.request.urlretrieve(BASE + name, dest)
    return dest


# 1) Metadata: tracks.csv has a two-level header
with zipfile.ZipFile(fetch("fma_metadata.zip")) as z:
    z.extract("fma_metadata/tracks.csv", tmp)
tracks = pd.read_csv(tmp / "fma_metadata/tracks.csv", index_col=0, header=[0, 1])
small = tracks[tracks[("set", "subset")] == "small"]
sel = small[small[("track", "genre_top")].isin(GENRES)]
meta = pd.DataFrame({
    "track_id": sel.index,
    "genre_fma": sel[("track", "genre_top")].values,
    "genre": sel[("track", "genre_top")].map(GENRES).values,
    "artist": sel[("artist", "name")].values,
    "title": sel[("track", "title")].values,
    "license": sel[("track", "license")].values,
})
meta["path"] = [f"{g}/{t:06d}.mp3" for g, t in zip(meta["genre"], meta["track_id"])]
print(meta["genre"].value_counts().to_string())

# 2) Audio: only the selected clips
with zipfile.ZipFile(fetch("fma_small.zip")) as z:
    for t, g in zip(meta["track_id"], meta["genre"]):
        member = f"fma_small/{t:06d}"[:13] + f"/{t:06d}.mp3"  # fma_small/XXX/XXXXXX.mp3
        (out / g).mkdir(exist_ok=True)
        with z.open(member) as src, open(out / g / f"{t:06d}.mp3", "wb") as dst:
            shutil.copyfileobj(src, dst)

meta.to_csv(out / "fma_subset_metadata.csv", index=False)
shutil.rmtree(tmp, ignore_errors=True)
print(f"{len(meta)} clips saved to {out}")
