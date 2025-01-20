import sys
input = sys.stdin.readline
from heapq import heappush, heappop

plus = list()
minus = list()
rp = int(input())

for _ in range(rp) :
    num = int(input())
    if num == 0 :
        if plus and minus :
            if plus[0] >= minus[0] :
                print(-heappop(minus))
            else :
                print(heappop(plus))
        elif plus :
            print(heappop(plus))
        elif minus :
            print(-heappop(minus))
        else :
            print(0)
    elif num > 0 :
        heappush(plus,num)
    else :
        heappush(minus,-num)