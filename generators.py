from random import randint

def RandTable(n):
    T = [0]*n
    for i in range(n):
        T[i] = randint(0,n)
    
    return T

def SetTable(n):
    T = [randint(0,n)]*n
    return T

def IncTable(n):
    T = [0]*n
    T[0] = randint(0,n)
    for i in range(1,n):
        T[i] = T[i-1] + randint(1,10)

    return T

def DecTable(n):
    return IncTable(n)[::-1]

def AshapeTable(n):
    T = IncTable(n)
    if n%2:
        return T[::2]+T[-2::-2]
    else:
        return T[::2]+T[-1::-2]

# print(RandTable(200))
