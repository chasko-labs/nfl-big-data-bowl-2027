# winners hall of fame

every winning entry, what it did, and where the idea ended up.
bracketed numbers are sources in [references](references.md).

## 2019 - sterken (open), simon fraser (college)

- sterken's routenet analyzed route combinations from tracking data [4].
- sfu (chu, reyers, wu, thomson) took the college division [2].
- neither produced a documented broadcast stat. the 2019 lesson is
  structural: open themes reward novelty, but prediction tasks are what
  transfer to tv.

## 2020 - gordeev + singer, "the zoo"

- predicted rushing yards from handoff positions and velocities [5].
- became expected rushing yards on next gen stats within ~6 months,
  then rushing yards over expected, 1st-down and td probability [9].
- the clearest proof of the bowl-to-broadcast pipeline. if the talk
  needs one slide on "why this contest matters," this is it.

## 2021 - peng, richards, walczak + team

- man-vs-zone coverage classifier plus a defender value metric [12].
- lineage into coverage classification [13] and later coverage
  responsibility [41]. exact attribution is murky (paywalled sbj +
  github mirrors) - cite carefully.

## 2022 - simon fraser (ritchie, kumagai, moreau, cavan)

- punt-return optimal-path algorithm + raye metric, with a public
  kaggle notebook that became a starter reference [16][45].
- stack signal: r, ggplot2/gganimate, shiny, bigquery, sportsdataverse -
  per the winners' own getting-started guide [45].
- no broadcast lineage found. special teams metrics are the hardest to
  get on tv - small sample sizes, weird geometry.

## 2023 - toronto trio, "between the lines"

- pocket pressure: cpp, ople/dple, surplus pressure for offensive and
  defensive lines [17].
- fed pressure probability (4 ai models, 90k plays) [27][42].
- names of the trio not found - a gap worth closing before the talk if
  we cite them by name.

## 2024 - chang, dai, jiang, cheng

- missed-tackle opportunity: tackle probability + conversion rate [20].
- definition with teeth: prob >75% for 0.5s, then a drop, no tackle
  within 1s [9]. found ~4x the missed tackles the league tracked [22].
- linked to tackle probability on tv (20 features x 11 defenders,
  trained 2018-22, tested 2023) [28][50].
- prize: $25k total via the $12.5k + $12.5k pattern [20].

## 2025 - winner unclear

- finalists: safety entropy, pollack, nyu, tendenciq, wendel [24].
  overall winner name not publicly found (nfl pages 404).
- theme rewarded: disguised coverage / tendency prediction from
  pre-snap looks [23].
- stack signal: sumersports' sports tracking transformer aided
  multiple winners [47] - transformers on tracking data are now
  table stakes for prediction-flavored years.

## 2026 - ohkawa3 / cjk handle / nofreelunch (prediction), ferraz "ghostbusters" (analytics)

- prediction podium known by handles only; scores and real names
  missing [33]. rist grandmasters takoi, mifune solo golds [36].
- analytics: rice's lucca ferraz, ghostbusters (counterfactual /
  ghost-player framing, per the title) [30].
- method signal from a preprint: lstm seq2seq, z-score + hyperband,
  rmse 50.3 -> 9.34 [35].
- caveat: most 2026 specifics are single-sourced to one blog -
  verify before presenting as fact.

## exemplar non-winner: strain

- the strain notebook (statsinthewild) defines pass-rush pressure
  from rusher-qb distance and closing rate, mirroring materials
  science strain rate. it predicts pressure and is stable across
  samples [40]. yurko holds it up as an exemplar entry [39].
- the kaggle notebook url 404s; method verified via the paper and
  cmu pointers, not the notebook. entry year and placement unknown.
- talk value: a one-metric idea, physically grounded, that outlived
  its entry. exactly the shape the judges reward.

## the career pipeline

- 50+ entrants hired into sports analytics, 30+ by nfl teams or
  vendors [51]. 75+ alumni claimed on the 2026 hype page [31].
- finalists present at the combine [30] - the real prize is the
  interview loop, not the $12.5k.
