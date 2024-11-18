
import numpy as np
import matplotlib.pyplot as plt

def Poisson(k,nu):
    return(nu**k*np.exp(-nu)/np.math.factorial(k))
           
vPoisson=np.vectorize(Poisson) #vektorizace funkce Poisson

N=2306 #pocet hodnot
nu=0.777 #ocekavana hodnota
data=np.random.poisson(nu,N) #simulce Poissonova rozdeleni

k=np.arange(0,9,1,dtype=int)
P=vPoisson(k,nu)


plt.hist(data,bins=k,density='True')
plt.plot([0,1],[P[0],P[0]],c='red')
plt.step(k+1,P,c='red')
plt.xlim(0,8)
