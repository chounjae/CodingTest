import sys
input = sys.stdin.readline

onoff = 1
primes = [True] * 250000
for i in range(2,250000) :
    if primes[i] == True :
        for j in range(2 * i,250000,i) :
            primes[j] = False
while 1 :
    N = int(input())
    if N == 0 :
        break
    result = 0

    for i in  range(N+1,2*N+1,1):
        if primes[i] == True :
            result += 1
    print(result)