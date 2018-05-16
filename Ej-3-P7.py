import math
def Potenciacion(numero, exponente):
  if exponente == 0:
    return 1
  resultado=numero
  for i in range(exponente - 1):
    resultado = resultado * numero
  return resultado
def f(a,b,c,d):
  cuenta= math.sqrt(Potenciacion((c-a),3)) - math.sqrt(Potenciacion((d-b),2))
  return cuenta
print ('¿ 1º X?')
a= int(input())#x1
print ('¿1º Y?')
b= int(input())#y1
print ('¿ 2º X?')
c= int(input())#x2
print ('¿2º Y?')
d= int(input())#y2
print ( f(a,b,c,d))
print('( ͡° ͜ʖ ͡°)')