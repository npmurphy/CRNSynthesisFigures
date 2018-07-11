%% Run the separatrix code

clear
close all
warning off

% Define constants
N = 10;
k0 = 1;
k1 = 1;
k2 = 1;
rates_36 = [18.6, 2.4, 2.11];
rates_28 = [94.789589, 0.011370, 0.711251];
rates_one = [1, 1, 1];

letterlabx = -0.25;
letterlaby = 1.2;

% load up the common figure text size settings
figure_style;

% Prepare figure
left = 0.1;
bottom = 0.16;
width = 0.33;
dx = 0.5;
dy = 0.47;

%opt_des = ' (optimised rates)';
opt_des = ' (opt. rates)';


fh = figure(1);
fh.Units='centimeters';
fwidth = 7.9;
fheight = 8.6;
fh.Position = [2 2 fwidth fheight]; sf = fwidth/fheight;

subplot('position',[left bottom+dy width width*sf])
[hunst1,hstab1,hex1,hsep1,hdom1] = separatrix(36, N, rates_one);
set(gca, ax_ticks_set{:})
title('CRN #36 (rate 1)', ax_title_set{:})
text(letterlabx,letterlaby,'a', Tset{:}) 

subplot('position',[left+dy bottom+dy width width*sf])
[hunst2,hstab2,hex2,hsep2,hdom2] = separatrix(36, N, rates_36);
set(gca, ax_ticks_set{:})
title(['CRN #36' opt_des], ax_title_set{:})
text(letterlabx,letterlaby,'b', Tset{:})
leg_ax = gca;

subplot('position',[left bottom width width*sf])
[hunst3,hstab3,hex3,hsep3,hdom3] = separatrix(28, N, rates_one);
set(gca, ax_ticks_set{:})
title('CRN #28 (rate 1)', ax_title_set{:})
text(letterlabx,letterlaby,'c', Tset{:})

subplot('position',[left+0.5 bottom width width*sf])
[hunst4,hstab4,hex4,hsep4,hdom4] = separatrix(28, N, rates_28);
set(gca, ax_ticks_set{:})
title(['CRN #28' opt_des], ax_title_set{:})
text(letterlabx,letterlaby,'d', Tset{:})

lhs = [hstab4(1) hunst4(1) hex4(1) hdom4(1) hsep4(1) hsep4(3)];
les = {'Stable equilibria','Unstable equilibria','Examples','Initial conditions (A+B=N)','Separatrix 1','Separatrix 2'};
% left bottom width, height
%l = legend(lhs,les,'box','off','position',[0.9 0.84, 0.01 0.06]);
l = legendflex(lhs,les,'xscale',0.5,'nrow',2,'box','off');
l.Units='normalized';
l.Position=[0 0 1 0.06];

save2pdf('separatrices',fh,300)


return