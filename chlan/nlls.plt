f(x) = m * x + c
fit f(x) 'datafit.dat' using 1:2 via m,c
plot 'datafit.dat', f(x)