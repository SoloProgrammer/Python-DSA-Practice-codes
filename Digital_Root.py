
def Retrive_root(num):
    sum = 0
    while(num != 0):
        n = num % 10
        sum += n 
        num = num//10
    return sum

num = int(input("Enter number to Know it digital root : "))

D_Root = Retrive_root(num)

if(D_Root >= 10):
   Digital_root = Retrive_root(D_Root)
   print(f"Digital root of {num} is {Digital_root}")
else:
   print(f"Digital root of {num} is {D_Root}")



