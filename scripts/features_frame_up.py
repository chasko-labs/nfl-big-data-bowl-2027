"""Build play-level features from frame tracking, frame level up.

usage:
    uv run python scripts/features_frame_up.py [--data samples/2024]
    BDB_DATA=data/2024 uv run python scripts/features_frame_up.py

grain: one row per (gameId, playId, side) with side = off/def.
motion cols (s/a/dis) and keys are picked from the file header at
runtime, so 2024/2025 schemas both work. formation context and the
label come from plays.csv. sink: data/scratch/<tag>_features.parquet.
"""

import argparse
import os
import pathlib
import sys

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRATCH = ROOT / "data" / "scratch"
CHUNKSIZE = 200_000
SNAP_EVENTS = ("ball_snap", "snap")


def die(msg):
    print(msg)
    sys.exit(1)


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


def snap_x_per_play(src, cols):
    """ball x at snap per (gameId, playId); fallback = ball x at first frame."""
    if "nflId" not in cols or "x" not in cols:
        return {}
    use = [c for c in ["gameId", "playId", "frameId", "nflId", "x", "event"] if c in cols]
    snaps, firsts = [], []
    for chunk in pd.read_csv(src, usecols=use, chunksize=CHUNKSIZE):
        ball = chunk[chunk.nflId.isna()]
        if not len(ball):
            continue
        if "event" in use:
            hit = ball[ball.event.isin(SNAP_EVENTS)]
            if len(hit):
                snaps.append(hit[["gameId", "playId", "x"]])
        firsts.append(ball.sort_values("frameId").drop_duplicates(["gameId", "playId"])[["gameId", "playId", "x"]])
    out = {}
    if firsts:
        base_map = pd.concat(firsts).drop_duplicates(["gameId", "playId"])
        out = {(r.gameId, r.playId): r.x for r in base_map.itertuples()}
    if snaps:
        snap_map = pd.concat(snaps).drop_duplicates(["gameId", "playId"])
        out.update({(r.gameId, r.playId): r.x for r in snap_map.itertuples()})
    return out


def convert(base, srcs, tag):
    header = pd.read_csv(srcs[0], nrows=0).columns.tolist()
    motion = [c for c in ["s", "a", "dis"] if c in header]
    if "gameId" not in header or "playId" not in header or "club" not in header:
        die(f"{srcs[0].name}: header lacks gameId/playId/club, cols={header}")
    if not (base / "plays.csv").exists():
        die_missing(base / "plays.csv", "plays.csv")
    plays = pd.read_csv(base / "plays.csv")
    if "possessionTeam" not in plays.columns or "defensiveTeam" not in plays.columns:
        die("plays.csv lacks possessionTeam/defensiveTeam, cannot assign off/def sides")

    teams = plays.set_index(["gameId", "playId"])[["possessionTeam", "defensiveTeam"]]
    off_of = teams["possessionTeam"].to_dict()
    def_of = teams["defensiveTeam"].to_dict()
    los = snap_x_per_play(srcs[0] if len(srcs) == 1 else srcs[0], header)
    # multi-week inputs share one snap map only per file; rebuild per file below
    lvl = [0, 1, 2]
    sum_parts, n_parts, max_parts, dmin_parts, ball_parts = [], [], [], [], []
    for src in srcs:
        if len(srcs) > 1:
            los = snap_x_per_play(src, header)
        for chunk in pd.read_csv(src, chunksize=CHUNKSIZE):
            chunk = chunk[chunk.nflId.notna()]  # drop ball rows from side agg
            if not len(chunk):
                continue
            key = list(zip(chunk.gameId, chunk.playId))
            poss = [off_of.get(k) for k in key]
            defe = [def_of.get(k) for k in key]
            df = chunk.assign(poss=poss, defe=defe)
            df["side"] = "other"
            df.loc[df.club == df.poss, "side"] = "off"
            df.loc[(df.side == "other") & (df.club == df.defe), "side"] = "def"
            df = df[df.side.isin(["off", "def"])]
            if not len(df):
                continue
            if los and "x" in df.columns:
                df = df.assign(
                    dline=df.apply(lambda r: abs(r.x - los.get((r.gameId, r.playId), r.x)), axis=1)
                )
            g = df.groupby(["gameId", "playId", "side"])
            use = [c for c in motion if c in df.columns]
            if "dline" in df.columns:
                use = use + ["dline"]
            if use:
                sum_parts.append(g[use].sum())
            n_parts.append(g.size().rename("n"))
            if "s" in df.columns:
                max_parts.append(g["s"].max().rename("s"))
            if "dline" in df.columns:
                dmin_parts.append(g["dline"].min().rename("dline"))
            nmen = df.drop_duplicates(["gameId", "playId", "side", "nflId"]).groupby(
                ["gameId", "playId", "side"]
            ).size().rename("men")
            ball_parts.append(nmen)

    if not n_parts:
        die(f"no off/def player rows found in {[s.name for s in srcs]}")
    counts = pd.concat(n_parts).groupby(level=lvl).sum()
    feat = pd.DataFrame({"n_frames": counts})
    if sum_parts:
        sums = pd.concat(sum_parts).groupby(level=lvl).sum()
        means = sums.div(counts, axis=0).add_suffix("_mean")
        feat = feat.join(means)
    if max_parts:
        feat["s_max"] = pd.concat(max_parts).groupby(level=lvl).max()
    if dmin_parts:
        feat["dline_min"] = pd.concat(dmin_parts).groupby(level=lvl).min()
    if ball_parts:
        feat["n_men"] = pd.concat(ball_parts).groupby(level=lvl).max()
    feat = feat.reset_index()

    # play context: formation encodings + down/distance + label, from runtime cols
    pcols = plays.columns.tolist()
    ctx_cols = [c for c in ["gameId", "playId", "down", "yardsToGo", "defendersInTheBox",
                            "offenseFormation", "playResult", "yardsGained"] if c in pcols]
    ctx = plays[ctx_cols].drop_duplicates(["gameId", "playId"]).copy()
    if "offenseFormation" in ctx.columns:
        dummies = pd.get_dummies(ctx["offenseFormation"].fillna("unknown"), prefix="form", dummy_na=False)
        dummies.columns = [c.lower().replace(" ", "_") for c in dummies.columns]
        ctx = pd.concat([ctx.drop(columns=["offenseFormation"]), dummies], axis=1)
    if "playResult" in ctx.columns and "yardsToGo" in ctx.columns:
        ctx["first_down"] = (ctx.playResult >= ctx.yardsToGo).astype(int)
    elif "yardsGained" in ctx.columns and "yardsToGo" in ctx.columns:
        ctx["first_down"] = (ctx.yardsGained >= ctx.yardsToGo).astype(int)
    else:
        die("plays.csv lacks playResult/yardsGained + yardsToGo, cannot build first_down label")
    # outcome cols are label sources: never features
    ctx = ctx.drop(columns=[c for c in ["playResult", "yardsGained"] if c in ctx.columns])
    feat = feat.merge(ctx, on=["gameId", "playId"], how="left")

    SCRATCH.mkdir(parents=True, exist_ok=True)
    dst = SCRATCH / f"{tag}_features.parquet"
    feat.to_parquet(dst, index=False)
    base_rate = feat.drop_duplicates(["gameId", "playId"])["first_down"].mean()
    print(f"{tag}: {len(feat)} side-rows, {len(feat.columns)} cols -> {dst.relative_to(ROOT)}")
    print(f"  base first-down rate: {base_rate:.3f}")
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
    convert(base, sources(base), base.name)


if __name__ == "__main__":
    main()
