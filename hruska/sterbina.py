import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib
matplotlib.rcParams['text.usetex']=True #muzeme pak psat v LATeXu
#modelova funkce
def func(x,d,x0):
    lmbd=550   #pouzita vlnova delka (nm)
    return (np.sinc(d*np.pi/lmbd*np.sin(x-x0)))**2
    
#simulace
d=2500
x0=2*np.pi/180.0
x=np.linspace(-15,15,100)
x=x*np.pi/180.0
np.random.seed(124)
ys=func(x,d,x0)+0.005*np.random.normal(0,1,x.shape[0])

fig,ax=plt.subplots()
ax.scatter(x*180./np.pi,ys)

#odhad pocatecnich hodnot
d0=2000
x00=0.0
#fit metodou nejmensich ctvrecu
par,pcov=curve_fit(func,x,ys,p0=[d0,x00],bounds=([0,-0.5],[5000,0.5]))
#vypis vysledku
print("d = (",par[0],"+/-",np.sqrt(pcov[0,0]),") nm")
print("alfa0 = (",par[1]*180./np.pi,"+/-",np.sqrt(pcov[1,1])*180/np.pi,") stupnu")
#vykresleni modelove funkce
ax.set_xlabel(r"$\alpha {}^{\circ}$",fontsize=15)
ax.set_ylabel("intenzita",fontsize=15)
ax.plot(x*180./np.pi,func(x,*par),c="red")
plt.show()
    