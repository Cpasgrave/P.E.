'''
Coin sums
Problem 31

In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
tot = 0
for i in range(0,201,200):
    if i == 200:
        tot+=1
        continue
    for j in range(0,201-i,100):
        if i+j == 200:
            tot+=1
            continue
        for k in range(0,201-i-j,50):
            if i+j+k == 200:
                tot+=1
                continue
            for l in range(0,201-i-j-k,20):
                if i+j+k+l == 200:
                    tot+=1
                    continue
                for m in range(0,201-i-j-k-l,10):
                    if i+j+k+l+m == 200:
                        tot += 1
                        continue
                    for n in range(0,201-i-j-k-l-m,5):
                        if i+j+k+l+m+n == 200:
                            tot += 1
                            continue
                        for o in range(0,201-i-j-k-l-m-n,2):
                            if i+j+k+l+m+n+o==200:
                                tot += 1
                                continue
                            for p in range(1,201-i-j-k-l-m-n-o):
                                if i+j+k+l+m+n+o+p==200:
                                    tot += 1
                                    continue
print(tot)
