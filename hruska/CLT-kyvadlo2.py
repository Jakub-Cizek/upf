import numpy as np
import matplotlib.pyplot as plt
N=10000
Nsum=10
x=np.zeros(N)
for i in range(1,Nsum):
    for j in range(0,i):
        x=x+np.sin(np.pi*(np.random.random_sample(N)-0.5))
    x=x/i
    fig,ax=plt.subplots()
    ax.set_title("Nsum="+str(i))
    ax.hist(x,bins=100,density=True)
    