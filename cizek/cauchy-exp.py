import numpy as np
import matplotlib.pyplot as plt
distance=50
x0=110
bcg=17.6
position=np.loadtxt("cauchy.dat",dtype=float,usecols=(0))
count=np.loadtxt("cauchy.dat",dtype=float,usecols=(1))
count=count-17.6
count=count/(np.sum(count)*7)
position=position-6.25
x=np.linspace(0,200,1000)
y=1/np.pi*distance/(distance**2+(x-x0)**2)
fig,ax=plt.subplots()
ax.step(position,count)
ax.plot(x,y,c="red")
