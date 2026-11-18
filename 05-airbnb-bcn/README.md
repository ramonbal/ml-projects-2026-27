# 5 · How much is this flat worth?

## The problem

Predict the price per night of Airbnb listings in Barcelona and, above all, understand what
makes a listing expensive. Tourist flats are a hot public debate in the city (housing,
regulation, neighbourhoods), and you can question your model with flats and areas you know.

**Final product:** a "price estimator" where you enter a flat and get an estimated price with
an interval, and a map of the neighbourhoods.

## Questions to get you started

- Look at the price distribution before modelling. Should you predict the price or something
  derived from it? What do you do with extreme values and missing prices?
- Read what the `price` column really means in each snapshot, and look at `minimum_nights`.
  Is every listing in the same market?
- How do you represent location: neighbourhood, coordinates, the prices of nearby listings?
- Which variables does a regularised model keep, and which does it discard?
- Does the text of the description add information that the structured columns do not have?
  Is it worth the extra complexity?
- Some hosts manage dozens of listings. Can you tell professional hosts from individuals?
- Train with one year and test with the next: how has the market changed?

Course topics that fit: linear and polynomial regression, Ridge and Lasso, kNN, trees, random
forests and boosting, bag of words / TF-IDF for text, logistic regression, clustering.

## The data

**Source:** [Inside Airbnb](https://insideairbnb.com/get-the-data/), Barcelona, licence
**CC BY 4.0**. Two snapshots about 10 months apart, to test your model on a later period.

Included in [`data/`](data/):

| File | Listings | With price | Minimum stay ≥ 31 nights | Columns |
|---|---|---|---|---|
| `2026-09-17/listings.csv.gz` (8.2 MB) | 15,236 | 12,610 | 5,264 (35%) | 90 |
| `2025-11-17/listings.csv.gz` (9.0 MB) | 17,934 | 14,231 | 7,161 (40%) | 79 |
| `2026-09-17/neighbourhoods.geojson` | 75 neighbourhood polygons with their district (10 districts) | | | |

- 12,055 listings appear in both snapshots (same `id`).
- Main columns: neighbourhood and coordinates, property and room type, guests, bedrooms,
  beds, bathrooms, `amenities` (list), `description` (text), host data (seniority,
  superhost, response rate, number of listings), review scores (overall + 7 sub-scores),
  availability, `license`, `minimum_nights`, `price`.
- `room_type` (2026): Entire home/apt 10,602, Private room 4,430, Shared room 125, Hotel
  room 79.
- **Careful with `price`:** in 2026 it is the price per night of a sample stay (it matches
  the `price_quote_*` columns); in 2025 it is the listed price per night. The definition is
  not the same in both snapshots.

```python
import pandas as pd, geopandas as gpd
listings = pd.read_csv("data/2026-09-17/listings.csv.gz")
barris = gpd.read_file("data/2026-09-17/neighbourhoods.geojson")
```

**More data (optional, not included):** [`download_data.py`](download_data.py) downloads the
reviews of the 2026 snapshot (148 MB, 1.13 M reviews with text, 2010–2026) and the 2025
availability calendar (16 MB, prices are empty). Reviews contain people's names: use them
only for the course and do not upload them to your repository.

```bash
python download_data.py
```

Inside Airbnb removes old snapshots from its website after some time; if a URL fails, check
the archive at <https://insideairbnb.com/get-the-data/>.

Extra libraries: `geopandas` or `folium` (maps).
