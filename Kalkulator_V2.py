def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnożenie(a, b):
    return a * b
def dzielenie(a, b):
    return a / b
def potęgowanie(a, b):
    return a ** b
def średnia(liczby):
    return sum(liczby) / len(liczby)
def wyświetl_menu():
    print("==== Menu ====")
    print("1 - Dodawanie")
    print("2 - Odejmowanie")
    print("3 - Mnożenie")
    print("4 - Dzielenie")
    print("5 - Potęgowanie")
    print("6 - średnia")
    print("0 - Koniec")
def main():
    wyświetl_menu()
    while True:
        wybór = input("Co liczymy")
        if wybór == "0":
            print("Koniec")
            break
        elif wybór in ["1", "2", "3", "5"]:
            a = int(input("Podaj liczbe 1: "))
            b = int(input("Podaj liczbe 2: "))
            if wybór == "1":
                wynik = dodawanie(a, b)
                print(f"Wynik dodawania: {wynik}")
            elif wybór == "2":
                wynik = odejmowanie(a, b)
                print(f"Wynik odejmowania: {wynik}")
            elif wybór == "3":
                wynik = mnożenie(a, b)
                print(f"Wynik mnożenia: {wynik}")
            elif wybór == "5":
                wynik = potęgowanie(a, b)
                print(f"Wynik potęgowania: {wynik}")
        elif wybór == "4":
            a = int(input("Podaj licznik: "))
            b = int(input("POdaj mianownik: "))
            wynik = dzielenie(a, b)
            print(f"Wynik dzielenia: {wynik}")
        elif wybór == "6":
            liczby = []
            decyzja = "t"
            while decyzja == "t":
                liczba = int(input("Podaj liczbe: "))
                liczby.append(liczba)
                decyzja = input("Podajesz kolejna (t/n): ")
            wynik = średnia(liczby)
            print(f"Średnia z liczb {liczby} to: {wynik}")


if __name__ == "__main__":
    main()