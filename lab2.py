# Wprowadzenie do pętli

# Obsługa wprowadzania liczby przez użytkownika. Założenia:
# (1) w przypadku wpisania czegoś, co nie jest liczbą, użytkownik może pomownie
# wprowadzić liczbę
# (2) akceptuje liczby od n_min do n_max; w przypadku wyjścia poza zakres,
# użytkownik jest ponownie proszony o wpisanie liczby

n_min = 1
n_max = 50

while True:
    try:
        n = int(input("Podaj liczbę: "))
        if n < n_min or n > n_max:
            print(f"Liczba spoza zakresu od {n_min} do {n_max}")
        else:
            break
    # to samo co wyżej, ale z zastosowaniem continue
    #         if n < 1 or n > 100:
    #             print("Liczba spoza zakresu od 1 do 100")
    #             continue
    #         break
    except:
        print("Musisz wpisać liczbę!")

# najprostsza pętla zliczająca powtórzenia (iteracje)
i = 1
while i <= n:  # pętla się wykonuje, czyli powtarza, jeśli warunek jest spełniony
    print(i)
    i = i + 1  # zwiększenie wartości zmiennej i o 1, czyli inkrementacja
