def fac(n):
  if n==1:
    return 1
  return n*fac(n-1)

def bing(a,k):
  if k==0:
    return 1
  r=1.0
  for i in range(k):
    a=a-i
    r=r*a
  return r/fac(k)

def raiz2(n):
  r=0.0
  for k in range(n):
    r=r+bing(0.5,k)
  return r

def r2(n):
  r=1.0
  a=0.5
  b=1.0
  for k in range(1,n+1):
    b=(b*a)/k
    r=r+b
    a=a-1
  return r
 
def r3(n):
  r=1.0
  a=0.5
  b=1.0
  for k in range(1,n+1):
    b=((b*a)/k)*2
    r=r+b
    a=a-1
  return r

def r5(n):
  r=1.0
  a=0.5
  b=1.0
  for k in range(1,n+1):
    b=((b*a)/k)*4
    r=r+b
    a=a-1
  return r

def horner(a,i,x):
  if i==0:
    return a[i]
  else:
    return x*horner(a,i-1,x)+a[i]

def coef(n,alfa):
  r=[1.0]
  a=alfa
  b=1.0
  for k in range(1,n+1):
    b=(b*a)/k
    r=r+[b]
    a=a-1
  return r
 
def horner1(a,x):
  r=0
  k=len(a)-1
  while k>=0:
    r=r*x+a[k]
    k=k-1
  return r



    





