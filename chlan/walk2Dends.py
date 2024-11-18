#import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.ion()    # zapneme interaktivni rezim

l=50   # pocet kroku
k=1000   # pocet namorniku

x = np.zeros((l,k))    # pole x-ovych souradnic
y = np.zeros((l,k))    # pole y-ovych souradnic
r = np.zeros((l,k))    # pole vzdalenosti

stepsx = np.zeros((l,k))   # pole kroku v x-ove souradnici
stepsy = np.zeros((l,k))   # pole kroku v y-ove souradnici


cm_subsection = np.linspace(0.0, 1.0, k)    # barvy pro namorniky
colors = [ cm.jet(w) for w in cm_subsection ]

# vygenerujeme vsechny nahodne kroky:
for b in range(k):
    stepsx[:,b] = np.random.random_sample(l)
    stepsy[:,b] = np.random.random_sample(l)

# vygenerujeme vsechny souradnice:
for a in range(l-1):
    for b in range(k):
        x[a+1,b] = x[a,b] + stepsx[a,b] * np.sin(stepsy[a,b]*2*np.pi) 
        y[a+1,b] = y[a,b] + stepsx[a,b] * np.cos(stepsy[a,b]*2*np.pi) 
        r[a+1,b] = np.sqrt(np.power(x[a+1,b],2) + np.power(y[a+1,b],2))

# pevny rozsah grafu
#plt.xlim(-10, 10) 
#plt.ylim(-10, 10) 


a=0
#for b in range(k):
#    plt.title('Step %s' % (a)) 
#    plt.scatter(x[a,b], y[a,b],c=colors[b])   
#plt.draw()
  
  
plt.subplots(figsize=(24,10))
plt.pause(1)
# postupne vykreslujeme prodluzujici se trajektorie, vsechny namorniky najednou: 
for a in range(l-1):
    plt.clf()
    plt.xlim(-10, 10) 
    plt.ylim(-10, 10) 
    for b in range(k):
     #   plt.title('Step %s' % (a)) 
 #       plt.plot(x[:a+1,b], y[:a+1,b],c=colors[b]) 
     #   plt.scatter(x[a,b], y[a,b],c=colors[b]) 
        
        plt.subplot(1, 2, 1)
        plt.xlim(-10, 10) 
        plt.ylim(-10, 10) 
        plt.scatter(x[a-1,b], y[a-1,b],s=10,color=colors[b],edgecolors="none")
        plt.title('Step %s' % (a))
        plt.xlabel('x')
        plt.ylabel('y')

    plt.subplot(1, 2, 2)
    plt.xlim(-0.5, 10.5) 
    #    plt.ylim(-10, 10)
    #    r=np.sqrt(np.power(x[a,b],2) + np.power(y[a,b],2))
    plt.hist(r[a-1,:], bins=20)
    #   plt.plot(x[:a+1,b], y[:a+1,b],c=colors[b])
    #    plt.scatter(x[a,b], y[a,b],s=10,c=colors[b],edgecolors="none")
    plt.xlabel('r')
    plt.ylabel('counts')   
    plt.pause(0.0001)
plt.show()    
