import numpy as np

def sig_func(x):
   f = 1/(1+np.exp(-x))
   return f
print(sig_func(0.458))