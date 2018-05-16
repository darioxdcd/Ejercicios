def Potenciacion(numero, exponente):
  if n == 0:
    return 1
  resultado=numero
  for i in range(exponente - 1):
    resultado = resultado * numero
  return resultado
print ('¿Cual es x ?')
x = int (input())
print ('¿Cual es n?')
n= int(input())
print (Potenciacion(x,n))
print ('¯\_ツ_/¯''      EZ')
