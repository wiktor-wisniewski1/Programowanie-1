wysokosc = input("Jak ma być wysokość choinki")
wysokosc = int(wysokosc)

for i in range(1, wysokosc + 1):
    print(" " * (wysokosc - i) + "*" * (2 * i - 1))

