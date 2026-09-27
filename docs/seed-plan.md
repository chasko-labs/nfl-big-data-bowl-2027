# seed plan

what local data we keep, in what order, and why. decided 2026-09-27
from the deep-research seed audit, updated for the no-kaggle path
(bryan has no kaggle account, so kaggle is out entirely). `data/` is
gitignored; this doc is the record of what should be in it.

## state

- [x] 2024 full set (sumersports mirror, 136 games / 12,486 plays)
- [x] 2025 full set (huggingface mirror, 136 games / 16,124 plays)
- [x] 2019 sample (official repo, 1 game by design)
- [x] nflverse 2017 + 2022 pbp (100% join verified)
- [ ] 2023/2022/2021/2020/2026 tracking: no public mirrors exist

environment: 195gb free on /home, 46gb ram free for pandas. project
`.venv` has kaggle cli, pandas, pyarrow, huggingface_hub. working
set totals ~9.5gb.

## seeded: 2024 tackling (1.6gb)

clean modern layout (games/plays/players/tackles + tracking weeks
1-9) from SumerSports/SportsTrackingTransformer data-v1.0 (kaggle
removed the official release). validated:

- 136 games, 12,486 plays, 1,683 players, 17,426 tackles
- tracking cols: gameId playId nflId ... frameId x y s a dis o dir
  event
- every plays.gameId resolves in games.csv

## seeded: 2025 pre-snap (7.7gb)

from huggingface public mirror `ameau01/Big-Data-Bowl-2025` (no
auth needed). validated:

- 136 games, 16,124 plays (confirms the earlier weak-mirror claim)
- player_play.csv: 53 cols incl. inMotionAtBallSnap,
  shift/motionSinceLineset, wasRunningRoute, routeRan,
  pff_defensiveCoverageAssignment + matchup nflIds
- tracking adds a `frameType` col vs 2024 - handle in loaders

caution: 2024 and 2025 both cover weeks 1-9 2022 with different
play counts (12,486 vs 16,124). diff gameId sets before treating
them as one corpus.

## seeded: 2019 sample (60mb) + nflverse joins (38mb)

- 2019: shallow clone of nfl-football-ops/big-data-bowl. the league
  intentionally ships only one game of tracking + full schema docs;
  the 91-game set was pulled. reference only.
- nflverse pbp 2017 + 2022 parquet join bowl plays 100% on
  (old_game_id, play_id). gotcha: play_id reads as float, cast to
  int before joining.

## explicitly not seeded (dead ends documented)

- 2026/2023/2022/2021/2020 tracking: checked huggingface (one hit:
  the 2025 mirror, nothing else), github releases and entry repos
  (all kb-sized, no vendored data), archive.org uploads (zero),
  wayback machine (only kaggle's 5.5kb js shell page archived -
  data files were auth-walled, never archivable). nothing public.
- a kaggle account would unlock all of the above. revisit if one
  ever exists; slugs are in this file's git history.
