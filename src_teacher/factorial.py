import time
import matplotlib

def fact(n):
    if n < 2:
        return 1
    else:
        return n *fact(n-1)

def factorial(n):
    fact = 1
    for k in range(1,n+1):
        fact *=k
    return fact

# Iterativo es más rápido que recursivo

for n in range(20,61,5):
    ini = time.time_ns()
    print("fact recursivo", fact(n))
    fin = time.time_ns()
    recursivo = ((fin-ini)/1e9)
    print("Duración bottom up ", recursivo)

    ini2 = time.time_ns()
    print("factorial iterativo", factorial(n))
    fin2 = time.time_ns()
    iterativo = ((fin2-ini2)/1e9)
    print("Duración top down ", iterativo,"\n")

    print("razon ", iterativo/ recursivo * 100)

    if recursivo < iterativo:
        print("gana recursivo")
    else:
        print("gana iterativo")
