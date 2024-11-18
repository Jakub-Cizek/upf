import numpy as np
import matplotlib.pyplot as plt
n=10000 #number of simulated data
l=1 #delka zavesu (m)
g=9.81 #gravitacni zrychleni (m/s2)
omega=np.sqrt(g/l) #uhlova frekvecne
T=2*np.pi/omega #perioda
print("perioda",T,"s" )
alfa_0=5 #pocatecni uhel vychyleni (deg)
x_0=l*alfa_0*np.pi/180 #amplituda
print("amplituda",x_0,"m" )
t=np.array(n)
x=np.array(n)
t=T*np.random.random_sample(n)
x=x_0*np.cos(omega*t)
fig,ax=plt.subplots() #to je potreba abychom mohli pojmenovat osy 
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.hist(x,bins=100,density=True)
eps=1e-3 #to je protoze v x_0 neni f(x) definovana 
xp=np.linspace(-x_0+eps,x_0-eps,1000)
f=1/np.pi*1/np.sqrt(x_0**2-xp**2)
plt.plot(xp,f)


