from re import A


arr = [9,0,1,23,45,5,3,6]

print(arr)

for j in range(len(arr)):
    for i in range(len(arr) - 1):
        if(arr[i] > arr[i + 1]):
            arr[i],arr[i + 1] = arr[i + 1],arr[i]
    print(arr)

print(arr)
