liczba = input("podaj liczbę: ")
suma = 0
dl = len(liczba)
for i in range (0,dl,1):
  suma = suma + int(liczba[i])
print ("suma cyfr wprowadzonej liczby: ", suma)