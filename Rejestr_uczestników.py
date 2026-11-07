warsztat_python = set()
warsztat_ai = set()

while True:
    print("=======Menu=======")
    print()
    print("1 - Zapisz na Python")
    print("2 - Zapisz na AI")
    print("3 - Wyświetl uczestników")
    print("4 - Uczestnicy obu warsztatów")
    print("5 - Wszyscy unikalni uczestnicy")
    print("0 - Zakończ!")
    print()
    print("==================")

    wybór = input("Co byś zrobił? ")

    if wybór == "1":
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        uczestnik = f"{imie} {nazwisko}"
        if uczestnik in warsztat_python:
            print("Jesteś już zapisany na ten warsztat!")
        else:
            warsztat_python.add(uczestnik)
            print("Dodano uczestnika!")
    elif wybór == "2":
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        uczestnik = f"{imie} {nazwisko}"
        if uczestnik in warsztat_ai:
           print("Jesteś już zapisany na ten warsztat!")
        else:
            warsztat_ai.add(uczestnik)
            print("Dodano uczestnika!")
    elif wybór == "3":
        print(f"uczestnicy: {warsztat_python | warsztat_ai}")
    elif wybór == "4":
        print(f"Uczestnicy obu warsztatów: {warsztat_python & warsztat_ai}")
    elif wybór == "5":
        for uczestnik in (warsztat_python | warsztat_ai) - (warsztat_python & warsztat_ai):
            print(f"Unikalny uczestnik: {uczestnik}")
    elif wybór == "0":
        print("Koniec!")
        break
    else:
        print("Masz tylko opcje od 0 do 5")

