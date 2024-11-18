#import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import time

plt.ion()    # zapneme interaktivni rezim

l=20   # pocet kroku
k=1  # pocet namorniku

x = np.zeros((l,k),dtype='int32')    # pole x-ovych souradnic
y = np.zeros((l,k),dtype='int32')    # pole y-ovych souradnic

stepsx = np.zeros((l,k),dtype='int32')   # pole kroku v x-ove souradnici
stepsy = np.zeros((l,k),dtype='int32')   # pole kroku v y-ove souradnici

cm_subsection = np.linspace(0.0, 1.0, k)    # barvy pro namorniky
colors = [ cm.jet(w) for w in cm_subsection ]

# vygenerujeme vsechny nahodne kroky:
for b in range(k):
    stepsx[0,b] = 0
    stepsy[0,b] = 0 
    stepsx[1:,b] = np.random.choice([-1, 1], size=l-1)
    stepsy[1:,b] = 1

for b in range(k):
    x[:,b] = np.cumsum(stepsx[:,b]) 
    y[:,b] = np.cumsum(stepsy[:,b])

# pevny rozsah grafu
#plt.xlim(-20, 20) 
plt.ylim(-1, l+1)  
plt.pause(2)
for a in range(1,l):
    for b in range(k):
        plt.title('Step %s' % (a)) 
        plt.plot(x[:a,b], y[:a,b], color=colors[b]) 
        plt.scatter(x[a-1,b], y[a-1,b], color=colors[b]) 
        plt.pause(0.01)
plt.show()
