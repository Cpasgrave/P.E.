"""
Square root digital expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

from decimal import *
getcontext().prec = 120
n = 100

def PE80():
	tot = 0
	for n in range(2,101):
		r = str(Decimal(n).sqrt())
		if '.' not in r: continue
		s = sum(int(k) for k in r.replace('.','')[:100])
		if n==2: print(r.split('.')[1][:100],s)
		tot += s
	return tot

print(PE80())