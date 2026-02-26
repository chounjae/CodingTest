import sys
input = sys.stdin.readline

repeat = int(input())
member = set()
for i in range(repeat):
    member.add(input().strip())

arr = list(member)
sorted_member = sorted(member, key= lambda x: (len(x), x))

for i in sorted_member:
    print(i)