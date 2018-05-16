#LOS APUNTES NO TIENEN SENTIDO,PUESTO QUE AL FINAL ACABAS RESTANDO 1, EL FIBONACCI ES A,B,B+A, Y ASI SUCESIVAMENTE SE SUMAN EL ULTIMO VALOR CON EL PENULTIMO.
def fib(n):
  a,b= 0,1
  while a<n:
    print(a, end='  ')
    a,b= b, b+a
  print()
print('Hasta que numero?')
a= int(input())
print(fib(a))
#la funcion end la he buscado por internet, a parte te hago toda la cadena de Fibonacci, un aporte extra al programa.