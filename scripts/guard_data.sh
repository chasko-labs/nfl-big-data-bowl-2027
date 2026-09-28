#!/usr/bin/env bash
# mtime canary: fail loudly if data/ changed during a run.
# usage: guard_data.sh snapshot <statefile>  # before the run
#        guard_data.sh check <statefile>     # after each step
set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

snap() {
	# raw inputs only: data/scratch/ is the write sink, its churn is expected
	find "$ROOT/data" -path "$ROOT/data/scratch" -prune -o -type f -printf '%p %s %T@\n' 2>/dev/null | sort
}

case "${1:-}" in
snapshot)
	snap >"${2:?statefile required}"
	echo "guard: snapshot of data/ at $2 ($(wc -l <"$2") files)"
	;;
check)
	state="${2:?statefile required}"
	[ -f "$state" ] || {
		echo "guard: FAIL, no snapshot at $state, refusing to trust data/"
		exit 1
	}
	tmp="$(mktemp)"
	snap >"$tmp"
	if ! diff -q "$state" "$tmp" >/dev/null; then
		echo "guard: FAIL, data/ changed mid-run. diff:"
		diff "$state" "$tmp" | head -20
		rm -f "$tmp"
		exit 1
	fi
	rm -f "$tmp"
	echo "guard: ok, data/ unchanged"
	;;
*)
	echo "usage: guard_data.sh snapshot|check <statefile>"
	exit 2
	;;
esac
