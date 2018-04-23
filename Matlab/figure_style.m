%%font_scalings
xx_small = 0.579;
x_small = 0.694;
small = 0.833;
medium = 1.0;
large = 1.200;
x_large = 1.440;
xx_large = 1.728;

% base font size
font_size = 8;

% Big letters indicating subplot 
Tset(:,1) = {'Units'; 'Normalized'};
Tset(:,2) = {'VerticalAlignment'; 'Top'};
Tset(:,3) = {'FontWeight'; 'bold'};
Tset(:,4) = {'FontSize'; font_size*large};

%title text size
ax_title_set(:,1) = {'Units'; 'Normalized'};
ax_title_set(:,2) = {'VerticalAlignment'; 'Bottom'};
ax_title_set(:,3) = {'HorizontalAlignment'; 'Center'};
ax_title_set(:,4) = {'FontWeight'; 'bold'};
ax_title_set(:,5) = {'FontSize'; font_size};

%x y ticks 
ax_ticks_set(:,1) = {'FontWeight'; 'normal'};
ax_ticks_set(:,2) = {'FontSize'; font_size*small};