import numpy as np
#import matplotlib.pyplot as plt

x=np.random.normal(3, 0.5, 1000)

#print(x)

np.savetxt('gauss.txt', x, fmt='%10.5f')

#plt.hist(x, bins=10)
#plt.show()