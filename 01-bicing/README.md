# 1 · Will there be a Bicing bike?

## The problem

You walk to a Bicing station and it is empty. Again. Can we predict how many bikes (and how
many free docks) a station will have in 30 or 60 minutes, so that a user can decide where to
go? Barcelona publishes the state of every station every few minutes, so there is plenty of
data, and the result can be shown on a map of the city.

**Final product:** a map of Barcelona with the prediction for each station.

## Questions to get you started

There are no right answers written here: finding them, with evidence, is the project.

- What does a user actually care about: the exact number of bikes, or whether the station
  will be empty? How does that change the model and the metric you choose?
- How should you split the data when the samples are ordered in time? What happens if you
  split at random?
- What is a reasonable baseline, one that any model must beat to be useful?
- Which information helps: the time of day, the day of the week, the recent past of the
  station, the neighbouring stations, the weather, the altitude?
- Do all stations behave the same way? Are there "residential" and "work" stations?
  Would one model for all stations be better than one per group of stations?
- Does your model still work on a week it has never seen?

Course topics that fit: regression and regularisation, logistic regression, SVM, trees,
random forests and boosting, clustering, model evaluation.

## The data

**Source:** Open Data BCN (Ajuntament de Barcelona), licence **CC BY 4.0**.

- Station status: <https://opendata-ajuntament.barcelona.cat/data/ca/dataset/estat-estacions-bicing>
- Station information: <https://opendata-ajuntament.barcelona.cat/data/ca/dataset/informacio-estacions-bicing>

Included in [`data/`](data/):

| File | Content | Size (compressed / CSV) | Rows |
|---|---|---|---|
| `2026_08_Agost_BicingNou_ESTACIONS.7z` | status of every station, August 2026 | 18 MB / 256 MB | 3,987,120 |
| `2026_09_Setembre_BicingNou_ESTACIONS.7z` | status of every station, September 2026 | 22 MB / 291 MB | 4,528,265 |
| `estacions_info_2026_09.csv` | one row per station: name, coordinates, altitude, district, capacity | 0.1 MB | 545 |

- One snapshot every ~5 minutes for each of the 545 stations: 8.5 M readings in total.
- Each `.7z` holds a single CSV. Unzip it with 7-Zip or in Python with `py7zr`.
- Timestamps are Unix epoch (UTC).
- You do not need all 8.5 M rows: aggregating by station and hour (or 15 min) is a sensible
  first step.

**Status fields** (`*_ESTACIONS.csv`): `station_id`, `num_bikes_available`,
`num_bikes_available_types.mechanical`, `num_bikes_available_types.ebike`,
`num_docks_available`, `is_charging_station`, `status` (IN_SERVICE / NOT_IN_SERVICE /
MAINTENANCE / PLANNED), `last_reported`, `is_installed`, `is_renting`, `is_returning`,
`last_updated`, `ttl`.

**Station fields** (`estacions_info_2026_09.csv`): `station_id`, `name`, `lat`, `lon`,
`altitude`, `address`, `cross_street` (district/neighbourhood, e.g. `02-Eixample/05-el Fort
Pienc`), `post_code`, `capacity`, ...

```python
import py7zr, pandas as pd
with py7zr.SevenZipFile("data/2026_09_Setembre_BicingNou_ESTACIONS.7z") as z:
    z.extractall("data/")
status = pd.read_csv("data/2026_09_Setembre_BicingNou_ESTACIONS.csv")
stations = pd.read_csv("data/estacions_info_2026_09.csv")
```

**More data (optional):**

- Other months, since 2019: same Open Data BCN page, one `.7z` per month.
- Hourly weather for Barcelona: [Open-Meteo](https://open-meteo.com/) (free, no key needed).

Extra libraries: `py7zr`, `folium` (map).
