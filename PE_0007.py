"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def primes_to(n):
	sieve=[1]*(n+1)
	primes = []
	for m in range(2,n+1):
		if sieve[m]:
			primes += [m]
			for j in range(m*m,n+1,m): sieve[j]=0
	return primes

primes = primes_to(1_000_000)
print(primes[10000])