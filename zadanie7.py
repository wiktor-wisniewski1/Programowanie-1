kwota_oszczedzanie = float(input("Podaj ile tygodniowo odkładasz: "))
ilosc_tygodni = int(input("Ile tygodni chcesz oszczędzać: "))
kwota_po = 0

for tydzien in range(0, ilosc_tygodni):
    kwota_po =  kwota_po + kwota_oszczedzanie
    print(f"Po {tydzien + 1} tygodniu masz: {kwota_po:.2f} zł")

print(f"Łączne oszczędnoci to: {kwota_po:.2f} zł") 