from random import randint

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def insertion_sort(arr,gap=1):
    n = len(arr)
    for j in range(gap,n):
        # k = arr[j]
        i = j
        while i >= gap and arr[i-gap] > arr[i]:
            arr[i],arr[i-gap] = arr[i-gap],arr[i]
            # arr[i] = arr[i-gap]
            i = i - gap
        # arr[i] = k
    return arr

def selection_sort(arr):
    n = len(arr) 
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr

def shell_sort(arr):
    length = len(arr)
    k = 1
    Przyrosty = [1]
    while Przyrosty[-1] < length:
        Przyrosty.append((4**k)+(3*2**(k-1))+1)
        k += 1

    for gap in Przyrosty[::-1]:
        insertion_sort(arr,gap)
    return arr

        # for i in range(0,przyrost):
        #     temp = insertion_sort(arr[i:length:przyrost])
        #     l = i
        #     for j in temp:
        #         T[l] = j
        #         l += przyrost


def quick_sort(arr,p,r,random=False):
    if p<r:
        q=q_pivot(arr,p,r,random)
        quick_sort(arr,p,q-1,random)
        quick_sort(arr,q+1,r,random)
    return arr

def q_pivot(arr,p,r,random):
    if random:
        q= randint(p,r)
        arr[p],arr[q]=arr[q],arr[p] #losowy element nie jest ułożony, trzeba go traktowac jak p przy lefcie
    pivot= arr[p]
    i=p+1
    j=r
    while True:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]>pivot:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[p],arr[j]= arr[j],arr[p]
    return j

###

def heap_sort(arr):
    n=len(arr) # czy len kosztuje czas? imo wiecej niz funkcja z przypisana wartoscia
    for i in range (n//2-1,-1,-1): # n//2-1 liczba rodzicow
        heap_sort_helper(arr,n,i) #pierwsze wydobycie maxa
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heap_sort_helper(arr,i,0) #kopanie maxow
    return arr

def heap_sort_helper(arr,n,i):
    maxi= i
    left=2*i+1
    right=2*i+2
    if left<n and arr[maxi]<arr[left]: #w/m
        maxi=left
    if right<n and arr[maxi]<arr[right]: #w/m
        maxi=right
    if maxi!=i:
        arr[i],arr[maxi]=arr[maxi],arr[i]
        heap_sort_helper(arr,n,maxi)
