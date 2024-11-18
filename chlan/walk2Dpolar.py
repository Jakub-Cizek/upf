import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.ion()    # zapneme interaktivni rezim

l=50    # pocet kroku
k=1   # pocet namorniku

x = np.zeros((l,k))    # pole x-ovych souradnic
y = np.zeros((l,k))    # pole y-ovych souradnic

stepsr = np.zeros((l,k))   # pole kroku v r
stepsf = np.zeros((l,k))   # pole kroku v phi

cm_subsection = np.linspace(0.0, 1.0, k)    # barvy pro namorniky
colors = [ cm.jet(w) for w in cm_subsection ]

# vygenerujeme vsechny nahodne kroky:
for b in range(k):
    stepsr[:,b] = np.random.random_sample(l) # delka r
    stepsf[:,b] = np.random.random_sample(l) # uhel phi

# vygenerujeme vsechny souradnice:
for a in range(l-1):
    for b in range(k):
        x[a+1,b] = x[a,b] + stepsr[a,b] * np.sin(stepsf[a,b]*2*np.pi) 
        y[a+1,b] = y[a,b] + stepsr[a,b] * np.cos(stepsf[a,b]*2*np.pi) 


plt.subplots(figsize=(24,10))
plt.pause(1)
for a in range(0,l):
    plt.clf()
    plt.xlim(-10, 10) 
    plt.ylim(-10, 10) 
    for b in range(k):      
        # postupne vykreslujeme prodluzujici se trajektorie, vsechny namorniky najednou: 
        plt.subplot(1, 2, 1)
        plt.xlim(-10, 10) 
        plt.ylim(-10, 10) 
        plt.xlabel('x')
        plt.ylabel('y')     
        plt.plot(x[:a+1,b], y[:a+1,b], color=colors[b]) 
        plt.scatter(x[a,b], y[a,b], color=colors[b]) 
        plt.title('Step %s' % (a))        
    # vygnerujeme histogram vzdalenosti r pro vsechny namorniky:
    plt.subplot(1, 2, 2)
    plt.title(r'Histogram vzdalenosti od pocatku')
    plt.xlabel('r')
    plt.ylabel('counts')     
    plt.hist(x[a,:], bins=21, range=(-10,10))
    plt.pause(0.01)
    plt.draw()

