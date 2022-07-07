
Given_array_list= [9,2,3,1,12,34,55,78,92,99]

for num in Given_array_list:
    for i in range(2,num):
        
        if num % i == 0:
            print(f"{num} is a prime number.. Bcz it is Divisible by {i}")
            break
        
        if(i == num - 1):
            print(f"{num} is not a prime number..")