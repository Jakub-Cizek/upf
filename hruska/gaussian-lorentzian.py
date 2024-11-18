import numpy as np
import matplotlib.pyplot as plt
from scipy import special

def Gaussian(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-mu)**2/(2*sigma**2))

def Lorentzian(x,x0,w):
    return 1/np.pi*w/2/((w/2)**2+x**2)

def G(x,mu,sigma):
    return 0.5*(1+special.erf((x-mu)/(sigma*np.sqrt(2))))

def L(x,x0,w):
    return 1/np.pi*(np.arctan(2*(x-x0)/w)+np.pi/2)

mu=0
w=1
sigma=1/(2*np.sqrt(2*np.log(2)))
x=np.arange(-5,5,0.01)
fig,ax=plt.subplots()
plt.plot(x,Gaussian(x,mu,sigma),label='Gaussian')
plt.plot(x,Lorentzian(x,mu,w),label='Lorentzian')
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('hustota pravděpodobnosti',fontsize=14)
plt.legend(fontsize=14)

fig,ax=plt.subplots()
plt.plot(x,G(x,mu,sigma),label='G(x)')
plt.plot(x,L(x,mu,w),label='L(x)')
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('distribuční funkce',fontsize=14)
plt.legend(fontsize=14)

print('Gaussián: P(|x|>2) = ',2*(1-G(2,0,sigma)))                              
print('Lorentzián: P(|x|>2) = ',2*(1-L(2,0,w)))                              