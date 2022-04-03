import numpy as np
import os
import matplotlib.pyplot as plt



os.chdir('/home/runner/lucapolano-7/py')
years, T_mu, T_m, T_M, rain = np.loadtxt('ex2_data_python_5.txt',unpack=True)

def var_mano(vec):
  mean = 0
  n=len(vec)
  for i in range(n):
    var = 0
    mean = mean +vec[i]
    mean = mean/n
  for i in range(n): 
    var = var + (vec[i]-mean)**2
    var =var/n
    return var, var**(0.5)
print(var_mano(T_m), var_mano(T_M))


def stat(years, T_mu, T_m, T_M, rain): 
  var_tmin, var_tmax  = np.var(T_m), np.var(T_M)
  dev_tmin, dev_tmax = np.sqrt(var_tmin), np.sqrt(var_tmax)
  plt.figure(2)
  plt.xlabel('years')
  plt.plot(years, T_m, color = 'blue', label = 'temperatura min')
  plt.plot(years, T_M, color = 'orange', label = 'temperatura max')
  plt.legend()
  plt.show()
  return var_tmin, dev_tmin, var_tmax, dev_tmax
print(stat(years, T_mu, T_m, T_M, rain))