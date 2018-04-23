%% cme_am_time

clear all
close all

% load up the common figure text size settings
run ../figure_style;

load times1
left = 0.12;
bottom = 0.24;
top = 0.69;
width = 0.36;

fh = figure(1);
% fwidth = 700;
% fheight = fwidth/2;
% fh.Position = [100 100 fwidth fheight]; sf = fwidth/fheight;
% subplot('position',[left bottom+dy width width*sf])
%fh.Position = [100 100 650 225];


subplot('position',[left bottom width top])
ph1 = loglog(Ns,ts,'ko--','MarkerSize',3);
xlabel('Total molecules')
ylabel('Time (seconds)')
set(gca, ax_ticks_set{:})
box off
set(gca,'Xlim',[3 3e3],'Xtick',10.^(0:6),'Ylim',[0.1 1e5],'Ytick',10.^(-1:5))
ph1.YDataSource = 'tm';

subplot('position',[left+0.5 bottom width top])
ph2 = loglog(Ss,ts,'ko--','MarkerSize',3);
xlabel('Number of states')
ylabel('Time (seconds)')
set(gca, ax_ticks_set{:})
box off
set(gca,'Xlim',[10 3e6],'Xtick',10.^(0:6),'Ylim',[0.1 1e5],'Ytick',10.^(-1:5))

annotation('TextBox','String','a','EdgeColor','none','Position',[-0.02 0.99 0.05 0.05],Tset{:});
annotation('TextBox','String','b','EdgeColor','none','Position',[0.48 0.99 0.05 0.05],Tset{:});

%%
fh.Units = 'centimeters';
fh.Position = [3, 3, 7.9, 3.5];
save2pdf('../../paper/TimeCME',fh,300)

return