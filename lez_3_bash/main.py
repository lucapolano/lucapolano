string= 'Hello world'
print(lambda string: print(string))
coordinate=['x','y','z']
value=[3,4,5]
result = zip(coordinate,value)
result_list=list(result)
print(result_list)
c,v = zip(*result_list)
print('c=', c)
print('v=',v)
a = ("mario", "luca", "io")
b = ("marta", "marco", "giovanna")
x=zip(a,b)
print(tuple(x))
class Person: 
  def __init__(self,name,age): 
    self.name=name
    self.age=age
p1=Person("Luca", 23)
print(p1.name)
print(p1.age)
infile='mydata.dat'
outfile='myout.dat'
import math
def f(y):
  if y>= 0.0:
    return y**5*math.exp(-y)
  else:
    return 0.0


indata = open(infile, 'r') 
linee=indata.readlines()
indata.close()
processati=[]
x=[]
print(linee)
for el in linee:
  valori=el.split()
  x.append(float(valori[0])); y =float(valori[1])
  processati.append(f(y))
outdata= open(outfile,'w')
i=0
for el in processati:
  outdata.write('%g%12.5e\n' %(x[i],el))
  i += 1
outdata.close() 
file = open(outfile, 'r')
filecontent=file.read()
print("File content")
print(filecontent)

import sys 
usage="""Requires two parameters (param1, param2) Usage: python script.py param1 param2"""
if len(sys.argv)<3:
  print('The script: ',sys.argv[0],usage) 
  sys.exit()
param1=sys.argv[1]
param2=sys.argv[2]
print('''The two parameters received as input for the script are:\n ''',param1, param2)
while(True):
  print('INSERT INTEGER IN 1-10')
  param1 = input()
  if int(param1) in range(11):
    while(True):
      print('INSTERT CHAR IN [A,B,C]')
      param2=input()
      if param2 in ['A','B','C']:
        print('uso i parametri passati dall utente:', param1, param2)
        sys.exit()
      else: print('TRY AGAIN')
  else:print('TRY AGAIN')   

