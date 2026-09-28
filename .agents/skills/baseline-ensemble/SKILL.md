# baseline-ensemble

frame-up features plus a lasso-logistic baseline, then ensembles.

## when to use

any modeling pass: start here for a comparable number before trying
heavier models. one seed + one config per output dir, always.

## procedure

```
uv run python scripts/features_frame_up.py --data data/2024
uv run python scripts/baseline_lasso.py --data data/2024
```

- features: one row per (gameId, playId, side=off/def). s/a/dis
  means, s_max, distance-to-line mean/min vs ball-x-at-snap,
  formation dummies, first_down label (playResult, yardsGained
  fallback; outcome cols never leak into features). sink:
  `data/scratch/<tag>_features.parquet`.
- baseline: l1 logistic (C=1.0, seed=7), GroupKFold on gameId+playId
  so a play never splits across folds. reports base rate, per-fold
  accuracy, mean +- standard error. sink:
  `data/scratch/baseline_<tag>/metrics.csv + config.txt`.
- cols come from headers at runtime; missing data/ exits 1 with the
  re-seed pointer.

## next rung

xgboost / lightgbm / catboost on the same feature parquet and folds,
optuna tuning, one config per new output dir. lightgbm first: picked
over xgboost for speed and memory on this shape before.

## verify

```
uv run python scripts/baseline_lasso.py   # samples: acc ~0.70 +- 0.11
```

## scripts

`scripts/features_frame_up.py`, `scripts/baseline_lasso.py`
