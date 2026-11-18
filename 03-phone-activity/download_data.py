"""Download UCI HAR and MotionSense into ./data (about 135 MB).

Usage: python download_data.py [output_folder]
"""
import sys
import urllib.request
import zipfile
from pathlib import Path

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent / "data")
OUT.mkdir(parents=True, exist_ok=True)

FILES = {
    # UCI HAR (CC BY 4.0). The zip contains another zip, "UCI HAR Dataset.zip".
    "UCI_HAR_Dataset.zip":
        "https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip",
    # MotionSense (ODbL)
    "MotionSense_A_DeviceMotion_data.zip":
        "https://github.com/mmalekzadeh/motion-sense/raw/master/data/A_DeviceMotion_data.zip",
    "MotionSense_data_subjects_info.csv":
        "https://raw.githubusercontent.com/mmalekzadeh/motion-sense/master/data/data_subjects_info.csv",
}


def unzip_all(path, dest):
    """Extract a zip, and any zip found inside it."""
    with zipfile.ZipFile(path) as z:
        z.extractall(dest)
        inner = [n for n in z.namelist() if n.endswith(".zip")]
    for name in inner:
        unzip_all(dest / name, dest)


for name, url in FILES.items():
    target = OUT / name
    if not target.exists():
        print("Downloading", url)
        urllib.request.urlretrieve(url, target)
    if target.suffix == ".zip":
        print("Extracting", name)
        unzip_all(target, OUT)

print("Done. Contents of", OUT)
for p in sorted(OUT.iterdir()):
    print("  ", p.name)
