"""Extract every shot from StatsBomb Open Data (La Liga, all seasons; men's World Cup;
women's World Cup) into a CSV file.

Requirements: pip install statsbombpy pandas
Usage:        python extract_shots.py [output.csv]
Data:         StatsBomb Open Data (https://github.com/statsbomb/open-data). Cite StatsBomb.
"""
import math
import sys
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
from statsbombpy import sb

warnings.filterwarnings("ignore")  # "credentials were not supplied" warning

COMPETITIONS = {
    "La Liga": 11,
    "FIFA World Cup": 43,
    "Women's World Cup": 72,
}
# StatsBomb pitch: 120x80, posts at (120, 36) and (120, 44)
GOAL_X, POST_L, POST_R = 120.0, 36.0, 44.0


def geometry(x, y):
    dx, dy = GOAL_X - x, 40.0 - y
    distance = math.hypot(dx, dy)
    angle = abs(math.atan2(POST_R - y, GOAL_X - x) - math.atan2(POST_L - y, GOAL_X - x))
    return distance, angle


def match_shots(match_id, competition, season):
    ev = sb.events(match_id=match_id)
    ev = ev[ev["type"] == "Shot"]
    rows = []
    for _, e in ev.iterrows():
        x, y = e["location"][0], e["location"][1]
        distance, angle = geometry(x, y)
        under = e.get("under_pressure")
        rows.append({
            "match_id": match_id,
            "competition": competition,
            "season": season,
            "player": e["player"],
            "team": e["team"],
            "x": x,
            "y": y,
            "distance": round(distance, 3),
            "angle": round(angle, 4),  # radians, angle between the two posts
            "body_part": e.get("shot_body_part"),
            "technique": e.get("shot_technique"),
            "shot_type": e.get("shot_type"),
            "play_pattern": e.get("play_pattern"),
            "under_pressure": bool(under) if pd.notna(under) else False,
            "statsbomb_xg": e.get("shot_statsbomb_xg"),
            "is_goal": int(e.get("shot_outcome") == "Goal"),
        })
    return rows


def main(out="shots.csv"):
    comps = sb.competitions()
    jobs = []
    for name, cid in COMPETITIONS.items():
        for _, c in comps[comps["competition_id"] == cid].iterrows():
            matches = sb.matches(competition_id=cid, season_id=c["season_id"])
            jobs += [(m, name, c["season_name"]) for m in matches["match_id"]]
            print(f"{name} {c['season_name']}: {len(matches)} matches", flush=True)
    print(f"Total matches: {len(jobs)}", flush=True)

    rows, failed = [], []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futs = {pool.submit(match_shots, *j): j for j in jobs}
        for i, f in enumerate(as_completed(futs), 1):
            try:
                rows += f.result()
            except Exception as ex:  # noqa: BLE001
                failed.append((futs[f][0], repr(ex)))
            if i % 100 == 0:
                print(f"  {i}/{len(jobs)} matches processed", flush=True)

    df = pd.DataFrame(rows).sort_values(["competition", "season", "match_id"])
    df.to_csv(out, index=False)
    print(f"{len(df)} shots saved to {out}; failed matches: {len(failed)}")
    for m, err in failed:
        print("  FAIL", m, err)


if __name__ == "__main__":
    main(*sys.argv[1:])
