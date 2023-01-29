'''
Powerful digit sum
Problem 56

A googol (10**100) is a massive number: one followed by one-hundred zeros;
 100**100 is almost unimaginably large: one followed by two-hundred zeros.
 Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100,
what is the maximum digital sum?
'''

s = 0
for a in range(1,100):
    for b in range(1,100):
        n = a**b
        s = max(s,sum(int(d) for d in list(str(n))))
print(s)
