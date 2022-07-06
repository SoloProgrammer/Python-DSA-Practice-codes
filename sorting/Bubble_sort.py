from multiprocessing.dummy import Array

from sklearn.metrics import consensus_score


temp = []

def func(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                # temp = arr[i + 1]
                # arr[i + 1] = arr[i]
                # arr[i] = temp
                arr[i+1],arr[i] = arr[i],arr[i + 1]
    
    return arr


arr = [2,4,3,6,5,9,8,10,99,34,67,44,1,0]
Sorted_array = func(arr)
# print(Sorted_array)

str = "pratham"

print(str.capitalize())



# num = numbers.split(" ")
# for i in range(len(num)):
#     num[i] = int(num[i])