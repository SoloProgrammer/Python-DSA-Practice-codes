#  remove prime no from arraylist || String sand arrays


list1 = [12,22,33,5,6,8,13,23,24,11,86]

prime = []
notprime = []

for item in list1:
    for i in range(2, item + 1):
        if item % i == 0:
            if i == item:
                prime.append(item)
                break
            else:
                notprime.append(item)
                break

    

print("\nhere is given list " + str(list1))

print(" \nprime no are - " + str(prime))


print( " \nhere are non-prime no - " + str(notprime))

