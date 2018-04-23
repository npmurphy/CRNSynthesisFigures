%% Timings figure for Z3

clear all
close all

datadir = '../paper/AMno11_z3_timmings/';
files = {'ApproximateMajorityNo11_3_3','ApproximateMajorityNo11_4_3','ApproximateMajorityNo11_3_4','ApproximateMajorityNo11_4_4'};

left = 0.11;
bottom = 0.22;
width = 0.37;
height = 0.7;

figure_style;

colors = lines(4);

fh = figure(1);
fh.Units='centimeters';
fwidth = 7.9;
fheight = 4;
fh.Position = [2 2 fwidth fheight];

subplot('position',[left bottom width height])
hold on
min_k = 1;
max_k = 9;
for i = 1:length(files)
  data = dlmread([datadir files{i} '.tsv'],'\t');
  data(:,2) = data(:,2) -1;
  t0 = 0;
  times = [];
  for j =  min(data(:,2)):max(data(:,2))
    times = [times; data(data(:,2)==j,3)+t0];
    t0 = times(end);
  end
  Nt = length(times);
  Nsol(i,:) = hist(data(:,2),min_k:max_k);
  
  loglog(times,1:Nt,'.-','Color',colors(i,:))
end
hold off
set(gca,'XScale','log','Yscale','log','Xtick',10.^(0:4))
xlabel('Time (seconds)')
ylabel('Number of solutions')
set(gca, ax_ticks_set{:})
hl = legendflex({'AM_{3,3}','AM_{4,3}','AM_{3,4}','AM_{4,4}'},'xscale',0.5,'box','off');
hl.Units = 'normalized';
hl.Position = [0.32 bottom 0.15 0.4];

%
subplot('position',[left+0.5 bottom width height])
bar(min_k:max_k,fliplr(Nsol'),1)
set(gca,'Yscale','log', 'Xlim',[min_k-1.0 max_k])
% x-axis ticks looked like tiny bar chart
ax = get(gca);
set(ax.XAxis,'TickLength',[0 0])


colormap(flipud(colors))
box off
xlabel('K')%, ax_ticks_set{:})
ylabel('Number of solutions')
set(gca, ax_ticks_set{:})

annotation('TextBox','String','a','EdgeColor','none','Position',[-0.02 0.99 0.05 0.05],Tset{:});
annotation('TextBox','String','b','EdgeColor','none','Position',[0.48 0.99 0.05 0.05],Tset{:});

%% Save
save2pdf('../paper/z3_time',fh,300)

return