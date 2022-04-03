import numpy as np
import os
import matplotlib.pyplot as plt
def istogramma_ast():
  os.chdir('/home/runner/lucapolano-7/py')
  a = np.loadtxt('data.dat', dtype=int)
  n=a.size
  for i in range(0,n):
    k = a[i]
    print("*"*k)

istogramma_ast()

def isto_graf():
  os.chdir('/home/runner/lucapolano-7/py')
  a = np.loadtxt('data.dat', dtype=int)
  plt.hist(a,bins=7)
  plt.xlabel('naturali')
  plt.ylabel('conteggi')
  plt.legend()
  plt.show()
isto_graf()