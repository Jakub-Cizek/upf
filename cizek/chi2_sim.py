import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import matplotlib
matplotlib.rcParams['text.usetex']=True #muzeme pak psat v LATeXu
theta=([0.3,-5,1.5]) #parametry paraboly
ndf=100-3 #pocet stupnu volnosti 
Nsim=1000
x=np.linspace(0,20,100)
residuals=np.empty(100)
H,bin_edges=np.histogram(residuals,bins=100,range=[-5,5])
chi2_exp=np.empty(Nsim)

fig,ax=plt.subplots(2,1)
ax[0].set_ylim(-5,5)
ax[0].plot([0,20],[0,0],c="black")
ax[0].set_ylabel(r"rezidua ($\sigma $)",fontsize=15)
ax[1].set_xlabel("x",fontsize=15)
ax[1].set_ylabel("y",fontsize=15)

for i in range(Nsim):
    y=np.polyval(theta,x)
    ey=np.abs(np.random.normal(5,1,100)) #nasimulovane chyby y
    y=y+np.random.normal(0,ey,100) #rozsumeni y
    model=np.polyfit(x,y,2,w=ey) #fit parabolou
    residuals=(y-np.polyval(model,x))/ey
    H+=np.histogram(residuals,bins=100,range=[-5,5])[0]
    ax[0].scatter(x,residuals,s=1)
    ax[1].scatter(x,y,marker="p",s=1)
    ax[1].plot(x,np.polyval(model,x),c="red",linewidth=1)
    chi2_exp[i]=np.sum(((y-np.polyval(model,x))/ey)**2) #vypocet chi2

H = H/(np.sum(H)*0.1)
fig,ax=plt.subplots()
ax.hist(chi2_exp,bins=20,range=(0,200),density=True)
x2=np.linspace(0,200,1000)
y2=chi2.pdf(x2,ndf)
ax.plot(x2,y2,c="red",linewidth=3)
ax.set_xlabel(r"$\chi^2$")
ax.set_ylabel("hustota pravděpodobnosti")

fig,ax=plt.subplots()
ax.step(bin_edges[1:],H)
xg=np.linspace(-5,5,1000)
yg=1/np.sqrt(2*np.pi)*np.exp(-xg**2/2)
ax.plot(xg,yg,c="red")
ax.set_ylim(0,)
ax.set_xlabel("rezidua")
ax.set_ylabel("hustota pravděpodobnosti")

