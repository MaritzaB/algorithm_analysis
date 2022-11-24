
def cambio(Monedas,Cantidad):
  tabla=[0]*64
  minMonedas=Cantidad ;lista=[]
  if Cantidad in Monedas:
    tabla[Cantidad]=1
    return 1,[Cantidad]
  elif tabla[Cantidad] >0 :
    return tabla[Cantidad]
  else:
    for i in [m for m in Monedas if m <= Cantidad]:
      minimo,monedas=cambio(Monedas,Cantidad-i)
      numeroMonedas=1+minimo
      if numeroMonedas < minMonedas:
        minMonedas=numeroMonedas
        tabla[Cantidad]=minMonedas 
        lista=monedas+[i]  
  return minMonedas,lista
  
cambio([1,5,10,25],63)
cambio([1,5,10,25],63,[0]*64)
  
