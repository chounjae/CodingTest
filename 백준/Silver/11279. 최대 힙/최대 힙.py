from heapq import heappop ,heappush
import sys 
repeat = int(sys.stdin.readline())
heap = []
for _ in range(repeat) :
    num = int(sys.stdin.readline())
    if num != 0 :
        heappush(heap,-num)
    elif heap :
        print(-heappop(heap))
    else :
        print(0)