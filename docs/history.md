# bowl history 2019-2026

every edition: topic, dataset, winners, finalists, and what escaped to
tv. bracketed numbers are sources in [references](references.md).
winner/finalist tables per league records (via bryan), spot-corroborated
against press [9][20][24][55][56].

## 2019 - pass offense, routes, track movement (inaugural)

open-ended statistical innovation on pass offense [1].

- dataset: 91 games across the first 6 weeks of 2017 [2]. shipped as
  per-game tracking csvs on github [3].
- winners (two divisions): open division elijah "nate" sterken -
  convolutional neural nets on spatial tracking coords to identify
  receiver routes (routenet) [4]. college division simon fraser (dani
  chu, matthew reyers, james thomson, lucas wu) - "routes to success",
  clustering tracking trajectories into route trees [2]. (sterken now
  leads data science for the browns, per an open-source football deck
  surfaced in verification.)
- finalists: sameer deshpande + vinayak evans (completion probability
  under pressure, qb decision-making).
- tv lineage: none found. no 2019 metric is documented reaching
  broadcast or next gen stats.
- gaps: prize pool, dates, judging criteria.

## 2020 - rushing yards at handoff

first kaggle edition and the template-setter: predict rushing yards at
the moment of handoff [5].

- dataset: train on 2017-18, test on 2019 weeks 13-17 [5].
- platform + scoring: kaggle [7], scored by crps over a yards cdf
  (-99..99) [6].
- winners: philipp singer + dmitry gordeev (h2o.ai), team "the zoo" -
  ensemble ml on handoff positions and velocities predicting full
  probability distributions of yards gained [5][9].
- tv lineage: the big one. the winning approach became expected
  rushing yards on next gen stats, debuting on national tv about six
  months later, and spun off rushing yards over expected plus 1st-down
  and td probability [9]. aws counts 75+ ml stats plus ryoe from the
  bowl pipeline overall [29].
- gaps: formal title of the zoo's kaggle writeup (kaggle renders via
  js); college division unmentioned anywhere found.

## 2021 - defensive pass coverage

theme: evaluate defensive performance on passing plays [10].

- dataset: 2018 passing plays, ~2.17gb across 20 csvs [11].
- platform: kaggle [8].
- winners: wei peng + marc richards (pitt) - "a defensive player
  coverage evaluation framework": classified man/zone responsibilities
  and evaluated performance pre- and post-pass [57].
- finalists: jill reiner (denison, coverage clustering + target/
  completion models); meyappan subbaiah, dani chu, matthew reyers,
  lucas wu ("illuminating the defense"); james venzor + matthew
  gartenhaus; joe andruzzi (one-cut routes + double moves); ella
  summer (db random effects on target/completion probability).
- tv lineage: pass-defense work inspired coverage classification [13];
  later coverage responsibility stat built with ai/ml traces to bowl
  submissions [41]. (naming conflict unresolved - verify before citing.)
- correction log: an earlier draft of this doc named a stolaf-led
  foursome as champions from a school paper [12]. that conflated the
  2022 finalist team (below); the paper's claim is now unattributed
  to a division. grand prize stands as peng + richards.
- gaps: dataset facts come from github mirrors, not kaggle or nfl.

## 2022 - special teams (punting, kickoffs, coverage)

theme: special teams, using 2018-20 next gen stats plus pff scouting
data [14].

- dataset: 5 csv groups including pff scouting [15].
- winners: simon fraser (robyn ritchie, brendan kumagai, ryker moreau,
  elijah cavan) - "punt returns: using the math to find the path":
  optimal-path algorithm + raye metric, with a shared kaggle notebook
  that became a starter reference [16][45].
- finalists: rahul kasar + jay li (firetime, gunners/vises); ryan
  gross, joseph rudoler, tai nguyen, ryan brill (kick-return path);
  ian barnett (coyote, conditional yards over expected); wei peng,
  marc richards, sam walczak, jack werner (where should punters
  aim?); john miller + uri smashnov (ar for kickoffs/punts).
- tv lineage: none found reaching broadcast or next gen stats.
- gaps: winning-entry detail beyond the notebook; no pff scouting
  schema documented.

## 2023 - pass rush and offensive line

theme: new pass-block and pass-rush analysis with next gen stats [17].

- dataset: 2021 qb dropbacks, sacks, scrambles, plus pff scouting [17].
  layout: games/players/plays/pffscoutingdata plus weeks 1-8 tracking,
  weekly tracking csvs ~1.5gb each [44].
- platform: kaggle [18]. tracks: coaching, undergraduate, metric;
  $100k pool [17].
- winners: hassaan inayatali, aaron white, daniel hocevar (toronto) -
  "between the lines: how do we measure pressure?": animated spatial
  heatmaps of pocket pressure intensity and pocket longevity, plus
  cpp, ople/dple, surplus pressure for linemen [17].
- finalists: dominic borsani (blitz strategy); joseph ferraiola, rohit
  kumar, ajay patel, cody alexander (xpassrush, pre-snap rusher id);
  gregory matthews + quang nguyen (strain: sacks, tackles, rushing
  aggression index [40]); nick bachelder (idpi situational rusher
  metric); jay sagrolikar + paul ibrahim (uchicago, open-space
  survival probabilities).
- tv lineage: pressure probability, built off bowl submissions - 4 ai
  models over 90k plays [27][42].
- gaps: exact file list, prize split, entrant counts.

## 2024 - tackling and defensive pursuit

