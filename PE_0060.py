'''
Prime pair sets
Problem 60

The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109,
both 7109 and 1097 are prime. The sum of these four primes, 792,
represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any
two primes concatenate to produce another prime.
'''
from sympy import sieve
from sympy.ntheory.primetest import isprime as ip

limit = 10000
primes = [*sieve.primerange(0,limit)]
primeset = set([*sieve.primerange(0,1000000)])
print('primes ok')

def isp(n):
    if n<1000000:
        return n in primeset
    else: return ip(n)

for i,p1 in enumerate(primes):
    sp1 = str(p1)

    for j,p2 in enumerate(primes[i+1:]):
        sp2 = str(p2)
        if not isp(int(sp1+sp2)) or not isp(int(sp2+sp1)): continue

        for k,p3 in enumerate(primes[j+1:]):
            sp3 = str(p3)
            if not isp(int(sp2+sp3)) or not isp(int(sp3+sp2)): continue
            if not isp(int(sp1+sp3)) or not isp(int(sp3+sp1)): continue

            for l,p4 in enumerate(primes[k+1:]):
                sp4 = str(p4)
                if not isp(int(sp3+sp4)) or not isp(int(sp4+sp3)): continue
                if not isp(int(sp2+sp4)) or not isp(int(sp4+sp2)): continue
                if not isp(int(sp1+sp4)) or not isp(int(sp4+sp1)): continue
                print(p1,p2,p3,p4)

                for p5 in primes[l:]:
                    sp5 = str(p5)
                    if not isp(int(sp4+sp5)) or not isp(int(sp5+sp4)): continue
                    if not isp(int(sp3+sp5)) or not isp(int(sp5+sp3)): continue
                    if not isp(int(sp2+sp5)) or not isp(int(sp5+sp2)): continue
                    if not isp(int(sp1+sp5)) or not isp(int(sp5+sp1)): continue
                    print(p1,p2,p3,p4,p5)
                    exit()


# 13 5197 5701 6733 8389
# 26033

# Meilleure idée: détecter pour chaque nombre premier en dessous de 10000
# s'il s'assemble avec au moins 4 autres, les stocker sous forme de
# dictionnaire et puis tourner sur les correspondances.
