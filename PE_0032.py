'''
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way
so be sure to only include it once in your sum.
'''
from itertools import permutations as perm

permut = perm(list('123456789'),9)
s = set()
for p in permut:
    a = int("{}{}".format(*p[:2]))
    b = int("{}{}{}".format(*p[2:5]))
    res = int("{}{}{}{}".format(*p[5:]))
    if a*b==res:
        s.add(res)
    a = int("{}".format(*p[:1]))
    b = int("{}{}{}{}".format(*p[1:5]))
    res = int("{}{}{}{}".format(*p[5:]))
    if a*b==res:
        s.add(res)
s = sum(s)
print(s) # 30424
