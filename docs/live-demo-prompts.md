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
> honor gpu_lock: if the lock is held, wait and retry, never force.

intro (30s): "first terminal wakes the local box. no cloud spend."
+60min: healthz up, no OOM. fallback: cold restart supervisor; if
VRAM low, stop the comfyui bridge first.

## T2 — frogger one-shot game dev

dir: ~/code/frogger (mkdir -p ~/code/frogger first)

prompt:

> write AGENTS.md first, then build in one pass, no iteration:
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
> say so and stop — do not work around auth. [VERIFY distribution
>
> > id plus profile at showtime.]

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
> call availableGestures() plus availableEmotes() first and only use
> calls that exist. wire it into the playground, screenshot at 720p
> via playwright into the new dir, report the screenshot path.

intro (30s): "fourth terminal teaches our squares hosts to react."
+60min: open the screenshot, click a host, watch it cheer or sulk.
fallback: play https://bryanchasko.com/sumerian-squares/ live and
narrate what the prompt asked for.

## T5 — NFL sweep, no downloads

dir: /home/bryanchasko/code/chasko-labs/nfl-big-data-bowl-2027/

prompt:

> guard snapshot first with scripts/guard_data.sh snapshot, then
> bash scripts/sweep_weeks.sh across every week in data/, then
> features plus lasso baseline per week. every csv plus png into
> data/scratch/, never touch data/ raw. if data/ is missing weeks,
> run samples/2024 plus samples/2025 instead and say so up front.
> report per-week accuracy with standard errors at the end.

intro (30s): "fifth terminal runs the season while we talk."
+60min: per-week accuracy table. fallback: sample slice plot.

preseeded plays (all in samples/2024, verified in repo):

- game 2022090800 play 56 — Bills at Rams, Diggs catch frame 12.
- frame 97 same play — tackle close, second vision input.
- fan-out questions: fastest ball-carrier per play; mean defender
  distance at pass arrival; quarterback over 3 yards per second
  at throw. join keys gameid, playid, nflid.

## T6 — floater, verify plus conflict watch

dir: ~

prompt:

> check four panes and report green or red each: tail the deploy
> log, guard_data.sh check in the NFL repo, curl
> https://clouddelnorte.org/not-frogger/ and head it, curl the
> glimmer healthz. own the first red pane, park the rest.

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
