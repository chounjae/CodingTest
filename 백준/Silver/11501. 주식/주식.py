import sys
input = sys.stdin.readline
N = int(input())



for _ in range(N) :
    day = int(input())
    test = list(map(int,input().split()))
    dp = test[-1]
    sell = 0
    for i in range(2,day+1) :
        if dp > test[-i] :
            sell += dp - test[-i]
        else : 
            dp = test[-i]
    print(sell)