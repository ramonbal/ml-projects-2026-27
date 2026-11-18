# 9 · A playlist from audio only

## The problem

Using **only the sound** (no metadata, no pre-computed features), classify the genre of a
song, group songs by how they sound, and recommend songs that sound like a given one. It is
the *bag of words* model applied to audio: the "words" are short fragments of sound.

**Final product:** a "songs that sound like this one" recommender, with a demo where you
listen to the recommendations.

## Questions to get you started

- How do you turn a 30-second waveform into something a classifier can use? What is a
  sensible baseline?
- A song is a sequence of short frames. How do you go from many frame descriptors to one
  vector per song? How many "audio words" do you need?
- This dataset has known problems: repeated clips, many clips by the same artist, some wrong
  labels. How can they inflate your results, and how would you split the data to avoid it?
- Which genres get confused? Listen to the misclassified clips: is the model wrong, or is the
  label debatable?
- If you cluster the songs without labels, do the groups make sense as playlists?
- How do you evaluate a recommender of similar songs?
- Does a model trained on this collection work on music from a different source?

Course topics that fit: bag of words (k-means vocabulary), Naive Bayes, logistic regression,
SVM, random forests and ensembles, clustering, retrieval metrics.

## The data

**GTZAN Genre Collection** (Tzanetakis & Cook, *Musical genre classification of audio
signals*, IEEE TSAP 2002). It is distributed for research only and has no open licence, so it
is not in this repository. Download it from Kaggle with
[`download_data.py`](download_data.py) (needs a Kaggle token, see the
[main README](../README.md#getting-the-data)); it keeps only the audio:

```bash
pip install kaggle
python download_data.py          # ./data/genres_original/<genre>/*.wav, ~1.3 GB
```

- Kaggle mirror: <https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification>.
  The mirror also contains CSV files with pre-computed features and spectrogram images:
  **this project works from the audio**, so the script discards them.
- 1,000 clips of ~30 s, **10 genres × 100**: blues, classical, country, disco, hiphop, jazz,
  metal, pop, reggae, rock.
- WAV, 16-bit PCM, **mono, 22,050 Hz**, 1.3 MB per clip.
- **`jazz/jazz.00054.wav` is corrupt** (it cannot be opened): skip it, 999 usable clips.
- Known issues: B. L. Sturm, *The GTZAN dataset: Its contents, its faults, their effects on
  evaluation, and its future use*, 2013 (arXiv:1306.1461). Worth reading before you choose
  how to split the data.

```python
import librosa
y, sr = librosa.load("data/genres_original/blues/blues.00000.wav", sr=None)   # sr = 22050
```

**Optional out-of-distribution test:** [`download_fma_subset.py`](download_fma_subset.py)
downloads the Hip-Hop, Pop and Rock clips of **FMA-small** (Free Music Archive,
<https://github.com/mdeff/fma>, Creative Commons licences per track): 1,000 clips of 30 s per
genre, MP3 at 44.1 kHz, plus a metadata CSV with artist and licence. It needs a temporary
download of ~7.2 GB.

```bash
pip install pandas
python download_fma_subset.py data/fma_subset /path/to/temp
```

Extra libraries: `librosa` (audio features), `soundfile`.
