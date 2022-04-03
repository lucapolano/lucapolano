import numpy as np
import os


rand = np.random.randint(30, size = (3,3))
row, element, centre = rand[0], rand[2][0], rand[1][1]
rand1 = np.randint(30, size =10) 
v1, v2, v3 = rand1[1:], rand1[4:9], rand1[:-2]
copia = rand1 #qui copi il puntatore all’area di memoria
copia1=rand1.copy() #qui creo una nuova area di memoria, che non mi porta ad avere problemi nel caso di modifiche di liste interne 
v1, v2 = np.array([1,2,3,4,5,6]), np.array([6,5,4,3,2,1])
sum = v1+v2
molt = v1*v2 