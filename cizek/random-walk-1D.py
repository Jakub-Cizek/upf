import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
Nsim=1000 #pocet nahodnych prochazek, ktere budeme simulovat
N=100 #počet kroku budu postupne zvysovat od 0 do N
p=0.5 #pravdepodobnost ze pujdu vpravo
k_data=np.array(Nsim,dtype=int) #pocet kroku vpravo, binom. rozdeleni 
x_N=np.linspace(0,N,N) #x osa pro vykresleni sqrt(N)
f=np.sqrt(x_N) #odmocninova zavislost
x_N_odd=np.arange(0,N+2,2,dtype=int) #pole sudych cisel N
P_teor=factorial(x_N_odd)/(factorial(x_N_odd/2))**2*(1/2)**x_N_odd # teoreticka P ze se vratim do nuly
distance=np.array(Nsim) #vzdalenosti od pocatku
distance_mean=np.empty(N) #prumerna vzdalenost
P_zero=np.empty(N) #P ze se vratim do nuly

for i in range(0,N): #sumulujeme pocet kroku od 0 do N 
    distance_zero_count=0 #pocet pripadu kdy jsem se vratil do nuly
    k_data=np.random.binomial(i,p,Nsim) #vygenerujeme Nsim hodnot z binom rozdeleni
    distance=(k_data - (i-k_data))**2 #vzdalenost od pocatku
    for k in range(0,Nsim):
        if distance[k]==0: distance_zero_count=distance_zero_count+1 #pocitam pripady kdy jsem skoncil v pocatku
    distance_mean[i]=np.sqrt(np.mean(distance)) #prumerna hodnota vzdalenosti od pocatku
    P_zero[i]=distance_zero_count/Nsim #P ze se vratim do pocatku
    
fig,ax=plt.subplots()   #graf zavislosti vzdalenosti od pocatku na N
ax.set_xlabel("N")
ax.set_ylabel("vzdálenost od počátku")
ax.step(x_N,distance_mean)    
ax.plot(x_N,f,c="red")

fig,ax=plt.subplots() #graf zavislosti P ze se vratim do pocatku na N
ax.set_xlabel("N")
ax.set_ylabel("Pravděpodobnost návratu do počátku")
ax.step(x_N,P_zero)    
ax.plot(x_N_odd,P_teor,c="red")


