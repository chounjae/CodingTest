import sys
input = sys.stdin.readline


N = int(input())

towns = list(map(int, input().split()))

limit = int(input())

left = 0
right = max(towns)

while left <= right :
    mid = (left+right)//2
    target = 0
    for i in towns :
        target += min(mid,i)
    if target <= limit : 
        left = mid + 1
        result = mid
    else : 
        right = mid - 1
print(result)