name = " "
while True:
    print("Kim jestes?")
    name = input()
    if name != "Janek":
        continue
    print("Witaj Janek podaj swoje hasło...(rybka)")
    password = input()
    if password == "rybka":
        break
print("milego dnia dziekuje")



