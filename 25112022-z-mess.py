import math


def liniowe(a, b):
  if a == 0:
    if b == 0:
      print('Równanie tożsamościowe')
    else:
      print('Równanie sprzeczne')
  else:
    x = -b / a
    print('x = ', x)


a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a == 0:
  liniowe(b, c)
else:
  delta = b * b - 4 * a * c
  if delta < 0:
    print('Brak rozwiązań')
  elif delta == 0:
    x = -b / (2 * a)
    print('Jedno rozwiązanie x = ', x)
  else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('x1 = ', x1)
    print('x2 = ', x2)
