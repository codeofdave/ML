# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/1 17:10
@Auth ： dave

"""
import matplotlib.pyplot as plt
import numpy as np

def creat_data(type='sin',size=10,rand=True):
    np.random.seed(1)
    x = np.linspace(0, 1, size).reshape(size, 1)
    if type=='sin':
        #return x, -1*np.log(1-x) + (np.random.normal(scale=0.1, size=x.shape) if rand else 0)
        return x,np.sin(2*np.pi*x)+ (np.random.normal(scale=0.1,size=x.shape) if rand else 0)
    if type=='cos':
        return x, np.cos(2 * np.pi * x) + (np.random.normal(scale=0.1, size=x.shape) if rand else 0)




