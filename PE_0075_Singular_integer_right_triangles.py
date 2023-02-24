"""
Singular integer right triangles

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle 
in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, 
and other lengths allow more than one solution to be found; 
for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 
can exactly one integer sided right angle triangle be formed?
"""

"""
a,b,c cotés du triangle rectangle :
m > n
a = m**2 - n**2
b = 2mn
c = m**2 + n**2 (hyp)
P = 2m (m + n)

les triangles pythagoriciens primitifs sont issus de m et n coprimes, avec m ou n impair et l'autre pair.
Il faut donc générer les trianglers primitifs, et leurs multiples, pour remplir une table des périmètres,
qui comportera des vides, des cases avec triangle unique, et des multiples, recouvrement de primitifs avec multiples
ou de plusieurs multiples.
La génération de paires de coprimes dont l'un est pair et l'autre impair se fait à partir de la paire (2,1)
en faisant pousser un arbre ternaire avec les formules : 
(2*m-n,m),(2*m+n,m),(m+2*n,n)
"""
from math import ceil, floor

def Euler75(limit):

	Ps = [0]*(limit+1)
	step = [(2,1)]
	while step:
		next_step = []
		for m,n in step:
			P = 2*m*(m+n)
			if P > limit: continue
			Pm = P
			while P <= limit:
				Ps[P] += 1
				P += Pm
			next_step += [(2*m-n,m),(2*m+n,m),(m+2*n,n)]
		step = next_step[:]
	ct = 0
	for i in range(limit+1):
		if Ps[i] == 1:
			# print(i)
			ct += 1
	return ct


limit=1500000

print(Euler75(limit))

