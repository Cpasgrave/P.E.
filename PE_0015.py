"""
Euler 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

"""
def lattice(n):
    G = [[0]*(n+1)for _ in range(n+1)]
    G[0][0] = 1
    for r in range(n+1):
        for c in range(n+1):
            up = 0
            left = 0
            if r: up = G[r-1][c]
            if c: left = G[r][c-1]
            G[r][c] += up + left
    return G[-1][-1]

for n in range(21):
    print(n,lattice(n))

# math solution:
# RDDRRD, RRDRDD, etc ...
# choosing n elements among 2n:
# binomial law
import math
n = 20
resultat = math.factorial(2*n)//(math.factorial(n)**2)
print(resultat)

# Hackerrank version (grid is M x N)

from math import factorial as f

euler_15 = lambda m,n:f(m+n)//(f(m)*f(n))

# n = int(input())

# for i in range(n):
#     M,N = [*map(int,input().split())]
#     print(euler_15(M,N)%(10**9+7))