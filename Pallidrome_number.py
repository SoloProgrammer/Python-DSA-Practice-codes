num = int(input("Enter number to check it is palidrome or not : "))

original_num = num

reversed_num = 0

while num != 0:
    n = num % 10
    reversed_num = reversed_num * 10 + n
    num = num//10

if(reversed_num == original_num):
    print(f"{original_num} is a Pallidrome number ")
else:
    print(f"{original_num} is not a Pallidrome number ")




