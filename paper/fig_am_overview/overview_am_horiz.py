import sys
import os.path

import matplotlib.patches as patches
from matplotlib import gridspec
import matplotlib.pyplot as plt
import pandas as pd
#from mpl_toolkits.axes_grid1.inset_locator import mark_inset, zoomed_inset_axes

sys.path += ["python"]
from figure_util import cm2inch, shift_legend
import figure_util

plt.style.use('paper/figstyle.mpl')
dpi = 300


def get_dataset(workdir, filename="summary_archetype.tsv"):
    score_df = pd.read_csv(os.path.join(workdir, filename), sep="\t")
    return score_df[score_df["unique"]].copy()


colorcyc = plt.rcParams['axes.prop_cycle'].by_key()['color']

am33 = get_dataset("paper/AMno11_S3_R3")
am44 = get_dataset("paper/AMno11_S4_R4", filename="summary_unique_subnets.tsv")

fig = plt.figure()
gs = gridspec.GridSpec(2, 2)
ax33 = plt.subplot(gs[0, 0])
ax44 = plt.subplot(gs[0, 1])
axLong = plt.subplot(gs[1, :])
ax = [ax33, ax44, axLong]

#we dont mark these at the moment.
am33_36 = am33[am33["CRN"] == 36].to_dict('list')["score"][0]
am33_28 = am33[am33["CRN"] == 28].to_dict('list')["score"][0]

ax33.set_title("AM$_{3,3}$ CRNs before and after optimization")
am33.plot.bar(
    y=["score"],
    x=["CRN"],
    ax=ax33,
    width=0.5,
    color=colorcyc[0],
    label="Optimized")
am33.plot.bar(
    y=["one"],
    x=["CRN"],
    ax=ax33,
    width=0.5,
    color=colorcyc[1],
    label="Rate 1")

leg = ax33.legend(["Optimized", "Rate 1"])

ax33.set_ylim(bottom=0, top=1.0)
ax33.tick_params(axis='x', which='both', direction="out")
labels = ax33.get_xticklabels()
plt.setp(labels, rotation=0)
ax33.set_ylabel("Accuracy")
ax33.set_xlabel("CRN Number: AM$_{3,3}$ #")
# Stars to show the CRNs groups in panel d
# top of column
# ax[0].plot(0,  am33_28, '*', color="blue", alpha=0.4)
# ax[0].plot(1,  am33_36 , '*', color="red", alpha=0.4)
# bottom of columns
# ax[0].plot(0.0,  0.1, '*', color="blue", alpha=0.8, markeredgecolor="none")
# ax[0].plot(1.0,  0.1, '*', color="red",  alpha=0.8, markeredgecolor="none")
# ax[0].plot(0.0,  1.01, '*', color="blue", alpha=0.8, markeredgecolor="none")
# ax[0].plot(1.0,  1.01, '*', color="red",  alpha=0.8, markeredgecolor="none")
# colored labels
#ax33.tick_params(axis='x', which='both', direction='out')
ax33.get_xticklabels()[0].set_color(colorcyc[4])
ax33.get_xticklabels()[0].set_fontweight("heavy")
ax33.get_xticklabels()[1].set_color(colorcyc[3])
ax33.get_xticklabels()[1].set_fontweight("heavy")
#############################
## here is am 44 overview
#############################
ax44.set_title("AM$_{4,4}$ CRNs before and after optimization")
ax44.plot(
    am44["score"],
    label="Optimized",
    marker="o",
    markersize=3,
    color=colorcyc[0],
    markeredgecolor="none",
    linestyle="none")
ax44.plot(
    am44["one"],
    label="Rate 1",
    marker="o",
    markersize=3,
    color=colorcyc[1],
    alpha=0.3,
    markeredgecolor="none",
    linestyle="none")
ax44.add_patch(
    patches.Rectangle(
        xy=(0, 0.9),
        width=123,
        height=0.1,
        fill=False,
        zorder=5,
        color="black"))
ax44.set_xlim(left=0)
ax44.set_ylim(bottom=0, top=1.0)
ax44.set_ylabel("Accuracy")
ax44.set_xlabel("Number of CRNs")


#############################
## here is the top am 44 close up
#############################
spiritually_similar_to_asym = [4854, 5308, 6238, 5050, 4540, 5108, 6264, 3471]
spiritually_similar_to_am = [
    6472, 6448, 6468, 6427, 6367, 6377, 6477, 6335, 6421
]
spiritually_hard_to_say = [
    5024,  # this is like AM33 but it aslo aysmetric
    5007,  # this like asym but broken
    4973,  # like asym but very strange, maybe a new type? 
    6293,  # kinda asym, kinda am but broken. 
]

