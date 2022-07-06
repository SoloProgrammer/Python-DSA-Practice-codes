###############################         with ......................min_val
# list1 = [3,5,1,6,7,0]

# for i in range(len(list1)):
#     min_val = list1[i]

#     for j in range(i+1,len(list1)):
#         if min_val > list1[j]:
#             min_val = list1[j]

            
#     min_ind = list1.index(min_val)

#     list1[i], list1[min_ind] = list1[min_ind],list1[i]


# print(list1)

###############################         with ......................min_index


list1 = [3,5,1,6,7,0]

for i in range(len(list1)):

    min_ind = i

    for j in range(i+1,len(list1)):
        if list1[min_ind] > list1[j]:
            min_ind = j

    
    list1[i], list1[min_ind] = list1[min_ind],list1[i]


print(list1)

