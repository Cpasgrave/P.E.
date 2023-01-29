'''
Diophantine equation
Problem 66

Consider quadratic Diophantine equations of the form:

x**2 – Dy**2 = 1

For example, when D=13, the minimal solution in x is 649**2 – 13×180**2 = 1.

It can be assumed that there are no solutions
in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7},
we obtain the following:

3**2 – 2 × 2**2 = 1
2**2 – 3 × 1**2 = 1
9**2 – 5 × 4**2 = 1
5**2 – 6 × 2**2 = 1
8**2 – 7 × 3**2 = 1

Hence, by considering minimal solutions in x for D ≤ 7,
the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x
for which the largest value of x is obtained.
'''
from time import perf_counter as time
from itertools import count

def cf(n):
    a0 = a = int(n**.5)
    b,c,cf = 0,1,[]
    while True:
        b = a*c - b
        c = (n-b*b)/c
        a = int((a0+b)/c)
        cf.append(a)
        if c==1: return [a0,cf]

def cf2f(cf):
    ''' continued fraction to fraction
    n = numerator, d = denominator'''
    n,d = 1,0
    for e in cf[::-1]: n,d = d+n*e,n
    return n,d

def E66(D):
    cfD = cf(D)
    cfgen = (cfD[1][c%len(cfD[1])] for c in count())
    contFrac = [cfD[0]]
    while True:
        n,d = cf2f(contFrac)
        if n*n-D*d*d==1: return [n,D]
        contFrac += [next(cfgen)]

skip = {n*n for n in range(33)}
x = [0,0]
for D in range(1001):
    if D in skip: continue
    x = max(E66(D),x)
print(x[1])





#
