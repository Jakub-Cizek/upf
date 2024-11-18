import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chi2
from matplotlib.gridspec import GridSpec

#nacteni dat
data=np.loadtxt("HVdata.txt")
t=data[:,0]
y=data[:,1]
ey=data[:,2]


fig=plt.figure(figsize=[8,8])
gs= GridSpec(2,1,height_ratios=[1,3])
ax1=fig.add_subplot(gs[0])
plt.xscale("log") #log skala na ose x
ax2=fig.add_subplot(gs[1])
ax2.errorbar(t,y,ey,linewidth=0,elinewidth=2,marker="o",capsize=5)
ax2.set_xlabel("t (s)",fontsize=15)
ax2.set_ylabel("HV (MPa)",fontsize=15)

#definice modelove funkce
def JMAK(t,HV0,dHV,t0,m):
    return HV0+dHV*(1-np.exp(-(t/t0)**m))

par0=([700,200,100000,1]) #pocatecni odhady parametru
par,pcov=curve_fit(JMAK,t,y,par0,sigma=ey) #fit metodou nejmensich ctvercu
yfit=JMAK(t,par[0],par[1],par[2],par[3]) #na vykresleni modelove funkce
ax2.plot(t,yfit,c="red")

rezidua=(y-yfit)/ey #rezidua
ax1.scatter(t,rezidua) #graf rezidui
tmin=np.min(t)
tmax=np.max(t)
ax1.plot([tmin,tmax],[0,0],c="black") #cara v nule
ax1.set_ylabel("rezidua",fontsize=15)
ax1.set_ylim(-3,3)
plt.xscale("log") #log skala na ose x

plt.show()

#vypis parametru
print("HV0 = ",par[0],"+/-",np.sqrt(pcov[0,0]))
print("dHV = ",par[1],"+/-",np.sqrt(pcov[1,1]))
print("t0  = ",par[2],"+/-",np.sqrt(pcov[2,2]))
print("m   = ",par[3],"+/-",np.sqrt(pcov[3,3]))

#chi2 test
N=np.size(t) #pocet dat
ndf=N-4 #stupnu volnosti
chi2_exp=np.sum(((y-yfit)/ey)**2)
print("")
print("chi2 test")
print("chi2 = ",chi2_exp)
print("pocet stupnu volnosti = ",ndf)
print("P = ",1-chi2.cdf(chi2_exp,ndf)) #P-hodnota
