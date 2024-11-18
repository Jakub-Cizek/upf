import numpy as np
import matplotlib.pyplot as plt

P=0.75
mu=10
sigma=2
tau=4

# simulace nahodne promenne s rozdelenim exp+gaussian 3:1
def sim():
    r=np.random.random_sample()
    if r>P:
        return np.random.normal(mu,sigma)
    else:
        return np.random.exponential(tau)
    
nbins=100 #pocet binu
ibin=10  #divame se na pocty hodnot v 10-tem binu
Nopakovani=100 #pocet opakovani pro kazde Ntot 
Ntot=np.arange(100,5000,100) #ruzne pocty Ntot
hodnota10=np.empty(Nopakovani) #pole hodnot v 10-tem binu
frakce10=np.empty(np.size(Ntot)) #frakce hodnot pripadajici na 10-ty bin
odchylka10=np.empty(np.size(Ntot)) #pole standardnich odchylek
ik=0
for k in Ntot:  #cyklus pro postupne narustajici celkove pocty dat Ntot
    print('počet dat = ',k)
    for j in range(Nopakovani): #100 opakovani pro kazde Not 
        data=np.empty(k)
        for i in range(k):  #generovani histogramu  
            data[i]=sim()
        hist,bin_edges=np.histogram(data,bins=nbins)
        hodnota10[j]=hist[ibin]
    frakce10[ik]=np.mean(hodnota10)/k #jaka frakce hodnot podne do 10-teho binu
    odchylka10[ik]=np.std(hodnota10)  #standardni odchylka pro pocty v 10-binu  
    ik+=1
frakce_mean=np.mean(frakce10) #prumerna frakce pripadajici na 10-ty bin

fig,ax=plt.subplots()
plt.scatter(Ntot,odchylka10)
plt.plot(Ntot,np.sqrt(Ntot*frakce_mean),c='red')
ax.set_xlabel('$N_{tot}$',fontsize=14)
ax.set_ylabel('$\sigma$',fontsize=14)


plt.savefig("hist-bin-err.png",dpi=300)