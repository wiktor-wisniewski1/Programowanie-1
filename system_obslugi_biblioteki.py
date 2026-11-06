biblioteka = []

while True:
    print("\n========== BIBLIOTEKA ==========")
    print("1. Dodaj ksiazke")
    print("2. Wyswietl wszystkie ksiazki")
    print("3. Wypozycz ksiazke")
    print("4. Zwroc ksiazke")
    print("5. Usun ksiazke")
    print("0. Zakoncz")
    print("================================")
    
    wybor = input("Wybierz opcje: ")

    if wybor == "1":
        biblioteka.append({"tytul": input("Tytuł: "), "autor": input("Autor: "), "dostepna": True})
    elif wybor == "2":
        for i, k in enumerate(biblioteka, 1):
            print(f"{i}. {k['tytul']} - {k['autor']} | {'Dostępna' if k['dostepna'] else 'Wypożyczona'}")
    elif wybor == "3":
        biblioteka[int(input("Numer: ")) - 1]["dostepna"] = False
    elif wybor == "4":
        biblioteka[int(input("Numer: ")) - 1]["dostepna"] = True
    elif wybor == "5":
        biblioteka.pop(int(input("Numer: ")) - 1)
    elif wybor == "0":
        break