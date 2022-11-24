import time
# Solucion y maximo beneficio alcanzable
# con los objetos 0.. i -1 , teniendo un peso m
# disponible en la mochila
def mochila_d_rec (i ,m ,p , b ) :
  # top down
  # i es el número de objetos que están entrando
  # base de la recurrencia : 0 objetos
  if i ==0:
    return [] ,0
  # opcion 1: el objeto i -1 NO se introduce
  sol_NO , max_b_NO = mochila_d_rec (i -1 , m ,p , b )
  # opcion 2: el objeto i -1 SI se introduce
  if p [i -1] <= m :
    sol_SI , max_b_SI = mochila_d_rec (i -1 , m - p [i -1] , p , b )
    if b [i -1] + max_b_SI > max_b_NO :
      return sol_SI+[1] , b [i -1]+ max_b_SI
  return sol_NO+[0] , max_b_NO

p=[2,5,3,6,1]
b=[28,33,5,12,20]
M=10

ini = time.time_ns()
print(mochila_d_rec(5,M,p,b))
fin = time.time_ns()
recursivo = (fin - ini)/1e9
print("Duración top down ", recursivo)

def fib_rec( n ):
  if n <2:
    return 1
  else:
    return fib_rec (n -1) + fib_rec (n -2)

def fib_rec_mem ( n ):
  global t
  if not n in t :
    t[ n ]= fib_rec_mem(n -1) + fib_rec_mem (n -2)
  return t [ n ]

def fib_rec_mem1 ( n ):
  if not t[n]:
    t[ n ]= fib_rec_mem(n -1) + fib_rec_mem (n -2)
  return t [ n ]


# Devuelve el maximo beneficio alcanzable con los objetos
# de pesos p y beneficios b , teniendo un peso M disponible
def mochila_d_pd1 (p ,b , M ):
  n = len ( p );x=[]
  d =[[0 for m in range ( M +1) ] for i in range ( n +1) ]
  t =[[0 for m in range ( M +1) ] for i in range ( n +1) ]
  for i in range (1 , n +1) :
    for m in range (1 , M +1) :
      # si se puede introducir el objeto i y el beneficio
      #es mayor que no haciendolo , lo introducimos
      if p[i -1] <= m and b[i -1]+ t[i -1][ m - p[i -1]] > t[i -1][ m ]:
        t[ i ][ m ]= b[i -1]+ t[i -1][ m - p[i -1]]
        d [ i ][ m ]=1
        # en caso contrario , no lo introducimos
      else :
        t[ i ][ m ]= t[i -1][ m ]
        d [ i ][ m ]=0
  return t[:][:],d[:][:]

def back_search(p,d,M):
  n=len(p)
  x =[]
  m=M
  for i in range (n ,0 , -1) :
    x.insert(0 , d[ i ][ m ])
    if d[ i ][ m ]==1:
      m = m - p[i -1]
  return x

t = []
d = []

ini2 = time.time_ns()
t,d = mochila_d_pd1(p,b,M)
fin2 = time.time_ns()
iterativo = (fin2 - ini2)/1e9
print("Duración ", iterativo)

print("razon ", iterativo/ recursivo * 100)

if recursivo < iterativo:
    print("gana recursivo")
else:
    print("gana iterativo")

print()
print("T= ", t,"\n")
print("D= ", d)

s = back_search(p,d,M)
print("Solución= ", s)

