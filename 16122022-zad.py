import os
q = 1
def pierwsze(text):
  liczba = int(input("podaj liczbę: "))
  liczba = liczba-1
  return text[liczba]

def odwrot(text):
  return text[::-1]

def parz(text, liczba):
  if liczba % 2 == 0:
    return text[::2]
  else:
    return text[1::2]

while q==1:
  os.system('clear')
  print("menu: ")
  print("1. Któryś element z tekstu")
  print("2. Odwróć napis")
  print("3. wypisz parzyste nieparzyste")
  print("q  Zakończ program")

  choice = input("\nWybierz opcję: ")

  if choice == "1":
    text = input("\npodaj tekst: ")

    print(pierwsze(text))
    m=(input("nacisnij enter"))
    
  elif choice == "2":
    text = input("\npodaj tekst: ")
    print(odwrot(text))
    m=(input("nacisnij enter"))
    
  elif choice == "3":
    text = input("\npodaj tekst: ")
    liczba = int(input("\npodaj liczbę: "))
    liczba = liczba-1
  
    print(parz(text, liczba))
    m=(input("\nnacisnij enter"))
    
  elif choice == "q":
    q=2
    
    
  else:
    print("niewłaściy wybór:\n")
  