import numpy as np
import os
from random import randint
import time

N=1000 # matrici NxN
start = time.time()
m1,m2 = np.zeros((N,N)), np.zeros((N,N))
for i in range (1,N):
    for j in range (1,N): 
      m1[i,j] = randint(1,200)
      m2[i,j] = randint(1,200)

end = time.time()
print('for_time', end-start)

start1=time.time()
m1 = np.random.randint(200, size=(N,N))
m2 = np.random.randint(200, size=(N,N))
end1=time.time()
print('np_time', end1-start1)