theme: tackling, on weeks 1-9 of 2022 tracking [19].

- dataset: games/plays/players/tackles csvs plus tracking_week files
  [26b][43].
- winners: matthew chang, katherine dai, daniel jiang, harvey cheng -
  "uncovering missed tackle opportunities": tackle probability +
  conversion rate. sbj confirms first place [20]. definition with
  teeth: tackle prob over 75% sustained 0.5s, then a drop, no tackle
  within 1s [9]. surfaced ~4x more missed-tackle chances than the
  league tracked [22]. $25k total ($12.5k finalist + $12.5k
  winner) [20].
- finalists: smit bajaj + viren bhatia (nyu, edge-setter framework,
  undergrad track); shane hauck, marion haney, devin basley, vinay
  maruri ("no edge, no chance"); quang nguyen, larry jiang, meg
  ellingwood, ron yurko (momentum-based fractional tackles); ben
  davis + nidiyan rajendran ("pull the plug").
- tv lineage: tackle probability - trained 2018-2022, tested 2023,
  20 features x 11 defenders [28][50]. (whether the deployed stat
  equals the winners' metric or a separate nfl model is unconfirmed.)
- gaps: kaggle url; weeks 1-9 2022 overlaps the 2025 dataset claim,
  unreconciled.

## 2025 - pre-snap data and strategic formations

theme: use pre-snap motion and alignment to predict offensive
tendencies and hidden coverages [23].

- dataset: 16,124 plays, 136 games, weeks 1-9 2022 [25]. (sourced to
  a weak github mirror - verify against kaggle.)
- platform: kaggle [26]. tracks: undergraduate, metric, coaching -
  one finalist each [23][37]. 400+ entrants, a record [24].
- winners: smit bajaj + vishakh sandwar (nyu) - "exposing coverage
  tells in the pre-snap": pre-snap alignment + motion patterns
  predicting hidden coverage schemes. $25k, presented at the
  combine [55]. built on the sumersports framework [56].
- finalists: eric steinberg, lindsay fleishman, lucca ferraz, daniel
  barcelona soriano - tendenciq: gradient-boosted models predicting
  te block-vs-route roles from pre-snap position. sbj's finalist
  list also names safety entropy, pollack, and wendel entries [24];
  rice news (mar 2025) confirms ferraz's finalist spot.
- tv lineage: whether disguised-coverage concepts have deployed as a
  broadcast stat is unresolved.
- gaps: track-to-finalist mapping; exact file list (player_play.csv
  schema change unverified).

## 2026 - player movement while the ball is in the air

the 8th annual bowl and a format break: first movement-prediction
topic, first-ever public leaderboard scored against next gen stats
truth [30].

- tracks: leaderboard (prediction) + data visualization, with
  university-only and broadcast-viz sub-tracks. kaggle hosts both
  competitions [31].
- dates + scale: entries opened sep 25 2025; leaderboard due dec 3,
  analytics dec 17 2025 [31][33]. $100k prizes, finalists present at
  the 2026 combine [30]. 8,329 registrations, 771 teams, 69
  countries [33] (single-sourced, provisional).
- dataset + scoring: train on 2023-24, scored against 2025 weeks
  14-18 [30]. 49 files, weekly train csvs, test via eval api [33].
  tracking at 10fps: x/y, speed, accel, direction, ball [34].
  one preprint puts the corpus at 18,009 pass plays [35] (unverified
  against official data).
- grand prize: lucca ferraz (rice, solo) - "ghostbusters: back off
  man, i'm a data scientist!": evaluated defender positioning and
  movement while the ball was airborne via spatial distributions of
  hypothetical ghost defenders [30][35b].
- finalist: grant nielson, connor thompson, evan miller, evan west
  (byu/uvu) - "defensive reaction options post-release": modeled
  split-second defensive reaction capability between qb release and
  catch point.
- prediction podium (handles only): ohkawa3, a cjk handle, and
  nofreelunch [33]; rist grandmasters takoi and mifune each took
  solo golds [36]. real names and scores missing.
- method signal: lstm seq2seq with z-score + hyperband, rmse 50.3
  down to 9.34 in the preprint [35].
- judging: analytics rubric football 30 / data 30 / writeup 20 /
  viz 20 [37b]. aws support: slack channel, builder center guide,
  up to $200 free tier credits [31].
- gaps: prediction-track scoring details, eval api mechanics, full
  viz/university/broadcast sub-track results, official file list.

## the rotation, compressed

2019 open innovation -> 2020 rushing prediction -> 2021 pass defense ->
2022 special teams -> 2023 pass rush/block -> 2024 tackling ->
2025 pre-snap -> 2026 movement prediction.

offense, defense, and open formats alternate; the contest keeps
returning to prediction tasks (2020, 2026) between concept/metric
years. that pattern is the main input to the [2027
forecast](2027-prediction.md).

## repeat names (the dynasty watch)

- quang nguyen: 2023 strain finalist -> 2024 fractional tackles
  finalist.
- smit bajaj: 2024 undergrad finalist (nyu) -> 2025 grand prize (nyu).
- lucca ferraz: 2025 tendenciq finalist (rice) -> 2026 grand prize.
- wei peng + marc richards: 2021 grand prize (pitt) -> 2022 punters
  finalists.
- ron yurko: writes the how-to-win guides, then finalists in 2024.
  listen to him.
- simon fraser: wins 2019 college and 2022 overall. program to watch.
