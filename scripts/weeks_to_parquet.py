"""Convert weekly tracking csvs to per-play parquet, chunked.

usage:
    uv run python scripts/weeks_to_parquet.py [--data samples/2024]
    BDB_DATA=data/2024 uv run python scripts/weeks_to_parquet.py

pattern mirrors scripts/make_samples.py: pandas + pathlib, chunksize
reads. aggregates each tracking file to one row per (gameId, playId,
nflId) with mean motion cols + frame count, sinks parquet to
data/scratch/. raw csvs are read-only, never written.
"""

import argparse
import os
import pathlib
import sys

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRATCH = ROOT / "data" / "scratch"
CHUNKSIZE = 200_000
KEYS = ["gameId", "playId", "nflId"]
# candidate motion cols: only those present in the file are used,
# so 2024 and 2025 schemas both work.
MOTION_CANDIDATES = ["s", "a", "dis", "x", "y"]


def die_missing(path, kind):
    if str(path).startswith(str(ROOT / "data")):
        print(f"missing {kind}: {path}")
        print("data/ is gitignored and not seeded here. re-seed it:")
        print("  see data/README.md (sumersports mirror, huggingface, nflverse)")
        print("or run against the in-git slice: --data samples/2024")
    else:
        print(f"missing {kind}: {path}")
        print("regenerate samples with: uv run python scripts/make_samples.py")
    sys.exit(1)


def sources(base):
    sample = base / "tracking_sample.csv"
    if sample.exists():
        return [sample]
    weeks = sorted(base.glob("tracking_week_*.csv"))
    if not weeks:
        die_missing(base, "tracking files (no tracking_sample.csv, no tracking_week_*.csv)")
    return weeks


def convert_one(src, base):
    header = pd.read_csv(src, nrows=0).columns.tolist()
    keys = [k for k in KEYS if k in header]
    if len(keys) < 2:
        print(f"skip {src.name}: no gameId/playId keys in header")
        return None
    motion = [c for c in MOTION_CANDIDATES if c in header]
    if not motion:
        print(f"skip {src.name}: no motion cols in header")
        return None

    # two-stage aggregate: per-chunk sums + counts, then combine.
    # nflId NaN (ball) kept as its own group via dropna=False.
    lvl = list(range(len(keys)))
    sum_parts, n_parts, max_parts = [], [], []
    for chunk in pd.read_csv(src, usecols=keys + motion, chunksize=CHUNKSIZE):
        g = chunk.groupby(keys, dropna=False)
        sum_parts.append(g[motion].sum())
        n_parts.append(g.size().rename("n"))
        if "s" in motion:
            max_parts.append(g["s"].max().rename("s"))
    sums = pd.concat(sum_parts).groupby(level=lvl).sum()
    counts = pd.concat(n_parts).groupby(level=lvl).sum()
    out = sums.div(counts, axis=0).add_suffix("_mean")
    out["n_frames"] = counts
    if max_parts:
        out["s_max"] = pd.concat(max_parts).groupby(level=lvl).max()
    out = out.reset_index()

    SCRATCH.mkdir(parents=True, exist_ok=True)
    dst = SCRATCH / f"{base.name}_{src.stem}.parquet"
    out.to_parquet(dst, index=False)
    print(f"{src.name} -> {dst.relative_to(ROOT)}: {len(out)} rows, {len(out.columns)} cols")
    return dst


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=None, help="samples/2024, samples/2025, data/2024 ...")
    args = ap.parse_args()

    base = pathlib.Path(args.data or os.environ.get("BDB_DATA", "samples/2024"))
    if not base.is_absolute():
        base = ROOT / base
    if not base.exists():
        die_missing(base, "tracking dir")
    for src in sources(base):
        convert_one(src, base)


if __name__ == "__main__":
    main()
