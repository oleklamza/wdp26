# Zgadnij, jaka to liczba?
# Program wymyśla (losuje) liczbę z danego zakresu
# Gracz odgaduje.
# Program daje podpowiedzi: za mało, za dużo.

import random

x_min = 1
x_max = 100
cnt = 0

# wylosowanie liczby
rnd = random.randint(x_min, x_max)
print(f"Zgadnij, o jakiej liczbie z zakresu {x_min}..{x_max} myślę w tej chwili?")
# print(f"Wylosowana liczba: {rnd}")

while True:
    # odpytanie użytkownika: szczegóły kodu w lab2.py
    while True:
        try:
            x = int(input("Podaj liczbę: "))
            if x < x_min or x > x_max:
                print(f"Liczba spoza zakresu od {x_min} do {x_max}")
            else:
                break
        except:
            print("Musisz wpisać liczbę!")

    # sprawdzanie
    cnt += 1 	# inkrementacja liczby prób

    if x > rnd:
        print("Źle, za dużo")
    elif x < rnd:
        print("Źle, za mało")
    else:
        print("BRAWO!")
        print(f"Liczba prób: {cnt}")
        break
