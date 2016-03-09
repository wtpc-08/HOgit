#3) Graficar un el siguiente polinomio, su derivada y puntos extremos.

#f(x) =x3+x2-4x+4
import numpy as np
import scipy
import matplotlib.pyplot as pp
from pylab import *

x=frange(-10,10,0.1)

from scipy.misc import derivative
def f(x):
    return x**3 + x**2-4*x+4

Y_prima = derivative(f, x, dx=1e-6)

Y = f(x)

pp.figure()
pp.plot(x, Y,color='r')
pp.plot(x,Y_prima,color='b')
title('Ejemplo 3')
pp.ylabel('Y Yderiv')
pp.grid(True)
pp.xlabel('X')
pp.show()
vec=np.c_[x,Y]
f_out_max = open('tabla.txt', 'w')
np.savetxt(f_out_max,vec,fmt='%f',delimiter='\t',header="x #f(x)") 
f_out_max.close()








#a) Colocar titulo a los ejes y agregarle una grilla en ambos. Definir #el rango de la funcion entre -10 y 10.

#b) Colocar titulo y colores distintos para la funcion y la derivada.

#c) Guardar los resultados de evaluar la funcion en el rango del punto #a cada 0.1 unidades en un txt.
