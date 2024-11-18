import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chi2 #chi2 rozdeleni

# prima umernost
def model1(x,a):
    return a*x

# odmocninova zavislost
def model2(x,a):
    return a*x**0.5

#chi2 test kvality fitu
def chi2_test(y_exp,y_fit,sigma,N):
    sum=0.0
    for i in range(N):
        sum=sum+((y_exp[i]-y_fit[i])/sigma[i])**2
    return sum

data=np.loadtxt("zavislost.dat")
x=data[:,0]
y=data[:,1]
ey=data[:,2]
N_data=np.size(x)
deg_freedom=N_data-1



par1,V1=curve_fit(model1,x,y,sigma=ey,absolute_sigma=True)
chisq=chi2_test(y,model1(x,par1),ey,N_data)
#vypocet P hodnoty pomoci distribucni fce chi2 rozdelenei
P=1-chi2.cdf(chisq,deg_freedom)
print(P)
print('---------------------------------------------------------')
print("model 1: y = a*x")
print("a = {0:6.4f} +/- {1:6.4f}".format(par1[0],np.sqrt(V1[0,0])))
print('pocet dat =       {0:3d}'.format(N_data))
print('pocet parametru =   1')
print('stupnu volnosti = {0:3d}'.format(N_data))
print('chi square = {0:8.2f}'.format(chisq))
print('chi square na stupen volnosti = {0:8.2f}'.format(chisq/deg_freedom))
print('P hodnota = {0:10.4f}'.format(P))
print('---------------------------------------------------------')

par2,V2=curve_fit(model2,x,y,sigma=ey,absolute_sigma=True)
chisq=chi2_test(y,model2(x,par2),ey,N_data)
#vypocet P hodnoty pomoci distribucni fce chi2 rozdelenei
P=1-chi2.cdf(chisq,deg_freedom)
print('---------------------------------------------------------')
print("model 2: y = a*sqrt(x)")
print("a = {0:5.3f} +/- {1:5.3f}".format(par2[0],np.sqrt(V2[0,0])))
print('pocet dat =       {0:3d}'.format(N_data))
print('pocet parametru =   1')
print('stupnu volnosti = {0:3d}'.format(N_data))
print('chi square = {0:8.2f}'.format(chisq))
print('chi square na stupen volnosti = {0:8.2f}'.format(chisq/deg_freedom))
print('P hodnota = {0:10.4f}'.format(P))
print('---------------------------------------------------------')


fig,ax=plt.subplots()
plt.errorbar(x,y,ey,marker='o',lw=0,elinewidth=2,capsize=5)
ax.set_xlabel('x',fontsize=12)
ax.set_ylabel('y',fontsize=12)
plt.plot(x,model1(x,par1),label='y=a*x')
plt.plot(x,model2(x,par2),label='y=b*sqrt(x)')
plt.legend()


