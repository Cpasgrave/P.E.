from math import gcd

# code based on Euclid's formula for generating primitive Pythagorean triples:
# a = mn, b = (m²-n²)/2, c = (m²+n²)/2
# where m>n, m and n are both odd, and coprimes

def triples(limit):
  # limit is the max sum of a+b+c, triangle sides
  tri = {}
  for m in range(3,limit//3+1,2):
    for n in range(1,m,2):
      if gcd(m,n)!=1: continue
      x = m*n
      y = (m*m-n*n)/2
      z = (m*m+n*n)/2
      s = x+y+z
      if s>limit: break
      if any(x%1 for x in[y,z,s])or s in tri: continue
      if x*x+y*y==z*z:
        s,y,z = map(int,(s,y,z))
        for k in range(1,limit//s+1):
          tri[k*s] = (k*x,k*y,k*z)
  return sorted(tri.items())

# try:
#   # n = int(input())
#   n = 1500000
#   T = triples(n)
#   for n,t in T[:13]:
#     print(n,'->',t)
#   print('...'.center(15))
#   for n,t in T[-13:]:
#     print(n,'->',t)
# except:
#     print('please input a positive integer')
t = triples(100_000)
print(len(t))
print('ok')
