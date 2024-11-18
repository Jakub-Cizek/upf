#import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import time

plt.ion()    # zapneme interaktivni rezim

l=30    # pocet kroku
k=100    # pocet namorniku

x = np.zeros((l,k),dtype='int32')    # pole x-ovych souradnic
y = np.zeros((l,k),dtype='int32')    # pole y-ovych souradnic

stepsx = np.zeros((l,k),dtype='int32')   # pole kroku v x-ove souradnici
stepsy = np.zeros((l,k),dtype='int32')   # pole kroku v y-ove souradnici

cm_subsection = np.linspace(0.0, 1.0, k)    # barvy pro namorniky
colors = [ cm.jet(w) for w in cm_subsection ]

# vygenerujeme vsechny nahodne kroky:
for b in range(k):
    stepsx[1:,b] = np.random.choice([-1, 1], size=l-1)
    stepsy[1:,b] = 1
    stepsx[0,b] = 0
    stepsy[0,b] = 0

for b in range(k):
    x[:,b] = np.cumsum(stepsx[:,b]) 
    y[:,b] = np.cumsum(stepsy[:,b])

# pevny rozsah grafu
#plt.xlim(-20, 20) 
#plt.ylim(-20, 20)  


plt.subplots(figsize=(24,10))
plt.pause(2)
for a in range(1,l):
    plt.clf()
    for b in range(k):      
        # postupne vykreslujeme prodluzujici se trajektorie, vsechny namorniky najednou: 
        plt.subplot(1, 2, 1)
#        plt.xlim(-np.sqrt(l), np.sqrt(l)) 
        plt.ylim(-2, l) 
        plt.plot(x[:a,b], y[:a,b], c=colors[b]) 
        plt.scatter(x[a-1,b], y[a-1,b], c=colors[b]) 
        plt.title('Step %s' % (a))        
    # vygnerujeme histogram poloh x pro vsechny namorniky:
    plt.subplot(1, 2, 2)
    plt.xlim(-3*np.sqrt(l), 3*np.sqrt(l))   # odhad vhodneho rozsahu histogramu
    plt.ylim(-1, k)     
    plt.hist(x[a-1,:], bins=15, range=(-3*np.sqrt(l),3*np.sqrt(l)))
    plt.xlabel('x')
    plt.ylabel('counts')     
    plt.pause(0.01)       

plt.show()


