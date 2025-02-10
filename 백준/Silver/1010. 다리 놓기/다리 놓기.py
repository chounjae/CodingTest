T = int(input())
for _ in range(T) :
    N, M = map(int,input().split())
    temp = 1
    sum = 1
    for i in range(N) :
        sum *= M-i
        temp *= i+1
    print(sum//temp)