zadania = []
while True:
    print("Menu:")
    print("1. Dodaj zadanie")
    print("2. Wyświetl zadania")
    print("3. Usuń zadanie")
    print("4. Wyświetl liczbę zadań")
    print("0. Zakończ")
    wybór = input("Wybierz opcję:")
    if wybór == "1":
        zadanie = input("Podaj zadanie: ")
        zadania.append(zadanie)
    elif wybór == "2":
        if len(zadania) == 0:
            print("Nie ma co wyświetlac")
        else:
            print("Lista zadań:")
            for i, zadanie in enumerate(zadania, start=1):
                print(f"{i}. {zadanie}")
    elif wybór == "3":
        if len(zadania) == 0:
            print("Nie ma co usuwać")
        else:
            print("Lista zadań:")
            for i, zadanie in enumerate(zadania, start=1):
                print(f"{i}. {zadanie}")
            indeks = int(input("Podaj numer zadania do usunięcia: "))
            if 1 <= indeks <= len(zadania):
                zadania.pop(indeks - 1)
            else:
                print("Niepoprawny numer zadania.")
    elif wybór == "4":
        print("Liczba zadań:", len(zadania))
    elif wybór == "0":
        print("Do widzenia!")
        break
