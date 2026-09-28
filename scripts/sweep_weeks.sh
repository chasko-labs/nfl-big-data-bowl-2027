#!/usr/bin/env bash
# batch exploration: one muse exec prompt per question across all weeks.
# each prompt writes its own csv + png under data/scratch/sweep_<name>/.
# guard_data.sh snapshots data/ first and re-checks after every prompt;
# the sweep aborts if raw inputs moved mid-run.
# usage: scripts/sweep_weeks.sh [--dry-run]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="${BDB_DATA:-data/2024}"
OUT="$ROOT/data/scratch"
CANARY="$OUT/.guard_sweep.snap"
DRY=0
[ "${1:-}" = "--dry-run" ] && DRY=1

scripts/guard_data.sh snapshot "$CANARY"

run_q() {
	name="$1"
	prompt="$2"
	echo "== sweep: $name =="
	if [ "$DRY" = 1 ]; then
		echo "[dry-run] muse exec: $prompt"
	else
		muse exec "$prompt"
	fi
	scripts/guard_data.sh check "$CANARY"
}

base="repo at $ROOT. read docs/data-guide.md and data/README.md first. \
input weeks: $DATA/tracking_week_1.csv through tracking_week_9.csv \
(chunked pandas reads, chunksize=200000). raw csvs are read-only."

run_q speed "$base question: per-week distribution of player speed (s). \
write one csv (week, mean_s, p50_s, p95_s) to $OUT/sweep_speed/speed.csv \
and one png of weekly means to $OUT/sweep_speed/speed.png."

run_q events "$base question: count non-null event tags per week \
(snap, tackles, catches...). write counts csv to \
$OUT/sweep_events/events.csv and a bar png to $OUT/sweep_events/events.png."

run_q formations "$base question: join plays.csv on gameId+playId, \
first-down rate (playResult >= yardsToGo, yardsGained fallback) by \
offenseFormation per week. write csv to \
$OUT/sweep_formations/formations.csv and a png to \
$OUT/sweep_formations/formations.png."

echo "sweep done. promote keepers into .agents/skills/ or the pipeline."
