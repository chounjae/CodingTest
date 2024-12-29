def primelist(start, limit) :
    primes = [True] * (limit+1)
    primes[0] = False
    primes[1] = False
    for i in range(2,limit+1) :
        if primes[i] :
            for j in range(i*i, limit + 1, i) :
                primes[j] = False 
    for i in range(start) :
        primes[i] = False
    return primes


start, limit = map(int,input().split())
result = primelist(start,limit)

for i in range(limit+1) :
    if result[i] :
        print(i)