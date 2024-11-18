import numpy as np
import matplotlib.pyplot as plt

P=0.75
mu=10
sigma=2
tau=4
Ntot=1000
nbins=100
data=np.empty(Ntot)

# simulace nahodne promenne s rozdelenim exp+gaussian 3:1
def sim():
    r=np.random.random_sample()
    if r>P:
        return np.random.normal(mu,sigma)
    else:
        return np.random.exponential(tau)
    
for i in range(1,Ntot):
    data[i]=sim()
hist,bin_edges=np.histogram(data,bins=nbins)

fig,ax=plt.subplots()
ax.step(bin_edges[0:nbins],hist) #nakresleni histogramu
ax.set_xlabel('$n_k$',fontsize=14)
ax.set_ylabel('$k$',fontsize=14)