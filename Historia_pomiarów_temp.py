temperatura = []
ilosc_pomiarow = int(input("Podaj ilość pomiarów temperatury: "))
for i in range(ilosc_pomiarow):
    temp = float(input("Podaj temperaturę: "))
    temperatura.append(temp)
print()
print(f"Pierwszy pomiar: {temperatura[0]}")
print(f"Ostatni pomiar: {temperatura[-1]}")
if len(temperatura) >= 6:
    print(f"Pierwsze 3 {temperatura[:3]}")
    print(f"Ostatnie 3 {temperatura[-3:]}")
else:
    print(temperatura)
print(f"Co 2 pomiar: {temperatura[::2]}")
print(f"Odwrócona lista: {temperatura[::-1]}")
print(f"Orginał: {temperatura}")
kopia = temperatura.copy()
kopia[0] = 0
print(f"Kopia po zmianie: {kopia}")

