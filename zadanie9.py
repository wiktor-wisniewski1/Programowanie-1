start = input("Podzaj początek zakresu: ")
koniec = input("Podaj koniec zakresu: ")
for x in range(int(start), int(koniec)+1):
    if x % 2 == 0:
        print(str(int(x)) + " - liczba parzysta")
    else:
        print(str(int(x)) + " - liczba nieparzysta")

print("Ilość liczb parzystych:" + str(len([x for x in range(int(start), int(koniec)+1) if x % 2 == 0])))
print("Ilość liczb nieparzystych:" + str(len([x for x in range(int(start), int(koniec)+1) if x % 2 != 0])))