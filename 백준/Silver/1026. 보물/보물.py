num = int(int(input()))
S = [0] * num
A = list(map(int, input().split()))
B = list(map(int, input().split()))
com = A.sort()
pare = B.sort(reverse=True)

for i in range(num) :
    S[i] = A[i] * B[i]

print(sum(S))