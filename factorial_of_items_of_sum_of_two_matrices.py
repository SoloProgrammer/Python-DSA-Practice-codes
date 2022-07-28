
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
cols = int(input(("Enter no of colums you want in Matrix A and B : ")))

print("Enter Matrix A :")

A = input_matrix(rows,cols,"A",[])

print(A)

print("Enter Matrix B :")

B = input_matrix(rows,cols,"B",[])

print(B)

sum_of_two_matrix = Sum_Matrix(A,B,[])

print(sum_of_two_matrix)


fact_matrix = []
for i in range(len(sum_of_two_matrix)):
    row = []
    for j in range(len(sum_of_two_matrix[i])):
        fact = 1
        for num in range(1,sum_of_two_matrix[i][j] + 1):
            fact = fact * num
        row.append(fact)
    fact_matrix.append(row)

print(fact_matrix)