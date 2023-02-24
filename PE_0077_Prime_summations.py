"""
Prime summations

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

def primes_to(n):
	sieve=[1]*(n+1)
	primes = []
	for m in range(2,n+1):
		if sieve[m]:
			primes += [m]
			for j in range(m*m,n+1,m): sieve[j]=0
	return primes


def count_summations(n):

	primes = primes_to(1000)
	ct = [1]+[0]*n

	for i in range(0, len(primes)):
		p = primes[i]
		for j in range(p, n + 1):
			ct[j] += ct[j-p]

	return ct[-1]

n = 2
while True:
	r = count_summations(n)
	if r>5000:
		print(n,r)
		break
	n += 1
