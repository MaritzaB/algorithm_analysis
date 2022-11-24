def bin(x):
    if x<2:
        return [x]
    else:
        return [x%2]+bin(x//2)

def power_bin(b,n):
    a = bin(n)
    s=1
    c=b
    n=len(a)
    for k in range(n):
        if a[k]==1:
            s=s*c
        c=c*c
    return s

# La máx complejidad de este es log b2 de n

potencia = power_bin(2,10) # 3*3*3*3c

print(potencia)

#Método de horner para evaluar polinomios

def horner(a,x):
    # a es una lista de coeficientes y x el número a evaluar
    n = len(a)
    p = 0
    for i in range(n):
        k=n-1-i
        p=p*x+a[k]
    return p

# Para recuperar el valor, es decir

a = bin(11)
print(horner(a,2))

