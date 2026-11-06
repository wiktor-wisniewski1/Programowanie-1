wiek = input("Podaj wiek: ")
zgoda = input("Czy masz zgodę rodziców? (tak/nie): ")
dokument = input("Czy masz dokument tożsamości? (tak/nie): ") 
if int(wiek) >= 18 and dokument.lower() == "tak":
    print("Wypożyczenie możliwe")
elif int(wiek) < 18 and zgoda.lower() == "tak" and dokument.lower() == "tak":
    print("Wypożyczenie możliwe")
else:
    print("Wypożyczenie niemożliwe")
