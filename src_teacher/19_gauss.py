import numpy as np
def gauss(a,b):
  n = len(b)
# Fase de eliminación
  for k in range(0,n-1):
    for i in range(k+1,n):
      if a[i,k] != 0.0:
        lam = a[i,k]/a[k,k]
        a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
        b[i] = b[i] - lam*b[k]
# Sustitución hacia atras
  for k in range(n-1,-1,-1):
    b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
  return b
  
  gauss(np.array([[4.0,-2.0,1.0],[-2.0,4.0,-2.0],[1.0,-2.0,4.0]]),np.array([11.0,-16.0,17.0]))
  
  
  
