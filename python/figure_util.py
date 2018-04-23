import string 

wide_figure = 18
medium_figure = 12
narrow_figure = 8

def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)


def shift_legend(ax, leg, xshift=0, yshift=0):
    bb = leg.get_bbox_to_anchor().inverse_transformed(ax.transAxes)
    bb.x0 += xshift
    bb.x1 += xshift
    bb.y0 += yshift
    bb.y1 += yshift
    leg.set_bbox_to_anchor(bb, transform = ax.transAxes)
    return leg, ax

dpi = 300

letters = string.ascii_lowercase

letter_labels = {"color": "black",
                 "fontsize": "large",
                 "weight": "bold"}