am44["look_like_asym"] = False
am44.ix[am44["CRN"].isin(spiritually_similar_to_asym), "look_like_asym"] = True
am44.ix[am44["CRN"].isin(spiritually_similar_to_am), "look_like_am"] = True

am44["am33score"] = am44["score"] * am44["hasAM33"]
am44["am33asymscore"] = am44["score"] * am44["has_asym33"]
am44["no_catagory_score"] = am44["score"] * (
    ~(am44["hasAM33"] | am44["has_asym33"]))
# am44["am33asym_sipr_score"] = am44["look_like_asym"] * am44["score"]
# am44["am33am_sipr_score"] = am44["look_like_am"] * am44["score"]
good_enough = (am44[am44["score"] > 0.90])  # 0.93 is how good am33 was
good_enough.plot.bar(
    x=["CRN"],
    y=["no_catagory_score"],
    color=colorcyc[2],
    ax=axLong,
    width=0.75)
good_enough.plot.bar(
    x=["CRN"], y=["am33score"], color=colorcyc[3], ax=axLong, width=0.75)
good_enough.plot.bar(
    x=["CRN"], y=["am33asymscore"], color=colorcyc[4], ax=axLong, width=0.75)
# good_enough.plot.bar(x=["CRN"], y=["am33asym_sipr_score"], color="blue",  ax=ax[2], width=0.80, alpha=0.5)
# good_enough.plot.bar(x=["CRN"], y=["am33am_sipr_score"], color="red",  ax=ax[2], width=0.80, alpha=0.5)
natnano_score = am33[am33["CRN"] == 36].to_dict('list')
asymbest_score = am33[am33["CRN"] == 28].to_dict('list')
print(natnano_score)

#3860 is in both 
am44_3860 = am44[am44["CRN"] == 3860]#.to_dict('list')["score"][0]
x_both = am44_3860.index
y_both = am44_3860.to_dict('list')["score"][0]
print(x_both)
print(y_both)
axLong.plot(x_both, y_both + 0.003, 'o', color=colorcyc[3], markeredgecolor="none", markersize=4)


#axLong.set_title(r"AM$_{4,4}$ CRNs ≤ $\geq 0.9$ after optimization")
axLong.set_title(r"AM$_{4,4}$ CRNs ≥ 0.9 after optimization")
axLong.axhline(y=natnano_score["score"], linewidth=1.0, linestyle=":", color=colorcyc[3])
axLong.axhline(y=asymbest_score["score"],linewidth=1.0, linestyle=":", color=colorcyc[4])
#.to_dict('list')
leg2 = axLong.legend([
    "also AM$_{3,3}$ #36 subnet",
    "AM$_{3,3}$ #36 score",  # opt'd score",
    "AM$_{3,3}$ #28 score",  # opt'd score",
    "No category",
    "AM$_{3,3}$ #36 subnet",
    "AM$_{3,3}$ #28 subnet",
])
legr2, ax[2] = shift_legend(ax[2], leg2, yshift=0.14)
axLong.set_ylim(0.90, 1.0)
axLong.set_ylabel("Accuracy")
axLong.tick_params(axis="x", labelsize="x-small")  #xticklabels(labels, fontsize='small')
axLong.xaxis.grid(False)
axLong.set_xlabel("CRN Number: AM$_{4,4}$ #")
axLong.tick_params(axis='x', which='both', direction='out', length=2, pad=0)
labels = axLong.get_xticklabels()
plt.setp(labels, rotation=80)

for a, l in zip(ax[:2], figure_util.letters):
    a.text(-0.16, 1.0, l, transform=a.transAxes, fontsize="x-large")
a, l = ax[2], figure_util.letters[2]
a.text(-0.07, 1.0, l, transform=a.transAxes, fontsize="x-large")

#fig.tight_layout()
fig.subplots_adjust(left= 0.08,  # the left side of the subplots of the figure
                    right = 0.98,   # the right side of the subplots of the figure
                    bottom = 0.11,   # the bottom of the subplots of the figure
                    top = 0.93,      # the top of the subplots of the figure
                    wspace = 0.3,   # the amount of width reserved for blank space between subplots,
                                   # expressed as a fraction of the average axis width
                    hspace = 0.5)   # the amount of height reserved for white space between subplots,
#fig.set_size_inches(cm2inch(7.9, 12))
fig.set_size_inches(cm2inch(figure_util.wide_figure, 7.9))
name = "am_overview_horiz"
fig.savefig(name + ".pdf", dpi=dpi)  #bbox_inches="tight")
fig.savefig(name + ".png", dpi=dpi)  #bbox_inches="tight")
