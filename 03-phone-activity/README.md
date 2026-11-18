# 3 · My phone knows what I'm doing

## The problem

Your phone can tell whether you are walking, climbing stairs or sitting, using only its
accelerometer and gyroscope. Train an activity recognition model on one dataset and then test
it on another one, recorded with **different people, a different phone and the phone in a
different place**. This is where you find out what "generalising" really means.

**Final product:** an activity classifier that still works with people and phones it has
never seen (and, optionally, a live demo with one of your phones).

## Questions to get you started

- If the same person appears in training and in test, what are you really measuring? How
  should you split the data?
- How do you turn a raw signal at 50 Hz into a fixed-size vector? Which window length, and
  which features (time domain, frequency domain)?
- The first dataset comes with 561 pre-computed features. Can you compute them on the second
  dataset? What happens if you cannot?
- Which activities get confused with each other, and why? What could you do about it?
- How much does performance drop on the second dataset, and which part of the pipeline is
  responsible?
- Without using the labels, do the activities appear as separate groups in the data?

Course topics that fit: kNN, logistic regression, SVM and kernels, random forests and
ensembles, Naive Bayes, clustering, cross-validation by groups.

## The data

Two public datasets. Download them with [`download_data.py`](download_data.py) (≈135 MB):

```bash
python download_data.py          # saves everything in ./data
```

### UCI HAR (training domain)

- <https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones>,
  licence **CC BY 4.0**.
- 30 people, Samsung Galaxy S II **on the waist**, accelerometer + gyroscope at 50 Hz.
- 10,299 windows of 2.56 s (128 readings, 50% overlap), already split 7,352 train / 2,947
  test by person.
- For each window: 561 pre-computed features (`X_*.txt`), label (`y_*.txt`), person
  (`subject_*.txt`) and the raw signals (`Inertial Signals/`).
- 6 classes: WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING.
- Cite: Anguita et al., *A Public Domain Dataset for Human Activity Recognition Using
  Smartphones*, ESANN 2013.

### MotionSense (test domain)

- <https://github.com/mmalekzadeh/motion-sense>, licence **ODbL**.
- 24 people, iPhone 6s **in the front pocket**, 50 Hz.
- 360 CSV files (one per person and trial), 1.41 M readings, in folders `dws_*`, `ups_*`,
  `wlk_*`, `jog_*`, `sit_*`, `std_*`.
- Columns: `attitude.roll/pitch/yaw`, `gravity.x/y/z`, `rotationRate.x/y/z`,
  `userAcceleration.x/y/z`.
- 6 classes: downstairs, upstairs, walking, jogging, sitting, standing.
- `data_subjects_info.csv`: `code, weight, height, age, gender` of each person.
- Cite: Malekzadeh et al., *Mobile Sensor Data Anonymization*, IoTDI 2019.

Look carefully at which activities, units and sensors the two datasets share before you
compare them.
