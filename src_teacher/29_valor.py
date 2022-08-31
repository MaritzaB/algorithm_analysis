import math
def valor(m, lim):  
  for n in range(lim):
    if m**n < math.factorial(n):
      return  n
  return -1
