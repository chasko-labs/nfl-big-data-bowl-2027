# chunk-to-parquet

convert weekly bowl tracking csvs to per-play parquet without holding a
week in memory.

## when to use

weekly tracking files run ~1gb+ each. any prompt that touches
`data/2024/tracking_week_*.csv` (or 2025) directly should go through
this loop first; later runs read parquet and get much faster.

## procedure

```
uv run python scripts/weeks_to_parquet.py --data data/2024
```

- chunked pandas reads (`chunksize=200000`, same as
  `scripts/make_samples.py`), two-stage sum/count aggregate to one row
  per (gameId, playId, nflId) with mean motion cols + n_frames + s_max.
- sink: `data/scratch/<tag>_tracking_week_N.parquet`. raw csvs stay
  read-only; nothing writes csv.
- motion cols and keys come from the file header at runtime, so 2024
  (no frameType) and 2025 schemas both pass.
- default input is `samples/2024` (override with `--data` or
  `BDB_DATA`). missing data/ exits 1 with the re-seed pointer, never a
  traceback.

## verify

```
uv run python scripts/weeks_to_parquet.py   # samples: 550 rows out
```

## script

`scripts/weeks_to_parquet.py`
