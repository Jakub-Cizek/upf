import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

x=np.arange(0,6,0.01)

fig,ax=plt.subplots()
plt.plot(x,gamma(x))
ax.set_xlabel('$x$')
ax.set_ylabel('$\Gamma(x)$')




