import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt("lr_data.txt")
model,V=np.polyfit(data[:,0],data[:,1],1,w=1.0/data[:,2],cov=True)
y_fit=np.polyval(model,data[:,0])
fig,ax=plt.subplots()
ax.errorbar(data[:,0],data[:,1],data[:,2],marker="o",linewidth=0,elinewidth=2,capsize=5)
ax.plot(data[:,0],y_fit,c="red")
ax.set_xlabel("x", fontsize=15)
ax.set_ylabel("y", fontsize=15)
plt.show()
print("y=ax+b")
print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
print("cov(a,b) = ",V[0,1])
print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))

