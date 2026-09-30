# live demo prompts — virtual event, 1 hour unattended

five windows, five standalone demos. fire T1 first (local box),
then fan out T2 through T4. T5 floats. one terminal per block: cd
to the dir, start muse, paste the prompt, walk away.

---

## T1 — glimmer local (fires first)

dir: ~/code/heraldstack/heraldstack-firecracker/muse-code/glimmer

prompt:

> produce tonight's three-line score report using only the local
> box. steps: 1) confirm it answers: curl
> http://127.0.0.1:8181/healthz. 2) read these two finished files:
> /home/bryanchasko/code/chasko-labs/nfl-big-data-bowl-2027/data/scratch/baseline_2024/metrics.csv
> and .../baseline_2025/metrics.csv. 3) hand both numbers to the
> local endpoint at http://127.0.0.1:8181/v1/chat/completions and
> get back one line per year (year, accuracy, standard error) plus
> a final line naming the higher year and the gap, 40 words max. 4) report the three lines plus elapsed seconds. rules: local
> endpoint only, never the cloud; short outputs stay fast on CPU;
> text in, text out — it cannot see images, do not send any; if
> gpu_lock is held, wait and retry, never force.

+60min: three-line report on screen, timed fast.
fallback: cold restart supervisor, retry once.

## T2 — frogger build plus deploy (one demo, build then ship)

dir: ~/code/frogger (AGENTS.md pre-staged, trial-built clean: 8.3KB
one-pass, node syntax ok, zero network refs, served 200, s3 dry-run
uploads index.html only)

prompt:

> read AGENTS.md and follow it exactly — it carries the
> coordinate, collision, and log-riding rules that prevent
> invisible bugs. then build in one pass, no iteration: grid 13
> wide by 14 tall. road lanes with cars, river lanes with logs
> and turtles, 5 home bays, 3 lives, score for forward hops plus
> home fills. one self-contained index.html, canvas 2d, no build
> step, no npm, relative paths only. arrows plus wasd plus swipe.
> run this window at maximum reasoning effort. acceptance (your
> definition of done): runs via python3 minus m http.server, zero
> console errors, cars kill only on real rect overlap, logs are
> rideable with drift and water without a log kills, home bays
> fill once and stay filled.
> then immediately ship it, same session: scoped prefix sync only
> with aws s3 sync . s3://clouddelnorte.org/not-frogger/
> --profile aerospaceug-admin --delete, excluding AGENTS.md, then
> a cloudfront invalidation on /not-frogger/\* only (dist
> ECC3LP1BL2CZS), then curl the url and head it. never run npm run
> build, never sync above the prefix. if SSO expired, say so and
> stop — do not work around auth. report the live url at the end.

+60min: https://clouddelnorte.org/not-frogger/ flips 404 to playable.
fallback: `aws login` then retry; mac mini scp as last resort.

## T3 — squares iteration on the live game (real feature)

dir: /home/bryanchasko/code/websites/bryan-chasko-com/assets/sumerian-squares
rule: this is the deployed bryanchasko.com/sumerian-squares game.
iterate it, never rewrite it. small diff, tests keep passing.

prompt:

> add src/host-answer-reactions.ts only: visual host reactions for
> right and wrong answers. read the existing pattern first: tap
> moments in src/game-controller.ts (~lines 735-775) dispatch
> playGesture plus playEmote from ./host-loader guarded by
> hasEmote, with cell CSS pulse classes like sh-cell--tap-pulse.
> keyword-to-gesture map lives in pickGestureForQuip in
> src/question-presenter.ts. new module exports
> reactToAnswer(cell, correct): on correct, applause emote if
> hasEmote else big gesture, plus a cell pulse class; on wrong,
> bored emote if hasEmote else aggressive gesture, plus a dim
> class. only use gesture plus emote names that exist in
> host-loader. wire it where answers resolve (follow playerDecision
> in src/game.ts to its controller call site). run the existing
> test suite for this dir before and after; new tests for the new
> module only. report the diff stat plus test result.

+60min: diff stat plus green tests, then play one round live.
fallback: play https://bryanchasko.com/sumerian-squares/ live and
narrate what the prompt asked for.

## T5 — NFL sweep, no downloads

dir: /home/bryanchasko/code/chasko-labs/nfl-big-data-bowl-2027/

prompt:

> live run is verification plus fast answers, about 5 minutes.
> full features are prebuilt (2024 408s, 2025 ~35min) and staged
> in data/scratch — never rebuild unless guard mismatches. run:
> guard snapshot plus check, re-run the two sweep questions live
> (events, formations, minutes), re-run both lasso baselines live
> (8s each, expect 0.779 plus-minus 0.001 and 0.743 plus-minus
> 0.003). report the staged answers: JUMBO 0.478 plus EMPTY 0.461
> top formations, SHOTGUN 0.403 on 6,378 plays; top events
> first_contact 242k, tackle 231k, ball_snap 145k. every csv plus
> png into data/scratch/, never touch data/ raw. only on guard
> mismatch: rebuild features first, then continue.

intro (30s): "fifth terminal runs the season while we talk."
+60min: per-week accuracy table. fallback: sample slice plot.

preseeded plays (2024 week 1 raw, game 2022090800 Bills at Rams):

- play 56 — Diggs catch. vision batch: pre1, mid12, late22.
- play 80 — second play, same treatment: pre1, mid16, late30.
- play 101 — third play: pre1, mid25, late49.
- nine frames staged in data/scratch/vision_batch/, pre plus mid
  plus late per play. spark describes all nine live. glimmer is
  text-only and never touches them.
- fan-out questions: fastest ball-carrier per play; mean defender
  distance at pass arrival; quarterback over 3 yards per second
  at throw. join keys gameid, playid, nflid.

## T6 — floater, verify plus conflict watch

dir: ~

prompt:

> check four panes and report green or red each: tail the deploy
> log, guard_data.sh check in the NFL repo, curl
> https://clouddelnorte.org/not-frogger/ and head it, curl the
> glimmer healthz. dist ECC3LP1BL2CZS confirmed live serving
> clouddelnorte.org off s3-website-us-east-1, profile
> aerospaceug-admin sso verified, prefix empty and clear.

intro (30s): "sixth terminal watches everything else."
+60min: four green. fallback: own the first red, park the rest.

## conflicts (read before showtime)

1. GPU: glimmer needs ~17GB. serialize via gpu_lock, glimmer wins.
2. deploy clobber: scoped prefix sync only, never root builds.
3. squares: additive-only, engine-adapter plus core untouched.
4. frogger: relative paths only, no fetch() of local files.
5. NFL: data/ present, never download gigabytes live.

## infra to narrate (mcp, valkey, s3vectors, agents)

- MCP: muse talks to AWS, valkey, docker through bridge launchers.
- valkey: gpu_lock serializes the card; findings log lives there.
- s3vectors: semantic memory across sessions.
- agents: subagents fan out in isolated worktrees; souls are the
  persistent personas behind them. T5 plus T6 show this live.
