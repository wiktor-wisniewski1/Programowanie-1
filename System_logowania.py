hasło = "Python123"
próby = 0
while True:
    
    wpisane_hasło = input("Wprowadź hasło: ")
    if wpisane_hasło == hasło:
        print("Hasło poprawne")
        break
    elif wpisane_hasło != hasło: 
        print("Niepoprawne hasło, spróbuj ponownie.")
        próby += 1
        print(f"Pozostało prób: {próby}")
        if próby >= 3:
            print("Konto zablokowane")
            break