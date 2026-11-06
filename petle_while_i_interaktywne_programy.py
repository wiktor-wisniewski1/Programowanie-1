napoje = ["cola", "fanta", "sprite", "woda", "sok"]
ceny = [5, 4, 4, 3, 6]
wybrane_ceny = []
print("Dostępne napoje:")
for i in range(len(napoje)):
        print(f"{i + 1}. {napoje[i]} - {ceny[i]} zł")
while True: 
    wybor = input("Wybierz napój (1-5) lub '0', aby zakończyć: ")
    
    if wybor == '0':
        print("Koniec zakupów.")
        print("łączna kwota do zapłaty:", sum(wybrane_ceny), "zł")
        break
    elif wybor in ['1', '2', '3', '4', '5']:
        index = int(wybor)
        print(f"Wybrałeś {napoje[index - 1]} za {ceny[index - 1]} zł.")
        wybrane_ceny.append(ceny[index - 1])
    else:
        print("Nieprawidłowy wybór.")