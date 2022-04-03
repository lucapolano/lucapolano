import numpy as np
import os 

os.chdir('/home/runner/lucapolano-7/lez_7_py')
x,y = np.loadtxt('ex2_data_python_4.txt', unpack=True)
n = len(x)
xg=0
yg=0
for i in (0,n-1):
  xg = xg + x[i]
  yg = yg + y[i]
xg = xg/n
yg = yg/n
print("(x,y) baricentro = ","(",xg,",",yg,")")