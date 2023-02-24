"""
Totient permutation

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""

from decimal import Decimal as D, getcontext as gc
from collections import Counter as Ct

def phi(n) :
    gc().prec = len(str(n))+3
    tot,p,n = D(n),D(1),D(n)
    while p*p <= n:
        p += 1+(p>2)
        if not n%p:
            while not n%p: 
                n //= p
            tot *= 1-1/p
    if n > 1: tot *= 1-1/n
    return int(tot)

best = (10,0,0)
for n in range(5000000,10000000,2):
    if n%3==0 or n%4==0 or n%5==0 or n%7==0 or n%11==0 or n%13==0 or n%17==0: continue
    p = phi(n)
    if Ct(str(n))==Ct(str(p)):
        ratio = n/p
        new = min((ratio,n,p),best)
        if best!=new:
            best = new
            print(best)

print(best)
(1.0007090511248113, 8319823, 8313928)

# if p prime, phi(p)=p-1
# that would be the smallest q=n/phi(n)
# primes pi can't be permutations of pi-1
# faster solution: look for coprimes

