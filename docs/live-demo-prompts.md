# live demo prompts — virtual event, 1 hour unattended

how to run: fire T1 first (local box, no network), then T2 through T6.
open one terminal per block, cd to the dir, paste the prompt into muse,
walk away. intro talk track + what to check at +60min below.

---

## T1 — glimmer vision batch (fires first, runs local)

dir: ~/code/heraldstack/heraldstack-firecracker/muse-code/glimmer
needs: quiet card. if the card is busy, skip this terminal.

prompt:

> for each png in
> ~/code/chasko-labs/nfl-big-data-bowl-2027/data/scratch/play\_\*.png,
> describe the football play in two sentences through the local
> endpoint at http://127.0.0.1:8181/v1: who has the ball, what the
> coverage looks like. save lines to /tmp/vision_batch.md. keep
> reasoning_strength low so it answers instead of thinking aloud.

intro (30s): "first terminal asks the local box to watch football."
+60min: read two descriptions aloud, show the plots they describe.
fallback: "card was busy — the deck already holds the vision numbers
slide from last run: 135 seconds, correct down to the subtitle."

## T2 — full pipeline sweep (the long job)

dir: ~/code/chasko-labs/nfl-big-data-bowl-2027

prompt:

> run the full pipeline end to end. guard snapshot first with
> scripts/guard_data.sh snapshot, then bash scripts/sweep_weeks.sh across
> every week in data/, then features and the lasso baseline per week.
> write every csv plus png into data/scratch/, never touch data/ raw.
> if data/ is missing weeks, run everything against samples/2024 plus
> samples/2025 instead and say so up front. report per-week accuracy
> with standard errors at the end.

intro (30s): "second terminal runs the whole season while we talk."
+60min: per-week accuracy table in data/scratch/. fallback: "sweep is
still running — the sample slice already finished, here is its plot."

## T3 — one-shot game dev from scratch (cookbook recipe, live)

dir: ~/code/game-crossy (new, empty)

prompt:

> write AGENTS.md first: forward is negative z, score is minus row,
> collision by mesh world position on x and z, water kills unless on
> a log, logs drift without snapping x back to grid. then build a
> crossy road clone as one self-contained index.html: three.js r160
> via importmap, no build step, no npm. blocky animal player, 6
> selectable variants, grid hop with squash and stretch, grass plus
> road plus water plus rail lanes, coins, score and best in
> localstorage, touch swipe plus d-pad. acceptance: wasd and arrows
> move on grid, cars kill only on real overlap, logs ride, runs via
> python3 minus m http.server with zero console errors.

intro (30s): "third terminal builds a game dev demo from one prompt."
+60min: serve it, play it on the shared screen, show the file count.
fallback: show the cookbook crossy screenshots, narrate the prompt.

## T4 — sumerian squares iterative pass (our game dev assets)

dir: ~/code/sumerian-hosts
rule: additive only. new files welcome, no edits to existing sources.

prompt:

> additive change only, do not modify any existing file. add a new
> demo page examples/squares-trivia/ that reuses the playground host
> loader to put three hosts on screen side by side, each speaking a
> different sumer trivia line on click. new files only plus one
> paragraph in docs/setup.md pointing at it. verify with bun run
> build:wasm and a playwright screenshot at 720p saved into the new
> dir. report the screenshot path when done.

intro (30s): "fourth terminal extends our shipped squares game dev."
+60min: open the screenshot, then the page, click a host.
fallback: play the live https://bryanchasko.com/sumerian-squares/
and narrate what the prompt asked for.

## T5 — parallel question fan-out (the speed story)

dir: ~/code/chasko-labs/nfl-big-data-bowl-2027

prompt:

> answer three questions against samples/2024 in parallel, one output
> csv plus png per question into data/scratch/fanout/:
>
> 1. fastest ball-carrier speed per play.
> 2. mean defender distance to the ball at pass arrival.
> 3. plays where the quarterback tops 3 yards per second at throw.
>    use join keys gameid, playid, nflid. print the three file paths
>    when done.

intro (30s): "fifth terminal answers three questions at once."
+60min: three csvs plus pngs, read the fastest speed aloud.
fallback: read whichever of the three finished first.

## T6 — iterative refine pass on the T3 build (cookbook loop, live)

dir: ~/code/game-crossy (same dir as T3, starts after T3 lands)
needs: T3 index.html exists. if T3 failed, skip this terminal.

prompt:

> playtest the index.html in ~/code/game-crossy and run three
> refinement passes, verifying each in a real browser before moving
> on: 1. camera — it must follow behind the player with smooth
> lerp, never snap on turns. 2. feel — hop squash and stretch,
> particle burst on death, camera shake. 3. difficulty — speed and
> traffic scale with score. serve via python3 minus m http.server,
> screenshot after every pass into shots/, read the console for
> errors, fix what you see. report the three screenshots when done.

intro (30s): "sixth terminal polishes the game dev build."
+60min: flip through the three screenshots, play the final build.
fallback: play the T3 build as-is, narrate the three passes.
