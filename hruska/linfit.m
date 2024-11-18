%linearni regrese y = ax+b
fprintf(1,'\n');
fprintf(1,'Linearni fit\n');
fprintf(1,'10.1. 2020\n');
%myVars={'x','y','vp'};
%1. sloupec x
%2. sloupec y
%3. slopuec err-y (st dev.)
%load('datal.dat',myVars{:}) %nacteni datoveho souboru
%load('lr-data.txt',myVars{:}); %nacteni datoveho souboru
load('lr-data.txt','-ascii');
x=lr_data(:,1);
y=lr_data(:,2);
ey=lr_data(:,3);
np=size(x);
n=np(1);     %pocet dat
fprintf(1,'pocet dat:%d\n',n);
%vytvoreni kovariancni matice V
e=eye(n); %jednotkova matice n x n
v=zeros(n); %matice samych nul n x n e
for i=1:n, v(i,i)=ey(i)^2;end; %do diagonaly napiseme kvadraty chyb
%obecna primka y=theta1*x+theta2
%vytvoreni matice A
a0=ones(n,1); %sloupcovy vektor jednicek 
a=[a0,x];%,matice A soustavy
b=inv(a'*inv(v)*a)*a'*inv(v); %matice (A^T V^-1 A)^-1 A^T V^-1
theta=b*y; %vektor odhadu parametru
u=b*v*b'; %kovariancni matice parametru
e_b=sqrt(u(1,1)); %chyba parametru b
e_a=sqrt(u(2,2)); %chyba parametru a
cor=u(1,2)/(e_a*e_b); %korelace a,b
%vystup
fprintf(1,'\n');
fprintf(1,'obecna primka y=a*x+b\n');
fprintf(1,'b=%f +/- %f\n',theta(1),e_b);
fprintf(1,'a=%f +/- %f\n',theta(2),e_a);
fprintf(1,'korelace(a,b)=%f\n',cor);
%grafika
xmin=min(x);
xmax=max(x);
dx=(xmax-xmin)/1000;
xx=[xmin:dx:xmax]; %x-ova souradnice pro vykresleni mocdelove funkce
yx=theta(1)+theta(2).*xx; %modelova funkce
subplot(2,1,1); %vytvoreni obrazku
errorbar(x,y,ey,'bo');hold on; %vykresleni experimentalnich bodu
xlabel('x');
ylabel('y');
plot(xx,yx,'r');title('y=ax+b'); %vykresleni nafitovane primky
hold off;
%primka prochazejici pocatkem y=m*x
fprintf(1,'\n');
fprintf(1,'primka prochazejici pocatkem y=m*x\n');
s1=x'*(y./(ey.*ey));
s2=x'*(x./(ey.*ey));
m=s1/s2;
%vypocet chyby 
e_m=sqrt(1/s2);
fprintf(1,'m=%f +/- %f\n',m,e_m);
%grafika
yx=m.*xx;
subplot(2,1,2);
errorbar(x,y,ey,'bo');hold on;
plot(xx,yx,'g');title('y=mx');
xlabel('x');
ylabel('y');
hold off;







