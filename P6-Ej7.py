cantidad = 0
mayor = 0
while True:
  cantidad += 1
  print('Dime un numero?')
  n = int(input())
  if n < mayor:
    mayor= mayor
  else:
    mayor= n
  if n == 0:
    break
print('Son' +' '+ str(cantidad-1)+' '+ 'numeros')
print('El mayor es' +' '+ str(mayor))