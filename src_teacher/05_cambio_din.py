def cambio_din(x,R):
  n=len(x)
  A=np.zeros((n+1,R+1))
  for m in range(1,R+1):
    if m % x[0] == 0 :
      A[0,m] = m//x[0]
    else:
      A[0,m] = inf
        
  for i in range(1,n):
    for m in range(1,R+1):
      if x[i] <= m:
        r=min(A[i,m-x[i]]+1,A[i-1,m])
      else:
        r=A[i-1,m]
      A[i,m]=r
  return A[n-1,R]
  
    
