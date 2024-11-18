import numpy as np
import matplotlib.pyplot as plt
n=100000 #pocet dat
nbins=100 #pocet binu
x=np.linspace(0,1,nbins) #x-ova souradnice grafu
y=np.zeros(nbins) #y-ova souradnice grafu
for i in range(0,n):
    ibin=int(nbins*np.random.random()) #generuje nahodne cislo
    y[ibin]=y[ibin]+1 #inkrementace histogramu
y=y/(n/nbins) #normalizace
plt.step(x,y) #vykresleni grafu

