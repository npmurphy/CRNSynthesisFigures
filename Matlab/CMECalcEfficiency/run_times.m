%% Time CME calculations for AM

clear all
close all

Ns = [10 15 20 30 50 70 100 150 200 300 500 700 1000 1500 2000];
N1 = length(Ns);
N2 = 4;
ts = nan(N1,N2); tm = nan(N1,1); Ss = nan(N1,1);

%%
fh = figure;
fh.Position = [100 100 600 250];
subplot('position',[0.09 0.18 0.38 0.74])
ph1 = loglog(Ns,tm,'ko--');
xlabel('Total molecules (N)')
ylabel('Time of calculation (sec)')
box off
set(gca,'Xlim',[3 3e3],'Xtick',10.^(0:6),'Ylim',[0.1 1e5],'Ytick',10.^(-1:5))
ph1.YDataSource = 'tm';
subplot('position',[0.59 0.18 0.38 0.74])
ph2 = loglog(Ss,tm,'ko--');
xlabel('Number of states (N)')
ylabel('Time of calculation (sec)')
box off
set(gca,'Xlim',[10 3e6],'Xtick',10.^(0:6),'Ylim',[0.1 1e5],'Ytick',10.^(-1:5))
ph2.YDataSource = 'tm';
ph2.XDataSource = 'Ss';
label('{\bfa}',[0 0.93 0.05 0.05]);
label('{\bfb}',[0.5 0.93 0.05 0.05]);

%%
tag3 = 'directive simulation cme';

for i = 1:N1
  tag1 = sprintf('directive sample %1.1f 500\n',100/Ns(i));
  tag2 = sprintf('directive parameters [X0 = %1.1f; Y0 = %1.1f]\n',Ns(i)*0.6,Ns(i)*0.4);
  
  fid = fopen('temp_parameters.lbs','w');
  fprintf(fid,[tag1 tag2 tag3]);
  fclose(fid);
  
  dos('copy /b temp_parameters.lbs+AM.lbs tempAM.lbs');
  for j = 1:N2
    [~,out] = dos('c:\clilbs\clilbs.exe tempAM.lbs -simulate','-echo');
    
    loc1 = strfind(out,'Number of states');
    loc2 = strfind(out,'Converting');
    loc3 = strfind(out,'Time elapsed');
    loc4 = strfind(out,'seconds');
    Ss(i) = str2num(out(loc1+18:loc2-2));
    ts(i,j) = str2num(out(loc3+32:loc4-2));
    save times Ns ts Ss tm
  end
  tm(i) = mean(ts(i,:));
  refreshdata;
end

return