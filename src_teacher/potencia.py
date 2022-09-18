
def convb(n,b=2):
    # n es el número a convertir y b a base
    if n<b:
        return [n]
    else:
        return convb(n//b) + [n%b]

print(convb(11))

# El número de cifras binarias es log base 2 de n
# 
import numpy as np

orden = int(np.log2(11)+1)

print(orden)