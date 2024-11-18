from scipy.special import erfinv
from numpy import sqrt
sigma=(80-100)/(sqrt(2)*erfinv(-0.80))
genius=100+sqrt(2)*sigma*erfinv(2*0.9995-1)
print('sigma=',sigma)
print('IQ =',genius)

