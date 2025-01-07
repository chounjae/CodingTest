import sys
input = sys.stdin.readline
N = int(input())



for _ in range(N) :
    repeat = int(input())
    cases = [0] * repeat
    dp = [1] * repeat
    for _ in range(repeat) :
        a, b = map(int,input().split())
        cases[a-1] = b
    cnt = 1
    max_ = cases[0]
    for i in range(1, repeat):
        if max_ > cases[i] :
            cnt += 1
            max_ = cases[i]
    print(cnt)