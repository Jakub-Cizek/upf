import numpy as np
import matplotlib.pyplot as plt
N=10000
Nsum=33

def gaussian(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-mu)**2/(2*sigma**2))

for i in range(1,Nsum):
    x=np.zeros(N)
    for j in range(0,i):
        x=x+np.sin(np.pi*(np.random.random_sample(N)-0.5))
    x=x/i
    mu=0
    sigma=np.sqrt(1/(2*i))
    xp=np.arange(-2,2,0.01)
    yp=gaussian(xp,mu,sigma)
    fig,ax=plt.subplots()
    ax.set_title("Nsum="+str(i))
    ax.hist(x,bins=100,density=True)
    ax.plot(xp,yp,c='red')
    plt.xlim(-1,1)    