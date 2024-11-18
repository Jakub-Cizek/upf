import numpy as np
import matplotlib.pyplot as plt
plt.ion() #zapnuti interaktivniho rezimu 
n=100000
x=np.array(n) #deklarace pole x-souradnice
y=np.array(n) #deklarace pole y-souradnice
colours=np.array([n,3]) #deklarace pole barva
x=np.random.random_sample(n)#vygeneruje 100000 nah. cisel U(0,1)
y=np.random.random_sample(n) #vygeneruje 100000 nah. cisel U(0,1)
colours=np.random.random_sample([n,3]) #vygeneruje 100000 nah. cisel U(0,148)
plt.scatter(x,y, s=500000/n, c=colours, edgecolors="none") #nakresli graf
#nastaveni os od 0 do 1
ax=plt.gca()
ax.set_xlim(left=0,right=1)
ax.set_ylim(bottom=0,top=1)
plt.draw()
#ulozeni do souboru formatu PNG
plt.savefig("randomcolours.png",dpi=150)