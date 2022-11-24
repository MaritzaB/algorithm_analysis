# Serie de Leibniz para calcular pi
def leibniz(n):
  r=0
  s=1.0
  for k in range(n):
    r=r+s/(2*k+1)
    s=s*(-1.0)
  return 4*r
