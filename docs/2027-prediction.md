# 2027 prediction

the 2027 edition has not been announced. everything below the line is
forecast, not fact - reasoning from eight years of evidence, marked
where it leaves the evidence. bracketed numbers are sources in
[references](references.md).

## timing: watch now

the 2026 bowl opened entries sep 25 2025 [33]. today is sep 27 2026.
if the league holds cadence, the 2027 announcement lands within days
or weeks, entries due early december, finalists february, winners at
the march combine. check kaggle + operations.nfl.com weekly until it
drops.

## the rotation pattern (evidence)

2019 open -> 2020 rushing prediction -> 2021 pass defense -> 2022
special teams -> 2023 pass rush -> 2024 tackling -> 2025 pre-snap ->
2026 movement prediction.

three regularities:

1. prediction years (2020, 2026) alternate with concept/metric years.
   2026 was prediction, so 2027 likely asks for a metric or concept.
2. offense and defense alternate. 2025 (pre-snap offense reads) and
   2026 (all-22 movement) lean offensive - defense is due.
3. the league follows its own product needs: each year's topic feeds
   next season's next gen stats push (pressure -> tackle -> coverage
   responsibility in consecutive years).

## forecast, ranked (opinion)

1. counterfactual / ghost-player applications. 2026 built movement
   models; the natural sequel is "what should have happened" - ghost
   defenders, expected positioning, blown-assignment detection. the
   2026 analytics winner was literally called ghostbusters [30].
   highest-probability pick.
2. the new kickoff. the dynamic kickoff rewrote return geometry in
   2024 and the league is still learning it. 2022 did punts, never
   kickoffs [14][16]. fresh scheme + tracking = ideal bowl material.
3. run blocking / offensive line. 2023 covered pass block [17]; run
   game line evaluation is untouched and teams pay for it.
4. qb decision-making. reads, progressions, throw-vs-checkdown under
   pressure - combines the 2023 and 2025 threads. hard to grade,
   which cuts both ways.
5. injury / load / player safety. the league cares enormously,
   but data sensitivity makes it unlikely as an open contest.

also possible: a second straight prediction year if the 2026 eval
api worked well (red zone? fourth down? play outcome?), or another
open year like 2019 to reset the rotation.

## prep checklist (do before announcement)

data:

- [ ] kaggle cli authed, rules accepted on 2023-2026 competitions
- [ ] one full past dataset local (2024 tackling: clean layout [43])
- [ ] nflverse play-by-play for joins (old_game_id / play_id)
- [ ] the 2026 eval-api format studied (prediction track may repeat it)

stack:

- [ ] tracking eda kit: animate plays, frame/event handling
- [ ] baselines ready: lasso-logistic, xgboost, lstm seq2seq, a
      transformer (sumersports helped multiple 2025 winners [47])
- [ ] viz track option: r + ggplot2/gganimate or python equiv -
      submissions should look expensive (patton #10)

method:

- [ ] yurko discipline wired in: base rates, simple baseline, cv
      with standard errors, downstream use over fit [39]
- [ ] writeup template: <2000 words, <10 figures, code appendix [37]
- [ ] patton 20 tips re-read the week of submission (craft.md)

logistics:

- [ ] aws free tier + credits lined up (~$200) [31]
- [ ] discord/slack community joined at announcement
- [ ] cmsac football workshop on the calendar [47]
- [ ] a proofreader recruited (patton #8 - easy points)

## what "ready to win" looks like

day one of the announcement: data downloads while the 2026-winning
approaches get re-read; day two: eda + baselines on the new schema;
week one: the metric or model exists and the writeup has a skeleton.
the teams that win are the ones whose tooling was done before the
topic existed.
