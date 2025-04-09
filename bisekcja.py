a = 3
b = -5
krok = 0.1

def f(x):
  return x*x*x + 3*x*x - 13*x - 15

def mz(a,b):
  ya = f(a)
  yb = f(b)

  print(str(a) + " " + "| " + str(b) + "  --  " + str(yb))

  TheEnd = 0
  if abs(ya) < krok:
    print("Mz ya = " + str(ya) + " dla x = " + str(a))
    TheEnd = 1
  if abs(yb) < krok:
    print("Mz yb = " + str(yb) + " dla x = " + str(b))
    TheEnd = 1
  if TheEnd == 1:
    exit()
  if (ya * yb < 0):
    mz(a,a + (b-a)/2)
    mz(a + (b-a)/2,b)

mz(a,b)

