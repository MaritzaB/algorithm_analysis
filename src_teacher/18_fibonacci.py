import inspect

def fibonacci(n):
  if n <= 2:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

def fibTabla(n):
  if not t[n]:
    t[n] = fibTabla(n-1) + fibTabla(n-2)
  return t[n]

t = [0] * 30
t[0] = 1
t[1] = 1
print(t)

import time
for i in range(1,22):
  ini = time.time_ns()
  print("Recursivo ", fibonacci(i))
  fin = time.time_ns()
  recursivo = (fin - ini)/1e9

  ini2 = time.time_ns()
  print("Con tabla ", fibTabla(i))
  fin2 = time.time_ns()
  iterativo = (fin2 - ini2)/1e9


for i in range(1,22):
  #print(fibonacci(i), end=" ")
  print(fibTabla(i))


def stack_depth():
  return len(inspect.getouterframes(inspect.currentframe()))-1
  
def fibonaccii(n):
  print("{indent}fibonaccii({n}) called".format( indent=" " * stack_depth(), n=n))
  if n <= 2:
    return 1
  return fibonaccii(n-1) + fibonaccii(n-2)
    
fibonaci_cache = {}
def fibonaci(n):
  if n <= 2:
    return 1
  if n not in fibonaci_cache:
    fibonaci_cache[n] = fibonaci(n-1) + fibonaci(n-2)
  return fibonaci_cache[n]

def fibonacci_bu(n):
  series = [1, 1]
  while len(series) < n:
    series.append(series[-1] + series[-2])
  return series[-1]

def fibona(n):
  previous = 1
  current = 1
  for i in range(n-2):
    next = current + previous
    previous, current = current, next
  return current 
