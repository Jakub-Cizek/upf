import numpy as np
import matplotlib.pyplot as plt
N=1000
#SIMULACE vysledku mereni
x0_real=5   #skutecna x-ova poloha majaku
l_real=10   #skutecna y-ova poloha majaku
x=np.empty(N)
x=l_real*np.tan(np.random.random_sample(N)*np.pi-np.pi/2.0)+x0_real  #generator nahodnych hodnot x 
                                                                     #pomoci rovnomerneho rozdeleni uhlu
fig,ax=plt.subplots()
x_range=l_real*np.tan(np.pi*80/180)     #rozsah hodnot x pro uhly od -80 do +80 stupnu
ax.hist(x,bins=20,range=(x0_real-x_range,x0_real+x_range),density=True)     #histogram hodnot x
xp=np.linspace(x0_real-x_range,x0_real+x_range,100)     #x-ove hodnoty pro modelovy lorentzian
yp=1/np.pi*l_real/(l_real**2+(xp-x0_real)**2)           #y-ove hodnoty pro modelovy lorentzian
ax.plot(xp,yp,c="red")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.savefig("majak-histogram.png",dpi=600)

#HLEDANI polohy majaku
x0=np.linspace(-15,15,100)  #pole hledanych hodnot x0
N_x0=np.size(x0)
l=np.linspace(0.1,20,100)   #pole hledanych hodnot l
N_l=np.size(l)

l_mesh,x0_mesh=np.meshgrid(l,x0)    #generace dvourozmerne mrizky l_mesh krat x0_mesh 
ln_L=np.zeros([N_x0,N_l])
for i in range(N):                  #funkce logaritmus verohodnostni funkce spocitana pro simulovane hodnoty x
    ln_L=ln_L+np.log(l_mesh)-np.log(np.pi*(l_mesh**2+(x[i]-x0_mesh)**2))
ln_L_max=np.max(ln_L)       #maximum logaritmu verohodnostni funkce
i_max,j_max=np.where(ln_L==ln_L_max)    #hledani maxima logaritmu vedohodnostni funkce 
fig,ax=plt.subplots()
ax.contour(x0_mesh,l_mesh,ln_L,levels=200)  #konturovy 2D graf pro funkce ln L s 200 vrstevnicemi
ax.scatter(x0_real,l_real)      #skutecna poloha majaku
ax.scatter(x0[i_max],l[j_max],c="red",marker="+",s=100)     #nalezena poloha majaku
ax.set_xlabel("x0")
ax.set_ylabel("l")
plt.savefig("majak-verohodnost.png",dpi=600)
plt.show()
print('x0= %.8f' % x0[i_max])
print('l= %.8f' % l[j_max])