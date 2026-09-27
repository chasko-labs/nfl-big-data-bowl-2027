# data

tracking data lives here. everything under this dir is gitignored -
the files are gigabytes. no kaggle account needed: every set below
came from a public mirror.

## what is seeded

- `2024/` - full tackling set (games/plays/players/tackles +
  tracking weeks 1-9, ~1.6gb). source: sumersports mirror release
  (kaggle removed the official files). validated: 136 games,
  12,486 plays, joins pass.
- `2025/` - full pre-snap set (games/players/plays/player_play +
  tracking weeks 1-9, ~7.7gb). source: huggingface public mirror
  `ameau01/Big-Data-Bowl-2025`. validated: 136 games, 16,124
  plays, joins pass. player_play has 53 cols including the
  pre-snap gold (inMotionAtBallSnap, shift/motionSinceLineset,
  routeRan, pff coverage assignments).
- `2019/` - sample only: the official repo (shallow clone, ~60mb)
  intentionally ships just one game of tracking + full schema docs.
  the 91-game set was pulled after the contest.
- `nflverse/` - play-by-play parquet for 2017 + 2022 (~38mb) from
  nflverse-data releases. joins bowl plays 100% on
  (old_game_id, play_id) - cast play_id to int first, it reads as
  float.

total: ~9.5gb. 195gb free, fits comfortably.

## environment

project venv holds the tooling:

```
source .venv/bin/activate
# has: kaggle cli, pandas, pyarrow, huggingface_hub
```

## re-seeding (if data/ is ever wiped)

```
# 2024 via sumersports mirror
gh release download data-v1.0 \
  -R SumerSports/SportsTrackingTransformer \
  -p "nfl-big-data-bowl-2024.zip" -D data/2024 --clobber
unzip -o data/2024/nfl-big-data-bowl-2024.zip -d data/2024-tmp/
mv data/2024-tmp/2024/*.csv data/2024/ && rm -rf data/2024-tmp

# 2025 via huggingface (no auth needed, public)
.venv/bin/hf download ameau01/Big-Data-Bowl-2025 \
  --repo-type dataset --local-dir data/2025-hf
mv data/2025-hf/big-data-bowl-data/*.csv data/2025/ && rm -rf data/2025-hf

# 2019 sample via official repo (shallow)
git clone --depth 1 https://github.com/nfl-football-ops/big-data-bowl.git data/2019/repo

# nflverse join seasons
gh release download pbp -R nflverse/nflverse-data \
  -p "play_by_play_2017.parquet" -p "play_by_play_2022.parquet" \
  -D data/nflverse --clobber
```

## not available without kaggle

2026 (prediction + analytics), 2023, 2022, 2021, 2020 tracking:
no public mirrors found (checked huggingface, github releases,
archive.org, wayback machine - the wayback has only kaggle's js
shell page, no data files were ever archivable behind auth).
if a kaggle account ever exists, the slugs are in git history of
this file - until then, 2024 + 2025 + nflverse is the working set.

see `docs/seed-plan.md` for phasing and `docs/data-guide.md` for schema.
