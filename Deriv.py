# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:01:06 2018

@author: Ben
"""

import numpy as np
from matplotlib import pyplot as pl
from math import sin
from myder import thirdorderdiff
from myder import seconddiff
from array import array

N = 100
a = 0.01
b = 1.99
x = np.linspace(a,b,num = N)
y = []

f = lambda x: sin(1/(x*(2-x)))**2

for i in x:
    y.append(f(i))
 
yp = thirdorderdiff(f,a,b,N)

ypp=seconddiff(f,a,b,N) 

pl.plot(x,y,'#a2d2e2')
pl.plot(x,yp,'#ffa587')
pl.plot(x,ypp,'#78ccd2')