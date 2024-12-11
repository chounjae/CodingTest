yours = int(input())
result = []
dp = [ _ for _ in range(10)]
while len(dp) > 0 :
    num = dp.pop(0)
    result.append(num)
    lastnum = num % 10
    for back in range(lastnum) :
        dp.append(num * 10 + back)

result.sort()
if len(result) < yours :
    print(-1) 
else :
    print(result[yours-1])