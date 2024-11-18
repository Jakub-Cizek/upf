import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,cauchy

N=1          # počet sumací
Nsim=100000    # počet vygenerovaných náhodných čísel

x=np.empty(N)
y=np.empty(Nsim)


for i in range(Nsim):
    x=np.random.standard_cauchy(N)
    y[i]=np.sum(x)/N
    

# Co očekáváme z CLV za parametry gaussovky?
mu=0
sigma=1/(2*np.sqrt(2*np.log(2)))
w=1


# Vykreslíme gaussovku a histogram N-krát sečtených náhodných čísel
xp=np.arange(-20,20,0.01)
yp=norm.pdf(xp,mu,sigma)
ypc=cauchy.pdf(xp,mu,w)

plt.pause(0.1)
plt.hist(y,bins=1000,range=(-20,20),density='True')    
plt.plot(xp,yp,c='red')
plt.plot(xp,ypc,c='green')

