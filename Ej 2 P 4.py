print('Numero A')
A = int(input())
print ('Numero B')
B = int(input())
if (A<B):
  for i in range (A,B+1):
    print(i)
else:
  for i in range (B,A+1):
    print(i)