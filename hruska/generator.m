%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% linearni kongruentni generator nahodnych cisel
%%% parametry linearni koeficient, konstantni koeficient a seed 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function fce=generator(a,c,seed)     

close all;

n=100000;
m=2^31-1;

krok = linspace(1,n,n);
y = zeros(n,1);
x = zeros(n,1);

y(1) = seed;
x(1) = y(1)/n;

for i=2:n
   y(i)=mod(a*y(i-1)+c,m);                
   x(i)=y(i)/m;
end

fig1=figure(1);
plot(krok,x,'b.')
axis([0 n 0 1]);
xlabel('n');
ylabel('x');
title('generátor');
grid off;
set(fig1,'PaperUnits','inches');
set(fig1,'PaperOrientation','landscape');
set(fig1,'PaperSize',[10,6]);
set(fig1,'PaperPosition',[0,0,10,6]);
print(fig1,'-dpng','-color','-FArial:14','generator-graph');

fig2=figure(2);
hist(x,1000,"facecolor", "r", "edgecolor", "r")
axis([0 1 70 130]);
xlabel('x');
ylabel('èetnosti');
title('histogram');
grid off;
set(fig2,'PaperUnits','inches');
set(fig2,'PaperOrientation','landscape');
set(fig2,'PaperSize',[10,6]);
set(fig2,'PaperPosition',[0,0,10,6]);
print(fig2,'-dpng','-color','-FArial:14','generator-histogram');