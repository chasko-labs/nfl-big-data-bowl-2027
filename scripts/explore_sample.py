"""Explore one sample play: join tracking + games/plays/players, plot a frame.

usage:
    uv run python scripts/explore_sample.py [--data samples/2024]
    BDB_DATA=data/2024 uv run python scripts/explore_sample.py

reads columns present in the files at runtime (2024/2025 schemas drift).
plot lands in data/scratch/.
"""

import argparse
import os
import pathlib
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRATCH = ROOT / "data" / "scratch"

# field meanings from docs/data-guide.md (2024 community mirror).
# absent cols (e.g. frameType in 2024) are skipped at print time.
GLOSSARY = {
    "x": "long-axis coord, 0-120 yards",
    "y": "short-axis coord, 0-53.3 yards",
    "s": "speed, yards/sec",
    "a": "acceleration, yards/sec^2",
    "dis": "distance traveled since prior frame",
    "o": "body orientation, 0-360 deg",
    "dir": "motion direction angle, 0-360 deg",
    "event": "tags: snap, pass_arrived, catch, tackle, etc",
    "frameId": "frame counter, starts at 1",
    "nflId": "player id; NaN means the ball",
    "frameType": "play phase tag (2025 only, absent in 2024)",
}


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


def resolve_data(arg):
    base = pathlib.Path(arg or os.environ.get("BDB_DATA", "samples/2024"))
    if not base.is_absolute():
        base = ROOT / base
    sample = base / "tracking_sample.csv"
    if sample.exists():
        return base, sample, True
    weeks = sorted(base.glob("tracking_week_*.csv"))
    if not weeks:
        die_missing(base, "tracking dir (no tracking_sample.csv, no tracking_week_*.csv)")
    return base, weeks[0], False


def first_play(track_path, is_sample):
    if is_sample:
        pairs = pd.read_csv(track_path, usecols=["gameId", "playId"])
    else:
        # week files are ~1gb: scan keys only, chunked
        chunks = [
            c for c in pd.read_csv(track_path, usecols=["gameId", "playId"], chunksize=200_000)
        ]
        pairs = pd.concat(chunks, ignore_index=True)
    play = pairs.sort_values(["gameId", "playId"]).iloc[0]
    return int(play.gameId), int(play.playId)


def load_frames(track_path, is_sample, game, play):
    if is_sample:
        df = pd.read_csv(track_path)
        return df[(df.gameId == game) & (df.playId == play)]
    hits = []
    for chunk in pd.read_csv(track_path, chunksize=200_000):
        hit = chunk[(chunk.gameId == game) & (chunk.playId == play)]
        if len(hit):
            hits.append(hit)
    return pd.concat(hits, ignore_index=True) if hits else pd.DataFrame()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=None, help="samples/2024, samples/2025, data/2024 ...")
    args = ap.parse_args()

    base, track_path, is_sample = resolve_data(args.data)
    for name in ["games.csv", "plays.csv", "players.csv"]:
        if not (base / name).exists():
            die_missing(base / name, name)

    game, play = first_play(track_path, is_sample)
    frames = load_frames(track_path, is_sample, game, play)
    if frames.empty:
        print(f"no frames for play {game}/{play} in {track_path}")
        sys.exit(1)

    plays = pd.read_csv(base / "plays.csv")
    games = pd.read_csv(base / "games.csv")
    players = pd.read_csv(base / "players.csv")

    # joins read keys present at runtime; nflId is float in tracking (NaN = ball)
    tr = frames.merge(plays, on=["gameId", "playId"], how="left", suffixes=("", "_play"))
    tr = tr.merge(games, on=["gameId"], how="left", suffixes=("", "_game"))
    key = tr["nflId"].dropna().astype("int64")
    pmap = players.set_index(players["nflId"].astype("int64")) if "nflId" in players.columns else None
    tr["position"] = tr["nflId"].map(
        lambda v: pmap.loc[int(v), "position"] if pd.notna(v) and pmap is not None and int(v) in pmap.index else ("ball" if pd.isna(v) else "?")
    )

    n_frames = tr["frameId"].nunique() if "frameId" in tr.columns else len(tr)
    n_players = tr["nflId"].nunique()
    print(f"play {game}/{play}: {len(tr)} rows, {n_frames} frames, {n_players} players + ball")

    # plot one frame: 22 dots + ball
    mid = sorted(tr["frameId"].unique())[len(tr["frameId"].unique()) // 2]
    f = tr[tr.frameId == mid]
    ball = f[f.nflId.isna()]
    men = f[f.nflId.notna()]
    fig, ax = plt.subplots(figsize=(10, 5))
    for club, g in men.groupby("club"):
        ax.scatter(g.x, g.y, label=str(club), s=40)
    if len(ball):
        ax.scatter(ball.x, ball.y, c="black", marker="x", s=80, label="ball")
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 53.3)
    ax.set_xlabel("x (yards)")
    ax.set_ylabel("y (yards)")
    ax.set_title(f"play {game}/{play} frame {mid}")
    ax.legend(markerscale=1.2, fontsize=8)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    out = SCRATCH / f"play_{game}_{play}_frame{mid}.png"
    fig.savefig(out, dpi=100)
    plt.close(fig)
    print(f"plot: {out.relative_to(ROOT)}")

    # frame-field glossary for the plotted frame
    print(f"--- frame {mid} field glossary ---")
    row = f.iloc[0]
    for col in f.columns:
        if col in GLOSSARY:
            print(f"  {col}={row[col]!r}: {GLOSSARY[col]}")


if __name__ == "__main__":
    main()
