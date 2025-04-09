import math
a = -5
b = 5
h = 0.1

def f(x):
  return x*x+11*x+18
def mz(a,b):
  ya = f(a)
  yb = f(b)
  if math.fabs(ya) < h:
    print("mz w a = " + str(a))
    exit()
  if math.fabs(yb) < h:
    print("mz w b = " + str(b))
    exit()
  if ( ya*yb < 0):
    mz(a, a + (b-a)/2 )
    mz(a + (b-a)/2 , b)
#start
mz(a,b)