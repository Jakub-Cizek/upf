import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['text.usetex']=True #muzeme pak psat v LATeXu
Q=0.4  #aktivacni energie difuze
k=8.617e-5 #Boltzmanova konstanta (eV/K)
nu=100 #frekvence preskoku
T=np.linspace(400,1000,10) #teploty pro simulaci (K)
y=nu*np.exp(-Q/(k*T)) #teoreticka hodnota difuzniho koeficientu
ey=np.array([0.5,0.5,1.0,1.0,2.0,2.0,3.0,3.0,5.0,5.0]) #chyby
ey=ey*2.0e-2

#simulace
for i in range(10): 
    y[i]=y[i]+1.5*ey[i]*np.random.normal()
    if y[i]<=0: y[i]=-y[i]

#vykresleni dat
fig,ax1=plt.subplots()
ax1.errorbar(T,y,ey,marker='o',lw = 0,elinewidth=2,capsize=5)
ax1.set_xlabel("T(K)",fontsize=15)
ax1.set_ylabel(r"D ($10^{-9} {\rm cm}^2/{\rm s}$)",fontsize=15)

#linearizace
T_inv=1.0/T
ln_y=np.log(y)
eln_y=1.0/y*ey
fig,ax2=plt.subplots()
ax2.errorbar(T_inv,ln_y,eln_y,marker='o',linewidth = 0,elinewidth=2,capsize=5)
ax2.set_xlabel(r"1/T (${\rm K}^{-1}$)",fontsize=15)
ax2.set_ylabel(r"ln D ($10^{-9} {\rm cm}^2/{\rm s}$)",fontsize=15)

#fit primkou
model=np.polyfit(T_inv, ln_y, 1, w=1.0/eln_y)
predict=np.poly1d(model) #modelova funkce
print(predict)
y_predict=predict[1]*T_inv+predict[0]
ax2.plot(T_inv,y_predict,c="red") #vykresleni primky
Q_fit=-predict[1]*k
nu_fit=np.exp(predict[0])
y_fit=nu_fit*np.exp(-Q_fit/(k*T))
print("Q= {} eV".format(Q_fit))
print("nu = {} 1e-9 cm2/s".format(nu_fit))
ax1.plot(T,y_fit,c="red") #vykresleni expoennty
plt.show()
