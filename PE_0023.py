'''
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors
 is exactly equal to the number.
 For example, the sum of the proper
 divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of
two abundant numbers is 24.
By mathematical analysis, it can be shown that
all integers greater than 28123 can be written
as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further
by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which
cannot be written as the sum of two abundant numbers.
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

abondant = set()
for n in range(1,28124):
    if sum(sorted(pFac(n,1))[:-1]) > n:
        abondant.add(n)

nas = []
for n in range(1,28124):
    summable = 0
    for ab in abondant:
        if n-ab in abondant:
            summable = 1
            break
        else: continue
    if summable == 0: nas.append(n)

print(sum(nas)) # 4179871
