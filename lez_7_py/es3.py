import numpy as np
import os

class Points():
    def __init__(self):
      os.chdir('/home/runner/lucapolano-7/lez_7_py')
      self.x, self.y = np.loadtxt('ex2_data_python_4.txt', unpack=True)
    def bar(self):
      n = len(self.x)
      if n == 0:
        exit 
      xg = np.mean(self.x)
      yg = np.mean(self.y)
      return xg,yg
        
pp = Points()
print(pp.bar())
        
      
