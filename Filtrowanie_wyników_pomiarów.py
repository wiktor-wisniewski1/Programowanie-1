próg_alarmowy = 50
pomiary = []
ilość_pomiarów = int(input("Podaj ilość pomiarów: "))
for i in range(ilość_pomiarów):
    pomiar = float(input(f"Podaj pomiar {i + 1}: "))
    pomiary.append(pomiar)
alarmowe = [i for i in pomiary if i > próg_alarmowy]
print(f"Pomiary alarmowe: {alarmowe}")
print(f"Pomiary pomnożone przez 2: {[pomiar * 2 for pomiar in pomiary]}")
print(f"Czy wystąpił alarm? {any(pomiar > próg_alarmowy for pomiar in pomiary)}")
print(f"Czy wszystkie pomiary są prawidłowe? {all(pomiar > 0 for pomiar in pomiary)}")

