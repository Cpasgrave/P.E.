'''
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
from time import perf_counter as time

t = time()

limit = 10**6

sieve = [0]+[1]*((limit-1)//2)
for i in range(3,int(limit**0.5)+1,2):
    for j in range(i**2//2,(limit+1)//2,i):
        sieve[j]=0
primes = [2]+[2*i+1 for i,j in enumerate(sieve)if j]
primeset = set(primes)

lp = len(primes)
upperLim = next(i for i in range(lp)if sum(primes[:i])>limit)-1
seqLen = upperLim
print(upperLim)
found = 0

while found == 0:
    for i in range(upperLim-seqLen+1):
        s = sum(primes[i:i+seqLen])
        if s in primeset:
            found = s
            break
    seqLen -= 1
    upperLim += 1

print(found) # 997651
print(time()-t)
