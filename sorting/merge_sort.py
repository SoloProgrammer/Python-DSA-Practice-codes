
def merge(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merge(left_list)
        merge(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] > right_list[j]:
                list1[k] = right_list[j]
                j += 1
                k += 1
                print(list1)
            else:
                list1[k] = left_list[i]
                i += 1
                k += 1
                print(list1)
        # print("len of rl : " + str(len(right_list)))
        # print("len of ll : " +str(len(left_list)))

        
        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1
            print(list1)

        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1
            print(list1)

    return list1


num = int(input("Enter How Many elements do you want in list : "))
list1 = [int(input(f"Enter item {i + 1} in list : " )) for i in range(num)] 

print(merge(list1))