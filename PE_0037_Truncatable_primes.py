'''
Truncatable primes

The number 3797 has an interesting property.
Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7.
Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both
truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from time import perf_counter as time
from math import log10

def primesto(n):
    sieve = [0]+[1]*((n-1)//2)
    for i in range(3,int(n**0.5)+1,2):
        for j in range(i**2//2,(n-1)//2+1,i): sieve[j]=0
    primes = set()
    for i,j in enumerate(sieve):
      if j:
        p = 2*i+1
        primes.add(p)
    return {2}|primes

def TPrimes(primes):
  TP = set()
  pdig = {'1','3','7','9'}
  for p in primes:
    stop = 0
    p1 = p//10
    while p1:
      if p1 in primes:
        p1 //= 10
        continue
      else:
        stop = 1
        break
    if stop: continue
    p2 = p%10**int(log10(p))
    while p2:
      if p2 in primes:
        p2 = p2%10**int(log10(p2))
        continue
      else:
        stop = 1
        break
    if stop: continue
    else:
      if p>10: TP.add(p)
  return sorted(TP)

t = time()
limit = 10**6
primes = primesto(limit)
TP = TPrimes(primes)

print(len(TP))
print(TP)
print(sum(TP))  # 748317
print(time()-t)
