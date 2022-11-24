def cambio(Monedas,Cantidad):
  minMonedas=Cantidad 
  if Cantidad in Monedas:
    return 1
  else:
    for i in [m for m in Monedas if m <= Cantidad]:
      numeroMonedas=1+cambio(Monedas,Cantidad-i)
      if numeroMonedas < minMonedas:
        minMonedas=numeroMonedas
  return minMonedas
  
cambio([1,5,10,25],63)
  
