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
    przyrost = 0
    while przyrost < length:
        przyrost = (4**k)+(3*2**(k-1))+1
        k += 1

    while k >= 0:
        insertion_sort(arr,przyrost)
        k -= 1
        przyrost = (4**k)+(3*2**(k-1))+1
    return arr

        # for i in range(0,przyrost):
        #     temp = insertion_sort(arr[i:length:przyrost])
        #     l = i
        #     for j in temp:
        #         T[l] = j
        #         l += przyrost


# def quick_sort_left(...):
#     def pivot_left(arr, l ,h):
#         return arr[l]
#     quick_sort(..., pivot_left)
#     quick_sort(..., lambda arr, l ,p : arr[l])
    

def quick_sort(arr,p,r,piv_func):
    if p<r:
        q=partition(arr,p,r,piv_func)#,pivot_f
        quick_sort(arr,p,q-1,piv_func)#,pivot_f
        quick_sort(arr,q+1,r,piv_func)#,pivot_f
    return arr

def partition(arr,p,r,piv_func):#,pivot_f):
    pivot=piv_func(arr,p,r) #pivot_f
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

def quick_sort_left(arr,p,r):
    return quick_sort(arr,p,r,lambda arr,p,r: arr[p])

def quick_sort_rand(arr,p,r):
    def rand_p(arr,p,r):
        q= randint(p,r)
        arr[p],arr[q]=arr[q],arr[p]
        return arr[p]
    return quick_sort(arr,p,r,rand_p)

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


T = [123,123,131,23,52,1,352,1,2352,1867]
print(quick_sort_rand(T,0,len(T)-1))