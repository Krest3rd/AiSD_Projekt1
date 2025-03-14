def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for j in range(1,n):
        k = arr[j]
        i = j-1
        while i >= 0 and arr[i] > k:
            arr[i+1] = arr[i]
            i = i -1
        arr[i+1] = k
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
    n = len(arr)
    T = [0]*n
    k = n//2
    while k > 0:
        for i in range(0,k):
            temp = insertion_sort(arr[i:n:k])
            l = i
            for j in temp:
                T[l] = j
                l += k
        k //=2
    return T

# def Partition_left(arr,start,end):
#     x = arr[start]
#     i = start
#     j = end
#     while True:
#         while arr[i] < x:
#             i += 1
#         while arr[j] > x:
#             j -= 1
#         if i <= j:
#             arr[i],arr[j] = arr[j],arr[i]
#             i += 1
#             j -=1
#         else:
#             return j



# print(Q_sort_left([3, 112, 74, 20, 143, 20, 196, 127, 118, 146, 114, 9, 186, 44, 111, 166, 55, 73, 29, 150, 94, 45, 38, 158, 43, 116, 78, 22, 121, 36, 180, 1, 68, 33, 71, 65, 15, 46, 149, 155, 181, 23, 39, 72, 130, 90, 9, 153, 73, 188, 101, 9, 28, 199, 13, 101, 59, 100, 16, 12, 42, 28, 7, 27, 196, 140, 86, 152, 177, 49, 3, 25, 27, 69, 119, 36, 153, 131, 35, 61, 153, 34, 2, 189, 194, 134, 144, 113, 55, 136, 128, 194, 44, 51, 115, 51, 69, 1, 73, 100, 112, 168, 158, 113, 98, 7, 146, 92, 7, 17, 149, 15, 110, 179, 114, 118, 147, 46, 0, 79, 179, 54, 124, 121, 178, 102, 130, 121, 179, 87, 111, 184, 118, 168, 51, 100, 147, 106, 141, 64, 35, 5, 187, 96, 200, 143, 188, 131, 35, 94, 155, 167, 92, 80, 56, 47, 197, 13, 80, 61, 50, 171, 76, 182, 4, 127, 106, 127, 21, 186, 68, 5, 37, 184, 43, 36, 40, 18, 40, 173, 159, 182, 84, 177, 153, 132, 74, 135, 135, 88, 143, 134, 72, 154, 188, 87, 159, 123, 82, 189]))