def block(n):
  lb = 1
  cp = n // 2
  rp = n % 2
  while (cp != 0):
    cn = cp // 2
    rn = cp % 2
    if rn != rp:
      lb=lb+1
    cp = cn
    rp = rn 
  return lb 


f = open("bin.txt")
licznik = 0
for l in f.readlines():
  if block(int(l, 2)) <=2:
    licznik += 1
print(licznik)