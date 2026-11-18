# 6 · What is this news story about?

## The problem

Classify Catalan news items by topic, discover topics without using the labels, and build a
search engine that, given a news item, returns related ones. You work with text in your own
language, and you connect bag of words, Bayesian classification and information retrieval.

**Final product:** a related-news search engine.

## Questions to get you started

- Which preprocessing does Catalan need (apostrophes, stop words, accents, lemmas)? Does each
  step actually help? How would you know?
- What is a good baseline for text classification, and how far is a more complex model from
  it?
- There are 4 broad categories and 53 fine ones. Which categories get confused, and is it the
  model's fault or the labels'?
- Which words are most informative for each category?
- If you cluster the news without labels, do the groups look like the editorial categories?
  How many groups make sense?
- How do you evaluate a "related news" engine without anybody telling you which news items
  are related?
- Does the model still work with very short texts, such as only the headline? Or with very
  little training data?

Course topics that fit: bag of words and TF-IDF, Naive Bayes, logistic regression and linear
SVM, dimensionality reduction (LSA), clustering, retrieval metrics.

## The data

**Source:** [TeCla v2.0](https://huggingface.co/datasets/projecte-aina/tecla), Projecte AINA
(Barcelona Supercomputing Center), news from the *Agència Catalana de Notícies*.
Licence **CC BY-NC-ND 4.0**: non-commercial use, cite it, and do not redistribute modified
versions. It is not included here: download it with [`download_data.py`](download_data.py)
(≈270 MB).

```bash
pip install datasets pandas
python download_data.py          # saves train.json, dev.json, test.json in ./data
```

| Split | News items |
|---|---|
| train | 90,700 |
| dev | 5,669 |
| test | 17,007 |

Each item has three fields:

- `text` (called `sentence` in some versions): title, subtitle and body of the news item.
- `label1`: broad category, 4 classes: Societat, Política, Economia, Cultura.
- `label2`: fine category, 53 classes, nested under `label1` (Esports, Salut, Parlament,
  Cinema, Música...).

```python
import pandas as pd
train = pd.read_json("data/train.json")
```

Cite: see the *Citation* section of the dataset card on Hugging Face.
