def pierwsze(text):
  liczba = int(input("podaj liczbę: "))
  return text[liczba]

def odwrot(text):
  return text[::-1]

def parz(text, liczba):
  if liczba % 2 == 0:
    return text[::2]
  else:
    return text[1::2]

while True:
  print("menu: ")
  print("1. Któryś element z tekstu")
  print("2. Odwróć napis")
  print("3. wypisz parzyste nieparzyste")
  print("q  Zakończ program")

choice = input("Wybierz opcję: ")

if choice == "1":
  text = input("podaj tekst: ")

  print(pierwsze(text))
  
elif choice == "2":
  text = input("podaj tekst:")
  print(odwrot(text))

elif choice == "3":
  text = input("podaj tekst: ")
  liczba = int(input("podaj liczbę: "))
  print(parz(text, liczba))

elif choice == "q":
  break
  
else:
  print("niewłaściy wybór")
