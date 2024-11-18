import numpy as np
import matplotlib.pyplot as plt

P=0.75
mu=10
sigma=2
tau=4
Ntot=1000
nbins=100
data=np.empty(Ntot)
    
for i in range(1,Ntot):
    r=np.random.random_sample()
    if r>P: 
        data[i]=np.random.normal(mu,sigma,1)
    else:
        data[i]=np.random.exponential(tau,1)
hist,bin_edges=np.histogram(data,bins=nbins)

fig,ax=plt.subplots()
ax.step(bin_edges[0:nbins],hist) #nakresleni histogramu
ax.set_xlabel('$n_k$',fontsize=14)
ax.set_ylabel('$k$',fontsize=14)