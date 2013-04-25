#Computing Matrix Multiplication
#two matrices for benchmark tests
x=[[26,42,18],[9,23,65],[10,3,17]]
y=[[5,1,7],[6,1,3],[19,11,12]]

#Python code
def matrixmult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print "Cannot multiply the two matrices. Incorrect dimensions."
      return
    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    print C
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k]*B[k][j]
    return C

#Python time
%timeit matrixmult(x,y)
625 loops, best of 3: 29.3 µs per loop



#Cython code
#This was the only code I could find that could use cdef or cpdef, the other ones threw errors for reasons unknown to me.
%cython
cpdef cmatrixmult(A, B):
    cdef int rows_A
    cdef int cols_A
    cdef int rows_B
    cdef int cols_B
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
      print "Cannot multiply the two matrices. Incorrect dimensions."
      return
    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    print C
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k]*B[k][j]
    return C

#Cython time
%timeit cmatrixmult(x,y)
625 loops, best of 3: 9.57 µs per loop


#Cython is over 3 times faster
29.3/9.57
3.06165099268548
