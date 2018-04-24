
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
import os
import numpy as np

plt.style.use('paper/figstyle.mpl')
dpi = 300

import sys
sys.path += ["python"]
from figure_util import cm2inch

def get_dataset(workdir, filename="summary_archetype.tsv"):
    score_df = pd.read_csv(os.path.join(workdir, filename), sep="\t")
    print("All CRNs", len(score_df))
    unique = score_df[score_df["unique"]].copy()
    print("role isomorphic", len(unique))
    return unique

max_df = get_dataset("paper/maximum_out_S4_R3/") 

plt.rc('xtick', labelsize="x-small")  

fig, ax = plt.subplots(1, 1)

colorcyc = plt.rcParams['axes.prop_cycle'].by_key()['color']

# max_df.plot.bar(y=["score"], x=["CRN"],  ax=ax, width=0.6, color="lightblue", label="Optimized")
# max_df.plot.bar(y=["one"], x=["CRN"],  ax=ax, width=0.6, color="orange", label="Rate 1")
max_df.plot.bar(y=["score"], x=["CRN"],  ax=ax, width=0.7, color=colorcyc[0], label="Optimized")
max_df.plot.bar(y=["one"], x=["CRN"],  ax=ax, width=0.7, color=colorcyc[1], label="Rate 1")
ax.legend(["Optimized", "Rate 1.0"])
ax.set_ylabel("Accuracy")
ax.set_xlabel("CRN Number: Max$_{4,3}$ #")
#labels = ax.get_xticklabels()
labels = ax.get_xticklabels()
for i, l in enumerate(labels):
    x, y = l.get_position() #print(type(l))
    if i % 2 == 0:
        y += 0.03
    else :
        y -= 0.03
    l.set_rotation(0)
    l.set_position((x,y))
    #print(x,y)
    #print(l.position)
#print(labels)
#ax[0].set_ylim(bottom=0, top=1.0)
#ax[0].tick_params(axis='x', which='both', length=0)
#plt.setp(labels, rotation=90)

fig.set_size_inches(cm2inch(7.9, 3.5))

#fig.tight_layout()
fig.subplots_adjust(left= 0.12,  # the left side of the subplots of the figure
                    right = 0.99,   # the right side of the subplots of the figure
                    bottom = 0.26,   # the bottom of the subplots of the figure
                    top = 0.99,      # the top of the subplots of the figure
                    wspace = 0.2,   # the amount of width reserved for blank space between subplots,
                                   # expressed as a fraction of the average axis width
                    hspace = 0.2)   # the amount of height reserved for white space between subplots,

fig.savefig("max_overview.pdf", dpi=dpi)#bbox_inches="tight")
fig.savefig("max_overview.png", dpi=dpi)#bbox_inches="tight")