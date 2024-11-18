import numpy as np
import matplotlib.pyplot as plt
n=100000 #pocet dat, ktera b udeme simulovat
point=np.array([n,5]) #5 nahodnych cisel x-souradnice, y-souradnice, barva R,G,B
point=np.random.random_sample([n,5]) #vygenerovani nahodnych cisel
plt.scatter(point[0:n,0],point[0:n,1],s=2,c=point[0:n,2:5],edgecolor="none") #nakresleni grafu   