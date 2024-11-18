import numpy as np
import matplotlib.pyplot as plt
n=100000 #pocet dat
nbins=100
data=np.array(n) #deklarace pole x-souradnic
data=np.random.random_sample(n) #naplni pole nahodnymi hodnotami
hist,bin_edges=np.histogram(data,bins=nbins,density=True) #udela histogram
x=bin_edges[0:nbins] #x-ova souradnice
y=hist  #y-ova souradnice
fig,ax=plt.subplots() #vytvoreni obrazku
ax.step(x,y) #vykresleni grafu
plt.xlim(0,1) #nastaveni rozmezi osy x: 0,1
plt.ylim(0.8,1.2) #nastaveni rozmezi osy y> 0.5,1.5

