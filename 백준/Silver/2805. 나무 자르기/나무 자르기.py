import sys
input = sys.stdin.readline
N, M = map(int,input().split())
trees = list(map(int,input().split()))
left = 0
right = max(trees)
result = 0
while left <= right :
    temp = 0
    mid = (left + right) // 2
    for tree in trees :
        if tree > mid :
            temp += tree - mid
    if M <= temp :   
        left = mid + 1
        result = mid
    else :
        right = mid - 1 
        
print(result)