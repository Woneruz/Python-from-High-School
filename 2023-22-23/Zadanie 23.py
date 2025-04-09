
nazwaPliku = "Dane/bin.txt"
# nazwaPliku = "Dane/bin_przyklad.txt"

plik = open(nazwaPliku, "r", encoding="utf-8")

licznik = 0

for linia in plik.readlines():
  liczba = linia[:-1]
  print(liczba)

print(licznik)

plik.close()