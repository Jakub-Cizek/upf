import numpy as np
import matplotlib.pyplot as plt
#simulace
a0=3
a1=1
a2=-0.5
a3=1.1
a4=-0.1
x=np.linspace(0,10,100)
y=np.polyval([a4,a3,a2,a1,a0],x)
ey=np.abs(np.random.normal(10,5,100))
y=y+(np.random.normal(0,ey,100))
#plot
fig,ax=plt.subplots()
ax.errorbar(x,y,ey,linewidth=0,elinewidth=2,marker="o",capsize=5,fillstyle="none")
#fit
model,V=np.polyfit(x,y,4,w=1/ey,cov=True)
ax.plot(x,np.polyval(model,x),c="red",lw=5)
ax.set_xlabel("x",fontsize=15)
ax.set_ylabel("y",fontsize=15)
plt.show()
print("a0 = ",model[4],"+/-",np.sqrt(V[4,4]))
print("a1 = ",model[3],"+/-",np.sqrt(V[3,3]))
print("a2 = ",model[2],"+/-",np.sqrt(V[2,2]))
print("a3 = ",model[1],"+/-",np.sqrt(V[1,1]))
print("a4 = ",model[0],"+/-",np.sqrt(V[0,0]))