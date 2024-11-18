x0=1.0

# hustota pravdepodobnosti
set term wxt 0
set xlabel 'x (cm)'
set ylabel 'f(x)'
set xrange [-x0:x0]
set yrange [0:2]
f(x)=1/pi*1/sqrt(x0**2-x**2)
plot f(x) title 'f(x)' with lines linestyle 1