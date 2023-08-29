import numpy as np
import matplotlib.pyplot as plt
from math import *
M1 = np.linspace(1,2,101)
L1 = np.empty(101,float)
D = 0.04
f = 0.001
p = D/(4*f)
k = 1.4
a = k+1
b = k-1
print("Mach No \t  Choke Length")
for i in range(0,101):
    M = M1[i]
    N = M**2
    def f(M):
        return p*(1/(k*N)+((a/(2*k))*log(N/(2+N*b))))
    L1[i] = f(M)
    print('%f \t %f' %(M1[i],L1[i]))




