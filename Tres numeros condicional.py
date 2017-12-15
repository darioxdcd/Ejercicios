print('Cual es el primer numero?')
x = int (input())
print('Cual es el segundo numero?')
y = int(input())
print('Cual es el tercer numero?')
z = int(input())
if (x < y) and (x < z):
  print(x)
if (z < x) and (z < y):
  print(z)
if (x < z) and (x < y):
  print(y)
if ( x == y ==z ):
  print(x)