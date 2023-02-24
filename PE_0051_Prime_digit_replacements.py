'''
Prime digit replacements

By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes
among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
'''
from itertools import combinations as comb
from itertools import compress
from collections import Counter
from time import perf_counter as time

def primesTo(n):
  sieve = bytearray([True]) * (n//2+1)
  for i in range(1,int(n**0.5)//2+1):
    if sieve[i]:sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
  return [2,*compress(range(3,n,2), sieve[1:])]

t = time()
primes = primesTo(1000000)
primeset = set(primes)

def find():
    for size in [5,6]:
        # assuming the solution exists in the first 1.000.000 primes
        indexes = range(size)
        pSized = [p for p in primes if 10**(size-1)<=p<10**size]
        # pSized is the list of primes fitting the current size (number of digits)
        for sim in range(2,size):
            # sim for similar digits at index
            for c in comb(indexes,sim):
                # combinations of n (sim) similarities in the primes
                # expressed as indexes. 124522 -> (1,4,5)
                notC = [i for i in indexes if i not in c]
                # with size of 6 and c = (1,4,5) -> (0,2,3)
                candidates = []
                for p in pSized:
                    sp = str(p)
                    if len(set(sp[i]for i in c))==1:
                        candidates.append(''.join([sp[i]for i in notC]))
                        # candidates will all respect the current c comb similarities
                ct = Counter(candidates)
                for k,v in ct.items():
                    if v>7:
                        for n in range(10):
                            sol = (d for d in k)
                            n = str(n)
                            p = int(''.join([n if i in c else next(sol) for i in range(size)]))
                            if p in primeset:
                                print(p)
                                return

find() # 121313
print(time()-t)
