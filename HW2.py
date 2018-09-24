# -*- coding: utf-8 -*-
"""
For some reason my E field plots aren't working. I commented them out for now and will
sumbit a revision once I figure out what's going on :( I also had trouble with the trapz function 
for the 2d case, so I used Romberg instead
@author: Ben
"""
from mpl_toolkits.mplot3d.axes3d import Axes3D
import scipy.integrate as sci
import numpy as np
from math import pi,cos,sin,sqrt
from matplotlib import pyplot as pl

f = lambda x,x_p: 2*x_p/(x-x_p)
x_p = np.linspace(0,1,100)
f_array = np.vectorize(f)
x = np.linspace(1.1,5,100)

V = []

for i in x:
    farray = f_array(i,x_p)
    V.append(sci.trapz(x_p,farray))

E = -np.diff(V)/np.diff(x)
   
pl.figure(1)
pl.plot(x,V,'m-')
pl.xlabel('x')
pl.ylabel('V(x)')

pl.figure(2)
pl.plot(x[0:99],E,'c-')
pl.xlabel('x')
pl.ylabel('E(x)')

x = np.linspace(1,5,80)
y = np.linspace(2,6,80)
V1 = np.zeros((len(x),len(y)))
V2 = np.zeros((len(x),len(y)))
V = np.zeros((len(x),len(y)))

for i in range(0,len(x)) :
    for j in range(0,len(y)) :
        f1 = lambda x_p: x_p**2/sqrt((x[i]-x_p)**2+(y[j])**2)
        f2 = lambda y_p: y_p/sqrt(x[i]**2+(y[j]-y_p)**2)
        V1[i,j] = sci.romberg(f1,0,1)
        V2[i,j] = sci.romberg(f2,1,2)
        V[i,j] = V1[i,j] + V2[i,j]
    
Ex = -np.diff(V,axis=0)/0.05
Ey = -np.diff(V,axis=1)/0.05 

fig = pl.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
X,Y = np.meshgrid(x,y)
ax.plot_surface(X, Y, V, shade=True, color='m')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V(x,y)')
"""
fig = pl.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
X,Y = np.meshgrid(x[0:79],y[0:79])
ax.plot_surface(X, Y, Ex, shade=True, color='r')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Ex(x,y)')

fig = pl.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
X,Y = np.meshgrid(x[0:79],y[0:79])
ax.plot_surface(X, Y, Ey, shade=True, color='y')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Ey(x,y)')
"""
x = np.linspace(-4,4,160)
y = np.linspace(-4,4,160)
z = 1
V = np.zeros((len(x),len(y)))
for i in range(0,len(x)):
    for j in range (0,len(y)):
        f = lambda r,theta : cos(theta)*r**2/sqrt((x[i]-r*cos(theta))**2 + (y[j]-r*sin(theta))**2 + z**2 )
        integral = sci.nquad(f,[[0,2],[0,2*pi]])
        V[i,j] = integral[0]    

Ex = -np.diff(V,axis=0)/0.05
Ey = -np.diff(V,axis=1)/0.05

fig = pl.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
X,Y = np.meshgrid(x,y)
ax.plot_surface(X, Y, V, shade=True, color='m')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V(x,y)')
"""
fig = pl.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
X,Y = np.meshgrid(x[0:159],y[0:159])
ax.plot_surface(X, Y, Ex, shade=True, color='r')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Ex(x,y)')

fig = pl.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
X,Y = np.meshgrid(x[0:159],y[0:159])
ax.plot_surface(X, Y, Ey, shade=True, color='y')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Ey(x,y)')
"""