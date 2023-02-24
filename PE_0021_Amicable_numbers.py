'''
Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from collections import defaultdict as dd

def pFac(n,div=0):
    if n<2:
        if div: return {}
        else: return []
    fac = dd(int)
    while n%2==0:
        n //= 2
        fac[2] += 1
    p = 3
    while p <= n:
        if n%p==0:
            n //= p
            fac[p] += 1
        else: p += 2
    pFactors = [(k,v) for k,v in fac.items()]
    if div==0:
        return pFactors
    else:
        divisors = [1]
        for p,pow in pFactors:
            divisors = [d*p**pw for d in divisors for pw in range(pow+1)]
        return divisors


amicables = []


for n in range(1,10000):
    n2 = sum(sorted(pFac(n,1))[:-1])
    if sum(sorted(pFac(n2,1))[:-1])==n:
        if n!=n2:
            print(n,n2)
            amicables.append(n)

print(sum(amicables))
