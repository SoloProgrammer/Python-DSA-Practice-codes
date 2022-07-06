# arr = [22,874678,34,1,9,0,14,5]

# for j in range(len(arr)):
#     for i in range(len(arr) - 1):
#         if(arr[i] > arr[i + 1]):
#             arr[i],arr[i + 1] = arr[i + 1],arr[i]

# print(arr)

arr = [9,2,34,12,1,0,8]

for i in range(len(arr)):

    # min_num = min(arr[i:])....// with minimun in build function of python..
   min_ind = i

   for j in range(i + 1,len(arr)):
        if(arr[j] < arr[min_ind]):
            min_ind = j

   if(arr[i] > arr[min_ind]):
        arr[i],arr[min_ind] = arr[min_ind],arr[i]

print(arr)
