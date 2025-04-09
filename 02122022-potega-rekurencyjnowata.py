def potega(podstawa,wykladnik):
  if wykladnik ==0:
    return 1
  else:
    return potega(podstawa,wykladnik-1)*podstawa

print(potega(int(input('podstawa: ')),int(input('potega: '))))