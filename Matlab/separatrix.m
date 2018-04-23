function [hunst,hstab,hex,hsep,hdom] = separatrix(system,N, rates)
%% Plot the separatrix for a specified bistable CRN
marker_size = 4;
rates_c = num2cell(rates);
[k0 k1 k2] = rates_c{:}; 
% Specify the system equations
switch system
  case 36
    % A + B ->{k0} 2I
    % A + I ->{k1} 2A
    % B + I ->{k2} 2B
%     k0 = 18.6;
%     k1 = 2.4;
%     k2 = 2.11;
    fA = @(A,B) A.*(k1*(N-A-B) - k0*B);
    fB = @(A,B) B.*(k2*(N-A-B) - k0*A);
    saddle = N/(1+(k1+k0)/k2)*[1;k1/k2];
  case 28
    % A + B ->{k0} 2I
    % 2I ->{k1} 2A
    % B + I ->{k2} 2B
%     k0 = 94.789589;
%     k1 = 0.011370;
%     k2 = 0.711251;
    fA = @(A,B) 2*k1*(N-A-B).*(N-A-B) - k0*A.*B;
    fB = @(A,B) B.*(k2*(N-A-B) - k0*A);
    saddle = N/(k0*(k1+k2)+k2^2)*[k2^2;2*k0*k1];
end

% Specify the location of the saddle point
stableA = [N;0];
stableB = [0;N];

% Do some numerical integration, starting from around the saddle
tmax = 10/N;
eps = 0.001*N;
[~,xf1] = ode15s(@(t,x)[fA(x(1),x(2));fB(x(1),x(2))],[0 100]*tmax,saddle+[eps;-eps]);
[~,xf2] = ode15s(@(t,x)[fA(x(1),x(2));fB(x(1),x(2))],[0 100]*tmax,saddle+[-eps;eps]);
[~,xb1] = ode15s(@(t,x)[fA(x(1),x(2));fB(x(1),x(2))],[0 -100]*tmax,saddle+[eps;eps]);
[~,xb2] = ode15s(@(t,x)[fA(x(1),x(2));fB(x(1),x(2))],[0 -100]*tmax,saddle+[-eps;-eps]);

% Do a couple of examples
[~,xe1] = ode15s(@(t,x)[fA(x(1),x(2));fB(x(1),x(2))],(0:0.001:1)*tmax,[0.1;0.2]*N);
[~,xe2] = ode15s(@(t,x)[fA(x(1),x(2));fB(x(1),x(2))],(0:0.001:1)*tmax,[0.6;0.4]*N);

%% Create plot

dx = N/20;
[x0,y0] = meshgrid(0:dx:N,0:dx:N);
locs = find((x0+y0<=N));
x = x0(locs);
y = y0(locs);
u = fA(x,y);
v = fB(x,y);
A = lines(2);

quiver(x,y,u,v)
hold on
hdom = plot(0:N,N:-1:0,'k--');
hunst(1) = plot(saddle(1),saddle(2),'ko', 'markers',marker_size);
switch system
  case 1
    hunst(2) = plot(0,0,'ko', 'markers',marker_size);
  case 2
end
hstab(1) = plot(stableA(1),stableA(2),'ko','MarkerFaceColor','k', 'markers',marker_size);
hstab(2) = plot(stableB(1),stableB(2),'ko','MarkerFaceColor','k', 'markers',marker_size);
xf1(xf1<1e-8)=0;
hsep(1) = plot(xf1(:,1),xf1(:,2),'Color',A(1,:));   % Towards A
hsep(2) = plot(xf2(:,1),xf2(:,2),'Color',A(1,:));   % Towards B
locs1 = find(xb1(:,1)+xb1(:,2)<=N);
xb1s1 = [xb1(locs1,1);N/2];
xb1s2 = [xb1(locs1,2);interp1(xb1(:,1),xb1(:,2),N/2)];
hsep(3) = plot(xb1s1,xb1s2,'Color',A(2,:));   % Towards (inf,inf)
hsep(4) = plot(xb2(:,1),xb2(:,2),'Color',A(2,:));   % Towards (0,0)
hex(1) = plot(xe1(:,1),xe1(:,2),'k');   % Example 1
plot(xe1(1,1),xe1(1,2),'k.');
%quiver(xe1(1:10:end,1),xe1(1:10:end,2),fA(xe1(1:10:end,1),xe1(1:10:end,2)),fB(xe1(1:10:end,1),xe1(1:10:end,2)),0.3,'Color','k','MaxHeadSize',0.1)

hex(2) = plot(xe2(:,1),xe2(:,2),'k');   % Example 2
plot(xe2(1,1),xe2(1,2),'k.');
%quiver(xe2(1:10:end,1),xe2(1:10:end,2),fA(xe2(1:10:end,1),xe2(1:10:end,2)),fB(xe2(1:10:end,1),xe2(1:10:end,2)),0.3,'Color','k','MaxHeadSize',1)
hold off
box off
axis([0 N 0 N])
xlabel('A')
ylabel('B')
set(gca,'TickDir','out')

return