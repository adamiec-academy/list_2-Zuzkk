def is_prime(liczba):
    prime = True
    if liczba < 2:
        prime = False
    for dzielnik in range(2, liczba):
        if liczba % dzielnik == 0:
            prime = False
    return prime


def is_diabolic(liczba):
    diabolic = "666" in str(liczba)
    return diabolic


i = 0
zakres = 100000

print(f"Diabelskie liczby pierwsze z zakresu 1-{zakres} to: ")

for liczba in range(1, zakres + 1):
    if is_diabolic(liczba) and is_prime(liczba):
        print(liczba)
        i += 1

print(f"Jest ich {i}.")
