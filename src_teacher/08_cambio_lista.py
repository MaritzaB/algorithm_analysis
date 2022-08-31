def cambio(Monedas,Cantidad):
  minMonedas=Cantidad ;lista=[]
  if Cantidad in Monedas:
    return 1,[Cantidad]
  else:
    for i in [m for m in Monedas if m <= Cantidad]:
      minimo,monedas=cambio(Monedas,Cantidad-i)
      numeroMonedas=1+minimo
      if numeroMonedas < minMonedas:
        minMonedas=numeroMonedas 
        lista=monedas+[i]  
  return minMonedas,lista
  
cambio([1,5,10,25],63)
  
