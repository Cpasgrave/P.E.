"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6,9 and . The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.

Constraints:
1 <= T <= 10**5 # number of cases
1 <= N <= 10**9

For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.

Sample Input

10 -> 23
100 -> 2318
"""

import sys

rgsum = lambda n:n*(n+1)//2

def euler001(N):
	n = N-1
	return 3*rgsum(n//3) + 5*rgsum(n//5) - 15*rgsum(n//15)

cases = [10,100,10**9]

for n in cases:
    print(n,euler001(n))
    print()

"""
il faut additionner tous les multiples de 3, et les multiples de 5,
qui sont des multiples de sommes de tous les entiers de 1 à n//3 et n//5 respectivement,
ensuite, on doit soustraire tous les nombres qui ont été comptés deux fois, donc tous les multiples de 15.
"""
