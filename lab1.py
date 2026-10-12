# Bot konwersacyjny

print("Cześć")

print("Jak masz na imię?") 
name = input()

print(f"Miło Cię poznać, {name}!")
## można też tak:
# print("Miło Cię poznać", name)
# print("Miło Cię poznać, " + name + "!")
## ale rozwiązanie z f" jest wygodniejsze

year = input("Podaj rok urodzenia: ") # pobranie danych jako tekstu (string)
year = int(year) # zamiana tekstu (string) na liczbę całkowitą (int)
## zwykle będziemy to skracać do formy jednolinijkowej:
# year = int( input("Podaj rok urodzenia: ") )

age = 2026 - year
print(f"Twój wiek: {age}")
print("Pozwól, że skomentuję:")

# instrukcja warunkowa if
if age > 30:
    print("No to z górki...")

# instrukcja warunkowa if-else
if age > 30:
    print("No to z górki...")
else:
    print("Młodość... Ciesz się, póki możesz :)")

# instrukcja warunkowa if-elif-else
if age == 100:
    print("Sto lat!")
elif age == 50:
    print("Nieźle, jeszcze tylko drugie tyle i będzie setka")
elif age > 30:
    print("No to z górki...")
elif age == 18:
    print("18!!!")
elif age >= 0 and age <= 10:
    print("Dzieciak")
elif age < 0:
    print("Przybywasz z przyszłości")
else:
    print("Młodość... Ciesz się, póki możesz :)")

## można też tak (ale kto by chciał...):
# if age > 30:
#     if age == 100:
#         print("Sto lat!")
#     else:
#         if age == 50:
#             print("Nieźle, jeszcze tylko drugie tyle i będzie setka")
#         else:
#             print("No to z górki...")
# else:
#     if age == 18:
#         print("18!!!")
#     else:
#         if age >= 0 and age <= 10:
#             print("Dzieciak")
#         else:
#             if age < 0:
#                 print("Przybywasz z przyszłości")
#             else:
#                 print("Młodość... Ciesz się, póki możesz :)")