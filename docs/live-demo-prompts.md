# live demo prompts — virtual event, 1 hour unattended

how to run: open one terminal per block, cd to the dir, paste the prompt
into muse, walk away. intro talk track + what to check at +60min below.

---

## T1 — full pipeline sweep (the long job)

dir: ~/code/chasko-labs/nfl-big-data-bowl-2027

prompt:

> run the full pipeline end to end. guard snapshot first with
> scripts/guard_data.sh snapshot, then bash scripts/sweep_weeks.sh across
> every week in data/, then features and the lasso baseline per week.
> write every csv plus png into data/scratch/, never touch data/ raw.
> if data/ is missing weeks, run everything against samples/2024 plus
> samples/2025 instead and say so up front. report per-week accuracy
> with standard errors at the end.

intro (30s): "this terminal runs the whole season while we talk."
+60min: per-week accuracy table in data/scratch/. fallback: "sweep is
still running — the sample slice already finished, here is its plot."

## T2 — route-runner game, one prompt (the crowd-pleaser)

dir: ~/code/chasko-labs/nfl-big-data-bowl-2027 (new subdir game-route-runner/)

prompt:

> in game-route-runner/, build a single-file three.js route-runner:
> a receiver dodging defenders on real tracking coordinates from
> ../samples/2024/tracking_sample.csv game 2022090800 play 56.
> arrow keys move, defender positions come from the csv, catch wins,
> tackle loses. static export plus index.html that runs from any host.
> no build step. acceptance: loads with no console errors, playable
> with keyboard, score persists in localstorage.

intro (30s): "second terminal builds a game out of the same data."
+60min: open index.html from bryanchasko.com deploy, play it live.
fallback: play the deployed copy, narrate the prompt that built it.

## T3 — parallel question fan-out (the speed story)

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

intro (30s): "third terminal answers three questions at once."
+60min: three csvs plus pngs, read the fastest speed aloud.
fallback: read whichever of the three finished first.

## T4 — glimmer vision batch (the one glimmer experiment)

dir: ~/code/heraldstack/heraldstack-firecracker/muse-code/glimmer
needs: quiet card. if the card is busy, skip this terminal.

prompt:

> for each png in
> ~/code/chasko-labs/nfl-big-data-bowl-2027/data/scratch/play\_\*.png,
> describe the football play in two sentences through the local
> endpoint at http://127.0.0.1:8181/v1: who has the ball, what the
> coverage looks like. save lines to /tmp/vision_batch.md. keep
> reasoning_strength low so it answers instead of thinking aloud.

intro (30s): "fourth terminal asks the local box to watch football."
+60min: read two descriptions aloud, show the plots they describe.
fallback: "card was busy — the deck already holds the vision numbers
slide from last run: 135 seconds, correct down to the subtitle."
