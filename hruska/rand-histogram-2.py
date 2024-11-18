import numpy as np
import matplotlib.pyplot as plt
n=100000 #pocet dat
nbins=100
data=np.array(n) #deklarace pole x-souradnic
data=np.random.random_sample(n) #naplni pole data nahodnymi hodnotami
plt.hist(data,bins=nbins,density=True) #udela a vykresli histogram

