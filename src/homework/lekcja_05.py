# Zadanie 5 – Parsowanie CSV
#Masz string CSV: "Alice,28,Data Scientist,75000" . Użyj
#Imię
#Wiek (jako int)
#Zawód
#Pensję (jako int)
#Wyświetl te informacje w formacie: split(',') aby wyciągnąć: "Alice ma 28 lat, pracuje jako Data Scientist i zarabia $75000" ***

print ('_'*50)

print("\nWynik zadania 5:")

csv = "Alice,28,Data Scientist,75000"

dane = csv.split(",")

imie = dane[0]
wiek = int(dane[1])
zawod = dane[2]
pensja = int(dane[3])

print(f"{imie} ma {wiek} lat, pracuje jako {zawod} i zarabia ${pensja}")

print ('_'*50)


# Zadanie 8 – Ekstakcja informacji ze stringa
#Masz nazwę pliku: "model_results_2024_Q3.csv" .

#Wyciągnij rok i kwartał używając slicing lub split.


print("\nWynik zadania 8:")

plik = "model_results_2024_Q3.csv"

czesci = plik.split("_")

rok = czesci[2]
kwartal = czesci[3].split(".")[0]

print(f"Rok: {rok}")
print(f"Kwartał: {kwartal}")

print ('_'*50)

# Zadanie 9 – Filtrowanie outlierów
#Masz listę pomiarów: [23, 24, 22, 150, 23, 25, -10, 24, 23] . 
# Outlierem jest wartość poza zakresem [20, 30].
# Stwórz nową listę bez outlierów używając list comprehension.


print("\nWynik zadania 9:")

pomiary = [23, 24, 22, 150, 23, 25, -10, 24, 23]

czyste = [x for x in pomiary if 20 <= x <= 30]

print(czyste)

print ('_'*50)

#Zadanie 10 – Agregacja danych po kategoriach 

# Masz listę transakcji (kategoria, kwota):
# transactions = [
# ('food', 50),
# ('transport', 20),
# ('food', 30),
# ('entertainment', 40),
# ('transport', 15),
# ('food', 25) ]
# Oblicz łączną kwotę dla każdej kategorii. Wynik zapisz w słowniku (użyj pętli i warunków).


print("\nWynik zadania 10:")

transactions = [
    ('food', 50),
    ('transport', 20),
    ('food', 30),
    ('entertainment', 40),
    ('transport', 15),
    ('food', 25)
]

suma_kategorii = {}

for kategoria, kwota in transactions:

    if kategoria in suma_kategorii:
        suma_kategorii[kategoria] += kwota
    else:
        suma_kategorii[kategoria] = kwota

print(suma_kategorii)


print ('_'*50)


