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

# print a Digital root of number  - input has to be taken from user  // using recursive function...................................


print("Digital root code")

def digi_root(provided_num):
    root = 0
    while(provided_num > 0):
        root += provided_num % 10
        provided_num = provided_num //10
    
    if(root > 10):
        digi_root(root)
    else:
        print(root)

digi_root(int(input("Enter number of which you want Digital root : ")))


# print reversed of string  - input has to be taken from user  // using recursive function...................................


def reverse_string(original_str,reverse_str = ""):
    while(len(original_str) > 0):
        reverse_str += original_str[len(original_str) - 1]
        original_str = original_str[:len(original_str) - 1]
        reverse_string(original_str,reverse_str)
    return reverse_str



print(reverse_string(input("Enter the String to reversed it : ")))

# print reversed of list items  - input has to be taken from user  // using recursive function...................................

def reversed_list(list1,result = []):
    if(len(list1) > 0):
        result.append(list1[len(list1) - 1])
        list1 = list1[:len(list1) - 1]
        reversed_list(list1,result)

    return result

list1 = []
n = int(input("how many numbers do you want to insert in a list :"))
for i in range(1,n + 1):
    list1.append(int(input(f"Enter num {i} :")))

print(reversed_list(list1))