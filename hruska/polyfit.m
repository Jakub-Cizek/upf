%poly regrese
%fit polynomu + chi2 test
fprintf(1,'\n');
fprintf(1,'Poly fit\n');
fprintf(1,'05.01. 2019\n');
load polydata.dat %nacteni datoveho souboru
%1. sloupec x
%2. sloupec y
%3. slopuec err-y (st dev.)
x=polydata(:,1);
y=polydata(:,2);
ey=polydata(:,3);
np=size(x);
n=np(1);     %pocet dat
fprintf(1,'pocet dat:%d\n',n);
%stupen fitovaneho polynomu m
m=input('Stupen polynomu: ');
%vytvoreni kovariancni matice V
e=eye(n);
V=zeros(n);
for i=1:n, V(i,i)=ey(i)^2;end; 
%fit polynomu stupne m
%vytvoreni matice A
for i=1:n
   for j=1:m+1
      A(i,j)=x(i)^(j-1);
   end
end
B=inv(A'*inv(V)*A)*A'*inv(V);
theta=B*y;
U=B*V*B';
R=U;
%korelacni matice
for i=1:m+1
   for j=1:m+1
      R(i,j)=U(i,j)/sqrt(U(i,i)*U(j,j));
   end
end
%vystup
fprintf(1,'\n');
fprintf(1,'stupen polynomu:obecna primka %d\n',m);
for j=1:m+1
   fprintf(1,'theta%d: %f +/- %f\n',j-1,theta(j),sqrt(U(j,j)));
end
fprintf(1,'kovariancni matice:\n');
U
fprintf(1,'korelacni matice:\n');
R
%grafika
%residua a chi2
res=zeros(1,n);
ym=zeros(1,n);
chisq=0;
subplot(2,1,1);
for i=1:n
   for j=1:m+1
      ym(i)=ym(i)+theta(j)*x(i)^(j-1);
   end
   res(i)=(y(i)-ym(i))/sqrt(V(i,i));
   chisq=chisq+res(i)^2;
end
plot(x,res,'b');title('polynom fit');
xlabel('x');
ylabel('residua (1 st.dev)');
hold off;
ndeg=n-(m+1);%pocet stupnu volnosti
fprintf('pocet stupnu volnosti: %d\n',ndeg);
e_chisq=sqrt(2*ndeg);
fprintf('chisq = %f +/- %f\n',chisq,e_chisq);
fprintf('chisq/deg.freedom  = %f +/- %f\n',chisq/ndeg,e_chisq/sqrt(ndeg));
%polynom
fout=fopen('Data.out','w'); %output
xmin=min(x);
xmax=max(x);
dx=(xmax-xmin)/1000;
xx=[xmin:dx:xmax];
yx=zeros(1,1001);
for i=1:1001
   for j=1:m+1
      yx(i)=yx(i)+theta(j)*xx(i)^(j-1);
   end
    fprintf(fout,'%f %f \n',xx(i),yx(i));
end
fclose(fout);
subplot(2,1,2);
errorbar(x,y,ey,'bo');hold on;
plot(xx,yx,'r');
xlabel('x');
ylabel('y');
hold off;

clear;