ur_input, num = map(int,input().split())
count = 0

for i in range(1, ur_input + 1) :
    if ur_input % i == 0 :
        count += 1
        if count == num :
            print(i)
            break
if count != num :
    print(0)