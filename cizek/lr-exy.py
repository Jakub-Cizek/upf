import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

x=np.array([0.1,2.1,3.3,4.9,5.6,6.5,7.7,8,10.5,13]) #data x
ex=np.array([0.9,0.3,0.1,0.1,0.5,0.5,0.1,0.2,0.9,2]) #chyby x
y=np.array([19,23,25,31,35,43,46,44,52,56]) #data y
ey=np.array([2,2,2,2,1,5,3,4,2,1]) #chyby y

Ndata=np.size(x)
print('pocet dat: ',Ndata)

#modelova funkce
def primka(x,a,b):
    return a*x+b

#chi kvadrat, tj. funkce, jejiz kvadrat budeme minimalizovat  
def chisq(theta,x,y,ex,ey):
    return (y-theta[1]-theta[0]*x)/np.sqrt(ey**2+(ex*theta[0])**2)
    
theta0=np.array([3,15]) #pocatecni odhady parametru a,b
#minimalizace funkce chisq
res=leastsq(chisq,theta0,args=(x,y,ex,ey),full_output=1)
a=res[0][0] #odhad parametru a
b=res[0][1] #odhad parametru b
#pole res[1] je kovariancni matice odhadu parametru
ea=np.sqrt(res[1][0][0]) #chyba odhadu a 
eb=np.sqrt(res[1][1][1]) #chyba odhadu v 
cov_ab=res[1][0][1] #kovariance odhau a, b
print('modelova funkce y = ax +b')
print('a = {0:3.1f} +/- {1:3.1f}'.format(a,ea))
print('b = {0:3.0f} +/- {1:3.0f}'.format(b,eb))
print('cov(a,b) = {0:3.1f}'.format(cov_ab))
y_fit=a*x+b

#extrapolace
x0=-b/a
ex0=np.sqrt((b/a**2)**2*ea**2+(1/a)**2*eb**2+2*(b/a**2)*(1/a)*cov_ab)
print('prusecik s osou x')
print('x0 = {0:3.1f} +/- {1:3.1f}'.format(x0,ex0))


#print(res)
fig,ax=plt.subplots()
ax.errorbar(x,y,ey,ex,lw=0,elinewidth=2,capsize=5,marker='o')
ax.plot(x,y_fit,c='red',lw=3)
ax.errorbar(x0,0,0,ex0,lw=0,elinewidth=2,capsize=5,marker='*',c='green')
ax.plot([x0,x[0]],[0,y_fit[0]],c='green',ls='dashed',lw=2)
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)


