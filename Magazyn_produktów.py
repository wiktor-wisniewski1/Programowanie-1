magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2,}
while True:
    print("Menu:")
    print("1. Stan magazynu")
    print("2. Przyjęcie towaru")
    print("3. Wydanie towaru")
    print("0. Zakończ")
    wybór = input("Wybierz opcję: ")
    if wybór == "1":
        print("Stan magazynu:")
        for produkt, ilość in magazyn.items():
            print(f"{produkt}: {ilość} szt.")
    if wybór == "2":
        produkt = input("Nazwa produktu: ")
        ilość = int(input("Ilość: "))
        if produkt in magazyn:
            magazyn[produkt] += ilość
        elif produkt not in magazyn:
            magazyn[produkt] = ilość
    if wybór == "3":
        produkt = input("Nazwa produktu: ")
        ilość = int(input("Ilość: "))
        if produkt in magazyn:
            if magazyn[produkt] >= ilość:
                magazyn[produkt] -= ilość
            else:
                print("Nie ma wystarczającej ilości towaru w magazynie.")
        else:
            print("Produkt nie istnieje w magazynie.")
    if wybór == "0":
        print("Do widzenia!")
        break