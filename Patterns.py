n = int(input("Enter no of rows to print : "))
# pattern 1...........................................

# * 
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,n + 1):
    for j in range(i):
        print("*",end=' ')
    print('\n')

# pattern 2...........................................

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range(1,n + 1):
    for j in range(1,n + 1):
        if(j >= ((n + 1)-i)):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print("\n")

# pattern 3...........................................

# * * * * * *
# * * * * * 
# * * * *   
# * * *     
# * *       
# *

for i in range(1,n + 1):
    for j in range(1,n + 1):
        if(j <= ((n + 1)-i)):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print("\n")


# pattern 4...........................................

#   * * * * * *
#     * * * * *
#       * * * *
#         * * *
#           * *
#             *


for i in range(1,n + 1):
    for j in range(1,n + 1):
        if(j >= i):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print("\n")



# pattern 5...........................................

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *


for i in range(1,n + 1):
    for j in range(1,2*n):
        if(j>=((n + 1) - i) and j <= ((n - 1) + i)):
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print("\n")


# pattern 6...........................................

# * * * * * * * * * * * 
#   * * * * * * * * *   
#     * * * * * * *     
#       * * * * *       
#         * * *
#           *


for i in range(1,n + 1):
    for j in range(1,2*n):
        if(j>=i and j <= ((2*n) - i)):
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print("\n")



# pattern 6...........................................

# * * * * * * 
# *         *
# *         *
# *         *
# *         *
# * * * * * *


for i in range(1,n + 1):
    for j in range(1,n + 1):
        if(i == 1 or j == 1 or i == n or j == n ):
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print("\n")


# pattern 7..........................................

# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1
# 1 0 1 0 1 0

for i in range(1,n + 1):
    for j in range(1,n + 1):
        if(j <= i):
            if(j%2 != 0):
                print("1",end=' ')
            else:
                print("0",end=' ')

        else:
            print(" ",end=' ')

    print('\n')

# pattern 8..........................................

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

for i in range(1,n + 1):
    for j in range(1,n + 1):
        if(j <= i):
           print(j,end=' ')
        else:
            print(" ",end=' ')

    print('\n')

# pattern 9..........................................

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

for i in range(1,n + 1):
    for j in range(1,n + 1):
        if(j <= i):
           print(j,end=' ')
        else:
            print(" ",end=' ')

    print('\n')


# pattern 10..........................................

# 6 5 4 3 2 1 
# 6 5 4 3 2
# 6 5 4 3
# 6 5 4
# 6 5
# 6


for i in range(1,n + 1):
    for j in range(n,0,-1):
        if(j >= i):
            print(j,end = ' ')
        else:
            print(" ",end=' ')
    print("\n")


# pattern 11..........................................

# 6 7 8 9 10 11
# 5 6 7 8 9
# 4 5 6 7
# 3 4 5
# 2 3
# 1

for i in range(1,n+1):
    for j in range(1,n + 1):
        if(j <= ((n + 1)-i)):
            print(n - i + j,end=' ')
        else:
            print(' ', end=' ')
    print("\n")
# pattern 11..........................................

# 6 7 8 9 10 11
# 5 6 7 8 9
# 4 5 6 7
# 3 4 5
# 2 3
# 1

for i in range(1,n+1):
    for j in range(1,n + 1):
        if(j <= ((n + 1)-i)):
            print(n - i + j,end=' ')
        else:
            print(' ', end=' ')
    print("\n")


# pattern 12..........................................

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

value = 1
for i in range(1,n + 1):
    for j in range(1,n + 1):
        if(j <= i):
            print(value,end=' ')
            value += 1
        else:
            print(" ",end=' ')
    print('\n')


# pattern 13..........................................

# A
# B C
# C D E
# D E F G
# E F G H I
# F G H I J K

# first method to print given pattern is as follows ..

for i in range(1,n + 1):
    k = ord("A") 
    if(i >= 2):
        k += i - 1
    for j in range(1,n + 1):
        if(j <= i):
            print(chr(k),end=' ')
            k += 1
        else:
            print(" ",end=' ')
    print("\n")


# second method to print given pattern is as follows ..

for i in range(n):
    k = ord("A") + i
    for j in range(n):
        if(j <= i):
            print(chr(k),end=' ')
            k += 1
        else:
            print(" ",end=' ')
    print("\n")


# pattern 14..........................................

# A
# A B
# A B A
# A B A B
# A B A B A
# A B A B A B


for i in range(0,n):
    for j in range(0,n):
        if(j <= i):
            if(j%2 == 0):   
                print(chr(k), end=' ')
            else:
                print(chr(k + 1), end=' ')
        else:
            print(" ",end=' ')
    print('\n')

# pattern 15..........................................

# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F


for i in range(0,n):
    for j in range(0,n):
        if(j <= i):
            if(j >= 1):
                print(chr(k + j),end=' ')
            else:
                print(chr(k),end=' ')

        else:
            print(" ",end=' ')
    print('\n')

# pattern 16..........................................

# 6 5 4 3 2 1 
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


for i in range(1, n + 1):
    for j in range(n,0,-1):
        if(j >= i):
            if(i > 1):
                print(j - (i - 1),end = " ")
            else:
                print(j ,end = " ")

    print("\n")


