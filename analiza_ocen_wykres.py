import matplotlib.pyplot as plt


punkty = []
nazwiska = []
oceny = []

ilosc = int(input("Podaj ilość studentów: "))

for i in range(ilosc):
    nazwisko = input(f"Podaj nazwisko osoby {i + 1}: ")
    punkt = int(input(f"Podaj punkty osoby {i + 1}: "))
    if punkt < 0 or punkt > 100:
        print("błąd")
    elif punkt >= 90:
        ocena = 5.0
    elif punkt >= 80:
        ocena = 4.5
    elif punkt >= 70:
        ocena = 4.0
    elif punkt >= 60:
        ocena = 3.5
    elif punkt >= 50:
        ocena = 3.0
    elif punkt <= 49:
        ocena = 2.0
    nazwiska.append(nazwisko)
    punkty.append(punkt)
    oceny.append(ocena)

for n, o in zip(nazwiska, oceny):
    print(f"{n} {o}")

średnia = sum(oceny) / len(oceny)
zaliczenia = sum(1 for o in oceny if o >= 3.0)
print(f"Średnia ocen: {średnia}")
print(f"Liczba zaliczeń: {zaliczenia}")
print("Generowanie wykresu...")

def rysuj_wykres(nazwiska, oceny):
    import matplotlib.pyplot as plt
    plt.bar(nazwiska, oceny)
    plt.xlabel("Nazwiska")
    plt.ylabel("Oceny")
    plt.title("Analiza ocen studentow")
    plt.show()

rysuj_wykres(nazwiska, oceny)