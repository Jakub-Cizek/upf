import numpy as np
import matplotlib.pyplot as plt
nbin=100
data=np.loadtxt("kyvadlo-1.db",usecols=(2))
print(data)
ndata=len(data)
data_min=np.amin(data)
data_max=np.amax(data)
print("precteno", ndata, "hodnot")
print("minimalni hodnota=",data_min)
print("maximalni hodnota=",data_max)
data=data/(0.5*(np.abs(data_min)+data_max))
fig,ax=plt.subplots()
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.hist(data,bins=nbin,density=True)
eps=1e-2
x=np.linspace(-1+eps,1-eps,nbin)
f=1/np.pi*1/np.sqrt(1-x**2)
plt.plot(x,f,c="red")