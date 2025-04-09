def parzystosc(a):
  if a % 2 == 0:
    return 1
  else:
    return 0




a = int(input("podaj liczbę: "))
if parzystosc(a):
  print("parzysta")
else:
  print("nieparzysta")