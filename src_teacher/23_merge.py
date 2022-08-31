def merge(l,r):
  nl=len(l)
  nr=len(r)
  i=j=0
  a=[]
  while (i<nl and j<nr):
    if l[i]<=r[j]:
      a.append(l[i])
      i=i+1
    else:
      a.append(r[j])
      j=j+1
  while i<nl:
    a.append(l[i])
    i=i+1
  while j<nr:
    a.append(r[j])
    j=j+1
  return a

def mergesort(a):
  if len(a)==1:
     return a
  else:
     return merge(mergesort(a[0:len(a)/2]),mergesort(a[len(a)/2:len(a)]))

def aptitud(a):
  s=0
  for i in range(8):
    j=0
    while j<i: 
      if (a[j]==a[i]-(i-j)) or (a[j]==a[i]+(i-j)):
        s=s+1
      j=j+1
    j=i+1
    while j<8:
      if (a[j]==a[i]-(j-i)) or (a[j]==a[i]+(j-i)):
        s=s+1
      j=j+1
  s=s/2
  return 1./(1+s)

def power(a,n):
  if n==0:
    return 1
  x=power(a,n//2)
  if n%2==0:
    return x*x
  else:
    return a*x*x

def power1(a,n):
  r = 1
  for i in range(n):
    r = r * a
  return r

import time
ini = time.time_ns()
print(power(2,640))
fin = time.time_ns()
power_time = ((fin-ini)/1e8)
print("Duración de power %f \n" % power_time)

ini2 = time.time_ns()
print(power1(2,640))
fin2 = time.time_ns()
power_time2 = ((fin2-ini2)/1e8)
print("Duración de power1 %f \n" % power_time2)

print("Proporción de tiempos: %i \n" % int(power_time2/power_time))

