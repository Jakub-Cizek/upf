import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chi2 

data=np.loadtxt("peakgl.txt") #nacteni dat
x=data[:,0] #nezavisla promenna x
y=data[:,1] #zavisla promenna y
N=np.size(x) #pocet dat
ey=np.sqrt(y) #chyba y je dana Poissonovym rozdelenim
 
 #definice Lonrentzianu
def lorentz(x,x0,w,A,bcg):
    return A/np.pi*(w/2)/((w/2)**2+(x-x0)**2)+bcg

p0=([5,1.0,500,3])  #pocatecni odhad parametru
pars,pcov=curve_fit(lorentz,x,y,p0,sigma=ey) #fit Lorentzianu nelinearni metoda nejmensich ctvercu 
yfit_lorentz=lorentz(x,pars[0],pars[1],pars[2],pars[3]) #modelova funkce
residua=(y-yfit_lorentz)/ey #rezidua
fig,ax=plt.subplots(2,1) #vykresleni grafu
ax[0].scatter(x,residua)
ax[0].plot([0,10],[0,0],c="black")
ax[1].scatter(x,y)
ax[1].plot(x,yfit_lorentz,c="red")
ax[1].set_xlabel("x",fontsize=12)
ax[1].set_ylabel("y",fontsize=12)
ax[0].set_ylabel("rezidua",fontsize=12)
chi2_exp=np.sum((y-yfit_lorentz)**2/ey**2) #vypocet chi2
ndf=N-4
plt.show()
print("LORENTZIAN:") #vypis parametru
print("x0  = ",pars[0],"+/-", np.sqrt(pcov[0,0]))
print("w   = ",pars[1],"+/-", np.sqrt(pcov[1,1]))
print("A   = ",pars[2],"+/-", np.sqrt(pcov[2,2]))
print("bcg = ",pars[3],"+/-", np.sqrt(pcov[3,3]))
print("chi2= ",chi2_exp)
print("počet stupňů volnosti:",ndf)
print("P = ",1-chi2.cdf(chi2_exp,ndf)) #P - hodnota

#definice Gaussianu
def gaussian(x,x0,w,A,bcg):
    sigma=w/(2*np.sqrt(2*np.log(2)))
    return A/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-x0)**2/(2*sigma**2))+bcg

p0=([5,1.0,500,3]) #pocatecni odhad parametru
pars,pcov=curve_fit(gaussian,x,y,p0,sigma=ey) #fit Gaussianu nelinearni metoda nejmensich ctvercu 
yfit_gauss=gaussian(x,pars[0],pars[1],pars[2],pars[3]) #modelova funkce
residua=(y-yfit_gauss)/ey #rezidua
fig,ax=plt.subplots(2,1) #vykreseleni grafu
ax[0].scatter(x,residua)
ax[0].plot([0,10],[0,0],c="black")
ax[1].scatter(x,y)
ax[1].plot(x,yfit_gauss,c="red")
ax[1].set_xlabel("x",fontsize=12)
ax[1].set_ylabel("y",fontsize=12)
ax[0].set_ylabel("rezidua",fontsize=12)
chi2_exp=np.sum((y-yfit_gauss)**2/ey**2) #vypocet chi2
ndf=N-4
plt.show()
print("GAUSSIAN:") #vypis parametru
print("x0  = ",pars[0],"+/-", np.sqrt(pcov[0,0]))
print("w   = ",pars[1],"+/-", np.sqrt(pcov[1,1]))
print("A   = ",pars[2],"+/-", np.sqrt(pcov[2,2]))
print("bcg = ",pars[3],"+/-", np.sqrt(pcov[3,3]))
print("chi2= ",chi2_exp)
print("počet stupňů volnosti:",ndf)
print("P = ",1-chi2.cdf(chi2_exp,ndf)) #P - hodnota



