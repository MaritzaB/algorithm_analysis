def cambio_dinsol(x,R):
  n=len(x)
  A=np.zeros((n+1,R+1))
  B=np.zeros((n+1,R+1))
  sol=[]
  
  for m in range(1,R+1):
    if m % x[0] == 0 :
      A[0,m] = m//x[0]
    else:
      A[0,m] = inf
        
  for i in range(1,n):
    for m in range(1,R+1):
      if x[i] <= m:
        if A[i-1,m]<A[i,m-x[i]]+1:
          r=A[i-1,m]
          s=-1
        else:
          r=A[i,m-x[i]]+1
          s=x[i]
      else:
        r=A[i-1,m]
        s=-1 
      A[i,m]=r
      B[i,m]=s
      
  i=n-1; j=R
  back=B[i,j]
  while back > 0 :
    if back>0:
      sol=sol+[back]
      back=B[i,j-back]
    else:
      back=B[i-1,j]
  return A[n-1,R],sol
  
    
