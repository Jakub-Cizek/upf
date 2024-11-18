import numpy as np
import matplotlib.pyplot as plt

N=10000
tau=100
r=np.random.random_sample(N)
x=-tau*np.log(r)
xp=np.linspace(0,10*tau,100)
yp=1/tau*np.exp(-xp/tau)
fig,ax=plt.subplots()
plt.hist(x,bins=100,density='True')
plt.plot(xp,yp,c='red')
ax.set_xlabel('t ($\mu$s)')
ax.set_ylabel('pdf')

