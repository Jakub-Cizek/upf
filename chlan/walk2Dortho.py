#import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.ion()    # zapneme interaktivni rezim

l=40   # pocet kroku
k=120  # pocet namorniku

x = np.zeros((l,k))    # pole x-ovych souradnic
y = np.zeros((l,k))    # pole y-ovych souradnic

stepsx = np.zeros((l,k))   # pole kroku v x-ove souradnici
stepsy = np.zeros((l,k))   # pole kroku v y-ove souradnici

cm_subsection = np.linspace(0.0, 1.0, k)    # barvy pro namorniky
colors = [ cm.jet(w) for w in cm_subsection ]

# vygenerujeme vsechny nahodne kroky:
for b in range(k):
    stepsx[1:,b] = np.random.random_sample(l-1)
    stepsy[1:,b] = np.random.random_sample(l-1)

# vygenerujeme vsechny souradnice:
for a in range(l):
    for b in range(k):
        x[a,b] = x[a-1,b] + stepsx[a,b] - 0.5
        y[a,b] = y[a-1,b] + stepsy[a,b] - 0.5

# pevny rozsah grafu
plt.xlim(-10, 10) 
plt.ylim(-10, 10) 
plt.pause(1) 
# postupne vykreslujeme prodluzujici se trajektorie, vsechny namorniky najednou: 
for a in range(l):
    plt.clf()
    plt.xlim(-10, 10) 
    plt.ylim(-10, 10) 
    plt.scatter(x[0,b], y[0,b],color=colors[b]) 
    for b in range(k):
        plt.title('Step %s' % (a)) 
        plt.plot(x[:a+1,b], y[:a+1,b],color=colors[b]) 
        plt.scatter(x[a,b], y[a,b],color=colors[b]) 
    plt.pause(0.001)

plt.show()    
