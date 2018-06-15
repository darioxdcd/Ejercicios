cantidad = 0
mayor = 0
posicion = 0
posicion_mayor = 0
while True:
  print('Dime un numero?')
  a = int(input())
  posicion =posicion + 1
  if a < mayor:
    mayor = mayor
  else:
    mayor = a
    posicion_mayor = posicion
  cantidad += 1
  if a == 0:
    break
print('Hay' +' '+ str(cantidad-1)+' '+'numeros')
print('El mayor es' +' '+ str(mayor) +' y está en' +' '+ str(posicion_mayor))