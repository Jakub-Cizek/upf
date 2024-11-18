import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

N=1              # počet sumací
Nsim=100000      # počet vygenerovaných náhodných čísel

x=np.empty(N)
y=np.empty(Nsim)

for i in range(Nsim):
    x=np.random.random_sample(N)
    y[i]=np.sum(x)
    

# Co očekáváme z CLV za parametry gaussovky?
mu=N/2          
sigma=np.sqrt(N/12)

# Vykreslíme gaussovku a histogram N-krát sečtených náhodných čísel
xp=np.arange(0,N,0.01)
yp=norm.pdf(xp,mu,sigma)
plt.pause(0.1)
plt.hist(y,bins=100,density='True')    
plt.plot(xp,yp,c='red')


