import sys
import string
sys.path += ["python"]

import matplotlib.pyplot as plt
from matplotlib import ticker
import pandas as pd
import figure_util

plt.style.use('paper/figstyle.mpl')


rules = list(range(2, 6))
species = list(range(3, 7))

fig, ax = plt.subplots(len(species), len(rules))

annotation = "$K_{{max}} = {0}$"
symbol_done = {"s":u"✔", "color":"darkgreen"}
symbol_notdone = {"s":u"✘", "color":"darkred"}
symbol_halfdone = {"s":u"🌗", "color":"orange"}


max_k_values = [[11, 11, 11, 6],
                [11, 10, 6,  3],
                [11, 9,  4,  1],
                [11, 8,  1,  1]]

print(plt.rcParams["font.family"])
for c, rule in enumerate(rules):
    for r, spec in enumerate(species):
        try:
            df = pd.read_csv(
                "paper/DivNsel_S{0}_R{1}/summary.tsv".format(spec, rule),
                sep="\t")
            ax[r, c].plot(df.index + 1, df["score"])
            
            # X ticks 
            xticks = [len(df) // 2, len(df)]
            ax[r, c].xaxis.set_major_locator(ticker.FixedLocator(xticks))
            ax[r, c].get_xticklabels()[-1].set_fontweight("heavy")
            ax[r, c].set_xlim(1, len(df) * 1.1)

            # Y ticks
            ymax = df["score"].max()
            special = -2
            if (ymax > 0.4) and (ymax < 0.51):
                yticks = [0, 0.25, ymax, 0.75, 1.0]
                special = -3
            elif (ymax > 0.55) and (ymax < 0.61):
                yticks = [0, 0.25, ymax, 1.0]
            elif ymax > 0.65:
                yticks = [0, 0.25, 0.5, ymax, 1.0]
            else:
                yticks = [i / 4 for i in range(5)]

            ax[r, c].yaxis.set_major_locator(ticker.FixedLocator(yticks))
            ax[r, c].yaxis.set_major_formatter(
                ticker.StrMethodFormatter("{x:0.2f}"))
            ax[r, c].get_yticklabels()[special].set_fontweight("heavy")


        except FileNotFoundError as e:
            print("No CRNs for S{0}_R{1}".format(spec, rule))
            yticks = [i / 4 for i in range(5)]
            ax[r, c].yaxis.set_major_locator(ticker.FixedLocator(yticks))
            ticks = [0, 1]
            ax[r, c].xaxis.set_major_locator(ticker.FixedLocator(ticks))
            ax[r, c].set_xlim(0, 1.1)
            #print(e)
            
        # add text
        anote = annotation.format(max_k_values[r][c])

        ax[r, c].annotate(
            anote,
            xy=(1.05, 0),
            xytext=(0.95, 0.90),
            textcoords='axes fraction',
            horizontalalignment='right',
            verticalalignment='top',
            fontsize="medium")
        
        symbol = symbol_halfdone
        if max_k_values[r][c] > 10:
            symbol = symbol_done
        elif max_k_values[r][c] == 1:
            symbol = symbol_notdone
        ax[r, c].text(
            x=0.90,
            y=0.75,
            transform=ax[r,c].transAxes,
            horizontalalignment='right',
            verticalalignment='top',
            fontsize="xx-large",
            fontname='Symbola',
            **symbol)

for a, l in zip(ax.flatten(), string.ascii_lowercase):
    a.set_ylim(0, 1.0)
    a.text(
        -0.45,
        1.0,
        l,
        horizontalalignment="center",
        verticalalignment="center",
        transform=a.transAxes,
        **figure_util.letter_labels)
    # a.set_xscale("log")
    # a.set_xlim(1,10**6)

for a, r in zip(ax[0, :], rules):
    a.set_title(str(r) + " Reactions")

for a in ax[-1, :]:
    a.set_xlabel("Number of CRNs")

for a, s in zip(ax[:, 0], species):
    a.set_ylabel("Optimised score")
    a.text(
        -0.7,
        0.5,
        str(s) + " Species",
        fontsize=plt.rcParams["axes.titlesize"],
        color="black",
        horizontalalignment="center",
        verticalalignment="center",
        rotation=90,
        transform=a.transAxes)

fig.set_size_inches(figure_util.cm2inch(12, 12))
#fig.tight_layout()
fig.subplots_adjust(
    left=0.14,  # the left side of the subplots of the figure
    right=0.98,  # the right side of the subplots of the figure
    bottom=0.07,  # the bottom of the subplots of the figure
    top=0.95,  # the top of the subplots of the figure
    wspace=0.55,
    # the amount of width reserved for blank space between subplots,
    # expressed as a fraction of the average axis width
    hspace=0.3
)  # the amount of height reserved for white space between subplots,

fig.savefig("div_overview.pdf", dpi=figure_util.dpi)  #bbox_inches="tight")
fig.savefig("div_overview.png", dpi=figure_util.dpi)  #bbox_inches="tight")
