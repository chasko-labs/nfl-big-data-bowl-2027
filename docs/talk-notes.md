# talk notes (one page)

cheat sheet for tomorrow's presentation. every line traces to the
research docs.

## what it is (30 seconds)

annual contest from nfl football operations, powered by aws. real
next gen stats tracking data (10 frames/sec, every player + ball).
goal: invent stats good enough for tv and team analytics departments.
2026 was the 8th edition; 2027 not announced yet.

## scale stats (the impressive slide)

- $100k prize pool; finalists present at the combine [31][30]
- 2026: 8,329 registrations, 771 teams, 69 countries [33, provisional]
- 75+ ml stats in the pipeline; 50+ entrants hired into sports
  analytics, 30+ by teams or vendors [29][51]
- aws processes 500m+ tracking points a season [52]

## the story arc (one line per year)

- 2019 open innovation - routenet wins, contest is born [4]
- 2020 rushing prediction - the zoo wins, becomes expected rushing
  yards on tv in six months [9]
- 2021 pass defense - man-vs-zone + defender value -> coverage
  stats [12]
- 2022 special teams - punt-return optimal path + raye [16]
- 2023 pass rush - pocket pressure -> pressure probability [17][27]
- 2024 tackling - missed-tackle metric -> tackle probability [20][28]
- 2025 pre-snap - nyu exposes coverage tells, wins it all [55][56]
- 2026 movement prediction - first public leaderboard vs ngs truth,
  ghostbusters takes analytics [30]

## the punchlines

1. entries escape: expected rushing yards, ryoe, pressure
   probability, tackle probability, coverage responsibility all went
   contest -> broadcast.
2. the real prize is the combine interview loop, not the check.
3. graders are team analysts volunteering nights - answer the prompt,
   write well, make it look expensive (patton tips, craft.md).
4. small data wins on downstream use, not fit quality (yurko).
5. 2027 timing: last year opened sep 25. announcement could be any
   day - and our forecast says ghost/counterfactual applications.

## if asked "what would you enter?"

2026 built movement models; 2027 likely asks what should have
happened - ghost defenders, expected positioning, blown assignments.
prep is done: data pipeline, baselines, and writeup template are in
this repo. see 2027-prediction.md.
