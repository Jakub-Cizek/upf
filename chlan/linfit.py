import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("datafit.dat", dtype=float)   # Nacteni dat ze souboru data.dat
x = np.vstack(data[:,0])        # prvni sloupec x-ova data
y = np.vstack(data[:,1])        # druhy sloupec y-ova data
err = np.vstack(data[:,2])      # treti sloupec y-ove nejistoty

# vyrobime matici A - doplneni sloupcem jednicek
A = np.append(x, np.vstack(np.ones(len(x))), axis=1)

# fitovani pomoci nejmensich ctvercu, [0] -> staci nam parametry  
m, c  = np.linalg.lstsq(A, y)[0]

print 'Smernice: m= ', m[0]
print 'Prusecik: c= ', c[0]

# nakresleni grafu
fig, ax = plt.subplots()
ax.errorbar(x, y,xerr=None,yerr=err,fmt='o',markersize=7)   # bodovy graf xy s y-ovymi chybovymi useckami 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('fit obecnou primkou')
ax.plot(x, m*x + c, 'r')    # graf fitovane funkce 
ax.legend(loc='upper left',labels=['data ze souboru data.dat','fit y = %.3fx + %.3f' %(m, c)])

plt.show()
