num = int(input())
scores = [0] * num
count = 0
result = 0
for i in range(num) :
    scores[i] = int(input())
for j in range(1,num) :
    if scores[num-j] <= scores[num-j-1] :
        count = scores[num-j-1] - scores[num-j] + 1
        scores[num-j-1] = scores[num-j-1] - count
        result += count
print(result)