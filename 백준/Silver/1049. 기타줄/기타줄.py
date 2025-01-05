import sys
input = sys.stdin.readline

N, M = map(int,input().split())
bundle = []
unit = []

for _ in range(M) :
    a,b = map(int,input().split())
    bundle.append(a)
    unit.append(b)
small = min(bundle)
smallunit = min(unit)
smallbundle = min(small,6*smallunit)

cut = N // 6 
rest = N % 6 
result = min(cut * smallbundle + rest * smallunit,(cut+1)*smallbundle)
print(result)