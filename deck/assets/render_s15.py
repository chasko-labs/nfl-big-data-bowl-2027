"""Slide 15 asset renderer. Real repo data only (session surface copy)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

NAVY = "#00002A"
INK = "#F0F0F0"
SECONDARY = "#C7B8E8"
VIOLET = "#9060F0"
GOLD = "#C9A23F"
ORANGE = "#FF9900"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Liberation Sans", "DejaVu Sans"],
    "font.serif": ["DejaVu Serif"],
    "font.monospace": ["JetBrainsMono NFM", "JetBrainsMono NFP",
                       "JetBrains Mono", "DejaVu Sans Mono"],
})

ROWS = [
    ("MCP read-only", "describe / list / get first; wire write access only when needed", VIOLET),
    ("sandbox", "reversible work runs free; destructive ops stay fenced", GOLD),
    ("/sessions", "every run logged; resume or audit any session", VIOLET),
    ("/rewind", "roll back to a checkpoint instead of patching forward", GOLD),
    ("evidence contract", "complete / evidence / unresolved via Spark API + Glimmer delegate", ORANGE),
]

fig, ax = plt.subplots(figsize=(16, 9), dpi=150)
fig.patch.set_facecolor(NAVY)
ax.set_facecolor(NAVY)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis("off")

# kicker: small, with a clear gap below it before the title
ax.text(0.9, 8.42, "SLIDE 15  |  TIPS: SESSION CONTROL",
        color=GOLD, fontsize=17, ha="left", va="center", weight="bold",
        family="sans-serif")
# one clear serif title line
ax.text(0.9, 7.72, "guard the run, keep the receipts",
        color=INK, fontsize=44, ha="left", va="center", weight="bold",
        family="serif")

top, height, gap = 6.75, 1.06, 0.20
for i, (head, sub, edge) in enumerate(ROWS):
    y0 = top - i * (height + gap) - height
    ax.add_patch(FancyBboxPatch((0.7, y0), 14.6, height,
                 boxstyle="round,pad=0.02,rounding_size=0.14",
                 facecolor="#0A0A33", edgecolor=edge, linewidth=2))
    ax.text(1.25, y0 + height - 0.30, "$ " + head,
            color=INK, fontsize=19, ha="left", va="center", weight="bold",
            family="monospace")
    ax.text(1.25, y0 + height - 0.58, sub,
            color=SECONDARY, fontsize=13.5, ha="left", va="top",
            family="sans-serif")

ax.text(0.9, 0.30,
        "source: real session surface -- read-only MCP, sandbox, /sessions, /rewind ship in the binary",
        color=GOLD, fontsize=11.5, ha="left", va="center", style="italic",
        family="sans-serif")

fig.savefig("/home/bryanchasko/code/chasko-labs/nfl-big-data-bowl-2027/deck/assets/s15_tips.png",
            facecolor=NAVY, bbox_inches="tight", pad_inches=0.15)
plt.close(fig)
print("s15 ok")
