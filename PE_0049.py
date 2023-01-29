'''
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three
1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating
the three terms in this sequence?
'''

from itertools import permutations as perm, combinations_with_replacement as combwr, combinations as comb
from collections import Counter
from time import perf_counter as time

t = time()
n = 10000
sieve = [0]+[1]*((n-1)//2)
for i in range(3,int(n**0.5)+1,2):
    for j in range(i**2//2,(n+1)//2,i):
        sieve[j]=0
primes = [2]+[2*i+1 for i,j in enumerate(sieve)if j]

percombs = [sorted(set(filter(lambda x:x in primes,[int(''.join(p)) for p in perm(c,4)])))for c in combwr('123456789',4)]
for pc in percombs:
    if len(pc)<4: continue
    else:
        pairs = [*comb(pc,2)]
        diff = [n2-n1 for n1,n2 in pairs]
        if len(set(diff)) != len(diff):
            for i,m in enumerate(diff):
                for j,n in enumerate(diff[:i]):
                    if m==n and i!=j:
                        p1,p2 = set(pairs[i]),set(pairs[j])
                        if p1&p2:
                            print(''.join(map(str,sorted(p1|p2))))
# 296962999629
print(time()-t)
