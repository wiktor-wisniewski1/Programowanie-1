temperatura = float(input("Podaj temperaturę w stopniach Celsjusza: "))
czy_ktoś_jest_w_domu = input("Czy ktoś jest w domu? (tak/nie): ")
czy_okna_sa_otwarte = input("Czy okna są otwarte? (tak/nie): ")

if  czy_okna_sa_otwarte.lower() == "tak":
    print("Ogrzeawnnie wyłączone")
    print("Powód: okna są otwarte")
elif temperatura < 20 and czy_ktoś_jest_w_domu.lower() == "tak":
    print("Ogrzewanie włączone")
    print("Powód: ktoś jest w domu i temperatura mniejsza niż 20 stopni")
elif temperatura < 16 and czy_ktoś_jest_w_domu.lower() == "nie" and czy_okna_sa_otwarte.lower() == "nie":
    print("Ogrzewanie włączone")
    print("Powód: Mimo że nikogo nie ma w domu, włączone ponieważ temperatura jest niższa niż 16 stopni")
else:
    print("Ogrzewanie wyłączone")
    print("Powód: temperatura jest wystarczająca lub nikogo nie ma w domu")
    