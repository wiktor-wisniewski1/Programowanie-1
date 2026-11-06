cena = float(input('Podaj cenę produktu: '))
rabat = int(input('Podaj wartość rbatu (%): '))

kwotarabatu = cena * (rabat/100)
cenapo = cena - kwotarabatu
print('Cena początkowa:', cena, 'zł')
print('Kwota rabatu:', kwotarabatu, 'zł')
print('Cena po rabacie:', cenapo, 'zł')

if rabat >= 20:
    print("Duża promocja")
else:
    print('Standardowa promocja')