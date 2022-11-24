def cambio_ds(x,R):
  n=len(x)
  A=np.zeros((n,R+1))
  B=np.zeros((n,R+1))
  sol=[]
  
  for m in range(1,R+1):
    if m % x[0] == 0 :
      A[0,m] = m//x[0]
      B[0,m] = x[0]
    else:
      A[0,m] = inf
        
  for i in range(1,n):
    for m in range(1,R+1):
      if x[i] <= m:
        if A[i-1,m]<=A[i,m-x[i]]+1:
          A[i,m]=A[i-1,m]
          B[i,m]=  B[i-1,m]
        else:
          A[i,m]=A[i,m-x[i]]+1
          B[i,m]=x[i]
      else:
        A[i,m]=A[i-1,m]
        B[i,m]=  B[i-1,m] 
  i=n-1; j=R
  r=int(B[i,j])
  while  r != 0 :
      sol=sol+[B[i,j]]
      jaux=j-r
      r=int(B[i,j-r])
      j=jaux
  return B[n-1,:],A[n-1,R],sol
  
    
