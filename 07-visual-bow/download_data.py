"""Download the image datasets into ./data.

Usage:
  python download_data.py indian     # Indian Food (Hugging Face mirror), ~1.6 GB  [default]
  python download_data.py food101    # Food-101, ~5.0 GB (tar.gz)
  python download_data.py oxford     # Oxford Buildings 5k, ~1.8 GB images + ground truth
  python download_data.py all
Better run it outside synced folders (OneDrive, Dropbox...).
"""
import sys
import tarfile
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent / "data"

URLS = {
    "food101": ["http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz"],
    "oxford": [
        # Original VGG website (Oxford). If it does not respond, see the README for alternatives.
        "https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/oxbuild_images-v1.tgz",
        "https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/gt_files_170407.tgz",
        # Ground truth of Revisited Oxford (ROxford5k), Radenovic et al. 2018
        "http://cmp.felk.cvut.cz/revisitop/data/datasets/roxford5k/gnd_roxford5k.pkl",
    ],
}


def progress(blocks, bsize, total):
    if total > 0 and blocks % 2000 == 0:
        print(f"\r  {blocks * bsize / 1e6:,.0f} / {total / 1e6:,.0f} MB", end="", flush=True)


def indian():
    """Indian Food: saved as JPEG files in data/indian_food/<split>/<class>/."""
    from datasets import load_dataset  # pip install datasets pillow

    ds = load_dataset("rajistics/indian_food_images")
    names = ds["train"].features["label"].names
    for split, part in ds.items():
        for i, ex in enumerate(part):
            folder = OUT / "indian_food" / split / names[ex["label"]]
            folder.mkdir(parents=True, exist_ok=True)
            ex["image"].convert("RGB").save(folder / f"{i:05d}.jpg", quality=95)
        print(f"{split}: {len(part)} images")


def fetch(name):
    dest = OUT / name
    dest.mkdir(parents=True, exist_ok=True)
    for url in URLS[name]:
        fn = dest / url.rsplit("/", 1)[-1]
        if not fn.exists():
            print("Downloading", url)
            urllib.request.urlretrieve(url, fn, progress)
            print()
        if fn.suffix in (".gz", ".tgz"):
            sub = dest / fn.name.split(".")[0] if name == "oxford" else dest
            print("Extracting", fn.name)
            with tarfile.open(fn) as t:
                t.extractall(sub, filter="data")
            fn.unlink()


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "indian"
    jobs = ["indian", "food101", "oxford"] if which == "all" else [which]
    for job in jobs:
        indian() if job == "indian" else fetch(job)
