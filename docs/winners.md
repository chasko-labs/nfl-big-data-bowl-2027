# winners hall of fame

every grand prize, how it worked, and where the idea ended up.
finalists condensed - full tables in [history](history.md).
bracketed numbers are sources in [references](references.md).

## 2019 - sterken (open), simon fraser (college)

- sterken: cnns on tracking coords to identify receiver routes
  (routenet) [4]. now leads data science for the browns.
- sfu (chu, reyers, thomson, wu): "routes to success" - clustered
  trajectories into route trees [2].
- neither produced a documented broadcast stat. the 2019 lesson is
  structural: open themes reward novelty, but prediction tasks are
  what transfer to tv.

## 2020 - singer + gordeev (h2o.ai), "the zoo"

- ensemble ml on handoff positions/velocities predicting full
  distributions of yards gained [5].
- became expected rushing yards on next gen stats within ~6 months,
  then rushing yards over expected, 1st-down and td probability [9].
- the clearest proof of the bowl-to-broadcast pipeline. if the talk
  needs one slide on "why this contest matters," this is it.

## 2021 - peng + richards (pitt)

- "a defensive player coverage evaluation framework": classified
  man/zone responsibilities, evaluated defenders pre- and
  post-pass [57].
- lineage into coverage classification [13] and later coverage
  responsibility [41]. exact attribution is murky - cite carefully.
- finalists to know: reiner (denison coverage clustering), the
  "illuminating the defense" squad, ella summer (db random effects).

## 2022 - simon fraser (ritchie, kumagai, moreau, cavan)

- "punt returns: using the math to find the path": optimal-path
  algorithm + raye metric, with a public kaggle notebook that became
  a starter reference [16][45].
- stack signal: r, ggplot2/gganimate, shiny, bigquery,
  sportsdataverse - per the winners' own getting-started guide [45].
- finalists to know: firetime (gunner evaluation), coyote (ian
  barnett), the peng/richards-led punters-aim team.
- no broadcast lineage found. special teams metrics are the hardest
  to get on tv - small samples, weird geometry.

## 2023 - inayatali, white, hocevar (toronto), "between the lines"

- "how do we measure pressure?": animated spatial heatmaps of pocket
  intensity + longevity, plus cpp, ople/dple, surplus pressure [17].
- fed pressure probability (4 ai models, 90k plays) [27][42].
- finalists to know: xpassrush (pre-snap rusher id), strain
  (matthews + nguyen [40]), idpi, uchicago survival probabilities.

## 2024 - chang, dai, jiang, cheng

- "uncovering missed tackle opportunities": tackle probability +
  conversion rate, confirmed first place by sbj [20].
- definition with teeth: prob >75% for 0.5s, then a drop, no tackle
  within 1s [9]. found ~4x the missed tackles the league tracked [22].
- linked to tackle probability on tv (20 features x 11 defenders,
  trained 2018-22, tested 2023) [28][50].
- finalists to know: nyu edge setters (bajaj's first appearance),
  "no edge, no chance", momentum fractional tackles (nguyen + yurko),
  "pull the plug".
- prize: $25k total via the $12.5k + $12.5k pattern [20].

## 2025 - bajaj + sandwar (nyu)

- "exposing coverage tells in the pre-snap": alignment + motion
  patterns predicting hidden coverages. $25k, combine
  presentation [55]. built on the sumersports framework [56].
- finalists to know: tendenciq (steinberg, fleishman, ferraz,
  barcelona soriano - te block-vs-route models); safety entropy,
  pollack, wendel entries [24].
- tv lineage unresolved - watch whether disguised-coverage concepts
  surface as a 2026-27 broadcast stat.

## 2026 - ferraz (rice, solo), "ghostbusters"

- "back off man, i'm a data scientist!": defender positioning while
  the ball is airborne, via spatial distributions of hypothetical
  ghost defenders [30][35b].
- finalist: byu/uvu squad (nielson, thompson, miller, west) -
  "defensive reaction options post-release".
- prediction podium by handles only: ohkawa3, cjk handle,
  nofreelunch [33]; rist grandmasters takoi, mifune solo golds [36].
- method signal: lstm seq2seq, z-score + hyperband, rmse 50.3 ->
  9.34 (preprint) [35].

## exemplar finalist: strain (2023)

- matthews + nguyen define pass-rush pressure from rusher-qb
  distance and closing rate, mirroring materials-science strain
  rate. predicts pressure, stable across samples [40]. yurko holds
  it up as an exemplar entry [39].
- the kaggle notebook url 404s; method verified via the paper.
- talk value: a one-metric idea, physically grounded, that outlived
  its entry. exactly the shape judges reward.

## the career pipeline

- 50+ entrants hired into sports analytics, 30+ by nfl teams or
  vendors [51]. 75+ alumni claimed on the 2026 page [31].
- sterken '19 now browns lead ds. repeat finalists (nguyen, bajaj,
  ferraz, peng/richards) keep showing up - the contest is a hiring
  filter as much as a prize fight.
- finalists present at the combine [30] - the real prize is the
  interview loop, not the $12.5k.
