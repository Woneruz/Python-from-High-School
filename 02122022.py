def zmienwartosc():
  global b
  b = int(input("Zmień wartość zmiennej b wewnątrz funkcji:"))
  return 1



b = int(input("Zmień wartość zmiennej b w programie głównym:"))
zmienwartosc()
print("Wartość zmniennej na koniec", b)