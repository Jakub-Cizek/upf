import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex']=True #muzeme pak psat v LATeXu
import matplotlib.pyplot as plt
T=300 #teplota [K]
m=28*1e-3 #molarni hmotnost N2 [g/mol]
R=8.314462 #univerzalni plynova konstanta [J/K]
mu=0 #ocekavana hodnota
sigma=np.sqrt(R*T/m) #standardni odchylka Gaussianu
print("sigma=",sigma)
n=10000 #pocet hodnot na simulaci
nbin=100 #pocet binu
vx=np.array(n) #x-ova slozka rychlosti
vy=np.array(n) #x-ova slozka rychlosti
vz=np.array(n) #x-ova slozka rychlosti
vx=sigma*np.random.randn(n)
vy=sigma*np.random.randn(n)
vz=sigma*np.random.randn(n)
v=np.sqrt(vx**2+vy**2+vz**2)
xg=np.linspace(-4*sigma,4*sigma,1000)  #x-osa pro gaussian
yg=1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(xg**2)/(2*sigma**2)) #gaussian
xmb=np.linspace(0,4*sigma,1000) #x-osa pro Maxwell-Boltznamovo rozdeleni
ymb=np.sqrt(2/np.pi)*1/sigma**3*xmb**2*np.exp(-xmb**2/(2*sigma**2)) #Maxwell-Boltznamovo rozdeleni
#ted se nakresli 3 obrazky s histogramy rozdeleni slozek rychlosti 
fig,ax=plt.subplots(3) #vytvoreni 3 obrazku pod sebou
ax[0].set_title(r"$v_x$",fontsize=20) #nadpis grafu
ax[0].set_xlabel(r"$v_x$ (m/s)") #popis osy x
ax[0].set_ylabel("pdf")
ax[1].set_title(r"$v_y$",fontsize=16)
ax[1].set_xlabel(r"$v_y$ (m/s)")
ax[1].set_ylabel("pdf")
ax[2].set_title(r"$v_z$",fontsize=16)
ax[2].set_xlabel(r"$v_z$ (m/s)")
ax[2].set_ylabel("pdf")
ax[0].hist(vx,bins=nbin,color="red", density=True) #nastaveni barvy histogramu
ax[1].hist(vy,bins=nbin,color="green", density=True)
ax[2].hist(vy,bins=nbin,color="blue", density=True)
ax[0].plot(xg,yg,color="green") #nastaveni barvy krivky
ax[1].plot(xg,yg,color="red")
ax[2].plot(xg,yg,color="magenta")           
fig.set_figheight(10) #nastraveni vysky obrazku
fig.tight_layout() #aby se neprakryvaly popisky os
plt.show() #vykresleni obrazku 
#ted se vykresli histogram roydeleni velikosti rychlosti
fig,ax=plt.subplots()
ax.set_title("velikost rychlosti",fontsize=16)
ax.set_xlabel("v (m/s)")
ax.set_ylabel("pdf")
ax.hist(v,bins=nbin,color="magenta", density=True)
ax.plot(xmb,ymb,color="blue")
plt.show()