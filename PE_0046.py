'''
Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.
9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2
It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written
as the sum of a prime and twice a square?
'''
from time import perf_counter as time
import numpy
def primesto(n):
# Input n>=6, Returns primes, 2 <= p < n
 sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
 for i in range(1,int(n**0.5)//3+1):
  if sieve[i]:
   k=3*i+1|1
   sieve[k*k//3::k+k] = False
   sieve[k*(k+4-2*(i&1))//3::k+k] = False
 return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

limit = 10**4

t = time()
primes = primesto(limit)
oddComposites = set(range(3,limit+1,2))-set(primes)
# c = p + 2*n**2
conjecture = set()
for p in primes:
    for n in range(1,int(limit**.5/2)+1):
        conjecture.add(p+2*n**2)
print(sorted(oddComposites-conjecture)[0])
print(time()-t)
