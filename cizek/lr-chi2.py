import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chi2 #chi2 rozdeleni

# nacteni dat
data=np.loadtxt('data-2a.dat')
x=data[:,0]
y=data[:,1]
ey=data[:,2]
Ndata=np.size(x)

#modelova funkce pro fit primkou prochazejici pocatkem
def primka(x,a):
    return a*x

#chi2 test kvality fitu
def chi2_test(y_exp,y_fit,sigma,N):
    sum=0.0
    for i in range(N):
        sum=sum+((y_exp[i]-y_fit[i])/sigma[i])**2
    return sum    
    
#fit primkou prochazejici pocatkem 
#(to musime udelat funkci curve_fit s modelovou funkci primka, kterou jsme si definovali,
#protoze mame fixovano b = 0 )
a,V=curve_fit(primka,x,y,sigma=ey) #fit funkci y=ax
print('---------------------------------------------------------')
print('model: y = a x')
print('a = {0:6.2f} +/- {1:6.2f}'.format(a[0],np.sqrt(V[0,0])))
yfit0=a[0]*x
chisq=chi2_test(y,yfit0,ey,Ndata) #chi2 test
deg_freedom=Ndata-1 #pocet stupnu volnosti 1
#vypocet P hodnoty pomoci distribucni fce chi2 rozdelenei
P=1-chi2.cdf(chisq,deg_freedom)
print('pocet dat =       {0:3d}'.format(Ndata))
print('pocet parametru =   1')
print('stupnu volnosti = {0:3d}'.format(deg_freedom))
print('chi square = {0:8.2f}'.format(chisq))
print('chi square na stupen volnosti = {0:8.2f}'.format(chisq/deg_freedom))
print('P hodnota = {0:10.4f}'.format(P))
print('---------------------------------------------------------')

#fit obecnou primkou (k tomu muzeme pouzit polyfit)
model,V=np.polyfit(x,y,1,w=1/ey,cov='True')
print('model: y = a x + b')
print('a = {0:6.2f} +/- {1:6.2f}'.format(model[0],np.sqrt(V[0,0])))
print('b = {0:6.2f} +/- {1:6.2f}'.format(model[1],np.sqrt(V[1,1])))
yfit1=np.polyval(model,x) #fit funkci y=ax+b
chisq=chi2_test(y,yfit1,ey,Ndata) #chi2 test
deg_freedom=Ndata-2 #pocet stupnu volnosti 1
#vypocet P hodnoty pomoci distribucni fce chi2 rozdelenei
P=1-chi2.cdf(chisq,deg_freedom)
print('pocet dat =       {0:3d}'.format(Ndata))
print('pocet parametru =   2')
print('stupnu volnosti = {0:3d}'.format(deg_freedom))
print('chi square = {0:8.2f}'.format(chisq))
print('chi square na stupen volnosti = {0:8.2f}'.format(chisq/deg_freedom))
print('P hodnota = {0:10.4f}'.format(P))
print('---------------------------------------------------------')


fig,ax=plt.subplots()
ax.errorbar(x,y,ey,marker='o',lw=0,elinewidth=2,capsize=5)
ax.plot(x,yfit0,c='green',ls='dashed',lw=2,label='y=ax')
ax.plot(x,yfit1,c='red',label=('y=ax+b'))
plt.legend(fontsize=14)
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)
