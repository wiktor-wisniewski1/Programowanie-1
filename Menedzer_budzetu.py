operacje = []

while True:
    print("\n========= MOJ BUDZET =========")
    print("1. Dodaj przychod")
    print("2. Dodaj wydatek")
    print("3. Wyswietl historie operacji")
    print("4. Wyswietl stan konta")
    print("5. Podsumowanie finansowe")
    print("6. Wyszukaj operacje")
    print("7. Usun operacje")
    print("0. Zakoncz")
    print("===============================")

    wybor = input("Wybierz opcje: ")

    if wybor =="1":
        opis = input("Podaj opis: ")
        kwota = float(input("Podaj kwote: "))
        operacje.append({"typ": "przychód", "opis": opis, "kwota": kwota})
        print("Dodano przychód.")
    elif wybor == "2":
        opis = input("Podaj opis: ")
        kwota = float(input("Podaj kwotę: "))
        operacje.append({"typ": "wydatek", "opis": opis, "kwota": kwota})
        print("Dodano wydatek.")
    elif wybor == "3":
        if not operacje:
            print("Brak operacji w historii.")
        else:
            print("--- HISTORIA OPERACJI ---")
            for i, op in enumerate(operacje, 1):
                print(f"{i}. [{op['typ'].upper()}] {op['opis']} - {op['kwota']:.2f} zł")  
    elif wybor == "4":
        bilans = sum(op['kwota'] if op['typ'] == 'przychód' else -op['kwota'] for op in operacje)
        print(f"\nAktualny stan konta: {bilans:.2f} zł")

    elif wybor == "5":
        if not operacje:
            print("Brak operacji do podsumowania.")
        else:
            suma_przychodow = sum(op['kwota'] for op in operacje if op['typ'] == 'przychód')
            suma_wydatkow = sum(op['kwota'] for op in operacje if op['typ'] == 'wydatek')
            bilans = suma_przychodow - suma_wydatkow

            wydatki = [op for op in operacje if op['typ'] == 'wydatek']
            if wydatki:
                najwiekszy_wydatek = max(wydatki, key=lambda x: x['kwota'])
                info_wydatek = f"{najwiekszy_wydatek['opis']} ({najwiekszy_wydatek['kwota']:.2f} zł)"
            else:
                info_wydatek = "Brak wydatków w historii."

            print("\n--- PODSUMOWANIE FINANSOWE ---")
            print(f"Suma przychodów: {suma_przychodow:.2f} zł")
            print(f"Suma wydatków: {suma_wydatkow:.2f} zł")
            print(f"Bilans: {bilans:.2f} zł")
            print(f"Największy wydatek: {info_wydatek}")

    elif wybor == "6":
        if not operacje:
            print("Brak operacji do przeszukania.")
        else:
            fraza = input("Podaj frazę do wyszukania w opisie: ").lower()
            znalezione = [op for op in operacje if fraza in op['opis'].lower()]
            
            if znalezione:
                print(f"\nZnaleziono {len(znalezione)} operacji:")
                for op in znalezione:
                    print(f"- [{op['typ'].upper()}] {op['opis']} - {op['kwota']:.2f} zł")
            else:
                print("Nie znaleziono operacji pasujących do frazy.")

    elif wybor == "7":
        if not operacje:
            print("Brak operacji do usunięcia.")
        else:
            print("\n--- HISTORIA OPERACJI ---")
            for i, op in enumerate(operacje, 1):
                print(f"{i}. [{op['typ'].upper()}] {op['opis']} - {op['kwota']:.2f} zł")

            nr = int(input("Podaj numer operacji do usunięcia: "))
            usunieta = operacje.pop(nr - 1)
            print(f"Usunięto operację: [{usunieta['typ'].upper()}] {usunieta['opis']} - {usunieta['kwota']:.2f} zł")

    elif wybor == "0":
        print("Koniec.")
        break
    else:
        print("Nieprawidłowa opcja menu.")