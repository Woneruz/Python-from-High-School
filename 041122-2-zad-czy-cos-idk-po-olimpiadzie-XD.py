print("Podaj napis: ", end=" ")
nap=input()
dl=len(nap)
for i in range (0, dl, 1):
    if not (ord(nap[i]) in range (65,91) or ord(nap[i]) in range (97,123)):
      print(nap[i],end="")