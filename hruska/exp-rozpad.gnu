tau=100.0

# hustota pravdepodobnosti
set term wxt 0
set xlabel 'x (um)'
set ylabel 'f(x)'
set xrange [0:4*tau]
set yrange [0:1/tau]
f(x)=1/tau*exp(-x/tau)
plot f(x) title 'f(x)' with lines linestyle 1

#distribucni funkce
set term wxt 1
set xlabel 'x (um)'
set ylabel 'F(x)'
set xrange [0:4*tau]
set yrange [0:1]
F(x)=1-exp(-x/tau)
plot F(x) title 'F(x)' with lines  linestyle 2