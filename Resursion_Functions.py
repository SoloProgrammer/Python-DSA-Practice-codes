# print a table of num - input taken from user // using recursive function...........................................

def print_table(num,i):
    Result = num * i
    print(f"{num} x {i} = {Result}")
    i += 1

    if(i <= 10):
        print_table(num,i) ## Calling parent function until a contodion satisfies called resursive function...
    
    if(i > 10):

        print("\n1.Enter (1) for Exit")
        print("2.Enter (2) for back again \n")

        user_inpt = int(input("Enter Your Choice :"))

        if user_inpt == 2:
            i = 1
            print_table(int(input("Enter num of which you want to print the table: ")),i)
        elif user_inpt == 1:
            print("\nThanks for using us..............................................\n")
            exit()


print_table(int(input("Enter num of which you want to print the table: ")),1)


# print a Fibbonacci series upto n numbes - input has to be taken from user  // using recursive function...................................

fibbo_list = [] 
def Fibbo_series(n,t1,t2):
    fibbo_num = t1 + t2
    fibbo_list.append(fibbo_num)

    t1 = t2
    t2 = fibbo_num
    n -= 1

    if(n > 0):
        Fibbo_series(n,t1,t2)

    return fibbo_list

fibbo_list = Fibbo_series(int(input("Enter upto which you want to print Fibbonacci Series : ")),-1,1)

print(fibbo_list)


# print a Factorial of  n number  - input has to be taken from user  // using recursive function...................................

def fact(num):
    fact1 = 1
    if(num > 0):
        fact1 = num * fact(num - 1)
        print(fact1)

    return fact1

    
print_table(fact(int(input("Enter num of which you want to print the Factorial : "))))

