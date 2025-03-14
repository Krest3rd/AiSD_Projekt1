from datetime import date

import generators as gen

def Menu():
    T=[]
    print("Witaj zanim zaczniesz sortować wygeneruj tablicę.")
    while True:
        op = input("1) Wygeneruj tablicę \n2) Posortuj tablicę \n3) Wyjdź \n")
        match op:
            case "1":
                T = TableGenerator()
            case "2":
                # Sorting(T)
                print("Not ready")
            case "3":
                break
            case _:
                print("Nie prawidłowy wybór")
    print("Żegnaj")


def TableGenerator():
    while True:
        n = -1
        while n <=0:
            n = int(input("Podaj długość tablicy: "))

        match input("Wybierz algorytm: \n 1) Losowa \n 2)Rosnąca \n 3)Malejąca \n 4)Stała \n 5) A-kształtna\n"):
            case "1":
                T = gen.RandTable(n)
                print(T)
                return T
            case "2":
                T = gen.IncTable
                print(T)
                return T
            case "3":
                T = gen.DecTable(n)
                print(T)
                return T
            case "4":
                T = gen.SetTable(n)
                print(T)
                return T
            case "5":
                T = gen.AshapeTable(n)
                print(T)
                return T
            case _:
                print("Zły wybór")