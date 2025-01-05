import sys
input = sys.stdin.readline

N = int(input())

cases = list(map(int,input().split()))
result = []
result.append(N)

for i in range(2,N+1) :
    if cases[-i] > 0 :
        cnt = 0
        for j in range(len(result)) :
            if result[j] > N+1-i :
                cnt += 1
            if cnt == cases[-i] :
                result.insert(j+1,N+1-i)
                break
    else :
        result.insert(0,N+1-i)
for i in result :
    print(i,end=' ')