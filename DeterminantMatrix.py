#finding the determinant of a matrix

#Python code
def det(l):
    n=len(l)
    if (n>2):
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(det(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (l[0][0]*l[1][1]-l[0][1]*l[1][0])

#Assigning a matrix to input 'l'
l = [[2.25,7,1.35,3],[1,9,6,8],[5,8,1,2],[7,3,6.91,9.08]]

#Computing time to run Python code
%timeit det(l)
625 loops, best of 3: 948 µs per loop



#Cython Code
%cython
cpdef float cdet(c):
    cdef int n
    cdef int i
    cdef int t
    cdef float sum
    cdef int t1
    cdef int m
    cdef dict d

    n=len(c)
    if (n>2):
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(c[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(c[0][t])*(cdet(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (c[0][0]*c[1][1]-c[0][1]*c[1][0])

#Assigning same matrix in 'l' to 'c'
c= [[2.25,7,1.35,3],[1,9,6,8],[5,8,1,2],[7,3,6.91,9.08]]

#Computing time to run Cython code
%timeit cdet(c)
625 loops, best of 3: 289 µs per loop

#Cython is over 3 times faster
float(948/289)
3.280276816608996




