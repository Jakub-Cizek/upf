import numpy as np
import matplotlib.pyplot as plt
N=10000 #pocet simulovanych dat
nbin=50 #pocet binu histogramu
mu=0   #ocekavana hodnota normalniho rozdeleni 
sigma=1 #standardni odchylka normalniho rozdeleni
x=np.empty(N) #nahodna promenna x z N(mu,sigma)
y=np.empty(N) #nahodna promenna y = exp(x)
x=np.random.normal(mu,sigma,N) #vygenerovani N nah. cisel z N(mu,sigma)
y=np.exp(x) #vypocet nove nahodne promenne y = exp(x)

xg=np.linspace(mu-4*sigma,mu+4*sigma,1000) #x-ova osa pro gaussian
eps=1e-4             #nezacnem presne v nule abychom se u fln vyhnuli deleni 0   
xln=np.linspace(eps,np.exp(mu+2*sigma),1000) #x-ova osa pro log-norm rozdeleni
fg=1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(xg-mu)**2/(2*sigma**2)) #gaussian
fln=1/(np.sqrt(2*np.pi))*1/xln*np.exp(-(np.log(xln)-mu)**2/(2*sigma**2)) #log-norm rozdeleni

fig,ax=plt.subplots()  #vykresleni norm. histogramu nahodne promenne x a gaussianu
ax.set_title("normalni rozdělení")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.hist(x,bins=nbin,density=True)
ax.plot(xg,fg,c="red")

fig,ax=plt.subplots() #vykresleni norm. histogramu nahodne promenne y a hustoty pst log-norm rozdeleni
ax.set_title("log-normalni rozdělení")
ax.set_xlabel("y")
ax.set_ylabel("f(y)")
ax.hist(y,bins=nbin,range=(0,np.exp(mu+2*sigma)),density=True)
ax.plot(xln,fln,c="red")
