import generators as gen
import sorters as sort

def Menu():
    # First menu
    T=[]
    print("Witaj zanim zaczniesz sortować wygeneruj tablicę.")
    while True:
        op = input("1) Wygeneruj tablicę \n2) Posortuj tablicę \n3) Wyjdź \n")
        match op:
            case "1":
                T = TableGenerator()
            case "2":
                Sorting(T)
                # print("Not ready")
            case "3":
                break
            case "4":
                print("Gratulacje użytkowniku! Zostałeś wybrany jako dzisiejszy zwycięzca darmowego ajfoą 6s, playstation 4 lub samsung galaxy s6")
            case _:
                print("Nie prawidłowy wybór")
    print("Bye bye")

#Person below me is gya
#*gay

def TableGenerator():
    # Meni do wyboru generatora tablicy
    while True:
        n = -1
        while n <=0:
            n = int(input("Podaj długość (liczba Naturalna dodatnia) tablicy: "))

        match input("Wybierz rodzaj: \n 1) Losowa \n 2) Rosnąca \n 3) Malejąca \n 4) Stała \n 5) A-kształtna\n "):
            case "1":
                T = gen.RandTable(n)
                print(T)
                return T
            case "2":
                T = gen.IncTable(n)
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

def Sorting(arr):
    # Menu do wyboru algorytmu sortowania
    while True:
        T = [i for i in arr]
        print("Przed sortowaniem:\n",arr)
        match input("Wybierz algorytm: \n 1) Selection \n 2) Insertion \n 3) Bubble \n 4) Heap \n 5) Quick(lewy)\n 6) Quick(losowy) \n 7) Shell \n q) Wróć\n"):
            case "1":
                T = sort.selection_sort(T)
            case "2":
                T = sort.insertion_sort(T)
            case "3":
                T = sort.bubble_sort(T)
            case "4":
                T = sort.heap_sort(T)
            case "5":
                T = sort.quick_sort(T,0,len(T)-1)
            case "6":
                T = sort.quick_sort(T,0,len(T)-1,True)
            case "7":
                T = sort.shell_sort(T)
            case "q":
                break
            case _:
                print("Zły wybór")
        print("Po sortowaniu:\n",T)

def AlgSelect(arr,n):
    T =[]
    match n:
        case "1":
            T = sort.insertion_sort(arr)
        case "2":
            T = sort.shell_sort(arr)
        case "3":
            T = sort.selection_sort(arr)
        case "4":
            T = sort.heap_sort(arr)
        case "5":
            T = sort.quick_sort(arr,0,len(arr)-1)
        case "6":
            T = sort.quick_sort(arr,0,len(arr)-1,random=True)
        case _:
            print("Nieprawidłowa opcja")
    return T