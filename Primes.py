#Compute a list of primes up to n

#Python code
def primes(n):
    s=range(0,n+1)
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
            while (bottom<=top):
                    if s[top]:
                            s[top*bottom]=0
                    top-=1
            bottom+=1
            top=n//bottom
    return [x for x in s if x]

#Python Time to compute the first 10000 primes
%timeit primes(104740)
5 loops, best of 3: 321 ms per loop


#Cython code
%cython
cpdef cprimes(int n):
    cdef s
    cdef int bottom
    cdef int top
    cdef int x
    s=range(0,n+1)
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
            while (bottom<=top):
                    if s[top]:
                            s[top*bottom]=0
                    top-=1
            bottom+=1
            top=n//bottom
    return [x for x in s if x]

#Cython time to compute first 10000 primes
%timeit cprimes(104740)
25 loops, best of 3: 23.8 ms per loop


#Cython is almost 13.5 times as fast

float(321/23.8)
13.487394957983193
