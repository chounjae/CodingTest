repeat = int(input())
meetings = []

for _ in range(repeat):
    a, b = map(int, input().split())
    meetings.append((a, b))

meetings.sort(key=lambda x: (x[1], x[0]))

result = 0
last_time = 0

while meetings:
    start, end = meetings.pop(0)
    if start >= last_time:
        result += 1
        last_time = end

print(result)