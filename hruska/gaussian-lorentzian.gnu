set term wxt 0
pi=3.1415926535897932384626433832795
mu=0    #poloha maxima
w=1     #FWHM
sigma=w/(2*sqrt(2*log(2)))
set xlabel 'x'
set ylabel 'hustota prevdepodobnosti'
set xrange [-5*sigma:5*sigma]
set yrange [0:1/(sqrt(2*pi)*sigma)]
# gaussian
g(x)=1/(sqrt(2*pi)*sigma)*exp(-(x-mu)**2/(2*sigma**2))
#lorentzian
l(x)=1/pi*w/2/(w**2/4.0+(x-mu)**2)
plot g(x) title 'Gaussian' with lines linestyle 1,l(x) title 'Lorentzian' with lines linestyle 2

set term wxt 1
set xlabel 'x'
set ylabel 'pravdepodobnost'
set xrange [-5*sigma:5*sigma]
set yrange [0:1]
#distribucni funkce normalni rozdeleni
G(x)=0.5*(1+erf((x-mu)/(sigma*sqrt(2))))
#distribucni funkce Breit-Wignerovo rozdeleni
L(x)=1/pi*(atan(2*x/w)+pi/2)
plot G(x) title 'G(x)' with lines linestyle 1, L(x) title 'L(x)' with lines linestyle 2

print sprintf('Normal distribution P(|x|>2)=%.10f',2*(1-G(2)))
print sprintf('Breit-Wigner distribution P(|x|>2)=%.10f',2*(1-L(2)))