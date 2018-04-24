
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import os
import numpy as np

plt.style.use('paper/figstyle.mpl')
dpi = 300

import sys 
sys.path += ["python"]
from figure_util import shift_legend, cm2inch


speedac = pd.read_csv("paper/maximum_out_S4_R3/Bimol_1.speedtime", sep="\t")
speedac["N"] = speedac["i0"] + speedac["i1"]
N = 50
one_N = speedac[speedac["N"] == N].copy()

fig, ax = plt.subplots(1, 2)

plot_settings = {
                "linestyle" : "-",
                "marker" : "o",
                "markersize" : 3,
                "linewidth" : 0.5,
                "markerfacecolor" : "none",
                "markeredgewidth" : 0.5}

for i in one_N["i0"].unique():
    one_run = one_N[one_N["i0"] == i]
    one_run = one_run.sort_values(by="r0")
    ax[0].loglog(one_run["r0"], one_run["score"], 
                 label="A = {0}".format(int(i)),
                 **plot_settings)

    ax[1].loglog(one_run["r0"], one_run["opt_time"]*N,
                 label="A = {0}".format(int(i)),
                 **plot_settings)

ax[0].set_xlabel("Ratio of slow/fast reactions")
ax[0].set_ylabel("Accuracy")
#ax[0].legend(loc="lower center")
ax[0].text(-0.3, 1.1, "a", transform=ax[0].transAxes, fontsize=10)

ax[1].set_xlabel("Ratio of slow/fast reactions")
ax[1].set_ylabel("Expected halt time")
leg = ax[1].legend()
leg, ax[1] = shift_legend(ax[1], leg, yshift=0.1)
ax[1].text(-0.35, 1.05, "b", transform=ax[1].transAxes, fontsize=10)

fig.set_size_inches(cm2inch(7.9, 3.5))

#fig.tight_layout()
fig.subplots_adjust(left= 0.15,  # the left side of the subplots of the figure
                   right = 0.99,   # the right side of the subplots of the figure
                   bottom = 0.3,   # the bottom of the subplots of the figure
                   top = 0.85,      # the top of the subplots of the figure
                   wspace = 0.5,   # the amount of width reserved for blank space between subplots,
                                  # expressed as a fraction of the average axis width
                   hspace = 0.2)   # the amount of height reserved for white space between subplots,

fig.savefig("max_speedac.pdf", dpi=dpi)#bbox_inches="tight")
fig.savefig("max_speedac.png", dpi=dpi)#bbox_inches="tight")
