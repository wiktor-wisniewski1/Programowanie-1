liczba_studentów = int(input("Podaj liczbę studentów: "))
punkty = []
for i in range(liczba_studentów):
    punkty_studenta = int(input("Punkty studenta {}: ".format(i + 1)))
    punkty.append(punkty_studenta)

srednia = sum(punkty) / len(punkty)

print("Średnia ilość punktów:", srednia)
print("Maksymalna ilość punktów:", max(punkty))
print("Minimalna ilość punktów:", min(punkty))
print("Punkty rosnąco:", sorted(punkty))

zaliczenia = []
for i in range(len(punkty)):
    if punkty[i] >= 50:
        zaliczenia.append(punkty[i])

print("ilość zaliczeń:", len(zaliczenia))