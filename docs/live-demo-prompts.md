# live demo prompts — virtual event, 1 hour unattended

fire T1 first (local box, no network), then fan out T2 through T5.
T6 floats. one terminal per block: cd to the dir, paste the prompt
into muse, walk away. showtime rechecks marked [VERIFY].

---

## T1 — glimmer local (fires first)

dir: ~/code/heraldstack/heraldstack-firecracker/muse-code/glimmer

prompt:

> start the local stack: valkey bridge, then glimmer_supervisor.py.
> expect the OpenAI-compat endpoint up at http://127.0.0.1:8181 and
> the VRAM floor holding per rocm-smi. report healthz plus free VRAM.
> precondition: ~12GB VRAM free. comfyui plus sibling jobs hold VRAM
> without the lock, so coordinate with their owners before showtime.
> honor gpu_lock: if the lock is held, wait and retry, never force,
> never kill sibling processes.

intro (30s): "first terminal wakes the local box. no cloud spend."
+60min: healthz up, no OOM. fallback: cold restart supervisor.
trial note: backend_down plus 7GB held observed pre-show — normal
until VRAM is coordinated quiet.

## T2 — frogger one-shot game dev

dir: ~/code/frogger (AGENTS.md pre-staged, trial-built clean: 8.3KB
one-pass, node syntax ok, zero network refs, served 200, s3 dry-run
uploads index.html only)

prompt:

> read AGENTS.md, then build in one pass, no iteration:
> grid 13 wide by 14 tall. road lanes with cars, river lanes with
> logs and turtles, 5 home bays, 3 lives, score for forward hops
> plus home fills. collision by rectangle overlap on lane rows.
> one self-contained index.html, canvas 2d, no build step, no npm,
> relative paths only. arrows plus wasd plus swipe. acceptance:
> runs via python3 minus m http.server, zero console errors, frog
> dies on road hit and water without a log, home bay fills score.

intro (30s): "second terminal builds frogger from one prompt."
+60min: serve it, play it on the shared screen.
fallback: re-gen the single file only, never npm or build.

## T3 — deploy not-frogger (starts after T2 lands)

dir: anywhere holding the T2 index.html

prompt:

> publish this dir to https://clouddelnorte.org/not-frogger/ with a
> scoped prefix sync only: aws s3 sync <DIR>/ s3://clouddelnorte.org/not-frogger/
> with exact timestamps plus no-cache, then a cloudfront
> invalidation on /not-frogger/\* only, then curl the url and head it.
> never run npm run build, never sync lib/ or root. if SSO expired,
> say so and stop — do not work around auth. dist ECC3LP1BL2CZS,
> profile aerospaceug-admin, both verified live pre-show. 404 on
> the url before first deploy is expected, not a failure.

intro (30s): "third terminal ships the game dev build to the public url."
+60min: last-modified on the url matches deploy time.
fallback: `aws login` then retry; mac mini scp as last resort.

## T4 — sumerian squares reactions (real feature, additive only)

dir: /home/bryanchasko/code/sumerian-hosts
rule: new files only. never touch src/engine-adapter/_ or src/core/_.

prompt:

> add src/game/hostReactions.ts only: map game events square-claim,
> correct, wrong, win, lose, tie onto BabylonEngineAdapter gesture
> plus emote calls — correct cheers big, wrong goes bored plus
> defense, win applauds with heart, lose goes aggressive, tie waves.
> await loadHost() first (gesture, emote, available lists all throw
> before it), then call availableGestures() plus availableEmotes()
> and only use names that exist. gesture takes {holdMs}, emote
> takes just a name, both return promises. hook reactions after
> line 347 in examples/playground/main.ts where loadHost resolves.
> screenshot at 720p via playwright into the new dir, report path.

intro (30s): "fourth terminal teaches our squares hosts to react."
+60min: open the screenshot, click a host, watch it cheer or sulk.
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
  plus late per play. T1 warms glimmer on all nine at fire time
  (blocked pre-show: VRAM held), spark takes mid16.
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
