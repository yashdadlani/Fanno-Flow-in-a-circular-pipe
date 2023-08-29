import numpy as np
import matplotlib.pyplot as plt
from math import *
n = 1000
M3 = np.linspace(0.6,1,n+1)
M2 = np.linspace(1,2,n+1)
# iterations = np.arange(0,41,1)
# print(iterations)
k = 1.4
a = k + 1
b = k-1
D = 0.04
f = 0.001

nd_chok_len2 = np.empty(n+1,float)
d_chok_len2 = np.empty(n+1,float)
d_chok_len1 = np.empty(n+1,float)
pred_pipe_len = np.empty(n+1,float)

# print('M2 \t\t M3(after shock) \t L1 ')
print('L1 \t\t\t L2 \t\t Total length ')
for i in range(0,n+1):
    M = M2[i]
    N = M**2
    M3[i] = sqrt((2+b*N)/(2*k*N - b))
    O = M3[i]
    Q = O**2
    d_chok_len1[i] = ((0.25/k) + (a/(2*k))*log(4/(4*k-2)) - ((1/(k*N)) + (a/(2*k))*log(N/(2+b*N))))*(D/(4*f))
    d_chok_len2[i] = (D/(4*f))*((1/(k*Q)) + (a/(2*k))*log(Q/(2+b*Q)) - (1/k) + (a/(2*k))*log(a))
    pred_pipe_len[i] = d_chok_len1[i] + d_chok_len2[i]
    
    # print('%f \t %f \t %f' %(d_chok_len1[i], d_chok_len2[i], pred_pipe_len[i]))

    # print('%f \t %f \t\t %f' %(M2[i],M3[i], d_chok_len1[i]))
for i in range(0,n):
   if abs(pred_pipe_len[i]-5) < 0.01:
       print(pred_pipe_len[i])
       print(M2[i])
       print(M3[i])
       print(d_chok_len1[i], d_chok_len2[i],pred_pipe_len[i])
       
       

       
       







    
    
    



    


    
   