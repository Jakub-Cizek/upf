import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
data=np.loadtxt("lr-data-exy.txt")
#data[:,0]  x
#data[:,1]  err-x
#data[:,2]  y
#data[:,3]  err-y
fig,ax=plt.subplots()
ax.errorbar(data[:,0],data[:,2],xerr=data[:,1],yerr=data[:,3],marker="o",linewidth=0,elinewidth=2,capsize=5)
ax.set_xlabel("x")
ax.set_ylabel("y")
#modelova funkce
def primka(theta,x):
    return theta[0]+theta[1]*x
#funkce, kterou budeme minimalizovat
def func(theta,x,y,ex,ey):
    return (y-theta[0]-theta[1]*x)/(np.sqrt(ey**2+ex**2*theta[1]**2))

theta0=np.array([0,1])
res=least_squares(func,theta0,args=(data[:,0],data[:,2],data[:,1],data[:,3]))
print(res.x)
ax.plot(data[:,0],primka(res.x,data[:,0]),c="red")
