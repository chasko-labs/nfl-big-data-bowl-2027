"""Lasso-logistic baseline on play-side features.

usage:
    uv run python scripts/baseline_lasso.py [--data samples/2024]
    BDB_DATA=data/2024 uv run python scripts/baseline_lasso.py

reads data/scratch/<tag>_features.parquet (run features_frame_up.py
first), fits one l1 logistic (C=1.0, seed=7) to first_down with
group-by-play folds (GroupKFold on gameId+playId, so the two side
rows of a play never split). reports base rate, per-fold accuracy,
and mean accuracy with standard error. one seed + one config per
output dir: data/scratch/baseline_<tag>/.
"""

import argparse
import os
import pathlib
import sys

import warnings

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold

warnings.filterwarnings("ignore", message="Inconsistent values.*", category=UserWarning)

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRATCH = ROOT / "data" / "scratch"
SEED = 7
C = 1.0
N_SPLITS = 5


def die(msg):
    print(msg)
    sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=None, help="samples/2024, samples/2025, data/2024 ...")
    args = ap.parse_args()

    base = pathlib.Path(args.data or os.environ.get("BDB_DATA", "samples/2024"))
    if not base.is_absolute():
        base = ROOT / base
    feat_path = SCRATCH / f"{base.name}_features.parquet"
    if not feat_path.exists():
        die(f"missing {feat_path.relative_to(ROOT)}: run features first:\n"
            f"  uv run python scripts/features_frame_up.py --data {base.name if base.is_absolute() else base.relative_to(ROOT)}")

    df = pd.read_parquet(feat_path)
    if "first_down" not in df.columns:
        die(f"{feat_path.name}: no first_down label col")
    y = df["first_down"].astype(int).to_numpy()
    groups = (df["gameId"].astype(str) + "_" + df["playId"].astype(str)).to_numpy()

    drop = {"gameId", "playId", "side", "first_down"}
    X = df.drop(columns=[c for c in drop if c in df.columns])
    X = pd.get_dummies(X, columns=[], dtype=float)  # already numeric; dummies prebuilt
    if "side" in df.columns:
        X = X.assign(side_off=(df["side"] == "off").astype(float))
    X = X.fillna(0).to_numpy(dtype=float)

    base_rate = y.mean()
    print(f"n={len(y)} plays-side rows, {len(set(groups))} plays, base rate={base_rate:.3f}")

    accs = []
    for fold, (tr, te) in enumerate(GroupKFold(n_splits=min(N_SPLITS, len(set(groups)))).split(X, y, groups)):
        clf = LogisticRegression(penalty="l1", solver="liblinear", C=C, random_state=SEED)
        clf.fit(X[tr], y[tr])
        acc = clf.score(X[te], y[te])
        accs.append(acc)
        print(f"  fold {fold}: acc={acc:.3f} (test plays={len(set(groups[te]))})")
    accs = np.array(accs)
    se = accs.std(ddof=1) / np.sqrt(len(accs)) if len(accs) > 1 else 0.0
    print(f"accuracy: {accs.mean():.3f} +- {se:.3f} (se, k={len(accs)})")

    outdir = SCRATCH / f"baseline_{base.name}"
    outdir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"fold": range(len(accs)), "accuracy": accs}).to_csv(outdir / "metrics.csv", index=False)
    (outdir / "config.txt").write_text(f"seed={SEED}\nC={C}\npenalty=l1\nbase_rate={base_rate:.4f}\n")
    print(f"wrote {outdir.relative_to(ROOT)}/metrics.csv + config.txt")


if __name__ == "__main__":
    main()
