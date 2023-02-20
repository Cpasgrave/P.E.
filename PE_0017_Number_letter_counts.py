'''
Number letter counts


If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

D = {
0:'',
1:'one',
2:'two',
3:'three',
4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine',
10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen',
20:'twenty',
30:'thirty',
40:'forty',
50:'fifty',
60:'sixty',
70:'seventy',
80:'eighty',
90:'ninety',
}

def lettersCount(n):
    m,c,d,u = [*map(int,[*str(n).zfill(4)])]
    text = (m>0)*(D[m]+' thousand '+(n%1000>0)*'and ')+(c>0)*(D[c]+' hundred'+(n%100>0)*'and ')+(D[n%100]if d==1 else D[d*10]+D[u])
    text = text.replace(' ','')
    return len(text)

s = 0
for n in range(1,1001):
    s += lettersCount(n)
print(s)

def write(n):
    *m,c,d,u = [*map(int,[*str(n).zfill(6)])]
    text = (write(n//1000)+' thousand '+(n%1000>0)*'and 'if n//1000 else '')+(c>0)*(D[c]+' hundred '+(n%100>0)*'and ')+(D[n%100]if d==1 else D[d*10]+'-'*(d*u>0)+D[u])
    return text

for n in [2,17,53,348,611,1000,900,1365,22222]:
    print(write(n))
