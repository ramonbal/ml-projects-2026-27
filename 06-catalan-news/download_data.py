"""Download TeCla v2.0 (Projecte AINA) from Hugging Face into ./data as JSON files.

Requirements: pip install datasets pandas
Usage:        python download_data.py [output_folder]
Licence:      CC BY-NC-ND 4.0 (https://huggingface.co/datasets/projecte-aina/tecla)
"""
import sys
from pathlib import Path

from datasets import load_dataset

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent / "data")
OUT.mkdir(parents=True, exist_ok=True)

ds = load_dataset("projecte-aina/tecla")
names = {"train": "train", "validation": "dev", "test": "test"}
for split, part in ds.items():
    df = part.to_pandas()
    # Turn integer class ids into their names, if the labels are stored as ClassLabel
    for col, feat in part.features.items():
        if hasattr(feat, "names"):
            df[col] = df[col].map(lambda i, n=feat.names: n[i])
    target = OUT / f"{names.get(split, split)}.json"
    df.to_json(target, orient="records", force_ascii=False)
    print(f"{split}: {len(df):,} news items -> {target}")
print("Columns:", list(df.columns))
