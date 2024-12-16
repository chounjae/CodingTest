
n, m = map(int, input().split())
trupeo = set(input().split()[1:])
collect = []
count = 0

for _ in range(m):
    collect.append(set(input().split()[1:]))

for _ in range(m):
    for party in collect:
        if party & trupeo:
            trupeo = trupeo.union(party)

for party in collect:
    if party & trupeo:
        continue
    count += 1

print(count)