# somme des primes au dessous de n (inclus)

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# first version:

def summationOfPrimes(n):
	sieve,s=[0]*(n+1),0
	for m in range(2,n+1):
		if sieve[m]==0:
			s+=m
			for j in range(m*m,n+1,m):
				sieve[j]=1
	return s

print(summationOfPrimes(1000000))

# hackerrank version (precalculations for speed):

lim = 10**6+1
sieve = [0,0]+[1]*lim
s = 0
for n in range(2,lim):
	if sieve[n]!=0:
		for j in range(2*n,lim,n): sieve[j]=0
		s += n
		sieve[n] = s

def summationOfPrimes(n):
	return next(sieve[i] for i in range(n,-1,-1) if sieve[i])

s = summationOfPrimes(1000000)
print(s)