def Init_tabla(n):
  for i in range(n):
    tabla[i,0]=1
    tabla[i,i]=1
    
def coef_rec(n,k):
  if k==0 or k==n:
    return 1
  else:
    return coef_rec(n-1,k)+coef_rec(n-1,k-1)
    
def coef_tab(n,k):
  if tabla[n,k] >0:
    return tabla[n,k]
  else:
    r=coef_tab(n-1,k)+coef_tab(n-1,k-1)
    tabla[n,k]=r
    return r
    
    
  
