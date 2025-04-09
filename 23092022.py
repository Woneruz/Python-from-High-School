print("Podaj pierwsą liczbą z zakresu ",end=(""))
a=int(input())
print("Podaj ostatnią liczbą z zakresu ",end=(""))
b=int(input())
suma=0
for i in range (a,b+1, 1):
  print( i, ", ",end=" ")

print("\n\nParzyste: ")
for i in range(a,b+1, 1):

  if i%2 == 0:

    print(i)

  suma=suma+i
print("\nsuma wynosi: ", suma, end=(""))



