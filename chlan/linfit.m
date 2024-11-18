%linearni regrese
fprintf(1,'\n');
fprintf(1,'Linearni fit\n');
load datafit.dat    %nacteni datoveho souboru
x=data(:,1);   %1. sloupec x
y=data(:,2);   %2. sloupec y
vp=data(:,3);   %3. slopuec err-y (st dev.)
np=size(x);
n=np(1);     %pocet dat
fprintf(1,'pocet dat:%d\n',n);

%vytvoreni kovariancni matice V
e=eye(n);
v=zeros(n);
for i=1:n, v(i,i)=vp(i)^2;end

%obecna primka y=beta1*x+beta0    y=a*x+b
%% vytvoreni matice A
a0=ones(n,1);
a=[a0,x];
b=inv(a'*inv(v)*a)*a'*inv(v);
beta=b*y;
u=b*v*b'; %kovariancni matice parametru

%%
e_b=sqrt(u(1,1));
e_a=sqrt(u(2,2));
cor=u(1,2)/(e_a*e_b); %korelace
%vystup
fprintf(1,'\n');
fprintf(1,'obecna primka y=a*x+b\n');
fprintf(1,'b=%f +/- %f\n',beta(1),e_b);
fprintf(1,'a=%f +/- %f\n',beta(2),e_a);
fprintf(1,'korelace(a,b)=%f\n',cor);

%% nakresleni grafu
xmin=min(x);
xmax=max(x);
dx=(xmax-xmin)/1000;
xx=[xmin:dx:xmax];   % pole x-ovych hodnot pro fitovanou zavislost
yx=beta(1)+beta(2).*xx;  % y-ove hodnoty zavislosti
subplot(2,1,1);
errorbar(x,y,vp,'bo');hold on;
plot(xx,yx,'r');title('y=ax+b');
hold off;

%primka prochazejici pocatkem y=m*x
fprintf(1,'\n');
fprintf(1,'primka prochazejici pocatkem y=m*x\n');
s1=x'*(y./(vp.*vp));
s2=x'*(x./(vp.*vp));
m=s1/s2;
%vypocet chyby 
e_m=sqrt(1/s2);
fprintf(1,'m=%f +/- %f\n',m,e_m);

%% nakresleni grafu
yx=m.*xx;
subplot(2,1,2);
errorbar(x,y,vp,'bo');hold on;
plot(xx,yx,'g');title('y=mx');
hold off;







