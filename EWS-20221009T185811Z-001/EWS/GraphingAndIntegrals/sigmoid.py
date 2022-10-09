# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:39:47 2021

@author: brady
"""

def sigmoid(values):
    import math as m
    
    return list(map(lambda k: 1/(1+m.e**(-k)), values))

def hyperbolic(values):
    import math as m 
    return (m.e**values-m.e**(-values))/(m.e**values+m.e**(-values))
def arctan(values):
    import numpy as np 
    return np.arctan(values)
def sqr(values):
    return values/((10+values**2)**(1/2))