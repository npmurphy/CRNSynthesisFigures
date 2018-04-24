%% Create AM heat map figures for paper

clear all
close all
saving = 1;   % Set to 1 to write PDF output


%datadir = '../paper/AMno11_S4_R4/'; withtime = 1;
datadir = '../paper/AMno11_S3_R3/'; withtime = 1;
%datadir = '../paper/DivNsel_S4_R4/'; withtime = 0;
%datadir = '../paper/DivNsel_S5_R4/'; withtime = 0;
%datadir = '../paper/DivNsel_leader/'; withtime = 0;


% Write an array of files to process
files = dir([datadir 'Bimol_*.tsv']);
Nf = length(files);

% Input dimensions
A = (1:20)'; NA = length(A);
B = (1:20)'; NB = length(B);
One = ones(NA*NB,1);

% Figure dimensions
if withtime
  left = 0.06; lleft = 0.62;
  width = 0.24;
  dx = 0.3;
  fwidth = 850;
else
  left = 0.08; lleft = 0.92;
  width = 0.36;
  dx = 0.45;
  fwidth = 600;
end
height = 0.73;
bottom = 0.17;
msize = 30;
titles = {'Before optimisation (rate 1.0)','After optimisation'};

for f = 1:Nf
  dataIn = dlmread([datadir files(f).name],'\t'); %, 1, 0);
  A = dataIn(:,1);
  B = dataIn(:,2);
  num_cols_p1 = size(dataIn,2) +1;
  fh(f) = figure(f);
  %fh(f).Position = [100 100 600 250];
  set(fh(f),'position',[100 100 fwidth 250]);
  colormap(jet);

  for j = 1:2
    Out = dataIn(:,num_cols_p1-j);
        
    subplot('position',[left+(j-1)*dx bottom width height]) 

    hold on
    
    
      
    if ~isempty(strfind(datadir, 'div'))
        rectangle('Position',[0.5,0.5,10,10], 'FaceColor',[0.8 0.8 0.8],'EdgeColor','k')
    elseif ~isempty(strfind(datadir, 'AMno11'))
        %rectangle('Position',[0.5,0.5,5,5], 'FaceColor',[0.8 0.8 0.8],'EdgeColor','k')
        %rectangle('Position',[5.5,5.5,5,5], 'FaceColor',[0.8 0.8 0.8],'EdgeColor','k')
        pg_x = [ 0.5, 0.5, 5.5, 5.5, 8.5, 8.5, 1.5, 1.5, 0.5 ];
        pg_y = [ 1.5, 8.5, 8.5, 5.5, 5.5, 0.5, 0.5, 1.5, 1.5 ];
        fill(pg_x, pg_y,[0.8 0.8 0.8]); %, 'EdgeColor', 'k')
        pw_x = [ 6.5,  6.5,  7.5, 7.5, 6.5];
        pw_y = [ 7.5, 10.5, 10.5, 7.5, 7.5];
        fill(pw_x, pw_y, [0.8 0.8 0.8]); %, 'EdgeColor', 'k')
        fill(pw_y, pw_x, [0.8 0.8 0.8]); %, 'EdgeColor', 'k')
    elseif ~isempty(strfind(datadir, 'DivNsel'))
        %rectangle('Position',[0.5,0.5,5,5], 'FaceColor',[0.8 0.8 0.8],'EdgeColor','k')
        %rectangle('Position',[5.5,5.5,5,5], 'FaceColor',[0.8 0.8 0.8],'EdgeColor','k')
        Ap = [ 3, 4, 11, 14, 7, 11, 12, 15, 4, 8, 9, 12, 5, 10, 15, 16, 1, 2, 2  1];
        Bp = [ 2, 2, 2,   2, 3,  3,  3,  3, 4, 4, 4,  4, 5,  5,  5,  5, 2, 3, 4, 5];
        for i = 1:length(Ap)
            Ax = Ap(i);
            By = Bp(i);
            pg_x = [ Ax-0.5, Ax-0.5, Ax+0.5, Ax+0.5, Ax-0.5];
            pg_y = [ By-0.5, By+0.5, By+0.5, By-0.5, By-0.5]; 
            fill(pg_x, pg_y, [0.8 0.8 0.8]); %, 'EdgeColor', 'k')
        end 
    end
    scatter3(A(:),B(:),Out,msize*One,Out,'filled','s')

    view([0 90])
    axis([-0.5 20.5 -0.5 20.5])
    caxis([0 1])
    box off
    xlabel('Input A')
    ylabel('Input B')
    title(titles{j})
  end
  %annotation('textbox',[0.3 0.95 0.4 0.05],'String',files(f).name,'EdgeColor','none','HorizontalAlignment','center','FontWeight','bold')
  hc = colorbar;  
  set(hc,'position',[lleft bottom 0.02 height]);
  
  % Time calculations?
  tfile = strrep(files(f).name,'.tsv','.time');
  if (exist([datadir tfile], 'file') && withtime)
    %timeIn = dlmread([datadir tfile],'\t', 1, 0);
    timeIn =  bioma.data.DataMatrix('File', [datadir tfile], 'Delimiter', '\t');
    n = timeIn(:,'i0') + timeIn(:,'i1'); % multiply by N to compare with complexity measure 
    subplot('position',[left+2*dx+0.08 bottom width height])
    loglog(n,n.*timeIn(:,'opt_time'),'kx')
    hold on
    loglog(n,n.*timeIn(:,'one_time'),'ko','MarkerFaceColor','k','MarkerSize',3)
    %set(gca,'YMinorTick','on'); % didnt work, want more ticks on y axis. 
    demo_lin = logspace(1,4,100);
    loglog(demo_lin, demo_lin)
    loglog(demo_lin, log(demo_lin))
    hold off
    ylabel('Expected absorption time')
    xlabel('Total molecule counts (n)')
    box off
    ylim([0.1 1e5])
  end
  drawnow;
  
  if saving
    set(gcf,'PaperPositionMode','auto')
    save2pdf([datadir strrep(files(f).name,'.tsv','')],fh(f),300)
  end
end

return
