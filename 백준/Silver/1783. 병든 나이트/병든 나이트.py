import sys
input = sys.stdin.readline

N,M = map(int,input().split())
steps = [(1,2),(2,1),(1,-2),(2,-1)]
if N == 1 :
    print(1)
else :
    if M < 7 :
        if N > 2 :
            result = min(4,M)
        else : 
            result = (M-1)//2+1
    else :
        if N > 2:
            result = (M-6) + 4
        else :
            result = min((M-1)//2+1, 4)
    print(result)