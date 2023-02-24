'''
Circular primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
from time import perf_counter as time

def primesto(n):
    sieve = [0]+[1]*((n-1)//2)
    for i in range(3,int(n**0.5)+1,2):
        for j in range(i**2//2,(n-1)//2+1,i): sieve[j]=0
    return {2}|{2*i+1 for i,j in enumerate(sieve)if j}

t = time()
n = 10**6
primes = primesto(n)
pdig = {'1','3','7','9'}

cp = 2 # to add 2 and 5
seen = set()
for n in primes:
  if n in seen: continue
  strn = str(n)
  if set(strn)-pdig: continue
  ls = len (strn)
  cycle = {int(strn[i:]+strn[:i])for i in range(ls)}
  if all(c in primes for c in cycle):
    seen.update(cycle)
    cp += len(cycle)

print(time()-t)
print(cp)
