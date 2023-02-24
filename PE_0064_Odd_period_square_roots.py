'''
Odd period square roots

All square roots are periodic when written as continued fractions and can be written in the form:

... ###### ...

It can be seen that the sequence is repeating. For conciseness,
we use the notation √23 = [4;(1,3,1,8)], to indicate that
the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational)
square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
'''
from decimal import Decimal as D, getcontext as gctxt
from time import perf_counter as time
'''
def contiFrac(n,end):
    r = D(n)**D(.5)
    init = itg = int(r)
    if init==r: return
    res = 0
    loop = []
    while True:
        r -= itg
        r = 1/r
        itg = int(r)
        res += 1
        loop.append(itg)
        if itg==end: break
    return res,loop

gctxt().prec = 600
t = time()
c = 0
end = 2
cur = 2
for n in range(2,10000):
    if cur ==0 :
        end += 2
        cur = end+1
    cur -= 1
    cf = contiFrac(n,end)
    if cf:
        if cf[0]%2: c += 1
        # print(n,cf,end)

print(c)
print(time()-t)
'''

def cfrac(n):
    a0 = a = int(n**.5)
    b,c,ct = 0,1,0
    while True:
        ct += 1
        b = a*c - b
        c = (n-b*b)/c
        if c==1: return ct%2
        a = int((a0+b)/c)

print(sum([cfrac(D)for D in range(2,10001)if D**.5%1!=0]))







#
