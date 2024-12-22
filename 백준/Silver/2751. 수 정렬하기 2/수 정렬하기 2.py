import sys
num = int(sys.stdin.readline().rstrip())
re = []
for _ in range(num) :
    re.append(int(sys.stdin.readline().rstrip()))
re.sort()
for i in re :
    print(i)