# Machine Learning · Group Projects 2026-27

Universitat Autònoma de Barcelona · *Aprenentatge Computacional*

This repository has everything you need to choose and start your group project: the
introduction slides, one folder per proposal with the problem and its data, and the rules
that apply to every project.

| | |
|---|---|
| **Groups** | 3 students |
| **Duration** | 4 weeks, with a follow-up session every week |
| **Weight** | 60% of the final grade |
| **Slides** | [`Projects-Introduction-2026-27.pdf`](Projects-Introduction-2026-27.pdf) |

## The proposals

| # | Project | The question that starts it | Data | Data in this repo? |
|---|---|---|---|---|
| 1 | [Will there be a Bicing bike?](01-bicing/) | Will this station have bikes in 30 minutes? | Open Data BCN, Bicing station status | Yes (2 months) |
| 2 | [Football analyst: the xG model](02-football-xg/) | What is the probability that this shot is a goal? | StatsBomb Open Data | Yes |
| 3 | [My phone knows what I'm doing](03-phone-activity/) | Can I recognise activity from a phone's accelerometer, on new people and phones? | UCI HAR + MotionSense | Download script |
| 4 | [What can I cook today?](04-recipe-search/) | I want cuisine X and I have these ingredients: which dishes can I make? | Food.com + What's Cooking (Kaggle) | Download script |
| 5 | [How much is this flat worth?](05-airbnb-bcn/) | What does a Barcelona Airbnb cost per night, and what makes it expensive? | Inside Airbnb, Barcelona | Yes (listings) |
| 6 | [What is this news story about?](06-catalan-news/) | What is this news item about, and which ones are similar? | TeCla (Projecte AINA) | Download script |
| 7 | [What's in this photo?](07-visual-bow/) | Can a model recognise what is in a photo without deep learning? | Indian Food (or Food-101, Oxford Buildings) | Download script |
| 8 | [Which game will I like?](08-steam-recommender/) | Which Steam game will I like? | Game Recommendations on Steam (Kaggle) | Yes (sample) |
| 9 | [What should I listen to next?](09-music-audio/) | What genre is this song, and which songs sound like it? | GTZAN (audio only) | Download script |

Each folder has a `README.md` with the problem, some open questions to get you thinking, a
description of the dataset and how to get it. **There is no step-by-step plan on purpose**:
deciding how to attack the problem is part of the project.

You can also **propose your own project**. Come and see us with: what the problem is, which
data you will use (it must already exist and be annotated: there is no time to collect or
label data in 4 weeks) and what your starting point is.

## What is valued: design decisions

The final product (a map, a search engine, a recommender, a demo) is there to make the
project fun. **What is graded is how you analyse your results and decide what to do next.**
Every week you will take at least one design decision, and you will present it with the same
structure:

1. **Hypothesis**: what you think and why.
2. **Experiment**: what you ran to check it (data, split, metric, baseline).
3. **Result**: the evidence (table, plot, examples of errors).
4. **Decision**: what you do next, and why the evidence supports it.

Keep all of them in a **decision log** in your repository's README (template:
[`DECISION_LOG_TEMPLATE.md`](DECISION_LOG_TEMPLATE.md)). A decision supported by a good
experiment is worth more than an extra point of accuracy.

### About AI assistants

You will use AI tools to write code, and that is fine: writing code is not what is graded.
What is graded is what no tool can do for you:

- **The problem**: state precisely which problem you are trying to solve at each step.
- **The approach**: how you propose to solve it, and why you expect it to work.
- **The evidence**: tables and plots that show whether it works, and **when it does not,
  why not**. A well-explained failure is a valid result.

Every member must be able to explain and defend any decision in the log, including the ones
another member ran.

## Weekly checkpoints

All projects share the same checkpoints, so every group is followed in the same way. Bring
clear questions and the evidence to answer them to each session.

| Week | What should be working at the follow-up session |
|---|---|
| 1 | Data loaded and understood, validation split defined, a baseline running. How you validate (split, main metric) and why. |
| 2 | At least two supervised models compared with a correct validation. |
| 3 | An improved model, plus the unsupervised or retrieval part of your project, with error analysis. |
| 4 | Test on out-of-distribution data (another period, dataset or domain) and the final product. |

Each week a different member presents the checkpoint, so all three of you present at least
once. In the final presentation, any member can be asked about a decision taken by another.

## What you deliver

Your group's GitHub repository is your report:

- Code that runs: notebooks or `.py` files, with instructions to reproduce your results.
- A `README.md` with the objective, where to get the data, the decision log, the results
  and a critical analysis of them: for each step, the problem, the proposed approach and the
  evidence (tables, plots) of whether it works and, if not, why.
- The requirements of your environment (`requirements.txt` or the exported conda `.yml`).
- **Do not upload the datasets** to your repository: link to them or to this repo.
- Commits spread over the 4 weeks and among the 3 members.

Plus a final presentation in class, where all members take part.

## Grading

| Component | Weight in the project grade | What is valued |
|---|---|---|
| Design decisions and evidence | 40% | Clear problem and hypothesis, a suitable experiment, a decision consistent with the evidence (decision log + weekly checkpoints) |
| Experimental rigour | 20% | Baseline, validation without leakage, error analysis |
| Presentation and final product | 15% | Clarity, and a product that works |
| Individual component | 15% | Individual questions about decisions taken by another member |
| Reproducibility | 10% | The code runs following your instructions, documentation, commits spread over time and members |

## Getting the data

```bash
git clone https://github.com/ramonbal/ml-projects-2026-27.git
```

- Small datasets with an open licence are already in each project's `data/` folder.
- The others come with a `download_data.py` script. Some of them use the Kaggle API:
  `pip install kaggle`, then in <https://www.kaggle.com/settings> click *Create New Token* and
  save `kaggle.json` in `~/.kaggle/` (Windows: `C:\Users\<you>\.kaggle\`).
- Everything is designed to fit in a laptop's memory and to work with `numpy`, `pandas`,
  `scikit-learn` and `matplotlib`. Some projects need one extra library (`librosa`,
  `opencv-python`, `folium`...), indicated in their README.
- Large downloads (GBs) are better kept **outside** synced folders such as OneDrive or Dropbox.

## Data licences

The data in this repository belongs to its owners and is redistributed under their licences
(CC BY 4.0, CC0, or the StatsBomb Open Data terms). Each project README states the source,
the licence and how to cite it. Datasets whose licence does not allow redistribution (Kaggle
competitions, GTZAN, TeCla...) are not included: use the download scripts.
