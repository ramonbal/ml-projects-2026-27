# 8 · Video game recommender

## The problem

Recommend Steam games to a player, based on what similar players liked and on the
description and tags of the games. You can judge the result yourselves: what does the system
recommend to someone who played a game you know well?

**Final product:** a game recommender, evaluated on users it has never seen (and tried with
your own tastes).

## Questions to get you started

- What is the simplest recommender that any other system must beat?
- What counts as "liking" a game: an explicit recommendation, the hours played, both?
- How do you split the data to evaluate a recommender honestly? Which metrics tell you
  whether the top of the list is good?
- When is it better to recommend from the content of the games, and when from the behaviour
  of similar users? Does the answer depend on how many games a user has played?
- A good score can hide a system that only recommends the same famous games. How would you
  detect it?
- What do you recommend to a brand new user?
- Can you predict whether a user will recommend a game they have not reviewed yet?

Course topics that fit: recommender systems (content-based, collaborative filtering, matrix
factorisation), kNN, TF-IDF, logistic regression and random forests, clustering, ranking
metrics.

## The data

**Source:** Kaggle,
[Game Recommendations on Steam](https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam)
(Anton Kozyriev), licence **CC0**. The full dataset has 41 M recommendations (2 GB); this
repository includes a **sample** that fits in memory.

Included in [`data/`](data/):

| File | Size | Rows | Columns |
|---|---|---|---|
| `recommendations_sample.csv.xz` | 46 MB (197 MB as CSV) | 4,000,039 recommendations · 339,169 users · 33,886 games | `app_id`, `helpful`, `funny`, `date`, `is_recommended`, `hours`, `user_id`, `review_id` |
| `games.csv` | 4.9 MB | 50,872 games | `app_id`, `title`, `date_release`, `win`, `mac`, `linux`, `rating`, `positive_ratio`, `user_reviews`, `price_final`, `price_original`, `discount`, `steam_deck` |
| `games_metadata.json.gz` | 5.6 MB | 50,872 games (one JSON per line) | `app_id`, `description`, `tags` |

- Target: `is_recommended` (84.6% positive in the sample), or a ranking of games per user.
- Dates: October 2010 to December 2022.
- How the sample was made ([`sample.py`](sample.py)): among the users with at least 5
  recommendations, users are picked at random (seed 42) until ~4 M rows, and **all** the
  recommendations of each picked user are kept (no user is cut in half).

```python
import pandas as pd
recs = pd.read_csv("data/recommendations_sample.csv.xz")
games = pd.read_csv("data/games.csv")
meta = pd.read_json("data/games_metadata.json.gz", lines=True)
```

**More data (optional):** to work with the full dataset, or with `users.csv` (number of
products and reviews per user, 193 MB), download it with
[`download_data.py`](download_data.py) (needs a Kaggle token, see the
[main README](../README.md#getting-the-data)) and make your own sample with `sample.py`:

```bash
pip install kaggle
python download_data.py                      # full dataset in ./data/full (>2 GB)
python sample.py data/full/recommendations.csv my_sample.csv
```
