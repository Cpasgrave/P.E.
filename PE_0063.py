'''
Powerful digit counts
Problem 63

The 5-digit number, 16807=7**5, is also a fifth power. Similarly,
the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

good = set()
for pow in range(1,1000):
    np = 0
    lnp = 0
    n = 1
    while lnp <= pow:
        np = n**pow
        lnp = len(str(np))
        if lnp==pow: good.add(np)
        n += 1

print(len(good)) # 49
