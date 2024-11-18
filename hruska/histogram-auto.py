import numpy as np
import matplotlib.pyplot as plt


data=np.loadtxt('data.dat') #nacteni dat ze souboru data.dat

Ndata=np.size(data)
C=np.empty(Ndata)
delta=np.empty(Ndata)
for i in range(1,Ndata):
    hist,bin_edges=np.histogram(data,bins=i) #vytvoreni histogramu
    mean=np.mean(hist)
    sigma=np.std(hist)
    delta[i]=bin_edges[1]-bin_edges[0]
    C[i]=(2*mean-sigma**2)/delta[i]**2

Cmin=np.min(C)
imin=np.where(C==Cmin)[0]
print('pocet dat:',np.size(data)) 
print('optimalni pocet binu: {0:d}'.format(imin[0]))
print('optimalni sirka binu: {0:f}'.format(delta[imin[0]]))

fig,ax=plt.subplots()
ax.scatter(delta[1:Ndata],C[1:Ndata]) #nakresleni histogramu
ax.plot([delta[imin[0]],delta[imin[0]]],[np.min(C),np.max(C)],c='red',ls='dashed' )
plt.xscale('log')
ax.set_xlabel('$\Delta$')
ax.set_ylabel('$C\, (\Delta)$')
plt.savefig("ztratova-funkce.png",dpi=300)

fig,ax=plt.subplots()
ax.hist(data,bins=imin[0],fc='orange',ec='black')
ax.set_xlabel('biny')
ax.set_ylabel('četnosti')
plt.savefig("optimalni-histogram.png",dpi=300)
