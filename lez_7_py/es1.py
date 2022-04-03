import numpy as np
class Points():
  def __init__(self):
    x, y, z = [input('x='), input('y='), input('z=')]
    self.Pt = [int(x), int(y), int(z)]

  def newp_dist(self):
    newx = input('cambiare punto si o no?')
    if newx=='si':
      x,y,z = [input('x='), input('y='), input('z=')]
      P = self.Pt
    else:
      P = self.Pt

    x1,y1,z1 = [input('x1='), input('y1='), input('z1=')]
    self.Pt1 = [int(x1), int(y1), int(z1)]
    Q = self.Pt1
    d = np.sqrt(pow(Q[0]-P[0],2)+pow(Q[1]-P[1],2)+pow(Q[2]-P[2],2))
    return d
PP = Points()
print(PP.newp_dist())
