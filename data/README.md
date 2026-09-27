# data

tracking data lives here. everything under this dir is gitignored - the
files are gigabytes and kaggle requires each user to accept the
competition rules before downloading.

## what is seeded already

- `2024/` - full 2024 tackling set from the sumersports mirror
  (kaggle removed the official release): games/plays/players/tackles
  - tracking weeks 1-9, ~1.6gb raw. validated: 136 games, 12,486
    plays, joins check out. source zip kept alongside the csvs.

## environment

project venv holds the tooling (kaggle cli, pandas):

```
source .venv/bin/activate
# or: uv run <cmd>
```

## kaggle auth (needed for everything except 2024)

1. sign in at kaggle.com in a browser
2. accept the rules on each competition page below (required before
   the api will serve files)
3. create an api token (account page) and save it:
   `~/.kaggle/kaggle.json`, chmod 600
4. verify: `.venv/bin/kaggle competitions files -c
nfl-big-data-bowl-2025`

## download past bowls (after auth)

```
# 2025 pre-snap (weeks 1-9 2022, ~7.7gb tracking - heaviest set)
kaggle competitions download -c nfl-big-data-bowl-2025 -p data/2025

# 2023 pass rush (2021 dropbacks + pff scouting, ~12gb est)
kaggle competitions download -c nfl-big-data-bowl-2023 -p data/2023

# 2026 is SPLIT into two competitions (no single slug):
kaggle competitions download -c nfl-big-data-bowl-2026-prediction -p data/2026-prediction
kaggle competitions download -c nfl-big-data-bowl-2026-analytics -p data/2026-analytics

# older / smaller:
kaggle competitions download -c nfl-big-data-bowl-2021 -p data/2021
kaggle competitions download -c nfl-big-data-bowl-2020 -p data/2020
```

2019 data is on github, not kaggle (per-game tracking csvs):
https://github.com/nfl-football-ops/big-data-bowl

2024 is NOT on kaggle (removed by host). if `data/2024/` is ever
missing, re-seed from the mirror:

```
gh release download data-v1.0 \
  -R SumerSports/SportsTrackingTransformer \
  -p "nfl-big-data-bowl-2024.zip" -D data/2024 --clobber
unzip -o data/2024/nfl-big-data-bowl-2024.zip -d data/2024-tmp/
mv data/2024-tmp/2024/*.csv data/2024/ && rm -rf data/2024-tmp
```

## layout

```
data/
  2024/          # seeded + validated (tackling)
  2025/          # needs kaggle auth
  2023/          # needs kaggle auth
  nflverse/      # optional join data (see seed plan)
  README.md (this file)
```

## size warnings

- 2025 weekly tracking runs 739-931mb per week (~7.7gb total)
- 2023 weekly tracking ~1.5gb per week
- start with one week file + games/plays/players before loading all

see `docs/seed-plan.md` for phasing and `docs/data-guide.md` for schema.
