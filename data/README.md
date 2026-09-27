# data

tracking data lives here. everything under this dir is gitignored - the
files are gigabytes and kaggle requires each user to accept the competition
rules before downloading.

## get the kaggle cli

```
pip install kaggle
# put your kaggle.json api token at ~/.kaggle/kaggle.json (chmod 600)
```

## download a past bowl dataset

accept the rules on the competition page first (logged-in browser click),
then:

```
# 2026 movement prediction (train 2023-24, scored vs 2025 weeks 14-18)
kaggle competitions download -c nfl-big-data-bowl-2026 -p data/bdb-2026

# 2025 pre-snap motion (weeks 1-9 2022, 16k plays)
kaggle competitions download -c nfl-big-data-bowl-2025 -p data/bdb-2025

# 2024 tackling (weeks 1-9 2022 + tackles.csv)
kaggle competitions download -c nfl-big-data-bowl-2024 -p data/bdb-2024

# 2023 pass rush (2021 dropbacks + pff scouting)
kaggle competitions download -c nfl-big-data-bowl-2023 -p data/bdb-2023

# 2021 pass defense (2018 passes, ~2.2gb)
kaggle competitions download -c nfl-big-data-bowl-2021 -p data/bdb-2021

# 2020 rushing (2017-18 train, 2019 test)
kaggle competitions download -c nfl-big-data-bowl-2020 -p data/bdb-2020
```

2019 data is on github, not kaggle (per-game tracking csvs):
https://github.com/nfl-football-ops/big-data-bowl

## suggested layout

```
data/
  bdb-2026/
  bdb-2025/
  ...
  README.md (this file)
```

## size warnings

- 2023 weekly tracking csvs run ~1.5gb each
- 2021 full set is ~2.2gb across 20 csvs
- 2026 ships 49 files
- start with one week file + games/plays/players before loading everything

see `docs/data-guide.md` for the schema (fields, keys, joins).
