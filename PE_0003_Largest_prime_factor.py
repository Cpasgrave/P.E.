#  Largest prime factor

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def primesTo(n):
	sieve=[1]*(n+1)
	primes = []
	for m in range(2,n+1):
		if sieve[m]:
			primes += [m]
			for j in range(2*m,n+1,m):
				sieve[j] = 0
	return primes

primes = primesTo(1000000)

def largestP(n,large=0):
	i,p = 0,2
	while p<=n**.5:
		if n%p==0: return largestP(n//p)
		i += 1
		p = primes[i]
	return large or n

cases = [
	10, # 5
	17, # 17
	10**12+1
]
for case in cases:
	lp = largestP(case)
	print(lp)