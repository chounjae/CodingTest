import sys
input = sys.stdin.readline

n = int(input())   #예제2의 상근이는 누가 놀아주냐..
m = int(input())
rela = list()
friends = set()
frifriends = set()
for _ in range(m) :
    a, b = map(int,input().split())
    rela.append((a,b))
for i, j in rela :
    if i == 1 :
        friends.add(j)
for i, j in rela :
    if i in friends :
        frifriends.add(j)
    elif j in friends :
        frifriends.add(i)
partypeople = friends | frifriends  - {1}
print(len(partypeople))