import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression   #balicek SciKit-learn

#data = np.loadtxt("datafitbig.dat", dtype=float)   # Nacteni dat ze souboru data.dat
data = np.loadtxt("random.dat", dtype=float)   # Nacteni dat ze souboru data.dat
#data = np.loadtxt("datafit.dat", dtype=float)   # Nacteni dat ze souboru data.dat
x = np.vstack(data[:,0])        # prvni sloupec x-ova data
y = np.vstack(data[:,1])        # druhy sloupec y-ova data
err = np.vstack(data[:,2])      # treti sloupec y-ove nejistoty

xt = x.ravel()  # prevod na 1D array
yt = y.ravel()
errt = err.ravel()/10.0


# linearni regrese

# vyrobime matici A - doplneni sloupcem jednicek
A = np.append(x, np.vstack(np.ones(len(x))), axis=1)
# fitovani pomoci nejmensich ctvercu, [0] -> staci nam parametry  
m, c  = np.linalg.lstsq(A, y, rcond=None)[0]

#print( 'Smernice: m= ', m[0] )
#print( 'Prusecik: c= ', c[0] )

# nakresleni grafu
fig, ax = plt.subplots()
ax.errorbar(xt, yt,xerr=None,yerr=errt,fmt='o',markersize=7)   # bodovy graf xy s y-ovymi chybovymi useckami 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('linearni regrese')
ax.plot(x, m*x + c, 'r')    # graf fitovane funkce 
ax.legend(loc='upper left',labels=['fit y = %.3fx + %.3f' %(m, c), 'data ze souboru bigerrorbars.dat'])
plt.show()

print('Linearni regrese: y = %.3fx + %.3f \n' %(m, c))

# alternativa ve scipy


slope, intercept, r_value, p_value, std_err = stats.linregress(xt,yt)
print('Linearni regrese #2: y = %.3fx + %.3f' %(slope, intercept))
#meanxt = xt.mean()
#xres = (xt-meanxt)**2
#sumxr = np.sqrt(xres.sum())
#err_slope = std_err / sumxr
#print('slope = %.6f +- %.6f \n' %(slope,  err_slope))


#### nelinearni regrese
#fitovani pomoci scipy.optimize.curve_fit

def line(r,a,b):
    return a * r + b

parameters, covmatrix = curve_fit(line,xt,yt,sigma=errt,absolute_sigma=True)
# zde rikame, ze 'err' jsou standardni odchylky 'y' a maji se zohlednit
# pri vypoctu do kovariacni matice

fig2, ax2 = plt.subplots()
ax2.errorbar(xt, yt,xerr=None,yerr=errt,fmt='o',markersize=7)   # bodovy graf xy s y-ovymi chybovymi useckami 
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('nelinearni regrese')
ax2.plot(xt, line(xt, *parameters), 'r')    # graf fitovane funkce 
ax2.legend(loc='upper left',labels=['fit y = %.3fx + %.3f' % ( parameters[0], parameters[1] ) , 'data ze souboru bigerrorbars.dat'])

plt.show()

parerr = np.sqrt(np.diag(covmatrix))  # odmocnina z prvku na diagonale
print('Nelinearni regrese: \n %.6f +- %.6f \n %.6f +- %.6f \n' %(parameters[0], parerr[0], parameters[1], parerr[1]))





# MC sampling

runs = 1000
mcy = np.zeros(shape=(runs,len(yt)))
a = np.zeros(runs)
b = np.zeros(runs)


for i in range(runs):
     mcy[i] = np.random.normal(yt,errt,len(yt))
   #  mcy[i] = np.random.uniform(yt-errt,yt+errt,len(yt))
     a[i], b[i], _, _, _ = stats.linregress(xt,mcy[i])

plt.subplots(figsize=(24,10))
plt.clf()

plt.subplot(1, 2, 1)
plt.xlim(np.amin(a),np.amax(a))
plt.hist(a[:], bins=25)
plt.xlabel('a')
plt.ylabel('counts')     
plt.pause(0.3)
      
plt.subplot(1, 2, 2)
plt.xlim(np.amin(b),np.amax(b))
plt.hist(b[:], bins=25)
plt.xlabel('b')
plt.ylabel('counts')     
plt.pause(0.3)
plt.show()
plt.close

print('MC simulace (n= %d): \n %.6f +- %.6f \n %.6f +- %.6f \n' %(runs, np.mean(a), np.std(a), np.mean(b), np.std(b)))

fig3, ax3 = plt.subplots()
ax3.errorbar(xt, yt,xerr=None,yerr=errt,fmt='o',markersize=7)   # bodovy graf xy s y-ovymi chybovymi useckami 
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_title('MC simulace')
for i in range(runs):
    ax3.scatter(xt, mcy[i], s=30, marker='x', color='g')
    ax3.plot(xt, a[i]*xt + b[i], 'r', linewidth=0.2)    # graf fitovane funkce 
plt.pause(0.3)
fig3.show()
#ax3.legend(loc='upper left',labels=['fit y = %.3fx + %.3f' % ( parameters[0], parameters[1] ) , 'data ze souboru bigerrorbars.dat'])

plt.show()
