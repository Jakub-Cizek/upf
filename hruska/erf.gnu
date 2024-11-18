pi=3.1415926535897932384626433832795
set xrange [-5:5]
set yrange [-2.0/sqrt(pi):2.0/sqrt(pi)]
set xlabel 'x'
set ylabel 'erf(x)'
plot erf(x) with lines