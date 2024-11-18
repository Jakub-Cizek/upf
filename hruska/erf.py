import numpy as np
import matplotlib.pyplot as plt 
from scipy import special

x=np.arange(-5,5,0.1)
fig,ax=plt.subplots()
ax.plot(x,special.erf(x))
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('erf(x)',fontsize=14)