"""Cut deterministic sample slices from local bowl data for git.

Samples = first 25 plays of week 1 (ordered by gameId, playId) + full
games/players metadata + sliced plays/tackles/player_play. Rerun any time:
    uv run python scripts/make_samples.py
"""

import pathlib

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
N_PLAYS = 25


def sample_year(year, extra_files):
    src = ROOT / "data" / str(year)
    dst = ROOT / "samples" / str(year)
    dst.mkdir(parents=True, exist_ok=True)

    plays = pd.read_csv(src / "plays.csv")
    week1_games = pd.read_csv(src / "tracking_week_1.csv", usecols=["gameId", "playId"]).drop_duplicates()
    # first N plays of week 1, deterministic order
    sample_pairs = (
        week1_games.merge(plays[["gameId", "playId"]], on=["gameId", "playId"])
        .sort_values(["gameId", "playId"])
        .head(N_PLAYS)
    )
    pairset = set(zip(sample_pairs.gameId, sample_pairs.playId))

    def subset(df):
        return df[df.apply(lambda r: (r.gameId, r.playId) in pairset, axis=1)]

    # full small metadata
    for f in ["games.csv", "players.csv"]:
        pd.read_csv(src / f).to_csv(dst / f, index=False)

    # sliced files
    plays_out = subset(plays)
    plays_out.to_csv(dst / "plays.csv", index=False)
    for f in extra_files:
        subset(pd.read_csv(src / f)).to_csv(dst / f, index=False)

    # tracking: all frames for sampled plays (chunked, week files are big)
    chunks = []
    for chunk in pd.read_csv(src / "tracking_week_1.csv", chunksize=200_000):
        hit = chunk[chunk.apply(lambda r: (r.gameId, r.playId) in pairset, axis=1)]
        if len(hit):
            chunks.append(hit)
    tracking = pd.concat(chunks, ignore_index=True)
    tracking.to_csv(dst / "tracking_sample.csv", index=False)

    print(f"== {year}: {len(plays_out)} plays, {len(tracking)} frames ==")
    for f in sorted(dst.iterdir()):
        print(f"  {f.name}: {f.stat().st_size / 1024:,.0f} KB")


if __name__ == "__main__":
    sample_year(2024, ["tackles.csv"])
    sample_year(2025, ["player_play.csv"])
