import numpy as np
import matplotlib.pyplot as plt


a=16807
#a=65539    # RANDU
m=2147483647    # m = 2^31 - 1
i_seed=23456
n=1000000
x = np.empty(n, dtype=float) #deklarace pole x-souradnic
y = np.empty(n, dtype=float) #deklarace pole y-souradnic
color=np.empty([n,3],dtype=float) #deklarace pole barva RGB


#ciste multiplikativni generator
i_old=i_seed
for i in range(0,n):
   i_next=(a*i_old) % m
   i_old=i_next
   x[i]=i_next/m
   
   i_next=(a*i_old) % m
   i_old=i_next
   y[i]=i_next/m
      
   i_next=(a*i_old) % m
   i_old=i_next
   color[i,0]=i_next/m

   i_next=(a*i_old) % m
   i_old=i_next
   color[i,1]=i_next/m

   i_next=(a*i_old) % m
   i_old=i_next
   color[i,2]=i_next/m

plt.scatter(x,y,s=1,c=color,edgecolors="none") #nakresli graf
