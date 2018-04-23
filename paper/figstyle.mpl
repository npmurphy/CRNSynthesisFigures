# This was originally the ggplot style from matplotlib
# from http://www.huyng.com/posts/sane-color-scheme-for-matplotlib/

# More options here
# https://matplotlib.org/users/customizing.html

patch.linewidth: 0.5
patch.facecolor: 348ABD  # blue
patch.edgecolor: EEEEEE
patch.antialiased: True
mathtext.default : regular

font.size: 6.0
font.family : sans-serif
font.sans-serif : DejaVu Sans #Arial also had a unicode problem
font.style : normal
#font.family: Arial # specifiying this because Bitstream doesnt show unicode

# Font Sizes
# xx-small, x-small, small, medium, large, x-large, xx-large, smaller, larger.
axes.facecolor: white #E5E5E5
#axes.edgecolor: white
axes.edgecolor: black
axes.spines.right : False
axes.spines.top : False
axes.linewidth: 0.5
axes.grid: False
axes.titlesize: large
axes.labelsize: medium 
axes.labelcolor: 555555
axes.axisbelow: True       # grid/ticks are below elements (e.g., lines, text)


# matlab color cycle
axes.prop_cycle: cycler('color', ['0071BC', 'D85218', 'ECB01F', '7D2E8D', '76AB2F', '4CBDED', 'A1132E'])

#['E24A33', '348ABD', '988ED5', '777777', 'FBC15E', '8EBA42', 'FFB5B8'])
                   # E24A33 : red
                   # 348ABD : blue
                   # 988ED5 : purple
                   # 777777 : gray
                   # FBC15E : yellow
                   # 8EBA42 : green
                   # FFB5B8 : pink


xtick.color: 555555
xtick.major.width: 0.5
#xtick.direction: in
xtick.direction: out

ytick.color: 555555
ytick.major.width: 0.5
#ytick.direction: in
ytick.direction: out

#grid.color: white
grid.color: lightgray
grid.linestyle: :    # solid line

figure.facecolor: FFFFFF #white
figure.edgecolor: 0.50

figure.subplot.wspace  : 0.2


#legend.labelspacing 
#legend.borderpad
legend.fontsize : small


