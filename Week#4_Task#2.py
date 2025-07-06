#In this task we wil perform multiplication of two matrices .
# Condition is number of columns of first matrix=number of rows of 2nd matrix

def Multiplication(matrix1,matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Incompatible matrices: Columns of matrix1 must equal rows of matrix2.")
    
    # Initialize result matrix with zeros
    m = len(matrix1)      # Rows of matrix1
    p = len(matrix2[0])   # Columns of matrix2
    result = [[0 for _ in range(p)] for _ in range(m)]
    
    # Perform multiplication
    for i in range(m):
        for j in range(p):
            for k in range(len(matrix2)):  # Or len(matrix1[0])
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result




matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [1, 0],
    [7, -1]
]
result = Multiplication(matrix1, matrix2)
print("Resultant matrix:")
for row in result:
    print(row)
        