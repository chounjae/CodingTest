from collections import Counter
import sys

num = int(input())
source = list()
for _ in range(num) :
    source.append(input())
tempt = Counter(source)
maxx = dict(sorted(tempt.items(), key=lambda a: (-a[1], a[0]))) 
print(list(maxx.keys())[0])