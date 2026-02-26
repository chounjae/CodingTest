num = int(input())
result = num
for j in range(num) :
    Str = list(input())
    for i in range(len(Str)) :
        if Str[i] in Str[0:i] :
            if Str[i-1] != Str[i] :
                result -= 1
                break
            
print(result)