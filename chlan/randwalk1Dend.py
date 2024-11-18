#import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import time

plt.ion()    # zapneme interaktivni rezim

l=111   # pocet kroku
k=400    # pocet namorniku

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


plt.subplots(figsize=(24,10))
for b in range(k):      
    plt.subplot(1, 2, 1)
    plt.ylim(-2, l) 
    plt.plot(x[:,b], y[:,b], color=colors[b]) 
    plt.scatter(x[:,b], y[:,b], s=4, color=colors[b]) 
plt.subplot(1, 2, 2)
plt.xlim(-3*np.sqrt(l), 3*np.sqrt(l))   # odhad vhodneho rozsahu histogramu
plt.ylim(-1, k)      # odhad vhodneho rozsahu histogramu
plt.hist(x[l-1,:], bins=15, range=(-3*np.sqrt(l),3*np.sqrt(l)))
plt.xlabel('x')
plt.ylabel('counts')     
plt.show()




