import math
def f(a,b,c,d):
  cuenta= math.sqrt((a - c)**2) - math.sqrt((b-d)**2)
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