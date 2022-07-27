
def input_matrix(r,c,matrix,output):
    for i in range(r):
        rows = []
        for j in range(c):
            value = int(input(f"Enter values at position [{i}][{j}] of Matrix {matrix} : "))
            rows.append(value)
        output.append(rows)
    
    return output
            
def Sum_Matrix(A,B,result):
    for i in range(len(A)):
        rows = []
        for j in range(len(A[i])):
            rows.append(A[i][j] + B[i][j])
        result.append(rows)
    return result

rows = int(input(("Enter no of rows you want in Matrix A and B : ")))
cols = int(input(("Enter no of colums rows you want in Matrix A and B : ")))

print("Enter Matrix A :")

A = input_matrix(rows,cols,"A",[])

# output of A be like
# [
    # [2, 1],
    # [2, 1],
    # [2, 1],
    # [1, 2]
# ]

print("Enter Matrix B :")

B = input_matrix(rows,cols,"B",[])

# output of B be like

# [
#     [1, 2],
#     [3, 2],
#     [0, 0],
#     [1, 0]
# ]

print(A)
print(B)

sum_of_two_matrix = Sum_Matrix(A,B,[])

print(sum_of_two_matrix)

# SUM OF MATRIX A AND b BE LIKE

# [
#     [3, 3],
#     [5, 3],
#     [2, 1],
#     [2, 2]
# ]