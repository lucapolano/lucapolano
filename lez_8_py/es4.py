import numpy as np
import os




os.chdir('/home/runner/lucapolano-7/py') 
mat = np.loadtxt('mat.txt', unpack=True)
aval, avec = np.linalg.eig(mat)
print(aval,avec)