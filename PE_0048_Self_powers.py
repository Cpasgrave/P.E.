'''
Self powers

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

s = 0
for n in range(1,1001):
    s += n**n
print(str(s)[-10:]) # 9110846700
