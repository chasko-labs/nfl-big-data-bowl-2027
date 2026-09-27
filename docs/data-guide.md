# data guide

what the tracking data is, what it looks like, and how past bowls
shipped it. bracketed numbers are sources in [references](references.md).

## capture

- rfid tags in shoulder pads (players), officials, pylons, chains, and
  the ball. zebra + wilson hardware, aws pipeline [46].
- location, speed, distance, acceleration at 10 frames per second [46].
- aws turns 500m+ next gen stats data points per season into stats [52].

## tracking fields

field semantics below come from a 2024 community mirror [43], not an
official dictionary - confirm against the current year's data
dictionary before modeling.

| field                  | meaning                                                |
| ---------------------- | ------------------------------------------------------ |
| x                      | long-axis coord, 0-120 yards                           |
| y                      | short-axis coord, 0-53.3 yards                         |
| s                      | speed, yards/sec                                       |
| a                      | acceleration, yards/sec^2                              |
| dis                    | distance traveled since prior frame                    |
| o                      | body orientation, 0-360 deg                            |
| dir                    | motion direction angle, 0-360 deg                      |
| event                  | tags: snap, release, catch, tackle, etc                |
| frameId                | frame counter, starts at 1                             |
| nflId                  | player id; NA means the ball                           |
| frameType              | play phase tag (2025 only, absent in 2024)             |
| absoluteYardlineNumber | tracking coord 11-109, flips with drive direction [44] |

keys and joins: gameId, gameId+playId, nflId. joins to nflverse via
old_game_id / play_id [43].

## per-year file layouts

- 2019: per-game tracking csvs on github [3].
- 2020: train/test split by season (2017-18 / 2019 wks 13-17) [5].
- 2021: 20 csvs, ~2.17gb, 2018 passes [11].
- 2022: 5 csv groups including pff scouting [15].
- 2023: games/players/plays/pffscoutingdata + weeks 1-8 tracking,
  ~1.5gb per weekly csv [44].
- 2024: games/plays/players/tackles + tracking weeks 1-9 [26b][43].
- 2025: weeks 1-9 2022 again (overlap with 2024 unresolved),
  16,124 plays / 136 games confirmed from seeded data [25].
  player_play.csv verified: 53 cols incl. inMotionAtBallSnap,
  shift/motionSinceLineset, wasRunningRoute, routeRan,
  pff_defensiveCoverageAssignment + matchup nflIds.
- 2026: 49 files, weekly train csvs, test through an eval api. train
  2023-24, scored vs 2025 weeks 14-18 [30][33]. ~18,009 pass plays
  per a preprint [35].

expect the 2027 layout to rhyme: games/players/plays + tracking_week
files + one topic-specific table (tackles, pffscoutingdata, ...).
always read the year's data dictionary first - schemas drift.

## reference models (how the league builds these)

- completion probability: 10 on-field measurements via sagemaker [49].
- tackle probability: 20 features x 11 defenders, trained 2018-22,
  tested 2023 [50].
- pressure probability: 4 ai models, 90k plays [42].
- the pattern: frame-level features, per-player models, aggregate to
  a play stat. winning entries mirror this shape.

## getting the data

see `data/README.md`. kaggle cli + accept the rules per competition.
2019 is github-only. budget disk: weekly tracking files run 1gb+.

## gaps to close

- no official nfl data dictionary found in any fetched source -
  everything is mirrors. grab the real one from kaggle at entry time.
- no pff scouting schema despite pff data in 2022/2023.
- no 2026 eval api mechanics documented outside kaggle.
- joins to nflverse verified 100%: (old_game_id, play_id), cast
  play_id to int first (reads as float).
