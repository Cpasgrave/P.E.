"""
Counting fractions in a range

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""

from math import ceil

def fracount(limit):

	avoid = {n:set() for n in range(4,limit+1)}
	ct = 0
	
	for d in range(4,limit+1):
		left = d//3 + 1
		right = ceil(d/2)
		av = avoid[d]
		for n in range(left,right):
			if n in av: continue
			ct += 1
			mul = 2
			dm = d*mul
			while dm <= limit:
				avoid[dm] |= {n*mul}
				mul += 1
				dm = d*mul

	return ct

limit = 120000

print(fracount(limit))
