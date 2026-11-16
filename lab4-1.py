# Program służący do kompletowania listy zakupów.

list = []  # pusta lista

# w pętli pytamy o produkty do listy zakupów
while True:
    item = input("Co dodać do listy? ")
    if item == "":  # jeśli pusta odpowiedź, przerywamy pętlę pytającą o produkty
        break
    list.append(item)  # tekst wpisany przez użytkownika dołączamy na końcu listy

    for i, item in enumerate(list):
        print(f"{i+1}. {item}")

# po wyjściu z pętli zapisujemy listę do pliku
with open("lista.txt", "w") as f:
    for i, item in enumerate(list):
        f.write(f"{i+1}. {item}\n")
