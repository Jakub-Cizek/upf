import numpy as np
import matplotlib.pyplot as plt

def gaussian(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-mu)**2/(2*sigma**2))

N=10
Nsim=10000

x=np.empty(N)
y=np.empty(Nsim)

for i in range(Nsim):
    x=np.random.random_sample(N)
    y[i]=np.sum(x)
    

mu=N/2
sigma=np.sqrt(N/12)
xp=np.arange(0,N,0.01)
yp=gaussian(xp,mu,sigma)
    
plt.hist(y,bins=100,density='True')    
plt.plot(xp,yp,c='red')