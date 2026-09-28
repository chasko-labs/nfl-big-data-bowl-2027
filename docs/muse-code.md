# muse code for bowl prep: a participant's answer

a participant asked: with limited experience at this data scale, is
muse code worth using while researching how to manipulate the data?
short answer: yes. what follows is the recommendation, the learning
path, and exactly which capability helps at each step. bracketed
numbers are sources in [references](references.md).

companion guide (the tool itself, 0-100):
https://github.com/heraldstack/muse-code-pro [66].

## why yes, concretely

1. the scale is real but tractable, and that is exactly where a
   coding assistant earns its keep. weekly tracking files run ~1.5gb
   each [59]; the 2024 set is 280mb compressed, 1.6gb uncompressed
   [58]; one 2025 mirror reports ~7.7gb of tracking total [25]. all
   of it is 10-frames-per-second csv [46]. the beginner failure mode
   is loading all of it into memory at once. muse code writes the
   chunked reads, the per-week loops, and the parquet conversions
   for you, and explains each line when you ask.
2. winning pipelines are code-heavy iteration loops, not one clever
   model. public entries show the shape: gradient-boosted trees
   (lightgbm picked over xgboost for speed and memory [60]),
   xgboost / lightgbm / catboost ensembles with group-by-play folds
   and optuna tuning [61], frame-by-frame convnets for tackle
   probability [62], and hand-built features from speed, accel, and
   distance to the line [63]. every one of those rewards fast,
   repeatable edit-run-plot cycles - the thing an agentic cli
   automates.
3. ai-assisted coding is mainstream practice now, including on
   kaggle-style work. stack overflow's 2025 survey cohort using ai
   agents reported 81.7% chatgpt, 67.9% copilot, 40.8% claude code
   use [65] (general developers, not kaggle-only - no kaggle-only
   assistant survey was found). the contest still grades your
   football thinking, not your tooling: judges are team analysts
   who know more football than you (see [craft](craft.md)), so use
   the assistant for velocity and keep your own judgment on the
   question being asked.

## 0-to-competing learning path

### step 1: understand the data (days 1-3)

goal: open one week of tracking, join it to games/plays/players,
and plot one play. start from [data-guide](data-guide.md), then
the `samples/` slices and `notebooks/` starters in this repo.

muse mapping: interactive pairing (`muse` tui). ask it to narrate
each column as it touches it, and to stop at anything that
contradicts the year's data dictionary - schemas drift year to
year, and mirrors are not the dictionary (see data-guide gaps).

exit check: you can say what x, y, s, a, dis, o, dir, event mean
for one frame of one play, and your plot shows 22 dots + a ball.

### step 2: manipulate at scale (days 4-10)

goal: process all weeks without melting your machine. the skills
are chunked reads (pandas chunksize or polars scan + sink),
per-week aggregation loops, and converting csv weeks to parquet
once so every later run is 10x faster.

muse mapping: `muse exec` for batch exploration - one headless
prompt per question ("mean defender speed by week, all weeks,
write csv + png"), run overnight across weeks. save what works as
a project skill (`.agents/skills/<name>/SKILL.md`: procedure +
script), so step-3 you inherits step-2 you. the companion guide's
sections 40 (exec) and 50 (skills) are the manual [66].

exit check: a one-command script rebuilds every intermediate file
from raw csvs. disk budget: plan for ~2gb per weekly file
uncompressed [58][59].

### step 3: feature pipelines (days 11-20)

goal: frame-level features, aggregated to play-level rows the way
the league itself builds these stats (per-player features, then a
play stat - see data-guide reference models). mirror the public
entry patterns: speed/accel/distance features [63], formation
encodings, then a simple lasso-logistic baseline before anything
fancy (yurko's discipline, [craft](craft.md)).

muse mapping: sandbox + permissions for safe iteration. let the
agent run profiling and plotting freely, but keep writes scoped:
raw data read-only, outputs to a scratch dir. the companion
guide's section 70 (sandbox, permissions) is the setup [66].

exit check: baseline with cross-validated accuracy, standard
errors, and base rates next to it. no baseline, no step 4.

### step 4: model iterations (days 21+)

goal: boosted-tree ensembles with group-by-play folds [61], tuned
with optuna, compared honestly against the step-3 baseline. keep
every run reproducible: one seed, one config, one output dir.

muse mapping: local review before metered spend. draft and review
loops run against the free local delegate (glimmer,
no per-token api spend) and only the kept runs go to paid apis or
burn kaggle's weekly gpu quota (30 gpu hrs/wk on the free tier
[64]) - so prototype features locally, submit from kaggle. the
companion guide's section 90 (glimmer) is the setup [66].

exit check: an ensemble that beats the baseline under grouped cv,
with a one-paragraph honest limitations note (patton tip 14,
[craft](craft.md)).

## what muse code does not do for you

- football judgment. graders do this nights and weekends and know
  the game cold - answer the prompt, don't solve all of football
  ([craft](craft.md)).
- the current year's data dictionary. fetch the real one from
  kaggle at entry time; mirrors (including this repo) lag it.
- your writeup. half-assed explanations never get through, and a
  proofread by a human friend is still easy points ([craft](craft.md)).

## if you only do three things

1. `samples/` + one `muse exec` prompt per question, batched.
2. one skill file capturing your scaling pattern (chunk, parquet,
   loop).
3. baseline with base rates before any ensemble.
