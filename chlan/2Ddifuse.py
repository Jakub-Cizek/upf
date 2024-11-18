import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib import cm
import numpy as np
from scipy.stats import norm
import scipy


plt.ion()    # zapneme interaktivni rezim

l=15 # pocet kroku
k=2000   # pocet namorniku

T=0.3 # "teplotni" parametr
width=0.2 # sirka binu

x = np.zeros((l,k))    # pole x-ovych souradnic
y = np.zeros((l,k))    # pole y-ovych souradnic

stepsr = np.zeros((l,k))   # pole kroku v r
stepsf = np.zeros((l,k))   # pole kroku v phi

cm_subsection = np.linspace(0.0, 1.0, k)    # barvy pro namorniky
colors = [ cm.jet(w) for w in cm_subsection ]

# vygenerujeme vsechny nahodne kroky:
for b in range(k):
   # stepsr[:,b] = np.random.random_sample(l) # delka r
    stepsr[:,b] = np.random.normal(2*T*np.sqrt(2/np.pi),T*np.sqrt(3*np.pi-8)/np.sqrt(np.pi),l)  # delka r podle Maxwell-Boltzmann
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
        plt.xlim(-6, 6) 
        plt.ylim(-6, 6) 
        plt.plot(x[:a+1,b], y[:a+1,b], color=colors[b]) 
        plt.scatter(x[a,b], y[a,b], color=colors[b])
        plt.title('Step %s' % (a))        
    # vygnerujeme histogram poloh x pro vsechny namorniky:
    plt.subplot(1, 2, 2)
    plt.xlim(-6, 6) 
    n, bins, patches = plt.hist(x[a,:], bins=np.arange(min(x[a,:]), max(x[a,:]) + width, width), density=True)

    # nafitujeme vznikly histogram Gaussovkou:    
    (mu, sigma) = norm.fit(x[a,:])
    gaussian = norm.pdf(bins, mu, sigma)
    plt.plot(bins, gaussian, 'r--', linewidth=2)
    
    plt.xlabel('r')
    plt.ylabel('counts (norm.)')     
    plt.title(r'Histogram vzdalenosti od pocatku $\mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
    plt.pause(0.03)
    plt.draw()      

#raw_input()


