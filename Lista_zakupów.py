lista = []
zakupy = int(input("Wprowadz ilość produktów: "))
for i in range(zakupy):
    produkt = input("Podaj nazwe produktu: ")
    lista.append(produkt)

print("Lista:", lista)
print(len(lista))

usuwanie = input("Podaj nazwe produktu do usunięcia: ")
if usuwanie.lower() in lista:
    lista.remove(usuwanie)

print("Nowa lista:", lista)

