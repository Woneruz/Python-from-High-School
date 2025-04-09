ciag = input("podaj ciag znaków: ")
kod = int(input("podaj kod: "))
kodznak = int(0)
dl = len(ciag)
znak = " "
cezar = ''
i = 0
int(i)
while i < dl:
  if ord(ciag[i]) + kod <=90:
    kodznak = ord(ciag[i]) + kod
    cezar = cezar + chr(kodznak)
  else:
    kodznak = ord(ciag[i]) + kod-26
    cezar = cezar + chr(kodznak)
  i = i + 1
print(ciag, "po zaszyfrowaniu kluczem ", kod , "to ", cezar)
