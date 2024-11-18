import numpy as np
from matplotlib import pyplot as plt

n = 10   # pocet hodu
hody = np.random.randint(1, 7, n)    # pole jednotlivych hodu 6-stennou kostkou
prumer = []    # pripravime pole pro aritmeticky prumer po i-tem hodu

for i in range(n):
    prumer.append(hody[:i+1].mean())    # pocitani prumeru po kazdem hodu
   
fig, ax = plt.subplots()
plt.pause(0.1)
ax.set_ylim(1,6)
ax.set_ylabel("Aritmeticky prumer")
ax.set_xlabel("Pocet hodu")
ax.grid(color='black', linestyle='-', linewidth=1, axis='y')

#ax.set_xscale('log')
#ax.text(10,4.5,prumer[9])
#ax.text(100,4.5,prumer[99])
#ax.text(1000,4.5,prumer[999])
#ax.text(10000,4.5,prumer[9999])
#ax.text(100000,4.5,prumer[99999])

plt.plot(prumer)
plt.show()
