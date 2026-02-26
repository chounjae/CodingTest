import sys
input = sys.stdin.readline

repeat = int(input())

arr = []
for _ in range(repeat):
    arr.append(input().strip())

ordered_arr = sorted(arr, key= lambda x: (len(x), sum(int(i) for i in x if i.isdigit()), x))

for i in ordered_arr:
    print(i)

# 1.짧은 시리얼부터
# 2.숫자만 더해서 작은 순
# 3.사전순, 숫자~영어로