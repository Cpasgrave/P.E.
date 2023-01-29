# Euler 72

"""Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""
from decimal import Decimal as D, getcontext as gc
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

f = 0
lim = 1000000
# for d in range(2,lim+1):
# 	f += phi(d)
# print(f)

f = 303963552391

from functools import lru_cache as lru

@lru(maxsize=10000)
def F(n):
	# based on 
	return n*(n+3)//2-sum([F(n//k) for k in range(2,n+1)])




for n in range(20):
	print(F(n))