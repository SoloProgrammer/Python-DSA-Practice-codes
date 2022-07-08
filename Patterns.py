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


