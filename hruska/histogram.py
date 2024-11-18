import numpy as np
import matplotlib.pyplot as plt

nbins=10 #pocet binu
data=np.loadtxt('data.dat') #nacteni dat ze souboru data.dat
hist,bin_edges=np.histogram(data,bins=nbins) #vytvoreni histogramu

fig,ax=plt.subplots(figsize=(4,4))
ax.step(bin_edges[0:nbins],hist) #nakresleni histogramu

print('pocet dat:',np.size(data)) 
print('pocet binu: ',nbins)
print('min. hodnota:',np.min(data))
print('max. hodnota:',np.max(data))
print('sirka binu: ',(np.max(data)-np.min(data))/nbins)
plt.savefig("histogram10.png",dpi=300)