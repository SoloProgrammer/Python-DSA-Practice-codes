##############    0 1 1 2 3 5 8 13............ This is called fibbonacci series

numbers_to_print = 8

t1 = -1
t2 = 1

fibbo_num = 0

fibbo_list = []

for i in range(numbers_to_print):
    fibbo_num = t1 + t2
    print(fibbo_num,end = ",")
    fibbo_list.append(fibbo_num)
    t1 = t2
    t2 = fibbo_num

print(" \n " + str(fibbo_list))

