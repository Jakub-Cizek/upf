import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy.optimize import curve_fit
import matplotlib
matplotlib.rcParams['text.usetex']=True #muzeme pak psat v LATeXu
data=np.loadtxt("HV.txt")
T=data[:,0]
HV=data[:,1]
eHV=data[:,2]
Tmin=np.min(T)
Tmax=np.max(T)
mean_HV=np.sum(HV/eHV**2)/np.sum(1/eHV**2) #vazeny prumer
residua=(HV-mean_HV)/eHV
fig,ax=plt.subplots(2,1)
ax[0].scatter(T,residua)
ax[0].plot([Tmin,Tmax],[0,0],c="black")
ax[0].set_ylabel("rezidua",fontsize=15)
ax[1].errorbar(T,HV,eHV,linewidth=0,elinewidth=2,marker="o",capsize=5)
ax[1].set_xlabel(r"teplota (${}^o$C)",fontsize=15)
ax[1].set_ylabel("tvrdost (MPa)",fontsize=15)
ax[1].plot([Tmin,Tmax],[mean_HV,mean_HV],c="red")
#plt.show()
chi2_konst=np.sum(((HV-mean_HV)/eHV)**2)
N=np.size(T)
print("počet dat = ",N)
ndf=N-1
print("konstatní závislost")
print("chi2 = ",chi2_konst)
print("počet stupňů volnosti = ",ndf)
print("P = ",1-chi2.cdf(chi2_konst,ndf))
print("chi2 na stupeň volnosti = ",chi2_konst/ndf)
plt.show()

def peak(x,x0,w,I,bcg):
    return I*np.exp(-((x-x0)/w)**2)+bcg

p0=([150,50,10,510])
params,pcov=curve_fit(peak,data[:,0],data[:,1],p0,sigma=data[:,2])
HVfit=peak(T,params[0],params[1],params[2],params[3])
residua=(HV-HVfit)/eHV
#ax.plot(data[:,0],peak(data[:,0],params[0],params[1],params[2],params[3]),c="blue")
T_plot=np.linspace(np.min(data[:,0]),np.max(data[:,0]),1000)
HV_plot=peak(T_plot,params[0],params[1],params[2],params[3])

fig,ax=plt.subplots(2,1)
ax[0].scatter(T,residua)
ax[0].plot([Tmin,Tmax],[0,0],c="black")
ax[0].set_ylabel("rezidua",fontsize=15)
ax[1].errorbar(T,HV,eHV,linewidth=0,elinewidth=2,marker="o",capsize=5)
ax[1].set_xlabel(r"teplota (${}^o$C)",fontsize=15)
ax[1].set_ylabel("tvrdost (MPa)",fontsize=15)
ax[1].plot(T_plot,HV_plot,c="red")



print("")
print("peak (Gaussián)")
print("T0 = ",params[0],"+/-",np.sqrt(pcov[0,0]))
print("w  = ",params[1],"+/-",np.sqrt(pcov[1,1]))
print("I  = ",params[2],"+/-",np.sqrt(pcov[2,2]))
print("bcg= ",params[3],"+/-",np.sqrt(pcov[3,3]))
chi2_peak=np.sum(((data[:,1]-peak(data[:,0],params[0],params[1],params[2],params[3]))/data[:,2])**2)
ndf=N-4
print("chi2 = ",chi2_peak)
print("počet stupňů volnosti = ",ndf)
print("P = ",1-chi2.cdf(chi2_peak,ndf))
print("chi2 na stupeň volnosti = ",chi2_peak/ndf)
plt.show()

