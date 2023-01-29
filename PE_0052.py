'''
Permuted multiples
Problem 52
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''
from time import perf_counter as time

t = time()

for size in range(2,7):
    limit = int('1'+'6'*(size-1))
    # number can't have first digit > 2
    # and other digits > 6
for n in range(10**(size-1),limit):
    sn = str(n)
    ssn = set(sn)
    multiples = [1 for m in range(1,7)if set(str(n*m))!=ssn]
    if multiples == []:
        print(n) # 142857
        break

print(time()-t)
# oneliner
t = time()
print(next((n for s in range(2,7)for n in range(10**(s-1),int('1'+'6'*(s-1)))if[1 for m in range(1,7)if set(str(n*m))!=set(str(n))]==[])))
print(time()-t)
