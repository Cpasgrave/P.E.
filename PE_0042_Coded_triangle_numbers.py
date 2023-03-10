'''
Coded triangle numbers

The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number
corresponding to its alphabetical position
and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number
then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly
two-thousand common English words, how many are triangle words?
'''
from urllib.request import urlopen
from time import perf_counter as time

url = "https://projecteuler.net/project/resources/p042_words.txt"
words = str(urlopen(url).read())[2:-1].replace('"','').split(',')

t = time()
dicval = {}
maxval = 0
orda = ord('A')-1
for w in words:
	val = 0
	for c in w:
		val += ord(c)-orda
	dicval[w] = val
	maxval = max(val,maxval)

triangles = set()
tri = 0
n = 1
while tri < maxval:
	tri = (n+1)*(n/2)
	triangles.add(tri)
	n += 1

c = 0
for w in words:
	if dicval[w] in triangles:
		c += 1

print(c) # 162
print(time()-t)
