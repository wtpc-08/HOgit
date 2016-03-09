import numpy as np
import scipy
import matplotlib.pyplot as pp
from pylab import *

X=np.array([ 7.5, 4.48, 8.60, 7.73, 5.28, 4.25, 6.99, 6.31, 9.15, 5.06],float32)

Y=np.array([ 28.66, 20.37, 22.33, 26.35, 22.29, 21.74, 23.11, 23.13, 24.68, 21.89],float32)

pp.figure()
pp.scatter(X, Y)
title('X VS Y')
pp.ylabel('Y')
pp.grid(True)
pp.xlabel('X')
pp.show()

from scipy.optimize import curve_fit
p=np.polyfit(X, Y, 1)

def fitFunc(t, a, b):
    return a*t + b

t = np.linspace(4,10,100)
temp = fitFunc(t, p[0],p[1])

pp.figure()
pp.scatter(X, Y)
pp.plot(t,temp,color='b')
title('X VS Y')
pp.ylabel('Y')
pp.grid(True)
pp.xlabel('X')
pp.show()


