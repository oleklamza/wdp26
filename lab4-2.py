import csv

# pytamy o plik z zestawem słówek
# plik składa się z par słów w dwóch językach, np.:
# kot: cat
# pies: dog
# itd.
filename = input("Podaj nazwę pliku: ")

# otwieramy plik
with open(filename, encoding="utf-8") as file:
    # potrzebny jest nam pusty słownik, ...
    d = {}
    # ...który w pętli idącej po kolejnych wierszach pliku...
    while True:
        line = file.readline()
        if line == "":
            break
        row = line.split(":")
        k = row[0].strip() # strip "obcina" ewentualne spacje z lewej i prawej strony słowa
        v = row[1].strip()
        # ...dodajemy do słownika
        d[k] = v

cor_ans = 0 # licznik poprawnych odpowiedzi
# lecimy po kolejnych parach (klucz-wartość) ze słownika, np.:
# kot: cat
# "kot" jest tu kluczem, "cat" wartością powiązaną z tym kluczem 
for k, v in d.items():
    print(k)
    ans = input("Odpowiedź: ")
    # sprawdzamy, czy padła poprawna odpowiedź
    if ans.lower() == v.lower(): # lower zamienia wszystkie litery na małe
        print("dobrze")
        cor_ans += 1
    else:
        print("źle")
        print(f"prawidłowa odpowiedź to: {v}")
    print() # pusta linijka przerwy
    
# podsumowanie sesji z programem
print(f"Liczba słów: {len(d)}")
print(f"Poprawnych odpowiedzi: {cor_ans}")
print(f"Niepoprawnych odpowiedzi: {len(d) - cor_ans}")