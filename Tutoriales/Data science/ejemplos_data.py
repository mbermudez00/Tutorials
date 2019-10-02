# Importar el paquete numpy como np
import numpy as np

a = np.loadtxt("data.txt", dtype=int)
yo = a[:,0:3]
vecino = a[:,3:]


result_yo = np.ceil((((yo[:3,0]/yo[:3,1])*yo[:3,2])+yo[:3,0])/yo[:3,1])
result_vec = np.ceil((((vecino[:3,0]/vecino[:3,1])*vecino[:3,2])+vecino[:3,0])/vecino[:3,1])

print(result_yo < result_vec)
print(result_yo > result_vec)
"""
for i in range(len(result_yo)):
    if result_yo[i] < result_vec[i]:
        print("YO " + str(int(result_yo[i])))
    elif result_yo[i] > result_vec[i]:
        print("VECINO " + str(int(result_vec[i])))
    else:
        print("EMPATE " + str(int(result_yo[i])))
"""