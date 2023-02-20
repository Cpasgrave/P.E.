
"""
A palindromic number reads the same both ways. The smallest 6 digit palindrome made from 
the product of two 3-digit numbers is 101101 = 143*707.

Find the largest palindrome made from the product of two 3-digit numbers which is less than n.

101101 < n < 1000000
"""

def palcheck(n):
	s = str(n)
	if s[0]!=s[-1]: return 0
	if s[1]!=s[-2]: return 0
	if s[2]!=s[-3]: return 0
	return 1


palindromes = set()
for p in range(100,1000):
	for q in range(100,1000):
		pq = p*q
		if palcheck(pq): palindromes |= {pq}
palindromes = sorted(palindromes)

def palProd(n):

	lo,hi = 0,len(palindromes)-1
	while hi-lo>1:
		mid = (lo+hi)//2
		if palindromes[mid]>n: hi = mid
		else: lo = mid
	return palindromes[lo-1] if palindromes[lo]==n else palindromes[lo]

cases = [
101110, # 101101
800000, # 793397
906609, # 888888
]

for case in cases:
	print(case,palProd(case))