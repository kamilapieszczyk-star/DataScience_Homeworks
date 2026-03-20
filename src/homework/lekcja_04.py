# Zadanie 4 – Formatowanie nazw kolumn
#Ustandaryzuj nazwę kolumny z datasetu.
#Dane:
#Nazwa raw: 
#" PATIENT_age_YEARS "
#Wymagania:
#Usuń białe znaki
#Zamień na małe litery
#Zastąp _ przez 
#Oczekiwany rezultat:
#" "
#Użyj title case
#Patient Age Years

print("\nWynik zadania 4:")

nazwa_raw = "PATIENT_age_YEARS"

nazwa = nazwa_raw.strip()
nazwa = nazwa.lower()
nazwa = nazwa.replace("_", " ")
nazwa = nazwa.title()
print(nazwa)

# Zadanie 6 – Dokładność w procentach
#Sformatuj metryki modelu.
#Dane:
#Accuracy: 0.9234
#Precision: 0.8891
#Recall: 0.9456
#Wymagania:
#Wyświetl każdą metrykę w procentach z 2 miejscami po przecinku
#Użyj f-strings z formatowaniem :.2%
#Dodaj estetyczne wyrównanie kolumn


print("\nWynik zadania 6:")

accuracy = 0.9234
precision = 0.8891
recall = 0.9456

print(f"{'Accuracy':<10}: {accuracy:.2%}")
print(f"{'Precision':<10}: {precision:.2%}")
print(f"{'Recall':<10}: {recall:.2%}")


# Zadanie 9 – Normalizacja Min-Max
#Znormalizuj wartość do zakresu [0, 1].
#Dane:
#Wartość: 75
#Minimum w kolumnie: 50
#Maximum w kolumnie: 100
#Wymagania:
#Wzór: normalized = (value - min) / (max - min)
#Oblicz dla wartości 75, 50, 100, 62.5
#Sprawdź, czy wynik mieści się w [0, 1]
#Wyświetl tabelkę: wartość oryginalna | wartość znormalizowana

print("\nWynik zadania 9:")

minimum = 50
maximum = 100

wartosci = [75, 50, 100, 62.5]

print(f"{'Wartosc oryginalna':<20} | {'Wartosc znormalizowana':<22}")
print("-" * 45)

for value in wartosci:

    normalized = (value - minimum) / (maximum - minimum)

    czy_poprawne = 0 <= normalized <= 1

    print(f"{value:<20} | {normalized:<22.2f}")
    