# -*- coding: utf-8 -*-
"""

@author: Ben
"""

import scipy.integrate as sci
import numpy as np
from matplotlib import pyplot as pl
from math import sqrt

a = 2   # amplitude 
N = 1000   # number of points
m = 1
x = np.linspace(0,a,N,endpoint=False)
f = lambda x:sqrt((8*m)/(a**4-x**4)) 
f_array = np.vectorize(f)
f_array = f_array(x)

t1 = sci.trapz(f_array,x)   #trapezoidal method

t2 = sci.simps(f_array,x)   #simpsons method

print ("t_trap , t_simp", t1,t2)

t = []
a = np.linspace(.01,4,1000)

for i in a:
    f = lambda x:sqrt((8*m)/(i**4-x**4))
    x = np.linspace(0,i,N,endpoint=False)
    f_array = np.vectorize(f)
    f_array = f_array(x)
    t.append(sci.trapz(f_array,x)) 
 

pl.plot(a,t)
pl.xlabel('Amplitude')
pl.ylabel('Period')