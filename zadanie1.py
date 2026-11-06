cena = int(input('Podaj cenę produktu: '))
ilosc = int(input('Podaj ilość: '))
wartosc = cena * ilosc

print('Wartość produktów:', wartosc, 'zł')
if wartosc > 100:
    koszt_dostawy = 0
else:
    koszt_dostawy = 12

zaplata = wartosc + koszt_dostawy

print('Koszt dostawy:', koszt_dostawy, 'zł')
print('Do zapłaty:', zaplata, 'zł')

