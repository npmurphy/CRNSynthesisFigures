function [headers,data] = importTSV(fname)

data = dlmread(fname,'\t',1,0);
fid = fopen(fname,'r');
headers = strsplit(fgetl(fid),'\t');
fclose(fid);

return