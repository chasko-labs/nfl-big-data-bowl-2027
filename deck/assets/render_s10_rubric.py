"""Slide 10 rubric asset renderer. Real repo data only (docs/craft.md: 30/30/20/20)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

NAVY = "#00002A"
VIOLET = "#9060F0"
GOLD = "#C9A23F"
ORANGE = "#FF9900"
INK = "#F0F0F0"
SECONDARY = "#C7B8E8"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial"],
    "font.serif": ["DejaVu Serif"],
    "font.monospace": ["DejaVu Sans Mono", "JetBrains Mono"],
})

# values from docs/craft.md: football 30 / data science 30 / report 20 / visualization 20
LABELS = ["Football", "Data Science", "Report", "Visualization"]
VALUES = [30, 30, 20, 20]
COLORS = [VIOLET, VIOLET, SECONDARY, SECONDARY]

fig, ax = plt.subplots(figsize=(16, 9), dpi=150)
fig.patch.set_facecolor(NAVY)
ax.set_facecolor(NAVY)

y = range(len(LABELS))
bars = ax.barh(list(y), VALUES, color=COLORS, edgecolor=ORANGE, linewidth=1.2, height=0.55)

ax.set_yticks(list(y))
ax.set_yticklabels(LABELS, color=INK, fontsize=16, family="sans-serif")
ax.set_xlabel("Points", color=INK, fontsize=16, family="sans-serif")
ax.set_title("Judging rubric - 100 points total", color=INK, fontsize=24,
             family="serif", loc="left", pad=18)
ax.set_xlim(0, 38)
ax.tick_params(axis="x", colors=INK, labelsize=13)
for lbl in ax.get_xticklabels():
    lbl.set_family("monospace")
ax.grid(axis="x", color=VIOLET, alpha=0.25, linewidth=0.8)
ax.set_axisbelow(True)
for spine in ax.spines.values():
    spine.set_color(ORANGE)
    spine.set_alpha(0.6)

for bar, v in zip(bars, VALUES):
    ax.text(bar.get_width() + 0.7, bar.get_y() + bar.get_height() / 2, str(v),
            color=GOLD, fontsize=17, weight="bold", va="center", ha="left",
            family="monospace")

ax.text(37.5, -1.15, "source: docs/craft.md - football 30 / data science 30 / report 20 / visualization 20",
        color=SECONDARY, fontsize=12, ha="right", va="top", style="italic")

# FIX: generous left margin so y-axis labels are never clipped
fig.subplots_adjust(left=0.24, right=0.95, top=0.88, bottom=0.12)

fig.savefig("/home/bryanchasko/code/chasko-labs/nfl-big-data-bowl-2027/deck/assets/s10_rubric.png",
            facecolor=NAVY)
plt.close(fig)
print("s10 ok")
