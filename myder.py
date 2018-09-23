# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:50:22 2018

@author: Tom K
"""
import numpy as np

def forwardiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(1,N):
        slop = (f(a+k*h)-f(a+(k-1)*h))/h
        g.append(slop)
    return array(g)
    
def backwardiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N-1):
        slop = (f(a+(k+1)*h)-f(a+k*h))/h
        g.append(slop)
    return array(g)

def centraldiff(f,a,b,N):
    h = (b-a)/N
    g = np.zeros(N)
    for k in range(0,N):
        slop = (f(a+(k+1/2)*h)-f(a+(k-1/2)*h))/h
        g[k] = slop
    return g

def seconddiff(f,a,b,N):
    h = (b-a)/N
    l=np.zeros(N)
    for k in range(0,N):
        slop = (f(a+(k+1)*h)-2*f(a+k*h)+f(a+(k-1)*h))/h**2
        l[k] = slop
    return l

def thirdorderdiff(f,a,b,N):                # Modification (3rd order method) 
    h = (b-a)/N
    g=[]
    for k in range(0,N):
        slop = ((1/24)*f(a+(k-1.5)*h) - (27/24)*f(a+(k-0.5)*h)      \
               + (27/24)*f(a+(k+0.5)*h) - (1/24)*f(a+(k+1.5)*h))/h
        g.append(slop)
    return g
