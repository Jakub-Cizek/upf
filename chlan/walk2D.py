#import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.ion()    # zapneme interaktivni rezim

l=40    # pocet kroku
k=200  # pocet namorniku

x = np.zeros((l,k),dtype='int8')    # pole x-ovych souradnic
y = np.zeros((l,k),dtype='int8')    # pole y-ovych souradnic

stepsx = np.zeros((l,k),dtype='int8')   # pole kroku v x-ove souradnici
stepsy = np.zeros((l,k),dtype='int8')   # pole kroku v y-ove souradnici

cm_subsection = np.linspace(0.0, 1.0, k)    # barvy pro namorniky
colors = [ cm.jet(w) for w in cm_subsection ]

# vygenerujeme vsechny nahodne kroky:
for b in range(k):
    stepsx[:,b] = np.random.choice([-1, 0, 1], size=l)
    stepsy[:,b] = np.random.choice([-1, 0, 1], size=l)

# vygenerujeme vsechny souradnice:
for a in range(l):
    for b in range(k):
        x[a,b] = x[a-1,b] + stepsx[a,b]
        y[a,b] = y[a-1,b] + stepsy[a,b]

# pevny rozsah grafu
plt.xlim(-20, 20) 
plt.ylim(-20, 20) 
plt.pause(2)    
# postupne vykreslujeme prodluzujici se trajektorie, vsechny namorniky najednou: 
for a in range(l):
    for b in range(k):
        plt.title('Step %s' % (a)) 
        plt.plot(x[:a,b], y[:a,b],c=colors[b]) 
    plt.pause(0.01)  
plt.show()    
