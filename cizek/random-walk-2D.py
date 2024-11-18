import numpy as np
import matplotlib.pyplot as plt
N=10000
x=np.empty(N)
y=np.empty(N)
x[0]=y[0]=0
for i in range(1,N):
    x[i]=x[i-1]+np.random.choice([-1,1],1)
    y[i]=y[i-1]+np.random.choice([-1,1],1)
 
plt.step(x,y)