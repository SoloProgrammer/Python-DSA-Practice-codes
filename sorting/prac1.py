
temp = []

def func(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
        
    return arr


arr = [2,1,4,3,6,5,9,8,10,99,34,67,44]
Sorted_array = func(arr)
print(Sorted_array)