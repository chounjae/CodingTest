a, b = map(int, input().split())

noSee = set()
noHear = set()

for i in range(a):
    noSee.add(input())

for j in range(b):
    noHear.add(input())

noBoth = noSee.intersection(noHear)

print(len(noBoth))
for name in sorted(noBoth):
    print(name)