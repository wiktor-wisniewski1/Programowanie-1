liczba_studentów = int(input("Podaj liczbę studentów: "))
liczba_zaliczen = 0
for x in range(liczba_studentów):
    nazwisko = input("Podaj nazwisko studenta: ")
    punkty = int(input("Podaj liczbę punktów zdobytych przez studenta: "))
   
    if punkty < 0 or punkty > 100:
        print("Nieprawidłowa liczba punktów.")
        continue
    elif punkty < 50:
        ocena = 2
    elif punkty < 60:
        ocena = 3
    elif punkty < 70:
        ocena = 3.5
    elif punkty < 80:
        ocena = 4
    elif punkty < 90:
        ocena = 4.5
    elif punkty <= 100:
        ocena = 5

    if ocena >= 3:
        liczba_zaliczen += 1

print(f"Liczba zaliczeń: {liczba_zaliczen}")
