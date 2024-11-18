set term wxt 0
tau=100.0
# hustota prandepodobnosti
set xlabel 'x'
set ylabel 'f(x)'
set xrange [0:4*tau]
set yrange [0:1/tau]
pdf(x)=1/tau*exp(-x/tau)
plot pdf(x) title 'f(x)' with lines linestyle 1

set term wxt 1
set xlabel 'x'
set ylabel 'F(x)'
set xrange [0:4*tau]
set yrange [0:1]
#distribucni funkce
F(x)=1-exp(-x/tau)
plot F(x) title 'F(x)' with lines  linestyle 2