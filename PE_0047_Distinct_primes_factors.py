'''
Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''
from time import perf_counter as time

t = time()
limit = 10**6
sieve = [0]*limit
consecutive = 0
for i in range(2,limit):
    if sieve[i] == 0:
        for j in range(i,limit,i):
            sieve[j] += 1
        consecutive = 0
    elif sieve[i]==4:
        consecutive +=1
        if consecutive == 4:
            print(i-3)
            break
    else: consecutive = 0
# 134043
print(time()-t)
