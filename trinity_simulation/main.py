# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:52:29 2020

@author: Erik Lie
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.getcwd())

import trinity
from brownian import *

s0 = [100,100,100]
mu = [0.1,0.1,0.1]
sig = [0.2,0.2,0.2]
cv = [[0.01,0.005,0.005],[0.005,0.04,0.02],[0.005,0.02,0.16]]
step = 252

Generator = Brownian(s0, mu, sig, cv, step)
s = Generator.generate()

# For plot graph only

x = np.linspace(0,step,step)
plt.figure(num = len(s0), figsize=(8, 5))
for i in range(len(s0)):
    plt.plot(x, s[i].flatten())
plt.show()