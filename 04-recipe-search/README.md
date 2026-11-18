# 4 · What can I cook today? A recipe search engine

## The problem

*"I want Italian food and I have tomato, garlic, basil and pasta: what can I make?"*
Build a system that answers this kind of query with a **ranked list of dishes**, and find a
way to measure whether that list is good. It is an information retrieval problem over a
*bag of words* of ingredients. Knowing the cuisine of each recipe helps, but only a small part
of the recipes have it.

**Final product:** a recipe search engine by cuisine and ingredients (try it with what is in
your fridge).

## Questions to get you started

- How do you represent a recipe so that you can compare it with a query? Do all ingredients
  weigh the same ("salt" vs "saffron")? Are "tomatoes", "chopped tomato" and "tomato" the
  same word?
- To evaluate a search engine you need to know which results are relevant. Nobody has
  annotated that for you. How could you build a set of queries with known answers from the
  data itself?
- Which metrics tell you whether a ranked list is good, beyond plain accuracy?
- Most recipes have no cuisine label. Can you predict it from the ingredients? Is a dataset
  from a different website useful to train or check that classifier?
- Should the cuisine filter the results, or just be one more signal in the ranking?
- Besides similarity, what else makes a recipe a good answer (rating, preparation time,
  popularity)? How do you avoid always recommending the same popular dishes?
- Can the ratings of other users personalise the results?

Course topics that fit: bag of words and TF-IDF, retrieval and ranking metrics, Naive Bayes,
logistic regression and SVM, clustering, recommender systems.

## The data

Both datasets are on Kaggle and **cannot be redistributed here**. Download them with
[`download_data.py`](download_data.py) (needs a Kaggle account and API token, see the
[main README](../README.md#getting-the-data)). For What's Cooking you must first **accept the
competition rules** at <https://www.kaggle.com/competitions/whats-cooking/rules> with the same
account.

```bash
pip install kaggle
python download_data.py          # saves everything in ./data
```

### Food.com Recipes and Interactions (the collection)

- <https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions>
- `RAW_recipes.csv` (295 MB): 231,637 recipes with `name`, `id`, `minutes`, `tags`,
  `nutrition`, `n_steps`, `steps`, `description`, `ingredients`, `n_ingredients`.
  About 37,000 recipes have a cuisine among their `tags` (18 cuisines).
- `RAW_interactions.csv` (349 MB): 1,132,367 ratings of 226,570 users, with `user_id`,
  `recipe_id`, `date`, `rating` (0–5) and `review`. 72% of the ratings are a 5; a 0 usually
  means "review without a rating".
- Cite: Majumder et al., *Generating Personalized Recipes from Historical User Preferences*,
  EMNLP 2019.

### What's Cooking (external labelled set)

- <https://www.kaggle.com/competitions/whats-cooking/data>
- `train.json`: 39,774 recipes with `id`, `cuisine` and `ingredients` (a list); 6,714
  different ingredients.
- 20 cuisines, very unbalanced: italian 7,838, mexican 6,438, southern_us 4,320, indian 3,003,
  chinese 2,673, french 2,646, ... russian 489, brazilian 467.
- `test.json` has no labels: to evaluate, split `train.json`.

```python
import pandas as pd
recipes = pd.read_csv("data/food_com/RAW_recipes.csv")
ratings = pd.read_csv("data/food_com/RAW_interactions.csv")
wc = pd.read_json("data/whats_cooking/train.json")
```
