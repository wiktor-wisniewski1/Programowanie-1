punkty = int(input('Ile masz punktów: '))

if punkty < 0:
    ocena = 0
elif punkty < 50:
    ocena = 2
elif punkty < 60:
    ocena = 3
elif punkty < 70:
    ocena = 3.5
elif punkty < 80:
    ocena = 4
elif punkty < 90:
    ocena = 4.5
elif punkty <= 100:
    ocena = 5
else:
    ocena = 0

if ocena > 0:
    print('Uzyskana ocena:', ocena)
else:
    print('Błąd')
    
