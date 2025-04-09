liczba = int(input("podaj liczbę: "))
dziel = 0

for i in range (1,liczba+1,1):
  if liczba % i == 0:
    dziel += 1

print("suma dzielników równa się:", dziel)