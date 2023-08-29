import numpy as np
import matplotlib.pyplot as plt
from math import *
M2 = np.linspace(2,1.816,185)
M4 = np.linspace(0.61296,1,388)
M3 = 0.61296
P = M3**2
D = 0.04
f = 0.001
k = 1.4
a = k+1
b = k-1
L1 = np.empty(185,float)
L1[0] = 0
for i in range(1,185):
    M = M2[i]
    L1[i] = (D/(4*f))*((0.25/k) + (2.4/2.8)*log(4/(4*k-2)) -(1/(k*M**2)) - (2.4/2.8)*log ((M**2)/ (2+ 0.4*(M**2) ) ) )
L2 = np.empty(388,float)
L2[0] = L1[184]
for i in range(1,388):
    N = (M4[i])**2
    L2[i] = (D/(4*f)) * ((1/(k*P))  + (a/(2*k))*log(P/(2+0.4*P)) -  (1/(k*N))  - (2.4/2.8)*log(N/(2+0.4*N) )) + L2[0]
L_final = np.empty(573,float)
M_final = np.empty(573,float)
for i in range(0,573):
    if 0<= i <=184:
        L_final[i] = L1[i]
    if 185<= i < 573:
        L_final[i] = L2[i-185]
for i in range(0,573):
    if 0<= i <=184:
        M_final[i] = M2[i]
    if 185<= i < 573:
        M_final[i] = M4[i-185]


# plt.plot(L_final,M_final)
# plt.xlabel("Length")
# plt.ylabel(' Mach No.')
# plt.title("Mach Number vs Length ")
# plt.grid()
# plt.show()
P1 = 100
Pressure2 = np.empty(185,float)
Pressure4 = np.empty(388,float)
Pressure2[0] = P1
M1 = 2
for i in range(1,185):
    Pressure2[i] = P1*(M1/M2[i])*(sqrt(3.6/(2 + 0.4* ((M2[i])**2))))
P3 = 422.154
Pressure4[0] = P3
M3 = 0.61296
for i in range(1,388):
    Pressure4[i] = P3*(M3/M4[i])*(sqrt(1.498/(2 + 0.4* ((M4[i])**2))))
Pressure_final = np.empty(573,float)
for i in range(0,573):
    if 0<= i <=184:
        Pressure_final[i] = Pressure2[i]
    if 185<= i < 573:
        Pressure_final[i] = Pressure4[i-185]
# plt.plot(L_final,Pressure_final)
# plt.xlabel("Length")
# plt.ylabel(' Static Pressure')
# plt.title("Static Pressure vs Length ")
# plt.grid()
# plt.show()
T1 = 300 
T2 = np.empty(185,float)
T2[0] = T1
for i in range(1,185):
    T2[i] = T1* ((2+b*(M1**2))/(2 + b*((M2[i])**2)))
# print(T2)
T4 = np.empty(388,float)
T4[0] = 502.258
T3 = T4[0]
for i in range(1,388):
    T4[i] = T3* ((2+b*(M3**2))/(2 + b*((M4[i])**2)))
T_final = np.empty(573,float)
for i in range(0,573):
    if 0<= i <=184:
        T_final[i] = T2[i]
    if 185<= i < 573:
        T_final[i] = T4[i-185]
plt.plot(L_final,T_final)
plt.xlabel("Length")
plt.ylabel(' Temp. ')
plt.title("Temp  vs Length ")
plt.grid()
plt.show()
den2 = np.empty(185,float)
den1= den2[0] = 1.157
for i in range(1,185):
    den2[i] = (den1 * T1 * Pressure2[i]) / (P1*T2[i])
den3 = 2.918
den4 = np.empty(388,float)
den4[0] = den3
for i in range(1,388):
    den4[i] = (den3 * T3 * Pressure4[i]) / (P3*T4[i])
den_final = np.empty(573,float)
for i in range(0,573):
    if 0<= i <=184:
        den_final[i] = den2[i]
    if 185<= i < 573:
        den_final[i] = den4[i-185]
plt.plot(L_final,den_final)
plt.xlabel("Length")
plt.ylabel(' Density ')
plt.title("Density  vs Length ")
plt.grid()
plt.show()
velocity1 = np.empty(185,float)
velocity1[0] = 696
for i in range(1,185):
    velocity1[i] =  696 * ( den1 / den2[i] )
velocity2 = np.empty(388,float)
velocity2[0] = 275.839
for i in range(1,388):
    velocity2[i] =  275.839 * ( den3 / den4[i] )
vel_final = np.empty(573,float)
for i in range(0,573):
    if 0<= i <=184:
        vel_final[i] = velocity1[i]
    if 185<= i < 573:
        vel_final[i] = velocity2[i-185]
# plt.plot(L_final,vel_final)
# plt.xlabel("Length")
# plt.ylabel(' Velocity ')
# plt.title("Velocity vs length ")
# plt.grid()
# plt.show()








