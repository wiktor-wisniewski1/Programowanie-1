temperatury = []
powyzej_sredniej = []
for i in range(7):
    temperatura = float(input(f"Dzień {i+1}: "))
    temperatury.append(temperatura)
srednia = sum(temperatury) / len(temperatury)
print("Średnia", srednia)

for temperatura in temperatury:
    if temperatura > srednia:
        powyzej_sredniej.append(temperatura)
print("Powyżej średniej:", powyzej_sredniej)
print("Ilość dni powyżej średniej:", len(powyzej_sredniej))
print("Najwyższa", max(temperatury), "C")

print("Najniższa", min(temperatury), "C")