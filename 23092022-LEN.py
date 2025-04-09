#print("Podaj wyraz: ", end="")
#napis = input()
#dl=len(napis)
#print(dl)
#for i in range (dl,0,-1):  
#  print(napis[i-1],end=" ")


#to nie dziala idk
print("Podaj wyraz: ", end="")
napis = input()
dl=len(napis)
#print(dl)
for i in range (0,dl,1):  
  if napis[i] != " ":
    print(napis[i], end=" ")