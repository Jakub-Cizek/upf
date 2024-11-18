import numpy as np
import matplotlib.pyplot as plt
N=1000
x0_real=5
l_real=10
x=np.empty(N)
x=l_real*np.tan(np.random.random_sample(N)*np.pi-np.pi/2.0)+x0_real

fig,ax=plt.subplots()
x_range=l_real*np.tan(np.pi*80/180)
ax.hist(x,bins=20,range=(x0_real-x_range,x0_real+x_range),density=True)
xp=np.linspace(x0_real-x_range,x0_real+x_range,100)
yp=1/np.pi*l_real/(l_real**2+(xp-x0_real)**2)
ax.plot(xp,yp,c="red")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

x0=np.linspace(-15,15,100)
N_x0=np.size(x0)
l=np.linspace(0.1,20,100)
N_l=np.size(l)

l_mesh,x0_mesh=np.meshgrid(l,x0)
ln_L=np.zeros([N_x0,N_l])
for i in range(N):
    ln_L=ln_L+np.log(l_mesh)-np.log(np.pi*(l_mesh**2+(x[i]-x0_mesh)**2))
ln_L_max=np.max(ln_L)
i_max,j_max=np.where(ln_L==ln_L_max)
fig,ax=plt.subplots()
ax.contour(x0_mesh,l_mesh,ln_L,levels=200)
ax.scatter(x0_real,l_real)
ax.scatter(x0[i_max],l[j_max],c="red",marker="+",s=100)
ax.set_xlabel("x0")
ax.set_ylabel("l")
plt.show()
print('x0= %.8f' % x0[i_max])
print('l= %.8f' % l[j_max])