def run_kut4(F,x,y,h):
  K0 = h*F(x,y)
  K1 = h*F(x + h/2.0, y + K0/2.0)
  K2 = h*F(x + h/2.0, y + K1/2.0)
  K3 = h*F(x + h, y + K2)
  return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0

def integrate(F,x,y,xStop,h):
  X = []
  Y = []
  X.append(x)
  Y.append(y)
  while x < xStop:
    h = min(h,xStop - x)
    y = y + run_kut4(F,x,y,h)
    x = x + h
    X.append(x)
    Y.append(y)
  return array(X),array(Y)

def F(x,y):
  return -x/y

def F1(x,y):
  return y

def F2(x,y):
  return -x

def integratev(F1,F2,x,y,tStop,h):
  X = []
  Y = []
  X.append(x)
  Y.append(y)
  t=0
  while t < tStop:
    h = min(h,tStop - t)
    x = x + run_kut4(F1,x,y,h)
    y = y + run_kut4(F2,x,y,h)
    t = t + h
    X.append(x)
    Y.append(y)
  return array(X),array(Y)

from numpy import array
x,y=integratev(F1,F2,-1.0,0.0,8.0,0.01)
from matplotlib import pyplot as plt
plt.plot(x,y)
plt.show()


