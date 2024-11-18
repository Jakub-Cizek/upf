import numpy as np
import matplotlib.pyplot as plt
import array

#plt.ion() #zapnuti interaktivniho rezimu pro nastavovani chovani grafu
plt.clf()   #smaze stary (napr. predchozi) obrazek

n=20000
x=np.array(n) #deklarace pole x-souradnic
y=np.array(n) #deklarace pole y-souradnic
colors=np.array([n,3]) #deklarace pole barev
x=np.random.random_sample(n) #vygeneruje n nahodnych cisel U(0,1)
y=np.random.random_sample(n) #vygeneruje n nahodnych cisel U(0,1)
colors=np.random.random_sample([n,3]) #vygeneruje n trojic nahodnych cisel U(0,1)

plt.scatter(x,y, s=10, c=colors, edgecolors="none") #nakresli graf

# hezci nastaveni vysledneho grafu
#ax=plt.gca()   # budeme menit nastaveni os
#ax.set_xlim(left=0,right=1)
#ax.set_ylim(bottom=0,top=1)
#plt.draw()   # znouv vykresli graf




#plt.savefig("colortest.png",dpi=150)   #ulozeni do souboru formatu PNG