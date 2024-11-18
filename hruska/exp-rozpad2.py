import numpy as np
import matplotlib.pyplot as plt

N=10000
nbins=100
tau=200
#simulace exponencialniho rozdeleni
r=np.random.random_sample(N)    #nahodne cisla s rovnomernym rozdelenim U(0,1)
t=-tau*np.log(r)                #nahodne cisla s exponencialnim rozdelenim
hist,bin_edges=np.histogram(t,bins=nbins)   #vytvoreni histogramu casu
tbins=bin_edges[0:nbins]                    #pole casu pro histogram
delta=(np.max(t)-np.min(t))/nbins           #sirka binu
S=N*delta                                   #plocha histogram
kumul=np.cumsum(hist)                       #vytvoreni kumulativniho histogramu casu
norm=np.cumsum(hist/N)                      #vytvoreni normovaneho kumulativniho histogramu casu
print('sirka binu:',delta)
print('plocha histogramu:',S)

#teoreticke zavislosti
x=np.linspace(0,10*tau,100)     #pole casu od 0 do 10 tau
y=1/tau*np.exp(-x/tau)          #teoreticka hustota pravdepodobnosti
z=1-np.exp(-x/tau)              #teoreticka distribucni funkce

#histogram
fig,ax=plt.subplots()           #vytvoreni obrazku
ax.bar(tbins,hist,width=delta,label='histogram')    #vykresleni sloupcoveho grafu
ax.plot(x,S*y,c='red',label='teoretická závislost') #vykresleni teoreticke zavislosti
plt.xlim(-tau/2,6*tau)          #nastaveni rozmezi osy t: -tau/2,6 tau
plt.ylim(0,1.1*S/tau)           #nastaveni rozmezi osy y: 0,1.1*max-y
ax.set_xlabel('t ($\mu$s)',fontsize=14)
ax.set_ylabel('n',fontsize=14)
plt.legend()

#hustota pravdepodobnosti
fig,ax=plt.subplots()           #vytvoreni obrazku
ax.step(tbins,hist/S)           #vykresleni schodoveho hrafu
ax.plot(x,y,c='red')            #vykresleni teoreticke zavislosti
plt.xlim(-tau/2,6*tau)          #nastaveni rozmezi osy t: -tau/2,6 tau
ax.set_xlabel('t ($\mu$s)',fontsize=14)
ax.set_ylabel('f(t)',fontsize=14)
plt.title('hustota pravděpodobnosti',fontsize=14)

#kumulativni histogram
fig,ax=plt.subplots()           #vytvoreni obrazku
ax.bar(tbins,kumul,width=delta,label='kumulativní histogram')  #vykresleni sloupcoveho grafu
ax.plot(x,N*z,c='red',label='teoretická závislost')            #vykresleni teoreticke zavislosti
plt.xlim(-tau/2,6*tau)          #nastaveni rozmezi osy t: -tau/2,6 tau
ax.set_xlabel('t ($\mu$s)',fontsize=14)
ax.set_ylabel('K',fontsize=14)
plt.legend()

#distribucni funkce
fig,ax=plt.subplots()           #vytvoreni obrazku
ax.step(tbins,norm) #vykresleni sloupcoveho grafu
ax.plot(x,z,c='red')            #vykresleni teoreticke zavislosti
plt.xlim(-tau/2,6*tau)          #nastaveni rozmezi osy t: -tau/2,6 tau
ax.set_xlabel('t ($\mu$s)',fontsize=14)
ax.set_ylabel('F(t)',fontsize=14)
plt.title('distribuční funkce',fontsize=14)




