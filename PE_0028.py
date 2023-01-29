'''
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
from numpy import rot90 as R, array as A, vstack as V,fliplr as F

a = 1001

sq=A([[1]])
for i in range((a-1)*2):
    sq = R(sq)
    sq = V([range(sq[0][0]+1,sq[0][0]+1+len(sq[0])),sq])

s = set(sq.diagonal())
s2 = set(F(sq).diagonal())

print(sum(s|s2)) # 669171001
