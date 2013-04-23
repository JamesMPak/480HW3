480HW3
======
%cython
cpdef int gcd(int a,int b):
    cdef int t
    cdef int r
    if a<b:
        temp = b
        b = a
        a = temp
    for i in xrange(b):
        t = a/b
        r = a - b*t
        if a % b == 0:
            break
        else:
            a=b
            b=r
    return b
