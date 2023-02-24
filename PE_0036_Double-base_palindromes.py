'''
Double-base palindromes

The decimal number, 585 = 1001001001 2 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number,
in either base, may not include leading zeros.)
'''
from time import perf_counter as time
from math import log10

limit = 10**6

t = time()

half = 10**(int(log10(limit))//2)
dbp = set()
for n in range(half):
  sn = str(n)
  pals = [int(sn+sn[::-1]),int(sn[:-1]+sn[::-1])]
  for pal in pals:
    b = bin(int(pal))[2:]
    if b[::-1]==b:
      dbp.add(pal)
print(sum(dbp)) # 872187
print(time()-t)
