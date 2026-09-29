"""Slide 9 + Slide 11 asset renderers. Real repo data only."""
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

NAVY = "#00002A"
LAV = "#D7C7EE"
GOLD = "#C9A23F"
VIOLET = "#9060F0"
DIM = "#8E84AE"
GREEN = "#7BD88F"

plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"]})

# ---------- Slide 9: real dry-run stdout as terminal ----------
TERMINAL_LINES = [
    ("$ ", "bash scripts/sweep_weeks.sh --dry-run", LAV),
    ("", "guard: snapshot of data/ at data/scratch/.guard_sweep.snap (82 files)", DIM),
    ("", "== sweep: speed ==", GOLD),
    ("", "[dry-run] muse exec: repo at $ROOT. read docs/data-guide.md", LAV),
    ("", "  and data/README.md first. input weeks: data/2024/", LAV),
    ("", "  tracking_week_1.csv through tracking_week_9.csv", LAV),
    ("", "  (chunked pandas reads, chunksize=200000). raw csvs read-only.", LAV),
    ("", "  q: per-week distribution of player speed (s) ->", LAV),
    ("", "  data/scratch/sweep_speed/speed.csv + speed.png", GREEN),
    ("", "guard: ok, data/ unchanged", DIM),
    ("", "== sweep: events ==", GOLD),
    ("", "[dry-run] muse exec: ... q: count non-null event tags per week", LAV),
    ("", "  -> data/scratch/sweep_events/events.csv + events.png", GREEN),
    ("", "guard: ok, data/ unchanged", DIM),
    ("", "== sweep: formations ==", GOLD),
    ("", "[dry-run] muse exec: ... join plays.csv on gameId+playId,", LAV),
    ("", "  first-down rate by offenseFormation per week", LAV),
    ("", "  -> data/scratch/sweep_formations/formations.csv + .png", GREEN),
    ("", "guard: ok, data/ unchanged", DIM),
    ("", "sweep done. promote keepers into .agents/skills/ or the pipeline.", GOLD),
]

fig, ax = plt.subplots(figsize=(16, 9), dpi=150)
fig.patch.set_facecolor(NAVY)
ax.set_facecolor(NAVY)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis("off")

# window chrome
ax.add_patch(FancyBboxPatch((0.4, 0.5), 15.2, 8.0, boxstyle="round,pad=0.08,rounding_size=0.25",
             facecolor="#0A0A33", edgecolor=VIOLET, linewidth=1.5))
for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
    ax.add_patch(Circle((0.95 + i * 0.42, 8.08), 0.12, color=c))
ax.text(8.0, 8.08, "sweep_weeks.sh --dry-run  |  guard_data.sh snapshot + check per prompt",
        color=DIM, fontsize=13, ha="center", va="center", family="monospace")
ax.plot([0.4, 15.6], [7.78, 7.78], color=VIOLET, lw=1, alpha=0.6)

y = 7.35
for prefix, body, color in TERMINAL_LINES:
    ax.text(0.75, y, prefix + body, color=color, fontsize=12.2,
            ha="left", va="top", family="monospace")
    y -= 0.335

ax.text(0.75, 0.78, "source: REAL stdout of `bash scripts/sweep_weeks.sh --dry-run` (82-file guard snapshot, 3 prompts, data/ unchanged)",
        color=GOLD, fontsize=11, ha="left", va="top", style="italic")
fig.savefig("/home/bryanchasko/code/chasko-labs/nfl-big-data-bowl-2027/deck/assets/s09_terminal.png",
            facecolor=NAVY, bbox_inches="tight", pad_inches=0.15)
plt.close(fig)
print("s09 ok")

# ---------- Slide 11: contest topic timeline 2019-2027 ----------
YEARS = [
    ("2019", "open\ninnovation", "concept"),
    ("2020", "rushing\nprediction", "prediction"),
    ("2021", "pass\ndefense", "concept"),
    ("2022", "special\nteams", "concept"),
    ("2023", "pass rush\n+ o-line", "metric"),
    ("2024", "tackling", "metric"),
    ("2025", "pre-snap", "concept"),
    ("2026", "movement\nprediction", "prediction"),
    ("2027", "ghost / kickoff?\nforecast", "forecast"),
]

fig2, ax2 = plt.subplots(figsize=(16, 9), dpi=150)
fig2.patch.set_facecolor(NAVY)
ax2.set_facecolor(NAVY)
ax2.set_xlim(0, 16)
ax2.set_ylim(0, 9)
ax2.axis("off")

ax2.text(8, 8.3, "BIG DATA BOWL 2019-2027: PREDICTION x METRIC ROTATION", color=LAV,
         fontsize=22, ha="center", va="center", weight="bold")
ax2.text(8, 7.82, "evidence: docs/history.md  |  forecast: docs/2027-prediction.md (ghost defenders, new kickoff, run blocking)",
         color=DIM, fontsize=12.5, ha="center", va="center", style="italic")

# rail
ax2.plot([0.7, 15.3], [4.4, 4.4], color=VIOLET, lw=4, alpha=0.9, solid_capstyle="round")
ax2.plot([0.7, 15.3], [4.4, 4.4], color=GOLD, lw=4, alpha=0.25, solid_capstyle="round")

n = len(YEARS)
xs = [1.15 + i * (14.1 / (n - 1)) for i in range(n)]
for x, (yr, topic, kind) in zip(xs, YEARS):
    up = (YEARS.index((yr, topic, kind)) % 2 == 0)
    if kind == "prediction":
        dot, ring = GOLD, GOLD
    elif kind == "forecast":
        dot, ring = NAVY, GOLD
    else:
        dot, ring = VIOLET, VIOLET
    ax2.add_patch(Circle((x, 4.4), 0.34, color=dot, ec=ring, lw=2.5, zorder=5))
    if kind == "forecast":
        ax2.text(x, 4.4, "?", color=GOLD, fontsize=20, ha="center", va="center", weight="bold", zorder=6)
    # year label toward rail, topic away
    yy = 3.55 if up else 5.25
    ty = 2.55 if up else 6.25
    ax2.plot([x, x], [4.05 if up else 4.75, yy + (0.3 if up else -0.3)], color=ring, lw=1.6, alpha=0.9)
    ax2.text(x, yy, yr, color=LAV if kind != "forecast" else GOLD, fontsize=17,
             ha="center", va="center", weight="bold")
    ax2.text(x, ty, topic, color=LAV if kind != "forecast" else GOLD, fontsize=12.5,
             ha="center", va="center", linespacing=1.3,
             style="italic" if kind == "forecast" else "normal",
             bbox=dict(boxstyle="round,pad=0.35", facecolor="#0A0A33", edgecolor=ring, lw=1.2))

# legend
lx = 1.0
for label, c in [("prediction year", GOLD), ("metric / concept year", VIOLET), ("2027 forecast", GOLD)]:
    ax2.add_patch(Circle((lx, 1.15), 0.16, color=c if label != "2027 forecast" else NAVY, ec=c, lw=2))
    ax2.text(lx + 0.32, 1.15, label, color=LAV, fontsize=13, ha="left", va="center")
    lx += 3.6
ax2.text(8, 0.55, "sources: docs/history.md + docs/2027-prediction.md", color=DIM,
         fontsize=11, ha="center", va="center", style="italic")

fig2.savefig("/home/bryanchasko/code/chasko-labs/nfl-big-data-bowl-2027/deck/assets/s11_forecast.png",
             facecolor=NAVY, bbox_inches="tight", pad_inches=0.15)
plt.close(fig2)
print("s11 ok")
