# samples (ships in git)

runnable slices of the bowl data so a fresh clone can demo without
the 9.5gb download. each year = first 25 plays of week 1 (ordered
by gameId, playId) with all frames, plus full games/players
metadata and sliced plays/tackles/player_play. tracking plays ==
plays exactly (verified at generation).

## contents (~14mb)

- `2024/` - games, players, plays, tackles, tracking_sample
  (25 plays, 19,113 frames, ~2.4mb)
- `2025/` - games, players, plays, player_play, tracking_sample
  (25 plays, 92,069 frames, ~11.7mb)

2025 runs more frames per play (pre-snap windows included).

## provenance

- 2024 source: SumerSports/SportsTrackingTransformer data-v1.0
  (kaggle removed the official release)
- 2025 source: huggingface `ameau01/Big-Data-Bowl-2025`
- full sets live in `data/` (gitignored) - see `data/README.md`

## regenerate

```
uv run python scripts/make_samples.py
```

deterministic: same inputs, same slices. bump N_PLAYS in the
script if the talk needs a bigger slice.
