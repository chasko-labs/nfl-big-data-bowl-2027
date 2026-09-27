# bowl history 2019-2026

every edition: topic, dataset, winners, and what escaped to tv.
bracketed numbers are sources in [references](references.md).

## 2019 - statistical innovations (open theme)

the inaugural bowl, run with cmu. open-ended call for statistical
innovations in football [1].

- dataset: 91 games across the first 6 weeks of 2017 [2]. shipped as
  per-game tracking csvs on github [3].
- winners: open division nate sterken with routenet (route combination
  analysis) [4]; college division a simon fraser team (chu, reyers, wu,
  thomson) [2].
- tv lineage: none found. no 2019 metric is documented reaching broadcast
  or next gen stats.
- gaps: no competition platform url, no documented judging criteria, prize
  pool, or dates found.

## 2020 - rushing yards at handoff

first kaggle edition and the template-setter: predict rushing yards at the
moment of handoff [5].

- dataset: train on 2017-18, test on 2019 weeks 13-17 [5].
- platform + scoring: kaggle [7], scored by crps over a yards cdf
  (-99..99) [6].
- winners: dmitry gordeev and philip singer, team "the zoo" - predicted
  yards from handoff positions and velocities [5][9].
- tv lineage: the big one. the winning approach became expected rushing
  yards on next gen stats, debuting on national tv about six months later,
  and spun off rushing yards over expected plus 1st-down and td
  probability [9]. aws counts 75+ ml stats plus ryoe from the bowl
  pipeline overall [29].
- gaps: formal title of the zoo's kaggle writeup (kaggle renders via js);
  college division unmentioned anywhere found.

## 2021 - evaluating pass defense

theme: evaluate defensive performance on passing plays [10].

- dataset: 2018 passing plays, ~2.17gb across 20 csvs [11].
- platform: kaggle [8].
- winners: matthew peng, will richards, daniel walczak, and a teammate
  (stolaf-led team) - a man-vs-zone coverage model plus defender value
  metric [12].
- tv lineage: pass-defense work inspired coverage classification [13];
  later coverage responsibility stat built with ai/ml traces to bowl
  submissions [41]. (naming conflict between the two unresolved in
  sources - verify before citing.)
- gaps: college-division winner names; dataset facts come from github
  mirrors, not kaggle or nfl.

## 2022 - special teams

theme: special teams, using 2018-20 next gen stats plus pff scouting
data [14].

- dataset: 5 csv groups including pff scouting [15].
- winners: simon fraser again (ritchie, kumagai, moreau, cavan) - a
  punt-return optimal-path algorithm and the raye metric, with a shared
  kaggle notebook [16][45].
- tv lineage: none found reaching broadcast or next gen stats.
- gaps: winning-entry details (sportspro page unfetched); no pff scouting
  schema documented.

## 2023 - pass rush and pass block

theme: new pass-block and pass-rush analysis with next gen stats [17].

- dataset: 2021 qb dropbacks, sacks, scrambles, plus pff scouting [17].
  layout: games/players/plays/pffscoutingdata plus weeks 1-8 tracking,
  weekly tracking csvs ~1.5gb each [44].
- platform: kaggle [18]. tracks: coaching, undergraduate, metric;
  $100k pool [17].
- winners: a university of toronto trio, "between the lines" - pocket
  pressure analysis. winning metrics: cpp, ople/dple, surplus pressure
  for linemen [17]. (individual names not found.)
- tv lineage: pressure probability, built off bowl submissions - 4 ai
  models over 90k plays [27][42].
- gaps: winner names, exact file list, prize split, entrant counts.

## 2024 - tackling

theme: tackling, on weeks 1-9 of 2022 tracking [19].

- dataset: games/plays/players/tackles csvs plus tracking_week files
  [26][43].
- winners: chang, dai, jiang, cheng - a tackle-probability plus
  conversion-rate metric framing missed-tackle opportunity [20][9].
  their definition: tackle probability over 75% sustained 0.5s then a
  drop, with no tackle within 1s. they surfaced ~4x more
  missed-tackle chances than the nfl tracked [22][9]. $25k total
  ($12.5k finalist + $12.5k winner) [20].
- tv lineage: tackle probability - trained 2018-2022, tested 2023,
  20 features x 11 defenders [28][50]. (whether the deployed stat
  equals the winners' metric or a separate nfl model is unconfirmed.)
- gaps: kaggle url; weeks 1-9 2022 overlaps the 2025 dataset claim,
  unreconciled.

## 2025 - pre-snap motion and alignment

theme: use pre-snap motion and alignment to predict offensive
tendencies [23].

- dataset: 16,124 plays, 136 games, weeks 1-9 2022 [25]. (sourced to a
  weak github mirror - verify against kaggle.)
- platform: kaggle [26]. tracks: undergraduate, metric, coaching -
  one finalist each [23][37].
- finalists: safety entropy, pollack (metric); nyu, tendenciq, wendel
  also named [24]. 400+ entrants; $12.5k finalist x2 pattern [24].
- winners: overall winner name not found in any public source -
  operations.nfl.com winner pages return 404. sumersports' tracking
  transformer aided multiple winners [47].
- tv lineage: whether the disguised-coverage concepts have deployed as
  a broadcast stat is unresolved.
- gaps: winner name, track-to-finalist mapping, exact file list
  (player_play.csv schema change unverified).

## 2026 - player movement prediction

the 8th annual bowl and a format break: first movement-prediction topic,
first-ever public leaderboard scored against next gen stats truth [30].

- tracks: leaderboard (prediction) + data visualization, with
  university-only and broadcast-viz sub-tracks. kaggle hosts both
  competitions [31].
- dates + scale: entries opened sep 25 2025; leaderboard due dec 3,
  analytics dec 17 2025 [31][33]. $100k prizes, finalists present at
  the 2026 combine [30]. 8,329 registrations, 771 teams, 69
  countries [33].
- dataset + scoring: train on 2023-24, scored against 2025 weeks
  14-18 [30]. 49 files, weekly train csvs, test via eval api [33].
  tracking at 10fps: x/y, speed, accel, direction, ball [34].
  one preprint puts the corpus at 18,009 pass plays [35] (unverified
  against official data).
- winners: prediction 1-2-3 by handles ohkawa3, a cjk handle, and
  nofreelunch [33]; kaggle grandmasters takoi and mifune (team rist)
  each took solo golds [36]. analytics winner: rice's lucca ferraz,
  "ghostbusters" [30][35b]. (solo-vs-team ambiguity: rice also credits
  ferraz + ascher with a dish award - verify.)
- method signal: lstm seq2seq with z-score + hyperband, rmse 50.3 down
  to 9.34 in the preprint [35].
- judging: analytics rubric football 30 / data 30 / writeup 20 /
  viz 20 [37b]. aws support: slack channel, builder center guide,
  up to $200 free tier credits [31].
- gaps: prediction-track scoring details, eval api mechanics, real
  names/scores of top 3, full analytics finalists list, official file
  list. six key facts single-sourced to the zennie62 blog - treat as
  provisional until nfl/kaggle corroborate.

## the rotation, compressed

2019 open innovation -> 2020 rushing prediction -> 2021 pass defense ->
2022 special teams -> 2023 pass rush/block -> 2024 tackling ->
2025 pre-snap -> 2026 movement prediction.

offense, defense, and open formats alternate; the contest keeps returning
to prediction tasks (2020, 2026) between concept/metric years. that
pattern is the main input to the [2027 forecast](2027-prediction.md).
