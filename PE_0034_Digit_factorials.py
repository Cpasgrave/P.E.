'''
Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
from functools import reduce

factorial =lambda n:1 if n<2 else n*factorial(n-1)

# 145 40585

print(sum(n if sum(factorial(c) for c in map(int,str(n)))==n else 0 for n in range (3,50000)))
