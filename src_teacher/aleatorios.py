from matplotlib import pyplot as plt
import numpy as np
# para la complejidad el for manda, cuantas instancias del for tengo? pues n

def seed(ini):
    global rand
    rand = ini

seed(5.0)

def randcon(n):
    global rand
    a = 16807   #7**5
    m = 2147483647  #2**31-1
    num = []
    for k in range(n):
        rand = a*rand%m
        num = num+[rand]
    return np.array(num)

plt.hist(randcon(50000), bins="auto")
plt.show()
