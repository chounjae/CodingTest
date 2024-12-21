num, N = map(int, input().split())
K = []
for i in range(num) :
    K.append(int(input()))

left = 1
right = max(K)
mid = (right + left) // 2

while right >= left :
    cnt = 0
    for i in K :
        cnt += i // mid
    if cnt < N :
        right = mid - 1
        mid = (right + left) // 2
    elif cnt >= N :
        left = mid + 1
        mid = (right + left) // 2 
print(mid)