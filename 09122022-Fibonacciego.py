def reku(n):
    if n == 0: return 0
    elif n == 1: return 1
    return reku(n-1) + reku(n-2)


def iter(n):
    if n == 0: return 0
    elif n == 1: return 1
    p, w = 0, 1
    for i in range(n-1):
        p, w = w, p+w
    return w

wybor = input("wybierz rekurencyjne lub iteracyjne (r lub i): ")

if wybor == "r":
  print("wwybrales rekurencyny")
elif wybor == "i":
  print("Wybrales iteracyjny")

n = int(input("podaj element ciagu: "))

if wybor == "r":
  print("Rekurencyjnie = ", reku(n))
elif wybor == "i":
  print("Iteracyjnie = ", iter(n))