# 7 · Images with visual Bag of Words

## The problem

Classify photos and find similar images **without deep learning**, using the *bag of visual
words* model: local descriptors (small patches around keypoints) are turned into "visual
words" with clustering, and each image becomes a histogram of words, just like a text
document. Choose one of two problems: dishes (Indian food) or famous buildings (Oxford), which
gives a cleaner image retrieval problem.

**Final product:** an image classifier and an image search engine ("show me photos like this
one").

## Questions to get you started

- Which local descriptor, and where do you compute it: at detected keypoints or on a dense
  grid? How does that affect accuracy and computing time?
- How many visual words do you need? What happens with too few or too many?
- How should the histograms be normalised, and which similarity or kernel suits them?
- Can you reuse ideas from text (TF-IDF, stop words) for visual words?
- For which classes does the model fail, and what information is it missing (shape, colour,
  background)?
- How robust is it to changes in lighting, scale or occlusion?
- How do you evaluate a search engine that returns a ranked list of images?

Course topics that fit: bag of words, k-means, kNN, SVM and kernels (including histogram
intersection), random forests, retrieval metrics (mAP).

## The data

Image datasets are large and their licences do not allow redistribution, so they are not in
this repository. Use [`download_data.py`](download_data.py):

```bash
pip install datasets pillow opencv-python
python download_data.py indian      # Indian Food, ~1.6 GB (default)
python download_data.py food101     # Food-101, ~5 GB (optional)
python download_data.py oxford      # Oxford Buildings 5k, ~1.8 GB (optional)
```

Do it outside synced folders (OneDrive, Dropbox...).

### Indian Food (main option)

- Kaggle: <https://www.kaggle.com/datasets/l33tc0d3r/indian-food-classification>;
  the script uses the equivalent Hugging Face mirror `rajistics/indian_food_images`.
- 6,269 RGB images (5,328 train / 941 test), 20 classes: burger, butter_naan, chai, chapati,
  chole_bhature, dal_makhani, dhokla, fried_rice, idli, jalebi, kaathi_rolls, kadai_paneer,
  kulfi, masala_dosa, momos, paani_puri, pakode, pav_bhaji, pizza, samosa.
- A good size for SIFT + k-means as it is.

```python
from datasets import load_dataset
ds = load_dataset("rajistics/indian_food_images")
img, y = ds["train"][0]["image"], ds["train"][0]["label"]   # PIL.Image, int
```

### Food-101 (optional, larger)

- <https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/>
- 101,000 images, 101 dishes (750 train + 250 test per class). Too big for BoW as it is:
  pick a subset of 10–20 classes.
- Cite: Bossard et al., *Food-101 – Mining Discriminative Components with Random Forests*,
  ECCV 2014.

### Oxford Buildings 5k (optional, retrieval)

- <https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/>
- 5,062 Flickr photos of 11 Oxford landmarks, with **55 query images and their annotated
  relevant images**: ready to evaluate a search engine with mAP.
- If the Oxford server does not respond, use the *Revisited Oxford* version
  (<http://cmp.felk.cvut.cz/revisitop/>) or a mirror on Kaggle / Hugging Face ("oxford5k").
- Cite: Philbin et al., *Object retrieval with large vocabularies and fast spatial
  matching*, CVPR 2007.

Extra libraries: `opencv-python` (SIFT/ORB descriptors).
