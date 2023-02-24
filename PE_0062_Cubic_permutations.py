'''
Cubic permutations

The cube, 41063625 (345**3), can be permuted to produce two other cubes:
56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations
of its digits are cube.
'''
from time import perf_counter as time
from collections import defaultdict as dd

t = time()

n = int(10000000**(1/3))
dic = dd(list)
while True:
    cube = n**3
    digits = ''.join(sorted(str(cube)))
    dic[digits].append(cube)
    if len(dic[digits])==5:
        print(min(dic[digits])) # 127035954683
        break
    n +=1

print(time()-t)
