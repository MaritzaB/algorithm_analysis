# Busqueda secuencial de x en una lista a

def ss(a,x):
  for k in range(len(a)):
    if x == a[k]:
      return 1
      
  return -1
  
  
