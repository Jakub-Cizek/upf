import numpy as np
import matplotlib.pyplot as plt
x1=np.array([5,6,7,8,9])
y1=np.array([3.5,4.2,5.7,6.9,7.3])
ey1=np.array([0.2,0.2,0.3,0.5,0.4])
x2=np.array([0,1,2,3])
y2=np.array([6.7,5.4,4.2,3.1])
ey2=np.array([0.4,0.2,0.3,0.5])
fig,ax=plt.subplots()
ax.errorbar(x1,y1,ey1,linewidth=0,elinewidth=2,capsize=5,marker="o",label="y1",c="blue")
ax.errorbar(x2,y2,ey2,linewidth=0,elinewidth=2,capsize=5,marker="o",label="y2",c="orange")
ax.legend(fontsize=15)
model1,pcov1=np.polyfit(x1,y1,1,w=1/ey1,cov=True)
model2,pcov2=np.polyfit(x2,y2,1,w=1/ey2,cov=True)
a1=model1[0]
b1=model1[1]
a2=model2[0]
b2=model2[1]
xfit=([0,1,2,3,4,5,6,7,8,9])
yfit1=np.polyval(model1,xfit)
yfit2=np.polyval(model2,xfit)
ax.plot(xfit,yfit1,c="blue")
ax.plot(xfit,yfit2,c="orange")
ax.set_ylim(0,8)
ax.set_xlabel("x",fontsize=15)
ax.set_ylabel("y",fontsize=15)
x0=(b1-b2)/(a2-a1)
y0=(a2*b1-a1*b2)/(a2-a1)
ax.plot([x0,x0],[1.2,3],"g--",c="black")
ax.plot([3,4.5],[y0,y0],"g--",c="black")
plt.show()
print("závislost 1: y = a1 x + b1 ")
print("a1 = ",a1,"+/-",np.sqrt(pcov1[0,0])) 
print("b1 = ",b1,"+/-",np.sqrt(pcov1[1,1])) 
print("cov(a1,b1) = ",pcov1[0,1]) 
print("závislost 2: y = a2 x + b2 ")
print("a2 = ",a2,"+/-",np.sqrt(pcov2[0,0])) 
print("b2 = ",b2,"+/-",np.sqrt(pcov2[1,1])) 
print("cov(a2,b2) = ",pcov2[0,1]) 

dx0_a1=(b1-b2)/(a2-a1)**2
dx0_a2=-(b1-b2)/(a2-a1)**2
dx0_b1=1/(a2-a1)
dx0_b2=-1/(a2-a1)
e_x0=np.sqrt(dx0_a1**2*pcov1[0,0]+dx0_b1**2*pcov1[1,1]+dx0_a2**2*pcov2[0,0]+dx0_b1**2*pcov2[1,1]+2*dx0_a1*dx0_b1*pcov1[0,1]+2*dx0_a2*dx0_b2*pcov2[0,1])
dy0_a1=a2*(b1-b2)/(a2-a1)**2
dy0_a2=a1*(b2-b1)/(a2-a1)**2
dy0_b1=a2/(a2-a1)
dy0_b2=-a1/(a2-a1)
e_y0=np.sqrt(dy0_a1**2*pcov1[0,0]+dy0_b1**2*pcov1[1,1]+dy0_a2**2*pcov2[0,0]+dy0_b2**2*pcov2[1,1]+2*dy0_a1*dy0_b1*pcov1[0,1]+2*dy0_a2*dy0_b2*pcov2[0,1])
print("průsečík:")
print("x0 = ",x0,"+/-",e_x0)
print("y0 = ",y0,"+/-",e_y0)

