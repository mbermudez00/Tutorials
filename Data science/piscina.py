import numpy as np

def load_txt():
    data = np.loadtxt("data.txt")
    print(data)
    print("")
    return data

data = load_txt()
yo =  data[0:, 0:3]
vecino = data[0:, 3:]

result_yo = ((((yo[:3,0]/yo[:3,1])*yo[:3,2])+yo[:3,0])/yo[:3,1])
result_vec = ((((vecino[:3,0]/vecino[:3,1])*vecino[:3,2])+vecino[:3,0])/vecino[:3,1])

a=0
for i in result_yo:
    print(i)
    print(result_vec[a])
    a+=1
    print("")

#print(result_yo)
#print(result_vec)