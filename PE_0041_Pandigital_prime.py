'''
Pandigital prime

We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
from time import perf_counter as time
from itertools import permutations as perm

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    # print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

t = time()
# no permutation of all the 9 digits will produce a prime because
# their repeted sum leads to 9
# same for 8 digits
P = (p for p in perm('7654321',7))

test = 0
for i in range(100):
	p = int(''.join(next(P)))
	test += 1
	if is_prime(p):
		print(p)
		break
print(test)
print(time()-t)
