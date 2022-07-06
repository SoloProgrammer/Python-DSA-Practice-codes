def Insertion_sort(array):
    for i in range(1,len(array)):
        current_element = array[i]
        
        pos = i

        while current_element < array[pos - 1] and pos > 0:
            array[pos] = array[pos - 1]
            pos = pos - 1

        array[pos] = current_element


array = [2,1,5,4,3]
Insertion_sort(array)
print(array)