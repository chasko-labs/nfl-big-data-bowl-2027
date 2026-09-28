# join-and-slice

join tracking to games/plays/players and cut deterministic play slices.

## when to use

exploring one play end to end, or cutting a new runnable sample slice
from full weeks. canonical keys: games on gameId, plays on
gameId+playId, players on nflId (float in tracking, NaN = ball).

## procedure

slice pattern (from `scripts/make_samples.py`): first 25 plays of week
1 ordered by (gameId, playId), all frames kept, games/players full,
plays/tackles sliced to the pair set. chunked key scan for big weeks:

```python
pairs = pd.concat(
    pd.read_csv(src, usecols=["gameId", "playId"], chunksize=200_000)
).sort_values(["gameId", "playId"]).head(25)
```

player join: tracking nflId is float (NaN = ball), players nflId is
int. map via `int(v)` with a NaN guard, or merge on
`tracking.nflId.astype("Int64")`.

## nflverse join (worked)

bowl plays join nflverse play-by-play 100% on (old_game_id, play_id).
play_id reads as float in parquet, so cast first:

```python
pbp = pd.read_parquet("data/nflverse/play_by_play_2022.parquet")
pbp["play_id"] = pbp["play_id"].astype("int64")       # reads as float
pbp["old_game_id"] = pbp["old_game_id"].astype("int64")  # reads as str
m = plays.merge(pbp, left_on=["gameId", "playId"],
                right_on=["old_game_id", "play_id"], how="left")
```

bowl gameId == nflverse old_game_id (e.g. 2022090800). unmatched rows
after the cast mean a wrong season file, not a key problem.

## verify

```
uv run python scripts/explore_sample.py   # joins + plots one play
```

## scripts

`scripts/explore_sample.py`, `scripts/make_samples.py`
