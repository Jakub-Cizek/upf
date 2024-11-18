import numpy as np

R=[1.33,1.35,1.3,1.32,1.33]


N_data=np.size(R)
print('pocet dat: {0:d}'.format(N_data))
mean_R=np.mean(R)
print('odhad R: {0:5.3f}'.format(mean_R))
sigma=np.std(R,ddof=1)
print('chyba jednoho mereni: {0:5.3f}'.format(sigma))
sigma_R=sigma/np.sqrt(N_data)
print('chyba odhadu R: {0:5.3f}'.format(sigma_R))
print('elektricky odpor R = ({0:5.3f} +/- {1:5.3f}) Ohm'.format(mean_R,sigma_R))

l=1.545 #delka dratu (m)
sigma_l=0.001 #nejistota delky dratu
d = 0.45e-3 #prumer dratu (m)
sigma_d=0.01e-3  #nejistota prumeru dratu
rho=mean_R*np.pi*d**2/(4*l)
sigma_rho=rho*np.sqrt((sigma_R/mean_R)**2+(sigma_l/l)**2+4*(sigma_d/d)**2)
print('merny elektricky odpor rho = ({0:5.3e} +/- {1:5.3e}) Ohm'.format(rho,sigma_rho))
