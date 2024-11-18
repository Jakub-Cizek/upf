import numpy as np
import matplotlib.pyplot as plt

# simulace nah. promemne s rozdeleni exp+gaussian
def sim():
    branching_ratio=0.7
    r=np.random.random_sample()
    if r>branching_ratio:
        return np.random.normal(8,1)
    else:
        return np.random.exponential(3)
    
nbins=100 #pocet binu
ibin=10  #divame se na pocty hodnot v 10-tem binu
Nopakovani=100 #pocet opakovani pro kazde Ntot 
Ntot=np.arange(100,5000,100) #ruzne pocty Ntot
hodnota=np.empty(Nopakovani) #pole hodnot v 10-tem binu
fraction=np.empty(np.size(Ntot)) #frakce hodnot pripadajici na 10-ty bin
std=np.empty(np.size(Ntot)) #pole standardnich odchylek
ik=0
for k in Ntot:  #cyklu pro postupne narustajici celkove pocty dat Ntot
    print('počet dat = ',k)
    for j in range(Nopakovani): #100 opakovani por kazde Not 
        data=np.empty(k)
        for i in range(k):  #generovani histogramu  
            data[i]=sim()
        hist,bin_edges=np.histogram(data,bins=nbins)
        hodnota[j]=hist[ibin]
    fraction[ik]=np.mean(hodnota)/k #jaka frakce hodnot podne do 10-teho binu
    std[ik]=np.std(hodnota)  #standardni odchylka pro pocty v 10-binu  
    ik+=1
fraction_mean=np.mean(fraction) #prumerna frakce pripadajici na 10-ty bin

fig,ax=plt.subplots()
plt.scatter(Ntot,std)
plt.plot(Ntot,np.sqrt(Ntot*fraction_mean),c='red')
ax.set_xlabel('$N_{tot}$',fontsize=14)
ax.set_ylabel('$\sigma$',fontsize=14)

