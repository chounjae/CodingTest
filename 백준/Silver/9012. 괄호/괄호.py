import sys
input = sys.stdin.readline
n = int(input())
for i in range(n) :
    on = 1
    a = 'YES'
    k = input()
    check = list()
    for j in k :
        if j == '(' :
            check.append(1) 
        elif j == ')' :
            if check :
                check.pop()
            else :
                on = 0
                break
    if on == 0 or check :
        a = 'NO'
    print(a)