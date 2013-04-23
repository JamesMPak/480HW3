#python code
def function(n):
    a=0
    for i in range(n+1):
        a += i**2
    return a

#Measuring time
%timeit function(10000)
125 loops, best of 3: 5.17 ms per loop


#cython optimized
%cython
cpdef long cfunction(int n):
    cdef long a
    for i in range(n+1):
        a += i**2
    return a

#Measuring time
%timeit cfunction(10000)
625 loops, best of 3: 860 µs per loop


#Cython is 6 times faster than the python code
float(5170/860)
6.011627906976743
