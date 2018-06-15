cantidad = 0
suma = 0
media = 1
while True:
  print('Dime un numero?')
  a = int(input())
  cantidad += 1
  suma = suma + a
  if a == 0:
    break
print('Hay' +' '+ str(cantidad-1)+''+ 'numeros')
print('Su suma es'+' '+str(suma))
media = suma/(cantidad-1)
print('Su media es' +' '+ str(media))