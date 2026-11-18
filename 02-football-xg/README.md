# 2 · Football analyst: the xG model

## The problem

*Expected goals* (xG) is the probability that a shot ends in a goal, given where it was taken
from and how. Clubs and TV broadcasts use it every weekend to judge whether a team deserved
to win or whether a striker is finishing above or below what is expected. Build your own xG
model, compare it with the professional one, and use it to analyse players.

**Final product:** a scouting report "like a club analyst": which players score above their
xG, and a search tool for similar players.

## Questions to get you started

- Only about 12% of shots are goals. Which metrics make sense, and which ones are misleading?
- From the raw coordinates `x, y`, which representation of the shot makes the problem
  easier for a linear model?
- When is a probability "good"? Is a model that ranks shots well also a model whose 0.3
  means 30%?
- Should penalties and free kicks be in the same model as the other shots?
- How close can you get to StatsBomb's own xG with the variables you have?
- A model trained on men's football: does it work on women's football?
- How would you describe a player's style with numbers, and find players that look alike?

Course topics that fit: logistic regression and regularisation, kNN, model evaluation and
calibration, trees, random forests and boosting, clustering, similarity search.

## The data

**Source:** [StatsBomb Open Data](https://github.com/statsbomb/open-data). Free to use for
research and education; **you must cite StatsBomb** (and show their logo in any publication),
following the StatsBomb Open Data terms.

Included in [`data/`](data/):

| File | Content | Size | Rows |
|---|---|---|---|
| `shots.csv` | every shot of the selected competitions | 4.1 MB | 28,077 shots, 1,130 matches, 3,423 goals (12.2%) |

- La Liga, all available seasons (mostly FC Barcelona matches, and the full 2015/16 season):
  21,181 shots.
- Men's World Cup (2018, 2022 and some historical matches 1958–1990): 3,904 shots.
- Women's World Cup (2019, 2023): 2,992 shots.

**Columns:** `match_id`, `competition`, `season`, `player`, `team`,
`x`, `y` (StatsBomb pitch 120×80; the opponent's goal is at x=120, posts at y=36 and y=44),
`distance` (yards to the centre of the goal), `angle` (radians between the two posts as seen
from the shot), `body_part`, `technique`, `shot_type` (Open Play, Penalty, Free Kick,
Corner...), `play_pattern`, `under_pressure`, `statsbomb_xg` (StatsBomb's own xG, for
comparison only), `is_goal` (**target**).

```python
import pandas as pd
shots = pd.read_csv("data/shots.csv")
```

**More data (optional):** [`extract_shots.py`](extract_shots.py) regenerates `shots.csv`
with `statsbombpy` and can be edited to add other competitions or other events (passes,
carries, pressures) to describe players' style:

```bash
pip install statsbombpy pandas
python extract_shots.py data/shots.csv
```
