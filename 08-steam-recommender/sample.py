"""Build a sample of recommendations from the full recommendations.csv (~2 GB) of Kaggle.

Sampling: take the active users (>= MIN_RECS recommendations) and pick them at random (fixed
seed) until the sample has ~TARGET_ROWS rows. ALL the recommendations of each picked user are
kept, so no user is cut in half.

Usage: python sample.py <recommendations.csv> [output.csv]
"""
import sys

import numpy as np
import pandas as pd

MIN_RECS = 5
TARGET_ROWS = 4_000_000  # ~200 MB
SEED = 42

src = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else "recommendations_sample.csv"

counts = pd.read_csv(src, usecols=["user_id"])["user_id"].value_counts()
active = counts[counts >= MIN_RECS]
rng = np.random.default_rng(SEED)
order = rng.permutation(active.index.to_numpy())
cum = active.loc[order].cumsum().to_numpy()
chosen = set(order[: np.searchsorted(cum, TARGET_ROWS) + 1])
print(f"users: {len(counts):,}; active (>= {MIN_RECS}): {len(active):,}; picked: {len(chosen):,}")

first, n = True, 0
for chunk in pd.read_csv(src, chunksize=2_000_000):
    part = chunk[chunk["user_id"].isin(chosen)]
    part.to_csv(out, mode="w" if first else "a", header=first, index=False)
    first, n = False, n + len(part)
print(f"{n:,} recommendations saved to {out}")
