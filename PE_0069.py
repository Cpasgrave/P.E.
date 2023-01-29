"""
Totient maximum
Problem 69

Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	                1   	2
3	1,2	                2	    1.5
4	1,3	                2     	2
5	1,2,3,4	            4     	1.25
6	1,5	                2     	3
7	1,2,3,4,5,6	        6     	1.1666...
8	1,3,5,7	            4     	2
9	1,2,4,5,7,8	        6     	1.5
10	1,3,7,9	            4    	2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

def phi(n) :
    tot,p = n,1
    while p*p <= n:
        p += 1+(p>2)
        if not n%p:
            while not n%p: n //= p
            tot *= 1-1/p
    if n > 1: tot *= 1-1/n
    return int(tot)

m = (0,0)
# for n in range(1,1000000):
#     m = max(m,(n/phi(n),n))
print(m) # (5.539388020833333, 510510)
print(2*3*5*7*11*13*17)
