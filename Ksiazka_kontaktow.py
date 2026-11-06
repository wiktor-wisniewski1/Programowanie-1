ksiazka_kontaktow = {}

while True:
    print("\n========== KSIAZKA KONTAKTOW ==========")
    print("1. Dodaj kontakt")
    print("2. Wyswietl wszystkie kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Edytuj kontakt")
    print("5. Usun kontakt")
    print("0. Zakoncz")
    print("=======================================")

    wybor = input("Wybierz opcje: ").strip()

    if wybor == "0":
        print("\nDziękuję za skorzystanie z książki kontaktów. Do widzenia!")
        break

    elif wybor == "1":
        telefon = input("Podaj numer telefonu: ").strip()
        if telefon in ksiazka_kontaktow:
            print("Błąd: Kontakt o takim numerze telefonu już istnieje!")
        else:
            imie = input("Podaj imię: ").strip()
            nazwisko = input("Podaj nazwisko: ").strip()
            ksiazka_kontaktow[telefon] = [imie, nazwisko]
            print(f"Pomyślnie dodano kontakt: {imie} {nazwisko} ({telefon})")

    elif wybor == "2":
        if not ksiazka_kontaktow:
            print("Książka kontaktów jest pusta.")
        else:
            print("\nLista kontaktów:")
            for telefon, dane in ksiazka_kontaktow.items():
                print(
                    f"Telefon: {telefon} | Imię: {dane[0]} | Nazwisko: {dane[1]}"
                )

    elif wybor == "3":
        telefon = input("Podaj numer telefonu do wyszukania: ").strip()
        if telefon in ksiazka_kontaktow:
            dane = ksiazka_kontaktow[telefon]
            print(
                f"Znaleziono kontakt -> Imię: {dane[0]}, Nazwisko: {dane[1]},"
                f" Telefon: {telefon}"
            )
        else:
            print("Nie znaleziono kontaktu o podanym numerze.")

    elif wybor == "4":
        telefon = input(
            "Podaj numer telefonu kontaktu do edycji: "
        ).strip()
        if telefon in ksiazka_kontaktow:
            print(
                f"Obecny kontakt: {ksiazka_kontaktow[telefon][0]}"
                f" {ksiazka_kontaktow[telefon][1]}"
            )
            nowe_imie = input("Podaj nowe imię: ").strip()
            nowe_nazwisko = input("Podaj nowe nazwisko: ").strip()
            ksiazka_kontaktow[telefon] = [nowe_imie, nowe_nazwisko]
            print("Kontakt został pomyślnie zaktualizowany.")
        else:
            print("Nie znaleziono kontaktu o podanym numerze.")

    elif wybor == "5":
        telefon = input(
            "Podaj numer telefonu kontaktu do usunięcia: "
        ).strip()
        if telefon in ksiazka_kontaktow:
            usuniety = ksiazka_kontaktow.pop(telefon)
            print(
                f"Usunięto kontakt: {usuniety[0]} {usuniety[1]} (Tel:"
                f" {telefon})"
            )
        else:
            print("Nie znaleziono kontaktu o podanym numerze.")

    else:
        print("Nieznana opcja! Wybierz numer od 0 do 5.")