def selection_sort(array):
     for i in range(len(array)):
          min_value = min(array[i:])
          min_index = array.index(min_value)
          if array[i] > min_value:
               array[i], array[min_index] = array[min_index],array[i]

array = [9,8,6,2,1,0]
selection_sort(array)
print(array)