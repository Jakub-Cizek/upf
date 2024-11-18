import numpy as np
import matplotlib.pyplot as plt
N=1000
x=np.empty(N)
x=np.random.randn(N)
z=1/x
xp=np.linspace(-10,10,1000) #x pro vykresleni hustoty pravdepodobnosti
yp=1/np.sqrt(2*np.pi)*np.exp(-xp**2/2) #normalni rozdeleni
zp=1/np.sqrt(2*np.pi)*np.exp(-1/(2*xp**2))*1/xp**2 #nova nahodona promenna z
#stara nahodna promenna
fig,ax=plt.subplots()
ax.hist(x,bins=50,range=(-5,5),density=True)
ax.plot(xp,yp,c="red")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
#nova nahodna promenna 
fig,ax=plt.subplots()
ax.hist(z,bins=50,range=(-10,10),density=True)
ax.plot(xp,zp,c="red")
ax.set_xlabel("z")
ax.set_ylabel("g(z)")