num_to_search = 12

# Linear search...............................................................................................

arr1 = [9,3,1,2,6,5,3,8,7]

for index in range(len(arr1)):
    if(arr1[index] == num_to_search):
        print(f"the num to seacrh i.e number { num_to_search } is found at index { index}")
        break;
    else:
     if(index == len(arr1) - 1):   
            print(f"{num_to_search } is not present in array { arr1 }")
    
# Binary search...............................................................................................

arr = [1, 2, 3, 5, 6, 7, 8 ,10 ,11,12]

def find_num(low,high):
    mid = (low + high)//2
    if(arr[mid] > num_to_search):
        find_num(low,mid)
    elif(arr[mid] == num_to_search):
        print(f"no found at position {mid} of array {arr}")
    elif(arr[mid] == arr[len(arr) - 2]):
        print(f"{num_to_search}  is found at position {len(arr) - 1} array {arr}")
    elif(arr[mid] < num_to_search):
        find_num(mid,high)


low = 0
high = len(arr) - 1

find_num(low,high)