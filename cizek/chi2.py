import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import matplotlib
matplotlib.rcParams['text.usetex']=True #muzeme pak psat v LATeXu
theta=([0.3,-5,1.5]) #parametry paraboly
ndf=100-3 #pocet stupnu volnosti 
x=np.linspace(0,20,100)
y=np.polyval(theta,x) #nasimulovane hodnoty y
ey=np.abs(np.random.normal(5,1,100)) #nasimulovane chyby y
y=y+np.random.normal(0,ey,100) #rozsumeni y
model=np.polyfit(x,y,2,w=ey) #fit parabolou
residuals=(y-np.polyval(model,x))/ey
fig,ax=plt.subplots(2,1)
ax[0].scatter(x,residuals)
ax[0].set_ylim(-4,4)
ax[0].plot([0,20],[0,0],c="black")
ax[0].set_ylabel(r"rezidua ($\sigma $)",fontsize=15)
ax[1].errorbar(x,y,ey,linewidth=0,elinewidth=2,marker="p",capsize=5)
ax[1].plot(x,np.polyval(model,x),c="red",linewidth=5)
ax[1].set_xlabel("x",fontsize=15)
ax[1].set_ylabel("y",fontsize=15)
plt.show()
chi2_exp=np.sum(((y-np.polyval(model,x))/ey)**2) #vypocet chi2
P = 1-chi2.cdf(chi2_exp,ndf)
print("počet stupňů volnosti = ",ndf)
print("chi2 = ",chi2_exp)
print("chi2 na stupeň volnosti = ",chi2_exp/ndf)
print("P =  ",P)


