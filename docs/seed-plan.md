# seed plan

what local data we keep, in what order, and why. decided 2026-09-27
from the deep-research seed audit. `data/` is gitignored; this doc is
the record of what should be in it.

## state

- [x] 2024 full set seeded (sumersports mirror, validated 136 games /
      12,486 plays, joins pass)
- [ ] kaggle auth (bryan browser clicks - see below)
- [ ] 2025 full set (~7.7gb)
- [ ] 2023 set (~12gb, optional)
- [ ] nflverse pbp (488mb, optional joins)

environment: 195gb free on /home, 46gb ram free for pandas. project
`.venv` has kaggle cli 2.2.4 + pandas. disk fits everything.

## phase 0 - done: 2024 smoke + full (1.6gb)

2024 tackling is the clean modern layout (games/plays/players/tackles

- tracking weeks 1-9) and the only set available without kaggle auth,
  because kaggle removed the official release. seeded from
  SumerSports/SportsTrackingTransformer data-v1.0 and validated:

* 136 games, 12,486 plays, 1,683 players, 17,426 tackles
* tracking cols match spec: gameId playId nflId ... frameId x y s a
  dis o dir event
* every plays.gameId resolves in games.csv

## phase 1 - after kaggle auth: 2025 full (~7.7gb)

2025 pre-snap is the other modern layout and the most relevant recent
tactics data: games/players/plays/player_play (51mb) + 9 tracking
weeks at 739-931mb each.

caution: 2024 and 2025 both claim weeks 1-9 2022 with different play
counts (12,486 vs 16,124). before treating them as one corpus, diff
gameId sets. do not assume they are the same plays.

## phase 2 - optional: 2023 + nflverse

- 2023 pass rush: games/players/plays/pffscoutingdata + weeks 1-8,
  ~1.5gb/week (~12gb). worth it only if 2027 touches the trenches
  (run blocking is candidate #3 in the forecast). naming conflict
  unresolved: weekN.csv vs tracking_week_N.csv - check the file
  list after auth.
- nflverse pbp 1999-2025 (488mb, 372 cols): joins bowl gameId/playId
  at 100% per community reports. pull if we need down/distance,
  epa, or roster context beyond the bowl files.

## explicitly not seeded

- 2026 prediction/analytics: 49 files, ~5m frames, but no per-file
  sizes, disputed analytics layout, eval-api mechanics undocumented
  outside kaggle. defer until authed file list + docs.
- 2022: no file names/sizes, pff schema undocumented. unplannable.
- 2021: season conflict (2019 vs 2018 across sources), older schema.
  low roi vs 2024/2025.
- 2020/2019: obsolete layouts, reference only.

## bryan action items (the only blockers)

1. kaggle.com sign-in + accept rules on: 2025, 2023,
   2026-prediction, 2026-analytics (2024 skipped - removed)
2. api token -> `~/.kaggle/kaggle.json`, chmod 600
3. say go - downloads + validation run from there
