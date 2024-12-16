import math

# 입력
A, B = map(int, input().split())

# 1. 에라토스테네스의 체로 sqrt(B) 이하의 소수 구하기
limit = int(math.sqrt(B)) + 1
sieve = [True] * (limit + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(math.sqrt(limit)) + 1):
    if sieve[i]:
        for j in range(i * i, limit + 1, i):
            sieve[j] = False
primes = [x for x in range(2, limit + 1) if sieve[x]]

# 2. 거의 소수 구하기
near_primes = set()
for prime in primes:
    power = prime * prime
    while power <= B:
        if power >= A:
            near_primes.add(power)
        if power > B // prime:  # 곱셈 오버플로 방지
            break
        power *= prime

# 3. 결과 출력
print(len(near_primes))
