from matplotlib import pyplot as plt
import numpy as np
from numpy import *
from math import sqrt


def rand_array(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.random()
      return np.array(lista)


def tri_rand(n):  #TRANFORMA NÚMEROS (integra e invierte la función)
  x = []
  U = rand_array(n) #valores uniformemente distribuidos
  for u in U:
    if u<0.5:
      x.append(sqrt(2*u)) #inversa de la función acumulada del trángulo
    else:
      x.append(2-sqrt(2-2*u))
  return np.array(x)

plt.hist(tri_rand(5000), bins='auto')
plt.savefig("triangulo.png")


def pi_aprox(n):
  con = 0.0 # 'con' numero de aciertos entre número de ensayos la probabilidad de atinarle
  for i in range(n):
    x=2*random.random()-1.0 # transformación lineal, mapeamos (coordenadas de dónde cae el dardo)
    y=2*random.random()-1.0
    if x*x+y*y<1:
      con=con+1.0 #círculo de radio 1
  return 4*(con/n)

print('Aproximación de pi', pi_aprox(9999))


def bufon(throws):  # distancia del centro a la recta más cercana entre 0 y 1
  x=rand_array(throws)  # línea del centro de la aguja a la línea paralela más cercana
  theta=rand_array(throws)  # angulo con el que cae la aguja
  theta=0.5*pi*theta  # proyección vertical de la mitad de la aguja
  hits=x<=0.5*sin(theta)  # Arreglo que tiene 0 o 1. Por cada valor de x comparo con este valor. Operación entre listas.
  return throws/sum(hits)

print('aproximación a pi con bufon', bufon(66666))
