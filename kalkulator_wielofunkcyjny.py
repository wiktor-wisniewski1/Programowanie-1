while True:
    print("=====KALKULATOR===")
    print("1. Dodoawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Średnia z podanych liczb")
    print("0. Zakończ")
    print("===================")
    wybor = input("Wybierz opcje: ")

    if wybor == "0":
        print("Koniec")
        break
    
    elif wybor == "1":
        liczba_1 = int(input("liczba 1: "))
        liczba_2 = int(input("liczba 2: "))
        wynik = liczba_1 + liczba_2
        print("Wynik: ", wynik)
    
    elif wybor == "2":
        liczba_1 = int(input("liczba 1: "))
        liczba_2 = int(input("liczba 2: "))
        wynik = liczba_1 - liczba_2
        print("Wynik: ", wynik)
    elif wybor == "3":
        liczba_1 = int(input("liczba 1: "))
        liczba_2 = int(input("liczba 2: "))
        wynik = liczba_1 * liczba_2
        print("Wynik: ", wynik)
    elif wybor == "4":
        liczba_1 = int(input("liczba 1: "))
        liczba_2 = int(input("liczba 2: "))
        if liczba_2 == 0:
            print("Nie dzieli się przez 0")
           
        wynik = liczba_1 / liczba_2
        print("Wynik: ", wynik)
    elif wybor == "5":
        liczba_1 = int(input("liczba 1: "))
        liczba_2 = int(input("liczba 2: "))
        wynik = liczba_1 ** liczba_2
        print("Wynik: ", wynik)
    
    elif wybor == "6":
        ile = int(input("Podaj liczbę elementów: "))
        if ile <= 0:
            print("Błąd: Liczba elementów musi być dodatnia.")
        else:
            suma = 0
            for i in range(ile):
                    liczba = float(input(f"Podaj liczbę {i + 1}: "))
                    suma += liczba
            wynik = suma / ile
            dzialanie = f"Średnia z {ile} liczb = {wynik}"
            print(f"Średnia: {wynik}")