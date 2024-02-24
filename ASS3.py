


"""Write a Python program to compute following computation on matrix:
a)Addition of two matrices   
B) Subtraction of two matrices
c) Multiplication of two matrices 
d) Transpose of a matrix"""



import array as arr
print("Enter 1st matrix")
rows= int(input("Input the number of rows: ")) 
cols = int(input("Input the number of columns: "))
arr1 = [[0] * cols for _ in range(rows)]

#taking input for 2d array

for i in range(0, rows):
    for j in range(0, cols):
        arr1[i][j]=int(input(f"Enter the value for index({i},{j})="))
print("First Matrix is :")

#printing array

for i in range(0,rows):
    for j in range(0,cols):
        print(arr1[i][j],end=" ")
    print()

print("Enter 2nd matrix")
rows2 = int(input("Input the number of rows: ")) 
cols2 = int(input("Input the number of columns: "))
arr2 = [[0] * cols for _ in range(rows)]

for i in range(0, rows):
    for j in range(0, cols):
        arr2[i][j]=int(input(f"Enter the value for index({i},{j})="))
        
print("Second Matrix is :")
for i in range(0,rows):
    for j in range(0,cols):
        print(arr2[i][j],end=" ")
    print()

#ADDITION OF MATRIx    
def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("Matrix addition is not possible. Matrices must have the same dimensions.")
        return None

    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)

    return result
addition = add_matrices(arr1, arr2)

if addition:
    print("Addition of Resulting Matrix is:")
    for i in range(0, rows):
        for j in range(0, cols):
            print(addition[i][j], end=" ")
        print()

#subtractionofmatrix
      
def sub_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("Matrix subtraction is not possible. Matrices must have the same dimensions.")
        return None

    sub = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] - matrix_b[i][j])
        sub.append(row)

    return sub
sub = sub_matrices(arr1, arr2)

if sub:
    print("Subtraction of Resulting Matrix is:")
    for i in range(0, rows):
        for j in range(0, cols):
            print(sub[i][j], end=" ")
        print()
        
def multiply_matrices(matrix_a, matrix_b):
    m = len(matrix_a)
    n = len(matrix_a[0])
    p = len(matrix_b)
    q = len(matrix_b[0])

    if n != p:
        print("Matrices cannot be multiplied!")
        return None

    mult = [[0 for _ in range(q)] for _ in range(m)]

    for i in range(m):
        for j in range(q):
            for k in range(p):
                mult[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return mult


mult = multiply_matrices(arr1,arr2)

if mult:
    print("Multiplication Of matrix is :")
    for row in mult:
        print(row)
transpose1 = [[0] * rows for _ in range(cols)] 

for i in range(0,cols):
    for j in range(0,rows):
        transpose1[j][i]=arr1[i][j]
print("Transpose of matrix1:")
for i in range(0,rows):
    for j in range(0, cols):
        print(transpose1[i][j],end=" ")
    print()
    
transpose2 = [[0] * cols for _ in range(rows)]
for i in range(0,cols):
    for j in range(0,rows):
        transpose2[j][i]=arr2[i][j]
print("Transpose of matrix2:")
for i in range(0,rows):
    for j in range(0, cols):
        print(transpose2[i][j],end=" ")
    print()


# In[ ]:




