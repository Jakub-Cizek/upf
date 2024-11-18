import numpy as np
import matplotlib.pyplot as plt
N=10000
x=np.empty(N)
y=np.empty(N)
x[0]=y[0]=0
for i in range(1,N):
    alpha=np.random.random_sample()*2*np.pi
    x[i]=x[i-1]+np.cos(alpha)
    y[i]=y[i-1]+np.sin(alpha)
 
fig,ax=plt.subplots()
ax.step(x,y)
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)
plt.savefig("randomwalk-2D-PH.png",dpi=300)