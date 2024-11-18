import numpy as np
import matplotlib.pyplot as plt
N=100
p=0.5
Nsim=100
mean_sq=np.zeros(N)
mean_abs=np.zeros(N)
step=np.zeros(N)
for i in range(1,N):
    data_k=np.random.binomial(i,p,Nsim)
    mean_sq[i]=np.sqrt(np.mean((2*data_k-i)**2))
    mean_abs[i]=np.mean(np.abs(2*data_k-i))
    step[i]=i
fig,ax=plt.subplots()
ax.plot(step,mean_sq,c="blue")  
ax.plot(step,mean_abs,c="green")  
ax.plot(step,np.sqrt(step),c="red")  