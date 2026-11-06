czas = input("Ile godzin będziesz tu stać (h): ")
print("Czas postoju:", czas, "godzin")
if int(czas) <= 1:
    print("Płacisz 5 zł")
elif int(czas) <= 3:
    print("Płacisz 12 zł")
elif int(czas) <= 5:
    print("Płacisz 20 zł")
else:
    print("Płacisz 30 zł")





