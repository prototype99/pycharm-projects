#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:01:10 2021
hill muscle model
@author: seirra
"""

import numpy as np
import matplotlib.pyplot as plt

Length, a, b = 1200, 380 * 0.098, 0.325
P0 = a / 0.257
vm = P0 * b / a
alpha = P0 / 0.1
LSE0 = 0.3
k = a / 25
t = [0 + 0.01 * i for i in range(1201)]
A = [1.001 + 0.001 * i for i in range(100)]
B = [1.099 - 0.001 * i for i in range(100)]
C = np.ones(100).tolist()
D = [0.999 - 0.001 * i for i in range(100)]
E = [0.901 + 0.001 * i for i in range(100)]
F = np.ones(100).tolist()
G = [1.001 + 0.001 * i for i in range(100)]
H = [1.099 - 0.001 * i for i in range(100)]
HH = np.ones(100).tolist()
J = [0.999 - 0.001 * i for i in range(100)]
K = [0.901 + 0.001 * i for i in range(100)]
KK = np.ones(101).tolist()
L = A + B + C + D + E + F + G + H + HH + J + K + KK
LSE = np.zeros(1200).tolist()
LCE = np.zeros(1200).tolist()
P = np.zeros(1201).tolist()
for i in range(1200):
    LSE[i] = 0.3 * P[i] / alpha
    LCE[i] = L[i] - LSE[i]
    dt = t[i + 1] - t[i]
    dL = L[i + 1] - L[i]
    dP = alpha * ((dL / dt) + b * ((P0 - P[i]) / (a + P[i]))) * dt
    P[i + 1] = P[i] + dP
P = np.array(P)
PP = (P0 / 100)  # * np.random.randn(1201) #adds noise
P = P + PP
P = P.tolist()
plt.figure()
plt.plot(L, P)
plt.xlabel('fraction of muscle length, mm', fontsize=15)
plt.ylabel('force ($mN / mm^2$)', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
