import numpy as np
import matplotlib.pyplot as plt
#from scipy.special import gamma
from scipy.stats import t
N=1000
eps=0.05
x=np.linspace(-5,5,N)
y=np.zeros([N,10])
legend=np.empty(10,dtype=object)
for i in range(1,10):
    #y[:,i-1]=gamma((i+1.0)/2.0)/(np.sqrt(i*np.pi)*gamma(i/2.0))*(1+x**2/i)**(-(i+1.0)/2.0)
    y[:,i-1]=t.pdf(x,i)
    plt.plot(x,y[:,i-1]) 
    legend[i-1]="v="+str(i)
plt.xlabel("x")
plt.ylabel("t(x)")
plt.legend(legend)
plt.savefig("student.png",dpi=600)

