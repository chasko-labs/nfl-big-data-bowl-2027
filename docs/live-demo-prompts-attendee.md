# live demo prompts — attendee reference

companion to a 1-hour live coding session: five standalone demos,
each runnable in its own terminal. start T1 first (local model),
then fan out T2 through T4. T5 floats. paste one prompt per
terminal and walk away.

personal details (home directories, AWS account IDs, bucket and
distribution names, profiles) are replaced with `<placeholders>` —
substitute your own values.

---

## T1 — local model first

dir: `<your-local-model-checkout>`

prompt:

> produce tonight's three-line score report using only the local
> box. steps: 1) confirm it answers: curl
> http://127.0.0.1:8181/healthz (your local endpoint — substitute
> your own host and port). 2) read these two finished files:
> `<repo>/data/scratch/baseline_2024/metrics.csv` and
> `<repo>/data/scratch/baseline_2025/metrics.csv`. 3) hand both
> numbers to the local chat-completions endpoint and get back one
> line per year (year, accuracy, standard error) plus a final line
> naming the higher year and the gap, 40 words max. 4) report the
> three lines plus elapsed seconds. rules: local endpoint only,
> never the cloud; short outputs stay fast on CPU; text in, text
> out — it cannot see images, do not send any; if the GPU lock is
> held, wait and retry, never force.

done: three-line report on screen, timed fast.
fallback: cold-restart the local server, retry once.

## T2 — game build plus deploy (one demo, build then ship)

dir: `<your-game-checkout>` (project instructions pre-staged,
trial-built clean before showtime)

prompt:

> read AGENTS.md and follow it exactly — it carries the
> coordinate, collision, and log-riding rules that prevent
> invisible bugs. then build in one pass, no iteration: grid 13
> wide by 14 tall. road lanes with cars, river lanes with logs
> and turtles, 5 home bays, 3 lives, score for forward hops plus
> home fills. one self-contained index.html, canvas 2d, no build
> step, no npm, relative paths only. arrows plus wasd plus swipe.
> run this window at maximum reasoning effort. acceptance (your
> definition of done): runs via a local static server, zero
> console errors, cars kill only on real rect overlap, logs are
> rideable with drift and water without a log kills, home bays
> fill once and stay filled.
> then immediately ship it, same session: scoped prefix sync only
> with `aws s3 sync . s3://<your-bucket>/<your-prefix>/ --profile
<your-aws-profile> --delete`, excluding AGENTS.md, then a
> CloudFront invalidation on `/<your-prefix>/*` only, then curl
> the url and head it. never run a build step, never sync above
> the prefix. if auth expired, say so and stop — do not work
> around auth. report the live url at the end.

done: `<your-deployed-url>` flips 404 to playable.
fallback: re-authenticate, then retry once.

## T3 — iteration on the live game (real feature)

dir: `<your-app-checkout>`
rule: this is a deployed game. iterate it, never rewrite it.
small diff, tests keep passing.

prompt:

> add src/host-answer-reactions.ts: visual host reactions for
> right and wrong answers. read the existing pattern first: tap
> moments in src/game-controller.ts dispatch playGesture plus
> playEmote guarded by hasEmote, with a cell CSS pulse class
> removed after a timeout. new module exports
> reactToAnswer(cell: HTMLElement, correct: boolean): void — on
> correct, applause emote if hasEmote else a generic gesture,
> plus the pulse class removed after 300ms; on wrong, bored emote
> if hasEmote else an aggressive gesture, plus the pulse class
> removed after 300ms. use only shipped clips, never unshipped
> ones. import play functions via the static ./engine re-export
> as game-controller.ts does, not dynamic import. wire it by
> REPLACING the inline guard-then-fallback reaction blocks at the
> answer call sites — replacement of those blocks only,
> everything else untouched. run the test suite from the repo
> root before and after, plus a typecheck of the build config;
> new tests for the new module only. report the diff stat plus
> test result.

done: diff stat plus green tests, then play one round live.
fallback: play the deployed game live and narrate what the
prompt asked for.

## T5 — data sweep, no downloads

dir: `<repo>/`

prompt:

> live run is verification plus fast answers, about 5 minutes.
> full features are prebuilt and staged in data/scratch — never
> rebuild unless the guard mismatches. run: guard snapshot plus
> check, re-run the two sweep questions live (events,
> formations, minutes), re-run both lasso baselines live (a few
> seconds each, expect ~0.779 and ~0.743). report the staged
> answers: JUMBO 0.478 plus EMPTY 0.461 top formations, SHOTGUN
> 0.403 on 6,378 plays; top events first_contact 242k, tackle
> 231k, ball_snap 145k. every csv plus png into data/scratch/,
> never touch data/ raw. only on guard mismatch: rebuild
> features first, then continue.

intro (30s): "fifth terminal runs the season while we talk."
done: per-week accuracy table. fallback: sample slice plot.

preseeded plays (example: 2024 week 1 raw, Bills at Rams):

- play 56 — Diggs catch. vision batch: pre1, mid12, late22.
- play 80 — second play, same treatment: pre1, mid16, late30.
- play 101 — third play: pre1, mid25, late49.
- nine frames staged in data/scratch/vision_batch/, pre plus mid
  plus late per play. the cloud model describes all nine live;
  the local text-only model never touches them.
- fan-out questions: fastest ball-carrier per play; mean defender
  distance at pass arrival; quarterback over 3 yards per second
  at throw. join keys gameid, playid, nflid.

## T6 — floater, verify plus conflict watch

dir: `~`

prompt:

> check four panes and report green or red each: tail the deploy
> log, run the data guard check in the repo, curl
> `<your-deployed-url>` and head it, curl the local model
> health endpoint.

intro (30s): "sixth terminal watches everything else."
done: four green. fallback: own the first red, park the rest.

## conflicts (read before showtime)

1. GPU: the local model needs most of the card. serialize via a
   lock; the local model wins.
2. deploy clobber: scoped prefix sync only, never root builds.
3. live game: additive-only, engine and core untouched.
4. game build: relative paths only, no fetch() of local files.
5. data sweep: raw data present, never download gigabytes live.

## infra to narrate (tool bridges, cache, vectors, agents)

- tool bridges: the coding agent talks to AWS, cache, and
  containers through bridge launchers.
- cache: a lock key serializes the card; findings log lives
  there.
- vectors: semantic memory across sessions.
- agents: subagents fan out in isolated worktrees with
  persistent personas behind them. T5 plus T6 show this live.
