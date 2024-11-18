import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def dvojgaussian(x,mu1,sigma1,mu2,sigma2):
    return 0.3/(np.sqrt(2*np.pi)*sigma1)*np.exp(-(x-mu1)**2/(2*sigma1**2)) + 0.7/(np.sqrt(2*np.pi)*sigma2)*np.exp(-(x-mu2)**2/(2*sigma2**2))


N=1      # počet sumací
Nsim=100000   # počet vygenerovaných náhodných čísel

x1=np.zeros(Nsim)
x2=np.zeros(Nsim)
x=np.zeros([N,Nsim])
y=np.zeros(Nsim)
y1=np.zeros(Nsim)
y2=np.zeros(Nsim)

for j in range(N):
    x1=np.random.normal(0,1,int(0.3*Nsim))
    x2=np.random.normal(5,1,int(0.7*Nsim))
    x[j,:]=np.random.choice(np.concatenate((x1,x2)),Nsim)

for i in range(Nsim):
    y[i]=np.sum(x[:,i])/N


# Co očekáváme z CLV za parametry gaussovky?
g2_mean=0.3*0 + 0.7*5
mu=g2_mean

g2_variance=0.3*1 + 0.7*1 + 0.3*(0-g2_mean)**2 + 0.7*(5-g2_mean)**2
sigma=np.sqrt(g2_variance/N)

# Vykreslíme gaussovku a histogram N-krát sečtených náhodných čísel
xp=np.arange(-4,8,0.01)
yp=norm.pdf(xp,mu,sigma)
plt.pause(0.1)
plt.hist(y,bins=200,density='True')    
plt.plot(xp,yp,c='red')

