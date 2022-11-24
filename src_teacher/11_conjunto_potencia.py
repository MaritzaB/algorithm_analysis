def conjunto_potencia(a):
  # Calcula y devuelve una lista de todos los subconjuntos del conjunto a 
  if len(a)==1:
    return [[],a]
  lst=[]
  b=conjunto_potencia(a[1:])
  for i in b:
    aux=[a[0]]+i
    lst=lst+[aux]
  return b+lst

def selec(a,p,m):
  s=conjunto_potencia(a)
  r=[]
  for i in s:
    if checa(i,p,m):
      r=r+[i]
  return r
def checa(lst,p,m):
  s=0
  for k in lst:
    s=s+p[k]
  return s<m

def max_val(a,b):
  m_val=-1;m_sol=a[0]
  for i in a:
    if val(i,b)>m_val:
      m_val=val(i,b)
      m_sol=i
  return m_sol,m_val

def val(lst,b):
  r=0
  for i in lst:
    r=r+b[i]
  return r

# Nos traemos los valores del programa 16_dinamic 
# Este prgrama es para validar
a=[0,1,2,3,4]
p=[2,5,3,6,1]   # pesos
b=[28,33,5,12,20] # valores
M=10

pot = conjunto_potencia(a)
print('\n', pot ,'\n')

s = selec(a,p,M)

solucion,maximo = max_val(s,b)
print("solucion ", solucion)
print("maximo ", maximo)
