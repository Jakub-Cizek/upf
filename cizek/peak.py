import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chi2
data=np.loadtxt("peak.txt") 
x=data[:,0]
y=data[:,1]
ey=np.sqrt(y)
fig,ax=plt.subplots()
ax.errorbar(x,y,ey,linewidth=0,elinewidth=2,capsize=5,marker="p")

def peak(x,x0,sigma,I,bcg):
    return I/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-x0)**2/(2*sigma**2))+bcg

p0=([7.4,0.2,800,50])
params,pcov=curve_fit(peak,x,y,p0,sigma=ey)
yfit=peak(x,params[0],params[1],params[2],params[3])
ax.plot(x,yfit,c="red",lw=3)
ax.set_xlabel("x")
ax.set_ylabel("y")

print("x0 = ",params[0],"+/-",np.sqrt(pcov[0,0]))
print("sigma = ",params[1],"+/-",np.sqrt(pcov[1,1]))
print("I = ",params[2],"+/-",np.sqrt(pcov[2,2]))
print("bcg = ",params[3],"+/-",np.sqrt(pcov[3,3]))

chi2_exp=np.sum(((y-yfit)/ey)**2)
N=np.size(x)
ndf=N-4
print("počet dat :",N)
print("počet stupňů volnosti :",ndf)
print("chi2 = ",chi2_exp)
print("chi2 na stupeň volnosti :",chi2_exp/ndf)
print("P = ",1-chi2.cdf(chi2_exp,ndf))
