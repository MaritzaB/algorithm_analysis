def delk(a,k):
  n=len(a);b=zeros((n-1,n-1))
  for i in range(1,n):
    for j in range(n):
      if j<k:
        b[i-1,j]=a[i,j]
      if j>k:
        b[i-1,j-1]=a[i,j]
  return b

def det(a):
  n=len(a)
  d=0
  if n==1:
    return a[0,0]
  for j in range(n):
    if j%2:
      s=-1.0
    else:
      s=1.0
    d=d+s*a[0,j]*det(delk(a,j))
  return d





