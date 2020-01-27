# -*- coding: utf-8 -*-
"""
@Time ： 2020/1/1 17:12
@Auth ： dave

"""
import matplotlib.pyplot as plt
import numpy as np
from Fitting.tools import *

#y = sin(2pi*x)
x,y = creat_data('sin',1000,False)
#print(x.shape,y.shape)
#input()



plt.scatter(x,y,s=5,label='training data')
plt.xlabel('x',size=20)
plt.ylabel('y',size=20)
plt.legend()
plt.show()
