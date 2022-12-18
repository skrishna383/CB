import random
import numpy as np
import matplotlib.pyplot as plt
x=np.array([[1,1],[2,2],[1,2]])
print(x)
y=['red']
plt.figure()
plt.scatter(x[:,0],x[:,1])
plt.show()

s=random.random()*1+1

k=random.random()*1+1
for i in range(10000):
  choose = random.random()
  if choose >0.66:
    s=s/2+1/2
    k=k/2+1/2
    
  elif choose >0.33:
    s=s/2+1/2
    k=k/2+2/2
  elif choose >0.00:
    s=s/2+2/2
    k=k/2+2/2
  n=np.array([s,k])
  x=np.append(x,[n],axis=0)
    
n=np.array([s,k])
x=np.append(x,[n],axis=0)
#print(x)
plt.scatter(x[:,0],x[:,1])
plt.show()