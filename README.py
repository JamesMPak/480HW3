#cython optimized code
%timeit gcd(7660,326)
625 loops, best of 3: 450 ns per loop

#un-optimized code
%timeit gcd(7660,326)
625 loops, best of 3: 4.25 µs per loop


4.25/.450
9.44444444444444
