import numpy as np

data=[1.371,1.457,1.430,1.389,1.321,1.415,1.394,1.387,1.394,1.404]
N=np.size(data)
print('pocet dat: {0:d}'.format(N))
mean=np.mean(data)
print('odhad ocekavane hodnoty: {0:5.3f} mA'.format(mean))
sigma=np.std(data,ddof=1) #ddof=1 zaruci deleni faktorem N-1
print('odhad statisticke chyby jednoho mereni: {0:5.3f} mA'.format(sigma))
sigma_mean=sigma/np.sqrt(N)
print('odhad statisticke chyby aritmetickeho prumeru: {0:5.3f} mA'.format(sigma_mean))
sigmaB=(mean*0.005+2*0.001)/np.sqrt(3)
print('odhad systematicke chyby aritmetickeho prumeru: {0:5.3f} mA'.format(sigmaB))
err=np.sqrt(sigma_mean**2+sigmaB**2)
print('odhad celkove chyby aritmetickeho prumeru: {0:5.3f} mA'.format(err))
print('vysledek I = ({0:4.2f} +/- {1:4.2f}) mA'.format(mean,err))

