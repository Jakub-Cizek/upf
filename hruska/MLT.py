import numpy as np
import matplotlib.pyplot as plt
N=10000
m_max=10
nbins=100
eps=1.0e-4
for i in range(1,m_max):
    x=np.zeros(N)+1
    for k in range(0,i): x=x*np.exp(np.random.random_sample(N))
    mu=i/2.0
    sigma=i/12.0
    xt=np.linspace(eps,np.max(x),1000)
    yt=1.0/(np.sqrt(2*np.pi)*sigma)*1.0/xt*np.exp(-((np.log(xt)-mu)**2/(2.0*sigma**2)))
    fig,ax=plt.subplots()
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    label="N="+str(i)
    ax.set_title(label)
    ax.hist(x,bins=nbins,density=True)
    ax.plot(xt,yt,c="red")    