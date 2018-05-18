primera = str(input('Dime una frase'))
ultima= str(input('Letra que quieres buscar'))

a = (primera.find(ultima))
z = (primera.rfind(ultima))

if(a == -1):
  print('')
else:
  print(a, z)